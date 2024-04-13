class User:
    def __init__(self, username, email):
        self.username = username
        self.email = email


class Customer(User):
    def __init__(self, username, email):
        super().__init__(username, email)
        self.cart = []

    def add_to_cart(self, product, quantity):
        self.cart.append(product)

    def remove_from_cart(self, product):
        if product in self.cart:
            self.cart.remove(product)
        else:
            print("Item not in cart")

    def view_cart(self):
        for item in self.cart:
            print(item.name)

    def save_cart(self):
        with open("cart.txt", "w") as f:
            items = [item for item in self.cart]
            f.writelines(self.cart)
            f.close()


class Seller(User):
    def __init__(self, username, email):
        super().__init__(username, email)


class Product:
    def __init__(self, id, description, price, seller):
        self.name = id
        self.description = description
        self.price = price
        self.seller = seller


def main():
    joel = Customer("joel01", "email@noemail.com")
    print(joel.username)


if __name__ == "__main__":
    main()
