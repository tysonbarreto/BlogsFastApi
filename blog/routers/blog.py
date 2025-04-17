from fastapi import FastAPI, Depends, HTTPException, status, Response, APIRouter
from blog.schemas import Blog
from blog import schemas, models, database
from blog.routers.oauth2 import get_current_user
from sqlalchemy.orm import Session
from blog.repository import blog, user

from typing import List


router = APIRouter(
    prefix='/blog',
    tags=['Blogs']
)

get_db = database.get_db

models.Base.metadata.create_all(database.engine)


@router.post('/', status_code=status.HTTP_201_CREATED)
def create(request:schemas.Blog, db:Session = Depends(get_db), get_current_user:schemas.User=Depends(get_current_user)):
    return blog.create(request, db)


@router.get('/', status_code=200, response_model=List[schemas.ShowBlog])
def get_all(db:Session = Depends(get_db), get_current_user:schemas.User=Depends(get_current_user)):
    return blog.get_all(db)

@router.get('/{id}', status_code=status.HTTP_200_OK, response_model=schemas.ShowBlog)
def get(id, db:Session = Depends(get_db)):
    return blog.get(id,db)
    

@router.delete('/{id}', status_code=status.HTTP_204_NO_CONTENT)
def delete(id, db:Session=Depends(get_db), get_current_user:schemas.User=Depends(get_current_user)):
    return blog.delete(id,db)

@router.put('/{id}', status_code=status.HTTP_202_ACCEPTED)
def update(id, request:schemas.Blog, db:Session=Depends(get_db), get_current_user:schemas.User=Depends(get_current_user)):
    return blog.update(id,request,db)