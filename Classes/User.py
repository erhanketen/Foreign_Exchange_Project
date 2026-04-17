import uuid

class User:
    def __init__(self, user_name, user_password):
        self.user_id = str(uuid.uuid4())
        self.user_name = user_name
        self.user_password = user_password


