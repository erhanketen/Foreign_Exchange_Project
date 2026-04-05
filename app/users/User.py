import datetime
import User_funcs as uf

""" USER CLASS """

class User:
    # init function generates whether the new user information or a user that logged in.
    def __init__(self,username:str,password:str,firstname:str,lastname:str):
        self.user_id = uf.generate_user_id() # Here the function generates a user id. In User_funcs, the function is detailed.
        self.username = username
        self.password = password
        self.firstname = firstname
        self.lastname = lastname
        self.registered_at = datetime.datetime.now()

    # When application needs the user information this function get called.
    def get_user_info(self):
        return [self.user_id,self.username,self.password,self.firstname,self.lastname,self.registered_at]

    # When an exchanging were proceeding the user wallet would be needed. This function gets the tokens of the user
    def get_user_wallet(self):
        tokens = uf.get_tokens(self.user_id) # In User_funcs, the function is detailed. It connects the function to DB.
        return tokens



