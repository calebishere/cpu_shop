# pickup information

print("Please do the following:")


valid = False
while not valid:
    print("Enter your name")
    name = input("Enter Here: ")
    if name != "":
        print(name)
        break
    else:
        print("Please re-enter your name.")


valid = False
while not valid:
    print("Enter your phone number")
    phone = input("Enter Here: ")
    if phone != "":
        print(phone)
        break
    else:
        print("please re-enter your phone number")
#print(name)
#print(phone)
