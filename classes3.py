class Cars():
    def __init__(self, model, colour, size, cost, seats):
        self.model = model
        self.colour = colour
        self.size = size
        self.cost = cost
        self.seats = seats

    def parking(self):
        print("We need to park the car!")

    def travelling(self):
        print("Let's drive in the car together!")

object1 = Cars("Tesla", "Red", "Large", "Expensive", 6)
object2 = Cars("Toyota", "Blue", "Small", "Cheap", 2)
object3 = Cars("BMW", "Black", "Medium", "Normal", 4)
object4 = Cars("Peugot", "White", "Large", "Expensive", 7)

print(object1.colour)
print(object2.seats)
print(object3.model)
print(object4.cost)

object1.travelling()
                 




