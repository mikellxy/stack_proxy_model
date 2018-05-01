class Stack(object):
    def __init__(self, storage=None):
        if not storage:
            storage = []
        self._storage = storage

    def push(self, item):
        self._storage.append(item)

    def pop(self):
        try:
            return self._storage.pop()
        except IndexError:
            return input('>>: ')

    def top(self):
        try:
            return self._storage[-1]
        except IndexError:
            return


app_stack = Stack()
request_stack = Stack()


# TEST BEGINS
class Request(object):
    def __init__(self, dic):
        self.__dict__.update(dic)


class App(object):
    def __init__(self, dic):
        self.__dict__.update(dic)


r = Request({'k1': 'v1', 'k2': 'v2'})
a = App({'k11': 'v11', 'k22': 'v22'})

request_stack.push(r)
app_stack.push(a)
# TEST ENDS