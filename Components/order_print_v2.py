# list to store ordered CPUs
order_list = ["i3-8100", "i7-9700"]
# list to store cost of CPUs
order_cost = [100.0, 255.0]

customer_detail = {"name": "Caleb", "phone": "020202020", "house": "4", "street": "Fanglorish", "suburb": "Gargafrum"}


#print("\n", customer_detail['name'],"\n", customer_detail["phone"], "\n", customer_detail["house"], "\n", customer_detail["street"], "\n", customer_detail["suburb"])


print("\nCustomer Name: {} \nCustomer Phone: {} \nCustomer House: {} \nCustomer Street: {} \nCustomer Suburb: {}" .format(customer_detail['name'], customer_detail["phone"], customer_detail["house"], customer_detail["street"], customer_detail["suburb"]))

count = 0
for item in order_list:
    print("Ordered: {} ${}".format(item, order_cost[count]))
    count = count+1