from Item import Item

class HPpotion(Item):
    """This is the HPpotion class, it's a subclass of Item class

           Attributes:
               name, weight, price same as Item class.
               hpRegenaation (int): The HP regeneration value of the potion.
    """
    def __init__(self, name, weight, price, hpRegeneration):
        """Constructor method for HPpotion.

                Args:
                    name, weight, price same as Item class.
                    hpRegenaation (int): The HP regeneration value of the potion.
         """
        super().__init__(name, weight, price)
        self._hpRegeneration = hpRegeneration

    def getHP(self):
        """
            This function gets the HP points of the potion.

            Args:
                none.

            Returns:
                int: the hp points of the potion.
        """
        return self._hpRegeneration

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
        print("Hp value:" + str(self._hpRegeneration))
        print("--------------------------------")