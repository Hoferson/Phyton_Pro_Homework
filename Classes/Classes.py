class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def __str__(self):
        return f'{self.name} - {self.price}$'

class Buyer:
    def __init__(self, name, surname, count_of_purchases):
        self.name = name
        self.surname = surname
        self.count_of_purchases = count_of_purchases

    def __str__(self):
        return f'{self.name} {self.surname}'


class Order:
    def __init__(self, buyer, product, amount, date):
        self.buyer = buyer
        self.product = product
        self.amount = amount
        self.date = date
        self.price = product.price
        self.count = self.price * self.amount
        
    def __str__(self):
        return f'{self.buyer}:\n{self.product}: {self.amount} pcs\nTo pay: {self.count}$'

laptop = Product('Laptop', 1000)
computer = Product('Computer', 1100)
router = Product('Router', 105)

buyer_1 = Buyer('Mr_Maxum', 'Wolker', 6)
buyer_2 = Buyer('Mr_Adam', 'Franklin', 23)
buyer_3 = Buyer('Mr_Lex', 'Murder', 9)

order_1 = Order(buyer_1, computer, 1, '11.11.2011')
order_2 = Order(buyer_2, router, 2, '11.11.2014')
order_3 = Order(buyer_3, laptop, 10, '11.11.2018')

total = order_1.count + order_2.count + order_3.count
print(f'\n\n-----Order History-----\n{order_1}\n----------------------\n{order_2}\n----------------------\n{order_3}\n______________________\nTOTAL: {total}$')