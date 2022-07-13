from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()


def run():
    user_choice = input(f"What would you like? ({menu.get_items()}off) ")
    if user_choice == 'off':
        print("Goodbye")
        return
    elif user_choice == 'report':
        coffee_maker.report()
        run()
    elif user_choice not in ['espresso', 'latte', 'cappuccino']:
        print("Sorry, not a valid choice.")
        run()
    else:
        menu_item = menu.find_drink(user_choice)
        if coffee_maker.is_resource_sufficient(menu_item) and money_machine.make_payment(menu_item.cost):
            coffee_maker.make_coffee(menu_item)
        run()


run()
