from unittest import TestCase
from app import app
from flask import session
from boggle import Boggle


class FlaskTests(TestCase):

    def setUp(self):
        """Stuff to do before every test."""

        self.client = app.test_client()
        app.config['TESTING'] = True
    
    def test_homepage(self):
        with self.client:
            response = self.client.get("/")
            self.assertIn("board",session)
            self.assertIsNone(session.get('highscore'))
            self.assertIsNone(session.get('num_plays'))
            self.assertIn(b'<p>High Score:', response.data)
            self.assertIn(b'Score:', response.data)
            self.assertIn(b'Seconds Left:', response.data)

    def test_valid_word(self):
        """Test if the word is in the sessions board."""

        with self.client as client:
            with client.session_transaction() as sess:
                sess['board'] = [["B", "A", "T", "T", "T"], 
                                 ["B", "I", "T", "T", "T"], 
                                 ["B", "E", "T", "T", "T"], 
                                 ["B", "O", "T", "T", "T"], 
                                 ["B", "U", "T", "T", "T"]]
        response = self.client.get('/make-guess?guess=bet')
        self.assertEqual(response.json['result'], 'ok')

    def test_invalid_word(self):
        """Test a word that is too long for the board."""

        self.client.get('/')
        response = self.client.get('/make-guess?guess=impossible')
        self.assertEqual(response.json['result'], 'not-on-board')

    def non_english_word(self):
        """Test if word is not in the words dictionary."""

        self.client.get('/')
        response = self.client.get(
            '/make-guess?guess=asdfasdfasdfasdfasdf')
        self.assertEqual(response.json['result'], 'not-word')

