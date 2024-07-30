from colorama import Fore,Style,init

init()
red = Fore.RED+Style.BRIGHT
blue = Fore.BLUE + Style.BRIGHT
green = Fore.GREEN + Style.BRIGHT
yellow = Fore.YELLOW +Style.BRIGHT
default = Style.RESET_ALL

class Player:
    def __init__(self, name):
        self.name = name
        self.hands = [] #contains 2 cards at each round
        self.hand_value = 0 #total value of the cards in player's hand
        self.credit = 1000
        self.paid_bet = 0 #if someone increases the bet, pay only the difference.
        self.special_value = 0  # if two player or more get the same hand, the value of the set will be calculated.
        self.hand_with_table = [] # self.hands + 5 cards on the table

        self.withdraw = False
        self.rest = False
    

        self.possess_any_special_hand = 10 # royal flush = 10, high card = 1. The loop will control every hand starting from highest poker hand. Each false return, -1
        # this list will be checked in a loop for each player.
        self.hand_dictionary = {
            'is_royal_flush': False,
            'is_straight_flush': False,
            'is_four_of_a_kind': False,
            'is_full_house': False,
            'is_flush': False,
            'is_straight': False,
            'is_three_of_a_kind': False,
            'is_two_pair': False,
            'is_one_pair': False,
            'is_high_card': False,
        }
    
      

    def print_info(self):
        print(
            f"Player Name: {self.name} | Credits: {self.credit}")

    def calculate_hand_value(self, Cards):
        self.hand_value = 0
        # Kinds
        for card in self.hands:
            self.hand_value += Cards.full_cards_values.get(card)

    def print_cards(self):
        print(f"{blue}{self.name}'s Cards: {green}{self.hands[0]} {yellow}|{green} {self.hands[1]} {yellow}| Hand value: {green}{self.hand_value} {yellow}| Credits: {green}{self.credit}{default}")

    # -----------------------------------------------------------------------------------------
    # Define Poker Hands
    def is_royal_flush(self, Cards):
        self.hand_with_table.clear()
        self.special_value = 0
        # 7cards on the table including player's cards
        combine_cards = Cards.table + self.hands
        royal_flush_set = ['10', 'A', 'J', 'K', 'Q']

        store_values_and_cards = {}  # to print cards in order
        organize_order_to_print = []
        store_indexes = []

        last_items = []  # hand set on the table.
        for item in combine_cards:
            kind, value = item.split()
            temp_index = Cards.card_values.get(value)
            if value in royal_flush_set:
                # if there is 5 proper item, it means it is royal flush
                last_items.append(item)
                # remove the current card to prevent duplication
                royal_flush_set.remove(value)
                # will use it for displaying cards in order.
                store_values_and_cards[Cards.card_values.get(value)] = item
            # check if there is a same card but more valuable one ex: Heart A is valuable than Spade A

            if temp_index in store_values_and_cards:
                compare_card1 = store_values_and_cards.get(temp_index)
                value_compare_card1 = Cards.full_cards_values.get(
                    compare_card1)

                # current card in the loop
                compare_card2 = item  # to prevent confusion
                value_compare_card2 = Cards.full_cards_values.get(item)

                if value_compare_card2 > value_compare_card1:
                    # if the new card is more valuable, replace it with the old one.
                    store_values_and_cards.update({temp_index: compare_card2})

        if len(last_items) == 5:
            for a in store_values_and_cards:  # to sort them as A K Q J 10
                organize_order_to_print.append(a)

            organize_order_to_print.sort(reverse=True)  # bigger to smaller
            self.hand_dictionary.update({'is_royal_flush': True})
            print(f"Royal Flush from {self.name}!")

            for c in organize_order_to_print:
                # add to final hand_with_table
                self.hand_with_table.append(store_values_and_cards.get(c))
            for each_card in self.hand_with_table:
                self.special_value += Cards.full_cards_values.get(each_card)
            return True
