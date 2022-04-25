# this code will ask user if order or delivary
print("Please confiurm your order")
print("Please enter 1 to confirm your order")
print("Please enter 2 to cancel your order")

while True:
    try:
        confirm = int(input("Enter here: "))
        if confirm >= 1 and confirm <= 2:
            if confirm == 1:
                print("Order Confirmed")
                print("We will go and get your CPU/s now")
                break
            
            elif confirm == 2:
                print("Order has been cancelled")
                print("You can restart your order or exit the BOT")
                break

        else:
            print("please try and choose 1 or 2")

    except ValueError:
        print("thats not a valid number")