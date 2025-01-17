# Build a class concept of cars 

class Car:
     
    def __init__(self, make,  model, year, price, number):
        self.make = make
        self.model =  model
        self.year = year
        self.price = price
        self.number = number
        
    def show_car(self):
        print(f"The {self.make}-{self.model} has been produced in {self.year}.")
        print(f"It is sold for {self.price}$ in {self.number} copies ")

    def update_numbers(self, current_number):
        self.number += current_number

    def total_sale(self, sales_number, car_sales ):
        print(f" This year there was {sales_number} {self.make}-{self.model} sold for a total amount of {car_sales}$.")
        
#Create an inherited class for Sport cars
class SportsCar(Car):
    def __init__(self, make, model, year, price, number, power, stable, pilot):
        super().__init__(make, model, year, price, number)
        self.power = power
        self.stable = stable
        self.pilot = pilot

    def show_car(self):
        return f"It runs this year for {self.stable} with {self.pilot} as a pilot in F1."
    
    def average_speed(self, distance, duration):
        speed = distance / duration
        print(f"The maximum speed of the {self.make}-{self.model} is {speed}km/h.")


car1 = Car('Toyota', 'Camry', 2020, 5000.0, 25)
car2 = Car('Toyota', 'Yaris', 2019, 6500.0, 15)

car1.show_car()
car2.show_car()

car3= SportsCar('Mercedes', 'AMG215','2024','1.5M', 2, 800, "Mercedes", "Georges Russell")
print(car3.show_car())