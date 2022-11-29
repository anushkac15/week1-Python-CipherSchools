name = input(" please enter your name : ")
# anushka gupta

#anushka
#name.count("a") , name.count(name[0]) = 2
#name.count("n") , name.count(name[1]) = 1
#name.count("u") , name.count(name[2]) = 1
#name.count("s") , name.count(name[3]) = 1
#name.count("h") , name.count(name[4]) = 1
#name.count("k") , name.count(name[5]) = 1
#name.count("a") , name.count(name[6]) = 2

#output
#name[0] = a : 2
# n : 1
# u : 1
# s : 1
# h : 1
# k : 1
# a : 2

temp_var = ""
i = 0
while i < len(name):
    if name[i] not in temp_var:
        temp_var += name[i]
        print(f"{name[i] }: {name.count(name[i])}")
    i += 1