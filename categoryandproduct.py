class Category():
    name: str
    description: str
    product: list
    total_categories = 0
    total_unique_products = 0
    def __init__(self, name, description, product):
        self.name = name
        self.description = description
        self.product = product
        Category.total_categories += 1
        unique_products = set(product)
        Category.total_unique_products += len(unique_products)






class Product():
    name: str
    description: str
    price: float
    count_in_stock = int
    def __init__(self, name, description, price, count_in_stock):
        self.name = name
        self.description = description
        self.price = price
        self.count_in_stock = count_in_stock

