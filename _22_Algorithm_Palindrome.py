# Palindrome Algorithm
# Check it's palindrome or not.

def palindrome(word):
    return word.lower()[::-1] == word.lower()
    # "return" means return some data to client when "palindrome()" run.
    # "word.lower()" means all lowercase letters of "word".
    # [::-1] makes reverse order.

print(palindrome("Mother"))
print(palindrome("Mom"))
