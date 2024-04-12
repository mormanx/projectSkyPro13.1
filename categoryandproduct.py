class Category():
    name: str
    description: str
    product: list
    total_categories = 0
    total_unique_products = 0
    def __init__(self, name, description, products):
        self.name = name
        self.description = description
        self.__products = products

        Category.total_categories += 1
        unique_products = set(self.__products)
        Category.total_unique_products = len(unique_products)

    def __str__(self):
        return f'{self.name},  количество продуктов:  {len(self)} шт.'

    def __len__(self):
        return sum(product.count_in_stock for product in self.__products)




    def add_product(self, product):
        self.__products.append(product)
        unique_products = set(self.__products)
        Category.total_unique_products = len(unique_products)

    @property
    def products(self):
        product_info = []
        for product in self.__products:
            info = f"{product.name}, {product.price}  руб. Остаток: {product.count_in_stock}шт."
            product_info.append(info)
        return '\n'.join(product_info)






class Product():
    name: str
    description: str
    __price: float
    count_in_stock = int
    def __init__(self, name, description, price, count_in_stock):
        self.name = name
        self.description = description
        self.__price = float(price)
        self.count_in_stock = int(count_in_stock)

    def __str__(self):
        return f'{self.name}, {self.price} руб. Остаток: {self.count_in_stock}шт.'

    def __add__(self, other):
        if isinstance(other, Product):
            return self.price * self.count_in_stock + other.price * other.count_in_stock
        else:
            raise TypeError('Error')
    @classmethod
    def create_product(cls, **kwargs):
        return cls(**kwargs)
    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, value):
        if value <= 0:
            print('Цена введена некорректно!')
        else:
            self.__price = value
# Создание продуктов
two = Product('mouse', 'wireless mouse', 32.2, 2)
four = Product('keyboard', 'wireless keyboard', 2222.2, 6)
three = Product('test1', 'test2', 55.5, 7)
five = Product('test3', 'test4', 32.2, 2)

# Создание категории с продуктами
one = Category('Electronics', 'Electronic devices', [two, three, four, five])

print(one.products)

# Проверка сеттера price
two.price = 50.2  # Изменение цены на корректное значение
print(f"Новая цена для {two.name}: {two.price}")

two.price = -5.0  # Попытка установить некорректное значение цены
print(f"Новая цена для {two.name}: {two.price}")

print(one)
print(two)
result = two + four
print(result)