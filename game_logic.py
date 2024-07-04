import random

class ContextoGame:
    def __init__(self):
        self.target_word = "example"
        self.guesses = []

    def check_guess(self, guess):
        self.guesses.append(guess)
        if guess == self.target_word:
            return "Correct!"
        else:
            return f"{guess} is not the word."

    def get_guesses(self):
        return self.guesses

game = ContextoGame()