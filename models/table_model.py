from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import String, Column, DateTime, Integer, create_engine
from datetime import datetime

Base = declarative_base()


class Items(Base):
    __tablename__ = 'inbox'
    id = Column(Integer(), primary_key=True, index=True)
    code = Column(Integer(), nullable=False)
    name = Column(String(200), nullable=False)
    created_on = Column(DateTime(), default=datetime.now)
