# currency calculations
import locale # accepts commas in number inputs
import os
import time
from .currencies import usd_idr, usd_mxn, usd_php

# clear console
def clear_screen():
    # for Windows:
    if os.name == 'nt':
        _ = os.system('cls')
    else:
        _ = os.system('clear')

# forward conversion
def usd_to_other(symbol, current_rate, abbreviation):
    while True:
        amount = input(f"\nEnter the amount of USD to convert: $").strip()
        if amount.lower() == 'q':
            return False
        try:
            amount_convert = locale.atof(amount)
            amount_convert_value = locale.format_string("%.2f", amount_convert, grouping=True)
            fc_operation = amount_convert * current_rate
            fc_converted_value = locale.format_string("%.2f", fc_operation, grouping=True)
            print(f"\n${amount_convert_value} USD converts to {symbol}{fc_converted_value} {abbreviation}.\nEnter a new amount or enter 'q' to go back.")
        except ValueError:
            print("\nInvalid amount.")

# backward conversion
def other_to_usd(symbol, current_rate, abbreviation):
    while True:
        amount = input(f"\nEnter the amount of {abbreviation} to convert: {symbol}").strip()
        if amount.lower() == 'q':
            return False
        try:
            amount_convert = locale.atof(amount)
            amount_convert_value = locale.format_string("%.2f", amount_convert, grouping=True)
            bc_operation = amount_convert / current_rate
            bc_converted_value = locale.format_string("%.2f", bc_operation, grouping=True)
            print(f"\n{symbol}{amount_convert_value} {abbreviation} converts to ${bc_converted_value} USD.\nEnter a new amount or enter 'q' to go back.")
        except ValueError:
            print("\nInvalid amount.")

def sub_main(symbol, rate, abbreviation):
    while True:
        current_rate = rate
        print(f"\nCurrent rate is $1 USD to {symbol}{current_rate} {abbreviation}.")
        currency_operation = input(f"\nSelect conversion:\n1) USD -> {abbreviation}\n2) {abbreviation} -> USD\nQ) Go back\n\n: ")
        if currency_operation.lower() == 'q':
            return False
        # repeatable
        elif currency_operation == '1':
            usd_to_other(symbol, current_rate, abbreviation)
        elif currency_operation == '2':
            other_to_usd(symbol, current_rate, abbreviation)
        else:
            print('\nInvalid selection')


# main function
def main():
    print('\ninitializing...\n')

    # accepts commas as input
    locale.setlocale(locale.LC_ALL, "")

    # MAKE UPDATES HERE
    php_rate = float(locale.atof(usd_php.get_usd_php_rate()))
    print('PHP', end=', ', flush=True)
    mxn_rate = float(locale.atof(usd_mxn.get_usd_mxn_rate()))
    print('MXN', end=', ', flush=True)
    idr_rate = float(locale.atof(usd_idr.get_usd_idr_rate()))
    print('IDR', end=', ', flush=True)

    # MAKE UPDATES HERE
    currency_list = {
        '1': ('₱', php_rate, 'PHP'),
        '2': ('$', mxn_rate, 'MXN'),
        '3': ('Rp ', idr_rate, 'IDR'),
    }

    while True:
        clear_screen()
        choice_convert = input('Select currency:\n1) Filipino PHP\n2) Mexican MXN\n3) Indonesian IDR\n\nY) Add New Currency \nQ) Return to Main Menu\n\n: ')

        if choice_convert.lower() == 'q':
            return False
        # set currency to Filipino PHP
        elif choice_convert == '1':
            sub_main(*currency_list[choice_convert]) 
        # set currency to Mexican MXN
        elif choice_convert == '2':
            sub_main(*currency_list[choice_convert]) 
        # set currency to Indonesian IDR
        elif choice_convert == '3':
            sub_main(*currency_list[choice_convert]) 
        
        # add new currency
        elif choice_convert.lower() == 'y':
            clear_screen()
            print('Adding a new currency is currently disabled. Try again later. Returning to menu...')
            time.sleep(5)
        else:
            print('\nInvalid selection.')

if __name__ == '__main__':
    main()