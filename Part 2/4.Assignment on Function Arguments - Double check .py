#lex_auth_01269441810970214471

def check_double(number):
    double = number * 2 # Calculate double of the number
    if len(str(number)) != len(str(double)):
        return False # If lengths are not equal, return False
    if sorted(str(number)) == sorted(str(double)):
        return True # If digits are the same, return True
    else:
        return False
    

#Provide different values for number and test your program
print(check_double(245))