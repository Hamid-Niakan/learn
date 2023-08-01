"""Module for printing even numbers up to ten"""
COUNT = 0

for number in range(0, 10, 2):
    if number > 0:
        COUNT += 1
        print(number)

print(f'we have {COUNT} even numbers')
