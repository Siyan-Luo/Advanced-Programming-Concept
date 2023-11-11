from Item import Item

class Weapon(Item):
    """This is the Weapon class, it's a subclass of Item class

           Attributes:
               name, weight, price same as Item class.
               attackPower (int): The attack power of the weapon,
                                  it's the hp loss of the monster when gets attacked by this weapon.
               energyConsumption (int): The energy consumption of the weapon,
                                        the energy cost of using this weapon.
    """
    def __init__(self, name, weight, price, attack_power, energyConsumption):
        """Constructor method for Weapon.

                Args:
                    name, weight, price same as Item class.
                    attackPower (int): The attack power of the weapon,
                                       it's the hp loss of the monster when gets attacked by this weapon.
                    energyConsumption (int): The energy consumption of the weapon,
                                             the energy cost of using this weapon.
         """
        super().__init__(name, weight, price)
        self._attackPower = attack_power
        self._energyConsumption = energyConsumption

    def display(self):
        """
            This function displays the attributes of the weapon.

            Args:
                none.

            Returns:
                none.
        """
        print("Name:" + self._name)
        print("Weight: " + self._weight.__str__())
        print("Price: " + self._price.__str__())
        print("Attack power: " + self._attackPower.__str__())
        print("Energy consumption: " + self._energyConsumption.__str__())
        print("--------------------------------")


    def getAttackPower(self):
        """
            This function displays the attack power of the weapon.

            Args:
                none.

            Returns:
                int: The attack power.
        """
        return self._attackPower

    def getEnergyConsumption(self):
        """
            This function gets the energy consumption every time using this weapon.

            Args:
                none.

            Returns:
                int: The energy consumption.
        """
        return self._energyConsumption