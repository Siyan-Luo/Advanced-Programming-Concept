from Adventurer import Adventurer
from Monster import Monster
from SmallMonster import SmallMonster
from MediumMonster import MediumMonster
from Weapon import Weapon
from EnergyPotion import EnergyPotion
from HPpotion import HPpotion
from Shield import Shield
from Shop import Shop

class Game():
    """This is the Game class, all the other classes except main interact in this class

           Attributes:
               adventurer (Adventurer): The adventurer in the game.
               enemyList (list<Monster>): The enemies (monsters) of the game.
               shop (Shop): The shop of the game.
               quit (Boolean): If the player has quit the game or not, the initial value is False.
    """

    def __init__(self):
        """Constructor method for Game.

                Args:
                    none.
         """
        self._adventurer = 0
        self._enemyList = []
        self._shop = Shop()
        self._quit = False

    def printIntro(self):
        """
            This function prints the introduction of the game.

            Args:
                none.

            Returns:
                none.
        """
        print('----Welcome to the Zork-style text-based game!----')
        print('')
        print('In this game, you will take on the role of an adventurer, ')
        print('who must battle through three stages filled with challenging enemies. ')
        print('To succeed, you will need to gain experience and money, ')
        print('which can be used to level up your character and purchase helpful items.')
        print('')
        print('To navigate through the game, you will be presented with a main menu ')
        print('where you can choose from six different operations: ')
        print('"Go to the battle field" "Recover your HP or energy" "Go to the shop" "Show my backpack" "Show my status" and "Exit the game" ')
        print('Use the arrow keys or type the corresponding number to select your desired option.')
        print('')
        print('During battles, you will need to select your actions carefully to defeat your opponents ')
        print('while preserving your own health and energy levels. ')
        print('You can choose to attack, recover, or run away. ')
        print('Use your strategic thinking to win the battle and move on to the next stage.')
        print('')
        print('Do not forget to use the "recover" operation to replenish your health and energy levels when necessary, ')
        print('and the "shop" operation to purchase helpful items such as weapons, shields, and potions. ')
        print('Keep track of your items using the "bag" operation and monitor your progress using the "status" operation.')
        print('')
        print('Good luck on your adventure!')
        print('----------------------------')

    def attack(self, monster):
        """
            This function allows a round of attacking each other

            Args:
                monster (Monster): The monster in the attack.

            Returns:
                none.
        """
        # The adventurer makes the attack first
        self._adventurer.attack(monster)
        # If the monster and adventurer are both alive, the monster attacks back
        if monster.getHp() > 0 and self._adventurer.getStatus():
            print("Watch out! The enemy is trying to attack you! ")
            print("")
            self._adventurer.attacked(monster)

    def battle(self, gameStage):
        """
            This function allows the battle in a specific game field.

            Args:
                gameStage (str): The name of the battle-field/stage.

            Returns:
                none.
        """

        print("Hello adventurer, here is the enemy you are going to challenge: ")
        print("----------------------------------------------------------------")
        self.refreshEnemy()
        m = next(filter(lambda i: str(i.getLevel()) == gameStage, self._enemyList), Monster("1", 1, 1, 1, 1))

        statusA = self._adventurer.getStatus()
        statusM = m.getStatus()

        # Display the monster information
        m.display()
        print("----------------------------------------------------------------")
        # The battle continues if nobody dies
        while statusA and statusM:
            print("Which action would you like to take: 1. Attack; 2. Recover; 3. Escape.")
            # print("Please enter your option: ")
            invalidInput = False
            while not invalidInput:
                choice = input("Please enter your option: ")
                print("")
                try:
                    choice = int(choice)
                    if choice in range(1, 4):
                        invalidInput = True
                        if choice == 1:
                            self._adventurer.back()
                            self.attack(m)
                            # Update the status
                            statusA = self._adventurer.getStatus()
                            statusM = m.getStatus()
                        if choice == 2:
                            self._adventurer.usePotion()
                        if choice == 3:
                            self._adventurer.escape()
                            return
                except ValueError:
                    print("Invalid input, please try again.")
        # If the adventurer is alive and the monster is dead
        if statusA and not statusM:
            print("You won the battle!")
            # If it's not the final stage,
            # update the obtained experience, money, item from the triumph,
            # and unlock the next field/stage
            if gameStage != '3':
                xp = m.getXP()
                g = m.getGold()
                self._adventurer.updateExperience(xp)
                self._adventurer.updateMoney(g)
                if type(m) == MediumMonster:
                    item = m.getEquipment()
                    print("You won ", item.getName())
                    self._adventurer.addItem(item)
                newGameStage = {
                    1.1: 1.2,
                    1.2: 2.1,
                    2.1: 2.2,
                    2.2: 3
                }.get(float(gameStage))
                if newGameStage is not None:
                    self._adventurer.addUnlocked(str(newGameStage))
                else:
                    self._adventurer.addUnlocked("4")  # 4 indicates victory in the whole game
                # Finds the corresponding next stage based on the current game stage gameStage
                # adds it to the player object's list of unlocked stages.
                # If no value for the next stage is found, assume the game is complete and
                # add the string representing the victory status to the list of unlocked stages


    def generatePlayer(self):
        """
            This function generate the adventurer, allow user to put the name.

            Args:
                none.

            Returns:
                none.
        """
        adventurerName = input("Please enter your name:")
        # print('----------------------------')
        self._adventurer = Adventurer(adventurerName)

    def generateEnemiesItems(self):
        """
            This function generates enemies and items.

            Args:
                none.

            Returns:
                none.
        """
        hpPotion1 = HPpotion(name='HP Potion(small)', weight=10, price=100, hpRegeneration=100)  # name, weight, price
        hpPotion2 = HPpotion('HP Potion(large)', 15, 200, 300)
        energyPotion1 = EnergyPotion('Energy Potion(small)', 10, 100, 100)
        energyPotion2 = EnergyPotion('Energy Potion(large)', 15, 200, 300)

        fist = Weapon('Your fist', 0, 0, 20, 10)  # name, weight, price, attack_power, energyConsumption
        # The initial item in the backpack is fist
        self._adventurer._backpack.append(fist)

        weapon1 = Weapon('Dagger', 16, 10, 80, 15)
        weapon2 = Weapon('Sword', 20, 100, 50, 10)
        shield1 = Shield('Wooden Shield', 10, 100, 5)  # name, weight, price, defencePower
        shield2 = Shield('Ironclad Defender', 20, 200, 10)

        self._enemyList.append(SmallMonster('Goblin', 50, 100, 10, 1.1, 100))  # name, hp, xp, attack_power, level, gold
        self._enemyList.append(SmallMonster('Skeleton', 70, 200, 20, 1.2, 200))
        self._enemyList.append(MediumMonster('Giant spider', 150, 400, 30, 2.1, 500,
                                             weapon1))  # name, hp, xp, attack_power, level, gold, equipment: Item
        self._enemyList.append(MediumMonster('Werewolf', 250, 200, 40, 2.2, 600, shield1))
        self._enemyList.append(Monster('Vampire', 300, 200, 50, 3))

        itemList = [hpPotion1, hpPotion2, energyPotion1, energyPotion2, weapon2, shield2]
        for i in itemList:
            self._shop.addItem(i)

    def refreshEnemy(self):
        """
            This function refreshes the enemyList, it is called every time after the battle.

            Args:
                none.

            Returns:
                none.
        """
        self._enemyList = []
        weapon1 = Weapon('Dagger', 20, 10, 80, 15)
        shield1 = Shield('Wooden Shield', 10, 100, 5)
        self._enemyList.append(SmallMonster('Goblin', 50, 100, 10, 1.1, 100))  # name, hp, xp, attack_power, level, gold
        self._enemyList.append(SmallMonster('Skeleton', 70, 200, 20, 1.2, 200))
        self._enemyList.append(MediumMonster('Giant spider', 150, 400, 30, 2.1, 500,
                                             weapon1))  # name, hp, xp, attack_power, level, gold, equipment: Item
        self._enemyList.append(MediumMonster('Werewolf', 250, 200, 40, 2.2, 600, shield1))
        self._enemyList.append(Monster('Vampire', 300, 200, 50, 3))


    def initialize(self):
        """
            This function initializes the game, generating adventurer, monsters, shop, and items.

            Args:
                none.

            Returns:
                none.
        """
        self.printIntro()
        self.generatePlayer()
        self.generateEnemiesItems()


    def checkWinLose(self):
        """
            This function checks the current status of the game.

            Args:
                none.

            Returns:
                int: represent different status of the game.
        """
        # There are 5 fields in the game in total,
        # if the length pf unlocked list exceeds 5, that's a sign of victory
        if len(self._adventurer.getUnlocked()) == 6:
            return 1  # unlock all the list, win
        elif self._quit == True:
            return 2  # quit, lose
        elif self._adventurer.getStatus() == False:
            return 3  # adventurer die, lose
        else:
            return 4

    def showOperation(self):
        """
            This function shows the operations the adventurer can make in the main menu.

            Args:
                none.

            Returns:
                none.
        """
        print('----------------MENU----------------')
        print("1. Go to the battle field.")
        print("2. Recover your HP or energy.")
        print("3. Go to the shop.")
        print("4. Show my backpack.")
        print("5. Show my status.")
        print("6. Exit the game.")

    def exit(self):
        """
            This function allows the adventurer to quit the game.

            Args:
                none.

            Returns:
                none.
        """
        self._quit = True

    def shop(self):
        """
            This function makes the adventurer enter the shop,
            sell or buy items in the shop.

            Args:
                none.

            Returns:
                Function: getMain() or shop().
        """
        print("-------------------------------------------------------------------------")
        print("Hello adventurer! Welcome to the Wonder Shop, do you want to sell or buy?")
        print("1. I want to sell something.")
        print("2. I want to buy something.")
        print("3. Exit.")
        chosen = input("Please enter your option:")
        if chosen == str(1):
            self._adventurer.sellItem()
        elif chosen == str(2):
            self._shop.display()
            choice = input("Please enter the index of item you want, if you want to exit, enter others:")
            try:
                choice = int(choice)
                if choice in range(0, self._shop.getLen()):
                    self._adventurer.buy(self._shop.getItem(choice))
                else:
                    return self.getMain()
            except ValueError:
                return self.getMain()
        elif chosen == str(3):
            return self.getMain()
        else:
            print("Invalid input, please try again.")
            return self.shop()


    def getMain(self):
        """
            This function leads to the main menu.

            Args:
                none.

            Returns:
                none.
        """
        print("Welcome to the main menu! Here you can choose one of the options below:")
        self.showOperation()
        print("--------------------------------------")
        operation = input("Which option would you like to choose:")
        print("")
        if len(self._adventurer.getUnlocked()) == 6:
            return
        elif operation == str(1):
            print("Battle fields you have unlocked:")
            print(self._adventurer.getUnlocked())
            print("")
            invalidInput = True
            while invalidInput:
                stageSelected = input("Please enter the level you want to challenge:")
                print("")
                if stageSelected in self._adventurer.getUnlocked():
                    invalidInput = False
                    self.battle(str(stageSelected))
                    if self._adventurer.getStatus():
                        return

        elif operation == str(2):
            self._adventurer.usePotion()
            return
        elif operation == str(3):
            self.shop()
            return
        elif operation == str(4):
            self._adventurer.displayBackpack()
            return
        elif operation == str(5):
            self._adventurer.display()
            return
        elif operation == str(6):
            self.exit()
        else:
            print('Invalid input, please try again.')

