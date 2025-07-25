#lex_auth_01269443477535129681

def find_duplicates(input_list):
    from collections import Counter

    freq = Counter(input_list)  # Count occurrences
    duplicates = []
    added = set()

    for num in input_list:
        if freq[num] > 1 and num not in added:
            duplicates.append(num)
            added.add(num)

    return duplicates

print(find_duplicates([12,54,68,759,24,15,12,68,987,758,25,69]))