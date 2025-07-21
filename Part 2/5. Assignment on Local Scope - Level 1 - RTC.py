#lex_auth_012693816779112448160
Price_per_ticket = 80
milage_of_bus = 10
fuel_cost_per_litre = 70
def calculate(distance,no_of_passengers):
    fuel_cost = (distance / milage_of_bus) * fuel_cost_per_litre
    passengers_earning = no_of_passengers * Price_per_ticket
    if passengers_earning >= fuel_cost:
        return passengers_earning - fuel_cost  # Return profit if earnings are greater than fuel cost
    else:
        return -1
    
#Provide different values for distance, no_of_passenger and test your program
distance=20
no_of_passengers=50
print(calculate(distance,no_of_passengers))