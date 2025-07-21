#lex_auth_01269438947391897654

#Global variable
list_of_marks=(12,18,25,24,2,5,18,20,20,21)

def find_more_than_average():
    average = sum(list_of_marks) / len(list_of_marks)
    cout = 0
    for mark in list_of_marks:
        if mark > average:
            cout += 1
    Percentage_of_studetnts = (cout / len(list_of_marks)) * 100
    return Percentage_of_studetnts
    

def sort_marks():
    sorted_marks = sorted(list_of_marks)
    return sorted_marks

def generate_frequency():
    frequency_dict = {}
    for mark in list_of_marks:
        frequency_dict[mark] = frequency_dict.get(mark, 0) + 1
    return list(frequency_dict.items())

print(find_more_than_average())
print(generate_frequency())
print(sort_marks())