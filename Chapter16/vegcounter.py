def return_cart(*items):
    '''
    This function returns the list of items added to the cart.    
    items: input the cart items. Eg: 'pens', 'pencils'
    '''
    cart_items = []
    for i in items:
        cart_items.append(i)
    return cart_items