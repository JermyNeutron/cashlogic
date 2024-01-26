forex = 56.292


def convert(forex):
    amount_convert = int(input("Enter a number to convert into PHP: "))
    return round(amount_convert * forex, 2)


print(convert(forex))
