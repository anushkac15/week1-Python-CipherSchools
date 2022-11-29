user_name = input("enter your name please : ")
user_age = int(input("enter your age please : "))
if user_age >= 10 and (user_name[0]=='a' or user_name[0] == 'A'):
    print("you can watch coco movie")
else:
    print("you can't watch coco movie")