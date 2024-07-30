
def remove_item():
    if len(player_inventory) == 0:
        print(f"\t\t{red}You don't have any item!{default}")
        input(f'{magenta}\n\nPress anything to continue.{default}')
        clear()
        return wear_item()
    elif len(equipped) == 0:
        print(f"{red}\n\t\tYou are not wearing any item!\n{default}")
        input(f'{magenta}\n\nPress anything to continue.{default}')
        clear()
        return wear_item()

    while True:
        clear()
        print(f"{blue}---------------------- REMOVE ITEM-----------------------{default}")
        print(f"\t\t{yellow}Here you can take off your items. They will stay in your inventory till you equip or sell them.{default}")
        print(f"{magenta}Available commands: '{yellow}ok{magenta}', '{yellow}menu{magenta}' or '{yellow}m{magenta}'{default}\n")
        remove_input = input(f"{magenta}Which item you want to remove: {default}").lower()
        if remove_input == "ok":
            return wear_item()
        elif remove_input == "info":
            player1.player_info()
            continue
        elif remove_input == "bla":
            print("bla")
        elif remove_input == "inventory":
            display_player_inventory()
            input(f'{magenta}\n\nPress anything to continue.{default}')
            continue
        elif remove_input not in item_tags:
            print(f"{red}\t\tNo such item!{default}")
            input(f'{magenta}\n\nPress anything to continue.{default}')
            continue
        elif remove_input not in equipped:
            print(f"{red}\t\tYou weren't wearing that item.{default}")
            input(f'{magenta}\n\nPress anything to continue.{default}')
            continue
        elif remove_input not in player_wearable and remove_input in equipped:
            print(f"{green}\t\tIt wasn't fitting you anyway.{default}")
            if remove_input in double_equipped:
                double_equipped.remove(remove_input)
            elif remove_input in single_equipped:
                single_equipped.remove(remove_input)
            player1.fullpower -= player1.power
            player1.power -= item_tags[remove_input] - 5
            player1.fullpower += player1.power
            equipped.remove(remove_input)
            print(f"{blue}\t\t'{remove_input}' is removed.{default}")
        elif remove_input in player_wearable and remove_input in equipped:
            if 'armor' in remove_input:
                armor_equipped.remove(remove_input)
                print(f"{blue}\t\t'{remove_input.title()}' is removed.{default}")
                player1.heal_point -= item_heals[remove_input]
                player1.mana_point -= item_mana[remove_input]
                equipped.remove(remove_input)
                print(
                    f"\t\t{green}Your current heal point is {yellow}{player1.heal_point}{green}.Your current mana point is {yellow}{player1.mana_point}{default}")
            else:
                if remove_input in single_equipped:
                    single_equipped.remove(remove_input)
                elif remove_input in double_equipped:
                    double_equipped.remove(remove_input)
                player1.fullpower -= player1.power
                player1.power -= item_tags[remove_input]
                player1.fullpower += player1.power
                print(f"{blue}\t\t'{remove_input}' is removed{default}")
                equipped.remove(remove_input)
                print(f"\t\t{green}Your current power is {yellow}{player1.fullpower}{default}")
                input(f'{magenta}\n\nPress anything to continue.{default}')

