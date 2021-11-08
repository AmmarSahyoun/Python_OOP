class LoggingProxy:
    """Intercept and log all attribute access to an object."""

    def __init__(self, target):
        super().__setattr__("target", target)

    """ Intercept all attribute reads through the dot operator """
    def __getattribute__(self, name):
        target = super().__getattribute__("target")
        try:
            value = getattr(target, name)
        except AttributeError as e:
            raise AttributeError(
                "{} could not forward request {} to {}".format(
                    super().__getattribute__("__class__").__name__,
                    name,
                    target
                )
            ) from e
        print(f"Retrieved attribute {name} == {value!r} from {target!r}")
        return value

    """ Intercept attribute writes """
    def __setattr__(self, name, value):
        target = super().__getattribute__("target")
        try:
            setattr(target, name, value)
        except AttributeError as e:
            raise AttributeError(
                "{} could not forward request {} to {}".format(
                    super().__getattribute__("__class__").__name__,
                    name,
                    target
                )
            ) from e
        print(f"Set attribute {name} == {value!r} on {target!r}")

    """ Get the string representation of the target ColoredVector rather than LoggingProxy"""
    def __repr__(self):
        target = super().__getattribute__("target")
        repr_callable = getattr(target, "__repr__")
        return repr_callable()