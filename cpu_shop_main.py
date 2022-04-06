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
    
main()