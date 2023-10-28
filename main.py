import products
import store

# setup initial stock of inventory
product_list = [products.Product("MacBook Air M2", price=1450, quantity=100),
                products.Product("Bose QuietComfort Earbuds", price=250, quantity=500),
                products.Product("Google Pixel 7", price=500, quantity=250)
                ]
best_buy = store.Store(product_list)


def start(store_obj):
    while True:
        print("\n1. List all products in store")
        print("2. Show total amount in store")
        print("3. Make an order")
        print("4. Quit")
        choice = input("Please enter your choice: ")

        if choice == "1":
            print("All products in the store:")
            all_products = store_obj.get_all_products()
            for product in all_products:
                print(product.show())

        elif choice == "2":
            total_quantity = store_obj.get_total_quantity()
            print(f"Total amount in store: {total_quantity}")

        elif choice == "3":
            order_list = []
            all_products = store_obj.get_all_products()
            print("Make an order: ")
            for idx, product in enumerate(all_products, start=1):
                print(f"{idx}. {product.Name}")
            product_choice = int(input("Enter the number of the product you want to purchase: "))
            quantity = int(input("Enter the quantity you want to purchase: "))
            order_list.append((all_products[product_choice - 1], quantity))
            total_cost = store_obj.order(order_list)
            print(f"Total cost of the order: {total_cost}")

        elif choice == "4":
            print("You have exited the program.")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    start(best_buy)
