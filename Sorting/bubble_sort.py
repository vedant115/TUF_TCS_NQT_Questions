"""
*Bubble Sort*
for arr of size n we require n-1 iterations(steps)
at each iteration we perform n-1-i swaps

time complexity - 
best = O(n)
worst = O(n*n)

space complexity - O(n)

auxiliary space(extra or temporary space) - O(1)
as constant auxiliary space it is in place sorting algorithm
"""

arr = [13,46,24,52,20,9,5,4,3,2,1]

for i in range(len(arr)-1):       #for iterations
    flag=0
    for j in range(len(arr)-1-i): #for swaps
        if arr[j] > arr[j+1]:
            arr[j], arr[j+1] = arr[j+1], arr[j]
            flag=1
    if flag == 0:
        break
print(arr)