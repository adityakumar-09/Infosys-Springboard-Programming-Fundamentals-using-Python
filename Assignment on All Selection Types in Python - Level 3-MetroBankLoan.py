#lex_auth_012693788748742656146

def calculate_loan(account_number,salary,account_balance,loan_type,loan_amount_expected,customer_emi_expected):
    eligible_loan_amount=0
    bank_emi_expected=0
    eligible_loan_amount=0
    
    if len(str(account_number)) != 4 or str(account_number)[0] != '1':
        print("Invalid account number")
        return
    if account_balance < 100000:
        print("Insufficient account balance")
        return

    if loan_type == "Car" and salary > 25000:
        eligible_loan_amount = 500000
        bank_emi_expected = 36
    elif loan_type == "House" and salary > 50000:
        eligible_loan_amount = 6000000
        bank_emi_expected = 60
    elif loan_type == "Business" and salary > 75000:
        eligible_loan_amount = 7500000
        bank_emi_expected = 84
    else:
        print("Invalid loan type or salary")
        return

    # Step 4: Check if customer's request is within limits
    if loan_amount_expected <= eligible_loan_amount and customer_emi_expected <= bank_emi_expected:
        print("Account number:", account_number)
        print("The customer can avail the amount of Rs.", eligible_loan_amount)
        print("Eligible EMIs :", bank_emi_expected)
        print("Requested loan amount:", loan_amount_expected)
        print("Requested EMI's:", customer_emi_expected)
    else:
        print("The customer is not eligible for the loan")

#Test your code for different values and observe the results
calculate_loan(1001,40000,250000,"Car",300000,30)
calculate_loan(1001,40000,250000,"Car",300000,40)