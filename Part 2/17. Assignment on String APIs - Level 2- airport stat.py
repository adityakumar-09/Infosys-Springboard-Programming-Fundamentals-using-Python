#lex_auth_0127382193364008961449

#Sample ticket list - ticket format: "flight_no:source:destination:ticket_no"
#Note: flight_no has the following format - "airline_name followed by three digit number

#Global variable
ticket_list=["AI567:MUM:LON:014","AI077:MUM:LON:056", "BA896:MUM:LON:067", "SI267:MUM:SIN:145","AI077:MUM:CAN:060","SI267:BLR:MUM:148","AI567:CHE:SIN:015","AI077:MUM:SIN:050","AI077:MUM:LON:051","SI267:MUM:SIN:146"]

def find_passengers_flight(airline_name="AI"):
    #This function finds and returns the number of passengers travelling in the specified airline.
    count=0
    for i in ticket_list:
        string_list=i.split(":")
        if(string_list[0].startswith(airline_name)):
            count+=1
    return count

def find_passengers_destination(destination):
    count=0
    for i in ticket_list:
        string_list=i.split(":")
        if(string_list[2].startswith(destination)):
            count+=1
    return count

def find_passengers_per_flight():
    '''Write the logic to find and return a list having number of passengers traveling per flight based on the details in the ticket_list
    In the list, details should be provided in the format:
    [flight_no:no_of_passengers, flight_no:no_of_passengers, etc.].'''
    flight_passenger_count = []
    flight_dict = {}
    for ticket in ticket_list:
        flight_no = ticket.split(":")[0]
        if flight_no in flight_dict:
            flight_dict[flight_no] += 1
        else:
            flight_dict[flight_no] = 1
    for flight_no, count in flight_dict.items():
        flight_passenger_count.append(f"{flight_no}:{count}")

def sort_passenger_list():
    '''Write the logic to sort the passenger list based on the flight number and return the sorted list.
    The list should be in the format: [flight_no:source:destination:ticket_no, flight_no:source:destination:ticket_no, etc.]'''
    sorted_ticket_list = sorted(ticket_list, key=lambda x: x.split(":")[0])
    return sorted_ticket_list


#Provide different values for airline_name and destination and test your program.
print(find_passengers_flight("AI"))
print(find_passengers_destination("LON"))
print(sort_passenger_list())