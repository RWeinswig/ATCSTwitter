from System import loadAccounts
from System import createAccount


def main():
    print ("Welcome to ATCS Twitter!")
    accounts = loadAccounts()
    """
    try: 
        initial_action = int(input("Options **** 1. Login 2. Create Account\n"))
    except ValueError:
        while True:
            try:
                initial_action = int(input("Please enter an integer 1-2: 1. Login 2. Create Account\n"))
                break
            except ValueError:
                continue

    if initial_action == 1:
        print("Login")
    else:
        print("Create Account")
        createAccount(accounts)
    """
    # Assuming that login and create account checking alr exists
    while current_user is not None:
        choice = input("1. Add Friend  2. Log Out\n")
        if choice == "1":
            addFriend(current_user, accounts)
        elif choice == "2":
            current_user = None

if __name__ == "__main__":
    main()
