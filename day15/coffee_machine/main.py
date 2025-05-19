MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
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
    "money" : 0,
}


def print_report():
    """Prints the resource values of the coffee machine"""
    print(f"Water is {resources['water']} ml")
    print(f"Milk is {resources['milk']} ml")
    print(f"Coffee is {resources['coffee']} gm")
    print(f"Money is ${resources['money']}")

def process_coins():
    """Returns the total calculated from the coins inserted and their values"""
    print("Please insert coins ")
    total = int(input("how many quarters? ")) * 0.25
    total += int(input("how many dimes? ")) * 0.1
    total += int(input("how many nickels? ")) * 0.05
    total += int(input("how many pennies? ")) * 0.01
    return total


def is_resource_sufficient(order_ingredients):
    """Returns true when order can be made, False when resources are insufficient"""
    is_enough = True
    for item in order_ingredients:
        if order_ingredients[item] >= resources[item]:
            print(f"Sorry there isn't enough {item}")
            is_enough = False
    return is_enough

def is_transaction_successful(money_received, actual_cost):
    """Return True of the payment is accepted, else return False """
    if money_received >= actual_cost:
        change = round(money_received - actual_cost, 2)
        print(f"Here is your change ${change}")
        resources['money'] += actual_cost
        return True
    else:
        print("Sorry that isn't enough money. Money refunded.")
        return False

def make_coffee(drink_name, order_ingredients):
    """Deduct the required ingredients from resources """
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"Here is your drink {drink_name} ☕")

is_on = True
while is_on:
    coffee_choice = input("What would you like to have? (espresso/latte/cappuccino) ").lower()
    if coffee_choice == "off":
        is_on = False
    elif coffee_choice == "report":
        print_report()
    else:
        drink = MENU[coffee_choice]
        if is_resource_sufficient(drink['ingredients']):
            payment = process_coins()
            if is_transaction_successful(payment, drink['cost']):
                make_coffee(coffee_choice, drink['ingredients'])

