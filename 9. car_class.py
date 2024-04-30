class Car:
    def __init__(self, manufacturer, model, year, color, fuel_type):
        self.manufacturer = manufacturer
        self.model = model
        self.year = year
        self.color = color
        self.fuel_type = fuel_type

    def start(self):
        print("The car starts.")

    def stop(self):
        print("The car stops.")

    def car_details(self):
        print("Manufacturer:", self.manufacturer)
        print("Model:", self.model)
        print("Year:", self.year)
        print("Color:", self.color)
        print("Fuel Type:", self.fuel_type)

car_1 = Car("Tesla", "S", "2024", "Red", "Null")
car_1.car_details()
car_1.stop()
