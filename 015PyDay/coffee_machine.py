# Day 15: Coffee Machine

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

profit = 0

resource_values = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}


def print_report():
    print("----Current Report Status----")
    for key in resource_values:
        resource_name = key.capitalize()
        value = resource_values[key]
        print(f"{resource_name}: {value}")


def check_resources(coffee):
    missing_ingredients = []
    chosen_coffee_ingredients = MENU[coffee]["ingredients"]
    for key in chosen_coffee_ingredients:
        if chosen_coffee_ingredients[key] > resource_values[key]:
            missing_ingredients.append(key.capitalize())
    return missing_ingredients


def process_coins(coffee):
    cost_of_coffee = MENU[coffee]["cost"]
    print(f"It's ${cost_of_coffee}, please insert coins.")

    quarters = float(input("Quarters: "))
    dimes = float(input("Dimes: "))
    nickles = float(input("Nickles: "))
    pennies = float(input("Pennies: "))

    total_money = quarters*0.25 + dimes*0.10 + nickles*0.05 + pennies*0.01

    if total_money >= cost_of_coffee:
        if total_money > cost_of_coffee:
            change = round(total_money - cost_of_coffee, 2)
            print(f"Here is your change. ${change}.")
        global profit
        profit += cost_of_coffee
        return True
    else:
        print("Sorry that's not enough money.")
        return False


def deduct_ingredients(coffee):
    coffee_ingredients = MENU[coffee]["ingredients"]
    for key in coffee_ingredients:
        resource_values[key] -= coffee_ingredients[key]


def make_coffe(coffee_type):
    missing_resources = []
    missing_resources = check_resources(coffee_type)

    if len(missing_resources) == 0:
        if process_coins(coffee_type):
            deduct_ingredients(coffee_type)
            print(f"Here is your {coffee_type}. Enjoy!")
    else:
        missing_resources_list = " ".join(missing_resources)
        print(f"Sorry there is not enough {missing_resources_list}")


turned_on = True

while turned_on:
    next_action = input("What would you like? (espresso/latte/cappuccino) -> ")

    if next_action == "off":
        turned_on = False
        print("Bye bye!")
    elif next_action == "espresso" or next_action == "latte" or next_action == "cappuccino":
        print(f"{next_action} selected...")
        make_coffe(next_action)
    elif next_action == "report":
        print_report()
    else:
        print("Not a valid input. Try again.")


