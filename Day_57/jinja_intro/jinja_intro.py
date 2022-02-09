import datetime

from flask import Flask, render_template
from datetime import time
import requests

app = Flask(__name__)

present_year = datetime.datetime.now().year


@app.route("/")
def home():
    return render_template("index.html", year=present_year)


@app.route("/guess/<name>")
def get_info(name):
    gender_url = f'https://api.genderize.io?name={name}'
    gender_response = requests.get(gender_url)
    gender_data = gender_response.json()
    gender = gender_data['gender']
    age_url = f'https://api.agify.io?name={name}'
    age_response = requests.get(age_url)
    age_data = age_response.json()
    age = age_data['age']
    return render_template('guess.html', person_name=name, person_age=age, person_gender=gender)


@app.route("/blog")
def get_blog():
    blog_url = "https://api.npoint.io/968fed6e845c137dddd9"
    blog_response = requests.get(blog_url)
    all_posts = blog_response.json()
    return render_template("blog.html", posts=all_posts)


if __name__ == '__main__':
    app.run()
