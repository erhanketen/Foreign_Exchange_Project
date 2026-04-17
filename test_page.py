import Classes, DataBase, Exchange

def logged(logged_user_id):
    print("""
-------------------------------

           WELCOME 

-------------------------------
    """)
    while True:
        print("""
ACTİONS
(0) Log Out
(1) Exchange
(2) See Your Wallet
        """)
        choice = input("-->")

        if choice == "0":
            print("Logging out...")
            break
        elif choice == "1":
            from_rate = input("From Rate: ")
            to_rate = input("To Rate: ")
            value = input("Value: ")

            exchange_info = \
                {
                "user_id": logged_user_id,
                "from": from_rate,
                "to": to_rate,
                "value": value
                }

            print("Exchanging...")
            Exchange.exchange.main(exchange_info)
            print("Exchanging Done!")

        elif choice == "2":
            DataBase.DB_connection.DataBase.get_user_info(logged_user_id)


def main():
    print("""
-------------------------------
    
    FOREİGN EXCHANGE PROGRAM
    
-------------------------------
    """)

    while True:
        print("""
ACTİONS
(0) Quit
(1) Register
(2) Login
        """)

        choice = input("-->")

        if choice == "0":
            print("Shutting down...")
            break

        elif choice == "1":
            username= input("Username: ")
            password = input("Password: ")
            new_user = Classes.User.User(username, password)

            print("Registering...")
            register = DataBase.DB_connection.DataBase.register(new_user)
            if register == "Already Registered":
                print("Already Registered")
            else:
                print("Registered!")

        elif choice == "2":
            username= input("Username: ")
            password = input("Password: ")
            logged_user = Classes.User.User(username, password)

            print("Logging in...")
            logged_user_id = DataBase.DB_connection.DataBase.login(logged_user)
            if not logged_user_id:
                print("Unable to log in!")
            else:
                print("Logged in!")
                logged(logged_user_id)

        else:
            print("Invalid choice!")


