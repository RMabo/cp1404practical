from Prac09.silver_servie_taxi import SilverServiceTaxi


def main():
    hummer = SilverServiceTaxi("Hummer", 200, 4)
    hummer.drive(18)
    print(hummer)
    print(hummer.get_fare())


main()

