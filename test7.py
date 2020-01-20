a = 65
b = 45

temp = a
a = b
b = temp

print(a, b)

# same as
a = 65
b = 45

a, b = b, a

print(a, b)


a = 65
b = 45
c = 100

a, b, c = b, c, a

print(a, b, c)
