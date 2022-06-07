from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import String, Column, DateTime, Integer, create_engine
from datetime import datetime
from sqlalchemy.orm import Session

engine = create_engine("postgresql://admin:01233210aA@192.168.0.204:5432/inbox")

Base = declarative_base()
session = Session(bind=engine)


class Items(Base):
    __tablename__ = 'inbox'
    id = Column(Integer(), primary_key=True, index=True)
    name = Column(String(200), nullable=False)
    created_on = Column(DateTime(), default=datetime.now)


Base.metadata.create_all(engine)
