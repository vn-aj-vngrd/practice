# Easy:

# Question: Given an array of integers, find the sum of all elements.
# Follow-up: Find the maximum and minimum elements in the array.

def sum(arr):
    sum = 0
    
    for i in arr:
        sum += i
        
    return sum

def min(arr):
    _min = arr[0]
    
    for i in arr:
        if (i < _min):
            _min = i
            
    return _min

def max(arr):
    _max = arr[0]
    
    for i in arr:
        if (i > _max):
            _max = i
            
    return _max

arr = [1, 2, 3, 4,5]
print(sum(arr))
print(min(arr))
print(max(arr))
        
