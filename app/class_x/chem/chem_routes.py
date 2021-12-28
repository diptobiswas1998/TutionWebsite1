from app import app
from flask import render_template

@app.route("/x/chem/chem_home")
def chem():
    return render_template('class_x/chem/chem_home.html')
