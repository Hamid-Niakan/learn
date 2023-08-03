"""
Module for fizz buzz
  if divisible by 3 return fizz
  else if divisible by 5 return buzz
  else if divisible by both 3 and 5 return fizz_buzz
  else return the input number
"""


def fizz_buzz(number):
    is_three_divisible = number % 3 == 0
    is_five_divisible = number % 5 == 0
    if is_three_divisible and is_five_divisible:
        print('fizz_buzz')
    elif is_three_divisible:
        print('fizz')
    elif is_five_divisible:
        print('buzz')
    else:
        print(number)


fizz_buzz(7)
