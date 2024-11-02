import product

class Phone(product.Product):
    def __init__(self, name, price, ram, cpu):
        product.Product.__init__(self, name, price)
        self.ram = ram
        self.cpu = cpu

    def __str__(self):
        propozitie = f"The new {self.name} is an unforgettable experience, CPU {self.cpu}, RAM {self.ram}."
        return propozitie
