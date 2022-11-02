from Prac_06.guitar import Guitar


def main():
    guitars = []
    print("My Guitars")
    name = input("Name: ")
    while name != "":
        year = int(input("Year: "))
        cost = float(input("Cost"))
        add_guitar = Guitar(name, year, cost)
        print(add_guitar, "added.")
        name = input("Name: ")

    guitars.append(Guitar("Gibson L-5 CES", 1922, 16035.40))
    guitars.append(Guitar("Line 6 JTV-59", 2010, 1512.9))

    print("These are my guitars:")
    for index, guitars in enumerate(guitars):
        vintage_string = "(vintage)"
        if Guitar.is_vintage() is True:
         print("Guitar {}: {:>20} ({}), worth ${:10,.2f}{:>10}".format(index + 1, guitars.name, guitars.year, guitars.cost,
                                                                      vintage_string))
    else:
        print("Quick YOU should BUY a guitar")


main()
