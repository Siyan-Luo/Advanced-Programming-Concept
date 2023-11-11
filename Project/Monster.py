
class Monster:
    """This is the Monster class, it's the parent class of MediumMonster and SmallMonster.

               Attributes:
                   name (str): The name of the monster.
                   hp (int): The hp value of the monster.
                   xp (int): The carried experience value of the monster,
                             it will be obtained by the adventurer once the monster loses.
                   attack_power (int): The attack power of the monster,
                                       it's the hp loss of the adventurer when getting attacked by the monster.
                   level (int): The level of the monster, it corresponds to the battle-field/stage.
    """
    def __init__(self, name, hp, xp, attack_power, level):
        """Constructor method for Monster.

                  Args:
                      name (str): The name of the monster.
                      hp (int): The hp value of the monster.
                      xp (int): The carried experience value of the monster,
                                it will be obtained by the adventurer once the monster loses.
                      attack_power (int): The attack power of the monster,
                                          it's the hp loss of the adventurer when getting attacked by the monster.
                      level (int): The level of the monster, it corresponds to the battle-field/stage.
        """
        self._name = name
        self._hp = hp
        self._xp = xp
        self._alive = True
        self._attack_power = attack_power
        self._level = level


    def getLevel(self):
        """
            This function gets the level of the monster.

            Args:
                none.

            Returns:
                int: the level of the monster.
        """
        return self._level


    def getAttackPower(self):
        """
            This function gets the attack power by the monster.

            Args:
                none.

            Returns:
                int: the attack power of the monster.
        """
        return self._attack_power

    def attacked(self, num):
        """
            This function makes the monster be attacked.

            Args:
                num(int)： The attacked power.

            Returns:
                none.
        """
        self._hp -= num
        print("You attacked " + self._name)
        print(self._name + " has lost " + str(num) + " hp.")
        if self._hp <= 0:
            self._alive = False
            print(self._name + " lost all hp and died.")
        else:
            print(self._name + " remains  " + str(self._hp) + " hp.")
        print("-----------------------------------")

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

    def getStatus(self):
        """
            This function gets the living status of the monster.

            Args:
                none.

            Returns:
                Boolean: The living status.
        """
        return self._alive


    def getXP(self):
        """
            This function gets the carried experience points by the monster.

            Args:
                none.

            Returns:
                int: carried experience points.
        """
        return self._xp


    def getHp(self):
        """
            This function gets the carried HP points by the monster.

            Args:
                none.

            Returns:
                int: carried HP points.
        """
        return self._hp


