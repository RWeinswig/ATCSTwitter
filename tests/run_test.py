import unittest
import pytest
from Run import checkLogIn
from Account import Account
from Run import validate_user_choice

def test_correct_check_login():
    my_account = Account("user1", "1234")
    accounts = {"user1": my_account}
    assert checkLogIn("user1", "1234", accounts) == True

def test_incorrect_check_login():
    my_account = Account("user1", "1234")
    accounts = {"user1": my_account}
    assert checkLogIn("user1", "12345", accounts) == False

def test_user_choice_correct_input():
    assert validate_user_choice("1") == 1
    assert validate_user_choice("2") == 2

def test_user_choice_incorrect_input_for_non_number():
    with pytest.raises(ValueError) as info:
        validate_user_choice("the")

    assert str(info.value) == "Please enter a number either 1 or 2! "

def test_user_choice_incorrect_input_for_wrong_number():
    with pytest.raises(ValueError) as info:
        validate_user_choice("3")

    assert str(info.value) == "Please enter an integer 1 or 2! "
    


    