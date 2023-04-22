from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from sqlalchemy.orm import sessionmaker
from db.models import Answer, Base
from sqlalchemy import create_engine
from .models import Answer

# Create the session

class DatabaseHandler:
    def __init__(self):
        self.engine = create_engine(f'sqlite:///melowise.db')
        Base.metadata.create_all(self.engine)
        self.session = Session(self.engine)
        self.Session = sessionmaker(bind=self.engine)

    def save_answer(self, question_id, answer):
        answer_model = Answer(question_id=question_id, answer=answer)
        self.session.add(answer_model)
        self.session.commit()
        self.close()
    
    def get_all_answers(self):
        session = self.Session()
        try:
            answers = session.query(Answer).all()
        finally:
            session.close()
        return answers

    def get_answers_from_db(self):
        print('aaaaaaaaaa')
        Session = sessionmaker()
        session = Session.configure(bind=self.engine)
        answers = session.query(Answer).all()
        session.close()
        print('bbbbbbb')
        return answers

    def close(self):
        self.session.close()
