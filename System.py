class System:

    

    accounts = {}
    posts = {}

    def checkIfUserNameIsRight(username):
        if (username in self.accounts):
            return True
        else:
            return False

    def checkIfPasswordIsRight(username, password):
        if (self.checkIfUserNameIsRight(username)):
            if (self.accounts[username] == password):
                return True

    def changePassword(account):
        pass

    def changeUsername(account):
        pass

    def logOut():
        pass

    def viewPosts(username):
        pass

    def logIn(username, password):

        pass

    def typePost():
        pass

    def addFriend():
        pass
