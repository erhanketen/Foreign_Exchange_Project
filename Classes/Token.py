import uuid

class Token:
    def __init__(self,token_rate,value,token_owner):
        self.token_id = str(uuid.uuid4())
        self.token_rate = token_rate
        self.token_owner = token_owner
        self.value = value

        self.token = \
            {
            "token_id":self.token_id,
            "token_rate":self.token_rate,
            "value":self.value,
            "token_owner":self.token_owner,
            }


