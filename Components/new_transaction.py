import sys

# list to store ordered CPUs
order_list = []
# list to store cost of CPUs
order_cost = []
# Cpu Shop
customer_detail = {}

def new_or_exit():
    print("Do you want to start another order or to exit?")
    print("Please enter 1 to start a new order")
    print("Please enter 2 to exit the program")
    while True:
        try:
            confirm = int(input("Enter here: "))
            if confirm >= 1 and confirm <= 2:
                if confirm == 1:
                    print("New Order")
                    order_list.clear()
                    order_cost.clear()
                    customer_detail.clear()
                    main()
                    break
                
                elif confirm == 2:
                    print("Exit")
                    order_list.clear()
                    order_cost.clear()
                    customer_detail.clear()
                    sys.exit
                    break

            else:
                print("please try and choose 1 or 2")

        except ValueError:
            print("thats not a valid number")

    def main():
        print("restart")

new_or_exit()