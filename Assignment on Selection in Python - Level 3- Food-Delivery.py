#lex_auth_012693782475948032141

def calculate_bill_amount(food_type, quantity_ordered, distance_in_kms):
    bill_amount = 0
    
    # Validation
    if food_type not in ('V', 'N') or quantity_ordered < 1 or distance_in_kms <= 0:
        return -1
    
    # Food cost
    if food_type == 'V':
        food_cost = 120 * quantity_ordered
    else:
        food_cost = 150 * quantity_ordered

    # Delivery charge calculation
    if distance_in_kms <= 3:
        delivery_charge = 0
    elif distance_in_kms <= 6:
        delivery_charge = (distance_in_kms - 3) * 3
    else:
        delivery_charge = (3 * 3) + ((distance_in_kms - 6) * 6)

    # Final bill
    bill_amount = food_cost + delivery_charge
    
    return bill_amount

# Test examples
bill_amount = calculate_bill_amount("N", 2, 7)
print(bill_amount)
