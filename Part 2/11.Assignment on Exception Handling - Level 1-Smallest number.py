#lex_auth_01269442760027340879

import math

def find_smallest_number(num):
    #start writing your code here
    try:
        if not isinstance(num, int) or num <= 0:
            raise ValueError("Input must be a positive integer.")

        def count_divisors(n):
            count = 0
            for i in range(1, int(math.isqrt(n)) + 1):
                if n % i == 0:
                    if i == n // i:
                        count += 1
                    else:
                        count += 2
            return count

        candidate = 1
        while True:
            if count_divisors(candidate) == num:
                return candidate
            candidate += 1

    except Exception as e:
        print("Error:", e)
        return None

# Do not change the code below
num = 16
print("The number of divisors :", num)
result = find_smallest_number(num)
print("The smallest number having", num, "divisors:", result)
