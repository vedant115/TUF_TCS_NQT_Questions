n = int(input("enter number "))

# Method 1
ans=""

while(n):
    ans+=str(n % 2)
    n//=2

print(ans[::-1])

# Method 2
ans=""
flag=0
for i in range(31, -1, -1):
        k = n >> i
        if (k & 1):
            print("1", end="")
        else:
            print("0", end="")

print((n>>2))