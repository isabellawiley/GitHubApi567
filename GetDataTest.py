import requests
import json

def getData():
    gitHubID = input('Please enter GitHub ID:')
    response = requests.get(f'https://api.github.com/users/{gitHubID}/repos')

    sCode = response.status_code

    if sCode >= 200 and sCode < 300:
        print(response.json())
    elif sCode >= 300 and sCode < 400:
        print('Redirect neccessary. Response:', response)
    elif sCode >= 400 and sCode < 500:
        print('Invalid input. Use a valid GitHub ID. Response:', response)
    elif sCode >= 500:
        print('Server Error. Response:', response)
    else:
        print('Failed. Response:', response)

getData()
