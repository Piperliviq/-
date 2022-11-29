class Vehicle:
    def __init__(self, brand, model, engine_vol, max_speed, total_km, max_passengers):
        self.brand = brand
        self.model = model
        self.engine_vol = engine_vol
        self.max_speed = max_speed
        self.total_km = total_km
        self.max_passengers = max_passengers

    def print_info(self):
        print(f"Vehicle: ({self.brand}, {self.model}, {self.engine_vol}, {self.max_speed}, {self.total_km}, {self.max_passengers})")

class Motorbike(Vehicle):
    def __init__(self, brand, model, engine_vol, max_speed, total_km, max_passengers, price, kosh):
        super().__init__(brand, model, engine_vol, max_speed, total_km, max_passengers=2)
        self.price = price
        self.kosh = kosh

    def print_info(self):
        print(f"Motorbike: ({self.brand}, {self.model}, {self.engine_vol}, {self.max_speed}, {self.total_km}, {self.max_passengers}, {self.price}, {self.kosh})")

class Car(Vehicle):
    def __init__(self, brand, model, engine_vol, max_speed, total_km, max_passengers, category, fuel_type):
        super().__init__(brand, model, engine_vol, max_speed, total_km, max_passengers=4)
        self.category = category
        self.fuel_type = fuel_type

    def print_info(self):
        print(
            f"Car: ({self.brand}, {self.model}, {self.engine_vol}, {self.max_speed}, {self.total_km}, {self.max_passengers}, {self.category}, {self.fuel_type})")

class Bus(Vehicle):
    def __init__(self, brand, model, engine_vol, max_speed, total_km, max_passengers, company, year):
        super().__init__(brand, model, engine_vol, max_speed, total_km, max_passengers)
        self.company = company
        self.year = year

    def print_info(self):
        print(f"Bus: ({self.brand}, {self.model}, {self.engine_vol}, {self.max_speed}, {self.total_km}, {self.max_passengers}, {self.company}, {self.year})")


list_vehicle = []
ex1 = Car("Mercedes", "C", 2.2, 220.0, 245254.0, 4, "coupe", "diesel")
ex2 = Motorbike("Kawasaki", "Z750", 1.2, 200.0, 36815.0, 2, 8000.2, False)
ex3 = Bus("Mercedes", "Bandit", 3.6, 160.2, 126585.1, 45, "Bambi", 2008)
ex4 = Car("Audi", "RS6 C7", 4.2, 280.0, 156582.0, 4, "hetchback", "gasoline")
ex5 = Motorbike("KTM", "Sand", 1.5, 200.0, 15879.0, 2, 65875.2, False)
ex6 = Bus("Iveco", "Evadys", 4.2, 170.0, 125896.5, 70, "Nirabus", 2021)
ex7 = Car("Ford", "Mustang", 4.5, 260.0, 210548.0, 4, "hatcback", "gasoline")
ex8 = Motorbike("Kawasaki", "Ninja", 1.0, 300.0, 31000.3, 2, 50000.2, False)
ex9 = Bus("VW", "Crafter", 3.5, 180.0, 145365.0, 55, "Union Uvkani", 2015)
ex10 = Car("BMW", "M5", 4.2, 280.0, 62150.0, 4, "estate", "gasoline")

list_vehicle.append(ex1)
list_vehicle.append(ex2)
list_vehicle.append(ex3)
list_vehicle.append(ex4)
list_vehicle.append(ex5)
list_vehicle.append(ex6)
list_vehicle.append(ex7)
list_vehicle.append(ex8)
list_vehicle.append(ex9)
list_vehicle.append(ex10)

ex1.print_info()
ex2.print_info()
ex3.print_info()
ex4.print_info()
ex5.print_info()
ex6.print_info()
ex7.print_info()
ex8.print_info()
ex9.print_info()
ex10.print_info()
