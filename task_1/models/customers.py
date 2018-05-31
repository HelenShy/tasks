import decimal
from .products import Product
from .currencies import Currency
from .purchases import Buy

class Customer:
    customer_list = []

    def __init__(self, name, discount, currency):
        self.name = name
        self.discount = discount
        self.currency = currency
        self.id = len(Customer.customer_list)
        Customer.customer_list.append(self)

    @property
    def discount(self):
        return self._discount

    @discount.setter
    def discount(self, value):
        try:
            value = decimal.Decimal(value)
        except decimal.InvalidOperation:
            raise ValueError('Discount value should be decimal.')
        if value < 0 or value > 100:
            raise ValueError('Discount should be between 0 and 100.')
        self._discount = value

    @property
    def currency(self):
        return self._currency

    @currency.setter
    def currency(self, value):
        if not Currency.exists(value):
            raise ValueError('Currency {} is not valid.'.format(value))
        self._currency = value


    def purchase(self, product_id, quantity):
        """
        Make a purchase of defined product.
        """
        buy = Buy(self, product_id, quantity)
        return buy.print_check()

    @classmethod
    def get_by_id(cls, id):
        """
        Return customer instance by it`s id.
        """
        try:
            id = int(id)
            try: 
                return Customer.customer_list[id]
            except IndexError:
                raise ValueError('Customer with this id does not exist')
        except ValueError:
            raise ValueError('Customer_id should be an integer.')

    @classmethod
    def print_all(cls):
        """
        Prit id and name for all customers.
        """
        print('List of customers:')
        for customer in Customer.customer_list:
            print(str(customer.id) + '. ' + customer.name)

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.name
