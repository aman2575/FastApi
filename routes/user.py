from fastapi import APIRouter
from config.db import conn
from models.index import users
from schemas.index import User

user = APIRouter()
@user.get("/")
async def read_data(id: int):
    return conn.execute(users.select().where(users.c.id == id)).fetchall()


@user.get("/{id}")
async def read_data(id: int):
    return conn.execute(users.select().where(users.c.id == id)).fetchall()


@user.post("/")
async def write_data(user: User):
    conn.execute(users.insert().values(
        name = user.name,
        image_url = user.imageurl,
        description = user.description
    ))
    return conn.execute(users.select()).fetchall()


@user.put("/{id}")
async def update_data(id:int, user:User):
    conn.execute(users.update(
        name = user.name,
        image_url = user.imageurl,
        description = user.description   
    ).where(users.c.id == id))
    return conn.execute(users.select()).fetchall()


@user.delete("/")
async def read_data():
    conn.execute(users.delete().where(users.c.id == id))
    return conn.execute(users.select()).fetchall()