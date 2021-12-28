from app import app
from flask import render_template

@app.route("/subjects_x")
def subjects_x():
    return render_template('class_x/subjects_x.html')