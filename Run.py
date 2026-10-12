from System import System, loadAccounts, createAccount, checkIfPasswordIsRight


# Turns the user's menu input into 1 or 2, raising a ValueError with a helpful message otherwise
def validate_user_choice(choice_str):
    try:
        choice = int(choice_str)
    except ValueError:
        raise ValueError("Please enter a number either 1 or 2! ")
    if choice not in (1, 2):
        raise ValueError("Please enter an integer 1 or 2! ")
    return choice


# First things the user sees
def homeScreen():
    while True:
        try:
            return validate_user_choice(input("Choose an option: \n 1. Create an account \n 2. Log In to your Account\n"))
        except ValueError as e:
            print(f"{e}\n")


def checkLogIn(username, password, accounts):
    if checkIfPasswordIsRight(username, password, accounts):
        print("Log In is possible")
        return True
    print("Log in is not possible")
    return False


# Creates an account or logs in based on the user's choice
# Returns the username of the logged-in user, or None if logging in failed
def initializeAccount(userInput, accounts):
    if userInput == 1:
        return createAccount(accounts).username
    username = input("Username: ")
    password = input("Password: ")
    if checkLogIn(username, password, accounts):
        return username
    return None


# Keeps going back to the home screen until someone is logged in
def logIn(accounts):
    current_user = None
    while current_user is None:
        current_user = initializeAccount(homeScreen(), accounts)
    return current_user


def main():
    print("Welcome to ATCS Twitter!")
    accounts = loadAccounts()
    current_user = logIn(accounts)

    # Main loop that the user experiences
    while True:
        choice = input("1. Add Friend  2. Log Out  3. Show Friends\n")
        if choice == "1":
            friend = input("Who do you want to add? ").strip()
            System.addFriend(current_user, friend, accounts)
        elif choice == "2":
            # This essentially serves as logging the user out
            current_user = logIn(accounts)
        elif choice == "3":
            accounts[current_user].showFriends()


if __name__ == "__main__":
    main()
