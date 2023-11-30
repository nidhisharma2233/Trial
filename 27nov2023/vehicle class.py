class Vehicle:
    def move(self):
        return "Vehicle is moving"


class Car(Vehicle):
    def move(self):
        return "Car is being driven"


class Bicycle(Vehicle):
    def move(self):
        return "Bicycle is being pedaled"


car = Car()
bicycle = Bicycle()
print(car.move())
print(bicycle.move())
