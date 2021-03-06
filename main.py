from fastapi import FastAPI,status,HTTPException
from db import session
from models import models
import bcrypt

from shemas import User
app = FastAPI()



@app.get("/api/v1/")
async def fetch_users():


    return  session.query(models.User).all()

@app.post('/add_user/',response_model=User,status_code=status.HTTP_201_CREATED)
async def add_user(user:User):
    user_temp=  models.User(username=user.username, email=user.email,password=bcrypt.hashpw(user.password.encode('utf-8'), bcrypt.gensalt()))
    session.add(user_temp)
    session.commit()
    return user

@app.put('/api/v1/user/{id}/')
async def user_put(user:User,id:int):
    user_get=  session.query(models.User).filter(models.User.id==id).first()
    if user_get is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="User Not Found")
    user_get.username=  user.username
    user_get.email=  user.email
    user_get.password=  bcrypt.hashpw(user.password.encode('utf-8'), bcrypt.gensalt())
    session.commit()
    return user_get

@app.patch("/api/v1/user/{id}/", response_model=User)
async def update_item(user: User,id: str,) :
    user_get=  session.query(models.User).filter(models.User.id==id).first()
    if user_get is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="User Not Found")
    user_d=user.dict(exclude_none=True)
    for key, value in user_d.items():
        user_get[key]=value
    session.commit()
    return user_get

@app.delete('/api/v1/user/{id}/')
async def user_delete(id:int):
    user_get=  session.query(models.User).filter(models.User.id==id).first()
    if user_get is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="User Not Found")
    session.delete(user_get)
    session.commit()
    return user_get

@app.get('/api/v1/user/{id}/')
async def user_get_id(id:int):
    user_get=  session.query(models.User).filter(models.User.id==id).first()
    if user_get is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="User Not Found")
    return user_get
