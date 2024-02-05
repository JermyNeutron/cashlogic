# Payment Plans

import locale
import os
# import time
import girlmath

def clear_screen():
    if os.name == 'nt':
        _ = os.system('cls')
    else:
        _ = os.system('clear')

# Divide a cost over 6 months
def paypal_6mo(set_tax=0.09):
    locale.setlocale(locale.LC_ALL, "")
    while True:
        tax_estimated = set_tax
        amount = input(f"\nEnter the cost you'd like to breakdown in 6 months:\n\n: $").strip()
        if amount.lower() == 'q':
            return False
        try:
            operation_base = locale.atof(amount) / 6
            operation_base_formatted = locale.format_string("%.2f", operation_base, grouping=True)
            operation_w_tax = operation_base * (1 + tax_estimated)
            operation_w_tax_formatted = locale.format_string("%.2f", operation_w_tax, grouping=True)
            print(f"""
Expect 6 monthly payments:     ${operation_base_formatted}.
With an estimated tax of {tax_estimated * 100}%: ${operation_w_tax_formatted}.

Enter a new amount or enter 'q' to go back.""")
        except ValueError:
            print("\nInvalid amount.")

# Divide a cost over 4 payments made every 15 days
def fourpayments(set_tax=0.09):
    locale.setlocale(locale.LC_ALL, "")
    while True:
        tax_estimated = set_tax
        amount = input(f"\nEnter the cost you'd like to breakdown in 4 payments:\n\n: $").strip()
        if amount.lower() == 'q':
            return False
        try:
            operation_base = locale.atof(amount) / 4
            operation_base_formatted = locale.format_string("%.2f", operation_base, grouping=True)
            operation_w_tax = operation_base * (1 + tax_estimated)
            operation_w_tax_formatted = locale.format_string("%.2f", operation_w_tax, grouping=True)
            print(f"""
Expect 4 equal payments:       ${operation_base_formatted}.
With an estimated tax of {tax_estimated * 100}%: ${operation_w_tax_formatted}.

Enter a new amount or enter 'q' to go back.""")
        except ValueError:
            print('\nInvalid amount.')

# Run program
def main():
    while True:
        clear_screen()
        print("PAYMENT PLANS")
        choice = input("\nWhich payment plan are we using?\n1) Paypal | 6 Months with 0%\n2) Paypal | 4 Payments over 6 Weeks\n3) Girl Math \nQ) Return to Main Menu\n\n: ")

        if choice == 'q':
            return False
        elif choice == '1':
            paypal_6mo()
        elif choice == '2':
            fourpayments()

            # UPDATE, temporary solution
        elif choice == '3':
            girlmath.main()
        else:
            print('\nInvalid choice.')

# testing purposes
if __name__ == '__main__':
    main()