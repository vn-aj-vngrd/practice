# Intermediate:

# Question: Implement a basic string compression algorithm. (e.g., "aabcccccaaa" -> "a2b1c5a3")
# Follow-up: If the compressed string is not smaller than the original, return the original string.

def compress(s):
    compressed = ''
    count = 1
    
    for i in range(len(s)):
        if (i == len(s) - 1 or s[i] != s[i + 1]):
            compressed += s[i] + str(count)
            count = 1
        else:
            count += 1
            
    return compressed if len(compressed) < len(s) else s

print(compress('aabbcc'))