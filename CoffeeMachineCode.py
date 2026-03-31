MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "milk": 0,
            "coffee": 18,
        },
        "cost": 1.5,
    },

    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

def report():
    print("Resources left: ")
    print(f"Water: {resources["water"]}")
    print(f"Milk: {resources["milk"]}")
    print(f"Coffee: {resources["coffee"]}")
    print(f"Total amount: {total_amount}")

def check_resources(order1):
    if resources["water"]<MENU[order1]["ingredients"]["water"]:
        print("There is not enough water")
        return False
    if resources["milk"]<MENU[order1]["ingredients"]["milk"]:
        print("there is not enough milk")
        return False
    if resources["coffee"]<MENU[order1]["ingredients"]["coffee"]:
        print("There is not enough coffee")
        return False
    return True

def check_balance(payed_amount, order):
    if payed_amount>MENU[order]["cost"]:
        print(f"Here is your change of ${round(payed_amount-MENU[order1]["cost"], 2)}")

def deduct_ingredients(order1, amount):
    global total_amount
    resources["water"] -= MENU[order1]["ingredients"]["water"]
    resources["milk"] -= MENU[order1]["ingredients"]["milk"]
    resources["coffee"] -= MENU[order1]["ingredients"]["coffee"]
    total_amount +=MENU[order1]["cost"]
    check_balance(amount, order1)

def make_order(order1, amount):
    if order1 in ["espresso", "latte", "cappuccino"]and amount>=MENU[order1]["cost"]:
        if check_resources(order1) == True:
            deduct_ingredients(order1, amount)
            print(f"You {order1} has been served! enjoy!")
    # elif order == "report":
    #     report()
    # elif order == "off":
    #     continue_or_not=False

def take_input(order1):
    print("Enter the number of coins: ")
    quarter=int(input("quarters: "))
    dime=int(input("dimes: "))
    nickle=int(input("nickles: "))
    penny=int(input("pennies: "))
    payed_amount= (penny * 0.01) + (dime * 0.10) + (nickle * 0.05) + (quarter * 0.25)
    if payed_amount<MENU[order1]["cost"]:
        print(f"Not enough amount, Here is your refund of {payed_amount} dollars")
    else:
        print(f"total amount payed: {payed_amount}")

    make_order(order1, payed_amount)



#start of the program

total_amount=0
continue_or_not=True

while continue_or_not:
    while True:
        order1= input("What would you like to order(espresso/latte/cappuccino)? ").lower()
        if order1 in ["espresso", "latte", "cappuccino"]:
            take_input(order1)
            break
        elif order1 == "report":
            report()
        elif order1 == "off":
            # global continue_or_not
            continue_or_not = False
            break
        else:
            print("Type a valid order")





