"""
Selection Sort

it selects correct element for every position starting from 0th position.
finds min element in every iterations 

time complexity : best/worst - O(n*n)
space complexity : O(n)

auxiliary space : O(1)
therefore it is in place sorting algorithm

"""

arr = [13,46,24,52,20,9,5,4,3,2,1]

for i in range(len(arr)-1):
    for j in range(i+1, len(arr)):
        if arr[i] > arr[j]:
            arr[i], arr[j] = arr[j], arr[i]
    print(arr)

print(arr)