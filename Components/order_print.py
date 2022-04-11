
# list to store ordered CPUs
order_list = ["i3-8100", "i7-9700"]
# list to store cost of CPUs
order_cost = [100.0, 255.0]

count = 0
for item in order_list:
    print("{} ${}".format(item, order_cost[count]))
    count = count+1