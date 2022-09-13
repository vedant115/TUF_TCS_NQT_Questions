arr = [1,2,3,4,5]

#Method 1
sm = 0
for i in arr:
    sm+=i
print(sm/len(arr))

#Method 2
print(sum(arr)/len(arr))