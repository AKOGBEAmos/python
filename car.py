# Build a class concept of cars 

class Car:
     
    def __init__(self, make,  model, year, price):
        self.make = make
        self.model =  model
        self.year = year
        self.price = price
        
    def show_car(self):
        print(f"The {self.make}-{self.model} has been produced in {self.year}.")
        print(f"It is sold for {self.price}$")

    def total_sale(self, sales_number, car_sales ):
        print(f" This year there was {self.make}-{self.model} sold for a total amount of {car_sales}$.")
        
#Create an inherited class for Sport cars
class Formula1Car(Car):
    def __init__(self, make, model, year, price, number, power, stable, pilot):
        super().__init__(make, model, year, price)
        self.number = number
        self.power = power
        self.stable = stable
        self.pilot = pilot

    def show_car(self):
        return f"It runs this year with  N°{self.number} for {self.stable} with {self.pilot} as a pilot in F1."
    
    def average_speed(self):
        speed = self.power / 2.415
        return round(speed,2)

F1_contenders = []

top_car = Car('Toyota', 'Camry', 2020, 5000.0)

car1 = Formula1Car("Red Bull", "RB21", 2025,'16M', 1, 1100, "Red Bull Racing", "Max Verstappen")
car2 = Formula1Car("Ferrari", "SF-25", 2025, '17', 55, 1050, "Ferrari", "Lewis Hamilton")
car3 =Formula1Car("Mercedes", "W15", 2025, '14M', 44, 1080, "Mercedes-AMG Petronas", "Georges Russell")
car4 = Formula1Car("Alpine", "A525", 2025, '11', 31, 1020, "Alpine F1 Team", "Esteban Ocon")
car5 = Formula1Car("McLaren", "MCL38", 2025,'12M', 4, 1030 , "McLaren F1 Team", "Lando Norris")

print(car3.show_car())

#Get the top car listed by speed 

F1_contenders = [car1,car2,car3,car4,car5]


# k1 = 2.5 ( 0-100km/h) 
# k2 = 2.39
# k3 = 2.45
# k4 = 2.32

" k = 2.415 "


top_speed = 250.0

for car in F1_contenders:
    car_speed = car.average_speed()
    if car_speed > top_speed:
        top_speed = car_speed
        top_car =  car

print(f"The fastest  car for this run is: {top_car.make} {top_car.model} with a high speed of {top_speed} Km/h")