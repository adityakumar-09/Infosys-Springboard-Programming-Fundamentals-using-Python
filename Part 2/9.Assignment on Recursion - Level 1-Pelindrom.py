#lex_auth_01269442114344550475

def is_palindrome(word):
    word = word.lower()  # Convert to lowercase for case-insensitive comparison
    if len(word) <= 1:
        return True
    if word[0] != word[-1]:
        return False
    return is_palindrome(word[1:-1])

# Test
result = is_palindrome("MamDad")
if result:
    print("The given word is a Palindrome")
else:
    print("The given word is not a Palindrome")