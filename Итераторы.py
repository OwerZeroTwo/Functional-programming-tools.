class EvenNumbers:
    def __init__(self, start=0, end=1):
        self.start = start
        self.end = end

    def __iter__(self):
        self.current = self.start
        return self

    def __next__(self):
        if self.current > self.end or self.current % 2 != 0:
            raise StopIteration
        else:
            result = self.current
            self.current += 2
            return result

# Пример использования
en = EvenNumbers(10, 25)
for i in en:
    print(i)
