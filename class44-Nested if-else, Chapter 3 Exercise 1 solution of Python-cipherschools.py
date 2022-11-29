# Exercise Solution
winning_number = 27
user_input = int(input("guess a number b/w 1 and 100 : "))
if user_input == winning_number:
    print("YOU WIN !!!!")
else:
    if user_input < winning_number :
        print("too low")
    else:
        print("too high")