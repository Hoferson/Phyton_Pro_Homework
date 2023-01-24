class Buyer:
    def __init__(self, name, surname, count_of_purchases):
        self.name = name
        self.surname = surname
        self.count_of_purchases = count_of_purchases

    def __str__(self):
        return f'{self.name} {self.surname}'