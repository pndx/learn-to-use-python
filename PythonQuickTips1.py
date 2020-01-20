# How to Convert Number to Binary In Python (bin() Function) - Python Quick Tips
num = 23
print(bin(num))
print(int(bin(num)[2:]))
print(bin(num)[2:])

class MyObject:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __index__(self):
        return self.x + self.y


obj = MyObject(2, 2)
print(bin(obj))
obj2 = MyObject(3, 2)
print(bin(obj2))
obj3 = MyObject(3, 7)
print(bin(obj3))
