# Python Splat/Unpack Operator - Python Quick Tips

my_list = ["hello", 'world', 4, 5]
my_dict = {"apple": 1, "pear": 2, "orange": 3}
function_args = {"name": "world", "age": 6}


def test1(name, age):
    print(name, age)


def test2(**kwargs):
    print(kwargs)


def test3(*args):
    print(args)


print(*my_list)
print(*my_dict)
test1(**function_args)
test2(name="tim", height=100, tim="cool")
test3("tim", 5, True)
