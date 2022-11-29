name = "anushka"
age = 18
print("hello " + name + " your age is " + str(age)) #ugly syntax
#string formatting
# python 2
# python 3
# python 3.6 (best)

print("hello {} your age is {} ".format(name, age)) # python 3
print("hello {} your age is {} ".format(name, age + 2)) # python 3

# python 3.6
print(f"hello {name} your age is {age}") # clean
print(f"hello {name} your age is {age + 2}") 