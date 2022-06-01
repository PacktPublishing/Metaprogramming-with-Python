class VegCounter:

    def __init__(self, *items):
        cartItems = []
        for i in items:
            cartItems.append(i)
        self.items = cartItems