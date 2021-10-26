# class Person:
#     def __init__(self, name, age, occupation):
#         self.name = name
#         self.age = age
#         self.occupation = occupation

#     def say_hello(self):
#         print(f"Hello, my name is {self.name}.")

#     def say_age(self):
#         print(f"I am{self.age} years old.")

# class Superhero(Person):
#     def __init__(self, name, age, occupation, secret_identity, nemesis):
#         super().__init__(name, age, occupation)
#         self.secret_identify = secret_identity
#         self.nemesis = nemesis
#     def reveal_secret_identity(self):
#         print('the secret', self.secret_identity)
#     def say_nemesis(self):
#         print('My nemesis is', self.nemesis )
#     def say_hello(self):
#         print(f'I am {self.name}, and criminals fear me')
#     def say_age(self):
#         print('Young or old, I will triumph over evil.')
#     def old_say_hello(self):
#         super().say_hello()
#     def old_say_age(self):
#         super().say_age()

# hero = Superhero("Storm", "30", "Queen of Wakanda", "Ororo Munroe", "Shadow King")
# hero.old_say_age()
# #hero.say_hello()
# #print(help(Superhero))
#----------------------------------
def two_digits(val):
    s = str(val)
    if len(s) == 1:
        s = '0' + s
    return s


class Timer:
    def __init__(self, hours=0, minutes=0, seconds=0):
        self.__hours = hours
        self.__minutes = minutes
        self.__seconds = seconds

    def __str__(self):
        return two_digits(self.__hours) + ":" + \
               two_digits(self.__minutes) + ":" + \
               two_digits(self.__seconds)

    def next_second(self):
        self.__seconds += 1
        if self.__seconds > 59:
            self.__seconds = 0
            self.__minutes += 1
            if self.__minutes > 59:
                self.__minutes = 0
                self.__hours += 1
                if self.__hours > 23:
                    self.__hours = 0

    def prev_second(self):
        self.__seconds -= 1
        if self.__seconds < 0:
            self.__seconds = 59
            self.__minutes -= 1
            if self.__minutes < 0:
                self.__minutes = 59
                self.__hours -= 1
                if self.__hours < 0:
                    self.__hours = 23


timer = Timer(23, 59, 59)
print(timer)
timer.next_second()
print(timer)
timer.prev_second()
print(timer)