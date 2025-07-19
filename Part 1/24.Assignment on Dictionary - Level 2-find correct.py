#lex_auth_01269444890062848087

def find_correct(word_dict):
    result = [0, 0, 0] # [CORRECT, ALMOST CORRECT, WRONG]
    for word, correct_word in word_dict.items():
        if word == correct_word:
            result[0] += 1
        elif len(word) != len(correct_word):
            result[2] += 1
        else:
            mismatch_count =0
            for i in range(len(word)):
                if word[i] != correct_word[i]:
                    mismatch_count += 1
            if mismatch_count <= 2:
                result[1] += 1
            else:
                result[2] += 1
         
    
    return result
word_dict={"THEIR": "THEIR","BUSINESS":"BISINESS","WINDOWS":"WINDMILL","WERE":"WEAR","SAMPLE":"SAMPLE"}
print(find_correct(word_dict))