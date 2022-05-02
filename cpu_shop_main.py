#CPU shop - where you can buy all kinds of
import time  # importing time so that the user has time to read exit before the code shuts down
import random  # this is going to import a random function into the code
from random import randint  # making random to randint
import sys  # importing system

# BUGS - NAME INPPUT ALLOWS NUMBERS AND PHONE NUMBER ALLOWS LETTER AND CAN BE ANY LENGHT

# CPU list and list of CPU prices
ls_name = ["Caleb", "Stacey", "David", "Mitchell", "Laurence", "Casey", "Garry", "Tom", "Tim", "Grace"]  # This is for the bot to have various of different names

cpu_list = ["i3-8100", "i3-9100", "i3-10400", "i3-1115GRE", "i5-8600", "i5-9400", "i5-10400", 
            "i5-11400", "i7-8700", "i7-9700", "i7-10900", "i7-11800"]  # This is holding all of the cpu names in the menu

cpu_prices = [100.0, 120.0, 140.0, 160.0, 170.0, 190.0, 210.0, 220.0, 240.0, 255.0, 270.0, 300.0 ]

# constants
ph_low = 7
ph_high = 10  
# list to store ordered CPUs
order_list = []
# list to store cost of CPUs
order_cost = []

# asking the user a question
customer_detail = {}  # This is what is holding all of the customer details in a dictionary
def not_blank(question):  # This is using the function not_blank() and the function is using question
    valid = False  # Making valid a variable for false
    while not valid:  # While loop
        response = input(question)  # this is asking the user a question
        if response != "":  # if the user puts the right input in
            return response.title()  # This will run when user puts correct input
        else:
            print("This cannot be blank ")  # this message will print when user puts incorrect input in 

# String validator
# Takes question as parameter
def check_string(question):  # This is using the function check_string() and the function is using question
    while True:  # A while loop
        response = input(question)  # Asking the user a question
        x = response.isalpha()  # checks input is alphebetical and sets x to true
        if x == False:  # if x is false prints error message
            print("Input should be letters only")
        else:
            return response.title()  # If true returns response in title class

# checks to see if they characters are numbers
def order_deliv(low, high, question):  # using variable order_deliv() and using variables low, high, question
    while True:  # a while loop
        try:  # Trying to see if user puts input correctly
            num = int(input(question))  # will ask user a question
            if num >= low and num <= high:  # If user puts expected value in will return number
                return num
            else:
                print(f"Please enter a number between {low} and {high}")  # if user does not but in correct value will print this message
        except ValueError:
            print("thats not a valid number")  # if user dosent put value or incorrect value in will print this message
# makes sure the user uses no letters or has a phone num to long
def check_phone(question, ph_low, ph_high):  # using variable check_phone() and using variables low, high, question
    while True:  # while loop
        try:  # Trying to see if user puts input correctly
            num = int(input(question))  # asking the user a question
            test_num = num  # making a variable for the question
            count = 0  # count is equivalent to 0
            while test_num > 0:  
                test_num = test_num//10
                count = count+1
            if count >= ph_low and count <= ph_high:  # if user puts correct length and value the program will return
                return str(num)
            else: 
                print("NZ phone numbers have between 7 and 10 digits")  # If user puts a long or short phone number it will print error message
        except ValueError:
            print("Please enter a number") # if the user uses anything but a number it will print this error message
# Welcome Message
def welcome_msg():  # setting this code to a deffinition of welcome_msg
    num = randint(0,9)  # randomising from 0 - 9

    name = (ls_name[num])

    '''
    Below will greet the user by saying a name from
    the randomly generated list
    '''


    print("***** Hello and welcome to my CPU shop! *****")  # prints welcome message
    print("***** My name is", name,"*****")  # Prints name from random list
    print("i am here to help you pick out special CPUS's")  # Prints its purpose

