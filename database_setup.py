#!/user/bin/python
# Author: Scott Iwako
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine

Base = declarative_base()

class Project(Base):
    __tablename__ = 'project'
    id = Column(Integer, primary_key=True)
    project_name = Column(String(250), nullable=False)
    image = Column(String(250), nullable=False)

class Education(Base):
    __tablename__ = 'education'
    id = Column(Integer, primary_key=True)
    school_name = Column(String(250), nullable=False)
    degree_achieved = Column(String(250), nullable=False)
    year = Column(Integer, nullable=True)

engine = create_engine('sqlite:///main.db')
Base.metadata.create_all(engine)
