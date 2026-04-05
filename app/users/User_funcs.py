import app.DB.DB as db
import random

""" USER FUNCTIONS """

""" 
This module is for connect the User class to the DB. 
The class file and the funcs are separate to make it more clear.
But there is lots of function that is connects to each other and maybe this might the program be more slow.
"""

# This function generates a unique user id.
def generate_user_id():
    num = random.randint(100_000_000, 999_999_999) # The method is strange, but I like to use this.
    user_id = "user_" + str(num)

    while True:
        if isUserIdUnique(user_id): # Checks the DB for is there any other user id same with the function generated.
            return user_id
        else:
            continue

def isUserIdUnique(user_id):
    if db.DB_connection.isIdUnique(user_id,"users"):
        return True
    else:
        return False

# Function goes to DB and gets the tokens that belongs to user.
def get_tokens(user_id):
    wallet = db.DB_connection.get_user_wallet(user_id)
    return wallet