# Ask user if order is for delivary or pickup
def pick_deli():  # defining pick_deli()
    deliv_pick = ""  
    LOW = 1    # LOW is equivalent to 1
    HIGH = 2   # HIGH is equivalent to 2
    question = (f"enter a number between {LOW} and {HIGH}: ")  # asking the user a question
    print("1 for delivery and 2 for pickup")  # tells the user what to put
    answer = order_deliv(LOW, HIGH, question)  # Making answer a variable to order_deliv whil using varialbes LOW, HIGH, question
    if answer == 1:  # if user enters 1 for pickup the code will print pickup
        print("Pick Up")
        deliv_pick = "pickup"  # making deliv_pick equal to "pickup"
        pick_up()  # printing the definition of pick_up()

    elif answer == 2:  # When user inputs 2 for delivery the code will print delivery
        print("Delivary")
        order_list.append("Delivery Charge")  # Showing the user there is also a delivery charge that comes with delivery
        order_cost.append(9)  # adding 9 dollar to the cost
        deliv_info()  # printing the def deliv_info()
        deliv_pick = "delivery"
    return deliv_pick  # returnning the variable.

# pickup information
def pick_up():  # when the user uses pickup
    question = ("Please enter your name: ")  # Will ask the user there name
    customer_detail["name"] = check_string(question)  # will hold the users name in the dictionary as well as checking for errors in the input
    print (customer_detail["name"])  # prints the users name

    question = ("Please enter your phone number: ")  # will ask the user there phone number
    customer_detail["phone"] = check_phone(question, ph_low, ph_high)  # will hold the users phone number in the dictionary as well as checking for errors in the input
    print(customer_detail["phone"])  # prints the users phone number

# delivery information

def deliv_info():  # when the user chose delivery will start here
    question = ("Please enter your name: ")  # asking the user a question
    customer_detail["name"] = check_string(question)  # will hold the users name in the dictionary as well as checking for errors in the input
    print (customer_detail["name"])  # prints the users name

    question = ("Please enter your phone number: ")  # will ask the user there phone number
    customer_detail["phone"] = check_phone(question, ph_low, ph_high)  # will hold the users phone number in the dictionary as well as checking for errors in the input
    print (customer_detail["phone"])  # prints the users phone number
    
    question = ("Please enter your house number: ")  # asking the user what there house number is
    customer_detail["house"] = not_blank(question)  # will hold the users house number in the dictionary as well as checking for errors in the input
    print (customer_detail["house"])  # Will print the users house number
    
    question = ("Please enter your street name: ")  # asking the user what there street name is
    customer_detail["street"] = check_string(question)  # will hold the users street name in the dictionary as well as checking for errors in the input
    print (customer_detail["street"])  # Will print the users street name
    
    question = ("Please enter your suburb: ")  # asks the user which suburb they  are in
    customer_detail["suburb"] = check_string(question)  # will hold the users suburb in the dictionary as well as checking for errors in the input
    print (customer_detail["suburb"])  # prints the users suburb out

# CPU list of sales
def menu():  # makes menu a definition
    number_cpu = 12  # making the number_cpu equal to 12

    for count in range(number_cpu):  # for loop for the cpu menu
        print("{} {} ${}" .format(count+1,cpu_list[count],cpu_prices[count]))  # formatting the menu to make it look presentable



# choose total number of CPUs which is max of 5 CPUs 
def order_cpu():
    # ask for the toal number of CPU's
    num_CPU = 0
    LOW = 1
    HIGH = 5
    MENU_LOW = 1
    MENU_HIGH = 12
    print("How many cpu's would you like to order")
    question = (f"enter a number between {LOW} and {HIGH}: ")  # asking user a question
    num_CPU = order_deliv(LOW, HIGH, question)
    # Choose cpu from the list provided
    
    for item in range(num_CPU):  # a for loop for the user when they are entering what number they are choosing 
        while num_CPU > 0:
            print("please choose your cpu by entering the number from the menu") 
            question = (f"enter a number between {MENU_LOW} and {MENU_HIGH}: ")  # asking the user a question
            CPU_ordered = order_deliv(MENU_LOW, MENU_HIGH, question)  # making CPU_orderd into a variable to order_deliv

            CPU_ordered = CPU_ordered -1  # making CPU_ordered into a variable and minus 1 of it
            order_list.append(cpu_list[CPU_ordered])  # printed the list of cpus the user is buying
            order_cost.append(cpu_prices[CPU_ordered])  # printed the cost of cpus ordered
            print("{} ${}".format(cpu_list[CPU_ordered],cpu_prices[CPU_ordered  ]))  # printing the amount of cpus ordered
            num_CPU = num_CPU-1  # making num_cpu into a variable and minus one of it



