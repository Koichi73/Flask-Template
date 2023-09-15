from flask_app import db


#TestDB
class Test(db.Model):
    __tablename__ = "test"
    id = db.Column(db.Integer, primary_key=True)
    hoge = db.Column(db.String(255))


#UserDB
class User(db.Model):
    __tablename__ = "user"
    id = db.Column(db.Integer, primary_key=True)
    user_name = db.Column(db.String(255), unique=True)
    password = db.Column(db.String(12))