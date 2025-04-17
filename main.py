from fastapi import FastAPI
from pydantic import BaseModel, Field
from typing import Optional

app = FastAPI()

@app.get('/')
def index():
    return {'data':{'name':'John'}}

@app.get('/about')
def about():
    return {'data':'about page'}

@app.get('/blog/unpublished')
def unpublished():
    return {'data':'hey'}

@app.get('/blog/{id}')
def show(id:int):
    return {'data':id}



@app.get('blog/{id}/comments')
def comments(id):
    return {'data':{'comments':{"hey":id}}}

class Blog(BaseModel):
    title:str
    body:str
    published_at:Optional[bool]



@app.post('blog')
def create_blog(blog:Blog):
    return {'data':f'blog is created {blog.title}'}

