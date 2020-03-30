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

    def __init__(self, *products):
        self.stock = {product.name: [product.type, product.price * self.tax, 0] for product in products}

    def add_product(self, product, quantity):
        if product.name in self.stock:
            self.stock[product.name][2] += quantity
        else:
            self.stock[product.name] = [product.type, product.price * self.tax, quantity]


if __name__ == '__main__':
    p1 = Product('drinks', 'Pepsi', 1.50)
    p2 = Product('clothes', 'T-shirt', 12.45)
    p1.info()
    s = ProductStore()
    s.add_product(p1, 5)
    s.add_product(p2, 3)
    print(s.stock)

