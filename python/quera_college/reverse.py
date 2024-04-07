class Reverse:
    def __init__(self, ls):
        self.ls = ls
        self.curr = len(ls) - 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.curr >= 0:
            value = self.ls[self.curr]
            self.curr -= 1
            return value
        raise StopIteration


ls = [10, 20, 30]
for it in Reverse(ls):
    print(it)
print(ls)
