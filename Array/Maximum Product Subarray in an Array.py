arr = [1,2,3,4,5,0]
# arr = [1,2,-3,0,-4,-5]

# method 1(brute force)(n^2)

ans = 0
for i in range(len(arr)-1):
    p=arr[i]
    for j in range(i+1, len(arr)):
        ans = max(ans, p)
        p*=arr[j]
    ans = max(ans, p)
print(ans)

# method 2 O(n)

ans = max(arr)
curMax = 1
curMin = 1

for n in arr:
    if n == 0:
        curMax = 1
        curMin = 1
        continue
    tmp = n*curMax
    curMax = max(n*curMax, n*curMin, n)
    curMin = min(tmp, n*curMin, n)
    ans = max(ans, curMax)
print(ans)

# ------------------------------------------- #
curMax, curMin = 1, 1
res = arr[0]
for n in arr:
    vals = (n, n * curMax, n * curMin)
    curMax, curMin = max(vals), min(vals)
    res = max(res, curMax) 
print(res)