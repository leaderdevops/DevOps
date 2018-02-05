class Person:
    def __init__(self, first_name, last_name, favorite_product='DD', citizenship='Canadian'):
        self.first_name = first_name
        self.last_name = last_name
        self.favorite_product = favorite_product
        self.citizenship = citizenship

    def full_name(self):
        return self.first_name + " " + self.last_name

    def __str__(self):
        return 'I am an object of type {} found at memory address {}'.format(type(self), id(self))