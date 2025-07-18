#lex_auth_012693819159732224162

def check_palindrome(word):
    # Convert the word to lowercase for case-insensitive comparison
    word = word.lower()
    # Check if the word is equal to its reverse
    if word == word[::-1]:
        return True  # The word is a palindrome
    else:
        return False  # The word is not a palindrome

status=check_palindrome("malayalam")
if(status):
    print("word is palindrome")
else:
    print("word is not palindrome")