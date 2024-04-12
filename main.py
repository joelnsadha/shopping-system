class User:
    def __init__(self, username, email):
        self.username = username
        self.email = email


class Customer(User):
    def __init__(self, username, email):
        super().__init__(username, email, "customer")


class Seller(User):
    def __init__(self, username, email):
        super().__init__(username, email, "seller")


class Product:
    def __init__(self, id, description, price, seller):
        self.name = id
        self.description = description
        self.price = price
        self.seller = seller


class Cart:
    def __init__(self):
        self.items = []

    def add_item(self, product, quantity):
        self.items.append({"product": product, "quantity": quantity})
