import decimal
import os

import colorama
from models.currencies import Currency
from models.customers import Customer
from models.products import Product
from models.purchases import Buy, Check
# Greeter is a terminal application that greets old friends warmly,
#   and remembers new friends.


### FUNCTIONS ###

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

    @classmethod
    def print_success(cls, msg):
        """
        Print message using green color text.
        """
        print(cls.OKGREEN + str(msg) + cls.ENDC)

    @classmethod
    def print_fail(cls, msg):
        """
        Print message using red color text.
        """
        print(cls.FAIL + str(msg) + cls.ENDC)


class Ecommerce:
    @staticmethod
    def display_title_bar():
        """
        Display a title bar in console.       
        """    
        print("\t**********************************************")
        print("\t***  Ecommerce  ***")
        print("\t**********************************************")
        
    @staticmethod
    def add_product():
        """
        Add new product.
        """
        name = input("\nProduct name:\n")
        cost = input("\nProduct cost:\n")
        price = input("\nProduct price:\n")
        weight = input("\nProduct weight:\n")
        try:
            product = Product(name, cost, price, weight)
            bcolors.print_success('{} was successfully added to product list!'.format(product.name))
        except ValueError as e:
            bcolors.print_fail(str(e))

    @staticmethod
    def add_customer():
        """
        Add new customer.
        """
        name = input("\nCustomer name:\n")
        discount = input("\nCustomer discount:\n")
        currency = input("\nCustomer currency:\n")
        try:
            customer = Customer(name, discount, currency)
            bcolors.print_success('{} was successfully added to customer list!'.format(customer.name))
        except ValueError as e:
            bcolors.print_fail(str(e))

    @staticmethod
    def make_sale():
        """
        Make a sale of product to customer.
        """
        Customer.print_all()
        customer_id = input("\nCustomer id:\n")
        Product.print_all()
        product_id = input("\nProduct id:\n")
        quantity = input("\nQuantity\n")
        try:
            customer = Customer.get_by_id(customer_id)
            check = customer.purchase(product_id, quantity)
            bcolors.print_success(check)
        except ValueError as e:
            bcolors.print_fail(str(e))

    @staticmethod
    def product_list():
        """
        List all entered products.
        """
        Product.print_all()

    @staticmethod
    def customer_list():
        """
        List all entered customers.
        """
        Customer.print_all()

    @staticmethod
    def run():
        """
        Main program method.
        """
        colorama.init()
        choice = ''
        while choice != 'q':    
            Ecommerce.display_title_bar()

            print("\n[1] Add new product.")
            print("[2] Add new customer.")
            print("[3] Make a sale.")
            print("[4] Products list.")
            print("[5] Customers list.")
            print("[q] Quit.")
            
            choice = input("What would you like to do? ")
            
            if choice == '1':
                Ecommerce.add_product()
            elif choice == '2':
                Ecommerce.add_customer()
            elif choice == '3':
                Ecommerce.make_sale()
            elif choice == '4':
                Ecommerce.product_list()
            elif choice == '5':
                Ecommerce.customer_list()
            elif choice == 'q':
                print("\nYou exited.")
            else:
                print("\nThere is no option for this choice.\n")


if __name__ == '__main__':
    app = Ecommerce()
    app.run()
