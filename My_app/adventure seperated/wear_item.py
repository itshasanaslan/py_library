
def wear_item():
    clear()
    if len(player_inventory) == 0:
        print(f"\t\t{red}You don't have any item yet.Try '{yellow}market{red}'{default}")
        return take_action()
    print(f"{blue}---------------------- WEAR ITEM-----------------------{default}\n\t\tType '{red}ok{default}' to return menu. '{red}remove{default}' to take off an item you equipped.")
    while True:
        input("..")
        clear()
        display_player_inventory()
        print(f"\n{magenta}Available commands:'{yellow}ok{magenta}', '{yellow}m{magenta}', '{yellow}remove{magenta}', '{yellow}inventory{magenta}'\n")
        wear_input = input(f"\n{magenta}Which item you want to wear: {default}").lower()
        if wear_input == "info":
            player1.player_info()
            continue
        if wear_input == "ok":
            clear()
            return take_action()
        elif wear_input == "inventory" or wear_input == 'i':
            display_player_inventory()
            continue
        elif wear_input == "m" or wear_input == 'menu':
            clear()
            return take_action()
        elif wear_input == "remove" or wear_input == 'r':
            return remove_item()
        elif wear_input not in item_tags:
            print(f"{red}\t\tNo such item!{default}")
            continue
        elif wear_input in equipped:
            print(f"{red}\t\tItem '{wear_input.title()}' already equipped!")
            input(f'{magenta}\n\nPress anything to continue.{default}')
            continue
        elif wear_input not in player_inventory:
            print(f"\t\t{red}You don't have '{wear_input.title()}' item.")
            input(f'{magenta}\n\nPress anything to continue.{default}')
            continue
        elif 'ring' in wear_input:
            equipped.append(wear_input)
            print(f"\t\t{green}'{wear_input.title()}' is equipped{default}")
            player1.power += item_tags.get(wear_input)
            input(f'{magenta}\n\nPress anything to continue.{default}')
            clear()
            continue
        elif wear_input not in player_wearable:
            if "armor" in wear_input:
                print(f"\t\t{red}This armor is not suitable for you.{default}")
                continue
            else:
                if wear_input in single_handed_list and len(single_equipped) == 0 and len(double_equipped) == 0:
                    equipped.append(wear_input)
                    single_equipped.append(wear_input)
                    player1.fullpower -= player1.power
                    player1.power += item_tags[wear_input]
                    player1.fullpower += player1.power
                    print(f"\t\t{green}'{wear_input.title()}' is equipped.{default}")

                elif wear_input in double_handed_list and len(single_equipped) == 0 and len(double_equipped) == 0:
                    print(f"\t\t{red}It is not suitable for you. So I decrease 5 power points.{default}")
                    equipped.append(wear_input)
                    double_equipped.append(wear_input)
                    item_tags[wear_input] -= 5
                    player1.fullpower -= player1.power
                    player1.power += item_tags[wear_input]
                    player1.fullpower += player1.power
                    print(f"\t\t{green}'{wear_input.title()}' is equipped.{default}")
                elif wear_input in single_handed_list and len(single_equipped) == 1 and len(double_equipped) == 0:
                    equipped.append(wear_input)
                    single_equipped.append(wear_input)
                    player1.fullpower -= player1.power
                    player1.power += item_tags[wear_input]
                    player1.fullpower += player1.power
                    print(f"\t\t{green}'{wear_input.title()}' is equipped.{default}")
                else:
                    print(f"\t\t{red}You can only carry one double handed or 2 single handed weapon at same time!{default}")
                    continue
        elif wear_input in player_wearable:
            if "pill" in wear_input:
                if wear_input in player_inventory:
                    global player_health_wo_pills, player_mana_wo_pills
                    player_health_wo_pills = player1.heal_point
                    player_mana_wo_pills = player1.mana_point
                    for b in equipped:
                        if b in item_heals:
                            player1.heal_point += item_heals[b]
                        if b in item_mana:
                            player1.mana_point += item_mana[b]

                    print(f"{green}\t\tPure heal is {player_health_wo_pills}, pure mana {player_mana_wo_pills}{default}")
                    player1.heal_point += item_heals[wear_input]
                    player1.mana_point += item_mana[wear_input]
                    player_inventory.remove(wear_input)
                    print(f"{green}\t\tYour current heal is {yellow}{player1.heal_point}. {green}Your mana point is {yellow}{player1.mana_point}{default}")
                    continue
                else:
                    print(f"\t\t{red}You don't have any pills!{default}")
            elif wear_input in equipped:
                print(f"\t\t{red}Item '{wear_input.title()}' already equipped!{default}")
                continue
            elif "armor" in wear_input:
                if len(armor_equipped) > 0:
                    print(f"\t\t{red}You need to take off '{armor_equipped[0]}'{default}")
                    continue
                armor_equipped.append(wear_input)
                equipped.append(wear_input)
                player1.heal_point += item_heals[wear_input]
                player1.mana_point += item_mana[wear_input]
                print(f"\t\t{green}'{wear_input.title()}' is equipped.{default}")
                print(f"\t\t{green}Your current heal is{yellow} {player1.heal_point}{green}. Your mana point is {yellow}{player1.mana_point}{default}")
            else:
                if wear_input in single_handed_list and len(single_equipped) == 0 and len(double_equipped) == 0:
                    equipped.append(wear_input)
                    single_equipped.append(wear_input)
                    player1.fullpower -= player1.power
                    player1.power += item_tags[wear_input]
                    player1.fullpower += player1.power
                    print(f"\t\t{green}'{wear_input.title()}' is equipped{default}")

                elif wear_input in double_handed_list and len(single_equipped) == 0 and len(double_equipped) == 0:
                    equipped.append(wear_input)
                    double_equipped.append(wear_input)
                    player1.fullpower -= player1.power
                    player1.power += item_tags[wear_input]
                    player1.fullpower += player1.power
                    print(f"{green}\t\t'{wear_input.title()}' is equipped{default}")
                elif wear_input in single_handed_list and len(single_equipped) == 1 and len(double_equipped) == 0:
                    equipped.append(wear_input)
                    single_equipped.append(wear_input)
                    player1.fullpower -= player1.power
                    player1.power += item_tags[wear_input]
                    player1.fullpower += player1.power
                    print(f"{green}\t\t'{wear_input.title()}' is equipped{default}")
                else:
                    print(f"{red}\t\t You can only carry one double handed or 2 single handed weapon at same time!{default}")
                    continue

