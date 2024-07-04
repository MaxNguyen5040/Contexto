import random

class ContextoGame:
    def __init__(self):
        self.words = ["example", "python", "context", "game", "learning", "data", "science", "machine", "intelligence", "code"]
        self.target_word = random.choice(self.words)
        self.guesses = []
        self.score = 0

    def check_guess(self, guess):
        self.guesses.append(guess)
        if guess == self.target_word:
            self.score += 1
            return f"{guess} is Correct! Your score is {self.score}"
        else:
            common_letters = set(guess) & set(self.target_word)
            common_positions = sum(1 for a, b in zip(guess, self.target_word) if a == b)
            return f"{guess} is not the word. Common letters: {', '.join(common_letters)}. Correct positions: {common_positions}"

    def reset(self):
        self.__init__()

    def get_guesses(self):
        return self.guesses

game = ContextoGame()