customer_detail = {}

# pickup information

print("Please do the following:")


valid = False
while not valid:
    print("Enter your name")
    customer_detail["name"] = input("Enter Here: ")
    if customer_detail["name"] != "":
        print(customer_detail["name"])
        break
    else:
        print("Please re-enter your name.")


valid = False
while not valid:
    print("Enter your phone number")
    customer_detail["phone"] = input("Enter Here: ")
    if customer_detail["phone"] != "":
        print(customer_detail["phone"])
        break
    else:
        print("please re-enter your phone number")
