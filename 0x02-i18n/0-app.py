#!/usr/bin/env python3
"""
Module containing single route that renders an HTML page.
"""

from flask import Flask, render_template


app = Flask(__name__)


@app.route('/')
def index() -> str:
    """
    Renders welcome page.

    Returns:
        str: HTML content of the welcome page.
    """
    return render_template('0-index.html')


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
