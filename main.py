class Car:
    NAME = "CLASS car"


    def __init__(self, name, color, year):
        self.car_name = name
        self.color = color
        self.year = year

    def pressent(self):
        print(self.car_name, self.color, self.year)
    def change_year(self,new_year):
        if type(new_year) is int:
            self.year = new_year
        else:
            raise ValueError(f"{new_year} is not an int")


car_1 = Car("bmw x5", "white", 2022)
car_2 = Car("mercedes", "red", 2021)
print(car_1.__dict__)
car_1.change_year(2015)
print(car_1.__dict__)
car_1.change_year('2019')
car_1.year = "gjhg"

print(car_1, car_2)
print(car_1.car_name, car_1.color, car_1.year)
print(car_2.car_name, car_2.color, car_2.year)
print(car_1.__dict__)
print(car_2.__dict__)
print(car_1.NAME)
print(car_1.NAME)
print(Car.NAME)
car_2.year = 2011
print(car_2.__dict__)
car_1.pressent()
car_2.pressent()
Car.pressent(car_2)
Car.pressent(car_1)
car_3 = Car("audi", "black", 2013)
car_3.model = "a6"
car_3.pressent()
print(car_1.__dict__,car_3.__dict__,sep="\n")
Car.type = "sport"
print(car_1.type)
car_2.type = "common"
print(car_2.type)
print("asd")










