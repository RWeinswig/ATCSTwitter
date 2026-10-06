import json
FILENAME = "accounts.JSON"

class Account:


    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.list_of_friends = []
        self.posts = []

    def to_dict(self):
        return {
            "username": self.username,
            "password": self.password,
            "list_of_friends": self.list_of_friends,
            "posts": self.posts,
        }

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


def saveAccounts(accounts):
    data = {}
    for username in accounts:
        data[username] = accounts[username].to_dict()
    with open(FILENAME, "w") as f:
        json.dump(data, f, indent=4)


def loadAccounts():
    try:
        with open(FILENAME, "r") as f:
            data = json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        return {}
    accounts = {}
    for username in data:
        info = data[username]
        account = Account(info["username"], info["password"])
        account.list_of_friends = info["list_of_friends"]
        account.posts = info["posts"]
        accounts[username] = account
    return accounts
