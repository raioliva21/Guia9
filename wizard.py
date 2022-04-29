
import random
from fighter import Fighter


class Wizard(Fighter):
        
    def __init__(self) -> None:
        self._fighter = "Wizard"
        self._vulnerable = False
        self._damagepoints = None
        self._prepareSpell = False
        pass
    
    @property
    def toString(self):
        return self._fighter

    def isVulnerable(self):
        if self._prepareSpell is True:
            self._vulnerable = False
        else:
            #print("Wizard no ha preparado ataque.")
            #print("Wizard es vulnerable.")
            self._vulnerable = True
        return self._vulnerable

    def prepareSpell(self):
        self._prepareSpell = random.choice([True, False])
        self.isVulnerable()
    
    def damagePoints(self, figther):
        if isinstance(figther, Fighter):
            if self._prepareSpell is True:
                self._damagepoints = 12
            else:
                self._damagepoints = 3
            return self._damagepoints
        else:
            print("Fighter no es tipo Warrior.")
            raise TypeError
    

    