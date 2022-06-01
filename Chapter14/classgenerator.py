class ElectronicCounter:
    TestItem = None

    def verifyCart(self, item, status):
        if status == 'Y':
            print('Test passed for', item)
        else:
            print('Get another', item)