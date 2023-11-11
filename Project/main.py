from Game import Game

if __name__ == '__main__':
    game = Game()
    game.initialize()
    while game.checkWinLose() == 4:
        # There is no lose or win, and the player doesn't exit the game
        game.getMain()
    if game.checkWinLose() == 1:
        print("***************************")
        print('Congrats! You won the game!')
        print("***************************")
    elif game.checkWinLose() == 2:
        print('You have exited successfully')
    elif game.checkWinLose() == 3:
        print('You just died, game over!')
