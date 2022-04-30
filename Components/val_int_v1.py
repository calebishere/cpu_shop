def pick_deliv():
    while True:
        try:
            num = int(input())
            if num >= 1 and num <= 2:
                return num
            else:
                print("please try and choose 1 or 2")
        except ValueError:
            print("thats not a valid number")

print("enter a number between 1 and 2")

answer = pick_deliv()

print(answer)