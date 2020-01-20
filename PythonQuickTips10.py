# Help and Dir Functions - Python Quick Tips

print(dir(int))
print(dir(str))
print(dir(bool))
print(help(int))


class MyObject:
    """
    This is a custom obj for testing
    """

    def __init__(self, name):
        """
        This is inits
        """
        self.name = name


print(help(MyObject))
