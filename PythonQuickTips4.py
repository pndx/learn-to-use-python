# Python Enumerate Function - Python Quick Tips

my_list = ["apples", "pears", "oranges", "fruits"]

# way 1
count = 0
for element in my_list:
    print(element)
    if count == 1:
        print("count is 1")

    count += 1


# way 2
for x in range(len(my_list)):
    print(my_list[x])
    if x == 1:
        print("x is 1")

# better
for x, element in enumerate(my_list):
    print(x, element)
    if x == 1:
        print("x is 1")
