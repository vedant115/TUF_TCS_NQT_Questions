arr = [4, 2, 8, 6, 15, 5, 9, 20]
arr = [8, 7, 1, 6, 5, 9]

#Method 1
sm=0
for i in arr:
    sm+=i
print(sm)

#Method 2
sm=0
for i in range(len(arr)):
    sm+=arr[i]
print(sm)

#Method 3
print(sum(arr))