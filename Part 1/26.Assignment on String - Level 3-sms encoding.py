#lex_auth_01269444961482342489

def sms_encoding(data):
    vowels = "aeiouAEIOU"
    sms_list = data.split()
    sms_encoded = []
    
    for word in sms_list:
        # If all characters in word are vowels, keep it as-is
        if all(char in vowels for char in word):
            sms_encoded.append(word)
        else:
            # Else, keep only consonants
            encoded_word = ""
            for char in word:
                if char not in vowels:
                    encoded_word += char
            sms_encoded.append(encoded_word)
    
    return ' '.join(sms_encoded)

# Test cases
data = ["I love Python", "I will not repeat mistakes", "MSD says I love cricket and tennis too"]
for i in data: 
    print(sms_encoding(i))