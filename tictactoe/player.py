import math
import random

class Player:
    def __init__(self,letter):
        #lrtter is "x" or "O"
        self.letter = letter
    #to get moves
    def get_moves(self,game):
        pass

class RandomComputerPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)
    
    def get_moves(self, game):
        square=random.choice(game.available_moves())
        return square

class HumanPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)

    def get_moves(self, game):
        valid_square=False
        val=None
        while not valid_square:
            square=input(self.letter + "\'s turn. Input move(0-9):")
            try:
                val=int(square)
                if val not in game.available_moves():
                    raise ValueError
                valid_square =True
            except ValueError:
                print('Invalid square.Try Again')
        return val