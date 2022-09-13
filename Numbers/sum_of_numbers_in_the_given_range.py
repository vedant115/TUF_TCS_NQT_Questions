l, r = map(int, input("enter left & right numbers ").split())

# Method 1
sum=0
for i in range(l, r+1):
    sum+=i
print(sum)

# Method 2
print(r*(r+1)/2-l*(l-1)/2)