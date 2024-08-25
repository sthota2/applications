from flask import Flask, request, jsonify
from models import db, User
from config import Config

app = Flask(__name__)
app.config.from_object(Config)
db.init_app(app)

@app.route('/register', methods=['POST'])
def register():
   data = request.get_json()
   user = User(username=data['username'])
   user.set_password(data['password'])
   db.session.add(user)
   db.session.commit()
   return jsonify({"message": "User registered successfully"}), 201

@app.route('/login', methods=['POST'])
def login():
   data = request.get_json()
   user = User.query.filter_by(username=data['username']).first()
   if user and user.check_password(data['password']):
       return jsonify({"message": "Login successful"}), 200
   return jsonify({"message": "Invalid credentials"}), 401

if __name__ == '__main__':
   app.run(host='0.0.0.0', port=5001)

