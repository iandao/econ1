from app import db, app
from flask import render_template


@app.route('/')
@app.route('/home')
def index():
    return render_template("home.html", title='Home')
