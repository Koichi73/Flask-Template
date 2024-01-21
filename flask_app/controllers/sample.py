from flask import Blueprint, render_template, request, redirect
from flask_app import db
from flask_app.models import Test

sample_bp = Blueprint('sample', __name__, url_prefix='/sample')


@sample_bp.route("/", methods=["GET", "POST"])
def index():
    hoge_lists = db.session.query(Test).all()

    return render_template("sample.html", hoge_lists=hoge_lists)