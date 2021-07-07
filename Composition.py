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