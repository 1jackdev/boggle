from boggle import Boggle
from flask import Flask, render_template, request, session, jsonify

app = Flask(__name__)

app.config["SECRET_KEY"] = "boggle1"

boggle_game = Boggle()


@app.route('/')
def show_homepage():
    board = boggle_game.make_board()
    session["board"] = board
    return render_template("index.html", board=board)


@app.route('/make-guess')
def handle_guess():
    board = session["board"]
    guess = request.args["guess"]
    result = boggle_game.check_valid_word(board, guess)
    return jsonify({"result": result})
    
    
