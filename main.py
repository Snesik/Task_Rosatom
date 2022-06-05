import uvicorn
import boto3
from botocore.client import Config
from fastapi import UploadFile, FastAPI

app = FastAPI()


@app.post("/flames/")
async def upload(files: list[UploadFile]):
    for file in files:
        try:
            contents = await file.read()
            with open('images/' + file.filename, 'wb') as f:
                f.write(contents)
        except:
            return {"message": "There was an error uploading"}
        finally:
            await file.close()
    return {"message": f"Successfuly uploaded {[file.filename for file in files]}"}


# @app.get("/")


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=9000)


