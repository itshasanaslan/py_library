class Stone:
    def __init__(self, belongs_to, current_location):
        self.belongs_to = belongs_to
        self.available_locations = []
        self.current_location = current_location
        self.moved_before = False

    def move(self,game, coords): # not board, game.
        if coords in self.available_locations:
            x, y = self.current_location
            eaten = False
             # add the eaten stone to the eaten (if there is a stone)
            if game.board[coords[0]][coords[1]].belongs_to != "Board":
                self.belongs_to.eaten.append(game.board[coords[0]][coords[1]])
                eaten = game.board[coords[0]][coords[1]]
                if game.board[coords[0]][coords[1]].name == "King":
                    game.over = True
                    game.winner = self.belongs_to
                    
            # change the location
            game.board[coords[0]][coords[1]] = game.board[x][y]
            # empty previous location
            game.board[x][y] = Empty((x, y))
            # update current location.
            self.current_location = (coords)
            if not self.moved_before:
                self.moved_before = True
            
            return True, eaten  # if can't move return False. To avoid unpack error, return two values at bottom too.
        return False, False    


class Pawn(Stone):
    def __init__(self, belongs_to, current_location):
        Stone.__init__(self,belongs_to, current_location)
        self.name = "Pawn"
        self.tag = "P"
     

    
    def calculate_available(self,board):
        self.available_locations.clear()
        # unpack the location
        location_row, location_col = self.current_location
        index = 1 if self.belongs_to.board_position == "top" else -1

        # check if the forward target empty
        if board[location_row + index][location_col].name == "Empty":
            self.available_locations.append((location_row + index, location_col))

            if not self.moved_before:
                if index == 1:
                    self.available_locations.append((location_row + index + 1, location_col))
                else:
                    self.available_locations.append((location_row + index - 1, location_col))
    

        if self.belongs_to.board_position == "top":
            # to the left of the table
            if location_col !=0 and self.check_target(board[location_row + 1][location_col - 1]):
                self.available_locations.append((location_row + 1, location_col - 1))
             # to the right of the table
            if location_col != 7 and self.check_target(board[location_row + 1][location_col + 1]):
                self.available_locations.append((location_row + 1, location_col + 1))

        elif self.belongs_to.board_position == "bottom":
            if location_col !=0 and self.check_target(board[location_row - 1][location_col - 1]):
                self.available_locations.append((location_row - 1, location_col - 1))

            if location_col != 7 and self.check_target(board[location_row -  1][location_col + 1]):
                self.available_locations.append((location_row - 1, location_col + 1))
                   
        self.available_locations.sort()

    def check_target(self,target): # to move cross, check if stone
        return target.belongs_to != "Board" and target.belongs_to != self.belongs_to

class Bishop(Stone):
    def __init__(self, belongs_to, current_location):
        Stone.__init__(self,belongs_to, current_location)
        self.name = "Bishop"
        self.tag = "B"
        

    def calculate_available(self, board):
        self.available_locations.clear()
        r, c = self.current_location # row, col unpacking
        locations = []
        # left top right bottom
        for i in range(8):
            try:
                if board[r + i][c + i].belongs_to == self.belongs_to and not (r + i == r and c + i == c):
                    break
                locations.append((r + i, c + i))
                if board[r + i][c + i].belongs_to != "Board" and not (r + i == r and c + i == c):
                    break
            except:
                pass
        # right top left bottom
        for i in range(8):
            try:
                if board[r + i][c - i].belongs_to == self.belongs_to and not (r + i == r and c - i == c):
                    break
                locations.append((r + i, c - i))
                if board[r + i][c - i].belongs_to != "Board" and not (r + i == r and c - i == c):
                    break
            except:
                pass
        # left bottom right top
        for i in range(8):
            try:
                if board[r - i][c + i].belongs_to == self.belongs_to and not (r - i == r and c + i == c):
                    break
                locations.append((r - i, c + i))
                if board[r - i][c + i].belongs_to != "Board" and not (r - i == r and c + i == c):
                    break
            except:
                pass
        # right bottom left top
        for i in range(8):
            try:
                if board[r - i][c - i].belongs_to == self.belongs_to and not (r - i == r and c - i == c):
                    break
                locations.append((r - i, c - i))
                if board[r - i][c - i].belongs_to != "Board" and not (r - i == r and c - i == c):
                    break
            except:
                pass

        for item in locations:
            if item[0] >= 0 and item[1] >= 1 and not (item[0] == r and item[1] == c):
                self.available_locations.append(item)
        self.available_locations.sort()

class Knight(Stone):
    def __init__(self, belongs_to, current_location):
        Stone.__init__(self,belongs_to, current_location)
        self.name = "Knight"
        self.tag = "H" # horse


    def calculate_available(self, board):
        self.available_locations.clear()
        row, col = self.current_location
        locations = [(row + 1, col - 2), (row + 2, col - 1), (row + 2 , col + 1), (row + 1, col + 2), (row - 1, col + 2), (row - 2, col + 1), (row - 2, col - 1), (row - 1, col - 2)]

        for location in locations:
            x, y = location
            try:
                if board[x][y].belongs_to != self.belongs_to:
                    self.available_locations.append(location)
            except:
                pass
        self.available_locations.sort()
