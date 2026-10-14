# Programmers: Ryan Weinswig and Fletcher Cahill
# Date: October 14th, 2026

class Account:
    # Initializes an account with a username, password, friend list, and posts list
    def __init__(self, username, password, list_of_friends=None, posts=None):
        self.username = username
        self.password = password
        self.list_of_friends = list_of_friends if list_of_friends is not None else []
        self.posts = posts if posts is not None else []

    # Checks if a user is already present in the friend list
    def alreadyFriends(self, friend):
        if friend in self.list_of_friends:
            return True
        return False

    # Adds a new friend to the user's friend list
    def addFriend(self, friend):
        if not self.alreadyFriends(friend):
            self.list_of_friends.append(friend)

    # Displays all friends currently added by the user
    def showFriends(self):
        if not self.list_of_friends:
            print("You don't have any friends added yet.")
        else:
            print("Your friends:")
            for friend in self.list_of_friends:
                print(f"- {friend}")

    # Converts the account instance into a dictionary format for JSON storage
    def to_dict(self):
        return {
            "username": self.username,
            "password": self.password,
            "list_of_friends": self.list_of_friends,
            "posts": self.posts
        }