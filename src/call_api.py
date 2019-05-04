import requests


def call_google():
    response = requests.get('https://www.google.com')
    return response
