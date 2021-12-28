from app import app
from flask import render_template

@app.route("/subjects_ix")
def subjects_ix():
    return render_template('class_ix/subjects_ix.html')