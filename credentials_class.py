import unittest
import readfiles
class User_credentials():

    list_of_credentials = []


    def __init__(self, website , user_name_cr , password_cr):
        self.website = website
        self.user_name_cr = user_name_cr
        self.password_cr = password_cr



class TestReadFiles(unittest.TestCase):
    """
    Class to test the  functions on the  readfiles module

    Args:
        unittest.TestCase: Class from the unittest module to create unit tests
    """
if __name__ == "__main__":
    unittest.main()
