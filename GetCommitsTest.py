import requests
import json


def getCommits():
    gitHubID = input('Please enter GitHub ID:')
    ghRepo = input('Please enter Repository:')
    response = requests.get(f'https://api.github.com/repos/{gitHubID}/{ghRepo}/commits')

    sCode = response.status_code
    commits = len(response.json())

    if sCode >= 200 and sCode < 300:
        print(gitHubID, ' Number of commits:', commits)
    elif sCode >= 300 and sCode < 400:
        print('Redirect neccessary. Response:', response)
    elif sCode >= 400 and sCode < 500:
        print('Invalid input. Use a valid GitHub ID and Repository. Response:', response)
    elif sCode >= 500:
        print('Server Error. Response:', response)
    else:
        print('Failed. Response:', response)

getCommits()