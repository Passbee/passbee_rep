class Product:
    def __init__(self, product_type, name, price):
        self.type = product_type
        self.name = name
        self.price = price

    def info(self):
        print(f'{self.type}:\n{self.name}|Price: {self.price}$]')


class ProductStore:
    tax = 3.6
    stock = dict
    budget = 0

    def __init__(self, *products):
        self.stock = {product.name: [product.type, product.price * self.tax, 0] for product in products}

    def add_product(self, product, quantity):
        if product.name in self.stock:
            self.stock[product.name][2] += quantity
        else:
            self.stock[product.name] = [product.type, product.price * self.tax, quantity]

    def sell_product(self, product, quantity):
        if self.stock[product.name][2] >= quantity:
            self.stock[product.name][2] -= quantity
            self.budget += self.stock[product.name][1] * quantity
        else:
            print(f'You can\'t sell {quantity} pieces of {product.name}, because you have only {self.stock[product.name][2]} piece(s)')

    def get_income(self):
        return f'You have {self.budget}$ in store budget'

    def get_storage(self):
        return f'You have {self.stock} in storage'

    def get_product_info(self, product):
        return f'{product.name}\n|Type: {product.type}|Quantity: {self.stock[product.name][2]}|Price with tax: {product.price * self.tax}$|'


if __name__ == '__main__':
    p1 = Product('drinks', 'Pepsi', 1.50)
    p2 = Product('clothes', 'T-shirt', 12.45)
    s = ProductStore()
    s.add_product(p1, 5)
    s.add_product(p2, 3)
    print(s.get_storage())
    s.sell_product(p1, 4)
    print(s.get_storage())
    s.sell_product(p1, 2)
    print(s.get_income())
    print(s.get_product_info(p1))
