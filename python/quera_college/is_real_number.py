import re


def real_numbers(numbers):
    result = []
    pattern = r'^[+-]?\d+(\.\d+)?([eE][+-]?\d+)?$'
    for i in range(len(numbers)):
        result.append('LEGAL' if re.match(
            pattern, numbers[i].strip()) else 'ILLEGAL')

    return result
