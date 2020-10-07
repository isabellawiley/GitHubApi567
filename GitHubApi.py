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
    
def getData(sCode, response):
   
    if sCode >= 200 and sCode < 300:
        return(response.json())
    elif sCode >= 300 and sCode < 400:
        return('Redirect neccessary.')
    elif sCode >= 400 and sCode < 500:
        return('Invalid input. Use a valid GitHub ID.')
    elif sCode >= 500:
        return('Server Error.')
