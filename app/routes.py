from app import app
from flask import render_template, send_file

@app.route("/")
def home_page():
    return render_template('home.html')

@app.route("/subjects")
def subjects():
    return render_template('subjects.html')

@app.route("/about")
def about():
    return render_template('about.html')

@app.route("/math")
def math():
    return render_template('math.html')

@app.route("/physics")
def physics():
    return render_template('physics.html')

@app.route("/chem")
def chem():
    return render_template('chem.html')

@app.route("/bio")
def bio():
    return render_template('bio.html')

@app.route("/bio_art_1")
def bio_art_1():
    return render_template('bio_art_1.html')

@app.route("/download_file")
def download_file():
    path = r"E:\Xtra 2\Xtra\Dev\Git\TutionWebsite1\output\test1.txt"
    return send_file(path, as_attachment=True)
