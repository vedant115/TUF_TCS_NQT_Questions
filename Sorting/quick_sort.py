"""
Quick Sort - 
*selecting pivot element
*partition function which returns pIndex 
pIndex is index such a way that all elements to left are smaller and all elements to right are larger than pIndex is
*recursively perform quickSort on left and right part.

Time Complexity - 
worst case = O(n*n)
best case = O(n*log(n))

Space Complexity - O(n)

"""

arr = [25, 40, 10, 30, 15, 20, 5, 35]

def partition(arr, start, end):
    pivot = arr[end]
    pIndex = start
    
    for i in range(start, end):
        if arr[i] < pivot:
            arr[i], arr[pIndex] = arr[pIndex], arr[i]
            pIndex+=1

    arr[pIndex], arr[end] = arr[end], arr[pIndex]
    return pIndex

def quickSort(arr, start, end):

    if(start < end):
        pIndex = partition(arr, start, end)

        quickSort(arr, start, pIndex-1)
        quickSort(arr, pIndex+1, end)


quickSort(arr, 0, len(arr)-1)
print("sorted array - ", arr)