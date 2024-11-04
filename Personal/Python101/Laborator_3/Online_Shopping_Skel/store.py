import cart

class Store:
    def __init__(self, stock):
        self.stock = stock
        self.customer_carts = dict() #! de explicat in enunt: dict(customer_id, cart)

    def login(self, customer_id):
        self.customer_carts[customer_id] = cart.Cart()

    def add_to_cart(self, customer_id, product_name):
        if customer_id in self.customer_carts:
            self.customer_carts[customer_id].add(product_name)
            self.stock.remove(product_name)
    
    def remove_from_cart(self, customer_id, product_name):
        if customer_id in self.customer_carts:
            self.customer_carts[customer_id].remove(product_name)
            self.stock.add(product_name)

    def view_cart(self, customer_id):        
        return [(product.name, product.price) for product in self.customer_carts[customer_id].list_cart]

    
    def checkout(self, customer_id):
        return self.customer_carts[customer_id].cart_checkout()
        '''
        m-am uitat in checker, este imposibil de dat pass la task 10 intrucat se adauga doar numele
        produsului, nu un obiect care sa contina pretul.
        '''