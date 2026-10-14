from datetime import datetime


class Post:
    def __init__(self, username, content):
        self.username = username
        self.content = content
        self.timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    #returns the post in its form
    def to_dict(self):
        return {
            "User": self.username,
            "Content": self.content,
            "Time stamp": self.timestamp
        }