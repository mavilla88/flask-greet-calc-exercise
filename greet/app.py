from flask import Flask, request

app = Flask(__name__)


@app.route('/welcome')
def welcome_page():
    """Return simple "welcome" greeting"""
    html = """
    <html>
        <body>
            <h1>Welcome 😀</h1>
            <p>Welcome to my simple app!</p>
            <a href='/welcome/home'>Go to home page</a>
            <a href='/welcome/back'>Go to welcome back page</a>
        </body>
    </html>
    """
    return html


@app.route('/welcome/home')
def home_page():
    """Return simple "welcome home" greeting"""
    html = """
    <html>
        <body>
            <h1>Welcome Home 🦝</h1>
            <p>This is the home page</p>
            <a href='/welcome'>Go to welcome page</a>
            <a href='/welcome/home'>Go to home page</a>
            <a href='/welcome/back'>Go to welcome back page</a>
        </body>
    </html>
    """
    return html


@app.route('/welcome/back')
def say_bye():
    """Return simple "welcome back" greeting"""
    html = """
    <html>
        <body>
            <h1>Welcome back! 🦝</h1>
            <h2>👋🏻</h2>
            <a href='/welcome/home'>Go to home page</a>
            <a href='/welcome'>Go to welcome page</a>
        </body>
    </html>
    """
    return html
