import random
import app.DB.DB as db

""" LOG FUNCTIONS """

# Generates a log_id
def generate_log_id():
    num = random.randint(100_000_000,999_999_999)
    log_id = "log_"+str(num)

    while True:
        if isLogIdUnique(log_id):
            return log_id

# checks if log id unique or not.
def isLogIdUnique(log_id):
    if db.DB_connection.isIdUnique(log_id,"logs"):
        return True
    else:
        return False






