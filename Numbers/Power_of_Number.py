n, k = map(int, input("Enter Number ").split())

# Mehtod 1
ans=1
for i in range(k):
    ans*=n
print(ans)

# Method 2
print(n**k)

# Method 3
from math import pow
print(pow(n, k))

# Method 4 - Binary exponentiation.
"""
If k is even (nk) can be written as  (n2)k/2. 
As we can see that computation steps were reduced from k to k/2 in just one step.

If k is odd (nk) can be written as n.(n)k-1, so now  (k-1) is even.
"""
ans=1
while k:
    if k%2 == 0:
        n = n*n
        k //= 2
    else:
        ans = ans * n
        k-=1
print(ans)