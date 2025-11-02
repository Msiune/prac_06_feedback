from guitar import Guitar

# guitar1 = Guitar("Gibson L-5 CES", 1922, 16035.40)
# print(guitar1)
# print(guitar1.get_age())
# print(guitar1.is_vintage())

print("Guitars!")


def main():
    # test
    guitars = [Guitar("Gibson L-5 CES", 1922, 16035.40), Guitar("Line 6 JTV-59", 2010, 1512.9)]

    # displays all the guitars
    display_guitars(guitars)


# def get_guitar(guitar):
#     name = input("name: ")
#     while name == "":
#         print("invalid name")
#         name = input("name: ")
#     guitar.append(name)
#
#     # valid_input = False
#     # while not valid_input:
#     #     try:
#     #         year = int(input("year: "))
#     #         if year >= 0:
#     #             valid_input = True
#     #         else:
#     #             print("must be non-negative")
#     #     except ValueError:
#     #         print("invalid number")
#     # guitar.append(year)
#     #
#     # valid_input = False
#     # while not valid_input:
#     #     try:
#     #         cost = int(input("cost: "))
#     #         if cost >= 0:
#     #             valid_input = True
#     #         else:
#     #             print("must be non-negative")
#     #     except ValueError:
#     #         print("invalid number")
#     # guitar.append(cost)
#     #
#     # return


def display_guitars(guitars):
    print("these are my guitars:")
    for i, guitar in enumerate(guitars, start=1):
        if guitar.is_vintage():
            print(
                f"Guitar {i}: {guitar.name:>20} ({guitar.year}), worth ${guitar.cost:10,.2f} (vintage)")
        else:
            print(f"Guitar {i}: {guitar.name:>20} ({guitar.year}), worth ${guitar.cost:10,.2f}")


main()
