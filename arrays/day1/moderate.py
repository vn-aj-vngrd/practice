# Moderate:

# Question: Given an array of integers, determine if it contains any duplicate elements.
# Follow-up: Find the first duplicate element in the array.

def dup(arr):
    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            if (arr[i] == arr[j]):
                return arr[i]
    return False

print(dup([1, 2, 2, 3, 4, 5]))