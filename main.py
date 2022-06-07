import uvicorn
import uuid
import io
from typing import List
from fastapi import UploadFile, FastAPI, File

from models.table_model import session, Items
from utils import client, creat_bucket

app = FastAPI()


@app.post("/flames/")
async def upload(files: List[UploadFile] = File(...)):
    all_files = []
    bucket = creat_bucket()
    if len(files) > 15:
        return {"message": "need <= 15"}
    for file in files:
        try:
            value_as_bytes = file.file.read()
            contents = io.BytesIO(value_as_bytes)
            file_name = str(uuid.uuid4())
            client.put_object(bucket, F'{file_name}.jpeg', contents, len(value_as_bytes))
            all_files.append(Items(name=file_name))
        except Exception:
            return {"message": "There was an error uploading"}
    for one_file in all_files:
        session.add(one_file)
        session.flush()
        session.commit()

    return {i.id: i.name for i in all_files}


@app.get("/flames/{number}/")
async def get(number: int):
    result = session.query(Items.name, Items.created_on).filter(Items.id == number).one()
    return {result[1], result[0]}


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=6000)
