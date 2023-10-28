from typing import List


class Store:
    def __init__(self, products: List['Product']):
        self.products = products

    def add_product(self, product):
        self.products.append(product)

    def remove_product(self, product):
        if product in self.products:
            self.products.remove(product)

    def get_total_quantity(self) -> int:
        total_quantity = 0
        for product in self.products:
            total_quantity += product.get_quantity()
        return total_quantity

    def get_all_products(self) -> List['Product']:
        return [product for product in self.products if product.is_active()]

    def order(self, shopping_list) -> float:
        total_cost = 0
        for product, quantity in shopping_list:
            if product in self.products:
                total_cost += product.buy(quantity)
        return total_cost


# Testing the class
if __name__ == "__main__":
    import products

    product_list = [products.Product("MacBook Air M2", price=1450, quantity=100),
                    products.Product("Bose QuietComfort Earbuds", price=250, quantity=500),
                    products.Product("Google Pixel 7", price=500, quantity=250),
                    ]

    store = Store(product_list)
    products = store.get_all_products()
    print(store.get_total_quantity())
    print(store.order([(products[0], 1), (products[1], 2)]))
