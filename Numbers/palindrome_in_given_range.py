min, max = map(int, input().split())

def is_valid(n):
    tn=n
    rn=0
    while n:
        rn = rn*10 + n%10
        n//=10
    return (rn == tn)


for i in range(min, max+1):
    if is_valid(i):
        print(i, end=" ")
