nums = [20, 15, 26, 2, 98, 6]
nums = [100, 5, 70, 2] 

# method 1 O(n^2)
ans=[]
for i in range(len(nums)):
    count=1
    for j in range(len(nums)):
        if nums[j] < nums[i]:
            count+=1
    ans.append(count)
print(ans)

# method 2
numSort = sorted(nums)
for i in range(len(nums)):
    nums[i] = numSort.index(nums[i])+1
print(nums)

# method 3
numSort = sorted(nums)
d=dict()
for ind, num in enumerate(numSort):
    d[num]=ind+1

for i in range(len(nums)):
    nums[i] = d[nums[i]]
print(nums)