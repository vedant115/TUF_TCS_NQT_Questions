n = 345

# octal to decimal
base=1
ans=0
while n:
    rem = n%10
    ans += rem*base
    base*=8
    n//=10


# decimal to binary
n = ans

ans=""
while n:
    ans += str(n%2)
    n//=2
print(ans[::-1])
