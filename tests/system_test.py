import pytest
from System import checkIfUserNameIsRight
from Account import Account
from System import checkIfPasswordIsRight


def test_username_correct():
    accounts = {"user1": "1234"}
    assert checkIfUserNameIsRight("user1", accounts) == True


def test_username_incorrect():
    accounts = {"user1": "1234"}
    assert checkIfUserNameIsRight("user2", accounts) == False

def test_password_correct():
    my_account = Account("user1", "1234")
    accounts = {"user1": my_account}
    assert checkIfPasswordIsRight("user1", "1234", accounts) == True

def test_password_incorrect():
    my_account = Account("user1", "1234")
    accounts = {"user1": my_account}
    assert checkIfPasswordIsRight("user1", "12345", accounts) == False

