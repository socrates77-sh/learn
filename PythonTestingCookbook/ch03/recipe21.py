"""
This is documentation for the this entire recipe.
With it, we can demonstrate usage of the code.

>>> cart = ShoppingCart().add("tuna sandwich", 15.0)
>>> len(cart)
1
>>> cart.item(1)
'tuna sandwich'
>>> cart.price(1)
15.0
>>> print(round(cart.total(9.25), 2))
16.39
"""


class ShoppingCart(object):
    """
    This object is used to store the goods.
    It conveniently calculates total cost including
    tax.
    """

    def __init__(self):
        self.items = []

    def add(self, item, price):
        "Add an item to the internal list."
        self.items.append(Item(item, price))
        return self

    def item(self, index):
        "Look up the item. The cart is a 1-based index."
        return self.items[index-1].item

    def price(self, index):
        "Look up the price. The cart is a 1-based index."
        return self.items[index-1].price

    def total(self, sales_tax):
        "Add up all costs, and then apply a sales tax."
        sum_price = sum([item.price for item in self.items])
        return sum_price*(1.0 + sales_tax/100.0)

    def __len__(self):
        "Support len(cart) operation."
        return len(self.items)


class Item(object):
    def __init__(self, item, price):
        self.item = item
        self.price = price
