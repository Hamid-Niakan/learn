class Strint(int):
    def __init__(self, num):
        self.value = str(num)
        self.last_value = str(num)[len(str(num)) - 1]

    def __lt__(self, other):
        return int(self.last_value) < int(other.last_value)

    def __gt__(self, other):
        return int(self.last_value) > int(other.last_value)

    def __le__(self, other):
        return int(self.last_value) <= int(other.last_value)

    def __ge__(self, other):
        return int(self.last_value) >= int(other.last_value)

    def __eq__(self, other):
        return int(self.last_value) == int(other.last_value)

    def __ne__(self, other):
        return int(self.last_value) != int(other.last_value)

    def __add__(self, other):
        if self.value != '0' and other.value != '0':
            return self.value + other.value
        elif self.value == '0':
            return other.value
        return self.value

    def __sub__(self, other):
        if self.value.endswith(other.value):
            result = self.value[0:self.value.rindex(other.value)]
            return result if result else '0'
        raise Exception('The subtraction is not valid!')

    def __len__(self):
        return len(self.value)

    def __call__(self):
        translation = {
            '1': '۱',
            '2': '۲',
            '3': '۳',
            '4': '۴',
            '5': '۵',
            '6': '۶',
            '7': '۷',
            '8': '۸',
            '9': '۹',
            '0': '۰',
        }
        result = ''
        for num in self.value:
            result += translation[num]
        return result


a = Strint(0)
b = Strint(2)
print(a + b)
