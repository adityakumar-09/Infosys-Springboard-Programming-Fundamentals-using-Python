#lex_auth_01269442963365068878

def find_factors(num):
    #Accepts a number and returns the list of all the factors of a given number
    factors = []
    for i in range(2,(num+1)):
        if(num%i==0):
            factors.append(i)
    return factors

def is_prime(num, i):
    #Accepts the number num and num/2 --> i and returns True if the number is prime ,else returns False
    if(i==1):
        return True
    elif(num%i==0):
        return False
    else:
        return(is_prime(num,i-1))

def find_largest_prime_factor(list_of_factors):
    #Accepts the list of factors and returns the largest prime factor from the list
    largest_prime = 0 #This creates a variable largest_prime and sets its value to 0.
    for factor in list_of_factors: #This for loop goes through each number in the list one by one.
        if is_prime(factor, factor//2): #This line checks whether the current factor is a prime number.
            if factor > largest_prime: #If the current factor is a prime number and greater than the current largest_prime, it updates largest_prime.
                largest_prime = factor  #This line updates the value of largest_prime to the current factor.
    return largest_prime 
    

def find_f(num):
    #Accepts the number and returns the largest prime factor of the number
    factors = find_factors(num)
    return find_largest_prime_factor(factors)

def find_g(num):
    #Accepts the number and returns the sum of the largest prime factors of the 9 consecutive numbers starting from the given number
    sum_of_largest_primes = 0
    for i in range(num, num + 9):
        largest_prime = find_f(i)
        sum_of_largest_primes += largest_prime
    return sum_of_largest_primes
#Note: Invoke function(s) from other function(s), wherever applicable.

print(find_g(10))