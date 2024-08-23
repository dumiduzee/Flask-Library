class adminValidation:
    def __init__(self,username,password):
        self.__username = username
        self.__password = password

    def usernameChecker(self):
        if self.__username == "dumidu":
            return True
        else:
            return False
        
    def passwordChecker(self):
        if self.__password == "dumidu":
            return True
        else:
            return False