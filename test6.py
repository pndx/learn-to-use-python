name = "tom"
age = 20

ex1 = "my name is " + name + " and I am " + str(age) + " years old"
ex2 = "my name is {0} and I am {1} years old".format(name, age)
ex3 = "my name is %s and I am %i years old" %(name, age)

ex4 = F"my name is {name} and I am {age + 5} years old"

print(ex4)
print(f"Hello {name}")
