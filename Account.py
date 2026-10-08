import json
FILENAME = "accounts.JSON"

class Account:


    def __init__(self, username, password, list_of_friends=None, posts=None):
        self.username = username
        self.password = password
        self.list_of_friends = list_of_friends if list_of_friends is not None else []
        self.posts = posts if posts is not None else []

    def to_dict(self):
        return {
            "username": self.username,
            "password": self.password,
            "list_of_friends": self.list_of_friends,
            "posts": self.posts,
        }

    def saveAccounts(accounts):
        data = {username: account.to_dict() for username, account in accounts.items()}
        with open (FILENAME, "w") as f:
            json.dump(data, f, indent=4)

    def loadAccounts():
        try:
            with open(FILENAME, "r") as f:
                data = json.load(f)
        except (FileNotFoundError, json.JSONDecodeError):
            return {}
        return {username: Account(**info) for username, info in data.items()}


    

    def typeAPost():
        pass

    def AddFriend(username):
        pass

    def changeUsername():
        pass

    def changePassword():
        pass

    def checkToSeeIfYouCanView():
        pass