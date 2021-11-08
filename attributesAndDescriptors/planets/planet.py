from positive import Positive

class Planet:
    def __init__(self,name,radius_metres,mass_kilograms,orbital_period_seconds,surface_temperature_kelvin):
        self.name = name
        self.radius_metres = radius_metres
        self.mass_kilograms = mass_kilograms
        self.orbital_period_seconds = orbital_period_seconds
        self.surface_temperature_kelvin = surface_temperature_kelvin

    """To assure that the values of the attributes for new instance are in a proper range we encapsulate 
    our attributes in property getter & setter which perform a validation by checking there values """
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not value:
            raise ValueError("Cannot set empty name")
        self._name = value

    radius_metres = Positive()
    mass_kilograms = Positive()
    orbital_period_seconds = Positive()
    surface_temperature_kelvin = Positive()


