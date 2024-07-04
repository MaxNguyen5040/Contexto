import random

class ContextoGame:
    def __init__(self):
        self.target_word = "example"
        self.guesses = []
        self.score = 0

    def check_guess(self, guess):
        self.guesses.append(guess)
        if guess == self.target_word:
            self.score += 1
            return f"{guess} is Correct! Your score is {self.score}"
        else:
            common_letters = set(guess) & set(self.target_word)
            return f"{guess} is not the word. Common letters: {', '.join(common_letters)}"
        
    def reset(self):
        self.__init__()
        
game = ContextoGame()