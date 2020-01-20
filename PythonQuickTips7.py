# List Comprehension - Python Quick Tips

x = [i for i in range(10)]

print(x)

x = [i for i in range(10) if i % 2 == 0]

print(x)

x = [(i, y) for i in range(10) for y in range(20)]

print(x)

x = [[] for i in range(10)]

print(x)

x = [[0 for i in range(5)] for j in range(10)]

print(x)

x = [[True for i in range(5)] for j in range(10)]

print(x)

x = [[[] for i in range(5)] for j in range(10)]

print(x)

x = [[0 for i in range(5)] for j in range(5)]

print(x)
