#  Girl Math

import locale
import os
import re # math expression validation, security precaution

# currency formatting
locale.setlocale(locale.LC_ALL, '')

def clear_screen():
    if os.name == 'nt':
        _ = os.system('cls')
    else:
        _ = os.system('clear')

# check for valid math expression
def is_valid_math_expression(key_input):
    # define a regular expression pattern for simple math expression
    pattern = r'^\s*\d+(\s*[\+\-\*/]\s*\d+(\s*[\+\-\*/]\s*\d+)*)*\s*$'

    #  use re.math to check if input matches pattern
    return bool(re.match(pattern, key_input))

# executes valid math expression
def evaluate_math_expression(expression):
    try:
        result = eval(expression)
        return result
    except Exception as e:
        print('{e}')
        return None

# accept list items
list1 = []
while True:
    key_test = input('Provide a key: ')
    if key_test == 'q':
        clear_screen()
        break
    else:
        key_input = key_test
    
    value_test = input(f"Provide a \"{key_input}\" divisor: ")
    try:
        float(value_test)
        list1.append((key_input, float(value_test)))
    except ValueError:
        if is_valid_math_expression(value_test):
            value_input = evaluate_math_expression(value_test)
            list1.append((key_input, float(value_input)))
        else:
            print('Invalid math expression. No symbols allowed.')

        

# create organized list
list2 = []
# add first element since no operation is conducted
list2.append(list1[0])

# division operations
for i in range(1, len(list1)):
    item = list1[i]
    previous_last_value = list2[i-1][-1]
    new_item = item + (float(previous_last_value) / float(item[1]),) # creates item of 3 values
    list2.append(new_item)

print(f"'{list2[0][0]}' = {locale.format_string('%.2f', (list2[0][1]), grouping=True)}")
for item in list2[1:]:
    key, divisor, value = item
    print(f"'{key}' ({divisor}) = {(locale.format_string('%.2f', value, grouping=True))}")