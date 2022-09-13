n=136

# Method 1
# ans=""
# while n:
#     ans+=str(n%8)
#     n//=8
# print(ans[::-1])


# Method 2
import math
ans=0
i=0
while n:
    rem = n%8
    ans += rem*int(math.pow(10, i))
    i+=1
    n//=8
print(ans)