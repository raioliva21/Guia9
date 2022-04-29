
from abc import abstractmethod
from abc import ABCMeta

"""Clase abstracta"""
class Fighter(metaclass = ABCMeta):

    def __init__(self) -> None:
        self._fighter = None
        self._vulnerable = None
        self._damagepoints = None
        pass

    @abstractmethod
    def toString (self):
        pass

    @abstractmethod
    def isVulnerable (self):
        pass

    @abstractmethod
    def damagePoints (self):
        pass




