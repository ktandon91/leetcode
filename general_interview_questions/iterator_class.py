class BarIterator(object):
    def __init__(self, data_sequence):
        self.idx = 0
        self.data = data_sequence
    def __iter__(self):
        return self
    def __next__(self):
        self.idx += 1
        try:
            return self.data[self.idx-1]
        except IndexError:
            self.idx = 0
            raise StopIteration  # Done iterating.

b = BarIterator([1,2,3])

for ele in b:
    print(ele)
