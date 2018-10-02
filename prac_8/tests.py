from SilverServiceTaxi import SilverServiceTaxi
from UnreliableCar import unreliablecar
def SSStaxi():
    taxi = SilverServiceTaxi("Test Fancy Taxi", 100, 2)
    taxi.drive(18)
    print(taxi)
    print(taxi.get_fare())

def cars():
    good_car = unreliablecar("Mostly Good", 100, 90)
    bad_car = unreliablecar("Dodgy", 100, 9)
    for i in range(1, 12):
        print("Attempting to drive {}km:".format(i))
        print("{:12} drove {:2}km".format(good_car.name, good_car.drive(i)))
        print("{:12} drove {:2}km".format(bad_car.name, bad_car.drive(i)))

    print(good_car)
    print(bad_car)