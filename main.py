from inventory_package import Product, Inventory


def main():
    """Create products, add them to inventory, and display results."""
    inventory = Inventory()

    mouse = Product("Mouse", 25.50, 3)
    keyboard = Product("Keyboard", 50.00, 10)
    monitor = Product("Monitor", 300.00, 10)

    inventory.add_product(mouse)
    inventory.add_product(keyboard)
    inventory.add_product(monitor)

    print("Total inventory value:", inventory.total_inventory_value())

    print("Low stock products:")

    low_stock = inventory.low_stock_products(5)

    for product in low_stock:
        print(f"- {product.name} (Qty: {product.quantity})")


if __name__ == "__main__":
    main()