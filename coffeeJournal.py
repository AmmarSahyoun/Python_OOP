import csv


class CoffeeJournal:
    def __init__(self, file):
        self._file = file
        self._roaster = ""
        self._country = ""
        self._region = ""
        self._stars = ""
        self._old_coffee = self.load_coffee()
        self._new_coffee = []

    def load_coffee(self):
        coffee = []
        with open(self._file) as f:
            reader = csv.reader(f, delimiter=',')
            for row in reader:
                coffee.append(row)
        return coffee

    @property
    def roaster(self):
        return self._roaster
    @roaster.setter
    def roaster(self, new_roaster):
        self._roaster = new_roaster
    @property
    def country(self):
        return self._country
    @country.setter
    def country(self, new_country):
        self._country = new_country
    @property
    def region(self):
        return self._region
    @region.setter
    def region(self, new_region):
        self._region = new_region
    @property
    def stars(self):
        return self._stars
    @stars.setter
    def stars(self, new_stars):
        self._stars = new_stars

    def save(self):
        with open(self._file, 'a') as f:
            writer = csv.writer(f)
            writer.writerows(self._new_coffee)

    def show_coffee(self):
        print()
        if len(self._old_coffee) < 2 and len(self._new_coffee) == 0:
            print("Enter a coffee first")
        elif len(self._old_coffee) < 2 and len(self._new_coffee) == 0:
            for row in self._old_coffee:
                print(f"{row[0]:15} {row[1]:15} {row[2]:15}  {row[3]:15}")
        else:
            for row in self._old_coffee:
                print(f"{row[0]:15} {row[1]:15} {row[2]:15}  {row[3]:15}")
            for row in self._new_coffee:
                print(f"{row[0]:15} {row[1]:15} {row[2]:15}  {row[3]:15}")
        print()

    def add_coffee(self):
        self._new_coffee.append([self._roaster, self._country, self._region, self._stars])

def main_menu():
    print("Coffess of the World")
    print("\t1. Show Coffee")
    print("\t2. Add Coffee")
    print("\t3. Save and Quit")
    choice = int(input("Enter the number of your selection: "))
    return choice

def perform_action(choice, coffee):
    if choice == 1:
        coffee.show_coffee()
    elif choice == 2:
        enter_coffee(coffee)
    elif choice == 3:
        quit(coffee)




# **********************************************
# code for testing your script
# **********************************************

# test_object3 = CoffeeJournal("test_journal1.csv")
# test_object3.roaster = "Peace River"
# test_object3.country = "Rawanda"
# test_object3.region = "Remera"
# test_object3.stars = "***"
# test_object3.add_coffee()
# test_object3.save()
# test_object3._old_coffee = test_object3.load_coffee()
# test_object3._roaster = ""
# test_object3._country = ""
# test_object3._region = ""
# test_object3._stars = ""
# test_object3._new_coffee = []
# test_object3.show_coffee()


# test_object2 = CoffeeJournal("test_journal1.csv")
# test_object2.show_coffee()


# test_object = CoffeeJournal("test_journal1.csv")
# print(test_object._old_coffee)
# test_object = CoffeeJournal("test_journal1.csv")
# test_object.roaster = "Peace River"
# test_object.country = "Rawanda"
# test_object.region = "Remera"
# test_object.stars = "***"
# print(test_object.roaster)
# print(test_object.country)
# print(test_object.region)
# print(test_object.stars)