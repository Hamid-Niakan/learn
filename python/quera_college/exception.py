class ExceptionProxy():
    def __init__(self, msg, function):
        self.msg = msg
        self.function = function

def transform_exceptions(func_ls):
    tr_ls = []
    for func in func_ls:
        try:
            func()
            tr_ls.append(ExceptionProxy('ok!', func))
        except Exception as e:
            tr_ls.append(ExceptionProxy(str(e), func))
    return tr_ls

def f():
    1/0

def g():
    pass

tr_ls = transform_exceptions([f, g])

for tr in tr_ls:
    print("msg: " + tr.msg + "\nfunction name: " + tr.function.__name__)