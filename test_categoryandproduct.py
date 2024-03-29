import pytest

from categoryandproduct import Category, Product


def test_category_initialization():
    product1 = Product('laptop', 'high-perfomance laptop', 150000.0, 10)
    product2 = Product('mouse', 'wireless mouse', 6000.0, 20)
    products = [product1, product2]
    category = Category('Electronics', 'Electronic devices', products)

    assert category.name == "Electronics"
    assert category.description == 'Electronic devices'
    assert category.product == products



def test_product_initialization():
    product = Product('keybord', 'mechanical keybord', 5000.0, 10)


    assert product.name == 'keybord'
    assert product.description == 'mechanical keybord'
    assert product.price == 5000.0
    assert product.count_in_stock == 10


def test_count_products_and_categories():
    initial_categories = Category.total_categories
    initial_products = Category.total_unique_products
    product1 = Product('Headphones', 'Noise-canselling headphones', 200.0, 5)
    product2 = Product('Smartphone', 'Latest smartphone model', 800.0, 8)
    products = [product1, product2]
    category = Category('Gadgets', 'Electronic gadgets', products)

    assert Category.total_categories == initial_categories + 1
    assert Category.total_unique_products == initial_products + len(products)