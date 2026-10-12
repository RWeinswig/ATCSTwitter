from System import loadAccounts
from System import createAccount
from System import checkIfPasswordIsRight
from System import System
from Account import *

'''
Will add comments later: wanted to get the code in. If you have any questions, please let me know
'''


def validate_user_choice(choice_str):
    try:
        choice = int(choice_str)
        # Fixes bug that didn't turn input into an integer
        if (choice not in (1,2)):
            raise ValueError("Please enter an integer 1 or 2! ")
        return choice
    except ValueError as e:

        if "Please enter" in str(e):
            raise

        raise ValueError("Please enter a number either 1 or 2! ")
    
        

def enterAnInputToLogIn():
    inputOfUser = input("Choose an option: \n 1. Create an account \n 2. Log In to your Account\n")
    return inputOfUser

def main():
    print ("Welcome to ATCS Twitter!")
    accounts = loadAccounts()

    
    while True:
        try:
            userInput = enterAnInputToLogIn()
            userInput = validate_user_choice(userInput)
            break
        except ValueError as e:
            print(f"{e}\n")

    # Initializes the state of the current user
    current_user = None
    if (userInput == 1):
        createAccount(accounts)
    else:
        
        username = input("Username: ")
        password = input("Password: ")
        if checkLogIn(username, password, accounts):
            current_user = username

    # Main loop that the user experiences
    while current_user is not None:
        choice = input("1. Add Friend  2. Log Out 3. Show Friends \n")
        if choice == "1":
            friend = input("Who do you want to add? ").strip()
            System.addFriend(current_user, friend, accounts)
        elif choice == "2":
            current_user = None
        elif choice == "3":
            accounts[current_user].showFriends()


def checkLogIn(username, password, accounts):
    if (checkIfPasswordIsRight(username, password, accounts)):
        print("Log In is possible")
        return True
    else:
        print("Log in is not possible")
        return False

if __name__ == "__main__":
    main()
