import random

class ContextoGame:
    def __init__(self):
        self.target_word = "example"
        self.guesses = []

    def check_guess(self, guess):
        self.guesses.append(guess)
        if guess == self.target_word:
            return f"{guess} is Correct!"
        else:
            # Example feedback logic
            common_letters = set(guess) & set(self.target_word)
            return f"{guess} is not the word. Common letters: {', '.join(common_letters)}"

game = ContextoGame()