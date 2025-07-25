#lex_auth_01269443664174284882
def is_palindrome(num):
    str_num = str(num)
    return str_num == str_num[::-1]

def nearest_palindrome(number):
    if is_palindrome(number):
        return number
    lower = number - 1
    upper = number + 1
    while True:
        if is_palindrome(lower):
            return lower
        if is_palindrome(upper):
            return upper
        lower -= 1
        upper += 1

number=12300
print(nearest_palindrome(number))