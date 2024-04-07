class Proxy:
    def __init__(self, obj):
        self._obj = obj
        self.last_invoked = ''
        self.calls = {}

    def last_invoked_method(self):
        if self.last_invoked:
            return self.last_invoked
        else:
            raise Exception('No Method Is Invoked')

    def count_of_calls(self, method_name):
        if method_name in self.calls:
            return self.calls[method_name]
        else:
            return 0

    def was_called(self, method_name):
        return self.calls.get(method_name, 0) > 0

    def __getattr__(self, name):
        def wrapper(*args, **kwargs):
            if hasattr(self._obj, name):
                self.last_invoked = name
                self.calls[name] = self.calls.get(name, 0) + 1
                return getattr(self._obj, name)(*args, **kwargs)
            else:
                raise Exception('No Such Method')
        return wrapper



class Radio():
    def __init__(self):
        self._channel = None
        self.is_on = False
        self.volume = 0

    def get_channel(self):
        return self._channel

    def set_channel(self, value):
        self._channel = value

    def power(self):
        self.is_on = not self.is_on


radio = Radio()
radio_proxy = Proxy(radio)

radio_proxy.set_channel(95)
radio_proxy.power()
print(radio.get_channel())


print(radio_proxy.last_invoked_method())
print(radio_proxy.count_of_calls('power'))
print(radio_proxy.was_called('power'))
