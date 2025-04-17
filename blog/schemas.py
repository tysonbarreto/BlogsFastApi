from pydantic import BaseModel, Field
from typing import List

class Blog(BaseModel):
    title:str
    body:str
    class Config:
        from_attributes=True

class User(BaseModel):
    name:str
    email:str
    password:str

class ShowUser(BaseModel):
    name:str
    email:str
    blogs:List[Blog]=[]
    class Config:
        from_attributes=True

class ShowBlog(BaseModel):
    title:str
    body:str
    creator: ShowUser
    class Config:
        from_attributes=True

class Login(BaseModel):
    username:str
    password:str
    class Config:
        from_attributes=True

class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    username: str | None = None
    scopes: list[str] = []

if __name__=='__main__':
    __all__=['Blog','ShowBlog','User','ShowUser']