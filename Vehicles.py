class Vehicle:
    __modeOfTransportation__ = ""
    __fuelCapacity__ = 0
    __costPerGallon__ = 0
    __milesPerGallon__ = 0
    def __init__(self, __modeOfTransportation__, __fuelCapacity__, __costPerGallon__, __milesPerGallon__):
        self.__modeOfTransportation__ = __modeOfTransportation__
        self.__fuelCapacity__ = __fuelCapacity__
        self.__costPerGallon__ = __costPerGallon__
        self.__milesPerGallon__ = __milesPerGallon__
    def range(self):
        return self.__fuelCapacity__ * self.__milesPerGallon__
    def costpermile(self):
        return self.__costPerGallon__ / self.__milesPerGallon__
    
def main():
    Motorcycle = Vehicle("Motorcycle", 5, 3.50, 40)
    print("The range of the motorcycle is:", Motorcycle.range(), "miles")
    print("The cost per mile of the motorcycle is:", Motorcycle.costpermile(), "dollars")

    car = Vehicle("Car", 15, 3.50, 25)
    print("The range of the car is:", car.range(), "miles")
    print("The cost per mile of the car is:", car.costpermile(), "dollars")

    plane = Vehicle("Plane", 2000, 500.00, 30)
    print("The range of the plane is:", plane.range(), "miles")
    print("The cost per mile of the plane is:", plane.costpermile(), "dollars")

    bus = Vehicle("Bus", 100, 3.50, 10)
    print("The range of the bus is:", bus.range(), "miles")
    print("The cost per mile of the bus is:", bus.costpermile(), "dollars")



if __name__ == "__main__":
    main()