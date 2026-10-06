from Account import Account, saveAccounts

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
        pass



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
