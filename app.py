import os
from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
#app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('database')
#app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL','mysql://root:example@db:3306/myflaskapp?charset=utf8mb4')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True)
    password = db.Column(db.String(50))

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/adduser', methods=['POST'])
def add_user():
    username = request.form['username']
    password = request.form['password']
    
    user = User(username=username, password=password)
    db.session.add(user)
    db.session.commit()
    
    return render_template('success.html', username=username)

@app.route('/users')
def users():
    users = User.query.all()
    
    return render_template('users.html', users=users)

with app.app_context():
    db.create_all()

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')

