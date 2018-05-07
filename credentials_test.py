import unittest,csv, sys, pyperclip
from credentials_class import Credentials
import credentials





class test_credentials(unittest.TestCase):

    def setUp(self):
        self.new_credentials = Credentials("www.decomagna.com","lulu","mypassword")


    def test_initialise(self):
        self.assertEqual(self.new_credentials.website,"www.decomagna.com")

    def test_save_credentials(self):
        self.new_credentials.save_credentials()
        self.assertEqual(len(Credentials.list_of_credentials),1)

    def test_get_data(self):
        """
        Test case to confirm that we are getting data from the file
        """
        with open("test.txt","r") as handle:
            data = handle.read()
            self.assertEqual(data,readfiles.read_file("credentials.txt"))








if __name__ == "__main__":
    unittest.main()
