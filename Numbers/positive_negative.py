ch = 1
while ch:
    n = int(input("Enter Number : "))

    # Method 1
    if (n > 0):
        print("positive")
    else:
        print("negative")

    # Method 2
    if (n >> 31 == 0):
        print("positive")
    else:
        print("negative")

    ch = int(input("Do you want to continue (0/1) "))