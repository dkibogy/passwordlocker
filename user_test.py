import unittest # Importing the unittest module
from user import User # importing the user class


class TestUser(unittest.TestCase):
    """
    test class that defines the test cases for the user behaviours,
    test case class helps in creating test cases
    """
    def setUp(self):

        self.new_user = User("daisy", "1234")
    
    def tearDown(self):

        User.user_list = []

    def test_init(self):
        """
        test case to test if objects are initialised properly
        """
        self.assertEqual(self.new_user.name,"daisy")
        self.assertEqual(self.new_user.password,"1234")

    def test_save_user(self):

        self.new_user.save_user()#saving the new user
        self.assertEqual(len(User.user_list),1)
    
    def test_save_multiple_user(self):

        self.new_user.save_user()
        test_user = User("Test", "0000")#new contact
        test_user.save_user()
        self.assertEqual(len(User.user_list),2)

    def test_delete_user(self):

        self.new_user.save_user()
        test_user = User("Test", "0000")
        test_user.save_user()
        self.new_user.delete_user() #deleting a user object
        self.assertEqual(len(User.user_list),1)
    


if __name__ == '__main__':
    unittest.main()