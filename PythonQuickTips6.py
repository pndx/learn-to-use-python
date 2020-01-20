# Swap Variables Values in One Line - Python Quick Tips

# way 1
a = 65
b = 45

temp = a
a = b
b = temp

print(a, b)

# python way
a = 65
b = 45

a, b = b, a

print(a, b)

# work also
a = 65
b = 45
c = 100

a, b, c = b, c, a

print(a, b, c)
