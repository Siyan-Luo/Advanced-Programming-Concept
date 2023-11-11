class Shop():
    """This is the Shop class.

           Attributes:
               items (list<Item>): it contains products in the shop.
    """
    def __init__(self):
        """Constructor method for Shop.

                Args:
                    none.
         """

        self._items = []

    def addItem(self, item):
        """
            This function adds item to the shop.

            Args:
                none.

            Returns:
                none.
        """
        self._items.append(item)

    def display(self):
        """
            This function displays the goods in the shop.

            Args:
                none.

            Returns:
                none.
        """
        for i in range(len(self._items)):
            print(str(i) + '.')
            self._items[i].display()


    def getItem(self, index):
        """
            This function gets a specific item from the shop.

            Args:
                index(int): the index of the item in the shop.

            Returns:
                Item: the wanted item.
        """
        return self._items[index]

    def getLen(self):
        """
            This function gets the number of varieties of the shop.

            Args:
                none.

            Returns:
                int: the number of varieties.
        """
        return len(self._items)