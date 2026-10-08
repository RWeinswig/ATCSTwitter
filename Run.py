from System import loadAccounts
from System import createAccount


def main():
    accounts = loadAccounts()
    createAccount(accounts)


if __name__ == "__main__":
    main()
