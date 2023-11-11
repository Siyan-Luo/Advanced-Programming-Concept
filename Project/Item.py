class Item:
    """This is the Item class, it's the parent class of EnergyPotion, HPpotion, Shield, and Weapon

           Attributes:
               name (str): The name.
               weight (int): The weight.
               price (int): The price.
    """
    def __init__(self, name, weight, price):
        """Constructor method for Item.

                Args:
                    name (str): The name.
                    weight (int): The weight.
                    price (int): The price.
        """
        self._name = name
        self._weight = weight
        self._price = price


    def getName(self):
        """
            This function gets the name of the item

            Args:
                none.

            Returns:
                str: the name of the item.
        """
        return self._name

    def getWeight(self):
        """
            This function gets the weight of the item.

            Args:
                none.

            Returns:
                int: the weight of the item.
        """
        return self._weight

    def getPrice(self):
        """
            This function gets the price of the item.

            Args:
                none.

            Returns:
                int: the price of the item.
        """
        return self._price

    def display(self):
        """
            This function displays the attributes of the item.

            Args:
                none.

            Returns:
                none.
        """
        print("name:" + str(self._name))
        print("weight: " + str(self._weight))
        print("price: " + str(self._price))