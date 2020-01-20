# Zip Function - Python Quick Tips

x = [1, 2, 3, 4]
y = [1, 1, 3, 7, 9]
z = ["one", "two"]

for i in range(min(len(x), len(y))):
    if x[i] == y[i]:
        print("Same")
    else:
        print('Not Same')


# Zip function
print(list(zip(x, y)))
print(list(zip(y, x)))
print(list(zip(y, x, z)))

for i, j in zip(x, y):
    if i == j:
        print("Same")
    else:
        print("Not Same")