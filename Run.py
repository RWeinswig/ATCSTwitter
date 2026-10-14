# Programmers: Ryan Weinswig and Fletcher Cahill
# Date: October 14th, 2026

from System import System, loadAccounts, createPost

# Turns the user's menu input into 1 or 2, raising a ValueError with a helpful message otherwise
def validate_user_choice(choice_str):
    try:
        choice = int(choice_str)
        # Fixes bug that didn't turn input into an integer
        if choice not in (1, 2):
            raise ValueError("Please enter an integer 1 or 2! ")
        return choice
    except ValueError as e:
        if "Please enter" in str(e):
            raise
        raise ValueError("Please enter a number either 1 or 2! ")


# First things the user sees
def homeScreen():
    while True:
        try:
            return validate_user_choice(input("Choose an option: \n 1. Create an account \n 2. Log In to your Account\n"))
        except ValueError as e:
            print(f"{e}\n")


# Verifies a correct login given a username and a password
def checkLogIn(username, password, accounts):
    if System.checkIfPasswordIsRight(username, password, accounts):
        print("Log In is possible")
        return True
    else:
        print("Log in is not possible")
        return False


# Creates an account or logs in based on the user's choice
# Returns the username of the logged-in user, or None if logging in failed
def initializeAccount(user_input, accounts):
    if user_input == 1:
        return System.createAccount(accounts).username
    username = input("Username: ")
    password = input("Password: ")
    if checkLogIn(username, password, accounts):
        return username
    return None


# Keeps going back to the home screen until someone is logged in
def logIn(accounts):
    current_user = None
    # Goes through process of either having the user create an account or login
    while current_user is None:
        current_user = initializeAccount(homeScreen(), accounts)
    return current_user


# Main loop that the user experiences 
def main():
    print("Welcome to ATCS Twitter!")
    accounts = loadAccounts()
    current_user = logIn(accounts)

    # Main loop that the user experiences
    while True:
        choice = input("1. Add Friend  2. Log Out  3. Show Friends  4. Browse Friends' Posts  5. Create a post \n")
        if choice == "1":
            friend = input("Who do you want to add? ").strip()
            System.addFriend(current_user, friend, accounts)
        elif choice == "2":
            # This essentially serves as logging the user out
            current_user = logIn(accounts)
        elif choice == "3":
            accounts[current_user].showFriends()
        elif choice == "4":
            System.viewPosts(current_user, accounts)
        elif choice == "5":
            createPost(current_user, accounts)


if __name__ == "__main__":
    main()