# 3-m
class Phone:
    def __init__(self, brand, peice):
        self.brand = brand
        self.peice = peice

    def show_price(self):
        print(f"{self.brand} narxi {self.peice}")

p1 = Phone("iPhone", "1200$")

p1.show_price()
