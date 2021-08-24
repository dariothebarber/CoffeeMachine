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
    "money": 0.0,
}

def make_drink(order, ingredients):
    
    resources["water"] = resources["water"] - ingredients["water"]
    resources["coffee"] = resources["coffee"] - ingredients["coffee"]
    if order == "espresso":
        return
    else:
        resources["milk"] = resources["milk"] - ingredients["milk"]
        return


def process_transaction(drink_cost, money_entered):
    if money_entered > drink_cost :
        print(f"Your refund is ${round(money_entered - drink_cost,2)}")
        resources["money"] += (drink_cost)
    else:
        print(f"Thank you for your order.  Here's you {choice}")


def enter_money(drink):
    quarters_val = input("how many quarters : ")
    dimes_val = input("how many dimes : ")
    nickles_val = input("how many nickles : ")
    pennies_val = input("how many pennies : ")
    tot_money = (float(quarters_val)*.25) + (float(dimes_val)*.1) + (float(nickles_val)*.2) + (float(pennies_val)*.01)

    if float(tot_money) >= drink["cost"]:
        return process_transaction(drink["cost"], tot_money)
    else:
        print("Insufficient funds")
        return False



def check_resources(order_ingredients):
    for item in order_ingredients:
        if order_ingredients[item] >= resources[item]:
            print(f"Sorry there is not enough {item}")
            return False
    return True

machine_on = True

while (machine_on):
    choice = input("What would you like? (espresso/latte/cappuccino):").lower()
    
    #Turning off program if secret word is used
    if choice == "off":
        machine_on = False
        exit()
    
    #Print report
    elif choice == "report":
        print("Water : {0}ml" .format(resources["water"]))
        print("Milk : {0}ml" .format(resources["milk"]))
        print("Coffee : {0}g" .format(resources["coffee"]))
        print("Money : ${0}" .format(resources["money"]))

    elif choice == "espresso" or choice == "latte" or choice == "cappuccino":
        drink = MENU[choice]
        
        if check_resources(drink["ingredients"]):
            enter_money(drink)
            make_drink(choice, drink["ingredients"])
            print(f"Transaction complete. Enjoy your {choice}!")

    
    else:
        print("Not a valid input")

