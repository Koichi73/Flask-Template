from flask_app.app import app
from flask_app import db

with app.app_context():
    db.create_all()