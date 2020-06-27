import unittest # Importing the unittest module
from user import User # importing the user class

class TestUser(unittest.TestCase):
    """
    test class that defines the test cases for the user behaviours,
    test case class helps in creating test cases
    """
    def setUp(self):

        pass

    def test_init(self):
        """
        test case to test if objects are initialised properly
        """
        pass 
if __name__ == '__main__':
    unittest.main()