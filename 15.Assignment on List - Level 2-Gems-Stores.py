#lex_auth_012693795044450304151

def calculate_bill_amount(gems_list, price_list, reqd_gems,reqd_quantity):
    bill_amount=0
    for gem, quantity in zip(reqd_gems, reqd_quantity):
        if gem not in gems_list:
            return -1  # Return -1 if any gem is not available in the store
        # Calculate the bill amount only for available gems
        if gem in gems_list:
            index = gems_list.index(gem)
            bill_amount += price_list[index] * quantity
        
    if bill_amount > 30000:
        bill_amount = bill_amount - (bill_amount * 0.05)  # Apply 5% discount 
        return bill_amount
    else:
        return bill_amount
#List of gems available in the store
gems_list=["Emerald","Ivory","Jasper","Ruby","Garnet"]

#Price of gems available in the store. gems_list and price_list have one-to-one correspondence
price_list=[1760,2119,1599,3920,3999]

#List of gems required by the customer
reqd_gems=["Ivory","Emerald","Garnet"]

#Quantity of gems required by the customer. reqd_gems and reqd_quantity have one-to-one correspondence
reqd_quantity=[3,10,12,]

bill_amount=calculate_bill_amount(gems_list, price_list, reqd_gems, reqd_quantity)
print(bill_amount)