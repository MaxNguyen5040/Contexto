import json
import os

WORDS_FILE = "words.json"

def save_word(word, definition):
    if os.path.exists(WORDS_FILE):
        with open(WORDS_FILE, 'r') as file:
            words = json.load(file)
    else:
        words = {}
    
    words[word] = definition
    
    with open(WORDS_FILE, 'w') as file:
        json.dump(words, file)

def load_words():
    if os.path.exists(WORDS_FILE):
        with open(WORDS_FILE, 'r') as file:
            words = json.load(file)
        return words
    return {}