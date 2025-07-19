#lex_auth_01269437590597632045

def find_number_of_combination(number_of_flavours):
    total_combination=2 ** number_of_flavours #Each topping has 2 states (include/exclude), and they're independent — so multiply 2 by itself N times.
    return total_combination

#Provide different values for number_of_flavours and test your program
number_of_combination=find_number_of_combination(6)
print(number_of_combination)