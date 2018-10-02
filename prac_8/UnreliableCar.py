from car import Car
from random import randint
class unreliablecar(Car):
    class UnreliableCar(Car):
        """An unreliable version of a car."""

        def __init__(self, name, fuel, reliability):

            super().__init__(name, fuel)
            self.reliability = reliability

        def drive(self, distance):

            random_number = randint(1, 100)
            if random_number >= self.reliability:
                distance = 0
         
            distance_driven = super().drive(distance)
            return distance_driven

