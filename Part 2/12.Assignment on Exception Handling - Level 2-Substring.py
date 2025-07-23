#lex_auth_01269442545042227276

def find_ten_substring(num_str):
    ten_substrings = []
    try:
        # Input validation: Check if the input is a string
        if not isinstance(num_str, str):
            raise TypeError("Input must be a string.")

        # Input validation: Check if the string contains only digits
        if not num_str.isdigit():
            raise ValueError("Input string must contain only digits.")

        n = len(num_str)

        # Iterate through all possible starting positions of a substring
        for i in range(n):
            current_sum = 0
            # Iterate through all possible ending positions for the current starting position
            for j in range(i, n):
                # Convert the current character to an integer digit
                digit = int(num_str[j])
                current_sum += digit

                # If the sum equals 10, add the substring to our list
                if current_sum == 10:
                    ten_substrings.append(num_str[i : j + 1])
                # Optimization: If the sum exceeds 10, any further extension
                # of this substring (by adding more non-negative digits)
                # will also exceed 10. So, we can break the inner loop.
                elif current_sum > 10:
                    break
    except (TypeError, ValueError) as e:
        # Catch specific input-related errors
        print(f"Error: {e}")
        return []  # Return an empty list on error
    except Exception as e:
        # Catch any other unexpected errors
        print(f"An unexpected error occurred: {e}")
        return []
    return ten_substrings

num_str="2825302"
print("The number is:",num_str)
result_list=find_ten_substring(num_str)
print(result_list)
