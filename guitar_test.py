from guitar import Guitar

# guitar1 = Guitar("Gibson L-5 CES", 1922, 16035.40)
# print(guitar1)
# print(guitar1.get_age())
# print(guitar1.is_vintage())

print("Guitars!")

def main():
    # test
    guitars = []

    guitars.append(Guitar("Gibson L-5 CES", 1922, 16035.40))
    guitars.append(Guitar("Line 6 JTV-59", 2010, 1512.9))

    name = input("Name:")
    while name != "":
        year = int(input("Year:"))
        while year < 0:
            print("invalid year")
            year = int(input("Year:"))

        cost = float(input("Cost:"))
        while cost < 0:
            print("invalid cost")
            cost = float(input("Cost:"))

        guitars.append(Guitar(name, year, cost))
        name = input("Name:")
    # displays all the guitars
    display_guitars(guitars)


def display_guitars(guitars):
    print("these are my guitars:")
    for i, guitar in enumerate(guitars, start=1):
        if guitar.is_vintage():
            print(
                f"Guitar {i}: {guitar.name:>20} ({guitar.year}), worth ${guitar.cost:10,.2f} (vintage)")
        else:
            print(f"Guitar {i}: {guitar.name:>20} ({guitar.year}), worth ${guitar.cost:10,.2f}")


main()
