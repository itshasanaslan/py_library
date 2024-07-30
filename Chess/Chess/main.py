import os
from board import *
from datetime import datetime
from stones import *


clear = lambda:os.system('cls')
clear()
print(datetime.now().strftime("%X"),"\n\n")

class Player:
    def __init__(self, name, board_position):
        self.name = name
        self.board_position = board_position
        self.eaten = [] #

game = Board()

player1 = Player("player1","bottom")
player2 = Player("player2","top")
game.initialize_board(player1, player2)


def get_coordinate(stone):
    global game
    
    stone_get = game.location_to_chess.get(stone)
    if stone_get != None:
        return stone_get
    else:
        print("Invalid coordinate:",stone)
        return False

def check_belongs_to(stone, player):
    return stone.belongs_to == player
    
    



def show(current_player):
    global game,clear
    while True:
        clear()
        game.print_board()
        print("Type 'ok' to leave.")
        stone = input("Enter a stone location to see available moves: ").upper()
        if stone.lower()== 'ok':
            break
        stone_coor = get_coordinate(stone)
        print(stone_coor)
        if not stone_coor:
            print("You don't have a stone at:",stone)
            input("Press enter.")
            continue
        x, y = stone_coor
        game.board[x][y].calculate_available(game.board)
        if len(game.board[x][y].available_locations) == 0 and game.board[x][y].belongs_to == current_player:
            print("You can't move your",game.board[x][y].name +".")
        elif len(game.board[x][y].available_locations) == 0:
            print(f"{game.board[x][y].name} at {stone_coor} is not yours. ")
        else:
            print(f"Available locations for {game.board[x][y].name} at {stone} ")
            for i in game.board[x][y].available_locations:
                print(f"{game.location_to_chess.get((x, y))}",end=', ')
            print("_________________")
        input()
        break
commands_str = """
                    Type location of your stone and target stone.
                    Example: C2 C3
                    Type 'show' to see available locations.
                    Example: show
                    """

index = 0
while True:
    players = [player1, player2]
    check = game.check_mate()
    if check:
        print("Game over")
        print(check.name,"has won.")
        input()
    else:
        print("go")
    clear()
    game.print_board()
    current_player = players[index]
    print(f"Turn: {current_player.name}")
   
    com = input(">>").upper().split()
    if com[0] == "SHOW":
        show(current_player)
        continue

    elif com[0] == "RECORD":
        for item,key in game.records_dict.items():
            print(item, key)
        input()
        continue

    elif com[0] == "TEST":
        print("King teleported besides you.")
        game.board[0][5] = game.board[7][4]
        input("Eli")

    elif len(com) <= 1:
        print(commands_str)
        input("Press enter")
        continue
   
    else:
        current_stone = get_coordinate(com[0]) # (x,y)
        x, y = current_stone
        if not current_stone:
            input("Press enter.")
            continue
        target_stone = get_coordinate(com[1]) # (x, y)
        if not target_stone:
            input("Press enter")
            continue
        # check belongs to.
        if not check_belongs_to(game.board[x][y], current_player):
            input("Not available for you.")
            continue

        
        game.board[current_stone[0]][current_stone[1]].calculate_available(game.board)
        print(current_stone)
        print(target_stone)
        # don't forget to check if stone belongs to him.
        if game.board[current_stone[0]][current_stone[1]].belongs_to == current_player:
            move_success, eaten_any = game.board[current_stone[0]][current_stone[1]].move(game, target_stone)
            if move_success:
                game.update_records(game.board[target_stone[0]][target_stone[1]], current_stone, target_stone, eaten_any)
            else:
                input("You can't move that")
                continue
        else:
            print(f"{game.board[current_stone[0]][current_stone[1]].name} at {com[0]} does not belong to you.")
        input()
        
    index += 1
    if index == 2:
        index = 0



"""
test_p1_r = 4
test_p1_c = 4

#game.board[test_p1_r][test_p1_c] = Queen(player2,(test_p1_r,test_p1_c))

game.print_board(True)

game.board[test_p1_r][test_p1_c].calculate_available(game.board)
print(game.board[test_p1_r][test_p1_c].available_locations)
print(game.board[test_p1_r][test_p1_c].belongs_to.name)
"""
