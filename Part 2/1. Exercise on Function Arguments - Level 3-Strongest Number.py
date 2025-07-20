def factorial(number):
    if number < 0:
        return "Invalid input, factorial is not defined for negative numbers"
    elif number == 0 or number == 1:
        return 1
    else:
        return number * factorial(number - 1)

def find_strong_numbers(num_list):
    strong_numbers = []
    for num in num_list:
        sum_of_factorials = 0
        original_num = num

        if num == 0:
            sum_of_factorials = factorial(0)
        else:
            while num > 0:
                digit = num % 10
                sum_of_factorials += factorial(digit)
                num //= 10

        if sum_of_factorials == original_num:
            strong_numbers.append(original_num)
        
    return strong_numbers

num_list = [145, 375, 100, 2, 10, 0]
strong_num_list = find_strong_numbers(num_list)
print(strong_num_list)

