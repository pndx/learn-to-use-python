# Python For Else Statement - Python Quick Tips

# example 1
my_list = [100, 55, 67, 33, 101, 23, 43, 100, 23]
look_for = 44

for x in my_list:
    if x == look_for:
        print("found", look_for)
        break
else:
    print("Not found", look_for)

# example 2
list1 = [1, 2, 3, 4, 5, 6]
list2 = [2, 4, 6]

for x in list1:
    for y in list2:
        if x == y:
            print(x, "is in both lists")
            break
    else:
        print(x, "is not in list1")
