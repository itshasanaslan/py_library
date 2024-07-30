import random
from colorama import Fore,Style,init

init()
red = Fore.RED+Style.BRIGHT
blue = Fore.BLUE + Style.BRIGHT
green = Fore.GREEN + Style.BRIGHT
yellow = Fore.YELLOW +Style.BRIGHT
default = Style.RESET_ALL
decorator_1 = f"{red}----------------------------------------------------------{default}"
class Cards:
    deck = []
    table = []
    full_cards_values = {}
    full_cards_values_contain_names = {}
   
    card_values = {'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9,'10':10,'J':11,'Q':12,'K':13,'A':14} 
    card_values_list = ['2','3','4','5','6','7','8','9','10','J','Q','K','A']
    temp_kinds_list =  ["Heart",'Diamond','Spade','Club'] #will use it when creating a full card.

    hand_values_and_names = {
        10:'Royal Flush',
        9:'Straight Flush',
        8:'Four of a Kind',
        7:'Full House',
        6:'Flush',
        5:'Straight',
        4:'Three of a Kind',
        3:'Two Pairs',
        2:'a Pair',
        1:'a High Card'
    }



    @classmethod
    def first_time_create_desk(cls):
        #Cards.kinds_list.clear()
        #multiply four of the kinds and add them to the dictionary for later value calculation
        for a in range(4): #Heart,Diamond,Spades,Club
            for b in range(13):# each kind has 14 cards.
                standart_card = Cards.card_values_list[b]
                kind_card = Cards.temp_kinds_list[a]
                value_card = kind_card +' '+ standart_card
                calculated_value = 0
                if kind_card == 'Club':
                    calculated_value = Cards.card_values.get(standart_card)
                elif kind_card == 'Spade':
                    calculated_value = Cards.card_values.get(standart_card)+13
                elif kind_card == 'Diamond':
                    calculated_value = Cards.card_values.get(standart_card)+26
                elif kind_card == 'Heart':
                    calculated_value = Cards.card_values.get(standart_card)+39
                
                Cards.full_cards_values[value_card] = calculated_value
                    

    @classmethod
    def create_desk(cls):
        Cards.table.clear()
        Cards.deck.clear()
                
        for item in Cards.full_cards_values:
            Cards.deck.append(item)

    @classmethod
    def distribute_cards(cls,any_player):
        if not len(any_player.hands)>2:

            card1 = random.choice(Cards.deck)
            Cards.deck.remove(card1)

            card2 = random.choice(Cards.deck)
            Cards.deck.remove(card2)

            return [card1,card2]
        else:
            print("You can only hold max 2 cards at a time!")
            return ["Error!"]
    @classmethod
    def distribute_to_table(cls):
        if len(Cards.table)<3:

            for a in range(3):
                card1 = random.choice(Cards.deck)
                
                Cards.deck.remove(card1)
                Cards.table.append(card1)

        elif 3<=len(Cards.table)<5:
            card1 = random.choice(Cards.deck)
            Cards.deck.remove(card1)
            Cards.table.append(card1)
        else:
            print("##An error occured while placing cards on the table! Check me under the Cards class, distribute table function")
            print(len(Cards.table))
    
    @classmethod
    def print_table(cls):
        print(decorator_1)
        print(f"{yellow}Cards on the table: ",default,end='')
        for card in range(0,len(Cards.table)):
            print(green,Cards.table[card],end=' ')
        print()
        print(decorator_1,'\n')
        
        