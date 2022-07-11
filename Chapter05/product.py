class Product:
    _product_id = 100902
    _product_name = 'Iphone X'
    _product_category = 'Electronics'
    _unit_price = 700
    
    def get_product(self):
        return self._product_id, self._product_name, self._product_category, self._unit_price

