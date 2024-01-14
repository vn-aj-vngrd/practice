# Advanced:

# Question: Given two sorted arrays, merge them into a single sorted array.
# Follow-up: Implement merge sort on an array.

def merge(arr1, arr2):
    arr = []
    
    while (len(arr1) > 0 and len(arr2) > 0):
        if (arr1[0] < arr2[0]):
            arr.append(arr1.pop(0))
        else:
            arr.append(arr2.pop(0))
            
    if (len(arr1) > 0):
        arr += arr1
    else:
        arr += arr2
        
    return arr

def mergeSort(arr):
    if (len(arr) <= 1):
        return arr
    
    mid = len(arr) // 2
    left = mergeSort(arr[:mid])
    right = mergeSort(arr[mid:])
    
    return merge(left, right)

arr1 = [1, 3, 5, 7, 9]
arr2 = [2, 4, 6, 8, 10]
print(merge(arr1, arr2))
    


