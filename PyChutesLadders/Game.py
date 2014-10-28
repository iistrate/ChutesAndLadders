import Spinner
import Player
import Board

class Game(object):
    """Game loop and settings """
    def __init__(self):
        self._mbrunning = True
    def quit(self):
        self._mbrunning = False
    
    #game loop
    def run(self):
        #settings
        PLAYER_TYPES = dict(PLAYER1 = 1, ENEMY = 2)
        MENU = dict(ADD_PLAYERS = 1, QUIT = 2, SPIN = 3)
        turn = 0 
        #objects
        spinner = Spinner.Spinner()
        board = Board.Board()

        print("Welcome to Mafia Boss 2014, the goal of the game is to become the Mafia Leader")
        print("In order to do that, you need to do jobs for the current Mafia Leader and move up the Organization ladder")
        print("You do jobs by rolling a dice, depending how the jobs go you move up or down the ladder")
        print("When you get on the highest ladder; you become the Mafia Leader; but be warned there are those who want to see you fail\n")
        print(board)
        while self._mbrunning:
            if (turn == 0):
                #in case we'll need to add more players in the future
                ui = MENU['ADD_PLAYERS']
                if ui == MENU['ADD_PLAYERS']:
                    #ui = int(input("Please choose nr of players 2-4: "))
                    #if ui in (2,3,4):
                    player = Player.Player(PLAYER_TYPES['PLAYER1'])
                    cpu = Player.Player(PLAYER_TYPES['ENEMY'])

            ui = int(input("\nPress 3 to Spin or 2 to Quit: "))

            if ui == MENU['QUIT']:
                self.quit()
            elif ui == MENU['SPIN']:
                #player turn
                ispin = spinner.spin()
                print("PLAYER1 rolled: {}".format(spinner))
                player.setPosition(ispin)
                #cpu turn
                ispin = spinner.spin()
                print("CPU rolled: {}".format(spinner))
                cpu.setPosition(ispin)
                board.Move(player)
            print()
            print(board)                
            #end of turn
            turn += 1;