# bütün eller bitince  returnları kaldır.Bütün elleri tek bir fonksiyondan yönet.
        self.possess_any_special_hand -=1
        return False

    def is_straight_flush(self, Cards):
        self.hand_with_table.clear()
        self.special_value = 0
        combine_cards = Cards.table + self.hands

        store_indexes_and_cards = {}
        # get card's indexes to check them if they are sorted.
        store_indexes = []

        for card in combine_cards:
            kind, value = card.split()
            # 14 13 12 11, standart card values
            temp_index = Cards.card_values.get(value)

            if temp_index in store_indexes:  # it means same card value exists
                compare_card1 = store_indexes_and_cards.get(temp_index)
                value_compared_card1 = Cards.full_cards_values.get(
                    compare_card1)

                value_compare_card2 = Cards.full_cards_values.get(card)

                # if the current card is more valuable, update the dictionary
                if value_compared_card1 > value_compare_card2:

                    # update store dictionary
                    store_indexes_and_cards[Cards.card_values.get(
                        value)] = card

            #store_indexes_and_cards[Cards.card_values.get(value)] = card
            store_indexes.append(temp_index)
            store_indexes_and_cards[Cards.card_values.get(value)] = card

        store_indexes.sort(reverse=True)
        count = 0

        if store_indexes[0]-1 == store_indexes[1] and store_indexes[1]-1 == store_indexes[2] and store_indexes[2]-1 == store_indexes[3] and store_indexes[3]-1 == store_indexes[4]:
            # take the ordered cards and put them into the player final cards set on the table
            for each_index_value in range(len(store_indexes)-2):
                put_a_card = store_indexes_and_cards.get(
                    store_indexes[each_index_value])
                self.hand_with_table.append(put_a_card)
                self.special_value += Cards.full_cards_values.get(put_a_card)

            print(f"Straight Flush from {self.name}!")
            self.hand_dictionary.update({'is_straight_flush': True})
            return True
        self.possess_any_special_hand -=1
        return False

    def is_four_of_a_kind(self, Cards):
        self.hand_with_table = [0, 0, 0, 0, 0]  # assign elements.
        self.special_value = 0
        combine_cards = Cards.table + self.hands

        store_indexes_and_cards = {}

        store_values = []
        for card in combine_cards:
            kind, value = card.split()
            store_values.append(value)
            if store_values.count(value) == 4:
                # sen bu kartları heart diamond diye sırala. Bi de sona kalan en değerli olsun.
                # Heart 8 Diamond 8 Spade 8 Club 8
                max = 0
                for a in combine_cards:
                    if a.endswith(value):
                        if a.startswith("H"):
                            self.hand_with_table[0] = a
                        elif a.startswith("D"):
                            self.hand_with_table[1] = a
                        elif a.startswith("S"):
                            self.hand_with_table[2] = a
                        elif a.startswith("C"):
                            self.hand_with_table[3] = a
                    else:

                        if Cards.full_cards_values.get(a) > max:
                            max = Cards.full_cards_values.get(a)
                            self.hand_with_table[4] = a

                for card in self.hand_with_table:
                    self.special_value += Cards.full_cards_values.get(card)
                print(f"Four of a Kind from {self.name}!")
                self.hand_dictionary.update({'is_four_of_a_kind': True})
                return True
        self.possess_any_special_hand -=1
        return False

# -----------------------------------------------------------------------------------------
    def is_full_house(self, Cards):
        self.hand_with_table.clear()
        self.special_value = 0
        combine_cards = Cards.table + self.hands
        combine_cards = Player.order_cards(Cards, combine_cards)
        first_set = False
        second_set = False
        store_full_values = []
        store_values = []  # 12345678910jqka is a a value 2-14

        for card in combine_cards:
            kind, value = card.split()

            value = Cards.card_values.get(value)
            store_values.append(value)
        store_values.sort(reverse=True)

        for card in combine_cards:
            kind, value = card.split()
            value = Cards.card_values.get(value)
            full_card_value = Cards.full_cards_values.get(card)
            if store_values.count(value) == 3:

                first_set = True
                store_full_values.append(full_card_value)
                self.hand_with_table.append(card)

            elif store_values.count(value) == 2:

                second_set = True
                store_full_values.append(full_card_value)
                self.hand_with_table.append(card)

        if not first_set or not second_set:
            self.possess_any_special_hand -=1
            return False

        for a in self.hand_with_table:
            self.special_value += Cards.full_cards_values.get(a)

        print(f"Full House from {self.name}!")
        self.hand_dictionary.update({'is_full_house': True})
        return True

