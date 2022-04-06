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



# Pickup order with name and phone number























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
    
main()