import os
import sys
# Lets this file find the project modules when run directly (not just via pytest)
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import unittest
import pytest
from Run import checkLogIn
from Account import Account
from Run import validate_user_choice
from System import System
from Post import Post

# Checks if log in actually works
def test_correct_check_login():
    my_account = Account("user1", "1234")
    accounts = {"user1": my_account}
    assert checkLogIn("user1", "1234", accounts) == True

# Makes sure that logIn isn't always correct
def test_incorrect_check_login():
    my_account = Account("user1", "1234")
    accounts = {"user1": my_account}
    assert checkLogIn("user1", "12345", accounts) == False

# Checks to see what happens with program when user inputted correct result
def test_user_choice_correct_input():
    assert validate_user_choice("1") == 1
    assert validate_user_choice("2") == 2

# Checks to see that correct error message for when they put in a string
def test_user_choice_incorrect_input_for_non_number():
    with pytest.raises(ValueError) as info:
        validate_user_choice("the")

    assert str(info.value) == "Please enter a number either 1 or 2! "

# Checks to see that correct error message when they put in a number other than 1 or 2
def test_user_choice_incorrect_input_for_wrong_number():
    with pytest.raises(ValueError) as info:
        validate_user_choice("3")

    assert str(info.value) == "Please enter an integer 1 or 2! "

# Checks that alreadyFriends detects a friend who has already been added
def test_friend_already_exists():
    account = Account("juan", "12345678", ["fletcher"])
    assert account.alreadyFriends("fletcher") == True
    assert account.alreadyFriends("ryan w") == False
# Tests if adding an invalid friend fails
def test_adding_invalid_friend():
    accounts = {"juan": Account("juan", "12345678", ["fletcher"])}
    assert System.addFriend("juan", "jacob", accounts) == False   # jacob doesn't exist

# This essentially tests the logout feature because the feature just prompts you to login as someone else
def test_logout():
    accounts = {
        "user1": Account("user1", "1234"),
        "user2": Account("user2", "5678")
    }
    assert checkLogIn("user2", "5678", accounts) == True

# Checks that browsing posts only shows posts from friends
def test_view_friends_posts():
    friend_post = Post("fletcher", "hello").to_dict()
    stranger_post = Post("jacob", "hi").to_dict()
    accounts = {
        "juan": Account("juan", "12345678", ["fletcher"]),
        "fletcher": Account("fletcher", "12345678", [], [friend_post]),
        "jacob": Account("jacob", "12345678", [], [stranger_post])
    }
    assert System.viewPosts("juan", accounts) == [friend_post]

if __name__ == "__main__":
    sys.exit(pytest.main([__file__]))
