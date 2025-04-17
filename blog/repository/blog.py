from blog import schemas, models, database
from blog.routers.oauth2 import get_current_user
from sqlalchemy.orm import Session
from fastapi import Depends, status, HTTPException
from typing import List

get_db = database.get_db




def create(request:schemas.Blog, db:Session = Depends(get_db)):
    new_blog = models.Blog(title=request.title, body=request.body,user_id=1)
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return new_blog


def get_all(db:Session = Depends(get_db)):
    return db.query(models.Blog).all()


def get(id:int, db:Session = Depends(get_db)):
    query = db.query(models.Blog).filter(models.Blog.id==id).first()

    if not query:
        #response.status_code=status.HTTP_404_NOT_FOUND
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Blog with id {id} is not does not exist!")
    #return {'detail':f"Blog with id {id} is not does not exist!"}
    else:
        return query
    


def delete(id:int, db:Session=Depends(get_db)):
    blog=db.query(models.Blog).filter(models.Blog.id==id)
    if not blog.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Blog with id {id} not found!")
    else:
        blog.delete(synchronize_session=False)
        db.commit()
        return {'detail':f'Blog with id {id} has been deleted!'}


def update(id:int, request:schemas.Blog, db:Session=Depends(get_db)):
    blog = db.query(models.Blog).filter(models.Blog.id==id)
    if not blog.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Blog with id {id} not found!")
    else:
        blog.update(values={'title':request.title, 'body':request.body}, synchronize_session=False)
        db.commit()
        return {'detail':f'Blog with id {id} has been updated!'}
    

if __name__=='__main__':
    __all__=["create","get_all","get","delete","update"]