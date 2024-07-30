from player import Player
from cards import Cards
from time import sleep
from colorama import Fore,Style,init
import random


init()
red = Fore.RED+Style.BRIGHT
blue = Fore.BLUE + Style.BRIGHT
green = Fore.GREEN + Style.BRIGHT
yellow = Fore.YELLOW +Style.BRIGHT
default = Style.RESET_ALL
decorator_1 = f"{red}\n----------------------------------------------------------{default}"
decorator_2 = f"{red}############################################################{default}" #evaluate and run a round
decorator_3 = f"{yellow}\n----------------------------------------------------------{default}" #seperate player's hands when displaying finally
decorator_4 = f"{red}################################################################################################{default}"
#manages the game and the entire players.
class Game:
    #store_values_for_each_round = {}
    rounds = 0
    player_list = [] #store Player class objects

    first_time_play = True #will use only once.
    blind_bet = False # is an option at the beginning
    give_bots_thinking_time = True

    rounds = 0
    player1= None #You
    

    current_bet = 50 #standart bet value
    bet_increase_check_index = len(player_list) # if a player increases the bet, reset the index and loop all players again(except the one increased the bet.)
    whole_money = 0 #at the table
    paid_index = 0 #check player's paid index. If someone pays 50 and another player increases it to 75, the player who paid 50, should only paid 25.
    
    random_user_names = ["Fynn","Leo",'Marshall',"Charlie","Joseph","Amy","David",'Julia',"John","Sarah",'Sophia','Mia','Rick','Morty']
    hard_bots = False
    winner_player = None #experimental
    

    @classmethod
    def welcome(cls):
        name = input("Welcome. Enter your name: ").title()
        
        if name == "" or name==" ":
            print("I will call you as 'YOU'")
            name = "YOU"
        blind_input = input("\nDo you want to enable blind bets? (You won't see the first three cards at the first round but you can bet)\nType 'y'/'n'\n>>>>").lower().split()
        
        if blind_input[0] == 'y':
            Game.blind_bet = True
            print("Blind bet enabled!")
        
        try:
            thinking_for_bots = input("\nDo you want the players to think?\n'y'/'n'\n>>>").lower().split()
            if thinking_for_bots[0]=='n':
                Game.give_bots_thinking_time = False
                print(blue,'#System:Thinking effect is disabled!',default)
        except:
            Game.give_bots_thinking_time = True
            print(blue,'#System:Thinking effect is enabled!',default)
    

        Game.player1 = Player(name)
        Game.player_list.append(Game.player1)
    
        if name in Game.random_user_names:
            Game.random_user_names.remove(name)

        while True:
            try:
                number_of_players = int(input("How many players you want to play with: "))
                #number_of_players = 4
                if not 1<number_of_players<8:
                    print(red,"(Error)# You need to enter a value between 1 and 7!",default)
                
                #Generate random players and add them to the list.
                for person in range(1,number_of_players+1):

                    random_username = random.choice(Game.random_user_names)
                    Game.random_user_names.remove(random_username) #So they won't pick the same name.
                   
                    Game.player_list.append(Player(random_username))
                Game.bet_increase_check_index = len(Game.player_list)
                break
            except Exception as f:
                print(red,"(Error)# You have to write a number between 1 and 7! ",default)
                print("\n\n",f)
                break
        
        

    @classmethod
    def print_players(cls):
        for person in Game.player_list:
            person.print_cards()
            print("*************************************************")
  
    @classmethod
    def distribute_everyone(cls):
        for player in Game.player_list:
            player.hands += Cards.distribute_cards(player)
            player.calculate_hand_value(Cards)
        
    
    @classmethod
    def new_round(cls):
        Game.rounds += 1
        Game.current_bet = 50 
        Game.whole_money = 0
        Game.bet_increase_check_index = len(Game.player_list)
        if not Game.first_time_play:
            #in each new round, the person at the right, starts the round.
            Game.player_list.append(Game.player_list[0]) 
            Game.player_list.remove(Game.player_list[0])

        for player in Game.player_list:
            for item in player.hand_dictionary:
                player.hand_dictionary.update({item:False})
                player.withdraw = False
                player.rest = False
                player.possess_any_special_hand = 10
            player.hands.clear()
        print(decorator_1)
        print(red,"#Game: Resetting everything and creating new round",Game.rounds,default)

        Cards.create_desk()
        Game.distribute_everyone()
        Cards.distribute_to_table()
        Game.first_time_play = False

    @classmethod
    def evaluate_players_card(cls,Cards):
        print(decorator_2)
        print(yellow,"# GAME: CHECKING PLAYER'S CARDS.\n",default)
        
        store_special_hands = []

        for player in Game.player_list:
            if player.withdraw:
                continue
            if Game.give_bots_thinking_time:
                sleep(1.3)
            #print(player.name,*player.hand_with_table)
            check = player.is_royal_flush(Cards)
            if not check: check = player.is_straight_flush(Cards)    
            if not check : check = player.is_four_of_a_kind(Cards)
            if not check:check = player.is_full_house(Cards)
            if not check: check = player.is_flush(Cards)
            if not check:check = player.is_straight(Cards)
            if not check: check = player.is_three_of_a_kind(Cards)
            if not check: check = player.is_two_pair(Cards)
            if not check: check = player.is_one_pair(Cards)
            if not check: 
                player.hand_with_table = Cards.table+player.hands
                player.hand_with_table = Player.order_cards(Cards,player.hand_with_table)
                player.hand_with_table = player.hand_with_table[0:5]
                for card in player.hand_with_table:
                    value = Cards.full_cards_values.get(card)
                    player.special_value += value
            print(*player.hand_with_table)
            print("Hand no:",player.possess_any_special_hand,'Special set value:',player.special_value,decorator_3)
            #print(player.name," control finished!\n")
            store_special_hands.append(player.possess_any_special_hand) #bunu for loopundaki continue oncesine alabilmeyi düşün. Başlarken thinki kapatınca hata var.
        #print("Special hands list:",*store_special_hands)        
        
        most_valuable_hand = max(store_special_hands)
        store_special_values = [] #player's special values.

        is_there_other_most_valuable_hand = store_special_hands.count(most_valuable_hand) #get the number of players that share most valuable hand. Royal, straight etc. but not their individual values.
        if is_there_other_most_valuable_hand==1:
            #if there is 1, the winner is obvious
            for player in Game.player_list:
                if player.possess_any_special_hand==most_valuable_hand:
                    print(f'{green}##Game: {player.name} wins with {Cards.hand_values_and_names.get(player.possess_any_special_hand)}!',default)
                    player.credit += Game.whole_money
                    Game.winner_player = player
                    print(f"{green}{player.name}'s set:{yellow}",*player.hand_with_table,default)
        else:
            print(red,"#Game: More than one player have same valuable hand!",default)
            print(yellow,"# Game: Press enter to see the winner.",default)
            input()
            for player in Game.player_list:
                if player.possess_any_special_hand==most_valuable_hand:
                    store_special_values.append(player.special_value)
            max_special_value = max(store_special_values)
            print("Max value is:",max_special_value,'\n')
            for player in Game.player_list:
                if player.possess_any_special_hand==most_valuable_hand:
                    if player.special_value == max_special_value:
                        print(f'{green}##Game: {player.name} wins with {Cards.hand_values_and_names.get(player.possess_any_special_hand)}!',default)
                        #print(player.name,"wins with",Cards.hand_values_and_names.get(player.possess_any_special_hand)+'!')
                        Game.winner_player = player
                        player.credit += Game.whole_money
                        print(f"{green}{player.name}'s set:{yellow}",*player.hand_with_table,default)

    @classmethod
    def play(cls,Cards,clear_screen):
        while Game.bet_increase_check_index>0:
            for player in Game.player_list:
                if player.withdraw or player.rest:
                    Game.bet_increase_check_index -=1
                    print(f"{yellow}# Game: Skipping {player.name}{default}")
                    continue
                #input(f"index: {Game.bet_increase_check_index}")
                if player.withdraw:
                    print(player.name,'is draw off,skipping')
                    #continue
                #input(f"Each player Game index: {Game.bet_increase_check_index}")
                if Game.bet_increase_check_index==0:
                    print(green,"##Game: Iteration for a tour is completed.",default)
                    break
                print('\n')
                if player == Game.player1 and not Game.player1.rest:
                    #since this is player1, I dont need to use player1 at all.
                    if player.credit>=Game.current_bet:
                        while True:
                            if Game.blind_bet:
                                print("There are 3 cards on the table.")
                            else:
                                Cards.print_table()
                                print(f"{yellow}Current bet is: {Game.current_bet}{default}")
                                Game.player1.calculate_hand_value(Cards)
                                Game.player1.print_cards()
                
                            try:
                                bet_decision = input(f"Type '{yellow}help{default}' for available commands{green}\n\nCommand>>>> {default}").lower().split()
                                if bet_decision[0] == 'go' or bet_decision[0]=='ok' or bet_decision[0]==None:
                                    print(f"{yellow}# Game: You are in!",default)
                                    player.credit -= (Game.current_bet-player.paid_bet)
                                    player.paid_bet += Game.current_bet-player.paid_bet
                                    Game.whole_money += Game.current_bet-player.paid_bet
                                    Game.bet_increase_check_index -=1
                                    break
                                
                                elif bet_decision[0] == 'w':
                                    player.withdraw = True
                                    Game.bet_increase_check_index -=1
                                    break
                                
                                elif bet_decision[0]=='i':
                                    try:
                                        amount = int(bet_decision[1])
                                        if amount<Game.current_bet:
                                            clear_screen()
                                            print(f"{red}#Error: You need to enter a bigger value than the current bet({Game.current_bet}){default}")
                                        elif amount>player.credit:
                                            clear_screen()
                                            print(f"{red}#Error: You cannot bet with credits that is much than yours!{default}")
                                        else:
                                            clear_screen()
                                            print(f"{yellow}You increased the bet to {amount}",default)
                                            Game.bet_increase_check_index =  len(Game.player_list)-1
                                            #print(f"Game index changed to: {Game.bet_increase_check_index} ")
                                            Game.current_bet = amount
                                            player.credit-=amount
                                            if player.credit==0:
                                                player.rest = True
                                                print(f"{yellow}Rest from {player.name}!{default}")
                                            break
                                    except:
                                        clear_screen()
                                        print(f"{red}#Error: Amount must be an integer, example: i 55{default}")
                                elif bet_decision[0]=='help':
                                    clear_screen()
                                    print(decorator_4)
                                    print(f'''
                            Available commands:
                            '{yellow}go{default}' or '{yellow}ok{default}' : continue
                            '{yellow}i amount{default}' to increase bet. For ex: '{yellow}i 60{default}'
                            '{yellow}w{default}' to withdraw.
                            '{yellow}r{default}' to rest.
                            '{yellow}blind{default}' to enable/disable blind bet.
                            '{yellow}think{default}' to enable/disable thinking time for bots.
                            {red}\n
                                      r/hasanaslan7
                                      Twitter.com/gepettolyon
                                      instagram/hasanaslan7
                                      aslanhassan98@gmail.com
                                      github/hasanaslan
                                    ''')
                                    print(decorator_4)
                                    continue
                                    #rest
                                elif bet_decision[0]=='r':
                                    print("Now index is this:",Game.bet_increase_check_index)
                                    player.rest = True
                                    Game.whole_money += player.credit
                                    Game.current_bet = player.credit
                                    player.credit = 0
                                    print(yellow,"Rest from",player.name+'!',default)
                                    Game.bet_increase_check_index = len(Game.player_list)
                                    break
                                elif bet_decision[0]=='blind':
                                    if Game.blind_bet:
                                        clear_screen()
                                        print(blue,"#System: Blind bet is disabled.",default)
                                        Game.blind_bet = False
                                    else:
                                        clear_screen()
                                        print(blue,"#System: Blind bet is enabled.",default)
                                        Game.blind_bet = True
                                elif bet_decision[0]=='think':
                                    clear_screen()
                                    if Game.give_bots_thinking_time:
                                        Game.give_bots_thinking_time = False
                                        print(blue,"#System: thinking time is disabled.",default)
                                    else:
                                        print(blue,"#System: thinking time is enabled.",default)
                                        Game.give_bots_thinking_time = True
                                    continue
                                else:
                                    clear_screen()
                                    print(red,"#Error: You need to enter a proper command!",default)
                            except Exception as wtf:
                                clear_screen()
                                print(blue,"#System->Handled exception:",wtf,default)
                                
                    else:
                        clear_screen()
                        print(red,"#Error: You don't have enough money or you withdraw.",default)    
                    
                    #bots
                if player!=Game.player1:
                    if not Game.hard_bots:
                        Game.easy_bot_decision(player)
                else:
                    if player.rest:
                        Game.bet_increase_check_index -=1 #if player.rest, we need to to this. Otherwise the loop will be unending.
                        print('rest')
                        continue
            




    @classmethod
    def easy_bot_decision(cls,player):
        #paralarını kontrol ettir.
        #birisi arttırırsa diğerleri de sadece farkı ödesin.
        while True:
            if player.credit>=Game.current_bet and not player.rest and not player.withdraw:
                number = random.randint(0,4)
                player.print_info()
                print(player.name,'is thinking. Credits:',player.credit)
                if Game.give_bots_thinking_time:
                    sleep(number+1)
            
                if number == 4:
                    while True:
                        number = random.randint(2,15)
                        number2 = random.randint(2,3)

                        money_increased =  int((Game.current_bet/number2) * number)
                        #botun parası varsa beti arttirsin.
                        if money_increased>Game.current_bet and  money_increased<player.credit:
                            Game.current_bet = money_increased
                            print(f"{yellow}# Game: {player.name} has increased the bet to {Game.current_bet}!{default}")
                            Game.bet_increase_check_index =  len(Game.player_list)-1
                            print(red,"Bot: Game index changed to:",Game.bet_increase_check_index,default)
                            input()
                            player.credit -= money_increased
                            break
                        elif money_increased>Game.current_bet and  money_increased>player.credit:
                            print(f"{player.name} is going to rest with {player.credit} credits!") 
                            Game.current_bet = player.credit
                            Game.whole_money += player.credit
                            Game.bet_increase_check_index -=1
                            player.credit = 0
                            player.rest = True
                            break
                        elif money_increased<Game.current_bet:
                            continue
                    break
                #withdraw
                if number == 3:
                    player.withdraw = True
                    print(f"{player.name} is draw off!")
                    Game.bet_increase_check_index-=1
                    break
                #player accept the round.
                else:

                    if Game.current_bet==player.credit:
                        print(f"{player.name} is accepted, and going to rest!")
                        player.rest = True
                    else:
                        print(f"{yellow}# Game: {player.name} is in!{default}")
                    player.credit -= Game.current_bet
                    Game.whole_money += Game.current_bet
                    Game.bet_increase_check_index -=1
                    break
            if not player.rest and not player.withdraw:
                print(f"{player.name}'s money:{player.credit}")
                Game.whole_money+= player.credit
                Game.bet_increase_check_index -=1
                print('Player money is smaller than bet.Rest from',player.name+'!')
                player.rest = True
                player.credit = 0
                break
            else:
                break



    @classmethod
    def hard_bot_decision(cls,player): # i dont know perhaps i can code it later.
        pass


    @classmethod
    def run_a_round(cls,clear_screen):
        '''print("Info for testing:")
        print(f"rounds: {Game.rounds}")
        print(f"Index loop: {Game.bet_increase_check_index}")
        print("number of players:",len(Game.player_list))'''
        input("Press enter to continue.")
        clear_screen()
        Game.play(Cards,clear_screen)
        Game.bet_increase_check_index = len(Game.player_list)
        print(yellow,"# Game: Going to distribute 4. card on the table!",default)
        input("enter..")
        clear_screen()
        print(decorator_2)
        Cards.distribute_to_table()
        print(yellow,'\n# Game: 4. card is distributed to the table.',default)
        Game.play(Cards,clear_screen)
        Game.bet_increase_check_index = len(Game.player_list) 
        print(yellow,"# Game: Going to distribute 5. card on the table!",default)
        input("enter...")
        clear_screen()
        print(decorator_2)
        Cards.distribute_to_table()
        print(yellow,'\n# Game: 5. card is distributed to the table.',default)
        Game.play(Cards,clear_screen)
        Game.bet_increase_check_index = len(Game.player_list)
        print(f"{yellow}# Game: Going to compare cards.",default)
        input("enter...")
        clear_screen()
        print(decorator_1)
        Game.evaluate_players_card(Cards)
        print(decorator_1)
        for player in Game.player_list:
             if player.credit <50:
                    print(f"{red}{player.name} have no credits!",default)
                    input()
                    if player == Game.player1:
                        print(red,"You lost. Game over!",default)
                        input()
                        exit()
                    else:
                        print(f"{red}{player.name} is disqualified!",default)
                        Game.player_list.remove(player)
                        if len(Game.player_list)==1 and Game.player_list[0]==Game.player1:
                            print(green,"Congratulations, you won!",default)
                            input()
                            exit()
