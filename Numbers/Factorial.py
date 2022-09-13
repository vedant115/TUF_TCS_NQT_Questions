n = int(input("Enter Number : "))

# Iterative
ans=1
for i in range(n, 1, -1):
    ans*=i
print(ans)

# Recursive
def fact(n):
    if n < 2:
        return 1
    return n * fact(n-1)

print(fact(n))