#lex_auth_01269446157664256093

def check_prime(number):
    if number <= 1:
        return False
    for i in range(2, int(number**0.5) + 1):
        if number % i == 0:
            return False
    return True

def rotations(num):
    rotations_list = []
    num_str = str(num)
    for i in range(len(num_str)):
        i = i % len(num_str) # to handle cases where i exceeds the length of num_str
        rotations_list.append(int(num_str[i:] + num_str[:i]))
    return rotations_list

def get_circular_prime_count(limit):
    circular_prime = []
    for num in range(2, limit +1 ):
        if check_prime(num):
            is_circular_prime = True
            for rotation in rotations(num):
                if not check_prime(rotation):
                    is_circular_prime = False
                    break
            if is_circular_prime:
                circular_prime.append(num)
    return circular_prime

#Provide different values for limit and test your program
print(get_circular_prime_count(100))