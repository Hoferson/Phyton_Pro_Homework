class Product_PriceAmount_error(Exception):
    def __init__(self, message):
        self.message = message

    def __str__(self):
        return f'{self.message}'