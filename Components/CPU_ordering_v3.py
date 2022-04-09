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

menu()
order_cpu()





    # countdown until all cpu's have been ordered





    # print the order