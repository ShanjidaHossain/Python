#  Write a function that takes a string input and
#  print out whether this string is a palindrome or not.
#  (A palindrome is a string that reads the same forwards and backwards.)

# function which return reverse of a string

def isPalindrome(str):
    return str == str[::-1]


# Driver code
str = "malayalam"
ans = isPalindrome(str)

if ans:
    print("Is Palindrome")
else:
    print("Not a Palindrome")
