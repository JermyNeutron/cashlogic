# currency calculations
import locale  # accepts commas in number inputs
from currencies import usd_php
import os

# everything I guess I'd wanna know
#  PHP

locale.setlocale(locale.LC_ALL, "")

current_usdphp_rate = usd_php.get_usd_php_rate()


def convert():
    while True:
        choice_convert = input(
            "\nHow would you like to convert?\n1. USD -> PHP\n2. PHP -> USD\nq) Go back\n\n: "
        )
        if choice_convert == "q":
            return False
        elif choice_convert == "1":
            amount_convert = input("\nEnter the amount of USD to convert: $")
            choice_value = locale.atof(amount_convert)
            operation = choice_value * current_usdphp_rate
            converted_value = locale.format_string("%.2f", operation, grouping=True)
            # return f"\n${amount_convert} converts to ₱{converted_value}.", True
            print(f"\n${amount_convert} converts to ₱{converted_value}.")
            continue
        elif choice_convert == "2":
            amount_convert = input("\nEnter the amount of PHP to convert: ₱")
            choice_value = locale.atof(amount_convert)
            operation = choice_value / current_usdphp_rate
            converted_value = locale.format_string("%.2f", operation, grouping=True)
            # return f"\n₱{amount_convert} converts to ${converted_value}.", True
            print(f"\n₱{amount_convert} converts to ${converted_value}.")
            continue


if __name__ == "__main__":
    print(f"The current rate is $1 to ₱{current_usdphp_rate}")
    convert()
