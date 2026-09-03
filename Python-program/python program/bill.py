def place_order(item, quantity):
    print("Item:", item)
    print("Quantity:" , quantity)

def generate_bill(price, quantity):
    total = price * quantity
    print("Total Bill:" , total)

def main():
    item = "pizza"
    price = 300
    quantity = 2

    place_order(item, quantity)
    generate_bill(price, quantity)

main()