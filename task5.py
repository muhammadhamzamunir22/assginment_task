
menu = {
    1: ("Burger", 500),
    2: ("Pizza", 800),
    3: ("Fries", 250),
    4: ("Drink", 150)
}

def order():
    total = 0

    while True:
        print("\n1. Burger - 500")
        print("2. Pizza - 800")
        print("3. Fries - 250")
        print("4. Drink - 150")
        print("0. Finish Order")

        n = int(input("Choice: "))

        if n == 0:
            break

        elif n in menu:
            q = int(input("Quantity: "))

            if q <= 0:
                print("Invalid quantity")
                continue

            item_total = menu[n][1] * q
            total += item_total

            print(menu[n][0], "Total:", item_total)

        else:
            print("Invalid choice")

    print("Final Bill:", total)

    with open("Orders.txt", "w") as f:
        f.write("Final Bill: " + str(total) + "\n")

    print("Order saved successfully.")


order()