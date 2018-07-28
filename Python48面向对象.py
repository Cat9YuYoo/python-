class MyClass:
    name ='Sam'

    def sayHi(self):
        print 'Hello %s '% self.name

mc=MyClass()
print mc.name
mc.name='Lily'
mc.sayHi()

class car:
    speed=0
    def drive(self,distance):
        time=distance/self.speed
        print time

car1=car()
car1.speed=60.0
car1.drive(100.0)
car1.drive(200.0)

car2=car()
car2.speed=150.0
car2.drive(100.0)
car2.drive(200.0)