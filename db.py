import sqlalchemy.orm
from sqlalchemy import databases
from sqlalchemy import create_engine
from models.models import Base

SQLALCHEMY_DATABASE_URL='postgresql://postgres:1@localhost/testmedu4'

engine = create_engine(SQLALCHEMY_DATABASE_URL)
Session = sqlalchemy.orm.sessionmaker(bind=engine)
session = Session()
Base.metadata.create_all(engine)
database = databases.postgresql