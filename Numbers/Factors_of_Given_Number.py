n = int(input("Enter Number "))

#Method 1
for i in range(1, n):
    if n%i ==0:
        print(i, end=" ")
print(n)

#Method 2
from math import sqrt
for i in range(1, int(sqrt(n))+1):
    if n%i ==0:
        if (n/i == i):
            print(i, end=" ")
        else:
            print(i, int(n/i), end=" ")