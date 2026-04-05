import app.users.User as User
import app.logs.Logs as Logs
import app.exchanges.Exchanges as Ex

""" DATABASE FUNCTIONS """

# Creates a new user object and returns the user information.
def produce_user(user_input): # User input comes from the UI.
    username = user_input[0]
    password = user_input[1]
    firstname = user_input[2]
    lastname = user_input[3]

    new_user = User.User(username = username, password = password, firstname = firstname, lastname = lastname)

    return new_user.get_user_info()

# Creates a new token and returns it as JSON format.
def produce_token():
    pass

# Creates a new exchange object and returns the exchange information.
def produce_exchange(exchange_input):
    exchange_user_id = exchange_input[0]
    tokens = exchange_input[1]
    rate_to_rate = exchange_input[3]
    value = exchange_input[4]

    new_exchange = Ex.Exchanges(exchange_user_id=exchange_user_id, tokens=tokens,rate_to_rate=rate_to_rate, value = value)

    return new_exchange.get_exchange_info()

# Creates a new log object and returns the log information.
def produce_log(log_input): # this argument comes from the UI.
    log_user_id = log_input[0]
    action = log_input[1]

    new_log = Logs.Logs(log_user_id = log_user_id, action = action)

    return new_log.get_log_info()


