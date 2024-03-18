class TicTacToe:
    def __init__(self):
        self.board=[" " for _ in range(9)]
        self.current_winner = None

    def print_board(self):
        for row in [self.board(i*3:(i+1)*3)] for i in range(3):
                    print("|"+"|".join(row)+"|")
    
    @staticmethod
    def print_board_nums():
          # 0|1|2 etc (tells us what number corresponds to what box)
          number_board =[[str(i) for i in range (j+3)] for j in range(3)]
          for row in number_board:
                print("|"+"|".join(row)+"|")

    def available_moves(self):
          moves=[]
          for (i,spot) in enumerate(self.board):
                #['x','x','o']--> [(0,x),(1,x),(2,0)]
                if spot == " ":
                      moves.append(i)   
          return moves 
    def empty_sqaures(self):
          return " " in self.board
    

    def num_empty_squares(self):
          return self.board.count(' ')
    

    def make_move(self,square,letter):
          if self.board[square]==' ':
                self.board[square]= letter
                if self.winner(square,letter):
                      self.current_winner= letter
                return True
          return False
    def winner(self,square,letter):
          
          


def play(game,x_player,o_player,print_game=True):
      if print_game:
            game.print_board_nums()
      letter='x'


      while game.empty_squares():
            if letter=='o':
                  square=o_player.get_moves(game)
            else:
                  square=x_player.get_moves(game)

            if game.make_move(square,letter):
                  if print_game:
                        print(letter+f'makemoves to square {square}')
                        game.print_board()
                        print('')

            if game.current_winner:
                  if print_game:
                        print(letter + 'wins')
                  return letter
                  
                  if letter == 'X':
                        letter = 'O'
                  else:
                        letter ='X'
      if print_game:
            print('Its a tie')

