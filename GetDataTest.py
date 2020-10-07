# import requests
# import json
# import unittest

# from GetData import getData

# # This code implements the unit test functionality
# # https://docs.python.org/3/library/unittest.html has a nice description of the framework

# class GetDataTest(unittest.TestCase):
#     # define multiple sets of tests that account for the different status codes that can occur with API requests
    
#     #tests for success ie. valid GitHub ID 
#     def testSuccess(self): 
#         response = requests.get(f'https://api.github.com/users/richkempinski/repos')
#         self.assertEqual(getData(200, response),response.json(), '200 should work')  
    
#     # tests for if the user needs to take additional actions to complete the request
#     def testFailure1(self): 
#         response = requests.get(f'https://api.github.com/users/isaellawiley/repos')
#         self.assertEqual(getData(300,response),'Redirect neccessary.', '300 should be Redirect neccessary')
   
#     #tests for user error ie. invalid GitHub ID
#     def testFailure2(self): 
#         response = requests.get(f'https://api.github.com/users/isaellawiley/repos')
#         self.assertEqual(getData(400,response),'Invalid input. Use a valid GitHub ID.', '400 should be Invalid input. Use a valid GitHub ID.')
    
#     #tests for server error
#     def testFailure3(self): 
#         response = requests.get(f'https://api.github.com/users/isaellawiley/repos')
#         self.assertEqual(getData(500,response),'Server Error.', '500 should be Server Error.')
        
# if __name__ == '__main__':
#     print('Running unit tests')
#     unittest.main()
