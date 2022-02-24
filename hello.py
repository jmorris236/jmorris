from flask import Flask, render_template

# Create a Flask Instance
app = Flask(__name__)


# These are html filters for Jinja
# safe
# capitalize
# lower
# upper
# title
# trim
# striptags

# Create a route decorator for home page
@app.route('/')
def index():
    first_name = "John"
    stuff = "This is bold text"
    favorite_pizza = ['Pepperoni', 'Mushroom', 'Chicken']
    return render_template('index.html', first_name=first_name, stuff=stuff, favorite_pizza=favorite_pizza)


# localhost:5000/user/john
@app.route('/user/<name>')
def user(name):
    return render_template('user.html', user_name=name)


# Create Custom Error Pages
# Invalid URL

@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html"), 404


@app.errorhandler(500)
def page_not_found(e):
    return render_template("500.html"), 500
