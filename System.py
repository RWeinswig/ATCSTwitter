# Programmers: Ryan Weinswig and Fletcher Cahill
# Date: October 14th, 2026

from Account import Account
from Post import Post
import json

FILENAME = "accounts.JSON"

class System:
    accounts = {}
    posts = []

    # This takes in a username and goes through all of the accounts
    # If the username matches with one in the accounts, it returns True
    @staticmethod
    def checkIfUserNameIsRight(username, accounts):
        if username in accounts:
            return True
        else:
            return False

    # This function takes in a username, password, and the accounts
    # It checks to make sure that the username exists, then checks to make sure that the password matches the username
    @staticmethod
    def checkIfPasswordIsRight(username, password, accounts):
        if System.checkIfUserNameIsRight(username, accounts):
            if accounts[username].password == password:
                return True
            return False
        return False

    # Prints every post made by the current user's friends and returns them            
    @staticmethod
    def viewPosts(current_user, accounts):
        # Prints every post made by the current user's friends and returns them
        friend_posts = []
        for friend in accounts[current_user].list_of_friends:
            friend_posts.extend(accounts[friend].posts)
        if not friend_posts:
            print("Your friends haven't posted anything yet")
        for post in friend_posts:
            print(f"{post['User']} ({post['Time stamp']}): {post['Content']}")
        return friend_posts

    @staticmethod
    def addFriend(current_user, friend, accounts):
        # Adds the friend to the current users friend list if friend is valid
        user_account = accounts[current_user]
        if friend == current_user:
            print("You can't add yourself")
            return False
        elif friend not in accounts:
            print("That user doesn't exist")
            return False
        elif user_account.alreadyFriends(friend):
            print("You already have this friend added")
            return False
        else:
            user_account.addFriend(friend)
            saveAccounts(accounts)
            print(f"Added {friend} as a friend")
            return True
            
    # Creates a new user account with validation
    @staticmethod
    def createAccount(accounts):
        # Accounts = dictionary of existing users {username: Account}

        # 1. Get a valid username
        while True:
            username = input("Choose a username: ").strip()
            if username == "":
                print("Username cannot be empty.")
            elif username in accounts:
                print("That username is already taken.")
            else:
                break

        # 2. Get a valid password
        while True:
            password = input("Choose a password (at least 8 characters): ")
            if len(password) < 8:
                print("Password must be at least 8 characters.")
                continue
            confirm = input("Re-enter your password: ")
            if password != confirm:
                print("Passwords do not match.")
            else:
                break

        # 3. Create the account and store it
        new_account = Account(username, password)
        accounts[username] = new_account
        saveAccounts(accounts)

        # 4. Confirm
        print(f"Account created. Welcome, {username}!")
        return new_account


# Saves each account to a JSON file when app is closed
def saveAccounts(accounts):
    data = {username: account.to_dict() for username, account in accounts.items()}
    with open(FILENAME, "w") as f:
        json.dump(data, f, indent=4)


# Reads in every account from the JSON file and creates account with all their info for each
def loadAccounts():
    try:
        with open(FILENAME, "r") as f:
            data = json.load(f)
    # This ensures that if the file path is off or there is a problem with JSON it doesn't crash
    except (FileNotFoundError, json.JSONDecodeError):
        return {}
    return {username: Account(**info) for username, info in data.items()}


def createPost(username, accounts):
    # Gets the username in order to store that with post
    user_account = accounts[username]

    content = input("What would you like to post? ").strip()

    if not content:
        print("Your post cannot be empty.")
        return

    # Create the post
    post = Post(username, content)

    # Store the post as a dictionary so it can be saved to JSON
    user_account.posts.append(post.to_dict())

    # Save the updated accounts
    saveAccounts(accounts)

    print("Post created successfully!")