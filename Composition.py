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