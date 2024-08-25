from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Result(db.Model):
   id = db.Column(db.Integer, primary_key=True)
   user_id = db.Column(db.Integer, nullable=False)
   quiz_id = db.Column(db.Integer, nullable=False)
   score = db.Column(db.Integer, nullable=False)

