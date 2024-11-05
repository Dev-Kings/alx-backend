#!/usr/bin/env python3
"""
Module containing index method.
"""
from flask import Flask, render_template


app = Flask(__name__)


@app.route('/')
def index():
    """Render welcome page."""
    return render_template('index.html')


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
