#  makes your class instantiate an iterable (which isn't technically a generator):

class Fib:
    def __init__(self):
        self.a, self.b = 0, 1
    def __iter__(self):
        while True:
            yield self.a
            self.a, self.b = self.b, self.a+self.b


###
class Fib(Generator):
    def __init__(self):
        self.a, self.b = 0, 1        
    def send(self, ignored_arg):
        return_value = self.a
        self.a, self.b = self.b, self.a+self.b
        return return_value
    def throw(self, type=None, value=None, traceback=None):
        raise StopIteration
