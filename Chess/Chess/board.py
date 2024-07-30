from stones import *

class Board:
    def __init__(self):
        self.board = []
        self.location_to_chess = {}
        self.rounds = 1
        self.over = False
        self.winner = None
        # this is just a template
        self.records_dict = {"Turn 0":[
            {"Stone":"StoneObject",
            "From": (2,2),
            "To": (3,2),
            "Eaten": False # or Eaten object.
            }
            ]} # which from where to where. Eaten who.
        # board starts with white square.

    def initialize_board(self,player1,player2):
        # initialize board first, to change them by using their index
        for i in range(8):
            temp = []
            for j in range(8):
                temp.append(Empty((i, j)))
            self.board.append(temp)


        # initialize stones except pawns
        second_player_done = False # to the top, initialize second player.
        
        for i in range(0,8,7):
            if second_player_done:
                player = player1
                index = 6
            else:
                player = player2
                index = 1 # index 1 and index 6 for pawns.
            for j in range(8):
                self.board[index][j] = Pawn(player, (index, j))

            self.board[i][0] = Rook(player, (i, 0))
            self.board[i][1] = Knight(player, (i, 1))
            self.board[i][2] = Bishop(player, (i, 2))
            self.board[i][3] = Queen(player, (i, 3))
            self.board[i][4] = King(player, (i, 4))
            self.board[i][5] = Bishop(player, (i, 5))
            self.board[i][6] = Knight(player, (i, 6))
            self.board[i][7] = Rook(player, (i, 7))
            second_player_done = True
      
        letters = "ABCDEFGH"
        x,y = 0, -1
        for num in range(8, 0, - 1):
            for letter in range(8):
                y += 1
                key = letters[letter] + str(num)
                self.location_to_chess[key] = (x, y)
                self.location_to_chess[(x, y)] = key
            x += 1
            y = -1
        
       

        
    def print_board(self, testing = False): # in test cases, to control indexes, do not print row numbers from higher to low.
        cols = "   A  B  C  D  E  F  G  H" if not testing else "   0  1  2  3  4  5  6  7"
        print(cols)
        count = 8 if not testing else 0
        for row in self.board:
            print(count, end="  ")
            if testing:
                count +=1
            else:
                count -= 1
            for col in row:
                print(col.tag, end= "  ") # print items instead.
            print()
    
    def update_records(self, StoneObject, from_pos, to_pos, eaten = False):
        self.records_dict[f"Turn {str(self.rounds)}"] = [
            {"Stone":StoneObject,
            "From": from_pos,
            "To": to_pos,
            "Eaten": eaten # or Eaten object.
            }]
        print("Record updated.")
        self.rounds += 1

    def check_mate(self):
        if self.over:
            input(f"Game over. Winner: {self.winner.name}")