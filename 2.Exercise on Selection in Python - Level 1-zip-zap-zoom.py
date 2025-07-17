#lex_auth_01269363490743091290

def display(num):
    if num%3 == 0 and num%5 == 0:
        message="ZOOM"
    elif num%3 == 0:
        message="ZIP"
    elif num%5 == 0:
        message="ZAP"
    else:
        message='Invalid'
    return message

#Provide different values for num and test your program
message=display(15)
print(message)