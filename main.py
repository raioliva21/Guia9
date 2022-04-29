
from warrior import Warrior
from wizard import Wizard

"""clase principal"""
class Battlefield():

    def __init__(self) -> None:
        warrior = Warrior()
        wizard = Wizard()

        for n in range(0,4):

            print("_____________________________")
            # asigna booleano a atributo 'self._prepateSpell'
            # tal atrbito es de clase 'Wizard'
            wizard.prepareSpell()
            # objeto 'wizard' ataca a 'warrior', y viceversa
            self.attack(wizard, warrior)
            self.attack(warrior, wizard)
            print("_____________________________")

    """aplica polimorfismo"""
    # funcion asociado a ataque de objeto a otro objeto
    def attack(self, object, object_attacked):

        damage_points = object.damagePoints(object_attacked)
        print(f"{object.toString} genera\
 {damage_points} puntos de daño a oponente.")


if __name__ == "__main__":
    battlefield = Battlefield()