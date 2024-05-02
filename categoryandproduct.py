from abc import ABC, abstractmethod

class AbstractProduct(ABC):
    @abstractmethod
    def __init__(self, name, description, price, count_in_stock):
        self.name = name
        self.descripption = description
        self.price = price
        self.count_in_stock = count_in_stock
        if count_in_stock == 0:
            raise ValueError('ValueError')

    @abstractmethod
    def __add__(self, other):
        pass

class LogCreationMixin:
    def __repr__(self):

        attribute_strings = []

        for attribute_name, attribute_value in self.__dict__.items():
            attribute_string = f'{attribute_name} = {attribute_value!r}'
            attribute_strings.append(attribute_string)

        attributes = ', '.join(attribute_strings)


        return f'{self.__class__.__name__} ({attributes})'



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
        print(repr(self))

    def __str__(self):
        return f'{self.name},  количество продуктов:  {len(self)} шт.'

    def __len__(self):
        return sum(product.count_in_stock for product in self.__products)




    def add_product(self, product):
        if isinstance(product, Product):
            if product.count_in_stock = 0:
                raise ValueError("Товар с нулевым количеством не может быть добавлен")
            self.__products.append(product)
            unique_products = set(self.__products)
            Category.total_unique_products = len(unique_products)
        else:
            raise TypeError

    @property
    def products(self):
        product_info = []
        for product in self.__products:
            info = f"{product.name}, {product.price}  руб. Остаток: {product.count_in_stock}шт."
            product_info.append(info)
        return '\n'.join(product_info)


    def average_price(self):
        total_price = sum(product.price for product in self.__products)
        try:
            return total_price / len(self.__products)
        except ZeroDivisionError:
            return 0





class Product(AbstractProduct, LogCreationMixin):
    name: str
    description: str
    __price: float
    count_in_stock = int
    def __init__(self, name, description, price, count_in_stock):
        super().__init__(name, description, price, count_in_stock)
        self.name = name
        self.description = description
        self.__price = float(price)
        self.count_in_stock = int(count_in_stock)
        print(repr(self))

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


class Smartphone(Product):
    def __init__(self, name, description, price, count_in_stock, perfomance, model, memory, color):
        super().__init__(name, description, price, count_in_stock)
        self.perfomance = perfomance
        self.model = model
        self.memory = memory
        self.color = color

    def __add__(self, other):
        if isinstance(other, Smartphone):
            return self.price * self.count_in_stock + other.price * other.count_in_stock
        else:
            raise TypeError("Unsupported operand type for +")


class LawnGrass(Product):
    def __init__(self, name, description, price, count_in_stock, manufacturer, germination_time, color):
        super().__init__(name, description, price, count_in_stock)
        self.manufacturer = manufacturer
        self.germination_time = germination_time
        self.color = color

    def __add__(self, other):
        if isinstance(other, LawnGrass):
            return self.price * self.count_in_stock + other.price * other.count_in_stock
        else:
            raise TypeError("Unsupported operand type for +")


# Создание продуктов
two = Product('mouse', 'wireless mouse', 32.2, 2)
four = Product('keyboard', 'wireless keyboard', 2222.2, 6)
three = Product('test1', 'test2', 55.5, 7)
five = Product('test3', 'test4', 32.2, 2)

# Создание смартфона
iphone = Smartphone('iPhone 13', 'Latest iPhone model', 999.99, 10, 'A15 Bionic', 'iPhone 13', 128, 'Midnight')

# Создание газонной травы
grass = LawnGrass('Premium Grass', 'High-quality lawn grass', 19.99, 50, 'GreenCo', 7, 'Green')

# Создание категории с продуктами
electronics = Category('Electronics', 'Electronic devices', [two, three, four, five])
smartphones = Category('Smartphones', 'Mobile phones', [iphone])
gardening = Category('Gardening', 'Gardening supplies', [grass])

print("Продукты в категории 'Electronics':")
print(electronics.products)

print("\nИнформация о смартфоне:")
print(iphone)

print("\nИнформация о газонной траве:")
print(grass)

# Проверка сеттера price
two.price = 50.2  # Изменение цены на корректное значение
print(f"\nНовая цена для {two.name}: {two.price}")

two.price = -5.0  # Попытка установить некорректное значение цены
print(f"Новая цена для {two.name}: {two.price}")

print("\nИнформация о категории 'Electronics':")
print(electronics)

print("\nИнформация о продукте 'mouse':")
print(two)



print(f"\nОбщее количество категорий: {Category.total_categories}")
print(f"Общее количество уникальных продуктов: {Category.total_unique_products}")
