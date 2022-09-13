arr = [9, 4, 1, 4 , 6, 2]

# method 1
mn=arr[0]
mx=arr[0]

for i in arr:
    if i < mn:
        mn=i
    if i > mx:
        mx=i

print("min",mn,"\nmax", mx)

# method 2

arr = sorted(arr)
print("min", arr[0])
print("max", arr[-1])