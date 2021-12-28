from app import app
from flask import render_template, send_file

@app.route("/")
def home_page():
    return render_template('home.html')

@app.route("/classes")
def classes():
    return render_template('classes.html')

@app.route("/about")
def about():
    return render_template('about.html')

@app.route("/download_file")
def download_file():
    path = r"E:\Xtra 2\Xtra\Dev\Git\TutionWebsite1\output\test1.txt"
    return send_file(path, as_attachment=True)
