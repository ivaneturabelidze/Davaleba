class MyList:
    def __init__(self, data):
        self.data = data

    def __add__(self, other):
        print(self.data + other.data)
        return self.data + other.data

    def __mul__(self, other):
        print(self.data * other)
        return self.data * other

    def __str__(self):
        print(str(self.data))
        return str(self.data)


if __name__ == '__main__':
    l1 = MyList([1, 2, 3])
    l2 = MyList([6, 7])
    l1 * 2
    l1 + l2
    str(l1)
