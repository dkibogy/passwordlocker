import unittest # Importing the unittest module
from user import User # importing the user class

class TestUser(unittest.TestCase):
    """
    test class that defines the test cases for the user behaviours,
    test case class helps in creating test cases
    """
    def setUp(self):

        self.new_user = User("daisy", "1234")

    def test_init(self):
        """
        test case to test if objects are initialised properly
        """
        self.assertEqual(self.new_user.name,"daisy")
        self.assertEqual(self.new_user.password,"1234")

    def test_save_user(self):

        self.new_user.save_user()#saving the new user
        self.assertEqual(len(User.user_list),1)
        
if __name__ == '__main__':
    unittest.main()