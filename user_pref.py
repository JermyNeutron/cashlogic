import sqlite3
from database import create_table, insert_config, get_config

def enable_php_parameter(cursor):
    insert_config(cursor, 'am_bookmarked_usd_php', 'enabled')
    print('PHP parameter enabled.')
    status = get_config(cursor, 'am_bookmarked_usd_php')
    print(f'Status after: {status}')

def disable_php_parameter(cursor):
    insert_config(cursor, 'am_bookmarked_usd_php', 'disabled')
    print('PHP parameter disabled.')
    status = get_config(cursor, 'am_bookmarked_usd_php')
    print(f'Status after: {status}')

def user_parameters(cursor):
    while True:
        print("""Parameters:
1) PHP
Q) Go back
              """)
        
        parameter_choice = input(': ')

        if parameter_choice.lower() == 'q':
            return False
        elif parameter_choice == '1':
            # Sub-menu for PHP
            # create menu if one does not exist
            print("""Choose an action:
Y) Enable,
N) Disable,
Q) Go back
                  """)
            action_choice = input(': ')

            if action_choice.lower() == 'q':
                return False
            elif action_choice.lower() == 'y':
                # enable PHP parameter
                enable_php_parameter(cursor)
            elif action_choice.lower() == 'n':
                # enable PHP parameter
                disable_php_parameter(cursor)
            else:
                print('\nInvalid choice. Choose again.')
        else:
            print('\nInvalid choice. Choose again.')

if __name__ == '__main__':
    conn = sqlite3.connect('scratchdb1.db')
    cursor = conn.cursor()

    create_table(cursor)

    insert_config(cursor, 'am_bookmarked_usd_php', 'enabled')

    user_parameters(cursor)