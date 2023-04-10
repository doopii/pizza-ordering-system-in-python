# LIST
list_type_topping = {"1" , "2" , "3" , "4" , "5"}
selected_topping = []
order_pizza = '1'

# FUNCTION
# menu base
def menu_base():
    print("This is the pizza base we have.")
    print("=" * 41)
    print("|".ljust(1), "Types of base".ljust(10), "|".rjust(7), "Price".ljust(10), "|".rjust(6))
    print("=" * 41)
    print("|".ljust(1), "1 - Thick".ljust(10), "|".rjust(10), "RM11".ljust(10), "|".rjust(6))
    print("|".ljust(1), "2 - Thin".ljust(10), "|".rjust(10), "RM12".ljust(10), "|".rjust(6))
    print("=" * 41)


# menu topping
def menu_topping():
    print("This is our menu for topping.")
    print("="*43)
    print("["+str("No"),"Types of topping".ljust(10),"|".rjust(4),"Price".ljust(6),"]".rjust(10))
    print("="*43)
    print("|"+str("1."),"Pepperoni".ljust(10),"|".rjust(10),"RM3".ljust(10),"|".rjust(6))
    print("|"+str("2."),"Chicken".ljust(10),"|".rjust(10),"RM4".ljust(10),"|".rjust(6))
    print("|"+str("3."),"Extra cheese".ljust(10),"|".rjust(8),"RM3.50".ljust(10),"|".rjust(6))
    print("|"+str("4."),"Mushrooms".ljust(10),"|".rjust(10),"RM2".ljust(10),"|".rjust(6))
    print("["+str("5."),"Olives".ljust(10),"|".rjust(10),"RM2".ljust(10),"]".rjust(6))
    print("="*43)
    
# invalid value
def error():
    print("Undefined , please try again.")

# welcoming
print("Hello. Welcome to our Pizza shop!")

while order_pizza == "1":
    # choose base
    menu_base()
    base = input("Choose your base of pizza \n= ")
    while base not in ['1', '2']:
        error()
        base = input("Choose your base of pizza \n= ")

    if base == '1':
        base = "thick"
        thick_quantity, thick_total, thin_quantity, thin_total = [1, 11, 0, 0]

    elif base == '2':
        base = "thin"
        thick_quantity, thick_total, thin_quantity, thin_total = [0, 0, 1, 12]

    print(f"You have selected {base} pizza base.")

    # order topping
    pep_qty = 0
    chicken_qty = 0
    cheese_qty = 0
    mushrooms_qty = 0
    olive_qty = 0
    num_topping = 0
    print("All pizzas come with tomato and cheese toppings as standard.")
    print("You can only add up to 3 toppings, no more additional toppings can be chosen!")
    order_topping = input("Would you like to add any extra topping? \n1 - Yes \n2 - no \n= ")
    while order_topping not in ['1', '2']:
        error()
        order_topping = input("Would you like to add any extra topping? \n1 - Yes \n2 - no \n= ")
        
    while order_topping == "1":
        menu_topping()
        topping = input("Enter an extra topping: ")
        while topping not in list_type_topping:
            error()
            topping = input("Enter an extra topping: ")

        num_topping += 1
        if num_topping == 3:
            order_topping = '2'

        if topping == "1":
            pep_qty += 1
        elif topping == "2":
            chicken_qty += 1
        elif topping == "3":
            cheese_qty += 1
        elif topping == "4":
            mushrooms_qty += 1
        else:
            olive_qty += 1

        print(f"{topping} is selected as the extra topping.")
        if num_topping < 3:
            order_topping = input("Would you like to add any extra topping? \n1 - Yes \n2 - no \n= ")
            while order_topping not in ['1', '2']:
                error()
                order_topping = input("Would you like to add any extra topping? \n1 - Yes \n2 - no \n= ")

    else:
        total_pep = pep_qty * 3
        total_chicken = chicken_qty * 4
        total_cheese = cheese_qty * 3.5
        total_mushrooms = mushrooms_qty * 2
        total_olive = olive_qty * 2
        total = thin_total + thick_total + total_pep + total_chicken + total_cheese + total_mushrooms + total_olive

        print("This is the receipt for your pizza.")
        print("-" * 64)
        print("Types of topping".ljust(25),"Price".ljust(10),"Quantity".ljust(15),"Total(RM)")
        print("-" * 64)
        print("Thin pizza".ljust(25), "RM12".ljust(10), str(thin_quantity).ljust(15), thin_total)
        print("Thick pizza".ljust(25), "RM11".ljust(10), str(thick_quantity).ljust(15), thick_total)

        print("Pepperoni".ljust(25), "RM3".ljust(10), str(pep_qty).ljust(15), total_pep)
        print("Chicken".ljust(25), "RM4".ljust(10), str(chicken_qty).ljust(15), total_chicken)
        print("Extra cheese".ljust(25), "RM3.50".ljust(10), str(cheese_qty).ljust(15), total_cheese)
        print("Mushrooms".ljust(25), "RM2".ljust(10), str(mushrooms_qty).ljust(15), total_mushrooms)
        print("Olives".ljust(25), "RM2".ljust(10), str(olive_qty).ljust(15), total_olive)
        print("-" * 64)
        print("Total amount:RM", total)
        print("-" * 64)

        order_pizza = input("Would you like to order another pizza? \n1 - Yes \n2 - no \n= ")
        while order_pizza not in ['1', '2']:
            error()
            order_pizza = input("Would you like to order another pizza? \n1 - Yes \n2 - no \n= ")

else:
    print("Thank you!")
