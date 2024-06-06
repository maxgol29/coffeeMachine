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

global profit
profit = 0
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}
def making_coffe(type_of_coffee):
    for ingredient in resources.items():
        ingredient = list(ingredient)
        resources[ingredient[0]] -= MENU[type_of_coffee]['ingredients'][ingredient[0]]
    print(f"Here is your {type_of_coffee}. Enjoy!")


def input_money():
    quarters = int(input("How many quarters?: "))
    dimes = int(input("How many dimes?: "))
    nickel = int(input("How many nickels?: "))
    pennies = int(input("How many pennies?: "))
    return quarters * 0.25 + dimes * 10 + nickel * 0.05 + pennies * 0.01


def checking_resources_for_coffee(type_of_coffee):
    for ingredient in resources.items():
        if ingredient[1] < MENU[type_of_coffee]['ingredients'][ingredient[0]]:
            print(f"Sorry there is not enough {ingredient[0]}")
            return False
    return True


def show_resources(profit):
    for ingredient in resources.items():
        if ingredient[0] in ['water', 'milk']:
            print(f"{ingredient[0].capitalize()}: {ingredient[1]}ml", end='\n')
        elif ingredient[0] == 'coffee':
            print(f"{ingredient[0].capitalize()}: {ingredient[1]}mg", end='\n')
        else:
            print(f"{ingredient[0].capitalize()}: ${ingredient[1]}", end='\n')
    print(f"${profit}")


def coffee_machine_program(profit):
    processing = True
    while processing:
        prompt = input("What would you like?: espresso, latte, cappuccino? ")  # espresso, latte, cappuccino, off,
        # report
        if prompt == 'off':
            processing = False
            print("The machine was stopped")
        elif prompt == "report":
            show_resources(profit)
        else:
            if checking_resources_for_coffee(prompt):
                cost_of_coffee = MENU[prompt]['cost']
                print(f"${cost_of_coffee}")
                print("--------------------------")
                customer_money = input_money()
                print("--------------------------")
                print("--------------------------")
                if customer_money < cost_of_coffee:
                    processing = False
                    print("Sorry that's not enough money")
                elif customer_money > cost_of_coffee:
                    print(f"Here is ${float(customer_money) - float(cost_of_coffee)} dollars in change.")
                    making_coffe(prompt)
                    profit += MENU[prompt]['cost']
                else:
                    making_coffe(prompt)
                    profit += MENU[prompt]['cost']
            else:
                print("We don't have resources")


coffee_machine_program(profit)
