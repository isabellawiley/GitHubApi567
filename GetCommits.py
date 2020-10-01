import requests
import json


def getCommits(gitHubID, ghRepo):
    
    response = requests.get(f'https://api.github.com/repos/{gitHubID}/{ghRepo}/commits')

    sCode = response.status_code
    commits = len(response.json())

    if sCode >= 200 and sCode < 300:
        return('{} Number of commits: {}'.format(ghRepo, commits))
    else:
        return('Invalid input. Use a valid GitHub ID and Repository.')
    