# -----------------------------------------------------------------------------------------
    def is_flush(self, Cards):
        self.hand_with_table.clear()
        self.special_value = 0
        combine_cards = Cards.table + self.hands
        combine_cards = Player.order_cards(Cards, combine_cards)
        store_kinds = []
        for card in combine_cards:
            kind, value = card.split()
            store_kinds.append(kind)
            if store_kinds.count(kind) == 5:
                for a in combine_cards:
                    if a.startswith(kind):
                        if len(self.hand_with_table) != 5:
                            self.hand_with_table.append(a)
                            self.special_value += Cards.full_cards_values.get(
                                a)
                print(f"Flush from {self.name}!")
                self.hand_dictionary.update({'is_flush': True})
                return True
        self.possess_any_special_hand -=1
        return False
# -----------------------------------------------------------------------------------------

    def is_straight(self, Cards):
        self.hand_with_table = [None,None,None,None,None]
        self.special_value = 0
        combine_cards = Cards.table + self.hands
        #combine_cards = ['Spade 3', 'Heart 9', 'Heart 7',
                         #'Heart 6', 'Heart 4', 'Club 5', 'Club A']
        combine_cards = Player.order_cards(Cards, combine_cards)

        # get card's indexes to check them if they are sorted.
        store_indexes = []
        temp_list = [] # will edit cards to sort them

        for card in combine_cards:
            kind, value = card.split()
            store_indexes.append(Cards.card_values.get(value))

        store_indexes.sort(reverse=True)
        
        counter = ['c', 'o', 'm', 'e', 'o', 'n', '!']

        check_if_its_straight = ''
        
        for a in range(len(store_indexes)-1):
            if store_indexes[a]-1 == store_indexes[a+1]:
                counter[a] = 'X'
                counter[a+1] = 'X'
    
            else:
                counter[a] = '0'

      
        for char in counter:
            check_if_its_straight += char
        if not 'XXXXX' in check_if_its_straight:
            self.possess_any_special_hand -=1
            return False
        check_substr = check_if_its_straight.find('XXXXX')
        highest_val = store_indexes[check_substr]
        highest_card = None

        for card in combine_cards:
            kind,value = card.split()
            new_card = value + ' ' + kind
            temp_list.append(new_card)
           

        sorted_temp_list = []
        temp_list.sort(reverse=True)
        for card in temp_list:
            value,kind = card.split()
            new_card = kind + ' '+value
            sorted_temp_list.append(new_card)
            value = Cards.card_values.get(value)
            if value==highest_val:
                highest_card = new_card
        self.hand_with_table[0] = highest_card
        combine_cards.remove(highest_card)

     
        for card in combine_cards:
            kind,value = card.split()
            num_value = Cards.card_values.get(value)
            if highest_val-1 ==num_value:
                self.hand_with_table[1] =card
            elif highest_val-2 ==num_value:
                self.hand_with_table[2] =card
            elif highest_val-3 ==num_value:
                self.hand_with_table[3] =card
            elif highest_val-4 ==num_value:
                self.hand_with_table[4] =card

        for card in self.hand_with_table:
            self.special_value += Cards.full_cards_values.get(card)

        print(f"Straight from {self.name}!")
        self.hand_dictionary.update({'is_straight': True})
        return True

