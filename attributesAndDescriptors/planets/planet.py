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

    @property
    def radius_metres(self):
        return self._radius_metres

    @radius_metres.setter
    def radius_metres(self, value):
        if value <= 0:
            raise ValueError(f"radius_metres value {value} is not positive.")
        self._radius_metres = value

    @property
    def mass_kilograms(self):
        return self._mass_kilograms

    @mass_kilograms.setter
    def mass_kilograms(self, value):
        if value <= 0:
            raise ValueError(f"mass_kilograms value {value} is not positive.")
        self._mass_kilograms = value

    @property
    def orbital_period_seconds(self):
        return self._orbital_period_seconds

    @orbital_period_seconds.setter
    def orbital_period_seconds(self, value):
        if value <= 0:
            raise ValueError(f"orbital_period_seconds value {value} is not positive.")
        self._orbital_period_seconds = value

    @property
    def surface_temperature_kelvin(self):
        return self._surface_temperature_kelvin

    @surface_temperature_kelvin.setter
    def surface_temperature_kelvin(self, value):
        if value <= 0:
            raise ValueError(f"surface_temperature_kelvin value {value} is not positive.")
        self._surface_temperature_kelvin = value

