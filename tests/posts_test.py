import os
import sys
import unittest
from datetime import datetime

# Adds the project root directory to sys.path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from Post import Post


class TestPost(unittest.TestCase):

    def setUp(self):
        # Set up a sample post instance before each test.
        self.username = "test_user"
        self.content = "Hello world! This is my first post."
        self.post = Post(self.username, self.content)

    def test_post_initialization(self):
        # Test that a Post object initializes attributes correctly.
        self.assertEqual(self.post.username, "test_user")
        self.assertEqual(self.post.content, "Hello world! This is my first post.")
        
        # Verify timestamp is formatted correctly (YYYY-MM-DD HH:MM:SS)
        try:
            datetime.strptime(self.post.timestamp, "%Y-%m-%d %H:%M:%S")
        except ValueError:
            self.fail("Post timestamp is not in the expected '%Y-%m-%d %H:%M:%S' format.")

    def test_to_dict(self):
        # Test that to_dict returns the expected dictionary representation.
        post_dict = self.post.to_dict()

        self.assertIsInstance(post_dict, dict)
        self.assertEqual(post_dict["User"], "test_user")
        self.assertEqual(post_dict["Content"], "Hello world! This is my first post.")
        self.assertEqual(post_dict["Time stamp"], self.post.timestamp)


if __name__ == "__main__":
    unittest.main()