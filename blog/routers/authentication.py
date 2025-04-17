from fastapi import APIRouter, status, Depends, HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from blog import schemas, database, models
from sqlalchemy.orm import Session

from blog.routers import hashing

from datetime import datetime, timedelta, timezone
from blog.routers.token import create_access_token, ACCESS_TOKEN_EXPIRE_MINUTES

get_db = database.get_db

router = APIRouter(
    prefix='/login',
    tags=['Login']
)

@router.post('/', status_code=status.HTTP_202_ACCEPTED)
def login(request:OAuth2PasswordRequestForm=Depends(), db:Session = Depends(get_db)):
    user = db.query(models.User).filter(request.username==models.User.email).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail= "Invalid username")
    
    #verify the password

    if not hashing.verify(secret=request.password,hash=user.password):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail= "Invalid password")
    
    #generate JWT token

    access_token = create_access_token(data={"sub": user.email})

    return {"access_token":access_token, "token_type":'bearer'}