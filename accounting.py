MELON_COST = 1.00
#
def pay_status(filename):
    """calculates cost of melons and determines who has underpaid or"""
    
    data = open(filename)

    for line in data:
        order = line.split("|")
        
        full_name = order[1]
        # first_name = full_name.split(" ")[0] #splitting the two names here after the space to split name
        
        first_name, last_name = full_name.split(" ")
        melons_qnty = float(order[2]) #why float here -- because these are strings and need to be floats
        amnt_paid = float(order[3]) #how would i typecast as integer -- answered above

        expected_price = melons_qnty * MELON_COST
        # print customer paid this amount expected and expected price
        if expected_price < amnt_paid:
            print (f"{full_name} paid ${amnt_paid}, expected", f"{expected_price: .2f}")
            print(f"{full_name} has overpaid for their melons.")
        
        elif expected_price > amnt_paid:
            print (f"{full_name} paid ${amnt_paid}, expected", f"{expected_price: .2f}")
            print(f"{full_name} owes me money.")    


    data.close()

pay_status("customer-orders.txt")
