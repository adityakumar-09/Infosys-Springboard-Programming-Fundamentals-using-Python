#lex_auth_012693749623193600122

def find_sum_of_digits(number):
    sum_of_digits=0
    abs_number = abs(number)  # Handle negative numbers
    while abs_number > 0:
        digit = abs_number % 10 # Get the last digit through remainder
        sum_of_digits += digit #add the last digit
        abs_number //= 10 # Remove the last digit by modulus division
    return sum_of_digits

#Provide different values for number and test your program
sum_of_digits=find_sum_of_digits(123)
print("Sum of digits:",sum_of_digits)
