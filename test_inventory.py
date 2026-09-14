from inventory_package import Product, Inventory


def test_total_value_single_product():
    product = Product("Mouse", 25.50, 3)

    assert product.total_value() == 76.50


def test_inventory_total_value():
    inventory = Inventory()

    inventory.add_product(Product("Mouse", 25.50, 3))
    inventory.add_product(Product("Keyboard", 50.00, 10))

    assert inventory.total_inventory_value() == 576.50


def test_low_stock_detection():
    inventory = Inventory()

    inventory.add_product(Product("Mouse", 25.50, 3))
    inventory.add_product(Product("Keyboard", 50.00, 10))

    low_stock = inventory.low_stock_products(5)

    assert len(low_stock) == 1
    assert low_stock[0].name == "Mouse"