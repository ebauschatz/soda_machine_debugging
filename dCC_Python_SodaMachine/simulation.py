from customer import Customer
from backpack import Backpack
from soda_machine import SodaMachine
import user_interface

class Simulation:
    def __init__(self):
        pass

    def run_simulation(self):
        """The central method called in main.py."""
        customer = Customer()
        soda_machine = SodaMachine()
        backpack = Backpack()
        will_proceed = False
        while will_proceed:
            user_option = user_interface.simulation_main_menu()
            if user_option == "1":
                soda_machine.begin_transaction(customer)
            elif user_option == "2":
                customer.check_coins_in_wallet()
            elif user_option == "3":
                customer.check_backpack(backpack)
            else:
                will_proceed = False