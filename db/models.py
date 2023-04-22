from sqlalchemy import create_engine, Column, Integer, String, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

class Question(Base):
    __tablename__ = 'questions'
    id = Column(Integer, primary_key=True)
    answer_1 = Column(String)
    answer_2 = Column(String)
    answer_3 = Column(String)
    answer_4 = Column(String)
    correct_answer = Column(String)
    user_answer = Column(String)

    def __init__(self, question_dto):
        self.answer_1 = question_dto.answer_1
        self.answer_2 = question_dto.answer_2
        self.answer_3 = question_dto.answer_3
        self.answer_4 = question_dto.answer_4
        self.correct_answer = question_dto.correct_answer
        self.user_answer = question_dto.user_answer

engine = create_engine('sqlite:///melowise.db')

# Create the session
Session = sessionmaker(bind=engine)
session = Session()
