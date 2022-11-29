name , character = input("enter comma seperated name and character :").split(",")
print(f"length of your name is {len(name)}")
print(f"character count : {name.count(character)}") # case sensitive
# Anushka - anushka
# A - a
name.lower().count(character.lower())
print(f"character count : {name.lower().count(character.lower())}") # case insensitive