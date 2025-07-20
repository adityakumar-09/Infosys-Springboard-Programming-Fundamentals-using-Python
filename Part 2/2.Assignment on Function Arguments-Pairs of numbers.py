#lex_auth_01269438594930278448

def find_pairs_of_numbers(num_list, n):
    seen = set()
    pairs = set()

    for num in num_list:
        complement = n - num
        if complement in seen:
            pairs.add(tuple(sorted((num, complement))))
        seen.add(num)

    return len(pairs)

num_list=[1, 2, 4, 5, 6]
n=6
print(find_pairs_of_numbers(num_list,n))