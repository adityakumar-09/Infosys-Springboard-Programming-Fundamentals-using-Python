#lex_auth_012693813706604544157

def find_max(num1, num2):
    max_num = -1
    
    if num1 >= num2:
        return -1

    valid_nums = []

    for num in range(num1, num2 + 1):
        if 10 <= num <= 99:
            digit_sum = sum(int(d) for d in str(num))
            if digit_sum % 3 == 0 and num % 5 == 0:
                valid_nums.append(num)

    if valid_nums:
        max_num = max(valid_nums)

    return max_num


print(find_max(10, 15))
print(find_max(90, 95))  
print(find_max(80, 89))
print(find_max(100, 120))
print(find_max(20, 19))     
