# list to store ordered CPUs
order_list = ["i3-8100", "i7-9700"]
# list to store cost of CPUs
order_cost = [100.0, 255.0]

customer_detail = {"name": "Caleb", "phone": "020202020", "house": "4", "street": "Fanglorish", "suburb": "Gargafrum"}


def print_order():
    total_cost = sum(order_cost)
    print("Customer Details")
    print(f"Customer Name: {customer_detail['name']} \nCustomer Phone: {customer_detail['phone']} \nCustomer Address {customer_detail['house']} {customer_detail['street']} {customer_detail['suburb']}")
    print()
    print("Order Details")
    count = 0
    for item in order_list:
        print("Ordered: {} ${}".format(item, order_cost[count]))
        count = count+1
    print("Total Order Cost")
    print(f"${total_cost}")

print_order()