# -----------------------------------------------------------------------------------------
    def is_three_of_a_kind(self, Cards):
        self.hand_with_table.clear()
        self.special_value = 0
        combine_cards = Cards.table + self.hands
        combine_cards = Player.order_cards(Cards,combine_cards)

        store_indexes_dict = {}
        store_indexes = []
        card1, card2, card3, temp1, temp2 = '', '', '', '', ''
        is_card2, is_card3 = False, False
        max = 0
        max1 = 0

        for card in combine_cards:
            kind, value = card.split()

            value = Cards.card_values.get(value)
            store_indexes.append(value)
            store_indexes.sort(reverse=True)
            if store_indexes_dict.get(value) == None:
                store_indexes_dict[value] = card
                continue
            if not is_card2:
                card2 = card
                is_card2 = True
                continue
            if not is_card3:
                card3 = card
                is_card3 = True

        find_best_remainder_cards = []

        for value in store_indexes:
            if store_indexes.count(value) == 3:
                card1 = store_indexes_dict.get(value)

                for item in store_indexes_dict:
                    if item == value:
                        continue
                    find_best_remainder_cards.append(
                        store_indexes_dict.get(item))

                for each_item in find_best_remainder_cards:

                    full_value = Cards.full_cards_values.get(each_item)
                    if full_value > max:
                        temp2 = temp1
                        temp1 = each_item
                        max1 = max
                        max = full_value
                    if full_value < max and full_value > max1:
                        temp2 = each_item
                        max1 = full_value

                self.special_value = Cards.full_cards_values.get(
                    card2)+Cards.full_cards_values.get(card3) + Cards.full_cards_values.get(card1) + max + max1
                self.hand_with_table = [card1, card2,
                                        card3, temp1, temp2]  # CARDS TO SHOW
                self.hand_dictionary.update({'is_three_of_a_kind':True})
                print(f"Three of a Kind from {self.name}!")
                return True
        self.possess_any_special_hand -=1
        return False



    def is_two_pair(self,Cards):
        self.hand_with_table.clear()
        self.special_value = 0
        combine_cards = Cards.table + self.hands
        combine_cards = Player.order_cards(Cards,combine_cards)

        store_values = [] #full values

        
        key_list = list(Cards.full_cards_values.keys())
        val_list = list(Cards.full_cards_values.values())
        hand_is_done = False #if two pairs, returns True

        #add full values to the list
        for card in combine_cards:
            value = Cards.full_cards_values.get(card)
            store_values.append(value)
          

        for value in store_values:

            for second_value in store_values:

                card = key_list[val_list.index(value)]
                card_matched = None

                if value-13==second_value:
                    card_matched = key_list[val_list.index(value-13)]
                    store_values.remove(second_value)

                elif value-26==second_value:
                    card_matched = key_list[val_list.index(value-26)]
                    store_values.remove(second_value)

                elif value-39==second_value:
                    card_matched = key_list[val_list.index(value-39)]
                    store_values.remove(second_value)

                elif value+13==second_value:
                    card_matched = key_list[val_list.index(value+13)]
                    store_values.remove(second_value)

                elif value+26==second_value:
                    card_matched = key_list[val_list.index(value+26)]
                    store_values.remove(second_value)

                elif value+39==second_value:
                    card_matched = key_list[val_list.index(value+39)]
                    store_values.remove(second_value)
                
                if card_matched and len(self.hand_with_table)<5:
                    if card not in self.hand_with_table and  card_matched not in self.hand_with_table:
                        self.hand_with_table.append(card)
                        self.hand_with_table.append(card_matched)
                        
                        if len(self.hand_with_table)==4:
                            hand_is_done = True

        if hand_is_done:
            for card in combine_cards:
                if card not in self.hand_with_table:
                    self.hand_with_table.append(card)
                    break
            
            self.hand_with_table = self.hand_with_table[0:5]
            for card in self.hand_with_table:
                value = Cards.full_cards_values.get(card)
                self.special_value += value
            self.hand_dictionary.update({'is_two_pair':True})
            print(f"Two pairs from {self.name}!")
            return True
        self.possess_any_special_hand -=1
        return False
    

    def is_one_pair(self,Cards):
        self.hand_with_table.clear()
        self.special_value = 0

        combine_cards = Cards.table + self.hands
        combine_cards = Player.order_cards(Cards,combine_cards)
        
        caught_value = None 
        caught_card = None
        store_values = [] #full values
        store_kinds = []

        for card in combine_cards:
            kind,value = card.split()
            store_kinds.append(kind)
            store_values.append(value)

        for i in range(len(store_values)):
            if store_values.count(store_values[i])==2:
                caught_value = store_values[i]
                caught_card = store_kinds[i] + ' ' + caught_value
                break
        if not caught_card:
            self.possess_any_special_hand -=1
            return False
        #else
        
        self.hand_with_table.append(caught_card)
        combine_cards.remove(caught_card)
        for card in combine_cards:
            kind,value = card.split()
            if value == caught_value:
                self.hand_with_table.append(card)
                combine_cards.remove(card)

    
        for card in combine_cards[0:3]:
            self.hand_with_table.append(card)

        
        for card in self.hand_with_table:
            value = Cards.full_cards_values.get(card)
            self.special_value += value
        print(f"One Pair from {self.name}!")
        self.hand_dictionary.update({'is_one_pair':True})
        return True


    # finally I realized i can order cards with a single function. I was an idiot.
    @classmethod
    def order_cards(cls, Cards, combine_cards):
        card_array = []
        full_cards_and_full_values = Cards.full_cards_values
        full_values_list = []

        key_list = list(full_cards_and_full_values.keys())
        val_list = list(full_cards_and_full_values.values())

        for card in combine_cards:
            full_value = Cards.full_cards_values.get(card)
            full_values_list.append(full_value)

        full_values_list.sort(reverse=True)
        for value in full_values_list:
            card = key_list[val_list.index(value)]
            card_array.append(card)
        return card_array

