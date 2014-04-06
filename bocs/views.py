from flask import render_template, url_for, redirect
from bocs import app
import random

def random_num():
  return random.randint(1, 100)


@app.route('/')
def index():
    return render_template('index.html', first=random_num(), second=random_num())
