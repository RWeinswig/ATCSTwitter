# Programmers: Ryan Weinswig and Fletcher Cahill
# Date: October 14th, 2026

import os
import sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import pytest
from Account import Account
from System import System
from Post import Post

# Tests that a user cannot add themselves as a friend
def test_add_self_friend():
    accounts = {"ryan": Account("ryan", "12345678")}
    assert System.addFriend("ryan", "ryan", accounts) == False

# Tests that adding a non-existent friend fails properly
def test_add_nonexistent_friend():
    accounts = {"ryan": Account("ryan", "12345678")}
    assert System.addFriend("ryan", "ghost_user", accounts) == False

# Tests that a post initializes with the correct attributes and dictionary format
def test_post_creation_fields():
    post = Post("fletcher", "Learning Python is awesome!")
    assert post.username == "fletcher"
    assert post.content == "Learning Python is awesome!"
    post_dict = post.to_dict()
    assert post_dict["User"] == "fletcher"
    assert post_dict["Content"] == "Learning Python is awesome!"
    assert "Time stamp" in post_dict

# Tests that checking an invalid username returns False correctly
def test_check_invalid_username_edge_case():
    accounts = {"ryan": Account("ryan", "12345678")}
    assert System.checkIfUserNameIsRight("nonexistent", accounts) == False

if __name__ == "__main__":
    sys.exit(pytest.main([__file__]))