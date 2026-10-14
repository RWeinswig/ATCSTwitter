# Programmers: Ryan Weinswig and Fletcher Cahill
# Date: October 14th, 2026

from datetime import datetime

class Post:
    # Initializes a post with a username, content, and an automatically generated timestamp
    def __init__(self, username, content):
        self.username = username
        self.content = content
        self.timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # Returns the post in dictionary form for JSON serialization
    def to_dict(self):
        return {
            "User": self.username,
            "Content": self.content,
            "Time stamp": self.timestamp
        }