import  sqlalchemy
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.sql import func

Base=declarative_base()


class User (Base):
    __tablename__='users'
    id =sqlalchemy.Column(sqlalchemy.INTEGER,primary_key=True,index=True,unique=True)
    username=sqlalchemy.Column(sqlalchemy.String,unique=True)
    email=sqlalchemy.Column(sqlalchemy.String,unique=True)
    password=sqlalchemy.Column(sqlalchemy.String)
    date_registered= sqlalchemy.Column(sqlalchemy.DateTime(timezone=True), default=func.now())
users=User.__tablename__

class Test(Base):
    __tablename__='test'
    id =sqlalchemy.Column(sqlalchemy.INTEGER,primary_key=True,index=True,unique=True)

    test=sqlalchemy.Column(sqlalchemy.String)

