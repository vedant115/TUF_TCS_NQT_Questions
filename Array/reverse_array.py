arr = [9, 4, 1, 7 , 6, 2, 5]

# method 1
ans = arr[::-1]
print("method 1", ans)

#method 2
ans=[]
for i in range(len(arr)-1, -1, -1):
    ans.append(arr[i])
print("method 2", ans)

#method 3
n=len(arr)
for i in range(n//2):
    arr[i], arr[n-1-i] = arr[n-1-i], arr[i]

print("method 3", arr)

#method 4
start=0
end=len(arr)-1

while (start<=end):
    arr[start], arr[end] = arr[end], arr[start]
    start+=1
    end-=1
print("method 4", arr)

#method 5
print("method 5", list(reversed(arr)))
