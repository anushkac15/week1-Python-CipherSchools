# replace() method
string = "she is beautiful and she is good dancer"
print(string.replace(" ","_"))
print(string.replace("is","was"))
print(string.replace("is","was",1))
print(string.replace("is","was",2))

# find() method
string = "is she is beautiful and she is good dancer"
print(string.find("is"))
print(string.find("is",1))
string = "she is beautiful and she is good dancer"
is_pos1 = string.find("is") # is_pos1 ------> number
is_pos2 = string.find("is",is_pos1 + 1)
print(is_pos2)