class Product:
    _productID = 100902
    _productName = 'Iphone X'
    _productCategory = 'Electronics'
    _unitPrice = 700
    
    def getProduct(self):
        return self._productID, self._productName, self._productCategory, self._unitPrice

