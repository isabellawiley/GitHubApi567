import requests
import json
import unittest

from GetCommits import getCommits

# This code implements the unit test functionality
# https://docs.python.org/3/library/unittest.html has a nice description of the framework


class GetDataTest(unittest.TestCase):
    # define multiple sets of tests that account for the different status codes that can occur with API requests
    
    #tests for success ie. valid GitHub ID 
    def testSuccess(self): 
        response = requests.get(f'https://api.github.com/repos/richkempinski/hellogitworld/commits')
        commits = len(response.json())
        self.assertEqual(getCommits('richkempinski', 'hellogitworld'),'hellogitworld Number of commits: {}'.format(commits))  
    
   
    #tests for user error ie. invalid GitHub ID
    def testFailure2(self): 
        self.assertEqual(getCommits('richkempinski','abcdefgzyxwvut'),'Invalid input. Use a valid GitHub ID and Repository.')
    
        
if __name__ == '__main__':
    print('Running unit tests')
    unittest.main()