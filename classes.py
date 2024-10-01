units = ["l", "km", "km/l", "l/100km"] 
class car:

    def __init__(self, name, brand, color, range, tankCapacity):
        self.name = name
        self.brand = brand
        self.color = color 
        self.range = range 
        self.tankCapacity = tankCapacity 
    
    def attributes(self, carChoice):
        if self.name == carChoice:
            print("\nBrand: ", self.brand,"\nColours: ", self.color,"\nRange: ", self.range, units[1],"\nTank Capacity: ", self.tankCapacity, units[0], "\nConsumption ({}) : ".format(units[2]), self.range / self.tankCapacity,"\nConsumption ({}) :".format(units[3]), self.tankCapacity / self.range * 100)
        
car1 = car("yaris", "toyota", "red", 680, 35)
car2 = car("golf", "volkswagen", "blue, black", 750, 45)
car3 = car("swift", "suzuki", "black", 600, 30)
car4 = car("civic", 'honda', "red, black", 500, 40)

carList = [car1.name, car2.name, car3.name, car4.name, "quit"]
carObjectList = [car1, car2, car3, car4]


def main():

    while True:

        choice = input("\n1.Add a car\n2.List specifications\n3.Quit\n> ")
        if choice == "1":
            x = input("Name:\n> ")
            x = car(x ,'', '', 0, 0) 
            x.brand = input("Brand:\n> ")
            x.color = input("Colour:\n> ")
            x.range = int(input("Range:\n> "))
            x.tankCapacity = int(input("Tank capacity:\n> ", ))
            carObjectList.append(x)
            carList.append(x.name)
            
        if choice == "2":
            print("\nList of cars: \n", carList)
            carChoice = input("\nChoose the car: ")
            
            for i in carObjectList:
                i.attributes(carChoice)
        if choice == "3":
            break

main()