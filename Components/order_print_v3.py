# list to store ordered CPUs
order_list = ["i3-8100", "i7-9700"]
# list to store cost of CPUs
order_cost = [100.0, 255.0]

customer_detail = {"name": "Caleb", "phone": "020202020", "house": "4", "street": "Fanglorish", "suburb": "Gargafrum"}

print(f"Customer Name: {customer_detail['name']} \nCustomer Phone: {customer_detail['phone']} \nCustomer Address {customer_detail['house']} {customer_detail['street']} {customer_detail['suburb']}")

count = 0
for item in order_list:
    print("Ordered: {} ${}".format(item, order_cost[count]))
    count = count+1