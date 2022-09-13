n = int(input("enter number to check palindrome "))
tn=n
rn=0
while n:
    rn=rn*10+(n%10)
    n//=10
print(tn==rn)