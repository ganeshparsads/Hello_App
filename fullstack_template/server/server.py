# server.py
from flask import Flask, render_template
import random

app = Flask(__name__, static_folder="../static/dist", template_folder="../static")

@app.route("/")
def index():
    """
    home
    """
    return render_template("index.html")

@app.route("/hello")
def hello():
    """
    another endpoint
    """
    return get_hello()

# helpers
def get_hello():
    greeting_list = ['Ciao', 'Hei', 'Salut', 'Hola', 'Hallo', 'Hej', 'gani']
    return random.choice(greeting_list)


if __name__ == "__main__":
    app.run()