class Rook(Stone):
    def __init__(self, belongs_to, current_location):
        Stone.__init__(self,belongs_to, current_location)
        self.name = "Rook" # kale
        self.tag = "R"
        
    
    def calculate_available(self, board):
        self.available_locations.clear()
        row, col = self.current_location
        locations = []
        r_up, r_down = False,False
        c_r, c_l = False,False

        for i in range(8):
            try:
                if not c_l:
                    if board[row][col - i].belongs_to != self.belongs_to:
                        if board[row][col - i].belongs_to != "Board":
                            c_l = True
                        locations.append((row, col - i))
                    if board[row][col - i].belongs_to == self.belongs_to and not (col - i == col):
                        c_l = True
            except:
                pass
            try:
                if not c_r:
                    if board[row][col + i].belongs_to != self.belongs_to:
                        if board[row][col + i].belongs_to != "Board":
                            c_r = True
                        locations.append((row, col + i))
                    if board[row][col + i].belongs_to == self.belongs_to and not (col + i == col):
                        c_r = True
            except:
                pass
            try:
                if not r_down:
                    if board[row + i][col].belongs_to != self.belongs_to:
                        if board[row + i][col].belongs_to != "Board":
                            r_down = True
                        locations.append((row + i, col))
                    if board[row + i][col].belongs_to == self.belongs_to and not (row + i == row):
                        r_down = True
            except:
                pass
            try:
                if not r_up:
                    if board[row - i][col].belongs_to != self.belongs_to:
                        if board[row - i][col].belongs_to != "Board":
                            r_up = True
                        locations.append((row - i, col))
                    if board[row - i][col].belongs_to == self.belongs_to and not (row - i == row):
                        r_up = True
            except:
                pass

        for item in locations:
            if item[0] >=0 and item[1] >= 0 and not (item[0] == self.current_location[0] and item[1] == self.current_location[1]): 
              self.available_locations.append(item)  
        self.available_locations.sort()

class Queen(Stone):
    def __init__(self, belongs_to, current_location):
        Stone.__init__(self,belongs_to, current_location)
        self.name = "Queen"
        self.tag = "Q"
        


    def calculate_available(self, board):
        self.available_locations.clear()
        row, col = self.current_location
        locations = []
        r_up, r_down = False,False
        c_r, c_l = False,False
        # rook
        for i in range(8):
            try:
                if not c_l:
                    if board[row][col - i].belongs_to != self.belongs_to:
                        if board[row][col - i].belongs_to != "Board":
                            c_l = True
                        locations.append((row, col - i))
                    if board[row][col - i].belongs_to == self.belongs_to and not (col - i == col):
                        c_l = True
            except:
                pass
            try:
                if not c_r:
                    if board[row][col + i].belongs_to != self.belongs_to:
                        if board[row][col + i].belongs_to != "Board":
                            c_r = True
                        locations.append((row, col + i))
                    if board[row][col + i].belongs_to == self.belongs_to and not (col + i == col):
                        c_r = True
            except:
                pass
            try:
                if not r_down:
                    if board[row + i][col].belongs_to != self.belongs_to:
                        if board[row + i][col].belongs_to != "Board":
                            r_down = True
                        locations.append((row + i, col))
                    if board[row + i][col].belongs_to == self.belongs_to and not (row + i == row):
                        r_down = True
            except:
                pass
            try:
                if not r_up:
                    if board[row - i][col].belongs_to != self.belongs_to:
                        if board[row - i][col].belongs_to != "Board":
                            r_up = True
                        locations.append((row - i, col))
                    if board[row - i][col].belongs_to == self.belongs_to and not (row - i == row):
                        r_up = True
            except:
                pass

        for item in locations:
            if item[0] >=0 and item[1] >= 0 and not (item[0] == self.current_location[0] and item[1] == self.current_location[1]): 
              self.available_locations.append(item)  
        
        # bishop
        r, c = self.current_location # row, col unpacking
        locations = []
        # left top right bottom
        for i in range(8):
            try:
                if board[r + i][c + i].belongs_to == self.belongs_to and not (r + i == r and c + i == c):
                    break
                locations.append((r + i, c + i))
                if board[r + i][c + i].belongs_to != "Board" and not (r + i == r and c + i == c):
                    break
            except:
                pass
        # right top left bottom
        for i in range(8):
            try:
                if board[r + i][c - i].belongs_to == self.belongs_to and not (r + i == r and c - i == c):
                    break
                locations.append((r + i, c - i))
                if board[r + i][c - i].belongs_to != "Board" and not (r + i == r and c - i == c):
                    break
            except:
                pass
        # left bottom right top
        for i in range(8):
            try:
                if board[r - i][c + i].belongs_to == self.belongs_to and not (r - i == r and c + i == c):
                    break
                locations.append((r - i, c + i))
                if board[r - i][c + i].belongs_to != "Board" and not (r - i == r and c + i == c):
                    break
            except:
                pass
        # right bottom left top
        for i in range(8):
            try:
                if board[r - i][c - i].belongs_to == self.belongs_to and not (r - i == r and c - i == c):
                    break
                locations.append((r - i, c - i))
                if board[r - i][c - i].belongs_to != "Board" and not (r - i == r and c - i == c):
                    break
            except:
                pass

        for item in locations:
            if item[0] >= 0 and item[1] >= 1 and not (item[0] == r and item[1] == c):
                self.available_locations.append(item)


        self.available_locations.sort()



        
class King(Stone):
    def __init__(self, belongs_to, current_location):
        Stone.__init__(self,belongs_to, current_location)
        self.name = "King"
        self.tag = "K"
        

    def calculate_available(self, board):
        self.available_locations.clear()
        row, col = self.current_location
        locations = [(row, col - 1),(row, col + 1),(row - 1, col),(row + 1,col),
        (row - 1, col - 1),(row - 1, col + 1),(row + 1, col - 1),(row + 1, col + 1)]

        for location in locations:
            x,y = location
            if x > 7 or y > 7:
                continue
            if board[x][y].belongs_to != self.belongs_to:
                self.available_locations.append(location)
            
            self.available_locations.sort()


class Empty:
    def __init__(self, current_location):
        self.tag = "■"
        self.name = "Empty"
        self.current_location = current_location
        self.belongs_to = "Board"