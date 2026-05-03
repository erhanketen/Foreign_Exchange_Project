from Exchange.exchange import main_exn, get_exchange_rates
from Classes.User import User
from DataBase.DB import DataBase
from API.api import get_rates



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
            from_rate = input("Chose a Base Rate: ")
            rates_api = get_rates()
            rates = get_exchange_rates(rates_api,from_rate)
            for i in rates:
                print(i,rates[i],sep=" : ")
            to_rate = input("Chose a Target Rate: ")
            value = int(input("How Much Do Yo Want To Buy: "))

            exchange_info = \
                {
                "user_id": logged_user_id,
                "from": from_rate,
                "to": to_rate,
                "value": value
                }

            print("Exchanging...")
            exchange_st = main_exn(exchange_info)
            if exchange_st:
                print("Exchanging Done!")
            else:
                print("Exchanging cancelled!")

        elif choice == "2":
            iformation = DataBase.get_user_info(logged_user_id)
            print("""
USER INFO

Username: {}
Password: {}
            """.format(iformation["user_info"][0][1], iformation["user_info"][0][2]))
            print("\nWALLET INFO\n")
            for i in iformation["wallet_info"]:
                print(i,iformation["wallet_info"][i],sep=" : ")


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
            DataBase.close_connection()
            break

        elif choice == "1":
            username= input("Username: ")
            password = input("Password: ")
            new_user = User(username, password)

            print("Registering...")
            register = DataBase.register(new_user)
            if register == "AlreadyRegistered":
                print("Already Registered")
            else:
                print("Registered!")

        elif choice == "2":
            username= input("Username: ")
            password = input("Password: ")
            logged_user = User(username, password)

            print("Logging in...")
            logged_user_id = DataBase.login(logged_user)
            if not logged_user_id:
                print("Unable to log in!")
            else:
                print("Logged in!")
                logged(logged_user_id)

        else:
            print("Invalid choice!")


