class Vehicle(object):
    def __init__(self,capacity,price):
        self.capacity=capacity
        self.price=price

    def fare(self):
        a=self.capacity*1.1
        b=self.price*a
        print(b)


class Bus(Vehicle):
    def __init__(self,capacity,price):
        Vehicle.__init__(self,capacity,price)

ob=Bus(50,100)
ob.fare()