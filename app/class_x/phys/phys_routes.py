from app import app
from flask import render_template

@app.route("/phys")
def phys():
    return render_template('class_x/phys/physics_home.html')
