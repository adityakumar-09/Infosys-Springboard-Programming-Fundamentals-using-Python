#lex_auth_01269446533799116898

def check_perfect_number(number):
    if number < 1:
        return False
    sum_of_divisors = 0
    for i in range(1, int(number)):
        if number % i == 0:
            sum_of_divisors += i
    return sum_of_divisors == number

def check_perfectno_from_list(no_list):
    super_numbers = []
    for i in no_list:
        if check_perfect_number(i):
            super_numbers.append(i)
    return super_numbers

perfectno_list=check_perfectno_from_list([18,6,4,2,1,28])
print(perfectno_list)


