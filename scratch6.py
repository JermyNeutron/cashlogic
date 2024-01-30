# currency calculations
import locale # accepts commas in number inputs
from currencies import usd_idr, usd_mxn, usd_php
import os

# accepts commas as input
locale.setlocale(locale.LC_ALL, "")

currency_list = {
    '1': ('1', '₱', usd_php.get_usd_php_rate, 'PHP'),
    '2': ('2', '$', usd_mxn.get_usd_mxn_rate, 'MXN'),
    '3': ('3', 'Rp', usd_idr.get_usd_idr_rate, 'IDR'),
}

# forward conversion
def usd_to_other(symbol, current_rate, abbreviation):
    while True:
        amount = input(f"\nEnter the amount of USD to convert: $")
        if amount == 'q':
            return False
        else:
            amount_convert = locale.atof(amount)
            fc_operation = amount_convert * current_rate
            fc_converted_value = locale.format_string("%.2f", fc_operation, grouping=True)
            print(f"\n${amount_convert} USD converts to {symbol}{fc_converted_value} {abbreviation}.\nEnter a new amount or enter 'q' to go back\n\n")

# backward conversion
def other_to_usd(symbol, current_rate, abbreviation):
    while True:
        amount = input(f"\nEnter the amount of {abbreviation} to convert: {symbol}")
        if amount == 'q':
            return False
        else:
            amount_convert = locale.atof(amount)
            bc_operation = amount_convert / current_rate
            bc_converted_value = locale.format_string("%.2f", bc_operation, grouping=True)
            print(f"\n{symbol}{amount_convert} converts to ${bc_converted_value} USD.\nEnter a new amount or enter 'q' to go back\n\n")

def sub_main(key, symbol, rate, abbreviation):
    while True:
        current_rate = currency_list[key][2]()
        print(f"Current rate is $1 USD to {symbol}{current_rate} {abbreviation}.")
        currency_operation = input(f"\nSelect conversion:\n1) USD -> {abbreviation}\n2) {abbreviation} -> USD\nQ) Go back\n\n: ")
        if currency_operation == 'q':
            return False
        # repeatable
        elif currency_operation == '1':
            usd_to_other(symbol, current_rate, abbreviation)
        elif currency_operation == '2':
            other_to_usd(symbol, current_rate, abbreviation)
        else:
            print('Invalid selection')


# main function
def main():
    while True:
        choice_convert = input('\nSelect currency:\n1) PHP\n2) MXN\n3) IDR\nQ) Go back\n\n: ')

        if choice_convert == 'q':
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

main()