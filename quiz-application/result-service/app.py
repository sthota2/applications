from flask import Flask, request, jsonify
from models import db, Result
from config import Config

app = Flask(__name__)
app.config.from_object(Config)
db.init_app(app)

@app.route('/result', methods=['POST'])
def save_result():
   data = request.get_json()
   result = Result(user_id=data['user_id'], quiz_id=data['quiz_id'], score=data['score'])
   db.session.add(result)
   db.session.commit()
   return jsonify({"message": "Result saved successfully", "result_id": result.id}), 201

@app.route('/result/<int:user_id>', methods=['GET'])
def get_results(user_id):
   results = Result.query.filter_by(user_id=user_id).all()
   return jsonify([{'quiz_id': r.quiz_id, 'score': r.score} for r in results]), 200

if __name__ == '__main__':
   app.run(host='0.0.0.0', port=5003)

