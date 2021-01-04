from boggle import Boggle
from flask import Flask, request, render_template

app = Flask(__name__)

boggle_game = Boggle()


@app.route('/')
def show_homepage():
   return render_template("index.html")