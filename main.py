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
    "money": 0
}


def report(res=resources):
    print(f"Water: {res['water']}ml")
    print(f"Milk: {res['milk']}ml")
    print(f"Coffee: {res['coffee']}g")
    print(f"Money: ${res['money']}")


def check_resources(user_choice, res=resources):
    if user_choice == 'espresso':
        if res['water'] < MENU[user_choice]['ingredients']['water'] or res['coffee'] < MENU[user_choice]['ingredients']['coffee']:
            return False
    else:
        for k in MENU[user_choice]['ingredients']:
            if res[k] < MENU[user_choice]['ingredients'][k]:
                return False
    return True


def process_coins(q=0.0, d=0.0, n=0.0, p=0.0):
    quarter = 0.25
    dime = 0.10
    nickles = 0.05
    pennies = 0.01
    return q * quarter + d * dime + n * nickles + p * pennies


def check_transaction(money, user_choice):
    if money < MENU[user_choice]['cost']:
        print("Sorry, that's not enough money. Money refunded.")
        return False
    elif money == MENU[user_choice]['cost']:
        resources['money'] += money
        return True
    else:
        change = money - MENU[user_choice]['cost']
        print(f"Here's your change: ${round(change, 2)}")
        resources['money'] += MENU[user_choice]['cost']
        return True


def make_coffee(user_choice):
    if user_choice == 'espresso':
        resources['water'] -= MENU[user_choice]['ingredients']['water']
        resources['coffee'] -= MENU[user_choice]['ingredients']['coffee']
    else:
        for k in MENU[user_choice]['ingredients']:
            resources[k] -= MENU[user_choice]['ingredients'][k]


def refill():
    for k in MENU['latte']['ingredients']:
        resources[k] += 500


def run():
    user_choice = input("What would you like? (espresso/latte/cappuccino/refill): ")
    if user_choice == 'off':
        print("Goodbye.")
        return
    elif user_choice == 'refill':
        refill()
        run()
    elif user_choice == 'report':
        report()
        run()
    elif user_choice not in ['espresso', 'latte', 'cappuccino']:
        print("Sorry, not a valid choice.")
        run()
    else:
        if check_resources(user_choice):
            print("Please insert coins.")
            quarter = float(input("How many quarters? "))
            dimes = float(input("How many dimes? "))
            nickles = float(input("How many dimes? "))
            pennies = float(input("How many pennies? "))
            money = process_coins(quarter, dimes, nickles, pennies)
            if check_transaction(money, user_choice):
                make_coffee(user_choice)
                print(f"Here is your {user_choice}. Enjoy!")
                run()
            else:
                run()
        else:
            print("Sorry, not enough resources.")
            run()


run()
