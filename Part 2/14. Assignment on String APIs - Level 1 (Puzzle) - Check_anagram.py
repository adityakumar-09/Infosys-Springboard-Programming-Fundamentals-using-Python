#lex_auth_0127382206342184961397

# def check_anagram(data1,data2):
#     #start writing your code here
#     data1 = data1.lower()
#     data2 = data2.lower()
#     if len(data1) != len(data2):
#         return False
#     elif sorted(data1) == sorted(data2):
#         return True
#     else:
#         return False


# alternatively, you can use the Counter class from the collections module to check for anagrams:
from collections import Counter
def check_anagram(word1, word2):
    return Counter(word1.lower()) == Counter(word2.lower())


print(check_anagram("eat","tea"))

