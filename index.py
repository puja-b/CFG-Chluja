# http://flask.pocoo.org/docs/1.0/


# pip is a Python package manager (like a vast plugin library)
# we use pip to install Flask, and the line below is how we bring in Flask (and a variety of other functions and helpers) into our app
from flask import Flask, url_for, render_template, jsonify, request

app = Flask(__name__)


# u"" is unicode, not necessary in Python3
# Here we are mimicking a database, in the form of an array of blog post objects

# INDEX PAGE
# the '/' is removed by default by the browser, but it represents the root page (eg www.facebook.com/)
@app.route("/")
def index():
    # When we visit http://localhost:5000 or http://127.0.0.1:5000 (they're the same thing) we fire this function which returns a string which is displayed in the browser
    return render_template('base.html')

# TEST PAGE
@app.route("/test/<name>")
# Similar to above, except this time we are using the <name> in the URL (referred to as params) and passing that value into the function. Think of it a bit like the input() function
def test(name):
    return "Hello World! Name {}".format(name)

# POST NEW EMAIL FORM:
@app.route("/email")
def email():
    return render_template('addPost.html')

# POST EMAIL FORM ACTION
@app.route("/email", methods=['POST'])
def emailPost():
    return "Thanks {} Email was sent successfully".format(request.form['name'])


# What actually runs the app
app.run()
