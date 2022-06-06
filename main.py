import uvicorn
import uuid
import io
from utils import client
from fastapi import UploadFile, FastAPI, File
from typing import List

app = FastAPI()


@app.post("/flames/")
async def upload(files: List[UploadFile] = File(...)):
    all_files = {}
    if len(files) > 15:
        return {"message": "need <= 15"}
    for file in files:
        try:
            value_as_bytes = file.file.read()
            contents = io.BytesIO(value_as_bytes)
            file_name = str(uuid.uuid4())
            client.put_object('mybucket1', F'{file_name}.jpeg', contents, len(value_as_bytes))
            all_files.update({files.index(file): file_name})
        except Exception as e:
            print(e)
            return {"message": "There was an error uploading"}

    return all_files


# @app.get("/")


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=6000)
