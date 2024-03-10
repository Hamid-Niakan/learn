def decorator(validator):
    def inner_fn(fn):
        def wrapper(*args):
            for arg in args:
                if isinstance(arg, str):
                    return 'error'
            if validator(*args):
                return fn(*args)
            else:
                return 'error'
        return wrapper
    return inner_fn


def validator(x, y):
    return type(x) == int and type(y) == int


@decorator(validator)
def f(x, y):
    return x + y


print(f(20, 10))  # should print 2.0
print(f("34", 20))  # should print error
