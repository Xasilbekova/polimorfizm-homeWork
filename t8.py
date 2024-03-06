class Transport:
    def __init__(self, brand, model, type) -> None:
        self.brand = brand
        self.model = model
        self.type = type

    def info(self):
        print(f"{self.brand}, {self.model}, {self.type}")

class ElentroCars(Transport):
    def __init__(self, brand, model, type, battery_life, chargin_time) -> None:
        super().__init__(brand, model, type)
        self.battery_life = battery_life
        self.chargin_time = chargin_time
    
    def more_info(self):
        print(f"{self.brand}, {self.model}, {self.type}, {self.battery_life}, {self.chargin_time}")

class SportCars(Transport):
    def __init__(self, brand, model, type, motor, color) -> None:
        super().__init__(brand, model, type)
        self.motor = motor
        self.color =color

    def more_info(self):
        print(f"{self.brand}, {self.model}, {self.type}, {self.motor}, {self.color}")

class Truck(Transport):
        def __init__(self, brand, model, type, motor, height, long, wieght) -> None:
            super().__init__(brand, model, type)
            self.motor = motor
            self.height = height
            self.long = long
            self.wieght = wieght
            
        def more_info(self):
            print(f"{self.brand}, {self.model}, {self.type}, {self.motor}, {self.height}, {self.long}, {self.wieght}")

transport = Transport("GM", "Cobalt", "Avto")
elentroCars = ElentroCars("GM", "Malibu", "Avto", "MSD2367", 2022)
sportCars = SportCars("GM", "Spark", "Avto", "DB 02941", "Grey")
truck = Truck("GM", "Labo", "Avto", "AK 7854", 15, 18, 5)

transport.info()
elentroCars.more_info()
sportCars.more_info()
truck.info()