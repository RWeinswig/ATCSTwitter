from System import loadAccounts
class Account:
    # Initializes somebody's account
    def __init__(self, username, password, list_of_friends=None, posts=None):
        self.username = username
        self.password = password
        self.list_of_friends = list_of_friends if list_of_friends is not None else []
        self.posts = posts if posts is not None else []
    # This function saves the account info to a dictionary to be saved to a JSON file when the account is closed
    def to_dict(self):
        return {
            "username": self.username,
            "password": self.password,
            "list_of_friends": self.list_of_friends,
            "posts": self.posts,
        }
    


    

    def typeAPost():
        pass

    def addFriend(self, username):
        if username in self.list_of_friends:
            return False
        else:
            return True

    def changeUsername():
        pass

    def changePassword():
        pass

    def checkToSeeIfYouCanView():
        pass