import DB_funcs as dbf
import sqlite3 as sql

""" DATABASE CLASS """

class DB:
    # init function sets the DB.
    def __init__(self):
        self.con = sql.connect("FEPDB.db")
        self.cursor = self.con.cursor()

        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (
        user_id TEXT PRIMARY KEY,
        user_name TEXT,
        password TEXT,
        first_name TEXT,
        last_name TEXT,
        registered_at TEXT
        );
        """)
        self.con.commit()

        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS tokens (
        token_id TEXT PRIMARY KEY,
        owner_id TEXT,
        value INTEGER,
        rate TEXT,
        production_date TEXT,
        FOREIGN KEY (owner_id) REFERENCES users (user_id)
        );
        """)
        self.con.commit()

        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS exchanges (
        exchange_id TEXT PRIMARY KEY,
        user_exchange_id TEXT,
        tokens TEXT,
        type TEXT,
        status TEXT,
        FOREIGN KEY (user_exchange_id) REFERENCES users (user_id)
        );
        """)
        self.con.commit()

        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS logs (
        log_id TEXT PRIMARY KEY,
        logged_user_id TEXT,
        logged_at TEXT,
        action TEXT,
        FOREIGN KEY (logged_user_id) REFERENCES users (user_id)
        )
        """)
        self.con.commit()

    # This function cuts the DB connection when the application is over
    def cut_connection(self):
        self.con.close()

    # This function inserts the registration information in to DB
    def register(self):
        user_info = dbf.produce_user() # produce_user function have explained in DB_funcs.py.
        user_id = user_info[0]
        user_name = user_info[1]
        password = user_info[2]
        first_name = user_info[3]
        last_name = user_info[4]
        registered_at = user_info[5]

        self.cursor.execute("""
        INSERT INTO users VALUES(?,?,?,?,?,?)
        """,(user_id, user_name, password, first_name, last_name, registered_at))
        self.con.commit()

    # Login function checks whether the user information is correct.
    def login(self,user_info:list):
        user_name = user_info[1]
        password = user_info[2]

        self.cursor.execute("""
        SELECT * FROM users WHERE user_name = ? AND password = ? 
        """, (user_name, password))
        pull = self.cursor.fetchall() # Users inputs their username and password.
                                      # The SQL checks is there any user with that information.

        if not pull: # If the SQL cannot find anything, we figure that user information is incorrect and return False.
            return False
        else:
            return pull # If the login is successful then function will return the user information

    # This function inserts the token information in to DB
    def create_token(self):
        token_info = dbf.produce_token() # produce_token function have explained in DB_funcs.py.
        token_id = token_info[0]
        owner_id = token_info[1]
        value = token_info[2]
        rate = token_info[3]
        production_date = token_info[4]

        self.cursor.execute("""
        INSERT INTO tokens VALUES(?,?,?,?,?)
        """,(token_id, owner_id, value, rate, production_date))
        self.con.commit()

    # This function inserts the exchange information in to DB
    def create_exchange(self):
        exchange_info = dbf.produce_exchange() # produce_exchange function have explained in DB_funcs.py.
        exchange_id = exchange_info[0]
        tokens = exchange_info[1]
        type = exchange_info[2]
        status = exchange_info[3]
        rate = exchange_info[4]
        production_date = exchange_info[5]

        self.cursor.execute("""
        INSERT INTO exchanges VALUES(?,?,?,?,?,?)
        """,(exchange_id, tokens, type, status, rate, production_date))
        self.con.commit()

    # This function inserts the log information in to DB
    def create_log(self):
        log_info = dbf.produce_log() # produce_log function have explained in DB_funcs.py.
        log_id = log_info[0]
        logged_user_id = log_info[1]
        logged_at = log_info[2]
        action = log_info[3]

        self.cursor.execute("""
        INSERT INTO logs VALUES(?,?,?,?)
        """,(log_id, logged_user_id,logged_at, action))
        self.con.commit()

    # Checks whether the id unique or not. It's generally can check every id that comes to it.
    # I didn't want to write them separately so there is another parameter in function.
    def isIdUnique(self,xxx_id,table_name):
        self.cursor.execute("""
        SELECT * FROM {} WHERE user_id = ?
        """.format(table_name),(xxx_id,))
        uniqueness = self.cursor.fetchall()

        if uniqueness:  # If there is an id that is same with the generated one, the function return False.
            return False
        else:
            return True

    def get_user_wallet(self,user_id):
        self.cursor.execute("""
        SELECT * FROM tokens WHERE owner_id = ?
        """, (user_id,))
        wallet_JSON = self.cursor.fetchall()
        # tokens stores as JSON. [({token1},{token2},{token3})] wallet will be like this.
        # To fix this I wrote the code below.

        wallet = list()
        for i in wallet_JSON[0]:
            wallet.append(i)     # With this code wallet will be like [{token1},{token2},{token3}], as I want.

        return wallet




DB_connection = DB()