import sqlalchemy.orm
from sqlalchemy import databases
from sqlalchemy import create_engine
from models.models import Base
import os

SQLALCHEMY_DATABASE_URL=os.environ.get('SQLALCHEMY_DATABASE_URL')

engine = create_engine(SQLALCHEMY_DATABASE_URL)
Session = sqlalchemy.orm.sessionmaker(bind=engine)
session = Session()
Base.metadata.create_all(engine)
database = databases.postgresql