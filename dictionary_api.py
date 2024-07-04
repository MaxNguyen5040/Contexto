import requests

API_URL = "https://api.dictionaryapi.dev/api/v2/entries/en"

def fetch_word_definition(word):
    response = requests.get(f"{API_URL}/{word}")
    if response.status_code == 200:
        data = response.json()
        if data:
            return data[0]['meanings'][0]['definitions'][0]['definition']
    return None