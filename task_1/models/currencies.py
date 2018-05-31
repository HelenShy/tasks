import decimal


class Currency:
    currency_list = {'UAH': 1, 'US': 27, 'EUR':30}

    @classmethod
    def calculate_in_currency(cls, currency_type, amount):
        """
        Calculate amount for bought products in selected currency.
        """
        return amount/ Currency.currency_list[currency_type]

    @classmethod
    def get_course(cls, name):
        """
        Return course for defined currency.
        """
        if Currency.exists(name):
            return cls.currency_list[name]
        raise ValueError('There is no currency ' + name)

    @classmethod
    def set_course(cls, name, course):
        """
        Set course for defined currency.
        """
        if Currency.exists(name):
            cls.currency_list[name] = course
        else:
            raise ValueError('There is no currency ' + name)

    @classmethod
    def exists(cls, name):
        """
        Check whether defined currency exists.
        """
        return name in cls.currency_list.keys()

    @classmethod
    def print_all(cls):
        """
        Prit all saved currencies.
        """
        print('List of currencies:')
        for currency in Currency.currency_list.keys():
            print(str(currency))
