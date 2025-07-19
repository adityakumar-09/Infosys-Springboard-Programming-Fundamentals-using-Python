#lex_auth_01269444195664691284

def encrypt_sentence(sentence):
    words = sentence.split()
    encrypted_words = []

    vowels = "aeiouAEIOU"

    for index, word in enumerate(words): 
        if index % 2 == 0:
            # Odd position (1st, 3rd, etc. → index 0, 2, ...) → Reverse
            encrypted_words.append(word[::-1])
        else:
            # Even position (2nd, 4th, etc. → index 1, 3, ...) → Consonants then vowels
            consonants = ''.join([ch for ch in word if ch not in vowels])
            only_vowels = ''.join([ch for ch in word if ch in vowels])
            encrypted_words.append(consonants + only_vowels)

    return ' '.join(encrypted_words)

sentence="The sun rises in the east"
encrypted_sentence=encrypt_sentence(sentence)
print(encrypted_sentence)