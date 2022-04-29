
from fighter import Fighter
from wizard import Wizard


class Warrior(Fighter):

    def __init__(self) -> None:
        self._fighter = "Warrior"
        self._vulnerable = False
        self._damagepoints = None
        pass

    @property
    def toString(self):
        return self._fighter

    def isVulnerable(self):
        return self._vulnerable


    def damagePoints(self, figther):
        if isinstance(figther, Wizard):
            if figther.isVulnerable() is True:
                self._damagepoints = 10
            else:
                self._damagepoints = 6
            return self._damagepoints

        else:
            print("Fighter no es tipo Wizard.")
            raise TypeError

    """
    @dispatch (Wizard)
    def damagePoints(self, warrior):
        if warrior.isVulnerable is True:
            self._damagepoints = 10
        else:
            self._damagepoints = 6
        print(self._damagepoints)
    """
            

        
    
    