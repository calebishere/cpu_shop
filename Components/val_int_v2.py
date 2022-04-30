def order_deliv(low, high, question):
    while True:
        try:
            num = int(input(question))
            if num >= low and num <= high:
                return num
            else:
                print(f"Please enter a number between {low} and {high}")
        except ValueError:
            print("thats not a valid number")


LOW = 1
HIGH = 2
question = (f"enter a number between {LOW} and {HIGH}: ")

answer = order_deliv(LOW, HIGH, question)

print(answer)