from fastapi import FastAPI, Depends, HTTPException, status, Response
from blog.schemas import Blog
from blog import schemas, models, database
from sqlalchemy.orm import Session

from typing import List
from passlib.context import CryptContext
import bcrypt

from blog.routers import blog, user, authentication



app = FastAPI()

models.Base.metadata.create_all(database.engine)

app.include_router(authentication.router)
app.include_router(blog.router)
app.include_router(user.router)



    

    
