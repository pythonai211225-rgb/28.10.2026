import login1

class User:

    def __init__(self, name):
        self.name = name

    # function1
    login = login1.login

    # function2
    logout = login1.logout

u = User("Alice")
u.login("alice123", "password")

