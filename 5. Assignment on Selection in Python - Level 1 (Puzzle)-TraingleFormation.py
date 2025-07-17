#lex_auth_012693802383794176153

def form_triangle(num1,num2,num3):
    #Do not change the messages provided below
    success="Triangle can be formed"
    failure="Triangle can't be formed"

    if num1 <= 0 or num2 <= 0 or num3 <= 0:
        return failure
    else:
        # Check if the sum of any two sides is greater than the third side
        if (num1 + num2 > num3) and (num1 + num3 > num2) and (num2 + num3 > num1):
            return success
        else:
            return failure

#Provide different values for the variables, num1, num2, num3 and test your program

print(form_triangle(3, 5, 0))
print(form_triangle(8, 3, 6))