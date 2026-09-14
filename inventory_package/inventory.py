class Inventory:
    """Manage a collection of Product objects."""

    def __init__(self):
        self.products = []

    def add_product(self, product):
        """Add a Product object to the inventory."""
        self.products.append(product)

    def total_inventory_value(self):
        """Return the combined value of all products."""
        return sum(product.total_value() for product in self.products)

    def low_stock_products(self, threshold):
        """Return products whose quantity is below the threshold."""
        return [
            product
            for product in self.products
            if product.quantity < threshold
        ]