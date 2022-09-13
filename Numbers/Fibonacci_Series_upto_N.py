n = int(input("Enter Number : "))

a=0
b=1
if (n==1):
    print(a, end=" ")
elif (n==2):
    print(a, b, end=" ")
else:
    print(a, b, end=" ")
    for i in range(2, n):
        no = a+b
        print(no, end=" ")
        a = b
        b = no