# currency calculations
import locale  # accepts commas in number inputs
import usd_php

# everything I guess I'd wanna know

locale.setlocale(locale.LC_ALL, "")


def convert(current_usdphp_rate):
    choice_convert = input(
        "\nHow would you like to convert?\n1. USD -> PHP\n2. PHP -> USD\n\n: "
    )
    if choice_convert == "1":
        amount_convert = input("\nEnter the amount of USD to convert: $")
        return f"\n${amount_convert} converts to ₱{round(amount_convert * current_usdphp_rate, 2)}."
    elif choice_convert == "2":
        amount_convert = input("\nEnter the amount of PHP to convert: ₱")
        choice_value = locale.atof(amount_convert)
        operation = choice_value / current_usdphp_rate
        converted_value = locale.format_string("%.2f", operation, grouping=True)
        return f"\n₱{amount_convert} converts to ${converted_value}."


if __name__ == "__main__":
    current_usdphp_rate = usd_php.get_usd_php_rate()
    print(convert(current_usdphp_rate))
