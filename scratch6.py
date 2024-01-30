# currency calculations
import locale # accepts commas in number inputs
from currencies import usd_idr, usd_mxn, usd_php

# accepts commas as input
locale.setlocale(locale.LC_ALL, "")

php_rate = float(locale.atof(usd_php.get_usd_php_rate()))
mxn_rate = float(locale.atof(usd_mxn.get_usd_mxn_rate()))
idr_rate = float(locale.atof(usd_idr.get_usd_idr_rate()))

currency_list = {
    '1': ('₱', php_rate, 'PHP'),
    '2': ('$', mxn_rate, 'MXN'),
    '3': ('Rp ', idr_rate, 'IDR'),
}

# forward conversion
def usd_to_other(symbol, current_rate, abbreviation):
    while True:
        amount = input(f"\nEnter the amount of USD to convert: $").strip()
        if amount.lower() == 'q':
            return False
        try:
            amount_convert = locale.atof(amount)
            fc_operation = amount_convert * current_rate
            fc_converted_value = locale.format_string("%.2f", fc_operation, grouping=True)
            print(f"\n${amount_convert} USD converts to {symbol}{fc_converted_value} {abbreviation}.\nEnter a new amount or enter 'q' to go back\n\n")
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
            bc_operation = amount_convert / current_rate
            bc_converted_value = locale.format_string("%.2f", bc_operation, grouping=True)
            print(f"\n{symbol}{amount_convert} {abbreviation} converts to ${bc_converted_value} USD.\nEnter a new amount or enter 'q' to go back\n\n")
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
        else:
            print('Invalid selection.')

if __name__ == '__main__':
    main()