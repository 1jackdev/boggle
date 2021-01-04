from boggle import Boggle
from flask import Flask, render_template, request, session, jsonify

app = Flask(__name__)

app.config["SECRET_KEY"] = "boggle1"

boggle_game = Boggle()


@app.route('/')
def show_homepage():
    """Show the board and its score data."""
    board = boggle_game.make_board()
    session["board"] = board
    highscore = session.get("highscore", 0)
    num_plays = session.get("num-plays", 0)
    return render_template("index.html", board=board, highscore=highscore, num_plays=num_plays)


@app.route('/make-guess')
def handle_guess():
    """take the guess from the board and check it. Then, return the result."""
    board = session["board"]
    guess = request.args["guess"]
    result = boggle_game.check_valid_word(board, guess)
    return jsonify({"result": result})


@app.route("/post-score", methods=["POST"])
def post_score():
    """Receive score, update num_plays, and update the high score."""

    score = request.json["score"]
    highscore = session.get("highscore", 0)
    num_plays = session.get("num_plays", 0)

    session['num_plays'] = num_plays + 1
    session['highscore'] = max(score, highscore)

    return jsonify(brokeRecord=score > highscore)
