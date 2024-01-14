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

arr1 = [2, 1, 10, 9, 2]
arr2 = [4, 7, 6, 8, 3]
arr = merge(arr1, arr2)
print(arr)
print(mergeSort(arr))
    


