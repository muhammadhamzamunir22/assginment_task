
def bill(products):
    total = 0

    for p in products:
        p["product_total"] = p["price"] * p["quantity"]
        total += p["product_total"]

    discount = total * 0.10 if total >= 10000 else 0
    final = total - discount

    expensive = max(products, key=lambda p: p["price"])

    print("Total Bill:", total)
    print("Discount:", discount)
    print("Final Bill:", final)
    print("Most Expensive:", expensive["name"])

    with open("bill.txt", "w") as f:
        f.write("Products: " + str(products) + "\n")
        f.write("Total Bill: " + str(total) + "\n")
        f.write("Discount: " + str(discount) + "\n")
        f.write("Final Bill: " + str(final) + "\n")
        f.write("Most Expensive: " + expensive["name"] + "\n")


products = []

for i in range(5):
    name = input("Product Name: ")
    price = float(input("Price: "))
    quantity = int(input("Quantity: "))

    products.append({
        "name": name,
        "price": price,
        "quantity": quantity
    })

bill(products)