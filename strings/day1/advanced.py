# Advanced:

# Question: Given a string, find the longest substring without repeating characters.
# Follow-up: Optimize the solution to achieve linear time complexity.

def longestSubstring(s):
    longest = ''
    current = ''
    
    for c in s:
        if (c in current):
            current = current[current.index(c) + 1:]
        current += c
        if (len(current) > len(longest)):
            longest = current
            
    return longest

print(longestSubstring('abcabcbb'))