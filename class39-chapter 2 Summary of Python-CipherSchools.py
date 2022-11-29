# # strings
# name = "anushka"
# # string indexing
# print(name[1])
# print(name[-1])
# #string slicing
# print(name[0:5])
# print(name[0:-4])
# print(name[0:])
# print(name[-4:])
# print(name[:-4])
# print(name[0:5:1])
# print(name[-1:0:-1])
# #take user input
# age = input("enter your age : ") # strings
# print(age)
# age = int(input("enter your age : "))
# print(age)
# # take two user inputs
# user_name,age = input("enter your name and age : ").split()
# print(user_name)
# print(age)
# user_name,age = input("enter your name and age : ").split(",")
# print(user_name)
# print(age)
# #len function
# print(len(name))
# lower , upper , title method
name = "AnuShKa"
# print(name.lower())
# print(name.upper())
# print(name.title())
# find, replace, center method
name = "anushka"
# print(name.find("a"))
# print(name.find("a",1)
a_pos1 = name.find("a")
a_pos2 = name.find("a",a_pos1 + 1)
print(a_pos2)
print(name.center(11,"*"))
print(name.center(15,"*"))
print(name.replace("a" , "A" , 1))
# strings are immutable
print(name.replace("a" , "A" , 1))
print(name)