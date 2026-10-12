from datetime import datetime

class Post:

    def __init__(self):
        pass

    def createPost(username):
        userPost = input("What would you like to post: ")
        
        now = datetime.now()
        current_time = now.strftime("%H:%M:%S")
        post = {"Time stamp": current_time, "User": username}
        return post


