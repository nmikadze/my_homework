# 1. მოცემულ კლასს მოარგე Single Responsibility პრინციპი და შესაბამისად შეცვალე კოდი. (კერძოდ დაშალე 4 კლასად User, Storage, HttpConnection, Logger)
########################################################################################################################


class User:
    def __init__(self, name):
        self.name = name
    def get_name(self):
        return self.name

class Storage:
    def save(self, data):
        # Storage
        pass

class HttpConnection:
    def send(self, data):
        # HttpConnection
        pass

class Logger:
    def log(self, message):
        # Logger
        pass



    #2. 
class Discount:
    def __init__(self, customer, price):
        self.customer = customer
        self.price = price

    def give_discount(self):
        if self.customer == 'favourite':
            return self.price * 0.2

class VIPDiscount(Discount):
    def give_discount(self):
        if self.customer == 'vip':
            return self.price * 0.4
        else:
            # თუ კლიენტი არ არის VIP, მაშინ გამოვიდეს თანხა ახალი ფასდაკლების გარეშე
            return super().give_discount()

# მაგალითი
discount1 = Discount('favourite', 100)
print(discount1.give_discount())  # 20.0

discount2 = VIPDiscount('vip', 100)
print(discount2.give_discount())  # 40.0
