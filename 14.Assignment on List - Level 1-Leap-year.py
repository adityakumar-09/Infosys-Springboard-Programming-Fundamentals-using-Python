#lex_auth_012693797166096384149

def find_leap_years(given_year):
    list_of_leap_years = []
    while len(list_of_leap_years) < 15:
        year=given_year
        if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
            list_of_leap_years.append(year)
        given_year += 1

    return list_of_leap_years

list_of_leap_years=find_leap_years(2000)
print(list_of_leap_years)