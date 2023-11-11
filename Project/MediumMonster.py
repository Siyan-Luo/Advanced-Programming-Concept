from Monster import Monster
from Item import Item

class MediumMonster(Monster):
    """This is the MediumMonster class, it's a subclass of Monster class.

           Attributes:
               name, hp, xp, attack_power, level same as Monster class.
               gold (int): The number of coins carried by the monster,
                           it will be obtained by the adventurer once the monster loses.
               equipment (Item): The equipment carried by the monster,
                                 it will be obtained by the adventurer once the monster loses.
    """
    def __init__(self, name, hp, xp, attack_power, level, gold, equipment: Item):
        """Constructor method for MediumMonster.

               Args:
                   name, hp, xp, attack_power, level same as Monster class.
                   gold (int): The number of coins carried by the monster,
                               it will be obtained by the adventurer once the monster loses.
                   equipment (Item): The equipment carried by the monster,
                                     it will be obtained by the adventurer once the monster loses.
        """
        super().__init__(name, hp, xp, attack_power, level)
        self._gold = gold
        self._equipment = equipment

    def getGold(self):
        """
            This function gets the gold carried by the monster.

            Args:
                none.

            Returns:
                int: get the carried gold of the monster.
        """
        return self._gold

    def getEquipment(self):
        """
            This function gets the item carried by the monster.

            Args:
                none.

            Returns:
                Item: get the carried item of the monster.
        """
        return self._equipment

    def display(self):
        """
            This function displays the attributes of the monster.

            Args:
                none.

            Returns:
                none.
        """
        print("Monster name: " + str(self._name))
        print("Health points: " + str(self._hp))
        print("Carried experience: " + str(self._xp))
        print("Attack power: " + str(self._attack_power))
        print("Carried gold: " + str(self._gold))
        print("Carried item: " + str(self._equipment.getName()))