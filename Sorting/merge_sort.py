"""
divide and conquer strategy
two function 
merge - two merge two sorted arrays
mergeSort - to divide array
"""

def merge(arr, start, mid, end):
    n1 = mid-start+1
    n2 = end-mid

    L = [0]*n1
    R = [0]*n2

    for i in range(n1):
        L[i] = arr[start+i]

    for j in range(n2):
        R[j] = arr[mid+1+j]

    i = 0 
    j = 0
    k = start

    while(i < n1 and j < n2):
        if L[i] <= R[j]:
            arr[k] = L[i]
            i+=1
        else:
            arr[k] = R[j]
            j+=1
        k+=1
    
    while (i < n1):
        arr[k] = L[i]
        i+=1
        k+=1

    while (j < n2):
        arr[k] = R[j]
        j+=1
        k+=1

    print(arr)

def mergeSort(arr, start, end):
    if start < end:
        mid = start+(end-start)//2

        mergeSort(arr, start, mid)
        mergeSort(arr, mid+1, end)
        merge(arr, start, mid, end)

arr = [10, 50, 12, 25, 40, 5, 20]
# arr = [9, 4, 7, 6, 3, 1, 5]
mergeSort(arr, 0, len(arr)-1)
print(arr)