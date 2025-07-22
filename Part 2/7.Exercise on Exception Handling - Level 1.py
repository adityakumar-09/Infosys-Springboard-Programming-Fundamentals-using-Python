#lex_auth_01269437504257228837

def find_average(mark_list):
    try:
        total = 0
        for i in range(0, len(mark_list)):
            total += mark_list[i]  # Fixed the typo: mark_list1 → mark_list
        marks_avg = total / len(mark_list)
        return marks_avg
    except ZeroDivisionError:
        print("The list is empty. Cannot divide by zero.")
        return None
    except IndexError:
        print("Index error occurred.")
        return None
    except TypeError:
        print("Invalid data type in the list.")
        return None
    except Exception as e:
        print("An unexpected error occurred:", e)
        return None

# Sample call
m_list = [1, 2, 3, 4]
print("Average marks:", find_average(m_list))
print(find_average([15, 26, 34, 24]))