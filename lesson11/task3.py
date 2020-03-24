class Product:
    def __init__(self, product_type, name, amount, price):
        self.product_type = product_type
        self.product_name = name
        self.product_price = price
        self.product_amount = amount

    def info(self):
        print(f'{self.product_type}:\n{self.product_name}[Amount: {self.product_amount}|Price: {self.product_price}$]')


class ProductStore:
    def __init__(self, products):
        self.products = products

    def add_product(self, products):
        self.products.append(products)


if __name__ == '__main__':
    p1 = Product('drinks', 'Pepsi', 1, 1.50)
    p1.info()
    s = ProductStore([])
    s.add_product(p1)
