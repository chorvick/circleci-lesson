from typing import Union

from fastapi import FastAPI

app = FastAPI()
'''fast api not working locally'''


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/users/{user_id}")
def read_user(user_id: int, q: Union[str, None] = None):
    return {"user_id": user_id, "q": q}


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/users/{user_id}")
def read_user(user_id: int, q: Union[str, None] = None):
    return {"user_id": user_id, "q": q}


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/users/{user_id}")
def read_user(user_id: int, q: Union[str, None] = None):
    return {"user_id": user_id, "q": q}
