#lex_auth_012693763253788672132

def generate_ticket(airline,source,destination,no_of_passengers):
    ticket_number_list=[]
    src = source[:3].upper()
    dest = destination[:3].upper()
    for i in range(no_of_passengers):
        ticket_number = f"{airline}:{src}:{dest}:{101+i}"
        ticket_number_list.append(ticket_number)

    #Use the below return statement wherever applicable
    return ticket_number_list[-5:]  # Return the last 5 ticket numbers

#Provide different values for airline,source,destination,no_of_passengers and test your program
print(generate_ticket("AI","Bangalore","London",7))
print(generate_ticket("BA","Australia","France",2))