import unittest


class Credentials():

    list_of_credentials = []


    def __init__(self, website , user_name_cr , password_cr):
        self.website = website
        self.user_name_cr = user_name_cr
        self.password_cr = password_cr


    def save_credentials(self):
        Credentials.list_of_credentials.append(self)

    def delete_credentials(self):
        Credentials.list_of_credentials.remove(self)


    def test_get_data(self):
        """
        Test case to confirm that we are getting data from the file
        """
        with open("test.txt","r") as handle:
            data = handle.read()
            self.assertEqual(data,readfiles.read_file("test.txt"))
