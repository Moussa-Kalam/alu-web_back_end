#!/usr/bin/env python3
"""Basic Flask app that implements i18n and internationalization"""

from flask import Flask, render_template, request, g
from flask_babel import Babel
import pytz

app = Flask(__name__)

users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


class Config:
    """Config class for your application, it deals with babel mostly"""
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app.config.from_object(Config)
babel = Babel(app)


@babel.localeselector
def get_locale():
    """Get locale for your application"""
    locale = request.args.get('locale')
    if locale and locale in app.config['LANGUAGES']:
        return locale
    user = g.get('user')
    if (user and user.get("locale", None)
            and user["locale"] in app.config['LANGUAGES']):
        return g.user["locale"]
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route('/', methods=['GET'], strict_slashes=False)
def home():
    """Home page for your application"""
    login = False
    if g.get('user'):
        login = True
    return render_template('6-index.html', login=login)


def get_user():
    """Get user information from users dict"""
    try:
        login_as = int(request.args.get('login_as'))
        return users.get(int(login_as))
    except Exception:
        return None


@app.before_request
def before_request():
    """Before request"""
    user = get_user()
    print(user)
    if user:
        g.user = user

@babel.timezoneselector
def get_timezone() -> str:
    "get the timezone and set it as the default timezone"
    try:
        if request.args.get('timezone'):
            return str(pytz.timezone(request.args.get('timezone')))
        if g.get('user') and g.user.get('timezone'):
            return str(pytz.timezone(g.user['timezone']))
    except pytz.exceptions.UnknownTimeZoneError:
        pass
    return app.config["BABEL_DEFAULT_TIMEZONE"]


if __name__ == "__main__":
    app.run()
