#CPU shop - where you can buy all kinds of
import time # importing time so that the user has time to read exit before the code shuts down
import random # this is going to import a random function into the code
from random import randint # making random to randint
import sys # importing system

# BUGS - NAME INPPUT ALLOWS NUMBERS AND PHONE NUMBER ALLOWS LETTER AND CAN BE ANY LENGHT

#CPU list and list of CPU prices
ls_name = ["Caleb", "Stacey", "David", "Mitchell", "Laurence", "Casey", "Garry", "Tom", "Tim", "Grace"] # This is for the bot to have various of different names

cpu_list = ["i3-8100", "i3-9100", "i3-10400", "i3-1115GRE", "i5-8600", "i5-9400", "i5-10400", 
            "i5-11400", "i7-8700", "i7-9700", "i7-10900", "i7-11800"] # This is holding all of the cpu names in the menu

cpu_prices = [100.0, 120.0, 140.0, 160.0, 170.0, 190.0, 210.0, 220.0, 240.0, 255.0, 270.0, 300.0 ]

# list to store ordered CPUs
order_list = []
# list to store cost of CPUs
order_cost = []

# Cpu Shop
customer_detail = {}
def not_blank(question):
    valid = False
    while not valid:
        response = input(question)
        if response != "":
            return response.title()
        else:
            print("This cannot be blank ")

# String validator
def check_string(question):
    while True:
        response = input(question)
        x = response.isalpha()
        if x == False:
            print("Your name should be only letters")
        else:
            return response.title()

# checks to see if they characters are numbers
def order_deliv(low, high, question):
    while True:
        try:
            num = int(input(question))
            if num >= low and num <= high:
                return num
            else:
                print(f"Please enter a number between {low} and {high}")
        except ValueError:
            print("thats not a valid number")

# Welcome Message
def welcome_msg():
    num = randint(0,9)

    name = (ls_name[num])

    '''
    Below will greet the user by saying a name from
    the randomly generated list
    '''


    print("***** Hello and welcome to my CPU shop! *****")
    print("***** My name is", name,"*****")
    print("i am here to help you pick out special CPUS's")

# Ask user if order is for delivary or pickup
def pick_deli():
    deliv_pick = ""
    LOW = 1
    HIGH = 2
    question = (f"enter a number between {LOW} and {HIGH}: ")
    print("1 for delivery and 2 for pickup")
    answer = order_deliv(LOW, HIGH, question)
    if answer == 1:
        print("Pick Up")
        deliv_pick = "pickup"
        pick_up()

    elif answer == 2:
        print("Delivary")
        order_list.append("Delivery Charge")
        order_cost.append(9)
        deliv_info()
        deliv_pick = "delivery"
    return deliv_pick

# pickup information
def pick_up():
    question = ("Please enter your name: ")
    customer_detail["name"] = check_string(question)
    print (customer_detail["name"])

    question = ("Please enter your phone number: ")
    customer_detail["phone"] = not_blank(question)
    print(customer_detail["phone"])

# delivery information

def deliv_info():
    question = ("Please enter your name: ")
    customer_detail["name"] = check_string(question)
    print (customer_detail["name"])

    question = ("Please enter your phone number: ")
    customer_detail["phone"] = not_blank(question)
    print (customer_detail["phone"])
    
    question = ("Please enter your house number: ")
    customer_detail["house"] = not_blank(question)
    print (customer_detail["house"])
    
    question = ("Please enter your street name: ")
    customer_detail["street"] = check_string(question)
    print (customer_detail["street"])
    
    question = ("Please enter your suburb: ")
    customer_detail["suburb"] = check_string(question)
    print (customer_detail["suburb"])

# CPU list of sales
def menu():
    number_cpu = 12

    for count in range(number_cpu):
        print("{} {} ${}" .format(count+1,cpu_list[count],cpu_prices[count]))



# choose total number of CPUs which is max of 5 CPUs 
def order_cpu():
    # ask for the toal number of CPU's
    num_CPU = 0
    LOW = 1
    HIGH = 5
    MENU_LOW = 1
    MENU_HIGH = 12
    print("How many cpu's would you like to order")
    question = (f"enter a number between {LOW} and {HIGH}: ")
    num_CPU = order_deliv(LOW, HIGH, question)
    # Choose cpu from the list provided1
    
    for item in range(num_CPU):
        while num_CPU > 0:
            print("please choose your cpu by entering the number from the menu")
            question = (f"enter a number between {MENU_LOW} and {MENU_HIGH}: ")
            CPU_ordered = order_deliv(MENU_LOW, MENU_HIGH, question)

            CPU_ordered = CPU_ordered -1
            order_list.append(cpu_list[CPU_ordered])
            order_cost.append(cpu_prices[CPU_ordered])
            print("{} ${}".format(cpu_list[CPU_ordered],cpu_prices[CPU_ordered  ]))
            num_CPU = num_CPU-1



# Display the cost 
def print_order(del_pick):
    total_cost = sum(order_cost)
    print("Customer Details")
    if del_pick == "pickup":
        print("Your order is for pickup")
        print(f"Customer Name: {customer_detail['name']} \nCustomer Phone: {customer_detail['phone']}")
    elif del_pick == "delivery":
        print("Your order is for delivery and a $9 delivery charge")    
        print(f"Customer Name: {customer_detail['name']} \nCustomer Phone: {customer_detail['phone']} \nCustomer Address {customer_detail['house']} {customer_detail['street']} {customer_detail['suburb']}")
    print()
    print("Order Details")
    count = 0
    for item in order_list:
        print("Ordered: {} ${}".format(item, order_cost[count]))
        count = count+1
    print("Total Order Cost")
    print(f"${total_cost}")



# be able to confirm or cancel order after completion
# this code will ask user if order or delivary
def confirm_cancel():
    LOW = 1
    HIGH = 2
    print("Please enter 1 to confirm your order")
    print("Please enter 2 to cancel your order")
    question = (f"enter a number between {LOW} and {HIGH}: ")
    confirm = order_deliv(LOW, HIGH, question)
    if confirm == 1:
        print("Order Confirmed")
        print("We will go and get your CPU/s now")
        new_or_exit()
        
                
    elif confirm == 2:
        print("Order has been cancelled")
        print("You can restart your order or exit the BOT")
        new_or_exit()

# Option for new order or to cancel the order

def new_or_exit():
    LOW = 1
    HIGH = 2
    question = (f"enter a number between {LOW} and {HIGH}: ")
    print("Do you want to start another order or to exit?")
    print("Please enter 1 to start a new order")
    print("Please enter 2 to exit the program")

    confirm = order_deliv(LOW, HIGH, question)
    if confirm == 1:
        print("New Order")
        order_list.clear()
        order_cost.clear()
        customer_detail.clear()
        main()
    elif confirm == 2:
        print("Exit")
        order_list.clear()
        order_cost.clear()
        customer_detail.clear()
        time.sleep(2)
        sys.exit

        
        
def main():
    '''
    This is incharge of holding
    all of the code definitions
    '''
    welcome_msg() # This is printing the welcome message for the user to feel welcome
    del_pick = pick_deli() # this is making del_pick to be equal to pick_deli()
    menu() # This is for printing the menu
    order_cpu() # this is for print the cpu order
    print_order(del_pick) # Del_pick are in the brackets so print_order() can use it in the function 
    confirm_cancel() # prints confirm_cancel() function

main() 