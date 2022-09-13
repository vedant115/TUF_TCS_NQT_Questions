n = int(input())

ans=0
while n:
    ans = ans*10 + (n%10)
    n//=10
print(ans)

"""
dont want number to get reversed
ans=0
ind=0
for i in range(len(str(n))):
    ans = (n%10)*(10**ind) + ans
    print("ans", ans)
    n//=10
    ind+=1
print(ans)
"""