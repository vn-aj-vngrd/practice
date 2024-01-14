# Intermediate:

# Question: Implement an algorithm to rotate an array to the right by k steps.
# Follow-up: Rotate the array in-place without using extra space.

def rotate(arr, k):
    for i in range(k):
        arr.insert(0, arr.pop())
        
    return arr

arr = [1, 2, 3, 4, 5]
k = 2
print(rotate(arr, k))

