from flask import render_template, url_for, redirect
from bocs import app

@app.route('/')
def index():
    return "Hello World!"
