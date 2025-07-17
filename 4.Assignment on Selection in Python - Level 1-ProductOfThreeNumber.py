#lex_auth_012693711503400960120

def find_product(num1,num2,num3):
    nums =[num1, num2, num3]
    product = 1
    if 7 in nums:
        index = nums.index(7)
        nums = nums[index+1:]  # Keep only the numbers after 7
    
    if len(nums) == 1:
        product = nums[0]
    elif len(nums) == 0:
        product = -1
    else:
        for num in nums:
            product *= num
    return product

#Provide different values for num1, num2, num3 and test your program
product=find_product(4,6,2)
print(product)