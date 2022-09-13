n = int(input())

def isPrime1(n):
    for i in range(2, n):
        if n%i == 0:
            return ("not prime")
    return ("prime")

from math import sqrt
def isPrime2(n):
    for i in range(2, int(sqrt(n))+1):
        if n%i == 0:
            return ("not prime")
    return ("prime")

print(isPrime1(n))
print(isPrime2(n))