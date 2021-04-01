from Champion import Champion
from ChampionList import CHAMPION_LIST, ChoGath, Maokai, Nunu, Ornn, Shyvana, TahmKench, Sett, Vi

class Comp:

  def __init__(self, name, champs):
    self.name = name
    self.champs = []

CULTIST = Comp("Cultist", [])
for champ in CHAMPION_LIST:
    if "Cultist" in champ.traits:
        CULTIST.champs.append(champ)

VANGUARD = Comp("Vanguard", [])
for champ in CHAMPION_LIST:
    if "Vanguard" in champ.traits:
        VANGUARD.champs.append(champ)

ASSASSIN = Comp("Assassin", [])
for champ in CHAMPION_LIST:
    if "Assassin" in champ.traits:
        ASSASSIN.champs.append(champ)

BRAWLER = Comp("Brawler", [])
for champ in CHAMPION_LIST:
    if "Brawler" in champ.traits:
        BRAWLER.champs.append(champ)

BETTER = Comp("Better", [ChoGath, Sett, TahmKench, Vi, Nunu, Shyvana, Maokai, Ornn])
BETTER.champs = [ChoGath, Sett, TahmKench, Vi, Nunu, Shyvana, Maokai]


COMPOS_LIST = [ASSASSIN, CULTIST, VANGUARD]
