n = int(input("enter number "))

tn = n
ans=0
count = len(str(tn))
while tn:
    ans += ((tn%10)**count)
    tn//=10

print("Is Armstrong Number - ", n == ans)