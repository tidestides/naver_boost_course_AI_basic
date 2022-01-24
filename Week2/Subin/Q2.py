#2
class Car():
    def __init__(self, fuel, wheels):
        self.fuel = fuel
        self.wheels = wheels

class Bike(Car):    
    def __init__(self,fuel,wheels,size):
        super().__init__(fuel,wheels) #Car 클래스 상속
        self.size = size #Bike 클래스는 size인자를 추가로 가짐

bike = Bike("gas",2,"small")
print(bike.fuel,bike.wheels,bike.size)