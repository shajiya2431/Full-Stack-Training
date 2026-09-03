def order_details(product, quantity):
    print("product:", product)
    print("quantity:", quantity)


def total_price(price, quantity):
    total = price *quantity
    print("Total Price:", total)

def main():
    product = "Laptop"
    quantity = 2
    price = 65000

    order_details(product, quantity)
    total_price(price, quantity)
    