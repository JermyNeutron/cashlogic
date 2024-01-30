import locale # accepts commas in number inputs
from currencies import usd_idr, usd_mxn, usd_php
import os

# accepts commas as input
locale.setlocale(locale.LC_ALL, "")

currency_list = {
    '1': ('₱', usd_php.get_usd_php_rate, 'pesos'),
    '2': ('$', usd_mxn.get_usd_mxn_rate, 'pesos'),
    '3': ('Rp', usd_idr.get_usd_idr_rate, 'rupiahs')
}

def sub_main(symbol, rate, title):
    pass

# forward conversion
def usd_to_other(amount, forex):
    operation = amount * forex
    converted_value = locale.format_string("%.2f", operation, grouping=True)

# backward conversion
def other_to_usd(amount, forex):
    pass

# main function
def main():
    while True:
        choice_convert = input('\nSelect currency:\n1) PHP\n2) MXN\n3) IDR\nQ) Go back\n\n: ')



        if choice_convert == 'q':
            return False
        # set currency to Filipino PHP
        elif choice_convert == '1':
            sub_main(*choice_convert) 
        elif choice_convert == '2':
            sub_main(*choice_convert) 
        elif choice_convert == '3':
            sub_main(*choice_convert) 


        # set currency to Mexican MXN
        # set currency to Indonesian IDR