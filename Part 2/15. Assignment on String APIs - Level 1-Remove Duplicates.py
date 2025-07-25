#lex_auth_01269446319507046499

# def remove_duplicates(value):
#     new_string = ""
#     seen = [] # To track characters already added
#     for char in value:
#         if char not in seen:
#             new_string += char
#             seen.append(char)  # Add the character to the set
#     return new_string

from collections import OrderedDict
def remove_duplicates(value):
    # Using OrderedDict to maintain order and remove duplicates
    return ''.join(OrderedDict.fromkeys(value))
print(remove_duplicates("11223445566666ababzzz@@@123#*#*"))
