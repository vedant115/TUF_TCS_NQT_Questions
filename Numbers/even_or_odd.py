ch = 1
while ch:
    n = int(input("Enter Number : "))

    # Method 1
    if (n % 2 == 0):
        print("even")
    else:
        print("odd")

    # Method 2
    if (n & 1 == 0):
        print("even")
    else:
        print("odd")

    ch = int(input("Do you want to continue (0/1) "))