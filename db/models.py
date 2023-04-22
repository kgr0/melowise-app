from sqlalchemy import create_engine, Column, Integer, String, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

class Answer(Base):
    __tablename__ = 'answers'
    id = Column(Integer, primary_key=True)
    question_id = Column(Integer)
    answer = Column(Boolean)

    def __init__(self, question_id, answer):
        self.question_id = question_id
        self.answer = answer

engine = create_engine('sqlite:///melowise.db')

# Create the session
Session = sessionmaker(bind=engine)
session = Session()
