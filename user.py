class User:
    """
    class that generates new instances of users
    """
    user_list = []

    def __init__(self, name, password):
        self.name = name
        self.password = password