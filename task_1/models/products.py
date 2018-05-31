import decimal

class Product:
    product_list = []

    def __init__(self, name, cost, price, weight):
        self.name = name
        self.cost = cost
        self.price = price
        self.weight = weight
        self.id = len(Product.product_list)
        Product.product_list.append(self)

    @property
    def cost(self):
        return self._cost

    @cost.setter
    def cost(self, value):
        try:
            value = decimal.Decimal(value)
        except decimal.InvalidOperation:
            raise ValueError('Cost value should be decimal.')
        if value < 0:
            raise ValueError('Cost cannot be less than zero.')
        self._cost = value

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        try:
            value = decimal.Decimal(value)
        except decimal.InvalidOperation:
            raise ValueError('Price value should be decimal.')
        if value < self.cost:
            raise ValueError('Price cannot be below cost.')
        self._price = value

    @property
    def weight(self):
        return self._weight

    @weight.setter
    def weight(self, value):
        try:
            value = decimal.Decimal(value)
        except decimal.InvalidOperation:
            raise ValueError('Weight value should be decimal.')
        if value < 0:
            raise ValueError('Product weight cannot be less than zero.')
        self._weight = value

    @classmethod
    def get_by_id(cls, id):
        """
        Return product instance by it`s id.
        """
        try:
            id = int(id)
            try: 
                return Product.product_list[id]
            except IndexError:
                raise ValueError('Product with this id does not exist')
        except ValueError:
            raise ValueError('Product_id should be an integer.')


    @classmethod
    def print_all(cls):
        """
        Print id and name for all products.
        """
        print('List of products:')
        for product in Product.product_list:
            print(str(product.id) + '. ' + product.name)

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.name