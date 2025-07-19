def make_amount(rupees_to_make,no_of_five,no_of_one):
    five_needed=min(rupees_to_make//5,no_of_five)
    one_needed= rupees_to_make - (five_needed * 5)
    if one_needed<=no_of_one:
        print("No. of Five needed :", five_needed)
        print("No. of One needed  :", one_needed)
    else:
        print(-1)


#Provide different values for rupees_to_make,no_of_five,no_of_one and test your program
make_amount(21,4,2)
make_amount(11,2,11)
make_amount(19,3,3)