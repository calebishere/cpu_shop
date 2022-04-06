cpu_list = ["i3-8100", "i3-9100", "i3-10400", "i3-1115GRE", "i5-8600", "i5-9400", "i5-10400", 
            "i5-11400", "i7-8700", "i7-9700", "i7-10900", "i7-11800"]
cpu_prices = [100.0, 120.0, 140.0, 160.0, 170.0, 190.0, 210.0, 220.0, 240.0, 255.0, 270.0, 300.0 ]

number_cpu = 12

#print("How many cpu's would you like to get?")
#print("-------------------------------------")
#num_cpu = int(input())
#print(num_cpu, "cpu's you want to buy")

for count in range(number_cpu):
    print(count,cpu_list[count],cpu_prices[count])