class Product:
    def __init__(self, name, price, quantity):
        if not name or price < 0 or quantity < 0:
            print("Invalid input parameters for product.")
            self.Name = ""
            self.Price = 0
            self.Quantity = 0
            self.Active = False
        else:
            self.Name = name
            self.Price = price
            self.Quantity = quantity
            self.Active = True

    def get_quantity(self) -> float:
        return self.Quantity

    def set_quantity(self, quantity):
        self.Quantity = quantity
        if self.Quantity == 0:
            self.deactivate()

    def is_active(self) -> bool:
        return self.Active

    def activate(self):
        self.Active = True

    def deactivate(self):
        self.Active = False

    def show(self) -> str:
        return f"{self.Name}, Price: {self.Price}, Quantity: {self.Quantity}"

    def buy(self, quantity) -> float:
        if quantity > self.Quantity:
            print("Not enough quantity available for purchase.")
            return 0
        if quantity < 0:
            print("Invalid quantity for purchase.")
            return 0

        total_price = self.Price * quantity
        self.Quantity -= quantity

        if self.Quantity == 0:
            self.deactivate()

        return total_price


# Testing the class
def main():
    bose = Product("Bose QuietComfort Earbuds", price=250, quantity=500)
    mac = Product("MacBook Air M2", price=1450, quantity=100)

    print(bose.buy(50))
    print(mac.buy(100))
    print(mac.is_active())

    print(bose.show())
    print(mac.show())

    bose.set_quantity(1000)
    print(bose.show())


if __name__ == "__main__":
    main()

