import requests

CORPUS_URL = "https://example.com/word-corpus.txt"

def fetch_word_corpus():
    response = requests.get(CORPUS_URL)
    if response.status_code == 200:
        words = response.text.splitlines()
        return words
    return []