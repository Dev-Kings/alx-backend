# 0x02. i18n - Internationalization in Flask

This project focuses on implementing internationalization (i18n) in a Flask application, enabling the app to display content in multiple languages and localize timestamps. You will learn how to infer the correct locale based on URL parameters, user settings, or request headers.

## Resources

Refer to the following resources to complete the project:

- [Flask-Babel Documentation](https://pythonhosted.org/Flask-Babel/)
- [Flask i18n Tutorial](https://flask.palletsprojects.com/tutorial/)
- [pytz Documentation](https://pytz.sourceforge.net/)

## Learning Objectives

- Parametrize Flask templates to support multiple languages.
- Infer the correct locale from URL parameters, user settings, or request headers.
- Localize timestamps based on the user's locale and timezone.

## Project Structure

1. **Set up Flask-Babel**:
   - Install and configure `Flask-Babel` in your Flask application.
   - Define supported languages, default locale, and default timezone.
   - Initialize Babel with your app.

2. **Translate Text**:
   - Use the `_()` function from Flask-Babel to mark text for translation in your templates.
   - Create translation files (.po files) for each supported language and compile them into .mo files.

3. **Locale Detection**:
   - Implement a `get_locale()` function to determine the correct language based on URL parameters, user preferences, or `Accept-Language` headers.

4. **Timestamp Localization**:
   - Use the `format_datetime()` function to localize timestamps.
   - Integrate `pytz` to manage timezone data effectively.

5. **Testing and Documentation**:
   - Ensure all functions are type-annotated and documented.
   - Adhere to `pycodestyle` and make all files executable.
   - Test locale switching and timestamp localization for accuracy.

## Example Code

### Setting up Flask-Babel

```python
    from flask import Flask, request
    from flask_babel import Babel, _

    app = Flask(__name__)
    app.config['BABEL_DEFAULT_LOCALE'] = 'en'
    app.config['BABEL_SUPPORTED_LOCALES'] = ['en', 'fr', 'es']
    app.config['BABEL_DEFAULT_TIMEZONE'] = 'UTC'

    babel = Babel(app)

    @babel.localeselector
    def get_locale():
        # Check URL, user settings, or headers for language preference
        return request.args.get('lang') or request.accept_languages.best_match(['en', 'fr', 'es'])
```

## Using Translations in Templates
```
    <h1>{{ _('Welcome to My Site') }}</h1>
```

### Localizing Timestamps
```
    from flask_babel import format_datetime
    from datetime import datetime

    @app.route('/')
    def home():
        now = datetime.now()
        localized_time = format_datetime(now)
        return f"The current time is: {localized_time}"
```
