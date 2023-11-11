
init_maxHP = 100
init_level = 1
init_money = 100
init_maxLoad = 50
init_maxEnergy = 100
init_maxExperience = 100
maxLevel = 5
# The increase every time upgrade
increase = 1.5

from Item import Item
from Weapon import Weapon
from Monster import Monster
from Shield import Shield
from HPpotion import HPpotion
from EnergyPotion import EnergyPotion

class Adventurer:
    """This is the adventurer class.

       Attributes:
           name (str): The name of the adventurer.
           maxHP (int): The maximum HP value.
           alive (Boolean): The living status, the initial value is True
           present (Boolean): The present status, the initial value is True.
           backpack (list<Item>): The backpack, it contains all the possessions.
           level (int): The reached level.
           money (int): The amount of coins.
           hp (int): The current HP value.
           load (int): The current load of the backpack.
           maxLoad (int): The maximum load of the backpack.
           energy (int): The current energy value.
           maxEnergy (int): The maximum energy value.
           experience (int): The current experience value.
           maxExperience (int): The maximum experience value.
           unlocked (list<str>): The unlocked battle-field/stage, the initial one is 1.1.
           defencePower (int): The defence power, it's the same value as the shield the adventurer equipped with,
                               the initial value is 0.
    """
    def __init__(self, name):
        """Constructor method for Adventurer.

               Args:
                   name (str): The name of the adventurer.
        """
        self._name = name
        self._maxHP = init_maxHP
        self._alive = True
        self._present = True
        self._backpack = list()
        self._level = 1
        self._money = init_money
        self._hp = init_maxHP
        self._load = 0
        self._maxLoad = init_maxLoad
        self._energy = init_maxEnergy
        self._maxEnergy = init_maxEnergy
        self._experience = 0
        self._maxExperience = init_maxExperience
        self._unlocked = ["1.1"]
        self._defencePower = 0


    def display(self):
        """
            This function displays the current information about the adventurer.

            Args:
                none.

            Returns:
                none.
        """
        print("Adventurer name: " + self._name)
        print("Current hp/Max hp: " + str(self._hp) + "/" + str(self._maxHP))
        print("Current energy:" + str(self._energy) + "/" + str(self._maxEnergy))
        print("Current load/Max load: " + str(self._load) + "/" + self._maxLoad.__str__())
        print("Current level: " + str(self._level))
        print("Current experience: " + self._experience.__str__())
        print("Current money: " + self._money.__str__())
        print("Current defence power: " + self._defencePower.__str__())
        print("Unlocked battle field: " + self._unlocked.__str__())


    def displayBackpack(self):
        """
            This function displays what are in the backpack.

            Args:
                none.

            Returns:
                none.
        """
        print('Item(s) in your backpack:')
        for i, item in enumerate(self._backpack):
            print('--Item ' + str(i) + '--' )
            item.display()

    def usePotion(self):
        """
            This function allows the adventurer use potions to recover hp points or energy points.

            Args:
                none.

            Returns:
                none.
        """
        # Firstly, we find out which potions are there in the backpack
        potionIndices = [i for i, item in enumerate(self._backpack) if isinstance(item, (HPpotion, EnergyPotion))]
        for i in potionIndices:
            print(str(i) + '.')
            self._backpack[i].display()
            # Traverse all potion elements in the _backpack list and
            # print out their indexes and corresponding information
        # If there are potions available in the backpack,
        # make the adventurer choose which one he would like to use.
        # Otherwise, using potions fails
        if len(potionIndices) > 0:
            validInput = False
            while not validInput:
                choice = input("Please enter the index of potion you want to use: ")
                try:
                    choice = int(choice)
                    if choice in potionIndices:
                        validInput = True
                        potion = self._backpack[choice]
                        self._load -= potion.getWeight()
                        if type(potion) == HPpotion:
                            self.updateHP(potion.getHP())
                        else:
                            self.updateEnergy(potion.getEnergy())
                        del self._backpack[choice]
                except ValueError:
                    print("Invalid input")
        else:
            print("There is no potion left in you backpack.")
            print("----------------------------------------")


    def updateHP(self, h):
        """
            This function updates the hp points of the adventurer.

            Args:
                h (int): The change of hp points.

            Returns:
                none.
        """
        self._hp += h
        # Check if the hp points get increased or decreased
        if h > 0:
            # Check do not exceed the maximum value
            if self._hp > self._maxHP:
                print("The hp value powered, your hp value is full now.")
                self._hp = self._maxHP
            else:
                print("The hp value got increased by " + str(abs(h)))
        else:
            print("Your hp value got decreased by " + str(abs(h)))
            # Check if the adventurer has lost all the hp
            if self._hp <= 0:
                print("You have lost all your hp.")
                self._alive = False
            else:
                print("You have ", self._hp, " hp points left.")
        print("---------------------------------------------")


    def updateMoney(self, m):
        """
            This function updates the money of the adventurer.

            Args:
                m (int): The change of money.

            Returns:
                boolean: If the update succeeds or not.
        """
        # Check if it's adding money or losing money
        if m > 0:
            print("You got " + str(m) + " coins.")
            self._money += m
            print("Now you have " + str(self._money) + " coins.")
        # When losing money, it's getting products from the shop
        if m < 0:
            # Check if the balance is enough
            if self._money + m >= 0:
                self._money += m
                print("You spent " +str(abs(m)) + " coins.")
                print("Now you have " + str(self._money) + " coins.")

            else:
                # self._money -= m
                print("You only have " + str(self._money) + " coins.")
                print("You don't have enough money. Transaction failed.")
                return False
        return True

    def buy(self, item):
        """
            This function allows the adventurer buy items from the shop.

            Args:
                item (Item): The wanted item.

            Returns:
                none.
        """
        # Check if there is enough space in the backpack
        if self._load + item.getWeight() <= self._maxLoad:
            # Check if the update of money is True, which means there is enough balance left
            if self.updateMoney(-item.getPrice()) == True:
                print("you bought the item successfully ")
                self.addItem(item)
        else:
            print("Sorry, there is no enough space in your backpack.")
            print("-------------------------------------------------")

    def updateExperience(self, e):
        """
            This function updates the experience points,
            and the adventurer level if the updated experience has reached the threshold.

            Args:
                e (int): The change of experience points.

            Returns:
                none.
        """
        self._experience += e
        # Check if the adventurer has reached the highest level
        if self._level < maxLevel:
            # Check if the increased experience has reached the threshold for upgrading level
            if self._experience > self._maxExperience:
                self._level += 1
                # upgrade the maximum values of attributes
                self._maxExperience = round(init_maxExperience * (increase ** (self._level - 1)))
                print("You reached level " + str(self._level))
                self._experience -= self._maxExperience
                self._maxHP = round(init_maxHP * (increase ** (self._level - 1)))
                self._maxLoad = round(init_maxLoad * (increase ** (self._level - 1)))
                self._maxEnergy = round(init_maxEnergy * (increase ** (self._level - 1)))
        else:
            print("You have reached the highest level.")


    def updateEnergy(self, e):
        """
            This function updates the energy points.

            Args:
                e (int): The change of the energy points.

            Returns:
                none.
        """
        self._energy += e
        if e > 0:
            # When power up energy, check if it has reached the maximum value
            if self._energy > self._maxEnergy:
                self._energy = self._maxEnergy
                print("The energy value powered, your energy is full now.")
            else:
                print("Your energy increased by", e)
            print("Current energy point: ", self._energy)
        else:
            print("This attack cost you " + str(abs(e)) + " energy points.")
            # When losing energy, check if there's energy left
            if self._energy <= 0:
                print("You have lost all your energy.")
                self._alive = False
            else:
                print("You have ", self._energy, " energy points left.")
        print("-----------------------------------------")



    def addItem(self, i: Item):
        """
            This function adds items to the backpack.

            Args:
                i (Item): The added item.

            Returns:
                itself, recursive function.
        """
        # Check if there is enough space in the backpack
        if self._load + i.getWeight() > self._maxLoad:
            print("Sorry, there's no enough space in your backpack for the loot drops.")
            print("Do you want to drop anything for it? ")
            choice = input("Enter yes or no: ")
            print("")
            if choice.lower() == "yes":
                if self.dropItem() == True:
                    # Successfully dropped item, then try to add the item again
                    return self.addItem(i)
        else:
            self._backpack.append(i)
            self._load += i.getWeight()
            print(str(i.getName()) + " was added.")


    def dropItem(self):
        """
            This function allows the adventurer to drop items.

            Args:
                none.

            Returns:
                Boolean: If the dropping operation succeeds or not.
        """
        print("Choose one of the item(s) you want to drop:")
        # The index starts from 1 because the 0th one is the fist which can't be dropped
        for i in range(1, len(self._backpack)):
            item = self._backpack[i]
            print("--Item " + str(i) +'--')
            item.display()
        choice = input("Enter the item index to drop, or anything else if you change your mind: ")
        if choice in [str(i) for i in range(1, len(self._backpack))]:
            # validInput = True
            self._load -= self._backpack[choice].getWeight()
            print("Successfully dropped ", self._backpack[choice].getName())
            del self._backpack[choice]
            return True
        else:
            return False


    def addUnlocked(self, field_name):
        """
            This function adds the unlocked field to the unlocked-field list.

            Args:
                field_name (str): The name of the field.

            Returns:
                none.
        """
        if field_name not in self._unlocked:
            self._unlocked.append(field_name)


    def getUnlocked(self):
        """
            This function gets the unlocked-stage list.

            Args:
                none.

            Returns:
                list: The unlocked-stage list.
        """
        return self._unlocked

    def escape(self):
        """
            This function allows the adventurer to escape,
            changing the present status to False.

            Args:
                none.

            Returns:
                none.
        """
        self._present = False

    def back(self):
        """
            This function brings the adventurer back to the battlefield,
            changing the present status to True.

            Args:
                none.

            Returns:
                none.
        """
        self._present = True

    def getStatus(self):
        """
            This function gets the living status.

            Args:
                none.

            Returns:
                Boolean: the living status of the adventurer.
        """
        return self._alive

    def attack(self, m: Monster):
        """
            This function allows the adventurer make an attack to the monster.

            Args:
                m (Monster): The attacked monster.

            Returns:
                none.
        """
        print("Good choice! You can use one of the following weapons to fight: ")
        # Firstly, check what are the weapons in the backpack
        # weaponIndices = []
        # for i, item in enumerate(self._backpack):
        #     if type(item) == Weapon:
        #         print('--Weapon ' + str(i) + '--')
        #         item.display()
        #         weaponIndices.append(str(i))
        weaponIndices = [str(i) for i, item in enumerate(self._backpack) if isinstance(item, Weapon)]
        for i in weaponIndices:
            print(f'--Weapon {i}--')
            self._backpack[int(i)].display()

        validInput = False
        while not validInput:
            choice = input("Which one would you like to use? Please enter your option:")
            print("")
            if choice in weaponIndices:
                validInput = True
                print("FIGHT!!!")
                print("")
                # get the chosen weapon
                w = self._backpack[int(choice)]
                # get the attack power and energy consumption
                attackPower = w.getAttackPower()
                energyConsumption = w.getEnergyConsumption()
                # The monster gets attacked
                m.attacked(attackPower)
                # Show the information of the monster if it's still alive
                if m.getStatus() == True:
                    m.display()
                self.updateEnergy(-energyConsumption)
            else:
                print("Invalid input.")

    def attacked(self, m: Monster):
        """
            This function allows the adventurer be attacked by the monster.

            Args:
                m (Monster): The attacking monster.

            Returns:
                none.
        """
        defencePower = self.getDefencePower()
        # The lost hp is the attack power of the monster minus the defence power of the adventurer
        attackPower = m.getAttackPower() - defencePower
        print("You got attacked by the monster.")
        self.updateHP(-attackPower)

    def equipSheild(self):
        """
            This function equips the adventurer with the best sheild in the backpack.

            Args:
                none.

            Returns:
                none.
        """
        # Check if there are shields in the backpack, if so, equip the most powerful one
        hasSheild = False
        for i in self._backpack:
            if type(i) == Shield:
                hasSheild = True
                if i.getDefencePower() > self._defencePower:
                    self._defencePower = i.getDefencePower()

        if not hasSheild:
            self._defencePower = 0
            print("Oops! There is no shield in your backpack, your defence power is 0.")
            print("---------------------------------------------------------------------")
        else:
            print("You are equipped with the most powerful shield in your backpack, which defend you from ", self._defencePower, " attack points.")
            print("-----------------------------------------------------------------------------------------------------------------")


    def getDefencePower(self):
        """
            This function gets the defence power.

            Args:
               none.

            Returns:
                int: the defence power.
        """
        self.equipSheild()
        return self._defencePower

    def sellItem(self):
        """
            This function allows the adventurer to sell items.

            Args:
                none.

            Returns:
                none.
        """
        # print("Please choose an item you want to sell expect fist.")
        # It is only possible to make sell operation when there are items except the fist
        if len(self._backpack) > 1:
            self.displayBackpack()
            print("Please note that the selling price is 20% less.")
            validInput = False
            while not validInput:
                choice = input("Please choose an item you want to sell (expect fist):")
                choice = int(choice)
                if choice in range(1, len(self._backpack)):
                        validInput = True
                        weight = self._backpack[choice].getWeight()
                        price = self._backpack[choice].getPrice() * 0.8
                        # Update backpack and money
                        self._load -= weight
                        self.updateMoney(price)
                        self._backpack.pop(choice)
        else:
            print("Sorry, there is nothing available to sell in your backpack.")
            print("-----------------------------------------------------------")































