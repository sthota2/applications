from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Quiz(db.Model):
   id = db.Column(db.Integer, primary_key=True)
   title = db.Column(db.String(150), nullable=False)
   questions = db.relationship('Question', backref='quiz', lazy=True)

class Question(db.Model):
   id = db.Column(db.Integer, primary_key=True)
   quiz_id = db.Column(db.Integer, db.ForeignKey('quiz.id'), nullable=False)
   text = db.Column(db.String(255), nullable=False)
   answers = db.relationship('Answer', backref='question', lazy=True)

class Answer(db.Model):
   id = db.Column(db.Integer, primary_key=True)
   question_id = db.Column(db.Integer, db.ForeignKey('question.id'), nullable=False)
   text = db.Column(db.String(255), nullable=False)
   correct = db.Column(db.Boolean, nullable=False)

