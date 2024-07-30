
class Monster:
    monster_names = ["Palotrix", "Othexus", "Dimpofsuax", "Resqulxalire"]
    adjectives = ["Outrageous", "Elder", "Mad", "Legendary", "Epic"]
    appeared_monsters = []

    Palotrix_skills_list = ["Basic Flame", "Mumbling Whistle", "Mad"]
    Palotrix_skills_attr = {"Basic Flame": 0.7, "Mumbling Whistle": 1.2, "Mad": 1.4}
    Palotrix_skills_explain = {"Basic Flame": "used her most basic skill.Apparently she is not minding this battle.",
                               "Mumbling Whistle": "It seem you made her a bit angry.",
                               "Mad": "Now she swore to destroy you!"}

    Othexus_skills_list = ["Lion-claw", "Deadly Whisper", "Sky Shout"]
    Othexus_skills_attr = {"Lion-claw": 1, "Deadly Whisper": 1.15, "Sky Shout": 1.3}
    Othexus_skills_explain = {"Lion-claw": "Basic but efficient.",
                              "Deadly Whisper": "He opens his mouth and inhaling deeply.",
                              "Sky Shout": "He looks at the sky for a few seconds. After a strong clench and inhale, he unleash the beast inside him."}

    Dimpofsuax_skills_list = ["Beast", "Thunder", "Nemrud's Mosquitos", "Call of Eire"]
    Dimpofsuax_skills_attr = {"Beast": 1, "Thunder": 1.1, "Nemrud's Mosquitos": 1.3, "Call of Eire": 1.4}
    Dimpofsuax_skills_explain = {"Beast": "the basic attack.", "Thunder": "like a Thor, but less efficient.",
                                 "Nemrud's Mosquitos": "such an enemy for one who is greedy!",
                                 "Call of Eire": "apparently, he is kin of Thor."}

    Resqulxalire_skills_list = ["Gritty Lawa", "Ingloriousness", "Lowness", "Poltroon"]
    Resqulxalire_skills_attr = {"Gritty Lawa": 1, "Ingloriousness": 1.2, "Lowness": 1.3, "Poltroon": 1.4}
    Resqulxalire_skills_explain = {"Gritty Lawa": "He open his hands and releases the grits and lawa.",
                                   "Ingloriousness": "the pure sign of evil.", "Lowness": "which is familiar.",
                                   "Poltroon": "which is unexpected!"}
    num_of_mons = 0

    def __init__(self):
        Monster.num_of_mons += 1
        while True:
            if player1.level in range(1, 4):
                self.adjective = Monster.adjectives[0]
            elif player1.level in range(4, 7):
                self.adjective = r.choice(Monster.adjectives[0:2], )
            elif player1.level in range(5, 9):
                self.adjective = r.choice(Monster.adjectives[0:3])
            elif player1.level in range(7, 12):
                self.adjective = r.choice(Monster.adjectives[0:4])
            elif player1.level >= 12:
                self.adjective = r.choice(Monster.adjectives)
            self.secondname = r.choice(Monster.monster_names)
            self.name = self.secondname + " The " + self.adjective
            if self.name in Monster.appeared_monsters:
                if len(Monster.appeared_monsters) <= 20:
                    self.secondname = r.choice(Monster.monster_names)
                    self.name = self.secondname + " The " + self.adjective
                    continue

            Monster.appeared_monsters.append(self.name)
            self.power = 1
            self.healpoint = 1
            self.level = 1
            break

    def monster_create(self):
        if self.secondname == "Palotrix":
            if player1.level <= 1:
                self.level = player1.level + r.randint(0, 1)
            else:
                self.level = player1.level + r.randint(-1, +4)
            self.power = self.level * 10
            self.healpoint = self.power * 4
            self.skills_list = Monster.Palotrix_skills_list
            self.skills_attr = Monster.Palotrix_skills_attr
            self.skills_explain = Monster.Palotrix_skills_explain
        elif self.secondname == "Othexus":
            if player1.level <= 1:
                self.level = player1.level + r.randint(0, 1)
            else:
                self.level = player1.level + r.randint(0, 1)
            self.power = self.level * 12
            self.healpoint = self.power * 5
            self.skills_list = Monster.Othexus_skills_list
            self.skills_attr = Monster.Othexus_skills_attr
            self.skills_explain = Monster.Othexus_skills_explain
        elif self.secondname == "Dimpofsuax":
            if player1.level <= 1:
                self.level = player1.level + r.randint(0, 1)
            else:
                self.level = player1.level + r.randint(-1, +4)
            self.power = self.level * 13
            self.healpoint = self.power * 6
            self.skills_list = Monster.Dimpofsuax_skills_list
            self.skills_attr = Monster.Dimpofsuax_skills_attr
            self.skills_explain = Monster.Dimpofsuax_skills_explain
        elif self.secondname == "Resqulxalire":
            if player1.level <= 1:
                self.level = player1.level + r.randint(0, 1)
            else:
                self.level = player1.level + r.randint(-1, +4)
            self.power = self.level * 14
            self.healpoint = self.power * 7
            self.skills_list = Monster.Resqulxalire_skills_list
            self.skills_attr = Monster.Resqulxalire_skills_attr
            self.skills_explain = Monster.Resqulxalire_skills_explain
        if self.adjective == "Outrageous":
            self.power *= int(1)
            self.healpoint *= int(1)
        elif self.adjective == "Elder":
            self.power *= int(1.2)
            self.healpoint *= int(1.2)
        elif self.adjective == "Mad":
            self.power *= int(1.5)
            self.healpoint *= int(1.5)
        elif self.adjective == "Legendary":
            self.power *= int(1.8)
            self.healpoint *= int(1.8)
        elif self.adjective == "Epic":
            self.power *= 2
            self.healpoint *= 2
        print(f"\t\t{red}{self.name} is appeared.\n\t\t{red}Level: {yellow}{self.level}{red} Power: {yellow}{self.power} {red}HP: {yellow}{self.healpoint}{default}\n")
        self.total_damage_give = 0
        self.monster_dead = False

    def attack(self):
        input("...")
        attacked_list = []
        attack = r.choice(self.skills_list)
        while not self.monster_dead:
            attack = r.choice(self.skills_list)
            if attack in attacked_list and len(attacked_list) == len(self.skills_list):
                break
            elif attack in attacked_list and len(attacked_list) < len(self.skills_list):
                continue
            else:
                attacked_list.append(attack)
                break
        damage = int(self.power * self.skills_attr[attack])
        print(f"\t{red}System: {green}{self.name} uses '{yellow}{attack}{green}' skill and gave you {yellow}{damage}{green} damage.{default}")
        player1.in_battle_heal_point -= damage
        if player1.in_battle_heal_point < 0:
            print(f"\t{red}System:{green} You died.{green}")
            game_over()
            return play_game()

    # en sona adjective a göre gold ekle.
    def drop_item(self):
        dropitem = r.choice(whole_item_control)
        gold = 100
        if self.level in range(1, 5):
            gold = r.randint(50, 150)
            chance = r.randint(1, 10)
            if chance == 5:
                templist = ['single sword', 'single axe', 'bow']
                dropitem = r.choice(templist)
        elif self.level in range(5, 8):
            gold = r.randint(150, 300)
            templist = ['dwarf armor', 'elven armor', 'warrior armor']
            dropitem = r.choice(templist)
        elif self.level in range(8, 1000):
            gold = r.randint(200, 3000)
            dropitem = r.choice(whole_item_control)
        if self.adjective == Monster.adjectives[1]:
            gold += r.randint(100, 400)
        elif self.adjective == Monster.adjectives[2]:
            gold += r.randint(250, 500)
        elif self.adjectives == Monster.adjectives[3]:
            gold += r.randint(500, 1000)
        elif self.adjectives == Monster.adjectives[4]:
            gold += r.randint(1000, 3000)
            templist = ['aragorn armor', 'legolas armor', 'gimli armor']
            dropitem = r.choice(templist)
        pills = ['blue pill', 'red pill']
        dropitem2 = r.choice(pills)
        dropitemchance = r.randint(1, 2)
        player_inventory.append(dropitem)
        player_inventory.append(dropitem2)
        if dropitemchance == 2:
            player_inventory.append(dropitem2)
        input(f"\t{red}System: {yellow}'{dropitem.title()}{default}' and '{yellow}{dropitem2.title()} x{dropitemchance}'{green} added to your inventory.{default}")
        input(f"\t{red}System: {yellow}'{gold} Gold'{green} added to your pocket.")
        player1.gold += gold
