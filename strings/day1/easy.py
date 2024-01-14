# Easy:

# Question: Check if a string is a palindrome.
# Follow-up: Ignore non-alphanumeric characters and check if the modified string is a palindrome.

def isPalindrome(s):
    s = s.lower()
    s = ''.join([c for c in s if c.isalnum()])
    return s == s[::-1]

print(isPalindrome('@racecar'))