# Display the cost 
def print_order(del_pick):  # defining print_order() and using variable del_pick
    total_cost = sum(order_cost)  # making total cost a variable of sum(order_cost)
    print("Customer Details")
    if del_pick == "pickup":  # if user chose pickup will not need to pay extra delivery fee
        print("Your order is for pickup")
        print(f"Customer Name: {customer_detail['name']} \nCustomer Phone: {customer_detail['phone']}")  # will print out customer name and phone
    elif del_pick == "delivery":  # If user selects delivery they will have to pay a $9 delivery fee charge
        print("Your order is for delivery and a $9 delivery charge")    
        print(f"Customer Name: {customer_detail['name']} \nCustomer Phone: {customer_detail['phone']} \nCustomer Address {customer_detail['house']} {customer_detail['street']} {customer_detail['suburb']}")  # Printing out all of the customer dets
    print("Order Details")
    count = 0  # making count equal to zero
    for item in order_list:  # uses for loop to print out what the users input
        print("Ordered: {} ${}".format(item, order_cost[count]))  # prints out the users input
        count = count+1  # making count equal itself plus one
    print("Total Order Cost") 
    print(f"${total_cost}")  # Prints the toal cost for customer



# be able to confirm or cancel order after completion
# this code will ask user if order or delivary
def confirm_cancel():
    LOW = 1  # setting LOW to = 1
    HIGH = 2  # setting HIGH to = 2
    # messages below are printed for the user
    print("Please enter 1 to confirm your order")
    print("Please enter 2 to cancel your order")
    question = (f"enter a number between {LOW} and {HIGH}: ")  # This is for the user to answer
    confirm = order_deliv(LOW, HIGH, question)
    if confirm == 1:# If user confirms, will print the messages below 
        print("Order Confirmed")
        print("We will go and get your CPU/s now")
        new_or_exit()# printing new_or_exit
        
                
    elif confirm == 2:  # If user cancels, will print the messages below 
        print("Order has been cancelled")
        print("You can restart your order or exit the BOT")
        new_or_exit()  # printing new_or_exit

# Option for new order or to cancel the order

def new_or_exit():  # making a definition to new_or_exit
    LOW = 1  # setting LOW to = 1
    HIGH = 2  # setting HIGH to = 2
    question = (f"enter a number between {LOW} and {HIGH}: ")  # This is a variable to ask the user a question
    print("Do you want to start another order or to exit?")
    print("Please enter 1 to start a new order")
    print("Please enter 2 to exit the program")

    confirm = order_deliv(LOW, HIGH, question) # The function order_deliv() is using the variables LOW, HIGH, question and is being set a variable to confirm
    if confirm == 1:  # if the user chooses a new order will print new order
        print("New Order")
        order_list.clear()  # will clear all users lists
        order_cost.clear()  # will clear all useres costs
        customer_detail.clear()  # will clear users details
        main()  # takes back to beginning
    elif confirm == 2:  # if user exits program will print exit
        print("Exit")
        order_list.clear()  # this will clear the users lissts
        order_cost.clear()  # This will clear all ordering cost
        customer_detail.clear()  # this will clear all customer details
        time.sleep(2)  # this will help the user be able to read the exit before the program is closed
        sys.exit  # this will cause the program the exit the system

        
        
def main():
    '''
    This is incharge of holding
    all of the code definitions
    '''
    welcome_msg()  # This is printing the welcome message for the user to feel welcome
    del_pick = pick_deli()  # this is making del_pick to be equal to pick_deli()
    menu()  # This is for printing the menu
    order_cpu()  # this is for print the cpu order
    print_order(del_pick)  # Del_pick are in the brackets so print_order() can use it in the function 
    confirm_cancel()  # prints confirm_cancel() function

main() 