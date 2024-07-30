import platform
from cards import Cards
from player import Player
from game import Game
from os import system
from colorama import Fore,Style,init

init()
red = Fore.RED+Style.BRIGHT
blue = Fore.BLUE + Style.BRIGHT
green = Fore.GREEN + Style.BRIGHT
default = Style.RESET_ALL
system('title Poker Game by aslan')

operation_system = ""
if platform.system() == 'Linux':
    operation_system = 'linux'
    clear_screen = lambda: system('clear')
elif platform.system() == 'windows' or platform.system() == 'Windows' or 'windows' in platform.system():
    operation_system = 'windows'
    clear_screen = lambda: system(('cls'))
   

clear_screen()


Game.welcome()
Cards.first_time_create_desk()

#This commented block is to check player special_hands quickly. In case any bug, can detect it quickly.
"""
Cards.create_desk()
Game.distribute_everyone()
Game.print_players() #####
"""

xx=False
'''
while xx==False:
    Game.new_round()
    Cards.distribute_to_table()
    Cards.distribute_to_table()
    xx = Game.player1.is_one_pair(Cards)


value = 0
itemlist = Game.player1.hand_with_table

for item in itemlist:
    try:
        value+= Cards.full_cards_values.get(item)
    except Exception as f:
        print(red,"\n\nError when calculating: ",f)
        break
print("\n")

if value == Game.player1.special_value:
    print(green,"Value calculation is correct")
else:
    print(red,"value calculation mismatch!")

'''
while len(Game.player_list)>1:
    Game.new_round()
    Game.run_a_round(clear_screen)
    print("This round is finished")
    Game.print_players()
    print(f"{green}Round {Game.rounds} is finished",default)

  



