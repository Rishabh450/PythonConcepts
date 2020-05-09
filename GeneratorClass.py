class FirstHundredGenerator:
    def __init__(self):
        self.number = 0

    def __next__(self):
        if self.number < 100:
            current = self.number
            self.number += 1
            return current
        else:
            raise StopIteration()

    def __iter__(self):
        return self

    def __getitem__(self, item):
        return self.__next__()


g = FirstHundredGenerator()
for i in g:
    print(i)
