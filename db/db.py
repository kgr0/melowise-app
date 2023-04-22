from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from sqlalchemy.orm import sessionmaker
from db.models import Question, Base
from sqlalchemy import create_engine
from .models import Question

# Create the session

class DatabaseHandler:
    def __init__(self):
        self.engine = create_engine(f'sqlite:///melowise.db')
        Base.metadata.create_all(self.engine)
        self.session = Session(self.engine)
        self.Session = sessionmaker(bind=self.engine)

    def save_question(self, question_dto):
        question_model = Question(question_dto=question_dto)
        self.session.add(question_model)
        self.session.commit()
        self.close()
    
    def get_all_questions(self):
        session = self.Session()
        try:
            questions = session.query(Question).all()
        finally:
            session.close()
        return questions

    def close(self):
        self.session.close()
