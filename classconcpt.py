class Product:
    count = 0

    def __init__(self, name, category, price):
        self.name = name
        self.category = category
        self.price = price
        Product.count += 1

    def display_product(self):
        print('Name:', self.name)
        print('Category:', self.category)
        print('Price:', self.price)

    def product_count(self):
        print('Total number of products:', Product.count)


prod1 = Product('Pen', 'Stationary', 10)
prod2 = Product('Orange', 'Food', 45)


prod1.display_product()
prod1.product_count()