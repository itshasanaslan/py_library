
warrior_item = (
    "single sword", "double sword", 'single axe', 'bow', 'ring', 'mighty ring', 'elven armor', 'warrior armor',
    'dwarf armor', 'aragorn armor', 'red pill', 'blue pill', 'shield', 'great shield')
dwarf_item = (
    'single sword', 'single axe', 'double axe', 'bow', 'ring', 'mighty ring', 'elven armor', 'warrior armor',
    'dwarf armor',
    'gimli armor', 'red pill', 'blue pill', 'shield')
elf_item = (
    'single sword', 'single axe', 'bow', 'mighty ring', 'ring', 'mighty bow', 'elven armor', 'warrior armor',
    'dwarf armor',
    'legolas armor', 'red pill', 'blue pill', 'shield', 'great shield')

single_handed_list = ("single sword", "shield", 'single axe', 'great shield')
double_handed_list = ('double sword', 'double axe', 'bow', 'mighty bow')

item_prices = {
    "aragorn armor": 2000,
    "legolas armor": 2400,
    'great shield': 1000,
    'double sword': 1000,
    "warrior armor": 550,
    "gimli armor": 3000,
    'mighty ring': 1420,
    'single sword': 500,
    'mighty bow': 1000,
    'double axe': 1000,
    "elven armor": 600,
    "dwarf armor": 700,
    'single axe': 500,
    "blue pill": 300,
    "red pill": 300,
    'shield': 600,
    'ring': 500,
    'bow': 500,
}

string_item_prices = {
    "aragorn armor": '  :   2000 Gold',
    "legolas armor": '  :   2400 Gold',
    'great shield': '   :   1000 Gold',
    'double sword': '   :   1000 Gold',
    "warrior armor": '  :   550  Gold',
    "gimli armor": '    :   3000 Gold',
    'mighty ring': '    :   1420 Gold',
    'single sword': '   :   500  Gold',
    'mighty bow': '     :   1000 Gold',
    'double axe': '     :   1000 Gold',
    "elven armor": '    :   600  Gold',
    "dwarf armor": '    :   700  Gold',
    'single axe': ':    :   500  Gold',
    "blue pill": '      :   300  Gold',
    "red pill": '       :   300  Gold',
    'shield': '         :   600  Gold',
    'ring': '           :   500  Gold',
    'bow': '            :   500  Gold'
}

string_item_tags = {
    "single sword": "   Gives '4' extra attack power.Warriors get +3 ",
    "single axe": "     Gives '4' extra attack power. ",
    "shield": "         Gives '4' extra attack power. Elves get +2",
    "great shield": "   Gives '7' extra attack power. Warriors get +3. ",
    "double sword": "   Gives '13' extra attack power.  ",
    "double axe": "     Gives '14' extra attack power. Dwarves get +2 ",
    "bow": "            Gives '4' extra attack power. Elves get +4",
    "mighty bow": "     Gives '10' extra attack power.",
    "ring": "           Gives '5' extra attack power. Elves get +3.",
    "mighty ring": "    Gives '10' extra attack power.If you are Dwarf, You will get +8.",
    "elven armor": "    Gives '90' heal points and '45' mana points.",
    "warrior armor": "  Gives '100' heal points and '60' mana points.",
    "dwarf armor": "    Gives '95' heal points and '45' mana points.",
    "aragorn armor": "  Gives '280' heal points and '200' mana points.",
    "legolas armor": "  Gives '240' heal points and '205' mana points.",
    "gimli armor": "    Gives '250' heal points and '190' mana points.",
    "red pill": "       Gives '50' heal points and '40' mana points for per level.",
    "blue pill": "      Gives '70' heal points and '60' mana points for per level."
}

item_tags = {
    "single sword": 4,
    "single axe": 4,
    "shield": 4,
    "great shield": 7,
    "double sword": 13,
    "double axe": 14,
    "bow": 4,
    "mighty bow": 10,
    "ring": 5,
    "mighty ring": 10,
    "elven armor": 0,
    "warrior armor": 0,
    "dwarf armor": 0,
    "aragorn armor": 0,
    "legolas armor": 0,
    "gimli armor": 0,
    "red pill": 0,
    "blue pill": 0
}

item_heals = {
    "elven armor": 90,
    "warrior armor": 100,
    "dwarf armor": 95,
    "aragorn armor": 280,
    "legolas armor": 240,
    "gimli armor": 250,
    "red pill": 50,
    "blue pill": 70
}

item_mana = {
    "elven armor": 45,
    "warrior armor": 60,
    "dwarf armor": 45,
    "aragorn armor": 200,
    "legolas armor": 205,
    "gimli armor": 190,
    "red pill": 40,
    "blue pill": 60
}


equipped = []
single_equipped = []
double_equipped = []
armor_equipped = []
player_inventory = []
upgraded_item_list = []
upgraded_item_price = {}