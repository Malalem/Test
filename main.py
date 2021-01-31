name = input("Please type your name in")
if len(name)<3:
    print("name must be at least 3 characters long")
elif len(name)>50:
    print("name can br a maximum of 50 characters")
else:
    print("looks Gucci")