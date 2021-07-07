class Car:
    def __init__(self, make, model, year, engine):
        self.make = make
        self.model = model
        self.year = year
        self.engine = engine
    def describe(self):
        print(f'{self.year} {self.make} {self.model}')
    def start(self):
        self.engine.ignite()
class Engine:
    def __init__(self, configuration, displacement, horsepower, torque):
        self.configuration = configuration
        self.displacement = displacement
        self.horsepower = horsepower
        self.torque = torque
    def ignite(self):
        print('Vroom, vroom!')
    def info(self): # the composition is a one way street, the engine class has no access
        self.describe() # to component class Car! But the Car has access to attr&meth on Engine class
my_engine = Engine("V8", 5.8, 326, 344)
my_car = Car("De Tomaso", "Pantera", 1979, my_engine)
my_car.describe()
my_car.engine.ignite()
my_car.start()
#my_car.engine.info()  #result error 'Engine' object has no attribute 'describe'

'''          Composition versus Inheritance
Use inheritance if there is an “is a” relationship, 
and use composition if there is a “has a” relationship.
For example, you have the Vehicle class and you want to make a Car class. 
Ask yourself if a car has a vehicle or if a car is a vehicle. A car is a vehicle; 
therefore you should use inheritance. Now imagine that you have a Phone class and 
you want to represent an app for the phone. Ask yourself if a phone is an app or if 
a phone has an app. A phone has an app; therefore you should use composition.
'''