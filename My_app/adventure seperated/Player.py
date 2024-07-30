from adventure import user_race
class Player:
    common_skill_manas = {"Iron Arrow": 0, "Silver Arrow": 0.15, "Call of Arwen": 0.20, "Forest Magic": 0.4,
                          'Soul Stealing': 0, 'Arken': 0.2, 'Athelas': 0.2, 'Whisper to the Dead': 0.4,
                          "Tenos": 0,
                          "Kalxelar": 0.2,
                          "Magic of Beard": 0.3,
                          "Madness": 0.6
                          }
    elf_skills = {
        "Iron Arrow": 1,  # standart attack
        "Silver Arrow": 1.20,  # standart
        "Call of Arwen": 1.3,  # gives attack and  heal
        "Forest Magic": 1.9  # standart
    }
    warrior_skills = {
        "Soul Stealing": 1,  # standart + heal
        "Arken": 1.6,  # standart
        "Athelas": 1.3,  # standart+heal
        "Whisper to the Dead": 2.4  # standart
    }
    dwarf_skills = {
        "Tenos": 0.7,  # heal, attack
        "Kalxelar": 1.7,  # attack
        "Magic of Beard": 2,  # attack
        "Madness": 1.8  # attack and heal
    }

    explain_elf_skills = {
        "Iron Arrow": "%100 damage. 0 MP.",
        "Silver Arrow": "%120 damage. -%15 MP.",
        "Call of Arwen": "%130 damage and %15 self-heal. -%20 MP.",
        "Forest Magic": "%190 damage. -%40 MP."
    }
    explain_warrior_skills = {
        "Soul Stealing": "%100 damage, 0 MP.",
        "Arken": "%160 damage. -%20 MP",
        "Athelas": "%130 damage amd %30 self-heal. -%20 MP.",
        "Whisper to the Dead": "Calling the dead and deals %240 damage. -%40 MP."
    }
    explain_dwarf_skills = {
        "Tenos": "%70 damage and %10 heal. 0 MP.",  # heal, attack
        "Kalxelar": "%170 damage. -%20 MP.",
        "Magic of Beard": "%200 damage. -%30 MP.",
        "Madness": "%220 damage. -%60 MP."
    }

    elf_skills_select_list = ["Iron Arrow", "Silver Arrow", "Call of Arwen", "Forest Magic"]
    warrior_skills_select_list = ['Soul Stealing', 'Arken', 'Athelas', 'Whisper to the Dead']
    dwarf_skills_select_list = ['Tenos', 'Kalxelar', 'Magic of Beard', 'Madness']

    def __init__(self, name):
        self.name = name
        self.level = 1
        self.power = 0
        self.gold = 0

        self.fullpower = self.level + self.power

    def level_up(self):
        self.level += 1  # bunu yaratığın gücüne göre değişken verdir.
        input(f"\t{green}Level up! New level is {yellow}{self.level}.{default}")
        if user_race == "Elf":
            self.fullpower = 10 + self.level * 3 + 3
            self.fullpower += self.power
            self.mana_point += self.level * 50
            self.heal_point += self.level * 45
        elif user_race == "Warrior":
            self.fullpower = 10 + self.level * 4 + 5
            self.fullpower += self.power
            self.mana_point += self.level * 43
            self.heal_point += self.level * 45
        elif user_race == "Dwarf":
            self.fullpower = 7 + self.level * 3 + 4
            self.fullpower += self.power
            self.mana_point += self.level * 50
            self.heal_point += self.level * 45

    def player_race_optimize(self):
        if user_race == "Elf":
            self.heal_point = 100 + self.level * 45
            self.mana_point = 120 + self.level * 50
            self.gold = 350
            self.fullpower = 10 + self.level * 3 + 2
            self.skills_list = Player.elf_skills_select_list
            self.explain_skills_list = Player.explain_elf_skills
            self.skills_damage = Player.elf_skills
        elif user_race == "Warrior":
            self.fullpower += 10 + self.level * 4 + 3
            self.heal_point = 100 + self.level * 45
            self.mana_point = 90 + self.level * 43
            self.gold = 300
            self.skills_list = Player.warrior_skills_select_list
            self.explain_skills_list = Player.explain_warrior_skills
            self.skills_damage = Player.warrior_skills
        elif user_race == "Dwarf":
            self.mana_point = 140 + self.level * 50
            self.heal_point = 110 + self.level * 45
            self.fullpower += 7 + self.level * 3 + 2
            self.gold = 430
            self.skills_list = Player.dwarf_skills_select_list
            self.explain_skills_list = Player.explain_dwarf_skills
            self.skills_damage = Player.dwarf_skills

        print(
            f"\t{green}Player created!\n\n\t{blue}{user_race}\t\t{self.name}\n\n\t{red}Level: {yellow}{self.level}{red}\tItem Power: {yellow}{self.power}\n\n\t{red}Full Power: {yellow}{self.fullpower}\t{red}Heal Point: {yellow}{self.heal_point}\n\n\t{red}Mana Point: {yellow}{self.mana_point}\t{red}Gold: {yellow}{self.gold}{default}")
        self.in_battle_heal_point = 0
        self.in_battle_mana_point = 0
        self.skills_mana_cost = Player.common_skill_manas

    def player_info(self):
        print(
            f"\t{green}CHARACTER INFO\n\t{blue}{user_race}\t\t{self.name}\n\n\t{red}Level: {yellow}{self.level}{red}\tItem Power: {yellow}{self.power}\n\n\t{red}Full Power: {yellow}{self.fullpower}\t{red}Heal Point: {yellow}{self.heal_point}\n\n\t{red}Mana Point: {yellow}{self   .mana_point}\t{red}Gold: {yellow}{self.gold}{default}")

    def player_attack(self):
        while True:
            input("...")
            clear()
            print(f"\n\t{red}{monster1.name}, {blue}Level: {yellow}{monster1.level} \n\t{blue}HP: {yellow}{monster1.healpoint}, {blue}Power: {yellow}{monster1.power}")
            print(
                f"\n\t{magenta}{self.name}, {blue}Level: {yellow}{player1.level} \n\t{blue}HP: {yellow}{self.in_battle_heal_point} {blue}MP: {yellow}{self.in_battle_mana} {blue}Power: {yellow}{player1.fullpower}{default}")

            print(f"\t\t{green}SKILLS")
            c = 1
            for key, value in player1.explain_skills_list.items():
                print(yellow,str(c) + "-)"+blue+key, ":"+yellow, value)
                c += 1
            print(f"\n{magenta}Type '{red}r{magenta}' or '{blue}b{magenta}' to use {red}red pill {magenta}or {blue}blue pill{default}\n")
            skill_input = input(f'{magenta}Select a skill: ').lower()
            if skill_input == '1':
                that_skill = self.skills_list[0]
                if user_race == "Dwarf":
                    self.in_battle_heal_point += int(player1.heal_point * 0.10)
                    print(f"\t{red}System: {int(player1.heal_point * 0.10)} HP {yellow} is restored.{default}")
            elif skill_input == '2':
                that_skill = self.skills_list[1]
            elif skill_input == '3':
                that_skill = self.skills_list[2]
                if user_race == "Elf":
                    self.in_battle_heal_point += int(player1.heal_point * 0.15)
                    print(f"\t{red}System: {int(player1.heal_point * 0.15)} HP {yellow}is restored.{default}")
                elif user_race == "Warrior":
                    self.in_battle_heal_point += int(player1.heal_point * 0.30)
                    print(f"\t{red}System: {int(player1.heal_point * 0.30)} HP {yellow}is restored.{default}")
            elif skill_input == '4':
                that_skill = self.skills_list[3]
            elif skill_input == 'r':
                if 'red pill' not in player_inventory:
                    print(f"\t{red}System: You don't have any red pill.")
                    continue
                else:
                    player1.in_battle_heal_point += 50 * player1.level
                    player1.in_battle_mana_point += 40 * player1.level
                    print(
                        f"\t{red}System: Red pill {yellow}used. {blue}HP: {yellow}{player1.in_battle_heal_point} {blue}MP: {yellow}{player1.in_battle_mana_point}{default}")
                    continue
            elif skill_input == 'b':
                if 'blue pill' not in player_inventory:
                    print(f"\t{red}System: You don't have any {blue}blue pill.{default}")
                    continue
                else:
                    player1.in_battle_heal_point += 70 * player1.level
                    player1.in_battle_mana_point += 60 * player1.level
                    print(
                        f"\t{red}System: {blue}Blue pill {yellow}used. {blue}HP: {yellow}{player1.in_battle_heal_point} {blue}MP: {yellow}{player1.in_battle_mana_point}{default}")
                    continue
            else:
                print(f"{red}\tSystem: Please enter a valid skill number!{default}")
                continue
            self.mana_cost = int(self.skills_mana_cost[that_skill] * self.mana_point)
            critical_hit = r.randint(1, 3)
            if critical_hit == 2:
                critical_hit = r.randint(2, 3)
                print(f"\t{red}System: {green}CRITICAL HIT! YOU HIT THE HEAD!{default}")
            else:
                critical_hit == 1
            attack_multipler = self.skills_damage[that_skill] * critical_hit
            self.damage_attack = int(self.fullpower * attack_multipler)
            if self.in_battle_mana < self.mana_cost:
                print(f"\n\t{red}System: Your mana(skill point) is not enough!{default}")
                continue
            self.in_battle_mana -= self.mana_cost
            monster1.healpoint -= self.damage_attack
            if monster1.healpoint <= player1.fullpower:
                clear()
                while True:
                    random_sentence = r.choice(monstersentences)
                    if random_sentence in used_monstersentences:
                        if len(used_monstersentences) >= 6:
                            break
                        else:
                            continue
                    else:
                        used_monstersentences.append(random_sentence)
                        break
                print(f"{red}{monster1.name}: {yellow}{random_sentence}{default}")
                input(f'{magenta}...{default}')
                clear()
            if monster1.healpoint >= player1.fullpower:
                random_number = r.randint(0, 3)
                if random_number == 2:
                    clear()
                    while True:
                        random_sentence = r.choice(generic_monster_sentences)
                        if random_sentence in used_monstersentences:
                            if len(used_monstersentences) - 2 < len(used_monstersentences):
                                break
                            else:
                                continue
                        used_monstersentences.append(random_sentence)
                    print(f"{red}{monster1.name}: {yellow}{random_sentence}")
                    input('...')
                    clear()
            print(f"\t{red}System: {green}You gave {yellow}{self.damage_attack} {green}damage.{default}")
            break


