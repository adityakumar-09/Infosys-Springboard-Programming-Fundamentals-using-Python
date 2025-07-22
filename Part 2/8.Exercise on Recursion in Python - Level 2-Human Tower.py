#lex_auth_01269437527007232044

# Recursive function to calculate total weight of the human pyramid
def human_pyramid(no_of_people):
    if no_of_people == 1:
        return 50  # Top person
    return no_of_people * 50 + human_pyramid(no_of_people - 2)

# Function to find the maximum number of people at the base within weight limit
def find_maximum_people(max_weight):
    no_of_people = 1  # Start with the smallest odd base
    while True:
        total_weight = human_pyramid(no_of_people)
        if total_weight > max_weight:
            return no_of_people - 2  # Return the last valid odd number
        no_of_people += 2  # Only odd numbers allowed

# Test the program with different max weight values
max_people = find_maximum_people(1000)
print(max_people)