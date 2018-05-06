import unittest, pyperclip
from user_class import User

class TestContact(unittest.TestCase):

    def setUp(self):
        '''
        Set up method to run before each test cases.
        '''
        self.new_user = User("lulu","aS2olidPas5") # create contact object


    def test_init(self):
        '''
        test_init test case to test if the object is initialized properly
        '''
        self.assertEqual(self.new_user.user_name,"lulu")
        print(self.new_user.user_name)
        self.assertEqual(self.new_user.password,"aS2olidPas5")
        print(self.new_user.password)

    def test_save_users(self):

        self.new_user.save_new_user() # save_new_user is defined in the user_class...
        self.assertEqual(len(User.list_of_users),1)
        print(len(User.list_of_users))


    def tearDown(self):
            '''
            tearDown method that does clean up after each test case has run.
            '''
            User.list_of_users = []


    def test_save_multiple_users(self):
            '''
            test_save_multiple_contact to check if we can save multiple contact
            objects to our contact_list
            '''
            self.new_user.save_new_user()
            test_user = User("juya","1234") # new user
            test_user.save_new_user()
            self.assertEqual(len(User.list_of_users),2)


    def test_delete_user(self):
            '''
            test_delete_contact to test if we can remove a contact from our contact list
            '''
            self.new_user.save_new_user()
            test_user = User("testy","Simpson") # new contact
            test_user.save_new_user()

            self.new_user.delete_user()# Deleting a contact object
            self.assertEqual(len(User.list_of_users),1)


    def test_find_user_by_name(self):
        '''
        test to check if we can find a user by name and display information
        '''

        self.new_user.save_new_user()
        test_user = User("testy","Simpson")
        test_user.save_new_user()

        active_user = User.find_by_name("testy")
        print(active_user.user_name)

        self.assertEqual(active_user.user_name,test_user.user_name)


    def test_user_exists(self):
        self.new_user.save_new_user()
        test_user = User("James","jamo") # new contact
        test_user.save_new_user()

        user_exists = User.user_exist("James")

        self.assertTrue(user_exists)

    def test_display_all_users(self):
        self.assertEqual(User.display_users(),User.list_of_users)


    # def test_copy_email(self):
    #     self.new_user.save_new_user()
    #     User.copy_passwords("jamo")
    #
    #     self.assertEqual(self.new_user.password,pyperclip.paste())



if __name__ == '__main__':
    unittest.main()
