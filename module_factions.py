# S T A R   W A R S   C O N Q U E S T   M O D U L E   S Y S T E M
# / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /
# By Taleworlds, HokieBT, MartinF and Swyter - Do not use/copy without permission

from header_factions import *

####################################################################################################################
#  Each faction record contains the following fields:
#  1) Faction id: used for referencing factions in other files.
#     The prefix fac_ is automatically added before each faction id.
#  2) Faction name.
#  3) Faction flags. See header_factions.py for a list of available flags
#  4) Faction coherence. Relation between members of this faction.
#  5) Relations. This is a list of relation records.
#     Each relation record is a tuple that contains the following fields:
#    5.1) Faction. Which other faction this relation is referring to
#    5.2) Value: Relation value between the two factions.
#         Values range between -1 and 1.
#  6) Ranks
#  7) Faction color (default is gray)
####################################################################################################################

default_faction_relations = [("outlaws",-0.05),("deserters", -0.05),("black_sun_pirates", -0.02),("blazing_claw_pirates", -0.02)]
factions = [
  ("no_faction","No Faction",0, 0.9, [], []),
  ("commoners", "Commoners", 0, 0.1,[("player_faction",0.1)], []),
  ("outlaws",   "Outlaws", max_player_rating(-30), 0.5,[("commoners",-0.6),("player_faction",-0.15)], [], 0xFFFF66),

##Factions before this point are hardwired into the game end their order should not be changed.
  ("neutral",  "Neutral",                      0, 0.1,[("player_faction",0.0)], [],0xFFFFFF),
  ("innocents","Innocents", ff_always_hide_label, 0.5,[("outlaws",-0.05)],      []),
  ("merchants","Merchants", ff_always_hide_label, 0.5,[("outlaws",-0.5),],      []),

##SW MF added new factions
  ("trade_federation","Independent", ff_always_hide_label, 0.5,[("outlaws",-0.5),("deserters", -0.2),("black_sun_pirates", -0.5),("blazing_claw_pirates", -0.5),("slavers", 0.1),("bountyhunters", 0.1)], [],0xDDDD33),
 #("privateers", "Privateers", 0, 0.5, [("outlaws",-0.5),("deserters", -0.2),("black_sun_pirates", -0.5),("blazing_claw_pirates", -0.5),("slavers", 0.1),("bountyhunters", 0.1)], [],0xCC2211),
 #("bounty_hunters", "Bounty Hunters", 0, 0.5, [("outlaws",0),("black_sun_pirates", 0),("blazing_claw_pirates", 0)],[],0x96CDCD),

 #("dark_knights","Dark Knights", 0, 0.5,[("innocents",-0.9),("player_faction",-0.4)], []),


  ("culture_1",  "<culture_1>", 0, 0.9, [], []),  ##@> Empire culture
  ("culture_2",  "<culture_2>", 0, 0.9, [], []),  ##@> Rebel culture
  ("culture_3",  "<culture_3>", 0, 0.9, [], []),  ##@> Hutt culture
  ("culture_4",  "<culture_4>", 0, 0.9, [], []),  ##@> Wookie culture
  ("culture_5",  "<culture_5>", 0, 0.9, [], []),  ##@> Mandalorian culture
  ("culture_6",  "<culture_6>", 0, 0.9, [], []),  ##@> Clone culture
  ("culture_7",  "<culture_7>", 0, 0.9, [], []),  ##@> Trandoshan culture
  ("culture_8",  "<culture_8>", 0, 0.9, [], []),  ##@> Jedi culture
  ("culture_9",  "<culture_9>", 0, 0.9, [], []),  ##@> Sith culture


 #("swadian_caravans","Swadian Caravans", 0, 0.5,[("outlaws",-0.8), ("dark_knights",-0.2)], []),
 #("vaegir_caravans","Vaegir Caravans", 0, 0.5,[("outlaws",-0.8), ("dark_knights",-0.2)], []),

  ("player_faction","Player Faction",0, 0.9, [], [], 0xC0C0FF),

## << Real Game factions Start Here >>
  ("player_supporters_faction","Player Faction",0, 0.9, [("player_faction",1.00),("outlaws",-0.05),("deserters", -0.02),("black_sun_pirates", -0.05),("blazing_claw_pirates", -0.05)], []),

  #Colors - 0xCC2211 = red, 0xDDDD33 = yellow, 0x33DDDD = blue, 0x33DD33 = green

  #SW - Swadia (Faction 1) = Galactic Empire
  ("galacticempire",
   "Galactic Empire", 0, 0.9,
   [("outlaws",-0.05),("deserters", -0.02),("black_sun_pirates", -0.05),("blazing_claw_pirates", -0.05),("rebelalliance", -0.4)],
  #[], 0xCC2211 # RED
   [], 0x33b3dd # BLUE old color: 33DDDD
  ), 

  #SW - Vaegir (Faction 2) = Rebal Alliance
  ("rebelalliance",
   "Rebel Alliance", 0, 0.9,
   [("outlaws",-0.05),("deserters", -0.02),("black_sun_pirates", -0.05),("blazing_claw_pirates", -0.05),("galacticempire", -0.4)],
  #[], 0x33DD33 #GREEN
   [], 0xce0b0b #RED
  ),

  #SW - Khergit Khanate (Faction 3) = Hutt Cartel
  ("huttcartel",
   "Hutt Cartel", 0, 0.9,
   [("outlaws",-0.05),("deserters", -0.02),("black_sun_pirates", -0.05),("blazing_claw_pirates", -0.05)], 
   [], 0xDD8844 #ORANGE old color: DD8844
  ),
  
 #4 = Nords
 #  ("faction_4",  "Faction of Nords",    0, 0.9, [("outlaws",-0.05),("deserters", -0.02),("black_sun_pirates", -0.05),("blazing_claw_pirates", -0.05)], [], 0xDDDD33),
 #5 = Rhodoks
 #  ("faction_5",  "Faction of Rhodoks",  0, 0.9, [("outlaws",-0.05),("deserters", -0.02),("black_sun_pirates", -0.05),("blazing_claw_pirates", -0.05)], [], 0x33DDDD),

## << Real Game factions End Here >>
 #("factions_end","factions_end", 0, 0,[], []),

  ("robber_knights",  "<robber_knights>", 0, 0.1, [], []),

  ("bountyhunters",
   "Bounty Hunters",0, 0.5,
   [("outlaws",-0.6),("player_faction",0.1)],
   []
  ),
  ("deserters",
   "Deserters", 0, 0.5,
   [("bountyhunters",-0.6),("merchants",-0.5),("player_faction",-0.1)],
   [], 0xFF99CC
  ),
  ("black_sun_pirates",
   "Black Sun Pirates", 0, 0.5,
   [("commoners",-0.2),("merchants",-0.5),("bountyhunters",-0.6),("player_faction",-0.15)],
   [], 0xFFFF66
  ),
  ("blazing_claw_pirates",
   "Blazing Claw Pirates", 0, 0.5,
   [("commoners",-0.2),("merchants",-0.5),("bountyhunters",-0.6),("player_faction",-0.15)],
   [], 0xFFFF66
  ),

 #("undeads","Undeads", max_player_rating(-30), 0.5,[("commoners",-0.7),("player_faction",-0.5)], []),
  ("enemy","<enemy_placeholder>", max_player_rating(-30), 0.5,[("commoners",-0.7),("player_faction",-0.5)], []),
  ("slavers","Slavers", 0, 0.1, [], []),
 #("peasant_rebels","Peasant Rebels", 0, 1.0,[("noble_refugees",-1.0),("player_faction",-0.4)], []),
 #("noble_refugees","Noble Refugees", 0, 0.5,[], []),
]
