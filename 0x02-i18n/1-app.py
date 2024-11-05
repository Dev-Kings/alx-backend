#!/usr/bin/env python3
"""
Module containing Flask app with Babel setup for internationalization.
The app has a single route that renders an HTML page.
"""

from flask import Flask, render_template
from flask_babel import Babel


class Config:
    """
    Config class for Babel and Flask app settings.

    Args:
        LANGUAGES (list): Languages for translation.
        BABEL_DEFAULT_LOCALE (str): Default locale for translations.
        BABEL_DEFAULT_TIMEZONE (str): Default timezone.
    """
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app = Flask(__name__)
app.config.from_object(Config)

babel = Babel(app)


@app.route('/')
def index() -> str:
    """
    Renders welcome page.

    Returns:
        str: HTML content of the welcome page.
    """
    return render_template('1-index.html')


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
