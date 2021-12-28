from app import app
from flask import render_template

@app.route("/bio")
def bio():
    return render_template('class_x/bio/bio_home.html')

@app.route("/bio/bio_art_1")
def bio_art_1():
    return render_template('class_x/bio/bio_art_1.html')
