# pick up information
customer_detail = {}
def not_blank(question):
    valid = False
    while not valid:
        response = input(question)
        if response != "":
            return response.title()
        else:
            print("This cannot be blank ")


def pick_up():
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

pick_up()
