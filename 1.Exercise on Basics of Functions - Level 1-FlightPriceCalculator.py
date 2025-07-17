#lex_auth_01269361601342668881
def calculate_total_ticket_cost(no_of_adults, no_of_children):
    total_ticket_cost=0
    Ticket_Cost = (no_of_adults*37550.0) + (no_of_children*(37550.0/3))
    Ticket_Cost_Taxed = Ticket_Cost + (Ticket_Cost * 0.07)
    total_ticket_cost = Ticket_Cost_Taxed - (Ticket_Cost_Taxed * 0.1)
    return total_ticket_cost


#Provide different values for no_of_adults, no_of_children and test your program
total_ticket_cost=calculate_total_ticket_cost(5,2)
print("Total Ticket Cost:",total_ticket_cost)