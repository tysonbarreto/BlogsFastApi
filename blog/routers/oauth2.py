
from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from jose import jwt
from jose.exceptions import JWTError
from blog import schemas
from blog.routers.token import SECRET_KEY, ALGORITHM, verify_token


oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")
def get_current_user(token:str=Depends(oauth2_scheme)):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate":"Bearer"}
    )
    return verify_token(token=token, credentials_exception=credentials_exception)
