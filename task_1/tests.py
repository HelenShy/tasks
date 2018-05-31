import unittest
import decimal

from models.currencies import Currency
from models.products import Product
from models.customers import Customer
from models.purchases import Buy, Check


class TestCurrencyClass(unittest.TestCase):
    def test_currency_get(self):
        """
        Test currency course value updating.
        """
        course = Currency.get_course('EUR')
        assert course == 30

    def test_currency_set(self):
        """
        Test currency returns course value for currency types in list.
        """
        course = Currency.set_course('EUR', 31)
        assert Currency.get_course('EUR') == 31

    def test_currency_get_exception(self):
        """
        Test exception is raised in response of querying for currency not among saved ones. 
        """
        with self.assertRaises(ValueError):
            course = Currency.get_course('EU')

    
class TestProductClass(unittest.TestCase):
    def test_product_creation(self):
        """
        Test product creation.
        """
        product = Product('Table', 50, 100, 15)
        assert product.cost == 50
        assert product.price == 100  
        assert product.weight == 15   

    def test_product_creation_exception(self):
        """
        Test product creation raises exception when price passed to constructor 
        is less then product cost.
        """
        try:
            product = Product('Table', 105, 100, 15)
            self.assertFail()
        except Exception as inst:
            self.assertEqual(str(inst), 'Price cannot be below cost.')

    def test_product_creation_exception_str(self):
        """
        Test product creation with string passed to decimal field.
        """
        try:
            product = Product('Table', 'one', 100, 15)
            self.assertFail()
        except Exception as inst:
            self.assertEqual(str(inst), 'Cost value should be decimal.')

    def test_product_get_by_id(self):
        """
        Test Product method get_by_id.
        """
        product = Product('Book', 10, 15, 2)
        assert Product.get_by_id(product.id).name =='Book'

    
class TestCustomerClass(unittest.TestCase):
    def test_customer_creation(self):
        """
        Test customer creation.
        """
        customer = Customer('John', 20, 'UAH')
        assert customer.name == 'John'
        assert customer.discount == 20  
        assert customer.currency == 'UAH' 

    def test_customer_creation_exception(self):
        """
        Test customer creation raises exception when entered discount  is not between 0 and 100.
        """
        try:
            customer = Customer('John', 105, 'UAH')
            self.assertFail()
        except Exception as inst:
            self.assertEqual(str(inst), 'Discount should be between 0 and 100.')

    def test_customer_get_by_id(self):
        """
        Test Customer method get_by_id.
        """
        customer = Customer('Mark', 10, 'EUR')
        assert Customer.get_by_id(customer.id).name =='Mark'


class TestBuyClass(unittest.TestCase):
    def test_buy_creation(self):
        """
        Test buy creation.
        """
        customer = Customer('Nancy', 20, 'EUR')
        product = Product('Chocolate', 50, 100, 15)
        buy = Buy(customer, product.id, 2) 
        assert buy.total_weight == 30
        assert buy.total_amount == 160
        assert buy.discount_amount == 40
        self.assertEqual(buy.total_amount_in_currency, 
            decimal.Decimal(5.33).quantize(decimal.Decimal('.01'), rounding=decimal.ROUND_DOWN))
        assert Buy.get_by_id(buy.id).customer.id == customer.id
        assert Buy.get_by_id(buy.id).product_id == product.id

 
class TestCheckClass(unittest.TestCase):
    def test_check_creation(self):
        """
        Test check creation.
        """
        customer = Customer('Lili', 10, 'EUR')
        product = Product('Chocolate', 50, 100, 15)
        buy = Buy(customer, product.id, 1)
        check = Check.print_check(buy.id, customer.currency)
        self.assertEqual(check, """1 Chocolate purchased for 3.00EUR\nDiscount amount: 0.33EUR""")


if __name__ == '__main__':
    unittest.main()