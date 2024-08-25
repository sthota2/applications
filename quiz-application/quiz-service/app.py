from flask import Flask, request, jsonify
from models import db, Quiz, Question, Answer
from config import Config

app = Flask(__name__)
app.config.from_object(Config)
db.init_app(app)

@app.route('/quiz', methods=['POST'])
def create_quiz():
   data = request.get_json()
   quiz = Quiz(title=data['title'])
   db.session.add(quiz)
   db.session.commit()
   return jsonify({"message": "Quiz created successfully", "quiz_id": quiz.id}), 201

@app.route('/quiz/<int:quiz_id>/question', methods=['POST'])
def add_question(quiz_id):
   data = request.get_json()
   question = Question(quiz_id=quiz_id, text=data['text'])
   db.session.add(question)
   db.session.commit()
   return jsonify({"message": "Question added successfully", "question_id": question.id}), 201

@app.route('/question/<int:question_id>/answer', methods=['POST'])
def add_answer(question_id):
   data = request.get_json()
   answer = Answer(question_id=question_id, text=data['text'], correct=data['correct'])
   db.session.add(answer)
   db.session.commit()
   return jsonify({"message": "Answer added successfully", "answer_id": answer.id}), 201

if __name__ == '__main__':
   app.run(host='0.0.0.0', port=5002)

