import shop_exceptions
import shop_buyers
import shop_products


class Order:
    def __init__(self, buyer, date):
        self.buyer = buyer
        self.date = date
        self.products = []
        self.amounts = []

    def add_product (self, product, amount):
        if product.price > 0 and amount > 0:
            self.products.append(product)
            self.amounts.append(amount)
        else:
            raise shop_exceptions.Product_PriceAmount_error('Wrong product price or wrong quantity!')
        
    def remove_product (self, product):
        if product in self.products:
            self.amounts[self.products.index(product)] = None
            self.products.remove(product)

    def order_sum (self):
        sum = 0
        for prod, num in zip(self.products, self.amounts):
            sum += prod.price * num
        return sum
        
    def __str__(self):
        result = f'{self.buyer}\n'
        result += '\n'.join(map(lambda item: f'{item[0]} * {item[1]} = {item[0].price * item[1]}$', zip(self.products, self.amounts)))
        result += f'\nTo pay: {self.order_sum()}$'
        return result

laptop = shop_products.Product('Laptop', 1000)
computer = shop_products.Product('Computer', 1100)
router = shop_products.Product('Router', 105)

buyer_1 = shop_buyers.Buyer('Mr_Maxum', 'Wolker', 6)
buyer_2 = shop_buyers.Buyer('Mr_Adam', 'Franklin', 23)
buyer_3 = shop_buyers.Buyer('Mr_Lex', 'Murder', 9)

order_1 = Order(buyer_1, '11.11.2011')
order_2 = Order(buyer_2, '11.11.2014')
order_3 = Order(buyer_3, '11.11.2018')

try:
    order_1.add_product(laptop, 2)
    order_2.add_product(laptop, 1)
    order_2.add_product(router, 0)
    order_3.add_product(computer,10)

except shop_exceptions.Product_PriceAmount_error as error:
    with open('log.txt', 'w') as file:
        file.write('\n'+str(error))
    print(error)


print(f'\n\n-----Order History-----\n{order_1}\n----------------------\n{order_2}\n----------------------\n{order_3}\n______________________\n')