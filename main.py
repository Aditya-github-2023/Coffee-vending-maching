from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

coffee_maker = CoffeeMaker()
menu = Menu()
money_machine = MoneyMachine()

should_continue = True
while should_continue:
    user = input(f"What would you like? {menu.get_items()}: ")
    if user == "off":
        should_continue = False
    elif user == "report":
        coffee_maker.report()
        money_machine.report()
    else:
        drink_name = menu.find_drink(user)
        if coffee_maker.is_resource_sufficient(drink_name) and money_machine.make_payment(drink_name.cost):
            coffee_maker.make_coffee(drink_name)
