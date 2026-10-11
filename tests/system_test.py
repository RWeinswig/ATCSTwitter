import pytest
from System import checkIfUserNameIsRight
from Account import Account
from System import checkIfPasswordIsRight



# Checks to ensure that we correctly determine that the username exists
def test_username_correct():
    accounts = {"user1": "1234"}
    assert checkIfUserNameIsRight("user1", accounts) == True

# Checks to make sure that checkUsername returns false when the username doesn't exist
def test_username_incorrect():
    accounts = {"user1": "1234"}
    assert checkIfUserNameIsRight("user2", accounts) == False

# Checks to make sure that the check_password works when the password matches with the username
def test_password_correct():
    my_account = Account("user1", "1234")
    accounts = {"user1": my_account}
    assert checkIfPasswordIsRight("user1", "1234", accounts) == True

# Checks to make sure that when the username exists and the password doesn't match, that it returns false
def test_password_incorrect():
    my_account = Account("user1", "1234")
    accounts = {"user1": my_account}
    assert checkIfPasswordIsRight("user1", "12345", accounts) == False

# Checks to make sure that when the username doesn't exist but tge password does, it still returns false
def test_check_password_but_username_incorrect():
    my_account = Account("user1", "1234")
    accounts = {"user1": my_account}
    assert checkIfPasswordIsRight("user2", "1234", accounts) == False
