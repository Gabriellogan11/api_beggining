from fastapi import FastAPI
from fastapi.responses import JSONResponse
import uuid

from starlette import status

app = FastAPI(
    title="API's en clase de MLops",
    version="0.0.1"
)

@app.post("/api/v1/users/")
async def create_user(username: str, name: str):
    return {
        "username": username,
        "name": name,
        "ID": str(uuid.uuid4()),
        "message": "The user has been created successfully",
        "status_Code": 201
    }


@app.get("/api/v1/{user_id}")
async def get_user(user_id: str):
    users = {
       "hola14662": {
           "username": "gato",
           "name": "gabo"
       },
        "ide-67": {
        "username": "perro",
        "name": "pam"
        }
    }
    if user_id in users:
        user = users[user_id]
        return JSONResponse(
            content=user,
            status_code= status.HTTP_200_OK
    )

    else:
        return JSONResponse(
            content="no existe el usuario",
            status_code=status.HTTP_400_BAD_REQUEST
        )