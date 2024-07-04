import requests

def fetch_text_data(url):
    """
    Fetches text data from a specified URL.

    Args:
        url (str): The URL from which to fetch data.

    Returns:
        list: A list of fetched text data.
    """
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise exception for bad status codes
        if response.status_code == 200:
            return response.json()
        else:
            print(f"Error: Failed to fetch data. Status code: {response.status_code}")
            return []
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
        return []

# testing
data = fetch_text_data("https://api.dictionaryapi.dev/api/v2/entries/en/hello")
print(f"Fetched data: {data}")