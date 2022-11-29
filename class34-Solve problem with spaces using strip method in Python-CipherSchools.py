name = "       anushka      "
dots = "...................."
print(name + dots)
# lstrip() method
print(name.lstrip() + dots)
# rstrip() method
print(name.rstrip() + dots)
#strip() method
print(name.strip() + dots)

name = "anus    hka"
print(name.replace(" ","") + dots)

# CONTINUATION OF PREVIOUS VIDEO
name , character = input("enter comma seperated name and character :").split(",")
print(f"length of your name is {len(name)}")
print(f"character count : {name.strip().lower().count(character.strip().lower())}") # case sensitive
# Anushka - anushka
# A - a
# "  Anushka  " -----------> "Anushka" -----------> "anushka"
# "  a  " -----------> "A" ----------> "a"
# (name.strip().lower().count(character.strip().lower())) 