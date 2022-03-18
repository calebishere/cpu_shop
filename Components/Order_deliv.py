# this code will ask user if order or delivary

print("Please enter 1 for pickup and 2 for delivary")

while True:
    try:
        enter = int(input("Enter here: "))
        if enter >= 1 and enter <= 2:
            if enter == 1:
                print("pickup")
                break

            elif enter == 2:
                print("Delivary")
                break

        else:
            print("please try and choose 1 or 2")

    except ValueError:
        print("thats not a valid number")