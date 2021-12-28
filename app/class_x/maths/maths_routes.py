from app import app
from flask import render_template

@app.route("/x/maths/maths_home")
def math():
    return render_template('class_x/maths/maths_home.html')

