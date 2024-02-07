# working main_test

from functions import currency_calculations, paymentplans
from functions.currencies import usd_php
from functions.database import create_table, insert_config, get_config # database.py
import sqlite3
import functions.user_pref as user_pref
import os

def clear_screen():
    if os.name == 'nt':
        _ = os.system('cls')
    else:
        _ = os.system('clear')

options = {
    '1': currency_calculations.main,
    '2': paymentplans.main,
}

# PHP bookmark
def am_bookmarked_usd_php(cursor):
    status = get_config(cursor, 'am_bookmarked_usd_php')
    if status == 'enabled':
        usd_php.am_bookmarked()
    print(f'Status after: {status}')

# main
def main():
    print("Welcome!")
    
    # connect to SQLite database
    conn = sqlite3.connect('database/user_pref.db')
    cursor = conn.cursor()

    # create table if one does not exist
    create_table(cursor)

    # bookmark statements
    am_bookmarked_usd_php(cursor)

    #enable or disable the am_bookmarked function in usd_php
    # insert_config(cursor, 'am_bookmarked_usd_php', 'enabled') # or 'disabled'

    # # call function
    # user_pref.user_parameters(cursor)

    while True:
        print("""
What's your response?
1) Convert Currencies
2) Payment Plans
Y) Parameters
Q) Exit
        """)
        choice = input(": ")


        if choice.lower() == "q":
            print("\nexiting...")
            break
        elif choice.lower() == 'y':
            user_pref.user_parameters(cursor)
        elif choice in options:
            options[choice]()
        else:
            print("\nInvalid choice. choose again")

        clear_screen()

    conn.commit()
    conn.close()
    print('goodbye')

if __name__ == '__main__':
    main()
