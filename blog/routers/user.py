from fastapi import FastAPI, Depends, HTTPException, status, Response, APIRouter
from blog.schemas import Blog
from blog import schemas, models, database
from blog.repository import user
from blog.routers.oauth2 import get_current_user
from sqlalchemy.orm import Session

from typing import List




get_db = database.get_db

router = APIRouter(
    prefix='/user',
    tags=['Users']
)

@router.post('/',response_model=schemas.ShowUser)
def create(request:schemas.User, db:Session=Depends(get_db), get_current_user:schemas.User=Depends(get_current_user)):
    return user.create(request, db)



@router.get('/',response_model=List[schemas.ShowUser])
def get_all(db:Session=Depends(get_db), get_current_user:schemas.User=Depends(get_current_user)):
    return db.query(models.User).all()

@router.get('/{id}', status_code=status.HTTP_200_OK, response_model=schemas.ShowUser)
def get_user(id, db:Session = Depends(get_db), get_current_user:schemas.User=Depends(get_current_user)):
    return user.get_all(id, db)



