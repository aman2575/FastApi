from pydantic import BaseModel


class User(BaseModel):
    id:int
    name:str
    image_url:str
    description:str