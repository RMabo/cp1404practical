"""CP1404/CP5632 Practical - Client code to use the Car class."""
# Note that the import has a folder (module) in it.

from Prac_06.car import Car


def main():
    """car class."""
    my_car = Car(180, 'Car')
    my_car.drive(30)
    print("fuel =", my_car.fuel)
    print("odo =", my_car.odometer)
    print(my_car)

    print("Car {}, {}".format(my_car.fuel, my_car.odometer))
    print("Car {self.fuel}, {self.odometer}".format(self=my_car))

    limo = Car(100, 'Limo')
    limo.add_fuel(20)
    print("Limo had {} units of fuel".format(limo.fuel))
    limo.drive(115)
    print("The Limo Odometer:{}".format(limo))
    print(limo)

main()
