def even(data):
    if isinstance(data, int):  # Used as a filter function
        return data % 2 == 0
    elif isinstance(data, list):  # Called directly with a list
        return [i for i in data if i % 2 == 0]

def odd(data):
    if isinstance(data, int):
        return data % 2 != 0
    elif isinstance(data, list):
        return [i for i in data if i % 2 != 0]

def sum_of_numbers(list_of_num, filter_func=None):
    if filter_func is None:
        return sum(list_of_num)
    else:
        total = 0
        for num in list_of_num:
            if filter_func(num):  # calls even(num) or odd(num)
                total += num
        return total

# Test data
sample_data = [10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25]

# Using as filters
print(sum_of_numbers(sample_data, even))  # 136
print(sum_of_numbers(sample_data, odd))   # 144

# Using as standalone functions
print(even(sample_data))  # [10, 12, 14, 16, 18, 20, 22, 24]
print(odd(sample_data))   # [11, 13, 15, 17, 19, 21, 23, 25]
