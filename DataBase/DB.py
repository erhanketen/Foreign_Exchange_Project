import os
import sqlite3

class DB:
    def __init__(self):
        base_dir = os.path.dirname(os.path.abspath(__file__))
        db_path = os.path.join(base_dir, "FEP.db")

        self.start_connection(db_path)

    def start_connection(self,db_path):
        self.con = sqlite3.connect(db_path)
        self.cursor = self.con.cursor()

        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS User (
        user_id TEXT PRIMARY KEY,
        user_name TEXT,
        password TEXT )
        """)
        self.con.commit()

        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS Token (
        token_id TEXT PRIMARY KEY,
        token_rate TEXT,
        token_owner TEXT,
        value INTEGER,
        FOREIGN KEY (token_owner) REFERENCES User (user_id) )
        """)
        self.con.commit()

        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS pics (
        pic_path TEXT,
        pic_user_id TEXT,
        state TEXT DEFAULT 'Default',
        FOREIGN KEY (pic_user_id) REFERENCES User (user_id) 
        )
        """)
        self.con.commit()

    def close_connection(self):
        self.con.close()

    def get_wallet(self,user_id):
        self.cursor.execute("SELECT * FROM Token WHERE token_owner = ?",(user_id,))
        wallet = self.cursor.fetchall()
        tokens = []

        while wallet:
            token = {}
            tokenize = wallet.pop()

            token["token_id"] = tokenize[0]
            token["token_rate"] = tokenize[1]
            token["token_owner"] = tokenize[2]
            token["value"] = tokenize[3]

            tokens.append(token)

        return tokens

    def rm_token(self,token_id):
        self.cursor.execute("""
        DELETE FROM Token WHERE token_id = ?
        """,(token_id,))
        self.con.commit()

    def update_wallet(self,wallet,user_id):
        for i in wallet:
            self.cursor.execute("""
            UPDATE Token SET value = ? WHERE token_id = ? AND token_owner = ?
            """,(i["value"],i["token_id"],user_id))
            self.con.commit()

    def add_token(self,token):
        self.cursor.execute("""
        INSERT INTO Token (token_id,token_rate,token_owner,value) VALUES (?,?,?,?)
        """,(token["token_id"],token["token_rate"],token["token_owner"],token["value"]))
        self.con.commit()

    def register(self,user_obj):
        user_id = user_obj.user_id
        user_name = user_obj.user_name
        user_password = user_obj.user_password

        self.cursor.execute("""
        SELECT * FROM User WHERE user_name = ?
        """,(user_name,))
        user = self.cursor.fetchall()

        if user:
            return "AlreadyRegistered"
        else:
            self.cursor.execute("""
            INSERT INTO User (user_id,user_name,password) VALUES (?,?,?)
            """,(user_id,user_name,user_password))
            self.con.commit()
            return "Registered"

    def login(self,user):
        user_name = user.user_name
        user_password = user.user_password

        self.cursor.execute("""
        SELECT * FROM User WHERE user_name = ? AND password = ?
        """,(user_name,user_password))
        user = self.cursor.fetchall()

        if user:
            return user[0][0]
        else:
            return False

    def get_user_info(self,user_id):
        self.cursor.execute("""
        SELECT * FROM User WHERE user_id = ?
        """,(user_id,))
        user = self.cursor.fetchall()

        tokens = self.get_wallet(user_id)
        wallet = {}

        if not tokens:
            return {"user_info":user,"wallet_info":{"EUR":0}}

        for i in tokens:
            value = i["value"]
            if not (i["token_rate"] in wallet):
                wallet[i["token_rate"]] = value
            else:
                wallet[i["token_rate"]] += value

        information = {"user_info":user,"wallet_info":wallet}
        return information

    def get_pp(self,user_id):
        self.cursor.execute("""
        SELECT * FROM Pics WHERE pic_user_id = ?
        """,(user_id,))
        pic = self.cursor.fetchall()

        picture = dict()

        picture["pp_path"] = pic[0][0]
        picture["pp_user_id"] = pic[0][1]
        picture["state"] = pic[0][2]

        return picture

    def add_default_pp(self,user_id):
        self.cursor.execute("""
        INSERT INTO Pics (pic_user_id) VALUES (?)
        """,(user_id,))
        self.con.commit()

    def change_profile_photo(self,user_id,path):
        self.cursor.execute("""
        UPDATE pics SET pic_path = ? WHERE pic_user_id = ?
        """,(path,user_id))
        self.con.commit()

        self.cursor.execute("""
        UPDATE pics SET state = 'Changed' WHERE pic_user_id = ?
        """,(user_id,))
        self.con.commit()


DataBase = DB()