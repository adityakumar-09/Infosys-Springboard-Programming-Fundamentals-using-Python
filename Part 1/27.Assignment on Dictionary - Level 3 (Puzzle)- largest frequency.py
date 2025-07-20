#lex_auth_0127382283825971201450

def max_frequency_word_counter(data):
    word=""
    frequency=0
    words = data.lower().split()
    freq_dict = {}
    for w in words:
        freq_dict[w] = freq_dict.get(w, 0) + 1
    max_freq = max(freq_dict.values())
    max_words = [w for w, f in freq_dict.items() if f == max_freq]
    word = max(max_words, key=len)
    frequency = max_freq


    print(word,frequency)


#Provide different values for data and test your program.
data="Listen to the big clock Tick tock tick"
max_frequency_word_counter(data)