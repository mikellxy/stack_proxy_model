from importlib import import_module
from functools import partial


mod = import_module('_local.stack')


class StackProxy(object):

    def __init__(self, lookup_func):
        stack = lookup_func()
        object.__setattr__(self, 'stack', stack)

    def __getattr__(self, item):
        obj = self.get_stack()
        return getattr(obj, item)

    def __setitem__(self, key, value):
        obj = self.get_stack()
        setattr(obj, key, value)

    def get_stack(self):
        return self.stack.top()


def stack_lookup(stack_name):
    stack = getattr(mod, stack_name)
    return stack


app = StackProxy(partial(stack_lookup, 'app_stack'))
request = StackProxy(partial(stack_lookup, 'request_stack'))
