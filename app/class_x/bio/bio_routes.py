from app import app
from flask import render_template

@app.route("/x/bio/bio_home")
def bio():
    return render_template('class_x/bio/bio_home.html')

@app.route("/x/bio/bio_art_1")
def bio_art_1():
    return render_template('class_x/bio/bio_art_1.html')
