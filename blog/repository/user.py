from blog import schemas, models, database
from blog.routers.oauth2 import get_current_user
from sqlalchemy.orm import Session
from fastapi import Depends, status, HTTPException
from typing import List
from blog.routers.hashing import hash

get_db = database.get_db



def create(request:schemas.User, db:Session=Depends(get_db)):
    new_user=models.User(name=request.name, email=request.email, password= hash(request.password))
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user#{'detail':f'New user {request.name} created!'}




def get_all(db:Session=Depends(get_db)):
    return db.query(models.User).all()


def get(id:int, db:Session = Depends(get_db)):
    query = db.query(models.User).filter(models.User.id==id).first()

    if not query:
        #response.status_code=status.HTTP_404_NOT_FOUND
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"User with id {id} is not does not exist!")
    #return {'detail':f"Blog with id {id} is not does not exist!"}
    else:
        return query