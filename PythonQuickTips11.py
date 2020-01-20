# __eq__ & is vs == | Python Quick Tips

class Dog:
    def __init__(self, name):
        self.name = name

    def __eq__(self, other):
        if isinstance(other, Dog):
            if other.name == self.name:
                return True


tim = Dog("tim")
joe = Dog("tim")
kim = tim

print(tim == joe)
print(tim is joe)
print(tim is kim)

class Cat:
    print(tim is joe)

    def __init__(self, name):
        self.name = name


jim = Cat("jim")
tom = Cat("jim")

print(jim == tom)

x = [1, 2]
y = [1, 2]

print(x == y)

print(x is y)
print(id(x))
print(id(y))

x = [1, 2]
y = x

print(x is y)
print(id(x))
print(id(y))
