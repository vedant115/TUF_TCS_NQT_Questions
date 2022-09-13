n = int(input("Enter Number "))

sum=0
while n:
    sum+=(n%10)
    n//=10
print(sum)