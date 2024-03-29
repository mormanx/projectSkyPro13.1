class Category():
    name: str
    description: str
    product: list
    def __init__(self, name, description, product):
        self.name = name
        self.description = description
        self.product = product


    pass




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

    pass