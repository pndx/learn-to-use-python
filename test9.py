def func():
    return 1, 2, 3


t1 = (1, 2)
t2 = (1, 2, 3)

x, y = t1
print(x, y)

x, y, z = t2
print(x, y, z)

print(func())

# Tuple
x, y, z = func()
print(x, y, z)
