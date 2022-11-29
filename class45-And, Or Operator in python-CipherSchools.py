# check two condition at same time
# and , or
name = 'abc'
age = 18
if name=='abc' and age== 18:
    print("condition True")
else:
    print("condition False")

if name=='abc' and age== 21:
    print("condition True")
else:
    print("condition False")

if name=='abcde' or age== 21:
    print("condition True")
else:
    print("condition False")

if name=='abc' or age== 18:
    print("condition True")
else:
    print("condition False")
if name=='abcde' or age== 18:
    print("condition True")
else:
    print("condition False")

if name=='abc' or age== 21:
    print("condition True")
else:
    print("condition False")

if name=='abcde' or age== 21:
    print("condition True")
else:
    print("condition False")