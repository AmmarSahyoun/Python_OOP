class Person:
    def __init__(self, name, age, occupation):
        self.name = name
        self.age = age
        self.occupation = occupation

    def say_hello(self):
        print(f"Hello, my name is {self.name}.")

    def say_age(self):
        print(f"I am{self.age} years old.")

class Superhero(Person):
    def __init__(self, name, age, occupation, secret_identity, nemesis):
        super().__init__(name, age, occupation)
        self.secret_identify = secret_identity
        self.nemesis = nemesis
    def reveal_secret_identity(self):
        print('the secret', self.secret_identity)
    def say_nemesis(self):
        print('My nemesis is', self.nemesis )
    def say_hello(self):
        print(f'I am {self.name}, and criminals fear me')
    def say_age(self):
        print('Young or old, I will triumph over evil.')
    def old_say_hello(self):
        super().say_hello()
    def old_say_age(self):
        super().say_age()

hero = Superhero("Storm", "30", "Queen of Wakanda", "Ororo Munroe", "Shadow King")
hero.old_say_age()
#hero.say_hello()
#print(help(Superhero))