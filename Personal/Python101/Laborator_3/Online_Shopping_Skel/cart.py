class Cart:
    def __init__(self):
        self.list_cart = []

    def add(self, new_product):
        self.list_cart.append(new_product)


    def remove(self, product_name):
        if product_name in self.list_cart:
            self.list_cart.remove(product_name)


    def view(self):
        return self.list_cart

    def cart_checkout(self):
        sum = 0

        for product in self.list_cart:
            sum += product.return_price()
        
        self.list_cart.clear()

        return sum