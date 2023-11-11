from Item import Item

class Shield(Item):
    """This is the Shield class, it's a subclass of Item class

           Attributes:
               name, weight, price same as Item class.
               defencePower (int): The defence power of the shield,
                                    it can decrease the hp loss when the adventurer gets attacked.
    """
    def __init__(self, name, weight, price, defencePower):
        """Constructor method for Shield.

                Args:
                    name, weight, price same as Item class.
                    defencePower (int): The defence power of the shield,
                                        it can decrease the hp loss when the adventurer gets attacked.
         """
        super().__init__(name, weight, price)
        self._defencePower = defencePower

    def getDefencePower(self):
        """
            This function gets the defence power of the shield.

            Args:
                none.

            Returns:
                int: the defence power.
        """
        return self._defencePower

    def display(self):
        """
            This function displays the attributes of the shield.

            Args:
                none.

            Returns:
                none.
        """
        print("Name:" + str(self._name))
        print("Weight: " + str(self._weight))
        print("Price: " + str(self._price))
        print("Defence power: " + str(self._defencePower))
        print("--------------------------------")