from boggle import Boggle
from flask import Flask, request, render_template

boggle_game = Boggle()


@app.route('/')
def show_homepage():
   return render_template("index.html")