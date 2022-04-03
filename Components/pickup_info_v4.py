# pick up information
customer_detail = {}
def not_blank(question):
    valid = False
    while not valid:
        response = input(question)
        if response != "":
            return response
        else:
            print("This cannot be blank ")

# pickup information
question = ("Please enter your name: ")
customer_detail["name"] = not_blank(question)
print (customer_detail["name"])

question = ("Please enter your phone number: ")
customer_detail["phone"] = not_blank(question)
print(customer_detail["phone"])

#print(customer_detail)
