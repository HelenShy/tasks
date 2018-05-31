import decimal
from .products import Product
from .currencies import Currency


class Buy:
    buy_list = []

    def __init__(self, customer, product_id, quantity):
        self.customer = customer
        self.product_id = product_id
        self.quantity = quantity
        product = Product.get_by_id(self.product_id)
        self.price = product.price
        self.id = len(Buy.buy_list)
        Buy.buy_list.append(self)

    @property
    def product_id(self):
        return self._product_id

    @product_id.setter
    def product_id(self, value):
        product = Product.get_by_id(value)
        self._product_id = product.id

    @property
    def quantity(self):
        return self._quantity

    @quantity.setter
    def quantity(self, value):
        try:
            value = int(value)
        except TypeError:
            raise ValueError('Quantity should be an integer value.')
        self._quantity = value

    @property
    def total_amount(self):
        return decimal.Decimal(self.price * self.quantity - self.discount_amount).quantize(
            decimal.Decimal('.01'), rounding=decimal.ROUND_DOWN)

    @property
    def total_amount_in_currency(self):
        return decimal.Decimal(Currency.calculate_in_currency(
            self.customer.currency, self.total_amount)).quantize(
            decimal.Decimal('.01'), rounding=decimal.ROUND_DOWN)

    @property
    def discount_amount(self):
        return decimal.Decimal(self.price * self.quantity * self.customer.discount  / 100).quantize(
            decimal.Decimal('.01'), rounding=decimal.ROUND_DOWN)

    @property
    def discount_amount_in_currency(self):
        return decimal.Decimal(Currency.calculate_in_currency(
            self.customer.currency, self.discount_amount)).quantize(
            decimal.Decimal('.01'), rounding=decimal.ROUND_DOWN)

    @property
    def total_weight(self):
        product = Product.get_by_id(self.product_id)
        return product.weight * self.quantity # product weight never changes

    def print_check(self):
        """
        Print check for purchased product
        """
        return Check.print_check(self.id, self.customer.currency)

    @classmethod
    def get_by_id(cls, id):
        """
        Get buy instance by it`s id.
        """
        try:
            id = int(id)
            try: 
                return Buy.buy_list[id]
            except IndexError:
                raise ValueError('Purchase with this id does not exist')
        except ValueError:
            raise ValueError('Purchase_id should be an integer.')


class Check:
    @staticmethod
    def print_check(buy_id, customer_currency):
        """
        Return data for check: amount of purchase and amount of discount
        in customer currency.
        """
        buy = Buy.get_by_id(buy_id)
        product = Product.get_by_id(buy.product_id)
        price_in_currency = buy.total_amount_in_currency
        check = '{} {} purchased for {}{}'.format(buy.quantity, 
                                                product.name, 
                                                price_in_currency, 
                                                customer_currency)
        check += '\nDiscount amount: {}{}'.format(buy.discount_amount_in_currency, customer_currency)
        return check
