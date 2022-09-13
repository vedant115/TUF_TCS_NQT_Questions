n = 345

# octal to decimal
base=1
ans=0
while n:
    rem = n%10
    ans += rem*base
    base*=8
    n//=10

print(ans)