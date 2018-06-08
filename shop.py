####################### DO NOT MODIFY THIS CODE ########################
menu = {
    "original cupcake": 2,
    "signature cupcake": 2.750,
    "coffee": 1,
    "tea": 0.900,
    "bottled water": 0.750
}
original_flavors = ["vanilla", "chocolate", "strawberry", "caramel", "raspberry"]
original_price = 2
signature_price = 2.750

############################# Start Here! ##############################
cupcake_shop_name = "Tony's"
signature_flavors = ["dark chocolate","milk chocolate","explosion", "swirl molten", "chocolate matcha"]
order_list=[]

def print_menu():
    """
    Print the items in the menu dictionary.
    """
    print("Our menu:")
    print()
    for  item in menu:
        print (item, "(KD %s)" % menu[item])
    print("_____________")


def print_originals():
    """
    Print the original flavor cupcakes.
    """
    print("Our original flavor cupcakes (KD %s each):" % original_price)
    print()
    [print(x)for x in original_flavors]
    print("_____________")


def print_signatures():
    """
    Print the signature flavor cupcakes.
    """
    print("Our signature flavor cupcake (KD %s each):" % signature_price)
    print()
    [print(x) for x in signature_flavors]
    print("_____________")


def is_valid_order(order):
    """
    Check if an order exists in the shop.
    """
    if order in menu or order in signature_flavors or order in original_flavors:
        return True
    else:
        return False 


def get_order():
    """
    Repeatedly ask customer for order until they end their order by typing "Exit".
    """
    print()
    print("Hello, welcome to Tony's!")
    order= input("Enter items from the menu with the exact spelling. Write 'Exit' when done.\n")
    while order.lower() != "exit":
        if is_valid_order(order) == True:
            order_list.append(order)
            order= input("What else would you like?")
    if  order.lower() == "exit":
        print_order(order_list)
        return
    else:
         order= input("Sorry, this item is not on the menu. What would you like?")
   

def accept_credit_card(total):
    """
    Return whether an order is eligible for credit card payment.
    """
    #minimum 2.5 kd
    if total >= 2.5:
        return("Your order is eligible for for credit card payment.")
    else:
        return("Your order does not meet the credit card minimum. Please use cash payment.")


def get_total_price(order_list):
    """
    Calculate and return total price of the order.
    """
    total = 0
    for order in order_list:
        if order in menu:
            total+= menu[order]
        if order in original_flavors:
            total += original_price
        if order in signature_flavors:
            total +=  signature_price
    return total


def print_order(order_list):
    """
    Print the order of the customer.
    """
    print()
    print("Your order is:")
    # your code goes heret
    
    for order in order_list:
        print("- %s" % order)
    total = get_total_price(order_list)
    print("total: %s" % (str(total)))
    print(accept_credit_card(total))
    print("Thank you for shopping with us!")
    print(cupcake_shop_name)