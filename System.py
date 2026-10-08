from Account import Account

import json
# Will add the filename into gitignore eventually
FILENAME = "accounts.JSON"

class System:

    accounts = {}
    posts = {}

    def checkIfUserNameIsRight(username):
        pass

    def checkIfPasswordIsRight(password):
        pass

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
        # Check this again 
        friend = input("Who do you want to add? ")
        if username == current_user.username:
            print("You can't add yourself")
        elif Account.addFriend(friend) == False:
            print("You already have this friend added")
        else:
            saveAccounts(Accounts)





def createAccount(accounts):
        # accounts = dictionary of existing users {username: Account}

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
    with open (FILENAME, "w") as f:
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
