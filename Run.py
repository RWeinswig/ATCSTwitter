from System import loadAccounts
from System import createAccount
from System import checkIfPasswordIsRight
from System import checkIfUserNameIsRight

def notAPossibleOption(exception):
    pass

'''
Will add comments later: wanted to get the code in. If you have any questions, please let me know
'''

def enterAnInput():
    inputOfUser = int(input("Choose an option: \n 1. Create an account \n 2. Log In to your Account\n"))
    return inputOfUser

def main():
    accounts = loadAccounts()
    while True:
        try:
            userChoice = enterAnInput()

            if (userChoice not in (1,2)):
                raise notAPossibleOption("Please enter a number either 1 or 2. ")
            
            break
        except ValueError:
            print("Please enter a number either 1 or 2. ")
        except notAPossibleOption as e:
            print(f"{e} \n")
       

    if (userChoice == 1):
        createAccount(accounts)
    else:
        username = input("Username: ")
        password = input("Password: ")
        if (checkIfPasswordIsRight(username, password, accounts)):
            print("Log In is possible")
        else:
            print("Log in is not possible")


if __name__ == "__main__":
    main()
