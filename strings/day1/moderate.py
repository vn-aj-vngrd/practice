# Moderate:

# Question: Determine if two strings are anagrams.
# Follow-up: Implement a function to find the minimum number of changes required to make two strings anagrams.

def isAnagram(s1, s2):
    if (len(s1) != len(s2)):
        return False
    
    s1 = s1.lower()
    s2 = s2.lower()
    
    s1 = ''.join(sorted(s1))
    s2 = ''.join(sorted(s2))
    
    return s1 == s2

def minChanges(s1, s2):
    if (len(s1) != len(s2)):
        return -1
    
    s1 = s1.lower()
    s2 = s2.lower()
    
    s1 = ''.join(sorted(s1))
    s2 = ''.join(sorted(s2))
    
    count = 0
    
    for i in range(len(s1)):
        if (s1[i] != s2[i]):
            count += 1
            
    return count

print(isAnagram('listen', 'silent'))
print(minChanges('listen', 'silent'))