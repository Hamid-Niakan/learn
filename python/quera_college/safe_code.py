import re

code_length = input()
code = input()
digit_selectors = []

for i in range(int(code_length)):
    digit_selectors.append(input())

rotation_count = 0


def get_rotation(digit_selector, code_digit):
    digit_place_in_selector = re.search(code_digit, digit_selector).start()
    reverse_step_count = 9 - digit_place_in_selector
    if reverse_step_count < digit_place_in_selector:
        return reverse_step_count
    else:
        return digit_place_in_selector


for i in range(int(code_length)):
    rotation_count += get_rotation(digit_selectors[i], code[i])

print(rotation_count)
