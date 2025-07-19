#lex_auth_01269441913243238467

def create_largest_number(number_list):
    # Convert numbers to strings for concatenation comparison
    number_list = list(map(str, number_list))

    n = len(number_list)

    # Manual sorting using nested loops
    for i in range(n):
        for j in range(i + 1, n):
            # Compare concatenated forms
            if number_list[i] + number_list[j] < number_list[j] + number_list[i]:
                # Swap if placing j before i gives a larger result
                number_list[i], number_list[j] = number_list[j], number_list[i]

    # Join the list to form the largest number
    return int(''.join(number_list))

# Sample test
number_list = [10, 20, 32]
largest_number = create_largest_number(number_list)
print((largest_number))
