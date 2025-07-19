#lex_auth_012693774187716608134
def translate(bilingual_dict, english_words_list):
    swedish_words_list = []  # define inside the function
    for word in english_words_list:
        if word not in bilingual_dict:
            print(f"'{word}' is not present in the bilingual dictionary.")
            return swedish_words_list
        else:
            swedish_words_list.append(bilingual_dict[word])
    return swedish_words_list  # make sure to return the list


bilingual_dict= {"merry":"god", "christmas":"jul", "and":"och", "happy":"gott", "new":"nytt", "year":"ar"}
english_words_list=["merry","christmas"]
print("The bilingual dict is:",bilingual_dict)
print("The english words are:",english_words_list)

swedish_words_list=translate(bilingual_dict, english_words_list)
print("The equivalent swedish words are:",swedish_words_list)