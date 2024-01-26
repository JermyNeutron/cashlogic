import usd_php
import curreny_calculations

# navigation
navigation = {
    "2": {"1": curreny_calculations.convert(), "2": None},
    "3": None,  # placeholder for option 3
    "4": None,  # placeholder for option 4
    "5": lambda: break_script(),
}


def home_screen(main_option, sub_a_option, sub_b_option):
    current_usdphp_rate = usd_php.get_usd_php_rate()
    main_option = main_option.lower()  # ensure lowercase
    sub_a_option = sub_a_option.lower()  # ensure lowercase
    sub_b_option = sub_b_option.lower()  # ensure lowercase

    current_level = 1  # initialize current level

    while True:
        if current_level == 1:
            print(f"Current rate is $1 USD to ₱{current_usdphp_rate} PHP")
            print("2. Convert")
            print("5. Exit")
        elif current_level == 2:
            if main_option == "2" and sub_a_option == "1":
                print(curreny_calculations.convert())

        user_input = input("hello: ")
        if user_input.lower() == "back" and current_level > 1:
            current_level -= 1
        elif user_input in navigation.get(main_option, {}).keys():
            current_level += 1
            main_option = user_input
        elif user_input.lower() == "exit":
            print("exiting..."),
            break
        elif main == "2" and user_input == "1":
            print(curreny_calculations.convert())
        else:
            print("Invalid choice. Please make a valid selection.\n")


#  while True:
#   print(f"Current rate is $1 USD to ₱{current_usdphp_rate} PHP")
#   print("2. Convert")
#   print("5. Exit")

#   choice = input("Enter your choice: ")

#   if choice == "2":
#       choice_convert = input('How would you like to convert?\n1. USD -> PHP\N2. PHP -> USD')
#       if choice_convert == '1':
#           amount_convert = int(input('Enter the amount of USD to convert: '))
#       else:
#           pass

#   elif choice == "5":
#       print("exiting...")
#       break
#   else:
#       print("Invalid choice. Please make a valid selection.\n")


def break_script():
    print("exiting...")
    exit()


def main():
    print("\nHello!")
    home_screen()


if __name__ == "__main__":
    main()
