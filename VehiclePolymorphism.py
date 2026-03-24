class BMW():
    def price(self):
        print("The price of BMW is 200,000")

    def weight(self):
        print("The weight of BMW is 5000 pounds")

class Ferrari():
    def price(self):
        print("The price of Ferrari is 300,000")

    def weight(self):
        print("The weight of Ferrari is 4100 pounds")

obj_bmw=BMW()
obj_ferrari=Ferrari()

for car in (obj_bmw, obj_ferrari):
    car.price()
    car.weight()