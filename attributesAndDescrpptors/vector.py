
class Vector:
    """An n-dimensional vector with Immutable attributes"""

    """ Immutable Attributes woth Read-only Properties"""
    def __init__(self, **components):
        private_components = {f"_{k}": v for k, v in components.items()}
        self.__dict__.update(private_components)

    """ Intercept attribute access by override __getattr__invoked after failed attribute lookups"""
    def __getattr__(self, name):
        private_name = f"_{name}"
        try:
            return self.__dict__[private_name]
        except KeyError:
            raise AttributeError(f"{self!r} object has no attribute {name!r}")


    """ Prevent write access to our attributes by overriding __setattr__"""
    def __setattr__(self, name, value):
        raise AttributeError(f"Can't set attribute {name!r}")


    """ Prevent attributes delete by overriding __delattr__"""
    def __delattr__(self, name):
        raise AttributeError(f"Can't delete attribute {name!r}")


    def __repr__(self):
        return "{}({})".format(type(self).__name__, ", ".join("{k}={v}".format(k=k, v=v,)
                                                for k, v in self._args().items() ))
    """ return mapping of the constructor argument names """
    def _args(self):
        return {k[1:]: v for k, v in self.__dict__.items()}


class ColoredVector(Vector):
    """ Mutable color channel attributes by override __setattr__  """

    COLOR_INDEXES = ("red", "green", "blue")

    def __init__(self, red, green, blue, **components):
        super().__init__(**components)
        self.__dict__["_color"] = [red, green, blue]

    def __getattr__(self, name):
        try:
            channel = ColoredVector.COLOR_INDEXES.index(name)
        except ValueError:
            return super().__getattr__(name)
        else:
            return self.__dict__["_color"][channel]

    def __setattr__(self, name, value):
        try:
            channel = ColoredVector.COLOR_INDEXES.index(name)
        except ValueError:
            super().__setattr__(name, value)
        else:
            self.__dict__["_color"][channel] = value

    def _args(self):
        args = {"red": self.red, "green": self.green, "blue": self.blue }
        args.update(super()._args())
        del args["color"]
        return args

""" It is better to prefer composition over inheritance because Vector class is not 
    deliberately designed as a parent class to the ColoredVector class """