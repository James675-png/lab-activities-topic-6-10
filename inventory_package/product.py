class Product:
    """Represent a product in the inventory."""

    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def total_value(self):
        """Return the total value of this product."""
        return self.price * self.quantity