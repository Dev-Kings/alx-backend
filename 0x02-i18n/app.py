#!/usr/bin/env python3
"""
Flask app to demonstrate i18n with user-based locale and timezone selection.
"""

from flask import Flask, g, render_template, request
from flask_babel import Babel, _
import pytz
from pytz import UnknownTimeZoneError
from typing import Optional, Dict, Any
from datetime import datetime


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


# Mock user data
users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


def get_user() -> Optional[Dict[str, str]]:
    """Retrieve a user based on the login_as parameter.

    Returns:
        dict: The user's data if found, otherwise None.
    """
    user_id = request.args.get("login_as")
    if user_id and int(user_id) in users:
        return users[int(user_id)]
    return None


@babel.timezoneselector
def get_timezone() -> str:
    """
    Determine the appropriate timezone based on URL, user settings,
    or default.

    Priority:
    1. Timezone from URL parameters.
    2. Timezone from user settings.
    3. Default to 'UTC' if no valid timezone is found.

    Returns:
        str: The determined timezone string.
    """
    # Check if timezone parameter is in URL and validate it.
    tz = request.args.get("timezone")
    if tz:
        try:
            pytz.timezone(tz)
            return tz
        except UnknownTimeZoneError:
            pass  # Ignore invalid timezone

    # Check user's preferred timezone if logged in and validate it.
    if g.user:
        tz = g.user.get("timezone")
        if tz:
            try:
                pytz.timezone(tz)
                return tz
            except UnknownTimeZoneError:
                pass  # Ignore invalid timezone
    # Default to UTC
    return "UTC"


@app.before_request
def before_request() -> None:
    """
    Execute before each request to check if a user is logged in.
    Sets the user in flask.g if present
    """
    g.user = get_user()


@babel.localeselector
def get_locale() -> str:
    """
    Determines the best match for supported languages based on the
    URL parameter, user settings, request headers, or default.

    Priority order:
    1. Locale from URL parameter (e.g., ?locale=fr)
    2. Locale from logged-in user's settings
    3. Locale from request headers
    4. Default locale ('en')

    Returns:
        str: The best matching language from the request headers.
    """
    locale = request.args.get('locale')
    if locale in Config.LANGUAGES:
        return locale

    if g.user and g.user["locale"] in Config.LANGUAGES:
        return g.user["locale"]

    return (request.accept_languages.best_match(app.config['LANGUAGES'])
            or "en")


@app.route('/')
def index() -> str:
    """
    Renders welcome page.

    Returns:
        str: HTML content of the welcome page.
    """
    timezone = pytz.timezone(get_timezone())
    current_time = datetime.now(timezone)
    formatted_time = current_time.strftime('%b %d, %Y, %I:%M:%S %p')

    return render_template('index.html', current_time=formatted_time)


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
