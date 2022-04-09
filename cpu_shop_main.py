#CPU list and list of CPU prices

cpu_list = ["i3-8100", "i3-9100", "i3-10400", "i3-1115GRE", "i5-8600", "i5-9400", "i5-10400", 
            "i5-11400", "i7-8700", "i7-9700", "i7-10900", "i7-11800"]
cpu_prices = [100.0, 120.0, 140.0, 160.0, 170.0, 190.0, 210.0, 220.0, 240.0, 255.0, 270.0, 300.0 ]



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

# Welcome Message
def welcome_msg():
    import random
    from random import randint

    ls_name = ["Caleb", "Stacey", "David", "Mitchell", "Laurence", "Casey", "Garry", "Tom", "Tim", "Grace"]

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
    print("Please enter 1 for pickup and 2 for delivary")

    while True:
        try:
            enter = int(input("Enter here: "))
            if enter >= 1 and enter <= 2:
                if enter == 1:
                    print("Pick Up")
                    pick_up()
                    break

                elif enter == 2:
                    print("Delivary")
                    deliv_info()
                    break

            else:
                print("please try and choose 1 or 2")

        except ValueError:
            print("thats not a valid number")

# pickup information
def pick_up():
    question = ("Please enter your name: ")
    customer_detail["name"] = not_blank(question)
    #print (customer_detail["name"])

    question = ("Please enter your phone number: ")
    customer_detail["phone"] = not_blank(question)
    #print(customer_detail["phone"])
    print(customer_detail)




# delivery information

def deliv_info():
    question = ("Please enter your name: ")
    customer_detail["name"] = not_blank(question)
    print (customer_detail["name"])

    question = ("Please enter your phone number: ")
    customer_detail["phone"] = not_blank(question)
    print (customer_detail["phone"])
    
    question = ("Please enter your house number: ")
    customer_detail["house"] = not_blank(question)
    print (customer_detail["house"])
    
    question = ("Please enter your street name: ")
    customer_detail["street"] = not_blank(question)
    print (customer_detail["street"])
    
    question = ("Please enter your suburb: ")
    customer_detail["suburb"] = not_blank(question)
    print (customer_detail["suburb"])

# CPU list of sales
def menu():
    number_cpu = 12

    for count in range(number_cpu):
        print("{} {} ${}" .format(count+1,cpu_list[count],cpu_prices[count]))



# choose total number of CPUs which is max of 5 CPUs 
# List of CPUs

cpu_list = ["i3-8100", "i3-9100", "i3-10400", "i3-1115GRE", "i5-8600", "i5-9400", "i5-10400", 
            "i5-11400", "i7-8700", "i7-9700", "i7-10900", "i7-11800"]
cpu_prices = [100.0, 120.0, 140.0, 160.0, 170.0, 190.0, 210.0, 220.0, 240.0, 255.0, 270.0, 300.0 ]

# list to store ordered CPUs
order_list = []
# list to store cost of CPUs
order_cost = []

def menu():
    number_cpu = 12

    for count in range(number_cpu):
        print("{} {} ${}" .format(count+1,cpu_list[count],cpu_prices[count]))


def order_cpu():
    # ask for the toal number of CPU's
    num_CPU = 0

    while True:
        try:
            num_CPU = int(input("How many Cpus's would you like to get?: "))
            if num_CPU >= 1 and num_CPU <=5:
                break
            else:
                print("Try and choose between 1 - 5") 
        except ValueError:
            print("Please enter a number...")
    # Choose cpu from the list provided
    for item in range(num_CPU):
        while num_CPU > 0:
            while True:
                try:
                    CPU_ordered = int(input("Please choose your CPU by entering the number from the menu: "))
                    if CPU_ordered >= 1 and CPU_ordered <=12:
                        break
                    else:
                        print("Try and choose between 1 - 12") 
            
                except ValueError:
                    print("Please enter a number...")
            CPU_ordered = CPU_ordered -1
            order_list.append(cpu_list[CPU_ordered])
            order_cost.append(cpu_prices[CPU_ordered])
            print("{} ${}".format(cpu_list[CPU_ordered],cpu_prices[CPU_ordered  ]))
            num_CPU = num_CPU-1
            
    print(order_list, order_cost)



# Display the cost 
























# display the whole order when finished

























# be able to quit or continue order after completion




def main():
    '''
    This is incharge of holding
    all of the code definitions
    '''
    welcome_msg()
    pick_deli()
    menu()
    order_cpu()
    
main()