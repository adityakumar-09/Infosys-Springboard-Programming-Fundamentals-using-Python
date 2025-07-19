#lex_auth_012693810762121216155

def solve(heads, legs):
    error_msg = "No solution"
    chicken_count = 0
    rabbit_count = 0

    if (legs - 2 * heads) % 2 != 0:
        print(error_msg)
        return

    rabbit_count = (legs - 2 * heads) // 2
    chicken_count = heads - rabbit_count

    if rabbit_count < 0 or chicken_count < 0:
        print(error_msg)
    else:
        print(chicken_count, rabbit_count)

# Test cases
solve(150, 400)   # Output: 100 50
solve(3, 11)      # Output: No solution
solve(3, 12)      # Output: 0 3
solve(5, 10)      # Output: 5 0
solve(38, 131)    # Output: No solution
