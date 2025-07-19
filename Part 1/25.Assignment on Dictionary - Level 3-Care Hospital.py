#lex_auth_012693816757551104165

def max_visited_speciality(patient_medical_speciality_list,medical_speciality):
    count_dict = {"P": 0, "O": 0, "E": 0}
    for key in medical_speciality:
        for values in patient_medical_speciality_list:
            if key == values :
                count_dict[key] += 1


    max_speciality_code = max(count_dict, key=count_dict.get)
    return medical_speciality[max_speciality_code]

#provide different values in the list and test your program
patient_medical_speciality_list=[301,'O',302, 'O' ,305, 'P' ,401, 'O' ,656, 'E']
medical_speciality={"P":"Pediatrics","O":"Orthopedics","E":"ENT"}
speciality=max_visited_speciality(patient_medical_speciality_list,medical_speciality)
print(speciality)