from Item import Item

class EnergyPotion(Item):
    """This is the EnergyPotion class, it's a subclass of Item class

           Attributes:
               name, weight, price same as Item class.
               egRegenaation (int): The energy regeneration value of the potion.
    """
    def __init__(self, name, weight, price, egRegeneration):
        """Constructor method for EnergyPotion.

                Args:
                    name, weight, price same as Item class.
                    egRegenaation (int): The energy regeneration value of the potion.
         """
        super().__init__(name, weight, price)
        self._egRegeneration = egRegeneration


    def getEnergy(self):
        """
            This function gets the energy points of the potion.

            Args:
                none.

            Returns:
                int: the energy points of the potion.
        """
        return self._egRegeneration

    def getWeight(self):
        """
            This function gets the weight of the potion.

            Args:
                none.

            Returns:
                int: the weight of the potion.
        """
        return self._weight

    def display(self):
        """
            This function displays the attributes of the potion.

            Args:
                none.

            Returns:
                none.
        """
        print("Name:" + str(self._name))
        print("Weight: " + str(self._weight))
        print("Price: " + str(self._price))
        print("Energy  value:" + str(self._egRegeneration))
        print("--------------------------------")