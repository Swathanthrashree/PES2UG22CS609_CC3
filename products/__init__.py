from products import dao


class Product:
    def __init__(self, id: int, name: str, description: str, cost: float, qty: int = 0):
        self.id = id
        self.name = name
        self.description = description
        self.cost = cost
        self.qty = qty

    @staticmethod
    def load(data):
        """Create a Product object from a dictionary."""
        return Product(data['id'], data['name'], data['description'], data['cost'], data['qty'])


def list_products() -> list[Product]:
    """Fetch and return all products as Product objects."""
    products = dao.list_products()
    # Using list comprehension for cleaner and more efficient processing
    return [Product.load(product) for product in products]


def get_product(product_id: int) -> Product:
    """Fetch a single product by its ID."""
    return Product.load(dao.get_product(product_id))


def add_product(product: dict):
    """Add a new product."""
    dao.add_product(product)


def update_qty(product_id: int, qty: int):
    """Update the quantity of a product."""
    if qty < 0:
        raise ValueError('Quantity cannot be negative')
    dao.update_qty(product_id, qty)
