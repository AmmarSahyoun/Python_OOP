import abc

""" The interface acts as a blueprint for designing other classes substitution"""
class AbsAuto(abc.ABC):

    @abc.abstractmethod
    def start(self):
        pass

    @abc.abstractmethod
    def stop(self):
        pass
