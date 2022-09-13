"""
Insertion Sort -
we compare every element to its previous elements and keep shifting elements to next index 
if it is greater than current element and finally place current element in the place where condition failed

Time Complexity :
Best - O(n)
Worst - O(n*n)

Space Complexity : O(n)

Auxiliary Space Complexity : O(1)
as it uses constant auxiliary space complexity it is in place sorting algorithm

"""

arr = [50, 40, 20, 30, 10]

for i in range(1, len(arr)):
    ind=i
    val=arr[i]
    while(ind>0 and arr[ind-1]>val):
        arr[ind] = arr[ind-1]
        ind-=1
    arr[ind] = val

print(arr)