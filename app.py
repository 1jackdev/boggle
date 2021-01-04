from boggle import Boggle
from flask import Flask, render_template, request, session

app = Flask(__name__)

app.config["SECRET_KEY"] = "boggle1"

boggle_game = Boggle()


@app.route('/')
def show_homepage():
    board = boggle_game.make_board()
    session["board"] = board
    return render_template("index.html", board=board)
