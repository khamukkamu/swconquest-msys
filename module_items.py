# S T A R   W A R S   C O N Q U E S T   M O D U L E   S Y S T E M 
# / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /
# By Taleworlds, HokieBT, MartinF and Swyter - Do not use/copy without permission

from ID_factions import *
from header_items import  *
from module_constants import *
from module_factions import *
from header_operations import *
from header_triggers import *

####################################################################################################################
#  Each item record contains the following fields:
#  1) Item id: used for referencing items in other files.
#     The prefix itm_ is automatically added before each item id.
#  2) Item name. Name of item as it'll appear in inventory window
#  3) List of meshes.  Each mesh record is a tuple containing the following fields:
#    3.1) Mesh name.
#    3.2) Modifier bits that this mesh matches.
#     Note that the first mesh record is the default.
#  4) Item flags. See header_items.py for a list of available flags.
#  5) Item capabilities. Used for which animations this item is used with. See header_items.py for a list of available flags.
#  6) Item value.
#  7) Item stats: Bitwise-or of various stats about the item such as:
#      weight, abundance, difficulty, head_armor, body_armor,leg_armor, etc...
#  8) Modifier bits: Modifiers that can be applied to this item.
#  9) [Optional] Triggers: List of simple triggers to be associated with the item.
####################################################################################################################

# Some constants for ease of use.
imodbits_none          = 0
imodbits_horse_basic   = imodbit_swaybacked|imodbit_lame|imodbit_spirited|imodbit_heavy|imodbit_stubborn
imodbits_cloth         = imodbit_tattered | imodbit_ragged | imodbit_sturdy | imodbit_thick | imodbit_hardened
imodbits_armor         = imodbit_rusty | imodbit_battered | imodbit_crude | imodbit_thick | imodbit_reinforced |imodbit_lordly
imodbits_plate         = imodbit_cracked | imodbit_rusty | imodbit_battered | imodbit_crude | imodbit_thick | imodbit_reinforced |imodbit_lordly
imodbits_polearm       = imodbit_cracked | imodbit_bent | imodbit_balanced
imodbits_shield        = imodbit_cracked | imodbit_battered |imodbit_thick | imodbit_reinforced
imodbits_sword         = imodbit_rusty | imodbit_chipped | imodbit_balanced |imodbit_tempered
imodbits_sword_high    = imodbit_rusty | imodbit_chipped | imodbit_balanced |imodbit_tempered|imodbit_masterwork
imodbits_axe           = imodbit_rusty | imodbit_chipped | imodbit_balanced |imodbit_heavy
imodbits_mace          = imodbit_rusty | imodbit_chipped | imodbit_balanced |imodbit_heavy
imodbits_pick          = imodbit_rusty | imodbit_chipped | imodbit_balanced | imodbit_heavy
imodbits_bow           = imodbit_cracked | imodbit_bent | imodbit_strong |imodbit_masterwork
imodbits_crossbow      = imodbit_cracked | imodbit_bent | imodbit_masterwork
imodbits_missile       = imodbit_bent | imodbit_large_bag
imodbits_thrown        = imodbit_bent | imodbit_heavy| imodbit_balanced| imodbit_large_bag

imodbits_horse_good    = imodbit_spirited|imodbit_heavy
imodbits_cloth_good    = imodbit_sturdy | imodbit_thick | imodbit_hardened
imodbits_good          = imodbit_sturdy | imodbit_thick | imodbit_hardened | imodbit_reinforced
imodbits_bad           = imodbit_rusty | imodbit_chipped | imodbit_tattered | imodbit_ragged | imodbit_cracked | imodbit_bent

#SW - added imodbits for guns, lightsaber
imodbits_gun           = imodbit_cracked | imodbit_rusty | imodbit_balanced | imodbit_heavy
imodbits_lightsaber    =                   imodbit_rusty | imodbit_balanced | imodbit_heavy | imodbit_tempered   | imodbit_chipped
imodbits_speeder       = imodbit_cracked |                 imodbit_battered | imodbit_heavy | imodbit_reinforced | imodbit_lame    | imodbit_spirited | imodbit_swaybacked | imodbit_champion
imodbits_speeder_basic = imodbit_cracked |                 imodbit_battered | imodbit_heavy | imodbit_reinforced | imodbit_lame    | imodbit_spirited | imodbit_swaybacked
imodbits_droid         = imodbit_cracked | imodbit_rusty | imodbit_battered | imodbit_thick | imodbit_reinforced
imodbits_ammo          = imodbit_large_bag

#Swyter's Muzzleflare system
muzzleflare_system = [
  #(position_move_x,pos1, -24), #up *-1
  #(position_move_y,pos1,  70), #length
  #(position_move_z,pos1,   0),(particle_system_burst,"psys_swy_muzzleflare",pos1,1) #,(set_current_color,255, 0, 255),(add_point_light, 10, 30)
]

#lightsaber price bonus--some balancing comes in handy in more civilized times
lsbr_vluemul = 1.7

# Replace winged mace/spiked mace with: Flanged mace / Knobbed mace?
# Fauchard (majowski glaive) 

# Kham Item factionization

empire_fac = [fac_galacticempire]
rebel_fac = [fac_rebelalliance]
hutt_fac = [fac_huttcartel]
force_fac = [fac_culture_8, fac_culture_9]
jedi_fac = [fac_culture_8]
sith_fac = [fac_culture_9]

items = [
# item_name, mesh_name, item_properties, item_capabilities, slot_no, cost, bonus_flags, weapon_flags, scale, view_dir, pos_offset
#SW - modified the no_item to be transparent so practice_swords wouldn't appear everywhere
 ["no_item","<dummy>", [("_",0)], 0,0,0,0,imodbits_none],
 ["horse_meat","Horse Meat", [("raw_meat",0)], itp_type_goods|itp_consumable|itp_food, 0, 12,weight(40)|food_quality(30)|max_ammo(40),imodbits_none],
 ["practice_boots", "Practice Boots", [("boot_slim_black_reinforced_L",0),("boot_slim_black_reinforced_inventory",ixmesh_inventory)], itp_type_foot_armor |itp_civilian  | itp_attach_armature,0, 11 , weight(1)|abundance(100)|head_armor(0)|body_armor(0)|leg_armor(10), imodbits_cloth ],

#SW - increased arena_tunic armor stats
["arena_tunic_white", "Arena Tunic White ", [("arena_tunicW_padded",0)], itp_type_body_armor |itp_covers_legs ,0, 50 , weight(2)|abundance(100)|head_armor(12)|body_armor(35)|leg_armor(12), imodbits_cloth ],
["arena_tunic_red", "Arena Tunic Red", [("arena_tunicR_padded",0)], itp_type_body_armor |itp_covers_legs ,0, 50 , weight(2)|abundance(100)|head_armor(12)|body_armor(35)|leg_armor(12), imodbits_cloth ], 
["arena_tunic_blue", "Arena Tunic Blue", [("arena_tunicB_padded",0)], itp_type_body_armor |itp_covers_legs ,0, 50 , weight(2)|abundance(100)|head_armor(12)|body_armor(35)|leg_armor(12), imodbits_cloth ], 
["arena_tunic_green", "Arena Tunic Green", [("arena_tunicG_padded",0)], itp_type_body_armor |itp_covers_legs ,0, 50 , weight(2)|abundance(100)|head_armor(12)|body_armor(35)|leg_armor(12), imodbits_cloth ],
["arena_tunic_yellow", "Arena Tunic Yellow", [("arena_tunicY_padded",0)], itp_type_body_armor |itp_covers_legs ,0, 50 , weight(2)|abundance(100)|head_armor(12)|body_armor(35)|leg_armor(12), imodbits_cloth ],

# A treatise on The Method of Mechanical Theorems Archimedes
 
#SW - modified books to be holocrons 
#This book must be at the beginning of readable books
 ["book_tactics","Tactics Holocron", [("holocron_new_a",0)], itp_type_book, 0, 4000,weight(2)|abundance(100),imodbits_none], 
 ["book_persuasion","Persuasion Holocron", [("holocron_new_b",0)], itp_type_book, 0, 5000,weight(2)|abundance(100),imodbits_none],
 ["book_leadership","Leadership Holocron", [("holocron_new_c",0)], itp_type_book, 0, 4200,weight(2)|abundance(100),imodbits_none],
 ["book_intelligence","Intelligence Holocron", [("holocron_new_d",0)], itp_type_book, 0, 2900,weight(2)|abundance(100),imodbits_none],
 ["book_trade","Trade Holocron", [("holocron_new_e",0)], itp_type_book, 0, 3100,weight(2)|abundance(100),imodbits_none],
 ["book_weapon_mastery", "Weapon Mastery Holocron", [("holocron_new_a",0)], itp_type_book, 0, 4200,weight(2)|abundance(100),imodbits_none],
 ["book_engineering","Engineering Holocron", [("holocron_new_b",0)], itp_type_book, 0, 4000,weight(2)|abundance(100),imodbits_none], 
 
#Reference books
#This book must be at the beginning of reference books
 ["book_wound_treatment_reference","2-1B Medical Droid", [("medical_droid",0)], itp_type_book, 0, 3500,weight(2)|abundance(100),imodbits_none],
 ["book_first_aid_reference","Medical Database", [("medical_database",0)], itp_type_book, 0, 3500,weight(2)|abundance(100),imodbits_none], 
 #["book_power_strike_reference","Mandalorian Crushgaunts", [("gauntlet_a_L",0)], itp_type_book, 0, 3500,weight(1)|abundance(100),imodbits_none],
 ["book_tactics_reference","Dejarik Table", [("holochess_set",0)], itp_type_book, 0, 3500,weight(1)|abundance(100),imodbits_none], 
 ["book_trade_reference","Sabacc Cards", [("sabacc_cards",0)], itp_type_book, 0, 3500,weight(1)|abundance(100),imodbits_none],
 ["book_ironflesh_reference","Personal Shield", [("personal_shield",0)], itp_type_book, 0, 3500,weight(1)|abundance(100),imodbits_none],
 ["book_horse_archery_reference","Laser Scope", [("laser_scope",0)], itp_type_book, 0, 3500,weight(1)|abundance(100),imodbits_none],
 ["book_training_reference","Training Remote", [("training_remote",0)], itp_type_book, 0, 3500,weight(2)|abundance(100),imodbits_none], 
 ["book_surgery_reference","Bacta Tank", [("bacta_tank_new",0)], itp_type_book, 0, 3500,weight(2)|abundance(100),imodbits_none], 
 

#foods (first one is smoked_fish)
 #SW - increased food quantity (ie, max_ammo) by 2x
  ["smoked_fish","Smoked Fish", [("smoked_fish",0)], itp_type_goods|itp_consumable|itp_food, 0, 49,weight(25)|abundance(110)|food_quality(50)|max_ammo(100),imodbits_none],
  ["dried_meat","Nerf Beef", [("smoked_meat",0)], itp_merchandise|itp_type_goods|itp_consumable|itp_food, 0, 72,weight(25)|abundance(100)|food_quality(70)|max_ammo(120),imodbits_none],
  ["cattle_meat","Nerf Meat", [("raw_meat",0)], itp_type_goods|itp_consumable|itp_food, 0, 103,weight(30)|abundance(100)|food_quality(80)|max_ammo(100),imodbits_none], 	#removed merch tag but didn't comment out since it may be used for scene props?
  ["bantha_steak","Bantha Steak", [("bantha_steak",0)], itp_merchandise|itp_type_goods|itp_consumable|itp_food, 0, 103,weight(30)|abundance(100)|food_quality(80)|max_ammo(100),imodbits_none], 
  ["pork","Pork", [("fried_pig",0)], itp_type_goods|itp_consumable|itp_food, 0, 85,weight(20)|abundance(100)|food_quality(70)|max_ammo(100),imodbits_none],
  ["bread","Bread", [("bread_a",0)], itp_type_goods|itp_consumable|itp_food, 0, 32,weight(25)|abundance(110)|food_quality(40)|max_ammo(100),imodbits_none],	#removed merch tag but didn't comment out since it may be used for scene props?
  ["vagnerian_canape","Vagnerian Canape", [("vagnerian_canape",0)], itp_merchandise|itp_type_goods|itp_consumable|itp_food, 0, 150,weight(5)|abundance(70)|food_quality(70)|max_ammo(25),imodbits_none],
  ["carbohydrate_pack","Carbohydrate Pack", [("carbohydrate_food",0)], itp_merchandise|itp_type_goods|itp_consumable|itp_food, 0, 20,weight(15)|abundance(110)|food_quality(40)|max_ammo(150),imodbits_none], 
  ["apples","Apples", [("apple_basket",0)], itp_type_goods|itp_consumable|itp_food, 0, 44,weight(35)|abundance(110)|food_quality(40)|max_ammo(100),imodbits_none],	#removed merch tag but didn't comment out since it may be used for scene props?
  ["blue_milk","Blue Milk", [("blue_milk",0)], itp_merchandise|itp_type_goods|itp_consumable|itp_food, 0, 100,weight(25)|abundance(110)|food_quality(60)|max_ammo(80),imodbits_none],
  ["mujo_fruit","Mujo Fruit", [("mujo_fruit",0)], itp_merchandise|itp_type_goods|itp_consumable|itp_food, 0, 44,weight(35)|abundance(110)|food_quality(40)|max_ammo(100),imodbits_none],
  ["cheese","Christophsis cheese", [("cheese_b",0)], itp_merchandise|itp_type_goods|itp_consumable|itp_food, 0, 95,weight(15)|abundance(110)|food_quality(40)|max_ammo(60),imodbits_none],
  ["chicken","Chicken", [("chicken_roasted",0)], itp_type_goods|itp_consumable|itp_food, 0, 75,weight(15)|abundance(110)|food_quality(40)|max_ammo(100),imodbits_none],	#removed merch tag but didn't comment out since it may be used for scene props?
  ["protein_pack","Protein Pack", [("protein_food",0)], itp_merchandise|itp_type_goods|itp_consumable|itp_food, 0, 20,weight(15)|abundance(110)|food_quality(40)|max_ammo(150),imodbits_none], 
  ["honey","Honey", [("honey_pot",0)], itp_merchandise|itp_type_goods|itp_consumable|itp_food, 0, 136,weight(5)|abundance(110)|food_quality(40)|max_ammo(40),imodbits_none],
  ["sausages","Nerf sausages", [("sausages",0)], itp_merchandise|itp_type_goods|itp_consumable|itp_food, 0, 60,weight(15)|abundance(110)|food_quality(40)|max_ammo(80),imodbits_none],
  ["cabbages","Cabbages", [("cabbage",0)], itp_type_goods|itp_consumable|itp_food, 0, 30,weight(25)|abundance(110)|food_quality(40)|max_ammo(100),imodbits_none],	#removed merch tag but didn't comment out since it may be used for scene props?
  ["bristle_melon","Bristle Melon", [("bristlemelon",0)], itp_merchandise|itp_type_goods|itp_consumable|itp_food, 0, 30,weight(25)|abundance(110)|food_quality(40)|max_ammo(100),imodbits_none],
  ["butter","Bantha butter", [("butter_pot",0)], itp_merchandise|itp_type_goods|itp_consumable|itp_food, 0, 150,weight(12)|abundance(110)|food_quality(40)|max_ammo(60),imodbits_none],

  #@> New Consumable supplies by Vector Dalon
 ["Container_spice_1","Shipment of Ryll Spice",        [("Container_spice_1",0)], itp_merchandise|itp_type_goods, 0, 150, weight(32)|abundance(110),imodbits_none],
 ["Container_spice_2","Shipment of Gree Spice",        [("Container_spice_2",0)], itp_merchandise|itp_type_goods, 0, 150, weight(32)|abundance(70), imodbits_none],
 ["Container_spice_3","Shipment of Glitterstim Spice", [("Container_spice_3",0)], itp_merchandise|itp_type_goods, 0, 150, weight(32)|abundance(40), imodbits_none],

 ["Container_food_1","Shipment of Vegetables",    [("Container_food_1",0)], itp_merchandise|itp_type_goods|itp_consumable|itp_food, 0, 190,weight(18)|abundance(111)|food_quality(40)|max_ammo(260),imodbits_none],
 ["Container_food_2","Shipment of Carbohydrates", [("Container_food_2",0)], itp_merchandise|itp_type_goods|itp_consumable|itp_food, 0, 150,weight(12)|abundance(110)|food_quality(60)|max_ammo(200),imodbits_none],
 ["Container_food_3","Shipment of Protein",       [("Container_food_3",0)], itp_merchandise|itp_type_goods|itp_consumable|itp_food, 0, 140,weight(10)|abundance(110)|food_quality(80)|max_ammo(170),imodbits_none],

 ["Container_metal_1","Shipment of Beskar bars",    [("Container_metal_1",0)], itp_merchandise|itp_type_goods, 0, 150, weight(40)|abundance(50), imodbits_none],
 ["Container_metal_2","Shipment of Durasteel bars", [("Container_metal_2",0)], itp_merchandise|itp_type_goods, 0, 180, weight(60)|abundance(110),imodbits_none],
 ["Container_metal_3","Shipment of Bronzium bars",  [("Container_metal_3",0)], itp_merchandise|itp_type_goods, 0, 210, weight(70)|abundance(70), imodbits_none],
 
 ["Container_death_sticks","Carton of Death Sticks", [("Container_death_sticks",0)], itp_merchandise|itp_type_goods, 0, 90, weight(6)|abundance(110),imodbits_none],

 ["Container_drink_1","Shipment of Water",      [("Container_drink_1",0)], itp_merchandise|itp_type_goods|itp_consumable|itp_food, 0,  60,weight(12)|abundance(110)|food_quality(30)|max_ammo(220),imodbits_none],
 ["Container_drink_2","Shipment of Black Ale",  [("Container_drink_2",0)], itp_merchandise|itp_type_goods|itp_consumable|itp_food, 0,  90,weight(14)|abundance(110)|food_quality(60)|max_ammo(150),imodbits_none],
 ["Container_drink_3","Shipment of Juri juice", [("Container_drink_3",0)], itp_merchandise|itp_type_goods|itp_consumable|itp_food, 0, 240,weight(20)|abundance(60)| food_quality(80)|max_ammo(60),imodbits_none],

 ["Carbonite_Tibanna","Carbonite Shipment of Tibanna Gas", [("Carbonite_Tibanna",0)], itp_merchandise|itp_type_goods, 0, 150,weight(12)|abundance(110),imodbits_none],
 ["Container_ore",    "Ore container",                     [("Container_ore",0)],     itp_merchandise|itp_type_goods, 0,  87,weight(56)|abundance(340),imodbits_none],

 ["butter","Bantha butter", [("butter_pot",0)], itp_merchandise|itp_type_goods|itp_consumable|itp_food, 0, 150,weight(12)|abundance(110)|food_quality(40)|max_ammo(60),imodbits_none],

 
 
#other trade goods (first one is wine)
  ["wine","Mandalorian wine", [("amphora_slim",0)], itp_merchandise|itp_type_goods|itp_consumable, 0, 141,weight(30)|abundance(60)|max_ammo(50),imodbits_none],
  ["ale","Corellian ale", [("ale_barrel",0)], itp_merchandise|itp_type_goods|itp_consumable, 0, 84,weight(30)|abundance(70)|max_ammo(50),imodbits_none],
  ["spice","Spice", [("spice_sack",0)], itp_merchandise|itp_type_goods, 0, 880,weight(40)|abundance(25),imodbits_none],
  ["salt","Bassel sea salt", [("salt_sack",0)], itp_merchandise|itp_type_goods, 0, 255,weight(50)|abundance(100),imodbits_none],
  ["grain","Wheat", [("wheat_sack",0)], itp_merchandise|itp_type_goods|itp_consumable, 0, 77,weight(50)|abundance(110)|food_quality(40)|max_ammo(50),imodbits_none],
  ["flour","Flour", [("salt_sack",0)], itp_merchandise|itp_type_goods|itp_consumable, 0, 91,weight(50)|abundance(100)|food_quality(45)|max_ammo(50),imodbits_none],
  ["iron","Durasteel", [("iron",0)], itp_merchandise|itp_type_goods, 0,264,weight(60)|abundance(60),imodbits_none],
  ["bacta_injector","Bacta Injector", [("bacta_injector",0)], itp_merchandise|itp_type_goods, 0,3000,weight(5)|abundance(40),imodbits_none],
  ["bacta_capsule","Bacta Capsule", [("bacta_capsule",0)], itp_merchandise|itp_type_goods, 0,500,weight(2)|abundance(100),imodbits_none], 
  ["binocular","Macrobinoculars", [("macrobinoculars",0)], itp_merchandise|itp_type_goods, 0,3000,weight(3)|abundance(40),imodbits_none], 
  ["jetpack","Jetpack", [("macrobinoculars",0)], itp_unique, 0,6000,weight(6)|abundance(35),imodbits_none],  
  ["oil","Oil", [("oil",0)], itp_merchandise|itp_type_goods, 0, 484,weight(50)|abundance(60),imodbits_none],
  ["pottery","Geonosian pottery", [("jug",0)], itp_merchandise|itp_type_goods, 0, 126,weight(50)|abundance(90),imodbits_none],
  ["linen","Lashaa silk", [("linen",0)], itp_merchandise|itp_type_goods, 0, 250,weight(40)|abundance(90),imodbits_none],
  ["furs","Ewok Furs", [("fur_pack",0)], itp_merchandise|itp_type_goods, 0, 391,weight(40)|abundance(90),imodbits_none],
  ["wookiee_fur","Wookiee Pelt", [("wookiee_fur",0)], itp_type_goods|itp_always_loot, 0, 250,weight(10)|abundance(60),imodbits_none], 	#no merch, only can get by killing wookiees
  ["trandoshan_skin","Trandoshan Skin", [("trandoshan_skin",0)], itp_type_goods|itp_always_loot, 0, 250,weight(10)|abundance(60),imodbits_none], 	#no merch, only can get by killing wookiees
  ["droid_parts","Droid Parts", [("robot_parts",0)], itp_merchandise|itp_type_goods|itp_always_loot, 0, 200,weight(15)|abundance(60),imodbits_none], 	#also given to droids
  ["wool","Nerf wool", [("wool_sack",0)], itp_merchandise|itp_type_goods, 0, 130,weight(40)|abundance(90),imodbits_none],
  ["velvet","Naboo Velvet", [("velvet",0)], itp_merchandise|itp_type_goods, 0, 1025,weight(40)|abundance(30),imodbits_none],
  ["tools","Hydrospanners", [("hydrospanner",0)], itp_merchandise|itp_type_goods, 0, 410,weight(50)|abundance(90),imodbits_none],
#@> New Trade Suplies by Vector Dalon
 # ["tools","Hydrospanners", [("hydrospanner",0)], itp_merchandise|itp_type_goods, 0, 410,weight(50)|abundance(90),imodbits_none],
 # ["tools","Hydrospanners", [("hydrospanner",0)], itp_merchandise|itp_type_goods, 0, 410,weight(50)|abundance(90),imodbits_none],
 # ["tools","Hydrospanners", [("hydrospanner",0)], itp_merchandise|itp_type_goods, 0, 410,weight(50)|abundance(90),imodbits_none],
 # ["tools","Hydrospanners", [("hydrospanner",0)], itp_merchandise|itp_type_goods, 0, 410,weight(50)|abundance(90),imodbits_none],

#************************************************************************************************
# ITEMS before this point are hardcoded into item_codes.h and their order should not be changed!
#************************************************************************************************

# Quest Items

 ["siege_supply","Supplies", [("ale_barrel",0)], itp_type_goods, 0, 96,weight(40)|abundance(70),imodbits_none],
 ["quest_wine","Wine", [("amphora_slim",0)], itp_type_goods, 0, 46,weight(40)|abundance(60)|max_ammo(50),imodbits_none],
 ["quest_ale","Ale", [("ale_barrel",0)], itp_type_goods, 0, 31,weight(40)|abundance(70)|max_ammo(50),imodbits_none],

 
#whalebone crossbow, yew bow, war bow, arming sword 
#SW - removed merchandise tag since bolts/arrows might be used for ammo for other star wars weapons
 # ["arrows","Arrows", [("arrow",0),("flying_missile",ixmesh_flying_ammo),("quiver", ixmesh_carry)], itp_type_arrows, itcf_carry_quiver_back, 72,weight(3)|abundance(160)|weapon_length(95)|thrust_damage(1,pierce)|max_ammo(30),imodbits_missile],
 # ["khergit_arrows","Khergit Arrows", [("arrow_b",0),("flying_missile",ixmesh_flying_ammo),("quiver_b", ixmesh_carry)], itp_type_arrows, itcf_carry_quiver_back_right, 410,weight(3.5)|abundance(30)|weapon_length(95)|thrust_damage(3,pierce)|max_ammo(30),imodbits_missile],
 # ["barbed_arrows","Barbed Arrows", [("barbed_arrow",0),("flying_missile",ixmesh_flying_ammo),("quiver_d", ixmesh_carry)], itp_type_arrows, itcf_carry_quiver_back_right, 124,weight(3)|abundance(70)|weapon_length(95)|thrust_damage(2,pierce)|max_ammo(30),imodbits_missile],
 # ["bodkin_arrows","Bodkin Arrows", [("piercing_arrow",0),("flying_missile",ixmesh_flying_ammo),("quiver_c", ixmesh_carry)], itp_type_arrows, itcf_carry_quiver_back_right, 350,weight(3)|abundance(50)|weapon_length(91)|thrust_damage(3,pierce)|max_ammo(29),imodbits_missile],
 # ["bolts","Bolts", [("bolt",0),("flying_missile",ixmesh_flying_ammo),("bolt_bag", ixmesh_carry),("bolt_bag_b", ixmesh_carry|imodbit_large_bag)], itp_type_bolts, itcf_carry_quiver_right_vertical, 64,weight(2.25)|abundance(90)|weapon_length(55)|thrust_damage(1,pierce)|max_ammo(25),imodbits_missile],
 # ["steel_bolts","Steel Bolts", [("bolt",0),("flying_missile",ixmesh_flying_ammo),("bolt_bag_c", ixmesh_carry)], itp_type_bolts, itcf_carry_quiver_right_vertical, 210,weight(2.5)|abundance(20)|weapon_length(55)|thrust_damage(2,pierce)|max_ammo(25),imodbits_missile],
#SW - commented out cartridges
# ["cartridges","Cartridges", [("cartridge_a",0)], itp_type_bullets|itp_merchandise, 0, 41,weight(2.25)|abundance(90)|weapon_length(3)|thrust_damage(1,pierce)|max_ammo(40),imodbits_missile],

["pilgrim_disguise", "Pilgrim Disguise", [("pilgrim_outfit",0)], 0|itp_type_body_armor|itp_covers_legs|itp_civilian ,0, 25, weight(2)   |abundance(100)|head_armor(0)|body_armor(19)|leg_armor(8)|difficulty(0), imodbits_cloth],
["pilgrim_hood",     "Pilgrim Hood",     [("pilgrim_hood",0)],   0|itp_type_head_armor|itp_civilian,                 0, 35, weight(1.25)|abundance(100)|head_armor(14)|body_armor(0)|leg_armor(0)|difficulty(0), imodbits_cloth],

# ARMOR
#handwear
["leather_gloves","Leather Gloves", [("lthr_glove_L",0)], itp_merchandise|itp_type_hand_armor|itp_civilian,0, 
 18, weight(0.25)|abundance(120)|body_armor(2)|difficulty(0),imodbits_cloth],

#footwear
["wrapping_boots", "Wrapping Boots", [("jawa_boots",0)], itp_merchandise| itp_type_foot_armor |itp_civilian | itp_attach_armature ,0,
 20 , weight(1)|abundance(100)|head_armor(0)|body_armor(0)|leg_armor(3)|difficulty(0) ,imodbits_cloth ],
["blue_hose", "Blue Hose", [("light_leather_boots",0)], itp_merchandise| itp_type_foot_armor |itp_civilian | itp_attach_armature ,0,
 40 , weight(1)|abundance(100)|head_armor(0)|body_armor(0)|leg_armor(5)|difficulty(0) ,imodbits_cloth ],
["hide_boots", "Hide Boots", [("grey_boots",0)], itp_merchandise| itp_type_foot_armor |itp_civilian  | itp_attach_armature,0,
 90 , weight(1)|abundance(100)|head_armor(0)|body_armor(0)|leg_armor(10)|difficulty(0) ,imodbits_cloth ],
["ankle_boots", "Ankle Boots", [("boot_slim_black_reinforced2_L",0),("boot_slim_black_reinforced2_inventory",ixmesh_inventory)], itp_merchandise| itp_type_foot_armor |itp_civilian,0,
 110 , weight(1)|abundance(100)|head_armor(0)|body_armor(0)|leg_armor(12)|difficulty(0) ,imodbits_cloth ],
["nomad_boots", "Nomad Boots", [("black_boots",0)], itp_merchandise| itp_type_foot_armor  |itp_civilian | itp_attach_armature,0,
 128 , weight(1.25)|abundance(100)|head_armor(0)|body_armor(0)|leg_armor(14)|difficulty(0) ,imodbits_cloth ],


#bodywear
["dress", "Dress", [("dress",0)], itp_merchandise| itp_type_body_armor|itp_covers_legs|itp_civilian, 0, 
 70 , weight(1)|abundance(100)|head_armor(0)|body_armor(6)|leg_armor(2)|difficulty(0) ,imodbits_cloth ],
["blue_dress", "Blue Dress", [("blue_dress",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs|itp_civilian, 0, 
 70 , weight(1)|abundance(100)|head_armor(0)|body_armor(6)|leg_armor(2)|difficulty(0) ,imodbits_cloth ],
["peasant_dress", "Colonist Dress", [("peasant_dress_b",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs|itp_civilian, 0, 
 70 , weight(1)|abundance(100)|head_armor(0)|body_armor(6)|leg_armor(2)|difficulty(0) ,imodbits_cloth ], 
["woolen_dress", "Woolen Dress", [("woolen_dress",0)], itp_merchandise| itp_type_body_armor|itp_civilian  |itp_covers_legs ,0,
 83 , weight(1.75)|abundance(100)|head_armor(0)|body_armor(8)|leg_armor(2)|difficulty(0) ,imodbits_cloth ],
["courtly_outfit", "Courtly Outfit", [("nobleman_outf",0)], itp_type_body_armor|itp_covers_legs|itp_civilian, 0, 
 200 , weight(4)|abundance(100)|head_armor(0)|body_armor(14)|leg_armor(10)|difficulty(0) ,imodbits_cloth ],
["nobleman_outfit", "Nobleman Outfit", [("nobleman_outfit_b",0)], itp_type_body_armor|itp_covers_legs|itp_civilian, 0, 
 270 , weight(4)|abundance(100)|head_armor(0)|body_armor(15)|leg_armor(12)|difficulty(0) ,imodbits_cloth ], 
["leather_armor", "Leather Armor", [("lthr_armor_a",0)], itp_merchandise|itp_type_body_armor |itp_covers_legs, 0, 
 110 , weight(7)|abundance(100)|head_armor(0)|body_armor(18)|leg_armor(0)|difficulty(0) ,imodbits_cloth ],
["shirt", "Shirt", [("shirt",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs|itp_civilian ,0,
 40 , weight(1)|abundance(100)|head_armor(0)|body_armor(5)|leg_armor(0)|difficulty(0) ,imodbits_cloth ],
["linen_tunic", "Linen Tunic", [("linen_tunic",0)], itp_merchandise| itp_type_body_armor |itp_civilian |itp_covers_legs ,0,
 60 , weight(1)|abundance(100)|head_armor(0)|body_armor(6)|leg_armor(1)|difficulty(0) ,imodbits_cloth ],
["short_tunic", "Rich Tunic", [("cvl_costume_a",0)], itp_merchandise| itp_type_body_armor |itp_civilian |itp_covers_legs ,0,
 70 , weight(1)|abundance(100)|head_armor(0)|body_armor(7)|leg_armor(1)|difficulty(0) ,imodbits_cloth ],
["robe", "Robe", [("robe",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs |itp_civilian,0,
 125 , weight(1.5)|abundance(100)|head_armor(0)|body_armor(8)|leg_armor(6)|difficulty(0) ,imodbits_cloth ],
["coarse_tunic", "Coarse Tunic", [("coarse_tunic",0)], itp_merchandise| itp_type_body_armor |itp_civilian |itp_covers_legs ,0,
 150 , weight(2)|abundance(100)|head_armor(0)|body_armor(11)|leg_armor(6)|difficulty(0) ,imodbits_cloth ],
["leather_apron", "Leather Apron", [("leather_apron",0)], itp_merchandise| itp_type_body_armor |itp_civilian |itp_covers_legs ,0,
 160 , weight(3)|abundance(100)|head_armor(0)|body_armor(12)|leg_armor(7)|difficulty(0) ,imodbits_cloth ],
["tabard", "Tabard", [("tabard_a",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs |itp_civilian,0,
 170 , weight(3)|abundance(100)|head_armor(0)|body_armor(14)|leg_armor(6)|difficulty(0) ,imodbits_cloth ],
["leather_vest", "Leather Vest", [("leather_vest",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs|itp_civilian ,0,
 180 , weight(4)|abundance(100)|head_armor(0)|body_armor(15)|leg_armor(7)|difficulty(0) ,imodbits_cloth ],

#SW - removed merchandise tag from gambesons since it was used for armor_faction but it still equipped for some of the town mayors/weaponsmiths/etc
["gambeson", "Gambeson", [("white_gambeson",0)], itp_type_body_armor|itp_covers_legs|itp_civilian,0,
 200 , weight(5)|abundance(100)|head_armor(0)|body_armor(20)|leg_armor(5)|difficulty(0) ,imodbits_cloth ],
["blue_gambeson", "Blue Gambeson", [("blue_gambeson",0)], itp_type_body_armor|itp_covers_legs|itp_civilian,0,
 210 , weight(5)|abundance(100)|head_armor(0)|body_armor(21)|leg_armor(5)|difficulty(0) ,imodbits_cloth ],
["red_gambeson", "Red Gambeson", [("red_gambeson",0)], itp_type_body_armor|itp_covers_legs|itp_civilian,0,
 210 , weight(5)|abundance(100)|head_armor(0)|body_armor(21)|leg_armor(5)|difficulty(0) ,imodbits_cloth ],
["padded_cloth", "Padded Cloth", [("aketon_a",0)], itp_merchandise| itp_type_body_armor  |itp_covers_legs ,0,
 170 , weight(11)|abundance(100)|head_armor(0)|body_armor(22)|leg_armor(6)|difficulty(0) ,imodbits_cloth ],
["leather_jerkin", "Leather Jerkin", [("leather_jerkin",0)], itp_merchandise| itp_type_body_armor |itp_civilian |itp_covers_legs ,0,
 230 , weight(6)|abundance(100)|head_armor(0)|body_armor(23)|leg_armor(6)|difficulty(0) ,imodbits_cloth ],
["padded_leather", "Padded Leather", [("padded_leather",0)], itp_type_body_armor  |itp_covers_legs|itp_civilian,0,
 250 , weight(12)|abundance(100)|head_armor(0)|body_armor(27)|leg_armor(10)|difficulty(0) ,imodbits_cloth ],

["straw_hat", "Straw Hat", [("straw_hat",0)],itp_merchandise|itp_type_head_armor|itp_civilian,0,9, weight(1)|abundance(100)|head_armor(2)|body_armor(0)|leg_armor(0)|difficulty(0),imodbits_cloth],
["common_hood", "Hood", [("hood_a",0),("hood_b",0),("hood_c",0),("hood_d",0)],itp_merchandise|itp_type_head_armor|itp_civilian,0,9, weight(1)|abundance(100)|head_armor(10)|body_armor(0)|leg_armor(0)|difficulty(0),imodbits_cloth],
["headcloth", "Headcloth", [("headcloth",0)], itp_merchandise| itp_type_head_armor  |itp_civilian ,0, 1 , weight(0.5)|abundance(100)|head_armor(4)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth ],
["woolen_hood", "Woolen Hood", [("woolen_hood",0)], itp_merchandise| itp_type_head_armor |itp_civilian  ,0, 4 , weight(1)|abundance(100)|head_armor(8)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth ],
["fur_hat", "Fur Hat", [("hat_fur_a",0)], itp_merchandise| itp_type_head_armor |itp_civilian  ,0, 4 , weight(0.5)|abundance(100)|head_armor(8)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth ],
["padded_coif", "Padded Coif", [("padded_coif",0)], itp_merchandise| itp_type_head_armor   ,0, 6 , weight(1)|abundance(100)|head_armor(11)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth ],
["woolen_cap", "Woolen Cap", [("woolen_cap",0)], itp_merchandise| itp_type_head_armor  |itp_civilian ,0, 2 , weight(1)|abundance(100)|head_armor(6)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth ],
["felt_hat", "Felt Hat", [("felt_hat_a",0),("felt_hat_b",imodbits_good)], itp_merchandise| itp_type_head_armor |itp_civilian,0, 4 , weight(1)|abundance(100)|head_armor(8)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth ],
["leather_cap", "Leather Cap", [("leather_cap",0)], itp_merchandise| itp_type_head_armor|itp_civilian ,0, 6 , weight(1)|abundance(100)|head_armor(10)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth ],
["arming_cap", "Arming Cap", [("linen_arming_cap",0)], itp_merchandise| itp_type_head_armor  |itp_civilian ,0, 6 , weight(1)|abundance(100)|head_armor(10)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth ],
["female_hood", "Lady's Hood", [("woolen_hood",0)], itp_merchandise| itp_type_head_armor |itp_civilian  ,0, 9 , weight(1)|abundance(100)|head_armor(10)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth ],


#WEAPONS

#SW - used in other parts of the code, removed merch flag
 ["wooden_stick",         "Wooden Stick", [("wooden_stick",0)], itp_type_one_handed_wpn| itp_primary, itc_scimitar, 4 , weight(2.5)|difficulty(0)|spd_rtng(99) | weapon_length(90)|swing_damage(13 , blunt) | thrust_damage(0 ,  pierce),imodbits_none ],

#SW - used in other parts of the code, removed merch flag
 ["club",         "Club", [("club",0)], itp_type_one_handed_wpn| itp_primary, itc_scimitar, 11 , weight(2.5)|difficulty(0)|spd_rtng(95) | weapon_length(95)|swing_damage(15 , blunt) | thrust_damage(0 ,  pierce),imodbits_none ],
#removed merch tag from sickle, cleaver, knife, butchering knife, dagger
["cleaver",         "Cleaver", [("cleaver",0)], itp_type_one_handed_wpn|itp_primary|itp_secondary|itp_no_parry, itc_cleaver, 3 , weight(1.5)|difficulty(0)|spd_rtng(103) | weapon_length(30)|swing_damage(24 , cut) | thrust_damage(0 ,  pierce),imodbits_none ],
["knife",         "Knife", [("peasant_knife",0)], itp_type_one_handed_wpn|itp_primary|itp_secondary|itp_no_parry, itc_dagger, 4 , weight(0.5)|difficulty(0)|spd_rtng(110) | weapon_length(40)|swing_damage(21 , cut) | thrust_damage(13 ,  pierce),imodbits_sword ],
["butchering_knife", "Butchering Knife", [("khyber_knife",0)], itp_type_one_handed_wpn|itp_primary|itp_secondary|itp_no_parry, itc_dagger, 13 , weight(0.75)|difficulty(0)|spd_rtng(108) | weapon_length(60)|swing_damage(24 , cut) | thrust_damage(17 ,  pierce),imodbits_sword ],
["hatchet",         "Hatchet", [("hatchet",0)], itp_type_one_handed_wpn| itp_primary|itp_secondary|itp_bonus_against_shield, itc_scimitar|itcf_carry_axe_left_hip, 3 , weight(2)|difficulty(0)|spd_rtng(97) | weapon_length(60)|swing_damage(23 , cut) | thrust_damage(0 ,  pierce),imodbits_axe ],

#used in other parts of the code, removed merch flag
 ["quarter_staff", "Quarter Staff", [("quarter_staff",0)], itp_type_polearm| itp_spear|itp_primary|itp_penalty_with_shield, itc_staff|itcf_carry_sword_back,
  60 , weight(2)|difficulty(0)|spd_rtng(104) | weapon_length(140)|swing_damage(20 , blunt) | thrust_damage(20 ,  blunt),imodbits_polearm ],


#RANGED
 ["throwing_axes", "Gamorrean Throwing Axes", [("francisca",0)], itp_type_thrown |itp_merchandise|itp_primary|itp_bonus_against_shield,itcf_throw_axe, 250, weight(5)|difficulty(0)|spd_rtng(99) | shoot_speed(20) | thrust_damage(38,cut)|max_ammo(18)|weapon_length(53),imodbits_thrown ],

#added merchandise flag
["rich_outfit", "Rich Outfit", [("merchant_outf",0)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_civilian   ,0, 
 160 , weight(4)|abundance(100)|head_armor(0)|body_armor(16)|leg_armor(4)|difficulty(0) ,imodbits_cloth ],

#used in other files, removed merch flag
["black_hood", "Black Hood", [("hood_black",0)], itp_type_head_armor   ,0, 
 60 , weight(2)|abundance(100)|head_armor(8)|body_armor(0)|leg_armor(0) ,imodbits_cloth ],
["light_leather", "Light Leather", [("light_leather",0)], itp_type_body_armor|itp_covers_legs|itp_merchandise   ,0, 
 280 , weight(5)|abundance(100)|head_armor(0)|body_armor(26)|leg_armor(7)|difficulty(0) ,imodbits_armor ],
["light_leather_boots",  "Light Leather Boots", [("light_leather_boots",0)], itp_type_foot_armor |itp_merchandise| itp_attach_armature,0, 
 140 , weight(1)|abundance(100)|head_armor(0)|body_armor(0)|leg_armor(15)|difficulty(0) ,imodbits_cloth ],


#====================================================================================================================

#SW - Star Wars items - many of the items are from the original Star Wars mod
#credits and readme file? would need to use extra_info script functionality
#["swc_readme", "Star Wars Calradia 0.5.3^^Credits:^  HokieBT - scripting, textures^  Hank - scripting, textures^etc...", [("book_a",0)], itp_type_thrown |itp_primary ,itcf_throw_knife, 0 , weight(2.0)|spd_rtng(80) | shoot_speed(30) | thrust_damage(4, blunt)|max_ammo(1)|weapon_length(0),imodbits_none ],

#common/shared items
["armors_begin", "<dummy>", [("_",0)], 0,0,0,0,imodbits_none],
# SW Handwear
["black_gloves","Black Gloves", [("black_glove_L",0)], itp_merchandise|itp_type_hand_armor|itp_civilian,0, 
#["black_gloves","Black Gloves", [("black_glove_w_cuff_L",0)], itp_merchandise|itp_type_hand_armor|itp_civilian,0, 
 28, weight(0.25)|abundance(100)|body_armor(3)|difficulty(0),imodbits_cloth], 
["black_gloves_long","Long Black Gloves", [("black_glove_long_L",0)], itp_merchandise|itp_type_hand_armor|itp_civilian,0, 
 38, weight(0.25)|abundance(80)|body_armor(4)|difficulty(0),imodbits_cloth],  
["right_hand_glove","Right Hand Glove", [("black_glove_rh_L",0),("black_glove_rh_R",ixmesh_inventory)], itp_merchandise|itp_type_hand_armor|itp_civilian,0, 
 28, weight(0.25)|abundance(60)|body_armor(3)|difficulty(0),imodbits_cloth],  
["grey_gloves","Grey Gloves", [("grey_glove_L",0)], itp_merchandise|itp_type_hand_armor|itp_civilian,0, 
 28, weight(0.25)|abundance(100)|body_armor(3)|difficulty(0),imodbits_cloth],
["darkgrey_gloves","Dark Grey Gloves", [("ArcTrooperGloves_L",0)], itp_merchandise|itp_type_hand_armor|itp_civilian,0, 
 28, weight(0.25)|abundance(100)|body_armor(3)|difficulty(0),imodbits_cloth], 
["lady_gloves","Lady Gloves", [("lady_glove_L",0)], itp_merchandise|itp_type_hand_armor|itp_civilian,0, 
 17, weight(0.25)|abundance(80)|body_armor(2)|difficulty(0),imodbits_cloth],
["mandalorian_crushgaunts","Mandalorian Crushgaunts", [("mandalorian_crushgaunts_L",0)], itp_merchandise|itp_type_hand_armor,0, 
 400, weight(0.3)|abundance(60)|body_armor(6)|difficulty(0),imodbits_none],

["imperial_royal_guard_gloves","Imperial Royal Guard Gloves", [("imperial_royal_guard_glove_L",0)], itp_merchandise|itp_type_hand_armor|itp_civilian,0, 
 28, weight(0.25)|abundance(40)|body_armor(3)|difficulty(0),imodbits_cloth, [], empire_fac],
["imperial_stormtrooper_gloves","Imperial Stormtrooper Gloves", [("stormie_glov_L",0)], itp_merchandise|itp_type_hand_armor|itp_civilian,0, 
 28, weight(0.25)|abundance(80)|body_armor(3)|difficulty(0),imodbits_cloth, [], empire_fac], 
["novatrooper_gloves","Novatrooper Gloves", [("stnova_glov_L",0)], itp_merchandise|itp_type_hand_armor|itp_civilian,0, 
 38, weight(0.25)|abundance(40)|body_armor(4)|difficulty(4),imodbits_cloth, [], empire_fac],
["incinerator_trooper_gloves","Incinerator Trooper Gloves", [("stincn_glov_L",0)], itp_merchandise|itp_type_hand_armor|itp_civilian,0, 
 43, weight(0.25)|abundance(40)|body_armor(4)|difficulty(6),imodbits_cloth, [], empire_fac],  
 
#clone gloves (w, g, b, r, y, o)
["clone_trooper_gloves_white","Clone Trooper Gloves", [("ArcTrooperWhite_glove_L",0)], itp_type_hand_armor|itp_civilian,0, 
 28, weight(0.25)|abundance(80)|body_armor(3)|difficulty(0),imodbits_cloth], 
["clone_trooper_gloves_green","Clone Trooper Gloves", [("ArcTrooperGreen_glove_L",0)], itp_type_hand_armor|itp_civilian,0, 
 28, weight(0.25)|abundance(80)|body_armor(3)|difficulty(0),imodbits_cloth], 
["clone_trooper_gloves_blue","Clone Trooper Gloves", [("ArcTrooperBlue_glove_L",0)], itp_type_hand_armor|itp_civilian,0, 
 28, weight(0.25)|abundance(80)|body_armor(3)|difficulty(0),imodbits_cloth], 
["clone_trooper_gloves_red","Clone Trooper Gloves", [("ArcTrooperRed_glove_L",0)], itp_type_hand_armor|itp_civilian,0, 
 28, weight(0.25)|abundance(80)|body_armor(3)|difficulty(0),imodbits_cloth], 
["clone_trooper_gloves_yellow","Clone Trooper Gloves", [("ArcTrooperYellow_glove_L",0)], itp_type_hand_armor|itp_civilian,0, 
 28, weight(0.25)|abundance(80)|body_armor(3)|difficulty(0),imodbits_cloth], 
["clone_trooper_gloves_orange","Clone Trooper Gloves", [("ArcTrooperOrange_glove_L",0)], itp_type_hand_armor|itp_civilian,0, 
 28, weight(0.25)|abundance(80)|body_armor(3)|difficulty(0),imodbits_cloth], 
 
#special gloves
["grey_gloves_with_bottle","Grey Gloves with Bottle", [("grey_glove_with_bottle_L",0)], itp_unique|itp_type_hand_armor|itp_civilian,0, 
 28, weight(0.25)|abundance(100)|body_armor(3)|difficulty(0),imodbits_cloth],
 
# SW Footwear
["leather_boots", "Leather Boots", [("boot_slim_brown_L",0),("boot_slim_brown_inventory",ixmesh_inventory)], itp_merchandise| itp_type_foot_armor  |itp_civilian,0, 
 108 , weight(1.25)|abundance(100)|head_armor(0)|body_armor(0)|leg_armor(12)|difficulty(0) ,imodbits_cloth ],
["leather_boots_reinforced", "Reinforced Leather Boots", [("boot_slim_brown_reinforced_L",0),("boot_slim_brown_reinforced_inventory",ixmesh_inventory)], itp_merchandise| itp_type_foot_armor  |itp_civilian,0, 
 208 , weight(1.75)|abundance(70)|head_armor(0)|body_armor(0)|leg_armor(18)|difficulty(0) ,imodbits_cloth ], 
["black_boots", "Black Boots", [("boot_slim_black_L",0),("boot_slim_black_inventory",ixmesh_inventory)], itp_merchandise| itp_type_foot_armor  |itp_civilian,0, 
 108 , weight(1.25)|abundance(100)|head_armor(0)|body_armor(0)|leg_armor(12)|difficulty(0) ,imodbits_cloth ],
["black_boots_reinforced", "Reinforced Black Boots", [("boot_slim_black_reinforced_L",0),("boot_slim_black_reinforced_inventory",ixmesh_inventory)], itp_merchandise| itp_type_foot_armor  |itp_civilian,0, 
 208 , weight(1.75)|abundance(70)|head_armor(0)|body_armor(0)|leg_armor(18)|difficulty(0) ,imodbits_cloth ], 
["grey_boots", "Grey Boots", [("boot_slim_grey_L",0),("boot_slim_grey_inventory",ixmesh_inventory)], itp_merchandise| itp_type_foot_armor  |itp_civilian,0, 
 108 , weight(1.25)|abundance(60)|head_armor(0)|body_armor(0)|leg_armor(12)|difficulty(0) ,imodbits_cloth ],
["white_boots", "White Boots", [("boot_slim_white_L",0),("boot_slim_white_inventory",ixmesh_inventory)], itp_merchandise| itp_type_foot_armor  |itp_civilian,0, 
 108 , weight(1.25)|abundance(70)|head_armor(0)|body_armor(0)|leg_armor(12)|difficulty(0) ,imodbits_cloth ],
["white_boots_reinforced", "Reinforced White Boots", [("boot_slim_white_reinforced_L",0),("boot_slim_white_reinforced_inventory",ixmesh_inventory)], itp_merchandise| itp_type_foot_armor  |itp_civilian,0, 
 208 , weight(1.75)|abundance(60)|head_armor(0)|body_armor(0)|leg_armor(18)|difficulty(0) ,imodbits_cloth ], 

["imperial_royal_guard_boots", "Imperial Royal Guard Boots", [("imperial_royal_guard_boots",0)], itp_merchandise| itp_type_foot_armor  |itp_civilian,0, 
 140 , weight(2.0)|abundance(50)|head_armor(0)|body_armor(0)|leg_armor(16)|difficulty(1) ,imodbits_cloth, [], empire_fac ],
["imperial_stormtrooper_boots", "Imperial Stormtrooper Boots", [("Stormtrooper_legs_L",0)], itp_merchandise| itp_type_foot_armor  |itp_civilian,0, 
 210 , weight(2.0)|abundance(50)|head_armor(0)|body_armor(0)|leg_armor(16)|difficulty(0) ,imodbits_armor, [], empire_fac ], 
["imperial_stormtrooper_boots_incinerator", "Incinerator Trooper Boots", [("Incinerator_legs_L",0)], itp_merchandise| itp_type_foot_armor  |itp_civilian,0, 
 257 , weight(2.7)|abundance(30)|head_armor(0)|body_armor(0)|leg_armor(19)|difficulty(6) ,imodbits_armor, [], empire_fac ], 
["imperial_stormtrooper_boots_novatrooper", "Novatrooper Boots", [("Novatrooper_legs_L",0)], itp_merchandise| itp_type_foot_armor  |itp_civilian,0, 
 250 , weight(2.4)|abundance(40)|head_armor(0)|body_armor(0)|leg_armor(18)|difficulty(4) ,imodbits_armor, [], empire_fac ], 
["imperial_scout_trooper_boots", "Imperial Scout Trooper Boots", [("scoutboots",0)], itp_merchandise| itp_type_foot_armor  |itp_civilian,0, 
 210 , weight(2.0)|abundance(50)|head_armor(0)|body_armor(0)|leg_armor(16)|difficulty(0) ,imodbits_armor, [], empire_fac ],  
["shadow_scout_trooper_boots", "Shadow Scout Trooper Boots", [("shadow_scoutboots",0)], itp_merchandise| itp_type_foot_armor  |itp_civilian,0, 
 240 , weight(2.0)|abundance(40)|head_armor(0)|body_armor(0)|leg_armor(18)|difficulty(0) ,imodbits_armor, [], empire_fac ],   

#removed merch flag on clone_trooper_boots
["clone_trooper_boots", "Clone Trooper Boots", [("ArcTrooperFeet",0)], itp_type_foot_armor  |itp_civilian,0, 
 210 , weight(2.0)|abundance(20)|head_armor(0)|body_armor(0)|leg_armor(16)|difficulty(0) ,imodbits_armor ],  

# SW Headwear
#["imperial_navy_helmet", "Imperial Navy Helmet", [("imperial_navy_helmet",0)], itp_merchandise| itp_type_head_armor|itp_civilian ,0, 
# 120 , weight(2)|abundance(100)|head_armor(10)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_armor ],
["lobot_headgear", "Borg Construct Aj^6", [("lobot_headgear",0)], itp_merchandise|itp_type_head_armor |itp_civilian,0, 500 , weight(2)|abundance(60)|head_armor(8)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_none ],
["glasses_black", "Shooting Glasses", [("glasses_black",0),("glasses_black_inv",ixmesh_inventory)], itp_merchandise|itp_type_head_armor |itp_civilian|itp_doesnt_cover_hair,0, 200 , weight(1)|abundance(80)|head_armor(6)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_none ],
["glasses_yellow", "Shooting Glasses", [("glasses_yellow",0)], itp_merchandise|itp_type_head_armor |itp_civilian|itp_doesnt_cover_hair,0, 200 , weight(1)|abundance(80)|head_armor(6)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_none ],
["eyepiece_tactics", "Tactics Eyepiece", [("eyepiece_down",0)], itp_merchandise|itp_type_head_armor |itp_civilian|itp_doesnt_cover_hair,0, 250 , weight(1)|abundance(100)|head_armor(6)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_none ],
["eyepiece_leadership", "Leadership Eyepiece", [("eyepiece_up",0)], itp_merchandise|itp_type_head_armor |itp_civilian|itp_doesnt_cover_hair,0, 250 , weight(1)|abundance(100)|head_armor(6)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_none ],
["slave_neck_chain", "Slave Neck Chain", [("slave_neck_chain",0)], itp_merchandise|itp_type_head_armor |itp_civilian|itp_doesnt_cover_hair,0, 200 , weight(5)|abundance(50)|head_armor(1)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_none ],

["officer_hat_white", "Officer Hat", [("impcap_white",0)], itp_merchandise| itp_type_head_armor |itp_civilian,0, 
 40 , weight(1)|abundance(100)|head_armor(5)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth, [], empire_fac ],

["civilian_cloak_hood", "Civilian Cloak and Hood", [("cloak08",0)], itp_type_head_armor|itp_merchandise| itp_attach_armature,0, 
 10 , weight(2)|abundance(40)|head_armor(2)|body_armor(1)|leg_armor(0) ,imodbits_cloth ],

["imperial_hat_green", "Imperial Hat", [("impcap_green",0)], itp_merchandise| itp_type_head_armor |itp_civilian,0, 
 140 , weight(1)|abundance(60)|head_armor(15)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth, [], empire_fac ],
["imperial_hat_black", "Imperial Hat", [("impcap_black",0)], itp_merchandise| itp_type_head_armor |itp_civilian,0, 
 110 , weight(1)|abundance(60)|head_armor(12)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth, [], empire_fac ],
["imperial_hat_grey", "Imperial Hat", [("impcap_grey",0)], itp_merchandise| itp_type_head_armor |itp_civilian,0, 
 70 , weight(1)|abundance(60)|head_armor(8)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth, [], empire_fac ], 

["rebel_technician_helmet", "Rebel Cadet Helmet", [("rebel_tech_helmet",0)], itp_merchandise| itp_type_head_armor|itp_civilian ,0, 
 120 , weight(2)|abundance(80)|head_armor(10)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_armor, [], rebel_fac ],
["rebel_trooper_helmet", "Rebel Trooper Helmet", [("rebel_fleet_trooper_helmet",0)], itp_merchandise| itp_type_head_armor|itp_civilian ,0, 
 195 , weight(2)|abundance(100)|head_armor(15)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_armor, [], rebel_fac ],
["rebel_heavy_trooper_helmet", "Rebel Heavy Trooper Helmet", [("rebel_heavy_trooper_helmet",0)], itp_merchandise| itp_type_head_armor|itp_civilian ,0, 
 300 , weight(2)|abundance(50)|head_armor(20)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_armor, [], rebel_fac ], 
["rebel_honor_guard_helmet", "Rebel Honor Guard Helmet", [("rebel_honor_guard_helmet",0)], itp_merchandise| itp_type_head_armor|itp_civilian ,0, 
 300 , weight(2)|abundance(50)|head_armor(20)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_armor, [], rebel_fac ], 

["transparent_helmet", "Transparent Helmet", [("_",0),("transparent_helmet_inv",ixmesh_inventory)], itp_unique|itp_type_head_armor|itp_doesnt_cover_hair|itp_civilian,0, 
 140 , weight(1)|abundance(60)|head_armor(15)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_none ], 
#["transparent_helmet_merch", "Transparent Helmet", [("_",0),("transparent_helmet_inv",ixmesh_inventory)], itp_merchandise|itp_type_head_armor|itp_doesnt_cover_hair|itp_civilian,0, 
# 140 , weight(1)|abundance(60)|head_armor(15)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_none ],  

["imperial_trooper_helmet", "Imperial Trooper Helmet", [("imperial_atst_driver_helmet",0)], itp_merchandise| itp_type_head_armor|itp_civilian ,0, 
 120 , weight(2)|abundance(100)|head_armor(10)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_armor, [], empire_fac ], 
["imperial_gunner_helmet", "Imperial Gunner Helmet", [("imperial_ds_gunner_helmet",0)], itp_merchandise| itp_type_head_armor|itp_covers_head|itp_civilian ,0, 
 140 , weight(2)|abundance(80)|head_armor(15)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_armor, [], empire_fac ],  
["imperial_navy_trooper_helmet", "Imperial Navy Trooper Helmet", [("imperial_ds_trooper_helmet",0)], itp_merchandise| itp_type_head_armor|itp_civilian ,0, 
 120 , weight(2)|abundance(80)|head_armor(10)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_armor, [], empire_fac ],

#["imperial_stormtrooper_helmet_2", "Imperial Stormtrooper Helmet", [("imperial_stormtrooper_helmet_2",0)], itp_merchandise| itp_type_head_armor|itp_covers_head|itp_civilian ,0, 
# 125 , weight(1)|abundance(100)|head_armor(14)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_armor ],
#["rebel_trooper_helmet_2", "Rebel Trooper Helmet", [("rebel_trooper_helmet_2",0)], itp_merchandise| itp_type_head_armor|itp_civilian ,0, 
# 125 , weight(2)|abundance(100)|head_armor(10)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_armor ], 

["mercenary_helmet", "Mercenary Helmet", [("mercenary_helmet",0)], itp_merchandise| itp_type_head_armor|itp_covers_head|itp_civilian ,0, 
 160 , weight(2.0)|abundance(50)|head_armor(14)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_armor ],   
["trandoshan_mask", "Trandoshan Mask", [("trandoshan_helmet_b",0)], itp_merchandise| itp_type_head_armor|itp_civilian ,0, 
 150 , weight(2.5)|abundance(50)|head_armor(14)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_armor ],   
["trandoshan_helmet", "Trandoshan Helmet", [("trandoshan_helmet_a",0)], itp_merchandise| itp_type_head_armor|itp_civilian ,0,  
 120 , weight(1)|abundance(40)|head_armor(10)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth ],   
["cap_military", "Cap", [("cap_military",0)], itp_merchandise| itp_type_head_armor|itp_civilian ,0, 
 30 , weight(2)|abundance(40)|head_armor(5)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth ],   
["cap_civilian_a", "Cap", [("cap_civilian_a",0)], itp_merchandise| itp_type_head_armor|itp_civilian ,0, 
 30 , weight(2)|abundance(40)|head_armor(5)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth ],    
["ewok_hat", "Ewok Hat", [("ewokhat",0)], itp_merchandise| itp_type_head_armor|itp_civilian ,0, 
 30 , weight(2)|abundance(40)|head_armor(5)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth ],   
["rancor_keeper_hat", "Rancor Keeper Hat", [("rancor_keeperhat",0)], itp_merchandise| itp_type_head_armor|itp_civilian ,0, 
 30 , weight(2)|abundance(40)|head_armor(5)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth ],    
["rodian_ventilator", "Rodian Ventilator", [("rodian_ventilator_green",0)], itp_merchandise| itp_type_head_armor|itp_civilian|itp_doesnt_cover_hair ,0, 
 120 , weight(2)|abundance(40)|head_armor(10)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_armor ],
["rodian_ventilator_black", "Rodian Ventilator", [("rodian_ventilator_black",0)], itp_merchandise| itp_type_head_armor|itp_civilian|itp_doesnt_cover_hair ,0, 
 120 , weight(2)|abundance(40)|head_armor(10)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_armor ],
["rodian_ventilator_red", "Rodian Ventilator", [("rodian_ventilator_red",0)], itp_merchandise| itp_type_head_armor|itp_civilian|itp_doesnt_cover_hair ,0, 
 120 , weight(2)|abundance(40)|head_armor(10)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_armor ], 
#["twilek_female_helmet", "Twilek Female Helmet", [("twilekwrap",0)], itp_merchandise| itp_type_head_armor|itp_civilian|itp_doesnt_cover_hair ,0, 
# 120 , weight(2)|abundance(50)|head_armor(10)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth ], 
["gamorrean_helmet", "Gamorrean Helmet", [("pigmask",0)], itp_merchandise| itp_type_head_armor|itp_civilian,0, 
 60 , weight(2)|abundance(40)|head_armor(8)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_armor ],   
["fang_helmet", "Fang Helmet", [("fanghelm",0)], itp_merchandise| itp_type_head_armor|itp_civilian ,0, 
 120 , weight(2)|abundance(60)|head_armor(10)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_armor ],   
["beak_helmet", "Beak Helmet", [("beakhelm",0)], itp_merchandise| itp_type_head_armor|itp_civilian ,0, 
 120 , weight(2)|abundance(60)|head_armor(10)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_armor ],   
["gas_mask", "Gas Mask", [("gasmask",0)], itp_merchandise| itp_type_head_armor|itp_covers_head|itp_civilian ,0, 
 120 , weight(2)|abundance(60)|head_armor(10)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_armor ],    
["mining_helmet", "Mining Helmet", [("genhelm",0)], itp_merchandise| itp_type_head_armor|itp_civilian ,0, 
 120 , weight(2)|abundance(60)|head_armor(10)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_armor ],     
["pipe_helmet", "Pipe Helmet", [("pipehelm",0)], itp_merchandise| itp_type_head_armor|itp_civilian ,0, 
 120 , weight(2)|abundance(60)|head_armor(10)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_armor ],
["skiff_guard_helmet", "Skiff Guard Helmet", [("skiffhelm",0)], itp_merchandise| itp_type_head_armor|itp_civilian ,0, 
 150 , weight(2)|abundance(60)|head_armor(12)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_armor ],
 
["imperial_stormtrooper_helmet", "Imperial Stormtrooper Helmet", [("Stormtrooper_helm",0)], itp_merchandise| itp_type_head_armor|itp_covers_head|itp_civilian ,0, 
 195 , weight(1)|abundance(100)|head_armor(14)|body_armor(0)|leg_armor(0)|difficulty(2) ,imodbits_armor, [], empire_fac ],
["imperial_stormtrooper_helmet_incinerator", "Incinerator Trooper Helmet", [("Incinerator_Trooper_helm",0)], itp_merchandise| itp_type_head_armor|itp_covers_head|itp_civilian ,0, 
 271 , weight(2)|abundance(40)|head_armor(20)|body_armor(0)|leg_armor(0)|difficulty(5) ,imodbits_armor, [], empire_fac ],
["imperial_stormtrooper_helmet_novatrooper", "Novatrooper Helmet", [("Novatrooper_helm",0)], itp_merchandise| itp_type_head_armor|itp_covers_head|itp_civilian ,0, 
 226 , weight(2)|abundance(50)|head_armor(15)|body_armor(0)|leg_armor(0)|difficulty(3) ,imodbits_armor, [], empire_fac ],
["imperial_pilot_helmet", "Imperial Pilot Helmet", [("tiepilot",0)], itp_merchandise| itp_type_head_armor|itp_covers_head|itp_civilian ,0, 
 175 , weight(1)|abundance(60)|head_armor(12)|body_armor(0)|leg_armor(0)|difficulty(1) ,imodbits_armor, [], empire_fac ], 

# removed merchandise, added unique & civilian, removed civilian from all clone_trooper_helmets so the head would be used indoors  (nevermind, added civilian back)
["clone_trooper_head", "Clone Trooper Head", [("cloneface_helmet",0)], itp_unique|itp_type_head_armor|itp_covers_head|itp_civilian ,0, 150 , weight(1)|abundance(0)|head_armor(10)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_none ], 
["clone_trooper_head_scar", "Clone Trooper Head", [("cloneface_scar_helmet",0)], itp_unique|itp_type_head_armor|itp_covers_head|itp_civilian ,0, 150 , weight(1)|abundance(0)|head_armor(10)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_none ], 
#removed merchandise tag since they will appear in a clone era merchant
["clone_trooper_helmet_white", "Clone Trooper Helmet", [("ArcTrooperHelmWhite",0)], itp_type_head_armor|itp_covers_head|itp_civilian ,0, 285 , weight(1)|abundance(10)|head_armor(10)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_armor ], 
["clone_trooper_helmet_green", "Clone Trooper Helmet", [("ArcTrooperHelmGreen",0)], itp_type_head_armor|itp_covers_head|itp_civilian,0, 315 , weight(1)|abundance(10)|head_armor(12)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_armor ],  
["clone_trooper_helmet_blue", "Clone Trooper Helmet", [("ArcTrooperHelmBlue",0)], itp_type_head_armor|itp_covers_head|itp_civilian,0, 345 , weight(1)|abundance(10)|head_armor(14)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_armor ], 
["clone_trooper_helmet_red", "Clone Trooper Helmet", [("ArcTrooperHelmRed",0)], itp_type_head_armor|itp_covers_head|itp_civilian ,0, 375 , weight(1)|abundance(10)|head_armor(16)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_armor ], 
["clone_trooper_helmet_yellow", "Clone Trooper Helmet", [("ArcTrooperHelmYellow",0)], itp_type_head_armor|itp_covers_head|itp_civilian ,0, 405 , weight(1)|abundance(10)|head_armor(18)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_armor ],  
["clone_trooper_helmet_orange", "Clone Trooper Helmet", [("ArcTrooperHelmOrange",0)], itp_type_head_armor|itp_covers_head|itp_civilian ,0, 405 , weight(1)|abundance(10)|head_armor(18)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_armor ], 
["clone_trooper_helmet_mand", "Clone Trooper Helmet", [("ArcTrooperHelmMand",0)], itp_type_head_armor|itp_covers_head|itp_civilian ,0, 405 , weight(1)|abundance(10)|head_armor(18)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_armor ], 
["clone_trooper_helmet_lux", "Clone Trooper Helmet", [("ArcTrooperHelmLux",0)], itp_type_head_armor|itp_covers_head|itp_civilian ,0, 405 , weight(1)|abundance(10)|head_armor(18)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_armor ], 
["clone_commando_helmet", "Clone Commando Helmet", [("clonecommando_helm",0)], itp_type_head_armor|itp_covers_head|itp_civilian ,0, 530 , weight(2)|abundance(8)|head_armor(20)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_armor ], 
 
["imperial_scout_trooper_helmet", "Imperial Scout Trooper Helmet", [("scouthelm",0)], itp_merchandise| itp_type_head_armor|itp_covers_head|itp_civilian ,0, 
 135 , weight(1)|abundance(100)|head_armor(10)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_armor, [], empire_fac ],
["shadow_scout_trooper_helmet", "Shadow Scout Trooper Helmet", [("shadow_scouthelm",0)], itp_merchandise| itp_type_head_armor|itp_covers_head|itp_civilian ,0, 
 195 , weight(1)|abundance(60)|head_armor(14)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_armor, [], empire_fac ],

["republic_pilot_helmet", "Rebel Pilot Helmet", [("republic_pilot_helmet",0)], itp_merchandise| itp_type_head_armor|itp_civilian ,0, 
 135 , weight(1)|abundance(100)|head_armor(10)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_armor, [], rebel_fac ],
["republic_commando_helmet", "Rebel Commando Helmet", [("republic_commando_helmet",0)], itp_merchandise| itp_type_head_armor|itp_civilian ,0, 
 180 , weight(2)|abundance(80)|head_armor(14)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_armor, [], rebel_fac ],
["republic_commando_desert_helmet", "Rebel Desert Commando Helmet", [("republic_commando_desert_helmet",0)], itp_merchandise| itp_type_head_armor|itp_civilian ,0, 
 180 , weight(2)|abundance(40)|head_armor(14)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_armor, [], rebel_fac ],
["republic_commando_urban_helmet", "Rebel Urban Commando Helmet", [("republic_commando_urban_helmet",0)], itp_merchandise| itp_type_head_armor|itp_civilian ,0, 
 180 , weight(2)|abundance(40)|head_armor(14)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_armor, [], rebel_fac ],
["rebel_sniper_helmet", "Rebel Sniper Helmet", [("republic_commando_helmet_b",0)], itp_merchandise| itp_type_head_armor|itp_civilian ,0, 
 180 , weight(2)|abundance(60)|head_armor(14)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_armor, [], rebel_fac ],

# jedi/sith hoods
["jedi_knight_hood", "Jedi Knight Hood", [("jedi_knight_hood",0)], itp_type_head_armor|itp_civilian|itp_merchandise   ,0, 
 105 , weight(0.1)|abundance(100)|head_armor(10)|body_armor(0)|leg_armor(0) ,imodbits_cloth, [], jedi_fac ],
["jedi_knight_hood_unique", "Jedi Knight Hood", [("jedi_knight_hood",0)], itp_type_head_armor|itp_civilian|itp_unique   ,0, 
 149 , weight(0.1)|abundance(0)|head_armor(15)|body_armor(0)|leg_armor(0) ,imodbits_cloth, [], jedi_fac ],
#["sith_hood", "Sith Hood", [("hood_black",0)],                     itp_type_head_armor|itp_merchandise   ,0, 75 , weight(0.1)|abundance(100)|head_armor(15)|body_armor(0)|leg_armor(0) ,imodbits_cloth ],
["sith_hood", "Sith Hood", [("sith_hood",0)],                     itp_type_head_armor|itp_civilian|itp_merchandise   ,0, 
 105 , weight(0.1)|abundance(100)|head_armor(10)|body_armor(0)|leg_armor(0) ,imodbits_cloth, [], sith_fac ],
["sith_hood_unique", "Sith Hood", [("sith_hood",0)],              itp_type_head_armor|itp_civilian|itp_unique   ,0, 
 149 , weight(0.1)|abundance(0)|head_armor(15)|body_armor(0)|leg_armor(0) ,imodbits_cloth, [], sith_fac ],
["jedi_master_hood", "Jedi Master Hood", [("jedi_master_hood",0)], itp_type_head_armor|itp_civilian|itp_merchandise   ,0, 
 105 , weight(0.1)|abundance(100)|head_armor(10)|body_armor(0)|leg_armor(0) ,imodbits_cloth, [], jedi_fac ],
["jedi_master_hood_unique", "Jedi Master Hood", [("jedi_master_hood",0)], itp_type_head_armor|itp_civilian|itp_unique   ,0, 
 149 , weight(0.1)|abundance(0)|head_armor(15)|body_armor(0)|leg_armor(0) ,imodbits_cloth, [], jedi_fac ],

# cloaks from OSP Cloaks
["jedi_knight_cloak", "Jedi Knight Cloak", [("cloak15",0)], itp_type_head_armor|itp_civilian|itp_merchandise| itp_attach_armature| itp_doesnt_cover_hair,0, 
 80 , weight(2)|abundance(80)|head_armor(5)|body_armor(5)|leg_armor(0) ,imodbits_cloth, [], jedi_fac ],
["jedi_knight_cloak_hood", "Jedi Knight Cloak with Hood", [("cloak16",0)], itp_type_head_armor|itp_civilian|itp_merchandise| itp_attach_armature,0, 
 130 , weight(2)|abundance(80)|head_armor(10)|body_armor(5)|leg_armor(0) ,imodbits_cloth, [], jedi_fac ],
["jedi_master_cloak", "Jedi Master Cloak", [("cloak05",0)], itp_type_head_armor|itp_civilian|itp_merchandise| itp_attach_armature| itp_doesnt_cover_hair,0, 
 80 , weight(2)|abundance(80)|head_armor(5)|body_armor(5)|leg_armor(0) ,imodbits_cloth, [], jedi_fac ],
["jedi_master_cloak_hood", "Jedi Master Cloak with Hood", [("cloak06",0)], itp_type_head_armor|itp_civilian|itp_merchandise| itp_attach_armature,0, 
 130 , weight(2)|abundance(80)|head_armor(10)|body_armor(5)|leg_armor(0) ,imodbits_cloth, [], jedi_fac ],
["sith_cloak", "Sith Cloak", [("cloak09",0)], itp_type_head_armor|itp_civilian|itp_merchandise| itp_attach_armature| itp_doesnt_cover_hair,0, 
 80 , weight(2)|abundance(80)|head_armor(5)|body_armor(5)|leg_armor(0) ,imodbits_cloth, [], sith_fac ],
["sith_cloak_hood", "Sith Cloak with Hood", [("cloak10",0)], itp_type_head_armor|itp_civilian|itp_merchandise| itp_attach_armature,0, 
 130 , weight(2)|abundance(80)|head_armor(10)|body_armor(5)|leg_armor(0) ,imodbits_cloth, [], sith_fac ],
["sith_cloak_mask", "Sith Cloak with Mask", [("cloak29",0)], itp_type_head_armor|itp_civilian|itp_merchandise| itp_attach_armature,0, 
 130 , weight(2)|abundance(80)|head_armor(10)|body_armor(5)|leg_armor(0) ,imodbits_cloth, [], sith_fac ],

["imperial_royal_guard_helmet", "Imperial Royal Guard Helmet", [("imperial_royal_guard_helmet",0)], itp_merchandise| itp_type_head_armor|itp_covers_head|itp_civilian ,0, 
 255 , weight(1)|abundance(60)|head_armor(18)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_armor, [], empire_fac ],
["shadow_guard_helmet", "Imperial Shadow Guard Helmet", [("shadow_guard_helmet",0)], itp_merchandise| itp_type_head_armor|itp_covers_head|itp_civilian ,0, 
 300 , weight(1)|abundance(40)|head_armor(20)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_armor, [], empire_fac ],

#["imperial_stormtrooper_helmet_black", "Imperial Darktrooper Helmet", [("imperial_stormtrooper_helmet_black",0)], itp_merchandise| itp_type_head_armor|itp_covers_head|itp_civilian ,0, 175 , weight(1)|abundance(100)|head_armor(18)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_armor ],
# ["desert_hat1", "Desert Hat", [("desert_hat1",0)],itp_merchandise|itp_type_head_armor|itp_civilian,0,90, weight(1)|abundance(50)|head_armor(10)|body_armor(0)|leg_armor(0)|difficulty(0),imodbits_cloth],
# ["desert_hat2", "Desert Hat", [("desert_hat2",0)],itp_merchandise|itp_type_head_armor|itp_civilian,0,90, weight(1)|abundance(40)|head_armor(10)|body_armor(0)|leg_armor(0)|difficulty(0),imodbits_cloth],
# ["desert_hat3", "Desert Hat", [("desert_hat3",0)],itp_merchandise|itp_type_head_armor|itp_civilian,0,90, weight(1)|abundance(40)|head_armor(10)|body_armor(0)|leg_armor(0)|difficulty(0),imodbits_cloth],
# ["urban_hat1", "Urban Hat", [("urban_hat1",0)],itp_merchandise|itp_type_head_armor|itp_civilian,0,90, weight(1)|abundance(50)|head_armor(10)|body_armor(0)|leg_armor(0)|difficulty(0),imodbits_cloth],
# ["urban_hat2", "Urban Hat", [("urban_hat2",0)],itp_merchandise|itp_type_head_armor|itp_civilian,0,90, weight(1)|abundance(40)|head_armor(10)|body_armor(0)|leg_armor(0)|difficulty(0),imodbits_cloth],
# ["urban_hat3", "Urban Hat", [("urban_hat3",0)],itp_merchandise|itp_type_head_armor|itp_civilian,0,90, weight(1)|abundance(40)|head_armor(10)|body_armor(0)|leg_armor(0)|difficulty(0),imodbits_cloth],
# ["camouflage_hat1", "Camouflage Hat", [("camouflage_hat1",0)],itp_merchandise|itp_type_head_armor|itp_civilian,0,90, weight(1)|abundance(50)|head_armor(10)|body_armor(0)|leg_armor(0)|difficulty(0),imodbits_cloth],
# ["camouflage_hat2", "Camouflage Hat", [("camouflage_hat2",0)],itp_merchandise|itp_type_head_armor|itp_civilian,0,90, weight(1)|abundance(40)|head_armor(10)|body_armor(0)|leg_armor(0)|difficulty(0),imodbits_cloth],
# ["camouflage_hat3", "Camouflage Hat", [("camouflage_hat3",0)],itp_merchandise|itp_type_head_armor|itp_civilian,0,90, weight(1)|abundance(40)|head_armor(10)|body_armor(0)|leg_armor(0)|difficulty(0),imodbits_cloth],

# SW Bodywear
["dress_yellow", "Lady Dress", [("court_dress",0)], itp_type_body_armor|itp_merchandise|itp_covers_legs|itp_civilian   ,0, 280 , weight(2)|abundance(60)|head_armor(0)|body_armor(20)|leg_armor(10)|difficulty(0) ,imodbits_cloth ],
["dress_red", "Lady Dress", [("lady_dress_r",0)], itp_type_body_armor  |itp_covers_legs|itp_civilian ,0, 280 , weight(2)|abundance(60)|head_armor(0)|body_armor(20)|leg_armor(10)|difficulty(0) ,imodbits_cloth],
["dress_green", "Lady Dress", [("lady_dress_g",0)], itp_type_body_armor  |itp_covers_legs|itp_civilian ,0, 280 , weight(2)|abundance(60)|head_armor(0)|body_armor(20)|leg_armor(10)|difficulty(0) ,imodbits_cloth],
["dress_blue", "Lady Dress", [("lady_dress_b",0)], itp_type_body_armor  |itp_covers_legs|itp_civilian ,0, 280 , weight(2)|abundance(60)|head_armor(0)|body_armor(20)|leg_armor(10)|difficulty(0) ,imodbits_cloth],
["tunic_green", "Tunic", [("arena_tunicG",0)], itp_merchandise|itp_type_body_armor|itp_civilian |itp_covers_legs ,0, 150 , weight(2)|abundance(30)|head_armor(0)|body_armor(16)|leg_armor(8)|difficulty(0) ,imodbits_cloth ],
["tunic_white", "Tunic", [("arena_tunicW",0)], itp_merchandise|itp_type_body_armor|itp_civilian |itp_covers_legs ,0, 150 , weight(2)|abundance(30)|head_armor(0)|body_armor(16)|leg_armor(8)|difficulty(0) ,imodbits_cloth ],
["tunic_blue", "Tunic", [("arena_tunicB",0)], itp_merchandise|itp_type_body_armor|itp_civilian |itp_covers_legs ,0, 150 , weight(2)|abundance(30)|head_armor(0)|body_armor(16)|leg_armor(8)|difficulty(0) ,imodbits_cloth ], 
["tunic_red", "Tunic", [("arena_tunicR",0)], itp_merchandise|itp_type_body_armor|itp_civilian |itp_covers_legs ,0, 150 , weight(2)|abundance(30)|head_armor(0)|body_armor(16)|leg_armor(8)|difficulty(0) ,imodbits_cloth ], 
["tunic_yellow", "Tunic", [("arena_tunicY",0)], itp_merchandise|itp_type_body_armor|itp_civilian |itp_covers_legs ,0, 150 , weight(2)|abundance(30)|head_armor(0)|body_armor(16)|leg_armor(8)|difficulty(0) ,imodbits_cloth ],
["padded_tunic_green", "Padded Tunic", [("arena_tunicG_padded",0)], itp_merchandise|itp_type_body_armor|itp_civilian |itp_covers_legs ,0, 250 , weight(3)|abundance(50)|head_armor(0)|body_armor(24)|leg_armor(10)|difficulty(0) ,imodbits_cloth ],
["padded_tunic_white", "Padded Tunic", [("arena_tunicW_padded",0)], itp_merchandise|itp_type_body_armor|itp_civilian |itp_covers_legs ,0, 250 , weight(3)|abundance(50)|head_armor(0)|body_armor(24)|leg_armor(10)|difficulty(0) ,imodbits_cloth ],
["padded_tunic_blue", "Padded Tunic", [("arena_tunicB_padded",0)], itp_merchandise|itp_type_body_armor|itp_civilian |itp_covers_legs ,0, 250 , weight(3)|abundance(50)|head_armor(0)|body_armor(24)|leg_armor(10)|difficulty(0) ,imodbits_cloth ], 
["padded_tunic_red", "Padded Tunic", [("arena_tunicR_padded",0)], itp_merchandise|itp_type_body_armor|itp_civilian |itp_covers_legs ,0, 250 , weight(3)|abundance(50)|head_armor(0)|body_armor(24)|leg_armor(10)|difficulty(0) ,imodbits_cloth ], 
["padded_tunic_yellow", "Tunic", [("arena_tunicY_padded",0)], itp_merchandise|itp_type_body_armor|itp_civilian |itp_covers_legs ,0, 250 , weight(3)|abundance(50)|head_armor(0)|body_armor(24)|leg_armor(10)|difficulty(0) ,imodbits_cloth ],
["officer_uniform_white", "Officer Uniform", [("imperial_uniform_white",0)], itp_merchandise| itp_type_body_armor |itp_covers_legs |itp_civilian  ,0, 380 , weight(2)|abundance(100)|head_armor(0)|body_armor(28)|leg_armor(12)|difficulty(0) ,imodbits_cloth ],
["imperial_uniform_black_plain", "Imperial Uniform", [("impofficer",0)], itp_merchandise| itp_type_body_armor |itp_covers_legs |itp_civilian  ,0, 380 , weight(2)|abundance(100)|head_armor(0)|body_armor(28)|leg_armor(12)|difficulty(0) ,imodbits_cloth ],
["female_outfit_femconblack", "Female Outfit", [("femconblack",0)], itp_merchandise| itp_type_body_armor |itp_covers_legs |itp_civilian  ,0, 350 , weight(5)|abundance(40)|head_armor(0)|body_armor(28)|leg_armor(12)|difficulty(0) ,imodbits_cloth ],
["female_outfit_femconbrowngreen", "Female Outfit", [("femconbrowngreen",0)], itp_merchandise| itp_type_body_armor |itp_covers_legs |itp_civilian  ,0, 350 , weight(5)|abundance(40)|head_armor(0)|body_armor(28)|leg_armor(12)|difficulty(0) ,imodbits_cloth ],
["female_outfit_femcongrey", "Female Outfit", [("femcongrey",0)], itp_merchandise| itp_type_body_armor |itp_covers_legs |itp_civilian  ,0, 350 , weight(5)|abundance(40)|head_armor(0)|body_armor(28)|leg_armor(12)|difficulty(0) ,imodbits_cloth ],
["female_outfit_femconorange", "Female Outfit", [("femconorange",0)], itp_merchandise| itp_type_body_armor |itp_covers_legs |itp_civilian  ,0, 350 , weight(5)|abundance(40)|head_armor(0)|body_armor(28)|leg_armor(12)|difficulty(0) ,imodbits_cloth ],
["female_outfit_femconwhite", "Female Outfit", [("femconwhite",0)], itp_merchandise| itp_type_body_armor |itp_covers_legs |itp_civilian  ,0, 350 , weight(5)|abundance(40)|head_armor(0)|body_armor(28)|leg_armor(12)|difficulty(0) ,imodbits_cloth ],
["female_outfit_femconwhitebrown", "Female Outfit", [("femconwhitebrown",0)], itp_merchandise| itp_type_body_armor |itp_covers_legs |itp_civilian  ,0, 350 , weight(5)|abundance(40)|head_armor(0)|body_armor(28)|leg_armor(12)|difficulty(0) ,imodbits_cloth ],
["outfit_tan", "Jumpsuit", [("outfit_tan",0)], itp_merchandise| itp_type_body_armor |itp_covers_legs |itp_civilian  ,0, 350 , weight(5)|abundance(30)|head_armor(0)|body_armor(28)|leg_armor(12)|difficulty(0) ,imodbits_cloth ],
["outfit_grey", "Jumpsuit", [("outfit_grey",0)], itp_merchandise| itp_type_body_armor |itp_covers_legs |itp_civilian  ,0, 350 , weight(5)|abundance(30)|head_armor(0)|body_armor(28)|leg_armor(12)|difficulty(0) ,imodbits_cloth ],
["outfit_black", "Jumpsuit", [("outfit_black",0)], itp_merchandise| itp_type_body_armor |itp_covers_legs |itp_civilian  ,0, 350 , weight(5)|abundance(30)|head_armor(0)|body_armor(28)|leg_armor(12)|difficulty(0) ,imodbits_cloth ],
["outfit_green", "Jumpsuit", [("outfit_green",0)], itp_merchandise| itp_type_body_armor |itp_covers_legs |itp_civilian  ,0, 350 , weight(5)|abundance(30)|head_armor(0)|body_armor(28)|leg_armor(12)|difficulty(0) ,imodbits_cloth ],
["vest_open_a", "Open Vest", [("vest_open_a",0)], itp_merchandise| itp_type_body_armor |itp_covers_legs |itp_civilian  ,0, 380 , weight(2)|abundance(50)|head_armor(0)|body_armor(28)|leg_armor(12)|difficulty(0) ,imodbits_cloth ],
["vest_open_b", "Open Vest", [("vest_open_b",0)], itp_merchandise| itp_type_body_armor |itp_covers_legs |itp_civilian  ,0, 380 , weight(2)|abundance(50)|head_armor(0)|body_armor(28)|leg_armor(12)|difficulty(0) ,imodbits_cloth ],
#vest_open_c is used for han_solo_outfit
["vest_closed_a", "Closed Vest", [("vest_closed_a",0)], itp_merchandise| itp_type_body_armor |itp_covers_legs |itp_civilian  ,0, 380 , weight(2)|abundance(50)|head_armor(0)|body_armor(28)|leg_armor(12)|difficulty(0) ,imodbits_cloth ],
["vest_closed_b", "Closed Vest", [("vest_closed_b",0)], itp_merchandise| itp_type_body_armor |itp_covers_legs |itp_civilian  ,0, 380 , weight(2)|abundance(50)|head_armor(0)|body_armor(28)|leg_armor(12)|difficulty(0) ,imodbits_cloth ],
["vest_closed_c", "Closed Vest", [("vest_closed_c",0)], itp_merchandise| itp_type_body_armor |itp_covers_legs |itp_civilian  ,0, 380 , weight(2)|abundance(50)|head_armor(0)|body_armor(28)|leg_armor(12)|difficulty(0) ,imodbits_cloth ],
["shirt_blue", "Shirt", [("vest_closed_d",0)], itp_merchandise| itp_type_body_armor |itp_covers_legs |itp_civilian  ,0, 380 , weight(2)|abundance(50)|head_armor(0)|body_armor(28)|leg_armor(12)|difficulty(0) ,imodbits_cloth ],
["shirt_green", "Shirt", [("vest_closed_e",0)], itp_merchandise| itp_type_body_armor |itp_covers_legs |itp_civilian  ,0, 380 , weight(2)|abundance(50)|head_armor(0)|body_armor(28)|leg_armor(12)|difficulty(0) ,imodbits_cloth ],
["vest_closed_f", "Snow Jacket", [("vest_closed_f",0)], itp_merchandise| itp_type_body_armor |itp_covers_legs |itp_civilian  ,0, 380 , weight(2)|abundance(50)|head_armor(0)|body_armor(28)|leg_armor(12)|difficulty(0) ,imodbits_cloth ],
["jacket_open_a", "Open Jacket", [("jacket_open_a",0)], itp_merchandise| itp_type_body_armor |itp_covers_legs |itp_civilian  ,0, 380 , weight(2)|abundance(50)|head_armor(0)|body_armor(28)|leg_armor(12)|difficulty(0) ,imodbits_cloth ],
["jacket_open_b", "Open Jacket", [("jacket_open_b",0)], itp_merchandise| itp_type_body_armor |itp_covers_legs |itp_civilian  ,0, 380 , weight(2)|abundance(50)|head_armor(0)|body_armor(28)|leg_armor(12)|difficulty(0) ,imodbits_cloth ],
["jacket_open_c", "Open Jacket", [("jacket_open_c",0)], itp_merchandise| itp_type_body_armor |itp_covers_legs |itp_civilian  ,0, 380 , weight(2)|abundance(50)|head_armor(0)|body_armor(28)|leg_armor(12)|difficulty(0) ,imodbits_cloth ],
["female_jacket_a", "Female Jacket", [("female_suit_a",0)], itp_merchandise| itp_type_body_armor |itp_covers_legs |itp_civilian  ,0, 380 , weight(2)|abundance(80)|head_armor(0)|body_armor(28)|leg_armor(12)|difficulty(0) ,imodbits_cloth ],
["female_jacket_b", "Female Jacket", [("female_suit_b",0)], itp_merchandise| itp_type_body_armor |itp_covers_legs |itp_civilian  ,0, 380 , weight(2)|abundance(80)|head_armor(0)|body_armor(28)|leg_armor(12)|difficulty(0) ,imodbits_cloth ],
["female_jacket_c", "Female Jacket", [("female_suit_c",0)], itp_merchandise| itp_type_body_armor |itp_covers_legs |itp_civilian  ,0, 380 , weight(2)|abundance(80)|head_armor(0)|body_armor(28)|leg_armor(12)|difficulty(0) ,imodbits_cloth ],
#start of surrearlarms mod
["female_dress_a", "Female Dress", [("anar_dress",0)], itp_merchandise| itp_type_body_armor |itp_covers_legs |itp_civilian  ,0, 200 , weight(1)|abundance(40)|head_armor(0)|body_armor(20)|leg_armor(6)|difficulty(0) ,imodbits_cloth ],
["female_dress_b", "Female Dress", [("anar_dress2",0)], itp_merchandise| itp_type_body_armor |itp_covers_legs |itp_civilian  ,0, 200 , weight(1)|abundance(40)|head_armor(0)|body_armor(20)|leg_armor(6)|difficulty(0) ,imodbits_cloth ],
["female_dancer_outfit_a", "Female Dancer Outfit", [("rogue_armor3",0)], itp_merchandise| itp_type_body_armor |itp_covers_legs |itp_civilian  ,0, 300 , weight(1)|abundance(40)|head_armor(0)|body_armor(14)|leg_armor(6)|difficulty(0) ,imodbits_cloth ],
["female_dancer_outfit_a_cloak", "Female Dancer Outfit", [("rogue_armor4",0)], itp_merchandise| itp_type_body_armor |itp_covers_legs |itp_civilian  ,0, 350 , weight(1)|abundance(40)|head_armor(0)|body_armor(20)|leg_armor(6)|difficulty(0) ,imodbits_cloth ],
["female_dancer_boots", "Female Dancer Boots", [("rogue_csizma",0)], itp_merchandise|itp_type_foot_armor | itp_attach_armature|itp_civilian,0, 250 , weight(1)|abundance(40)|head_armor(0)|body_armor(0)|leg_armor(6)|difficulty(0) ,imodbits_cloth ],
#end of surrearlarms mod
["female_leather_a", "Female Leather Outfit", [("female_leather_a",0)], itp_merchandise| itp_type_body_armor |itp_covers_legs |itp_civilian  ,0, 350 , weight(1.5)|abundance(30)|head_armor(0)|body_armor(20)|leg_armor(8)|difficulty(0) ,imodbits_cloth ],
["female_leather_b", "Female Leather Outfit", [("female_leather_b",0)], itp_merchandise| itp_type_body_armor |itp_covers_legs |itp_civilian  ,0, 350 , weight(1.5)|abundance(30)|head_armor(0)|body_armor(20)|leg_armor(8)|difficulty(0) ,imodbits_cloth ],
["female_leather_c", "Female Leather Outfit", [("female_leather_c",0)], itp_merchandise| itp_type_body_armor |itp_covers_legs |itp_civilian  ,0, 350 , weight(1.5)|abundance(30)|head_armor(0)|body_armor(20)|leg_armor(8)|difficulty(0) ,imodbits_cloth ],
["female_leather_d", "Female Leather Outfit", [("female_leather_d",0)], itp_merchandise| itp_type_body_armor |itp_covers_legs |itp_civilian  ,0, 350 , weight(1.5)|abundance(30)|head_armor(0)|body_armor(20)|leg_armor(8)|difficulty(0) ,imodbits_cloth ],
["jacket_closed_a", "Closed Jacket", [("jacket_closed_a",0)], itp_merchandise| itp_type_body_armor |itp_covers_legs |itp_civilian  ,0, 380 , weight(2)|abundance(50)|head_armor(0)|body_armor(28)|leg_armor(12)|difficulty(0) ,imodbits_cloth ],
["jacket_closed_b", "Closed Jacket", [("jacket_closed_b",0)], itp_merchandise| itp_type_body_armor |itp_covers_legs |itp_civilian  ,0, 380 , weight(2)|abundance(50)|head_armor(0)|body_armor(28)|leg_armor(12)|difficulty(0) ,imodbits_cloth ],
["jacket_closed_c", "Closed Jacket", [("jacket_closed_c",0)], itp_merchandise| itp_type_body_armor |itp_covers_legs |itp_civilian  ,0, 380 , weight(2)|abundance(50)|head_armor(0)|body_armor(28)|leg_armor(12)|difficulty(0) ,imodbits_cloth ],
["klatooinian_armor", "Klatooinian Armor", [("klatooinian_armor",0)], itp_merchandise| itp_type_body_armor |itp_covers_legs |itp_civilian  ,0, 420 , weight(5)|abundance(50)|head_armor(0)|body_armor(32)|leg_armor(14)|difficulty(0) ,imodbits_cloth ],
["scavenger_armor", "Scavenger Armor", [("scavenger_armor",0)], itp_merchandise| itp_type_body_armor |itp_covers_legs |itp_civilian  ,0, 460 , weight(5)|abundance(50)|head_armor(0)|body_armor(35)|leg_armor(16)|difficulty(0) ,imodbits_cloth ],
["mercenary_armor", "Mercenary Armor", [("mercenary_armor",0)], itp_merchandise| itp_type_body_armor |itp_covers_legs |itp_civilian  ,0, 460 , weight(5)|abundance(50)|head_armor(0)|body_armor(35)|leg_armor(16)|difficulty(0) ,imodbits_cloth ],
["crime_lord_armor", "Crime Lord Armor", [("zann_armor",0)], itp_merchandise| itp_type_body_armor |itp_covers_legs |itp_civilian  ,0, 460 , weight(5)|abundance(50)|head_armor(0)|body_armor(35)|leg_armor(16)|difficulty(0) ,imodbits_cloth ],
#["jacket_closed_e", "Closed Jacket", [("jacket_closed_c",0)], itp_merchandise| itp_type_body_armor |itp_covers_legs |itp_civilian  ,0, 380 , weight(2)|abundance(50)|head_armor(0)|body_armor(28)|leg_armor(12)|difficulty(0) ,imodbits_cloth ],
["trandoshan_flight_suit", "Trandoshan Flight Suit", [("jacket_closed_f",0)], itp_merchandise| itp_type_body_armor |itp_covers_legs |itp_civilian  ,0, 420 , weight(2)|abundance(50)|head_armor(0)|body_armor(34)|leg_armor(14)|difficulty(0) ,imodbits_cloth ],
["civilian_cloak", "Civilian Cloak", [("cloak07",0)], itp_type_head_armor|itp_merchandise| itp_attach_armature| itp_doesnt_cover_hair,0, 10 , weight(2)|abundance(100)|head_armor(1)|body_armor(1)|leg_armor(0) ,imodbits_cloth ],
["white_cloak", "White Cloak", [("cloak11",0)], itp_type_head_armor|itp_merchandise| itp_attach_armature| itp_doesnt_cover_hair,0, 10 , weight(2)|abundance(100)|head_armor(1)|body_armor(1)|leg_armor(0) ,imodbits_cloth ],

["padded_armor_white", "Padded Armor", [("white_gambeson",0)], itp_merchandise| itp_type_body_armor|itp_covers_legs|itp_civilian,0, 320 , weight(5)|abundance(70)|head_armor(0)|body_armor(25)|leg_armor(12)|difficulty(0) ,imodbits_cloth ],
["padded_armor_red", "Padded Armor", [("red_gambeson",0)], itp_merchandise| itp_type_body_armor|itp_covers_legs|itp_civilian,0, 320 , weight(5)|abundance(70)|head_armor(0)|body_armor(25)|leg_armor(12)|difficulty(0) ,imodbits_cloth ],
["padded_armor_blue", "Padded Armor", [("blue_gambeson",0)], itp_merchandise| itp_type_body_armor|itp_covers_legs|itp_civilian,0, 320 , weight(5)|abundance(70)|head_armor(0)|body_armor(25)|leg_armor(12)|difficulty(0) ,imodbits_cloth ],
#
["armor_blue", "Armor", [("sw_armor3_blue",0)], itp_merchandise| itp_type_body_armor |itp_covers_legs |itp_civilian  ,0, 400 , weight(5)|abundance(50)|head_armor(0)|body_armor(32)|leg_armor(12)|difficulty(0) ,imodbits_cloth ],
["armor_brown", "Armor", [("sw_armor3_brown",0)], itp_merchandise| itp_type_body_armor |itp_covers_legs |itp_civilian  ,0, 400 , weight(5)|abundance(50)|head_armor(0)|body_armor(32)|leg_armor(12)|difficulty(0) ,imodbits_cloth ],
["armor_red", "Armor", [("sw_armor3_red",0)], itp_merchandise| itp_type_body_armor |itp_covers_legs |itp_civilian  ,0, 400 , weight(5)|abundance(50)|head_armor(0)|body_armor(32)|leg_armor(12)|difficulty(0) ,imodbits_cloth ],
["armor_white", "Armor", [("sw_armor3_white",0)], itp_merchandise| itp_type_body_armor |itp_covers_legs |itp_civilian  ,0, 400 , weight(5)|abundance(50)|head_armor(0)|body_armor(32)|leg_armor(12)|difficulty(0) ,imodbits_cloth ],

["pirate_armor", "Armor", [("sw_armor3_white",0)], itp_merchandise| itp_type_body_armor |itp_covers_legs |itp_civilian  ,0, 
 230 , weight(7)|abundance(80)|head_armor(0)|body_armor(28)|leg_armor(12)|difficulty(0) ,imodbits_cloth ],

### - Civilians - Outfits (TAS):

["ind_clothes_outfitvest_red", "Civilian vest", [("civilian_outfit_vest_1",0)], itp_merchandise|itp_type_body_armor|itp_attach_armature|itp_covers_legs|itp_civilian, 0, 
 150 , weight(2)|abundance(30)|head_armor(0)|body_armor(16)|leg_armor(8)|difficulty(0) ,imodbits_cloth ],
["ind_clothes_outfitvest_green", "Civilian vest", [("civilian_outfit_vest_2",0)], itp_merchandise|itp_type_body_armor|itp_attach_armature|itp_covers_legs|itp_civilian, 0, 
 150 , weight(2)|abundance(30)|head_armor(0)|body_armor(16)|leg_armor(8)|difficulty(0) ,imodbits_cloth ],


### - Civilians - Security guard armors:
["ind_clothes_securityguarda1", "Security Guard Armor", [("security_guard_1",0)], itp_merchandise|itp_type_body_armor|itp_attach_armature|itp_covers_legs|itp_civilian, 0, 
 320 , weight(5)|abundance(100)|head_armor(0)|body_armor(25)|leg_armor(12)|difficulty(0) ,imodbits_cloth ],   
["ind_clothes_securityguarda2", "Security Guard Armor", [("security_guard_2",0)], itp_merchandise|itp_type_body_armor|itp_attach_armature|itp_covers_legs|itp_civilian, 0, 
 320 , weight(5)|abundance(100)|head_armor(0)|body_armor(25)|leg_armor(12)|difficulty(0) ,imodbits_cloth ],   
["ind_clothes_securityguarda3", "Security Guard Armor", [("security_guard_3",0)], itp_merchandise|itp_type_body_armor|itp_attach_armature|itp_covers_legs|itp_civilian, 0, 
 320 , weight(5)|abundance(100)|head_armor(0)|body_armor(25)|leg_armor(12)|difficulty(0) ,imodbits_cloth ],   
["ind_clothes_securityguarda4", "Security Guard Armor", [("security_guard_4",0)], itp_merchandise|itp_type_body_armor|itp_attach_armature|itp_covers_legs|itp_civilian, 0, 
 320 , weight(5)|abundance(100)|head_armor(0)|body_armor(25)|leg_armor(12)|difficulty(0) ,imodbits_cloth ],   
["ind_clothes_securityguarda5", "Security Guard Armor", [("security_guard_5",0)], itp_merchandise|itp_type_body_armor|itp_attach_armature|itp_covers_legs|itp_civilian, 0, 
 320 , weight(5)|abundance(100)|head_armor(0)|body_armor(25)|leg_armor(12)|difficulty(0) ,imodbits_cloth ],   


### - Civilians - Tight Coveralls (TAS):
["ind_clothes_tightcoverall_blue", "Tight coverall", [("fem_bodyglove_blue",0)], itp_merchandise|itp_type_body_armor|itp_attach_armature|itp_covers_legs|itp_civilian, 0, 400, weight(10)|abundance(100)|head_armor(0)|body_armor(44)|leg_armor(30)|difficulty(0), imodbits_cloth ], 
["ind_clothes_tightcoverall_red", "Tight coverall", [("fem_bodyglove_red",0)], itp_merchandise|itp_type_body_armor|itp_attach_armature|itp_covers_legs|itp_civilian, 0, 400, weight(10)|abundance(100)|head_armor(0)|body_armor(44)|leg_armor(30)|difficulty(0), imodbits_cloth ], 
["ind_clothes_tightcoverall_green", "Tight coverall", [("fem_bodyglove_green",0)], itp_merchandise|itp_type_body_armor|itp_attach_armature|itp_covers_legs|itp_civilian, 0, 400, weight(10)|abundance(100)|head_armor(0)|body_armor(44)|leg_armor(30)|difficulty(0), imodbits_cloth ], 
["ind_clothes_tightcoverall_wblue", "Tight coverall", [("fem_bodyglove_wblue",0)], itp_merchandise|itp_type_body_armor|itp_attach_armature|itp_covers_legs|itp_civilian, 0, 400, weight(10)|abundance(100)|head_armor(0)|body_armor(44)|leg_armor(30)|difficulty(0), imodbits_cloth ], 
["ind_clothes_tightcoverall_wred", "Tight coverall", [("fem_bodyglove_wred",0)], itp_merchandise|itp_type_body_armor|itp_attach_armature|itp_covers_legs|itp_civilian, 0, 400, weight(10)|abundance(100)|head_armor(0)|body_armor(44)|leg_armor(30)|difficulty(0), imodbits_cloth ], 
["ind_clothes_tightcoverall_sato", "Saato armor", [("saato_armor",0)], itp_merchandise|itp_type_body_armor|itp_attach_armature|itp_covers_legs|itp_civilian, 0, 400, weight(10)|abundance(100)|head_armor(0)|body_armor(44)|leg_armor(30)|difficulty(0), imodbits_cloth ], 

### - Civilians - Outfits (TAS):

# Replaces itm_padded_armor
["ind_clothes_outfsmuggler_red", "Smuggler Outfit", [("smuggler_outfit_1",0)], itp_merchandise|itp_type_body_armor|itp_attach_armature|itp_covers_legs|itp_civilian, 0, 
 320 , weight(5)|abundance(70)|head_armor(0)|body_armor(25)|leg_armor(12)|difficulty(0) ,imodbits_cloth],
["ind_clothes_outfsmuggler_green", "Smuggler Outfit", [("smuggler_outfit_2",0)], itp_merchandise|itp_type_body_armor|itp_attach_armature|itp_covers_legs|itp_civilian, 0, 
 320 , weight(5)|abundance(70)|head_armor(0)|body_armor(25)|leg_armor(12)|difficulty(0) ,imodbits_cloth],
["ind_clothes_outfsmuggleralter1_red", "Smuggler's Jacket", [("smuggler_outfit_3",0)], itp_merchandise|itp_type_body_armor|itp_attach_armature|itp_covers_legs|itp_civilian, 0, 
 320 , weight(5)|abundance(70)|head_armor(0)|body_armor(25)|leg_armor(12)|difficulty(0) ,imodbits_cloth],
["ind_clothes_outfsmuggleralter1_green", "Smuggler's Jacket", [("smuggler_outfit_4",0)], itp_merchandise|itp_type_body_armor|itp_attach_armature|itp_covers_legs|itp_civilian, 0, 
 320 , weight(5)|abundance(70)|head_armor(0)|body_armor(25)|leg_armor(12)|difficulty(0) ,imodbits_cloth],

# Replaces itm_armor
### - Civilians - Hutts (TAS):
["ind_clothes_hutttunic_red", "Hutt tunic", [("hutt_tuniccl1",0)], itp_merchandise|itp_type_body_armor|itp_attach_armature|itp_covers_legs|itp_civilian, 0, 
 400 , weight(5)|abundance(50)|head_armor(0)|body_armor(32)|leg_armor(12)|difficulty(0) ,imodbits_cloth], 
["ind_clothes_hutttunic_grey", "Hutt tunic", [("hutt_tuniccl2",0)], itp_merchandise|itp_type_body_armor|itp_attach_armature|itp_covers_legs|itp_civilian, 0, 
 400 , weight(5)|abundance(50)|head_armor(0)|body_armor(32)|leg_armor(12)|difficulty(0) ,imodbits_cloth], 
["ind_clothes_hutttunic_brown", "Hutt tunic", [("hutt_tuniccl3",0)], itp_merchandise|itp_type_body_armor|itp_attach_armature|itp_covers_legs|itp_civilian, 0, 
 400 , weight(5)|abundance(50)|head_armor(0)|body_armor(32)|leg_armor(12)|difficulty(0) ,imodbits_cloth], 
["ind_clothes_hutttuniccape_red", "Hutt tunic with cape", [("hutt_tunic1",0)], itp_merchandise|itp_type_body_armor|itp_attach_armature|itp_covers_legs|itp_civilian, 0, 
 400 , weight(5)|abundance(50)|head_armor(0)|body_armor(32)|leg_armor(12)|difficulty(0) ,imodbits_cloth], 
["ind_clothes_hutttuniccape_grey", "Hutt tunic with cape", [("hutt_tunic2",0)], itp_merchandise|itp_type_body_armor|itp_attach_armature|itp_covers_legs|itp_civilian, 0, 
 400 , weight(5)|abundance(50)|head_armor(0)|body_armor(32)|leg_armor(12)|difficulty(0) ,imodbits_cloth], 
["ind_clothes_hutttuniccape_brown", "Hutt tunic with cape", [("hutt_tunic3",0)], itp_merchandise|itp_type_body_armor|itp_attach_armature|itp_covers_legs|itp_civilian, 0, 
 400 , weight(5)|abundance(50)|head_armor(0)|body_armor(32)|leg_armor(12)|difficulty(0) ,imodbits_cloth], 

# - Light Mercenary Armor
["ind_arm_lightmercenarya1", "Light Mercenary Armor (A1)", [("light_mercenary_armor",0)], itp_merchandise|itp_type_body_armor|itp_attach_armature|itp_covers_legs|itp_civilian, 0, 
 420 , weight(6)|abundance(100)|head_armor(0)|body_armor(35)|leg_armor(14)|difficulty(0) ,imodbits_cloth ],
["ind_arm_lightmercenarya2", "Light Mercenary Armor (A2)", [("light_mercenary_armor2",0)], itp_merchandise|itp_type_body_armor|itp_attach_armature|itp_covers_legs|itp_civilian, 0, 
 420 , weight(6)|abundance(100)|head_armor(0)|body_armor(35)|leg_armor(14)|difficulty(0) ,imodbits_cloth ],
["ind_arm_lightmercenarya3", "Light Mercenary Armor (A3)", [("light_mercenary_armor3",0)], itp_merchandise|itp_type_body_armor|itp_attach_armature|itp_covers_legs|itp_civilian, 0, 
 420 , weight(6)|abundance(100)|head_armor(0)|body_armor(35)|leg_armor(14)|difficulty(0) ,imodbits_cloth ],
["ind_arm_lightmercenarya4", "Light Mercenary Armor (A4)", [("light_mercenary_armor4",0)], itp_merchandise|itp_type_body_armor|itp_attach_armature|itp_covers_legs|itp_civilian, 0, 
 420 , weight(6)|abundance(100)|head_armor(0)|body_armor(35)|leg_armor(14)|difficulty(0) ,imodbits_cloth ],
["ind_arm_lightmercenaryb1", "Light Mercenary Armor (B1)", [("light_mercenary_armorb",0)], itp_merchandise|itp_type_body_armor|itp_attach_armature|itp_covers_legs|itp_civilian, 0, 
 420 , weight(6)|abundance(100)|head_armor(0)|body_armor(35)|leg_armor(14)|difficulty(0) ,imodbits_cloth ],
["ind_arm_lightmercenaryb2", "Light Mercenary Armor (B2)", [("light_mercenary_armorb2",0)], itp_merchandise|itp_type_body_armor|itp_attach_armature|itp_covers_legs|itp_civilian, 0, 
 420 , weight(6)|abundance(100)|head_armor(0)|body_armor(35)|leg_armor(14)|difficulty(0) ,imodbits_cloth ],
["ind_arm_lightmercenaryb3", "Light Mercenary Armor (B3)", [("light_mercenary_armorb3",0)], itp_merchandise|itp_type_body_armor|itp_attach_armature|itp_covers_legs|itp_civilian, 0, 
 420 , weight(6)|abundance(100)|head_armor(0)|body_armor(35)|leg_armor(14)|difficulty(0) ,imodbits_cloth ],
["ind_arm_lightmercenaryb4", "Light Mercenary Armor (B4)", [("light_mercenary_armorb4",0)], itp_merchandise|itp_type_body_armor|itp_attach_armature|itp_covers_legs|itp_civilian, 0, 
 420 , weight(6)|abundance(100)|head_armor(0)|body_armor(35)|leg_armor(14)|difficulty(0) ,imodbits_cloth ],
["ind_arm_lightmercenaryc1", "Light Mercenary Armor (C1)", [("light_mercenary_armorc",0)], itp_merchandise|itp_type_body_armor|itp_attach_armature|itp_covers_legs|itp_civilian, 0, 
 420 , weight(6)|abundance(100)|head_armor(0)|body_armor(35)|leg_armor(14)|difficulty(0) ,imodbits_cloth ],
["ind_arm_lightmercenaryc2", "Light Mercenary Armor (C2)", [("light_mercenary_armorc2",0)], itp_merchandise|itp_type_body_armor|itp_attach_armature|itp_covers_legs|itp_civilian, 0, 
 420 , weight(6)|abundance(100)|head_armor(0)|body_armor(35)|leg_armor(14)|difficulty(0) ,imodbits_cloth ],
["ind_arm_lightmercenaryc3", "Light Mercenary Armor (C3)", [("light_mercenary_armorc3",0)], itp_merchandise|itp_type_body_armor|itp_attach_armature|itp_covers_legs|itp_civilian, 0, 
 420 , weight(6)|abundance(100)|head_armor(0)|body_armor(35)|leg_armor(14)|difficulty(0) ,imodbits_cloth ],
["ind_arm_lightmercenaryc4", "Light Mercenary Armor (C4)", [("light_mercenary_armorc4",0)], itp_merchandise|itp_type_body_armor|itp_attach_armature|itp_covers_legs|itp_civilian, 0, 
 420 , weight(6)|abundance(100)|head_armor(0)|body_armor(35)|leg_armor(14)|difficulty(0) ,imodbits_cloth ],
["ind_arm_lightmercenaryd1", "Light Mercenary Armor (D1)", [("light_mercenary_armord",0)], itp_merchandise|itp_type_body_armor|itp_attach_armature|itp_covers_legs|itp_civilian, 0, 
 420 , weight(6)|abundance(100)|head_armor(0)|body_armor(35)|leg_armor(14)|difficulty(0) ,imodbits_cloth ],
["ind_arm_lightmercenaryd2", "Light Mercenary Armor (D2)", [("light_mercenary_armord2",0)], itp_merchandise|itp_type_body_armor|itp_attach_armature|itp_covers_legs|itp_civilian, 0, 
 420 , weight(6)|abundance(100)|head_armor(0)|body_armor(35)|leg_armor(14)|difficulty(0) ,imodbits_cloth ],
["ind_arm_lightmercenaryd3", "Light Mercenary Armor (D3)", [("light_mercenary_armord3",0)], itp_merchandise|itp_type_body_armor|itp_attach_armature|itp_covers_legs|itp_civilian, 0, 
 420 , weight(6)|abundance(100)|head_armor(0)|body_armor(35)|leg_armor(14)|difficulty(0) ,imodbits_cloth ],
["ind_arm_lightmercenaryd4", "Light Mercenary Armor (D4)", [("light_mercenary_armord4",0)], itp_merchandise|itp_type_body_armor|itp_attach_armature|itp_covers_legs|itp_civilian, 0, 
 420 , weight(6)|abundance(100)|head_armor(0)|body_armor(35)|leg_armor(14)|difficulty(0) ,imodbits_cloth ],


# - Guard armors (TAS)
#["ind_rep_guardarmor1", "Guard Armor", [("guard_armor1",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs|itp_civilian, 0, 
# 550 , weight(15)|abundance(60)|head_armor(0)|body_armor(50)|leg_armor(20)|difficulty(0) ,imodbits_cloth ], 
["ind_rep_guardarmor2", "Guard Armor", [("guard_armor2",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs|itp_civilian, 0, 
 720 , weight(10)|abundance(100)|head_armor(0)|body_armor(42)|leg_armor(18)|difficulty(0) ,imodbits_armor, [], [] ],
#["ind_rep_guardarmor3", "Guard Armor", [("guard_armor3",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs|itp_civilian, 0, 
# 550 , weight(15)|abundance(60)|head_armor(0)|body_armor(50)|leg_armor(20)|difficulty(0) ,imodbits_cloth ], 

["ind_rep_guardarmor_black", "Guard Armor (Black)", [("guard_armor_black",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs|itp_civilian, 0, 
 720 , weight(10)|abundance(100)|head_armor(0)|body_armor(42)|leg_armor(18)|difficulty(0) ,imodbits_armor, [], hutt_fac ],
["ind_rep_guardarmor_hutt", "Guard Armor (Hutt)", [("guard_armor_hutt",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs|itp_civilian, 0, 
 720 , weight(10)|abundance(100)|head_armor(0)|body_armor(42)|leg_armor(18)|difficulty(0) ,imodbits_armor, [], hutt_fac ],


# - Heavy Armor
["ind_arm_heavyarmor_blue", "Heavy Armor (Blue)", [("heavy_armor2",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs|itp_civilian, 0, 
 800 , weight(10)|abundance(40)|head_armor(0)|body_armor(43)|leg_armor(19)|difficulty(6) ,imodbits_armor, [], [] ],
["ind_arm_heavyarmor_purple", "Heavy Armor (Purple)", [("heavy_armor3",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs|itp_civilian, 0, 
 800 , weight(10)|abundance(40)|head_armor(0)|body_armor(43)|leg_armor(19)|difficulty(6) ,imodbits_armor, [], [] ],
["ind_arm_heavyarmor_green", "Heavy Armor (Green)", [("heavy_armor4",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs|itp_civilian, 0, 
 800 , weight(10)|abundance(40)|head_armor(0)|body_armor(43)|leg_armor(19)|difficulty(6) ,imodbits_armor, [], [] ],

# Gave to Hutt Palace Guard
["ind_arm_heavyarmor_silver", "Heavy Armor (Silver)", [("heavy_armor5",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs|itp_civilian, 0, 
 800 , weight(10)|abundance(40)|head_armor(0)|body_armor(43)|leg_armor(19)|difficulty(6) ,imodbits_armor, [], hutt_fac],
["ind_helm_heavyhelmet_silver", "Heavy Helmet (Silver)", [("heavy_helmet5",0)], itp_merchandise|itp_type_head_armor|itp_covers_head|itp_civilian ,0, 
 271 , weight(2)|abundance(40)|head_armor(18)|body_armor(0)|leg_armor(0)|difficulty(5) ,imodbits_armor, [], hutt_fac ],
["ind_arm_heavyarmor_gold", "Heavy Armor (Gold)", [("heavy_armor",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs|itp_civilian, 0, 
 800 , weight(10)|abundance(40)|head_armor(0)|body_armor(43)|leg_armor(19)|difficulty(6) ,imodbits_armor, [], hutt_fac],
["ind_helm_heavyhelmet_gold", "Heavy Helmet (Gold)", [("heavy_helmet",0)], itp_merchandise|itp_type_head_armor|itp_covers_head|itp_civilian ,0, 
 271 , weight(2)|abundance(40)|head_armor(18)|body_armor(0)|leg_armor(0)|difficulty(5) ,imodbits_armor, [], hutt_fac ],

["ind_helm_heavyhelmet_blue", "Heavy Helmet (Blue)", [("heavy_helmet2",0)], itp_merchandise|itp_type_head_armor|itp_covers_head|itp_civilian ,0, 
 271 , weight(2)|abundance(40)|head_armor(18)|body_armor(0)|leg_armor(0)|difficulty(5) ,imodbits_armor, [], [] ],
["ind_helm_heavyhelmet_purple", "Heavy Helmet (Purple)", [("heavy_helmet3",0)], itp_merchandise|itp_type_head_armor|itp_covers_head|itp_civilian ,0, 
 271 , weight(2)|abundance(40)|head_armor(18)|body_armor(0)|leg_armor(0)|difficulty(5) ,imodbits_armor, [], [] ],
["ind_helm_heavyhelmet_green", "Heavy Helmet (Green)", [("heavy_helmet4",0)], itp_merchandise|itp_type_head_armor|itp_covers_head|itp_civilian ,0, 
 271 , weight(2)|abundance(40)|head_armor(18)|body_armor(0)|leg_armor(0)|difficulty(5) ,imodbits_armor, [], [] ],



# uniforms for imperial officers
["imperial_uniform_black", "Imperial Officer Uniform", [("imperial_uniform_black",0)], itp_merchandise| itp_type_body_armor |itp_covers_legs |itp_civilian  ,0, 
 580 , weight(2)|abundance(100)|head_armor(0)|body_armor(42)|leg_armor(18)|difficulty(0) ,imodbits_cloth, [], empire_fac ],
["imperial_uniform_green", "Imperial Officer Uniform", [("imperial_uniform_green",0)], itp_merchandise| itp_type_body_armor |itp_covers_legs |itp_civilian  ,0, 
 660 , weight(2)|abundance(100)|head_armor(0)|body_armor(46)|leg_armor(22)|difficulty(0) ,imodbits_cloth, [], empire_fac ],
# uniforms for rebel officers
["rebel_uniform_tanblue", "Rebel Commander Uniform", [("rebel_uniform_tanblue",0)], itp_merchandise| itp_type_body_armor |itp_covers_legs |itp_civilian  ,0, 
 580 , weight(2)|abundance(100)|head_armor(0)|body_armor(42)|leg_armor(18)|difficulty(0) ,imodbits_cloth, [], rebel_fac ],
["rebel_uniform_green", "Rebel Officer Uniform", [("rebel_uniform_green",0)], itp_merchandise| itp_type_body_armor |itp_covers_legs |itp_civilian  ,0, 
 410 , weight(2)|abundance(100)|head_armor(0)|body_armor(35)|leg_armor(14)|difficulty(0) ,imodbits_cloth, [], rebel_fac ],
#tier 1 faction troop equipment (keep them similar stats so game is balanced)

#tier 2 faction troop equipment (keep them similar stats so game is balanced)
["imperial_trooper_armor", "Imperial Trooper Armor", [("impinfantry",0)], itp_merchandise| itp_type_body_armor|itp_covers_legs|itp_civilian,0, 
 320 , weight(5)|abundance(100)|head_armor(0)|body_armor(25)|leg_armor(12)|difficulty(0) ,imodbits_cloth, [], empire_fac ], 
["imperial_navy_trooper_armor", "Imperial Navy Trooper Armor", [("imperial_navy_uniform",0)], itp_merchandise| itp_type_body_armor|itp_covers_legs|itp_civilian,0, 
 320 , weight(5)|abundance(100)|head_armor(0)|body_armor(25)|leg_armor(12)|difficulty(0) ,imodbits_cloth, [], empire_fac ], 
["imperial_trooper_armor", "Imperial Trooper Armor", [("impinfantry",0)], itp_merchandise| itp_type_body_armor|itp_covers_legs|itp_civilian,0, 
 320 , weight(5)|abundance(100)|head_armor(0)|body_armor(25)|leg_armor(12)|difficulty(0) ,imodbits_cloth, [], empire_fac ],   

["rebel_technician_armor", "Rebel Cadet Armor", [("rebel_tech_armor",0)], itp_merchandise| itp_type_body_armor|itp_covers_legs|itp_civilian,0, 
 320 , weight(5)|abundance(100)|head_armor(0)|body_armor(25)|leg_armor(12)|difficulty(0) ,imodbits_cloth, [], rebel_fac ],   
["republic_trooper_armor", "Rebel Trooper Armor", [("republic_trooper_armor",0)], itp_merchandise| itp_type_body_armor |itp_covers_legs |itp_civilian  ,0, 
 340 , weight(6)|abundance(100)|head_armor(0)|body_armor(35)|leg_armor(12)|difficulty(0) ,imodbits_cloth, [], rebel_fac ],
["rebel_heavy_trooper_armor", "Rebel Heavy Trooper Armor", [("guard_armor1",0)], itp_merchandise|itp_type_body_armor |itp_covers_legs |itp_civilian  ,0, 
 550 , weight(10)|abundance(60)|head_armor(0)|body_armor(50)|leg_armor(20)|difficulty(0) ,imodbits_armor, [], rebel_fac ], 
["rebel_heavy_trooper_armor_1", "Rebel Heavy Trooper Armor", [("guard_armor3",0)], itp_merchandise|itp_type_body_armor |itp_covers_legs |itp_civilian  ,0, 
 550 , weight(10)|abundance(60)|head_armor(0)|body_armor(50)|leg_armor(20)|difficulty(0) ,imodbits_armor, [], rebel_fac ],

#jedi/sith tier 2 troop equipment (keep them similar stats so game is balanced)
["jedi_initiate_robe", "Jedi Initiate Robe", [("jedi_padawan_robe1",0)], itp_merchandise| itp_type_body_armor |itp_civilian |itp_covers_legs |itp_civilian,0, 
 406 , weight(1.4)|abundance(80)|head_armor(0)|body_armor(25)|leg_armor(8)|difficulty(0) ,imodbits_cloth, [], jedi_fac ],
["jedi_padawan_robe", "Jedi Padawan Robe", [("jedi_padawan_robe2",0)], itp_merchandise| itp_type_body_armor |itp_civilian |itp_covers_legs |itp_civilian,0, 
 478 , weight(1.2)|abundance(80)|head_armor(0)|body_armor(28)|leg_armor(10)|difficulty(0) ,imodbits_cloth, [], jedi_fac ],
["sith_acolyte_outfit", "Sith Acolyte Outfit", [("ragged_outfit_a",0)], itp_merchandise| itp_type_body_armor |itp_civilian |itp_covers_legs ,0, 
 350 , weight(1.4)|abundance(80)|head_armor(0)|body_armor(25)|leg_armor(8)|difficulty(0) ,imodbits_cloth, [], sith_fac ],
["sith_apprentice_outfit", "Sith Apprentice Outfit", [("nomad_robe_a",0)], itp_merchandise| itp_type_body_armor |itp_civilian |itp_covers_legs ,0, 
 478 , weight(1.2)|abundance(80)|head_armor(0)|body_armor(28)|leg_armor(10)|difficulty(0) ,imodbits_cloth, [], sith_fac ],

#tier 3 faction troop equipment (keep them similar stats so game is balanced)
["imperial_scout_trooper_armor", "Imperial Scout Trooper Armor", [("scoutarmour",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs|itp_civilian, 0, 
 610 , weight(6)|abundance(100)|head_armor(0)|body_armor(35)|leg_armor(14)|difficulty(0) ,imodbits_armor, [], empire_fac ],
["shadow_scout_trooper_armor", "Shadow Scout Trooper Armor", [("shadow_scoutarmour",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs|itp_civilian, 0, 
 720 , weight(5)|abundance(60)|head_armor(0)|body_armor(40)|leg_armor(16)|difficulty(0) ,imodbits_armor, [], empire_fac ], 

["republic_pilot_armor", "Rebel Pilot Armor", [("republic_pilot_armor",0)], itp_merchandise| itp_type_body_armor |itp_covers_legs |itp_civilian  ,0, 
 320 , weight(6)|abundance(100)|head_armor(0)|body_armor(35)|leg_armor(14)|difficulty(0) ,imodbits_cloth, [], rebel_fac ],
["republic_commando_armor", "Rebel Commando Armor", [("republic_commando_armor",0)], itp_merchandise| itp_type_body_armor |itp_covers_legs |itp_civilian  ,0, 
 480 , weight(10)|abundance(80)|head_armor(0)|body_armor(42)|leg_armor(18)|difficulty(0) ,imodbits_cloth, [], rebel_fac ],
["republic_commando_desert_armor", "Rebel Desert Commando Armor", [("republic_commando_desert_armor",0)], itp_merchandise| itp_type_body_armor |itp_covers_legs |itp_civilian  ,0, 
 480 , weight(10)|abundance(40)|head_armor(0)|body_armor(42)|leg_armor(18)|difficulty(0) ,imodbits_cloth, [], rebel_fac ],
["republic_commando_urban_armor", "Rebel Urban Commando Armor", [("republic_commando_urban_armor",0)], itp_merchandise| itp_type_body_armor |itp_covers_legs |itp_civilian  ,0, 
 480 , weight(10)|abundance(40)|head_armor(0)|body_armor(42)|leg_armor(18)|difficulty(0) ,imodbits_cloth, [], rebel_fac ],
["rebel_sniper_armor", "Rebel Sniper Armor", [("republic_commando_armor_b",0)], itp_merchandise| itp_type_body_armor |itp_covers_legs |itp_civilian  ,0, 
 480 , weight(10)|abundance(60)|head_armor(0)|body_armor(42)|leg_armor(18)|difficulty(0) ,imodbits_cloth, [], rebel_fac ], 

["imperial_stormtrooper_armor", "Imperial Stormtrooper Armor", [("Stormtrooper_body",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs|itp_civilian, 0, 
 720 , weight(10)|abundance(100)|head_armor(0)|body_armor(42)|leg_armor(18)|difficulty(0) ,imodbits_armor, [], empire_fac ],
["imperial_stormtrooper_armor_incinerator", "Incinerator Trooper Armor", [("Incinerator_Trooper_body",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs|itp_civilian, 0, 
 1263, weight(10)|abundance(30)|head_armor(0)|body_armor(45)|leg_armor(21)|difficulty(9) ,imodbits_armor, [], empire_fac ],
["imperial_stormtrooper_armor_novatrooper", "Novatrooper Armor", [("Novatrooper_body",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs|itp_civilian, 0, 
 840 , weight(10)|abundance(40)|head_armor(0)|body_armor(43)|leg_armor(19)|difficulty(6) ,imodbits_armor, [], empire_fac ],
["imperial_stormtrooper_armor", "Imperial Stormtrooper Armor", [("Stormtrooper_body",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs|itp_civilian, 0, 
 720 , weight(10)|abundance(100)|head_armor(0)|body_armor(42)|leg_armor(18)|difficulty(0) ,imodbits_armor, [], empire_fac ],

["rebel_honor_guard_armor", "Rebel Honor Guard Armor", [("outfit_green",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs|itp_civilian, 0, 
 760 , weight(6)|abundance(50)|head_armor(0)|body_armor(44)|leg_armor(20)|difficulty(0) ,imodbits_armor, [], rebel_fac ],  
 
#SW - removed merchandise flag since they will appear in a clone era merchant 
["clone_trooper_armor_white", "Clone Trooper Armor", [("ArcTrooperWhite",0)], itp_type_body_armor|itp_covers_legs|itp_civilian, 0, 500 , weight(12)|abundance(100)|head_armor(0)|body_armor(34)|leg_armor(10)|difficulty(0) ,imodbits_armor ], 
["clone_trooper_armor_green", "Clone Trooper Armor", [("ArcTrooperGreen_plain",0)], itp_type_body_armor|itp_covers_legs|itp_civilian, 0, 560 , weight(12)|abundance(100)|head_armor(0)|body_armor(36)|leg_armor(12)|difficulty(0) ,imodbits_armor ], 
["clone_trooper_armor_blue", "Clone Trooper Armor", [("ArcTrooperBlue_plain",0)], itp_type_body_armor|itp_covers_legs|itp_civilian, 0, 620 , weight(12)|abundance(100)|head_armor(0)|body_armor(38)|leg_armor(14)|difficulty(0) ,imodbits_armor ], 
["clone_trooper_armor_red", "Clone Trooper Armor", [("ArcTrooperRed_plain",0)], itp_type_body_armor|itp_covers_legs|itp_civilian, 0, 680 , weight(12)|abundance(100)|head_armor(0)|body_armor(40)|leg_armor(16)|difficulty(0) ,imodbits_armor ], 
["clone_trooper_armor_yellow", "Clone Trooper Armor", [("ArcTrooperYellow_plain",0)], itp_type_body_armor|itp_covers_legs|itp_civilian, 0, 740 , weight(12)|abundance(100)|head_armor(0)|body_armor(42)|leg_armor(18)|difficulty(0) ,imodbits_armor ],  
["clone_trooper_armor_orange", "Clone Trooper Armor", [("ArcTrooperOrange_plain",0)], itp_type_body_armor|itp_covers_legs|itp_civilian, 0, 740 , weight(12)|abundance(100)|head_armor(0)|body_armor(42)|leg_armor(18)|difficulty(0) ,imodbits_armor ], 
["clone_trooper_armor_mand", "Clone Trooper Armor", [("ArcTrooperMand_plain",0)], itp_type_body_armor|itp_covers_legs|itp_civilian, 0, 740 , weight(12)|abundance(100)|head_armor(0)|body_armor(42)|leg_armor(18)|difficulty(0) ,imodbits_armor ], 
["clone_trooper_armor_lux", "Clone Trooper Armor", [("ArcTrooperLux_plain",0)], itp_type_body_armor|itp_covers_legs|itp_civilian, 0, 740 , weight(12)|abundance(100)|head_armor(0)|body_armor(42)|leg_armor(18)|difficulty(0) ,imodbits_armor ], 
["arc_trooper_armor_green", "Arc Trooper Armor", [("ArcTrooperGreen",0)], itp_type_body_armor|itp_covers_legs|itp_civilian, 0, 600 , weight(10)|abundance(100)|head_armor(0)|body_armor(38)|leg_armor(14)|difficulty(0) ,imodbits_armor ], 
["arc_trooper_armor_blue", "Arc Trooper Armor", [("ArcTrooperBlue",0)], itp_type_body_armor|itp_covers_legs|itp_civilian, 0, 660 , weight(10)|abundance(100)|head_armor(0)|body_armor(40)|leg_armor(16)|difficulty(0) ,imodbits_armor ], 
["arc_trooper_armor_red", "Arc Trooper Armor", [("ArcTrooperRed",0)], itp_type_body_armor|itp_covers_legs|itp_civilian, 0, 720 , weight(10)|abundance(100)|head_armor(0)|body_armor(42)|leg_armor(18)|difficulty(0) ,imodbits_armor ], 
["arc_trooper_armor_yellow", "Arc Trooper Armor", [("ArcTrooperYellow",0)], itp_type_body_armor|itp_covers_legs|itp_civilian, 0, 780 , weight(10)|abundance(100)|head_armor(0)|body_armor(44)|leg_armor(20)|difficulty(0) ,imodbits_armor ],  
["arc_trooper_armor_orange", "Arc Trooper Armor", [("ArcTrooperOrange",0)], itp_type_body_armor|itp_covers_legs|itp_civilian, 0, 780 , weight(10)|abundance(100)|head_armor(0)|body_armor(44)|leg_armor(20)|difficulty(0) ,imodbits_armor ], 
["arc_trooper_armor_mand", "Arc Trooper Armor", [("ArcTrooperMand",0)], itp_type_body_armor|itp_covers_legs|itp_civilian, 0, 780 , weight(10)|abundance(100)|head_armor(0)|body_armor(44)|leg_armor(20)|difficulty(0) ,imodbits_armor ], 
["arc_trooper_armor_lux", "Arc Trooper Armor", [("ArcTrooperLux",0)], itp_type_body_armor|itp_covers_legs|itp_civilian, 0, 780 , weight(10)|abundance(100)|head_armor(0)|body_armor(44)|leg_armor(20)|difficulty(0) ,imodbits_armor ], 
["clone_commando_armor", "Clone Commando Armor", [("clonecommando_armor",0)], itp_type_body_armor|itp_covers_legs|itp_civilian, 0, 1280 , weight(20)|abundance(80)|head_armor(0)|body_armor(52)|leg_armor(22)|difficulty(0) ,imodbits_armor ], 
 
 
["skiff_guard_armor_brown", "Skiff Guard Armor", [("sw_armor1_brown",0)], itp_merchandise| itp_type_body_armor |itp_covers_legs |itp_civilian  ,0, 
 400 , weight(4)|abundance(50)|head_armor(0)|body_armor(32)|leg_armor(12)|difficulty(0) ,imodbits_cloth, [], hutt_fac ],
["skiff_guard_armor_grey", "Skiff Guard Armor", [("sw_armor1_grey",0)], itp_merchandise| itp_type_body_armor |itp_covers_legs |itp_civilian  ,0, 
 400 , weight(4)|abundance(50)|head_armor(0)|body_armor(32)|leg_armor(12)|difficulty(0) ,imodbits_cloth, [], hutt_fac ],
["skiff_guard_armor_white", "Skiff Guard Armor", [("sw_armor1_white",0)], itp_merchandise| itp_type_body_armor |itp_covers_legs |itp_civilian  ,0, 
 400 , weight(4)|abundance(50)|head_armor(0)|body_armor(32)|leg_armor(12)|difficulty(0) ,imodbits_cloth, [], hutt_fac ], 
["hutt_palace_guard_armor", "Hutt Palace Guard Armor", [("nobleman_outfit_b",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs|itp_civilian   ,0, 
 500 , weight(4)|abundance(100)|head_armor(0)|body_armor(38)|leg_armor(16)|difficulty(0) ,imodbits_cloth, [], hutt_fac ], 

#jedi/sith tier 3 troop equipment (keep them similar stats so game is balanced)
["jedi_knight_robe", "Jedi Knight Robe", [("jedi_knight_robe",0)], itp_merchandise| itp_type_body_armor |itp_civilian |itp_covers_legs |itp_civilian,0, 
 722 , weight(0.8)|abundance(55)|head_armor(0)|body_armor(30)|leg_armor(10)|difficulty(0) ,imodbits_cloth, [], jedi_fac ],
["jedi_knight_robe_unique", "Jedi Knight Robe", [("jedi_knight_robe",0)], itp_unique| itp_type_body_armor |itp_civilian |itp_covers_legs |itp_civilian,0, 
 722 , weight(0.8)|abundance(0)|head_armor(10)|body_armor(45)|leg_armor(18)|difficulty(0) ,imodbits_cloth, [], jedi_fac ], 
["jedi_guardian_robe_a", "Jedi Guardian Robe", [("jedi_guardian_a",0)], itp_merchandise| itp_type_body_armor |itp_civilian |itp_covers_legs |itp_civilian,0, 
 722 , weight(0.8)|abundance(50)|head_armor(10)|body_armor(45)|leg_armor(18)|difficulty(0) ,imodbits_cloth, [], jedi_fac ], 
["jedi_guardian_robe_b", "Jedi Guardian Robe", [("jedi_guardian_b",0)], itp_merchandise| itp_type_body_armor |itp_civilian |itp_covers_legs |itp_civilian,0, 
 722 , weight(0.8)|abundance(50)|head_armor(10)|body_armor(45)|leg_armor(18)|difficulty(0) ,imodbits_cloth, [], jedi_fac ], 
["jedi_guardian_robe_c", "Jedi Guardian Robe", [("jedi_guardian_c",0)], itp_merchandise| itp_type_body_armor |itp_civilian |itp_covers_legs |itp_civilian,0, 
 722 , weight(0.8)|abundance(50)|head_armor(10)|body_armor(45)|leg_armor(18)|difficulty(0) ,imodbits_cloth, [], jedi_fac ], 
["jedi_guardian_robe_d", "Jedi Guardian Robe", [("jedi_guardian_d",0)], itp_merchandise| itp_type_body_armor |itp_civilian |itp_covers_legs |itp_civilian,0, 
 722 , weight(0.8)|abundance(50)|head_armor(10)|body_armor(45)|leg_armor(18)|difficulty(0) ,imodbits_cloth, [], jedi_fac ], 

["sith_knight_robe", "Sith Knight Robe", [("jedi_master_robe_black",0)], itp_merchandise| itp_type_body_armor |itp_civilian |itp_covers_legs |itp_civilian,0, 
 722 , weight(0.8)|abundance(55)|head_armor(10)|body_armor(30)|leg_armor(10)|difficulty(0) ,imodbits_cloth, [], sith_fac ],
["sith_knight_robe_unique", "Sith Knight Robe", [("jedi_master_robe_black",0)], itp_unique| itp_type_body_armor |itp_civilian |itp_covers_legs |itp_civilian,0, 
 722 , weight(0.8)|abundance(0)|head_armor(10)|body_armor(45)|leg_armor(18)|difficulty(0) ,imodbits_cloth, [], sith_fac ], 
["sith_knight_robe_a", "Sith Knight Robe", [("sith_knight_robe_a",0)], itp_merchandise| itp_type_body_armor |itp_civilian |itp_covers_legs |itp_civilian,0, 
 722 , weight(0.8)|abundance(50)|head_armor(10)|body_armor(45)|leg_armor(18)|difficulty(0) ,imodbits_cloth, [], sith_fac ], 
["sith_knight_robe_b", "Sith Knight Robe", [("sith_knight_robe_b",0)], itp_merchandise| itp_type_body_armor |itp_civilian |itp_covers_legs |itp_civilian,0, 
 722 , weight(0.8)|abundance(50)|head_armor(10)|body_armor(45)|leg_armor(18)|difficulty(0) ,imodbits_cloth, [], sith_fac ], 
["sith_knight_robe_c", "Sith Knight Robe", [("sith_knight_robe_c",0)], itp_merchandise| itp_type_body_armor |itp_civilian |itp_covers_legs |itp_civilian,0, 
 722 , weight(0.8)|abundance(50)|head_armor(10)|body_armor(45)|leg_armor(18)|difficulty(0) ,imodbits_cloth, [], sith_fac ], 

#tier 4 faction troop equipment (keep them similar stats so game is balanced)
["imperial_royal_guard_robe", "Imperial Royal Guard Robe", [("imperial_royal_guard_robe",0)], itp_merchandise| itp_type_body_armor |itp_covers_legs |itp_civilian  ,0, 
 855 , weight(10)|abundance(80)|head_armor(0)|body_armor(45)|leg_armor(22)|difficulty(0) ,imodbits_armor, [], empire_fac ],
["shadow_guard_robe", "Imperial Shadow Guard Robe", [("shadow_guard_robe",0)], itp_merchandise| itp_type_body_armor |itp_covers_legs |itp_civilian  ,0, 
 900 , weight(8)|abundance(40)|head_armor(0)|body_armor(50)|leg_armor(25)|difficulty(0) ,imodbits_armor, [], empire_fac ], 
#["imperial_stormtrooper_armor_black", "Imperial Darktrooper Armor", [("imperial_stormtrooper_armor_black",0)], itp_merchandise| itp_type_body_armor |itp_covers_legs |itp_civilian  ,0, 
# 500 , weight(12)|abundance(100)|head_armor(0)|body_armor(45)|leg_armor(22)|difficulty(0) ,imodbits_armor ],
["imperial_stormtrooper_armor_officer", "Imperial Stormtrooper Officer Armor", [("Sandtrooper_body_orangepauldron",0)], itp_merchandise|itp_type_body_armor|itp_covers_legs|itp_civilian, 0, 
 825 , weight(12)|abundance(80)|head_armor(0)|body_armor(45)|leg_armor(22)|difficulty(0) ,imodbits_armor, [], empire_fac ], 
#["sw_desert_armor", "Heavy Desert Armor", [("desert_armor_heavy",0)], itp_merchandise| itp_type_body_armor |itp_covers_legs |itp_civilian  ,0, 
# 795 , weight(14)|abundance(60)|head_armor(0)|body_armor(45)|leg_armor(22)|difficulty(0) ,imodbits_armor ],
#["sw_urban_armor", "Heavy Urban Armor", [("urban_armor_heavy",0)], itp_merchandise| itp_type_body_armor |itp_covers_legs |itp_civilian  ,0, 
# 795 , weight(14)|abundance(60)|head_armor(0)|body_armor(45)|leg_armor(22)|difficulty(0) ,imodbits_armor ],
#["sw_sniper_armor", "Sniper Armor", [("kevlarvest_woodland",0)], itp_merchandise| itp_type_body_armor |itp_civilian  ,0, 
# 885 , weight(8)|abundance(80)|head_armor(0)|body_armor(45)|leg_armor(22)|difficulty(0) ,imodbits_armor ],

#new jedi robes 
["jedi_robe_a", "Jedi Robe", [("jedi_robe_a",0)], itp_merchandise| itp_type_body_armor |itp_civilian |itp_covers_legs |itp_civilian,0, 
 765 , weight(0.3)|abundance(40)|head_armor(0)|body_armor(40)|leg_armor(14)|difficulty(0) ,imodbits_cloth, [], jedi_fac ], 
["jedi_robe_a_unique", "Jedi Robe", [("jedi_robe_a",0)], itp_unique| itp_type_body_armor |itp_civilian |itp_covers_legs |itp_civilian,0, 
 765 , weight(0.3)|abundance(0)|head_armor(10)|body_armor(60)|leg_armor(24)|difficulty(0) ,imodbits_cloth, [], jedi_fac  ],  
["jedi_robe_b", "Sith Robe", [("jedi_robe_b",0)], itp_merchandise| itp_type_body_armor |itp_civilian |itp_covers_legs |itp_civilian,0, 
 765 , weight(0.3)|abundance(40)|head_armor(0)|body_armor(40)|leg_armor(14)|difficulty(0) ,imodbits_cloth, [], jedi_fac  ], 
["jedi_robe_b_long", "Long Sith Robe", [("jedi_robe_b_long",0)], itp_merchandise| itp_type_body_armor |itp_civilian |itp_covers_legs |itp_civilian,0, 
 865 , weight(0.3)|abundance(40)|head_armor(0)|body_armor(46)|leg_armor(18)|difficulty(0) ,imodbits_cloth, [], jedi_fac  ], 
["jedi_robe_c", "Jedi Robe", [("jedi_robe_c",0)], itp_merchandise| itp_type_body_armor |itp_civilian |itp_covers_legs |itp_civilian,0, 
 765 , weight(0.3)|abundance(40)|head_armor(0)|body_armor(40)|leg_armor(14)|difficulty(0) ,imodbits_cloth, [], jedi_fac  ], 
["jedi_robe_c_long", "Long Sith Robe", [("jedi_robe_c_long",0)], itp_merchandise| itp_type_body_armor |itp_civilian |itp_covers_legs |itp_civilian,0, 
 865 , weight(0.3)|abundance(40)|head_armor(0)|body_armor(46)|leg_armor(18)|difficulty(0) ,imodbits_cloth, [], jedi_fac  ], 
["jedi_robe_d", "Jedi Robe", [("jedi_robe_d",0)], itp_merchandise| itp_type_body_armor |itp_civilian |itp_covers_legs |itp_civilian,0, 
 765 , weight(0.3)|abundance(40)|head_armor(0)|body_armor(40)|leg_armor(14)|difficulty(0) ,imodbits_cloth, [], jedi_fac  ], 
["jedi_robe_d_unique", "Jedi Robe", [("jedi_robe_d",0)], itp_unique| itp_type_body_armor |itp_civilian |itp_covers_legs |itp_civilian,0, 
 765 , weight(0.3)|abundance(0)|head_armor(10)|body_armor(60)|leg_armor(24)|difficulty(0) ,imodbits_cloth, [], jedi_fac  ],  
["jedi_robe_e", "Jedi Robe", [("jedi_robe_e",0)], itp_merchandise| itp_type_body_armor |itp_civilian |itp_covers_legs |itp_civilian,0, 
 765 , weight(0.3)|abundance(40)|head_armor(0)|body_armor(40)|leg_armor(14)|difficulty(0) ,imodbits_cloth, [], jedi_fac  ], 
["jedi_robe_e_unique", "Jedi Robe", [("jedi_robe_e",0)], itp_unique| itp_type_body_armor |itp_civilian |itp_covers_legs |itp_civilian,0, 
 765 , weight(0.3)|abundance(0)|head_armor(10)|body_armor(60)|leg_armor(24)|difficulty(0) ,imodbits_cloth, [], jedi_fac  ],  
["jedi_robe_f", "Jedi Robe", [("jedi_robe_f",0)], itp_merchandise| itp_type_body_armor |itp_civilian |itp_covers_legs |itp_civilian,0, 
 765 , weight(0.3)|abundance(40)|head_armor(0)|body_armor(40)|leg_armor(14)|difficulty(0) ,imodbits_cloth, [], jedi_fac  ],  
["jedi_robe_f_unique", "Jedi Robe", [("jedi_robe_f",0)], itp_unique| itp_type_body_armor |itp_civilian |itp_covers_legs |itp_civilian,0, 
 765 , weight(0.3)|abundance(0)|head_armor(10)|body_armor(60)|leg_armor(24)|difficulty(0) ,imodbits_cloth, [], jedi_fac  ],   
 
#jedi/sith tier 4 troop equipment (keep them similar stats so game is balanced)
["jedi_master_robe", "Jedi Robe", [("jedi_master_robe",0)], itp_merchandise| itp_type_body_armor |itp_civilian |itp_covers_legs |itp_civilian,0, 
 740 , weight(0.4)|abundance(80)|head_armor(0)|body_armor(35)|leg_armor(12)|difficulty(0) ,imodbits_cloth, [], jedi_fac  ],
["jedi_master_robe_unique", "Jedi Robe", [("jedi_master_robe",0)], itp_unique| itp_type_body_armor |itp_civilian |itp_covers_legs |itp_civilian,0, 
 866 , weight(0.4)|abundance(0)|head_armor(10)|body_armor(60)|leg_armor(24)|difficulty(0) ,imodbits_cloth, [], jedi_fac  ], 

["sith_marauder_robe", "Sith Marauder Robe", [("sith_master_robe",0)], itp_merchandise| itp_type_body_armor |itp_civilian |itp_covers_legs |itp_civilian,0, 
 740 , weight(0.4)|abundance(80)|head_armor(0)|body_armor(35)|leg_armor(12)|difficulty(0) ,imodbits_cloth, [], sith_fac  ],
["sith_marauder_robe_unique", "Sith Marauder Robe", [("sith_master_robe",0)], itp_unique| itp_type_body_armor |itp_civilian |itp_covers_legs |itp_civilian,0, 
 866 , weight(0.4)|abundance(0)|head_armor(10)|body_armor(55)|leg_armor(22)|difficulty(0) ,imodbits_cloth, [], sith_fac ], 
["sith_marauder_robe_a", "Sith Marauder Robe", [("sith_marauder_robe_a",0)], itp_unique| itp_type_body_armor |itp_civilian |itp_covers_legs |itp_civilian,0, 
 866 , weight(0.4)|abundance(0)|head_armor(10)|body_armor(55)|leg_armor(22)|difficulty(0) ,imodbits_cloth, [], sith_fac ], 
["sith_marauder_robe_b", "Sith Marauder Robe", [("sith_marauder_robe_b",0)], itp_unique| itp_type_body_armor |itp_civilian |itp_covers_legs |itp_civilian,0, 
 866 , weight(0.4)|abundance(0)|head_armor(10)|body_armor(55)|leg_armor(22)|difficulty(0) ,imodbits_cloth, [], sith_fac ], 
["sith_marauder_robe_c", "Sith Marauder Robe", [("sith_marauder_robe_c",0)], itp_unique| itp_type_body_armor |itp_civilian |itp_covers_legs |itp_civilian,0, 
 866 , weight(0.4)|abundance(0)|head_armor(10)|body_armor(55)|leg_armor(22)|difficulty(0) ,imodbits_cloth, [], sith_fac ], 
["sith_marauder_robe_d", "Sith Marauder Robe", [("sith_marauder_robe_d",0)], itp_unique| itp_type_body_armor |itp_civilian |itp_covers_legs |itp_civilian,0, 
 866 , weight(0.4)|abundance(0)|head_armor(10)|body_armor(55)|leg_armor(22)|difficulty(0) ,imodbits_cloth, [], sith_fac ], 
 
 #jedi/sith tier 5 troop equipment (keep them similar stats so game is balanced)
#["jedi_councilor_robe", "Jedi Robe", [("jedi_master_robe",0)], itp_merchandise| itp_type_body_armor |itp_civilian |itp_covers_legs |itp_civilian,0, 
# 866 , weight(0.2)|abundance(60)|head_armor(5)|body_armor(45)|leg_armor(16)|difficulty(0) ,imodbits_cloth ],
#["jedi_councilor_robe_unique", "Jedi Robe", [("jedi_master_robe",0)], itp_unique| itp_type_body_armor |itp_civilian |itp_covers_legs |itp_civilian,0, 
# 1008 , weight(0.2)|abundance(0)|head_armor(15)|body_armor(60)|leg_armor(26)|difficulty(0) ,imodbits_cloth ],
["sith_master_robe", "Sith Master Robe", [("sith_lord_robe",0)], itp_merchandise| itp_type_body_armor |itp_civilian |itp_covers_legs |itp_civilian,0, 
 866 , weight(0.2)|abundance(60)|head_armor(5)|body_armor(45)|leg_armor(16)|difficulty(0) ,imodbits_cloth, [], sith_fac ],
["sith_master_robe_unique", "Sith Master Robe", [("sith_robe_a",0)], itp_unique| itp_type_body_armor |itp_civilian |itp_covers_legs |itp_civilian,0, 
 1008 , weight(0.2)|abundance(0)|head_armor(15)|body_armor(60)|leg_armor(26)|difficulty(0) ,imodbits_cloth, [], sith_fac ], 

 
#guards
["guard_armor", "Guard Armor", [("sw_armor2",0)], itp_merchandise| itp_type_body_armor |itp_covers_legs |itp_civilian  ,0, 
 290 , weight(5)|abundance(70)|head_armor(0)|body_armor(28)|leg_armor(10)|difficulty(0) ,imodbits_cloth ],
["guard_armor_red", "Guardian Armor", [("sw_armor2_red",0)], itp_merchandise| itp_type_body_armor |itp_covers_legs |itp_civilian  ,0, 
 430 , weight(5)|abundance(70)|head_armor(0)|body_armor(28)|leg_armor(12)|difficulty(0) ,imodbits_cloth ],
["blast_armor_black", "Blast Armor", [("blast_armour_black",0)], itp_merchandise| itp_type_body_armor |itp_covers_legs |itp_civilian  ,0, 
 430 , weight(5)|abundance(60)|head_armor(0)|body_armor(35)|leg_armor(14)|difficulty(0) ,imodbits_cloth ], 
["blast_armor_red", "Blast Armor", [("blast_armour_red",0)], itp_merchandise| itp_type_body_armor |itp_covers_legs |itp_civilian  ,0, 
 430 , weight(5)|abundance(60)|head_armor(0)|body_armor(35)|leg_armor(14)|difficulty(0) ,imodbits_cloth ], 
["blast_armor_grey", "Blast Armor", [("blast_armour_grey",0)], itp_merchandise| itp_type_body_armor |itp_covers_legs |itp_civilian  ,0, 
 430 , weight(5)|abundance(60)|head_armor(0)|body_armor(35)|leg_armor(14)|difficulty(0) ,imodbits_cloth ], 
["blast_armor_bluegrey", "Blast Armor", [("blast_armour_bluegrey",0)], itp_merchandise| itp_type_body_armor |itp_covers_legs |itp_civilian  ,0, 
 430 , weight(5)|abundance(60)|head_armor(0)|body_armor(35)|leg_armor(14)|difficulty(0) ,imodbits_cloth ],  

#other
["ubese_armor", "Ubese Armor", [("ubese_armour",0)], itp_merchandise| itp_type_body_armor |itp_covers_legs |itp_civilian  ,0, 
 430 , weight(5)|abundance(80)|head_armor(0)|body_armor(35)|leg_armor(14)|difficulty(0) ,imodbits_cloth ],   
["ubese_armor_alt", "Ubese Armor", [("ubese_armour_alt",0)], itp_merchandise| itp_type_body_armor |itp_covers_legs |itp_civilian  ,0, 
 430 , weight(5)|abundance(80)|head_armor(0)|body_armor(35)|leg_armor(14)|difficulty(0) ,imodbits_cloth ],   

# mercenary equipment
# wookiee
#["wookiee_head1", "Wookiee Head", [("wookiee_head1",0)], itp_unique|itp_type_head_armor|itp_covers_head |itp_civilian ,0, 
# 75 , weight(1)|abundance(80)|head_armor(10)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth ],
#["wookiee_head2", "Wookiee Head", [("wookiee_head2",0)], itp_unique|itp_type_head_armor|itp_covers_head |itp_civilian ,0, 
# 75 , weight(1)|abundance(80)|head_armor(10)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth ],
#["wookiee_hands","Wookiee Hands", [("wookiee_hand_L",0)], itp_unique|itp_type_hand_armor|itp_civilian,0, 
# 50, weight(0.2)|abundance(80)|body_armor(3)|difficulty(0),imodbits_cloth],

#added unique flag so it is not left in the loot after battles, but the player can buy it from the shops if they want (nevermind, this didn't work, need to have separate items for unique vs shop)

["wookiee_fullbody", "Wookiee Skin", [("Wookie",0)], itp_type_body_armor|itp_covers_head|itp_replaces_helm|itp_covers_legs|itp_civilian, 0, 
 530 , weight(3)|abundance(50)|head_armor(5)|body_armor(35)|leg_armor(14)|difficulty(0) ,imodbits_armor ],

["wookiee_armor1", "Wookiee Chestarmor", [("wookie_armor",0)], itp_type_foot_armor|itp_replaces_helm|itp_covers_legs|itp_civilian, 0, 
 530 , weight(3)|abundance(50)|head_armor(0)|body_armor(20)|leg_armor(0)|difficulty(0) ,imodbits_armor ],

["wookiee_armor2", "Wookiee Chestarmor", [("wookie_armor",0)], itp_type_foot_armor|itp_replaces_helm|itp_covers_legs|itp_civilian, 0, 
 530 , weight(3)|abundance(50)|head_armor(0)|body_armor(20)|leg_armor(0)|difficulty(0) ,imodbits_armor ],

["wookiee_hunter_armor", "Wookiee Hunter Armor", [("wookiee_hunter_armor",0)], itp_merchandise|itp_type_body_armor |itp_covers_legs |itp_civilian  ,0, 
 700 , weight(5)|abundance(40)|head_armor(0)|body_armor(42)|leg_armor(16)|difficulty(0) ,imodbits_cloth ],  

["wookiee_hunter_helmet", "Wookiee Hunter Helmet", [("wookiee_hunter_helmet",0)], itp_merchandise|itp_type_head_armor|itp_covers_head |itp_civilian ,0, 
 150 , weight(2.5)|abundance(40)|head_armor(12)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth ], 
 
#["wookiee_feet", "Wookiee Feet", [("wookiee_feet",0)], itp_unique| itp_type_foot_armor  |itp_civilian,0, 
# 75 , weight(0.4)|abundance(80)|head_armor(0)|body_armor(0)|leg_armor(16)|difficulty(0) ,imodbits_cloth ],

["wookiee_female_head", "Wookiee Female Head", [("wookiee_female_head",0)], itp_unique|itp_type_head_armor|itp_covers_head |itp_civilian ,0, 75 , weight(1)|abundance(0)|head_armor(10)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth ],
["wookiee_female_body", "Wookiee Female Body", [("wookiee_female_body",0)], itp_unique|itp_type_body_armor|itp_covers_legs |itp_civilian ,0, 530, weight(3)|abundance(0)|head_armor(0)|body_armor(32)|leg_armor(12)|difficulty(0) ,imodbits_cloth ],
["wookiee_female_hands","Wookiee Female Hands", [("wookiee_female_mittenL",0)], itp_unique|itp_type_hand_armor|itp_civilian,0, 50, weight(0.2)|abundance(0)|body_armor(3)|difficulty(0),imodbits_cloth],
["wookiee_female_feet", "Wookiee Female Feet", [("wookiee_female_feet",0)], itp_unique |itp_type_foot_armor | itp_attach_armature|itp_civilian,0, 150 , weight(2)|abundance(80)|head_armor(0)|body_armor(0)|leg_armor(10)|difficulty(0) ,imodbits_cloth ],


["kaminoan_female_head", "Kaminoan Female Head", [("kaminoan_head",0)], itp_unique|itp_type_head_armor|itp_covers_head|itp_attach_armature|itp_civilian,0 ,75 , weight(1)|abundance(0)|head_armor(10)|body_armor(0)|leg_armor(0)|difficulty(0), imodbits_cloth ],
["kaminoan_female_body", "Kaminoan Female Body", [("kaminoan_body",0)], itp_unique|itp_type_body_armor|itp_covers_legs|itp_civilian, 0,530 , weight(3)|abundance(0)|head_armor(0)|body_armor(32)|leg_armor(12)|difficulty(0), imodbits_cloth ],


#bothan
# 75 , weight(1)|abundance(80)|head_armor(10)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth ],
#["bothan_head", "Bothan Head", [("bothan_head",0)], itp_unique|itp_type_head_armor|itp_covers_head |itp_civilian ,0, 

#no attack ability since the droid armor moves and the animation looks bad when they attack
["droid_weapon_no_attack","Droid Melee Weapon (No Attack)", [("_",0),("force_block_inv",ixmesh_inventory)], itp_unique|itp_primary, 0, 
 1 , weight(1)|abundance(0)|difficulty(0)|spd_rtng(40) | weapon_length(25)|swing_damage(0, blunt) | thrust_damage(0, blunt),imodbits_none ],

#r2series
# ["r2series_blue", "R2-Series Blue", [("r2series_blue",0)], itp_unique|itp_type_body_armor|itp_covers_legs|itp_civilian,0, 
 # 500 , weight(50)|abundance(0)|head_armor(15)|body_armor(30)|leg_armor(15)|difficulty(0) ,imodbits_none ], 
# ["r2series_green", "R2-Series Green", [("r2series_green",0)], itp_unique|itp_type_body_armor|itp_covers_legs|itp_civilian,0, 
 # 500 , weight(50)|abundance(0)|head_armor(15)|body_armor(30)|leg_armor(15)|difficulty(0) ,imodbits_none ], 
# ["r2series_orange", "R2-Series Orange", [("r2series_orange",0)], itp_unique|itp_type_body_armor|itp_covers_legs|itp_civilian,0, 
 # 500 , weight(50)|abundance(0)|head_armor(15)|body_armor(30)|leg_armor(15)|difficulty(0) ,imodbits_none ], 
# ["r2series_purple", "R2-Series Purple", [("r2series_purple",0)], itp_unique|itp_type_body_armor|itp_covers_legs|itp_civilian,0, 
 # 500 , weight(50)|abundance(0)|head_armor(15)|body_armor(30)|leg_armor(15)|difficulty(0) ,imodbits_none ],  
 ["r2series_blue", "R2-Series Blue", [("swy_R2D2",0)], itp_unique|itp_type_body_armor|itp_covers_legs|itp_civilian,0, 
 500 , weight(50)|abundance(0)|head_armor(15)|body_armor(30)|leg_armor(15)|difficulty(0) ,imodbits_none ], 
["r2series_green", "R2-Series Green", [("swy_R2D2_alt_green",0)], itp_unique|itp_type_body_armor|itp_covers_legs|itp_civilian,0, 
 500 , weight(50)|abundance(0)|head_armor(15)|body_armor(30)|leg_armor(15)|difficulty(0) ,imodbits_none ], 
["r2series_orange", "R2-Series Orange", [("swy_R2D2_alt_orange",0)], itp_unique|itp_type_body_armor|itp_covers_legs|itp_civilian,0, 
 500 , weight(50)|abundance(0)|head_armor(15)|body_armor(30)|leg_armor(15)|difficulty(0) ,imodbits_none ], 
["r2series_purple", "R2-Series Purple", [("swy_R2D2_alt_purple",0)], itp_unique|itp_type_body_armor|itp_covers_legs|itp_civilian,0, 
 500 , weight(50)|abundance(0)|head_armor(15)|body_armor(30)|leg_armor(15)|difficulty(0) ,imodbits_none ],  

#mse6 droid
["mse6_armor", "MSE-Series Droid Body", [("MSE-6",0)], itp_unique|itp_type_body_armor|itp_covers_legs|itp_civilian,0, 
 250 , weight(35)|abundance(0)|head_armor(10)|body_armor(20)|leg_armor(10)|difficulty(0) ,imodbits_none ], 
#no attack ability since the armor moves and the animation looks bad when they attack

#lin droid
["lin_droid_armor", "LIN Droid Body", [("lin_droid_2",0)], itp_unique|itp_type_body_armor|itp_covers_legs|itp_civilian,0, 
 200 , weight(45)|abundance(0)|head_armor(10)|body_armor(20)|leg_armor(10)|difficulty(0) ,imodbits_none ], 
["lin_droid_armor_w_arm", "LIN Droid Body", [("lin_droid",0)], itp_unique|itp_type_body_armor|itp_covers_legs|itp_civilian,0, 
 200 , weight(45)|abundance(0)|head_armor(10)|body_armor(20)|leg_armor(10)|difficulty(0) ,imodbits_none ],  
#no attack ability since the armor moves and the animation looks bad when they attack

#power_droid_armor
#["power_droid_tan", "Power Droid", [("swy_power_droid_body",0)], itp_unique|itp_type_body_armor|itp_covers_legs|itp_civilian,0, 
# 500 , weight(50)|abundance(0)|head_armor(15)|body_armor(30)|leg_armor(15)|difficulty(0) ,imodbits_none ],  
["power_droid_grey", "Power Droid", [("powerdroid_grey_resized",0)], itp_unique|itp_type_body_armor|itp_covers_legs|itp_civilian,0, 
 500 , weight(50)|abundance(0)|head_armor(15)|body_armor(30)|leg_armor(15)|difficulty(0) ,imodbits_none ],   
["power_droid_snow", "Power Droid", [("powerdroid_snow_resized",0)], itp_unique|itp_type_body_armor|itp_covers_legs|itp_civilian,0, 
 500 , weight(50)|abundance(0)|head_armor(15)|body_armor(30)|leg_armor(15)|difficulty(0) ,imodbits_none ],    
["power_droid_tan", "Power Droid", [("powerdroid_tan_resized",0)], itp_unique|itp_type_body_armor|itp_covers_legs|itp_civilian,0, 
 500 , weight(50)|abundance(0)|head_armor(15)|body_armor(30)|leg_armor(15)|difficulty(0) ,imodbits_none ],   
#["power_droid_legs", "Power Droid legs", [("swy_power_droid_leg_L",0)], itp_unique| itp_type_foot_armor  |itp_civilian,0, 
# 150 , weight(15)|abundance(0)|head_armor(0)|body_armor(0)|leg_armor(10)|difficulty(0) ,imodbits_none ], 
 
["fxseries_droid_armor", "FX-Series Medical Droid Body", [("med_droid_resized",0)], itp_unique|itp_type_body_armor|itp_covers_legs|itp_civilian,0, 
 500 , weight(50)|abundance(0)|head_armor(15)|body_armor(30)|leg_armor(15)|difficulty(0) ,imodbits_none ], 
 
#c3po droid parts (removed merch flag)
["c3po_blue_head", "3PO-Series Head", [("C3PO_blue_head",0)], itp_type_head_armor|itp_covers_head|itp_civilian,0, 
 500 , weight(5)|abundance(0)|head_armor(10)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_droid ],  
["c3po_blue_hands", "3PO-Series Hands", [("C3PO_blue_hand_L",0)], itp_type_hand_armor|itp_civilian,0, 
 250 , weight(5)|abundance(0)|head_armor(0)|body_armor(5)|leg_armor(0)|difficulty(0) ,imodbits_droid ],   
["c3po_blue_body", "3PO-Series Body", [("C3PO_blue_body",0)], itp_type_body_armor|itp_covers_legs|itp_civilian,0, 
 1000 , weight(30)|abundance(0)|head_armor(0)|body_armor(40)|leg_armor(10)|difficulty(0) ,imodbits_droid ],
["c3po_blue_feet", "3PO-Series Feet", [("C3PO_blue_feet",0)], itp_type_foot_armor | itp_attach_armature|itp_civilian,0, 
 500 , weight(5)|abundance(0)|head_armor(0)|body_armor(0)|leg_armor(10)|difficulty(0) ,imodbits_droid ],
["c3po_gold_head", "3PO-Series Head", [("C3PO_gold_head",0)], itp_type_head_armor|itp_covers_head|itp_civilian,0, 
 500 , weight(5)|abundance(0)|head_armor(10)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_droid ],  
["c3po_gold_hands", "3PO-Series Hands", [("C3PO_gold_hand_L",0)], itp_type_hand_armor|itp_civilian,0, 
 250 , weight(5)|abundance(0)|head_armor(0)|body_armor(5)|leg_armor(0)|difficulty(0) ,imodbits_droid ],   
["c3po_gold_body", "3PO-Series Body", [("C3PO_gold_body",0)], itp_type_body_armor|itp_covers_legs|itp_civilian,0, 
 1000 , weight(30)|abundance(0)|head_armor(0)|body_armor(40)|leg_armor(10)|difficulty(0) ,imodbits_droid ],
["c3po_gold_feet", "3PO-Series Feet", [("C3PO_gold_feet",0)], itp_type_foot_armor | itp_attach_armature|itp_civilian,0, 
 500 , weight(5)|abundance(0)|head_armor(0)|body_armor(0)|leg_armor(10)|difficulty(0) ,imodbits_droid ], 
["c3po_grey_head", "3PO-Series Head", [("C3PO_grey_head",0)], itp_type_head_armor|itp_covers_head|itp_civilian,0, 
 500 , weight(5)|abundance(0)|head_armor(10)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_droid ],  
["c3po_grey_hands", "3PO-Series Hands", [("C3PO_grey_hand_L",0)], itp_type_hand_armor|itp_civilian,0, 
 250 , weight(5)|abundance(0)|head_armor(0)|body_armor(5)|leg_armor(0)|difficulty(0) ,imodbits_droid ],   
["c3po_grey_body", "3PO-Series Body", [("C3PO_grey_body",0)], itp_type_body_armor|itp_covers_legs|itp_civilian,0, 
 1000 , weight(30)|abundance(0)|head_armor(0)|body_armor(40)|leg_armor(10)|difficulty(0) ,imodbits_droid ],
["c3po_grey_feet", "3PO-Series Feet", [("C3PO_grey_feet",0)], itp_type_foot_armor | itp_attach_armature|itp_civilian,0, 
 500 , weight(5)|abundance(0)|head_armor(0)|body_armor(0)|leg_armor(10)|difficulty(0) ,imodbits_droid ],  
["c3po_red_head", "3PO-Series Head", [("C3PO_red_head",0)], itp_type_head_armor|itp_covers_head|itp_civilian,0, 
 500 , weight(5)|abundance(0)|head_armor(10)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_droid ],  
["c3po_red_hands", "3PO-Series Hands", [("C3PO_red_hand_L",0)], itp_type_hand_armor|itp_civilian,0, 
 250 , weight(5)|abundance(0)|head_armor(0)|body_armor(5)|leg_armor(0)|difficulty(0) ,imodbits_droid ],   
["c3po_red_body", "3PO-Series Body", [("C3PO_red_body",0)], itp_type_body_armor|itp_covers_legs|itp_civilian,0, 
 1000 , weight(30)|abundance(0)|head_armor(0)|body_armor(40)|leg_armor(10)|difficulty(0) ,imodbits_droid ],
["c3po_red_feet", "3PO-Series Feet", [("C3PO_red_feet",0)], itp_type_foot_armor | itp_attach_armature|itp_civilian,0, 
 500 , weight(5)|abundance(0)|head_armor(0)|body_armor(0)|leg_armor(10)|difficulty(0) ,imodbits_droid ],

#full-body equipment for town walkers (itp_unique)
["3poseries_gold", "3PO-Series Gold", [("C3PO_fullbody",0)], itp_unique|itp_type_body_armor|itp_covers_legs|itp_civilian,0, 
 1000 , weight(60)|abundance(0)|head_armor(15)|body_armor(45)|leg_armor(15)|difficulty(0) ,imodbits_none ], 
["3poseries_blue", "3PO-Series Blue", [("C3PO_fullbody_blue",0)], itp_unique|itp_type_body_armor|itp_covers_legs|itp_civilian,0, 
 1000 , weight(60)|abundance(0)|head_armor(15)|body_armor(45)|leg_armor(15)|difficulty(0) ,imodbits_none ], 
["3poseries_red", "3PO-Series Red", [("C3PO_fullbody_red",0)], itp_unique|itp_type_body_armor|itp_covers_legs|itp_civilian,0, 
 1000 , weight(60)|abundance(0)|head_armor(15)|body_armor(45)|leg_armor(15)|difficulty(0) ,imodbits_none ], 
["3poseries_grey", "3PO-Series Grey", [("C3PO_fullbody_grey",0)], itp_unique|itp_type_body_armor|itp_covers_legs|itp_civilian,0, 
 1000 , weight(60)|abundance(0)|head_armor(15)|body_armor(45)|leg_armor(15)|difficulty(0) ,imodbits_none ],  
["3poseries_attack","3PO-Series Melee Attack", [("_",0),("C3PO_gold_hand_L",ixmesh_inventory)], itp_unique|itp_type_one_handed_wpn|itp_primary|itp_secondary, itc_dagger, 
250 , weight(1)|abundance(0)|difficulty(0)|spd_rtng(50) | weapon_length(15)|swing_damage(5, blunt) | thrust_damage(4, blunt),imodbits_none ], 

#b1 battledroid & others
["b1series_body", "B1-Series Battle Droid Body", [("battledroid",0)], itp_unique|itp_type_body_armor|itp_covers_legs|itp_civilian,0, 
 2000 , weight(45)|abundance(0)|head_armor(15)|body_armor(45)|leg_armor(15)|difficulty(0) ,imodbits_none ],
#bxseries
["bxseries_body", "BX-Series Commando Droid Body", [("battledroid_bx",0)], itp_unique|itp_type_body_armor|itp_covers_legs|itp_civilian,0, 
 3000 , weight(25)|abundance(0)|head_armor(25)|body_armor(60)|leg_armor(25)|difficulty(0) ,imodbits_none ],
#oom
["oomseries_body", "OOM Security Droid Body", [("battledroid_security",0)], itp_unique|itp_type_body_armor|itp_covers_legs|itp_civilian,0, 
 2000 , weight(45)|abundance(0)|head_armor(15)|body_armor(45)|leg_armor(15)|difficulty(0) ,imodbits_none ],
["oomseries_pilot_body", "OOM Pilot Droid Body", [("battledroid_pilot",0)], itp_unique|itp_type_body_armor|itp_covers_legs|itp_civilian,0, 
 2500 , weight(40)|abundance(0)|head_armor(20)|body_armor(50)|leg_armor(20)|difficulty(0) ,imodbits_none ],
["oomseries_marine_body", "OOM Marine Droid Body", [("battledroid_marine",0)], itp_unique|itp_type_body_armor|itp_covers_legs|itp_civilian,0, 
 2500 , weight(40)|abundance(0)|head_armor(20)|body_armor(50)|leg_armor(20)|difficulty(0) ,imodbits_none ],
["oomseries_command_body", "OOM Command Droid Body", [("battledroid_commander",0)], itp_unique|itp_type_body_armor|itp_covers_legs|itp_civilian,0, 
 2750 , weight(35)|abundance(0)|head_armor(25)|body_armor(55)|leg_armor(25)|difficulty(0) ,imodbits_none ],
 #melee attack
 ["battle_droid_attack","Battle Droid Melee Attack", [("_",0),("ArcTrooperGloves_L",ixmesh_inventory)], itp_unique|itp_type_one_handed_wpn|itp_primary|itp_secondary, itc_dagger, 
250 , weight(1)|abundance(0)|difficulty(0)|spd_rtng(65) | weapon_length(15)|swing_damage(7, blunt) | thrust_damage(6, blunt),imodbits_none ], 

#b2series
 ["b2series_body", "B2-Series Battle Droid Body", [("B2-Battledroid",0)], itp_unique|itp_type_body_armor|itp_covers_legs|itp_civilian,0, 
  4160, weight(50)|abundance(0)|head_armor(20)|body_armor(60)|leg_armor(20)|difficulty(0) ,imodbits_none ],
#b2 series reskin
 ["b2series_body_enhanced", "C-B3 Battle Droid Body", [("B2-Battledroid_enhanced",0)], itp_unique|itp_type_body_armor|itp_covers_legs|itp_civilian,0, 
 7420, weight(55)|abundance(0)|head_armor(30)|body_armor(70)|leg_armor(30)|difficulty(0) ,imodbits_none ],
  
 ["b2series_attack","B2-Series Battle Droid Attack", [("_",0),("ArcTrooperGloves_L",ixmesh_inventory)], itp_unique|itp_type_one_handed_wpn|itp_primary|itp_secondary, itc_dagger, 
  500, weight(1)|abundance(0)|difficulty(0)|spd_rtng(75) | weapon_length(20)|swing_damage(10, blunt) | thrust_damage(8, blunt),imodbits_none ], 
 ["b2series_blaster", "B2-Series Battle Droid Blaster", [("_",0),("ArcTrooperGloves_L",ixmesh_inventory)], itp_unique|itp_type_pistol|itp_primary|itp_bonus_against_shield,itcf_shoot_pistol|itcf_reload_pistol, 
	 500 , weight(2)|abundance(0)|difficulty(0)|spd_rtng(90) | shoot_speed(145) | thrust_damage(35,pierce)|max_ammo(24)|accuracy(88),imodbits_none,
	 [(ti_on_weapon_attack, [(play_sound,"snd_bigblaster19"),(position_move_x, pos1,12),(position_move_y, pos1,15)])]],	

["transparent_droid_head", "Transparent Head (for Droids)", [("_",0),("transparent_helmet_inv",ixmesh_inventory)], itp_unique|itp_type_head_armor|itp_covers_head|itp_civilian,0, 1, weight(0.25)|abundance(0)|head_armor(1)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_none ], 
["transparent_droid_hands", "Transparent Hands (for Droids)", [("_",0),("transparent_helmet_inv",ixmesh_inventory)], itp_unique|itp_type_hand_armor|itp_civilian,0, 1 , weight(0.25)|abundance(0)|head_armor(0)|body_armor(1)|leg_armor(0)|difficulty(0) ,imodbits_none ], 
["transparent_droid_feet", "Transparent Feet (for Droids)", [("_",0),("transparent_helmet_inv",ixmesh_inventory)], itp_unique|itp_type_foot_armor|itp_civilian,0, 1 , weight(0.25)|abundance(0)|head_armor(0)|body_armor(0)|leg_armor(1)|difficulty(0) ,imodbits_none ], 
 
#IG88 parts (removed merch flag)
["ig88_head", "IG-Series Head", [("IG88_head",0)], itp_type_head_armor|itp_covers_head|itp_civilian,0, 
 500 , weight(5)|abundance(0)|head_armor(20)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_none ],  
["ig88_hands", "IG-Series Hands", [("IG88_hand_L",0)], itp_type_hand_armor|itp_civilian,0, 
 500 , weight(5)|abundance(0)|head_armor(0)|body_armor(5)|leg_armor(0)|difficulty(0) ,imodbits_none ],   
["ig88_body", "IG-Series Body", [("IG88_body",0)], itp_type_body_armor|itp_covers_legs|itp_civilian,0, 
 1000 , weight(35)|abundance(0)|head_armor(0)|body_armor(65)|leg_armor(0)|difficulty(0) ,imodbits_none ],
["ig88_feet", "IG-Series Feet", [("IG88_feet",0)], itp_type_foot_armor | itp_attach_armature|itp_civilian,0, 
 500 , weight(5)|abundance(0)|head_armor(0)|body_armor(0)|leg_armor(20)|difficulty(0) ,imodbits_none ],
["ig88_attack","_", [("_",0),("ArcTrooperGloves_L",ixmesh_inventory)], itp_unique|itp_type_one_handed_wpn|itp_primary|itp_secondary|itp_bonus_against_shield, itc_dagger, 
250 , weight(1)|abundance(0)|difficulty(0)|spd_rtng(80) | weapon_length(25)|swing_damage(30, cut) | thrust_damage(25, pierce),imodbits_none ], 
["ig88_e11_shield", "IG-88's E-11 Shield", [("E11_IG88",0)], itp_unique|itp_type_shield, 0,  500 , weight(3.0)|abundance(0)|hit_points(200)|body_armor(10)|spd_rtng(70)|weapon_length(45),imodbits_none ], 
# no merchandise and no unique flag so there is a chance they will be in the loot after battle (must give 2x to the troops for this to happen)
["ig88_dlt20a", "IG-88's DLT-20A", [("DLT20A_IG88",0)], itp_type_pistol|itp_primary|itp_bonus_against_shield,itcf_shoot_pistol|itcf_carry_sword_back|itcf_reload_pistol, 1300 , weight(6.7)|abundance(0)|difficulty(0)|spd_rtng(100) | shoot_speed(190) | thrust_damage(55, pierce)|max_ammo(30)|accuracy(97),imodbits_none,
 [(ti_on_weapon_attack, [(play_sound,"snd_bigblaster01"),(position_move_x, pos1,4),(position_move_y, pos1,5)])]],

#lomseries
["4lom_head", "LOM-Series Head", [("4lom_head",0)], itp_type_head_armor|itp_covers_head|itp_civilian,0, 
 400 , weight(5)|abundance(0)|head_armor(15)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_none ],   
 
#hkseries
["hk_head", "HK-Series Head", [("HK_series_head",0)], itp_type_head_armor|itp_covers_head|itp_civilian,0, 
 300 , weight(5)|abundance(0)|head_armor(14)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_none ],  
["hk_hands","HK-Series Hands",[("HK_series_hands_L",0),("HK_series_hands_inv",ixmesh_inventory)], itp_type_hand_armor|itp_civilian,0, 
 300 , weight(3)|abundance(0)|head_armor(0)|body_armor(3)|leg_armor(0)|difficulty(0) ,imodbits_none ],   
["hk_body", "HK-Series Body", [("HK_series_body",0)], itp_type_body_armor|itp_covers_legs|itp_civilian,0, 
 7000 , weight(30)|abundance(0)|head_armor(0)|body_armor(45)|leg_armor(0)|difficulty(0) ,imodbits_none ],
["hk_feet", "HK-Series Feet", [("HK_series_feet",0)], itp_type_foot_armor | itp_attach_armature|itp_civilian,0, 
 300 , weight(5)|abundance(0)|head_armor(0)|body_armor(0)|leg_armor(14)|difficulty(0) ,imodbits_none ], 
["hk_attack","_", [("_",0),("HK_series_hands_inv",ixmesh_inventory)], itp_unique|itp_type_one_handed_wpn|itp_primary|itp_secondary|itp_bonus_against_shield, itc_dagger, 
250 , weight(1)|abundance(0)|difficulty(0)|spd_rtng(70) | weapon_length(25)|swing_damage(24, cut) | thrust_damage(18, pierce),imodbits_none ],  
 
# mandalorians
["mandalorian_tunic", "Mandalorian Tunic", [("mandalorian_tunic",0)], itp_merchandise|itp_type_body_armor|itp_civilian |itp_covers_legs ,0, 
 270 , weight(2)|abundance(80)|head_armor(0)|body_armor(25)|leg_armor(4)|difficulty(0) ,imodbits_cloth ],
["mandalorian_soldier_helmet", "Mandalorian Soldier Helmet", [("mandalorian_soldier_helmet",0)], itp_merchandise| itp_type_head_armor|itp_covers_head|itp_civilian,0, 
 195 , weight(2)|abundance(80)|head_armor(15)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_armor ],
 ["mandalorian_soldier_helmet2", "Mandalorian Soldier Helmet", [("mandalorian_soldier_helmet2",0)], itp_merchandise| itp_type_head_armor|itp_covers_head|itp_civilian,0,
 195 , weight(2)|abundance(80)|head_armor(15)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_armor ],
 ["mandalorian_soldier_helmet3", "Mandalorian Soldier Helmet", [("mandalorian_soldier_helmet3",0)], itp_merchandise| itp_type_head_armor|itp_covers_head|itp_civilian,0,
 195 , weight(2)|abundance(80)|head_armor(15)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_armor ],
["mandalorian_soldier_armor", "Mandalorian Soldier Armor", [("mandalorian_soldier_armor",0)], itp_merchandise| itp_type_body_armor |itp_civilian |itp_covers_legs,0,
 540 , weight(8)|abundance(80)|head_armor(0)|body_armor(34)|leg_armor(10)|difficulty(0) ,imodbits_armor ],
 ["mandalorian_soldier_armor2", "Mandalorian Soldier Armor", [("mandalorian_soldier_armor2",0)], itp_merchandise| itp_type_body_armor |itp_civilian |itp_covers_legs,0,
 540 , weight(8)|abundance(80)|head_armor(0)|body_armor(34)|leg_armor(10)|difficulty(0) ,imodbits_armor ],
["mandalorian_soldier_boots", "Mandalorian Soldier Boots", [("mandalorian_soldier_boots",0)], itp_merchandise |itp_type_foot_armor | itp_attach_armature|itp_civilian,0,
 150 , weight(2)|abundance(80)|head_armor(0)|body_armor(0)|leg_armor(12)|difficulty(0) ,imodbits_armor ],
["mandalorian_commando_helmet", "Mandalorian Commando Helmet", [("mandalorian_commando_helmet",0)], itp_merchandise| itp_type_head_armor|itp_covers_head|itp_civilian,0,
 270 , weight(2)|abundance(80)|head_armor(20)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_armor ],
["mandalorian_commando_armor", "Mandalorian Commando Armor", [("mandalorian_commando_armor",0)], itp_merchandise| itp_type_body_armor |itp_civilian |itp_covers_legs,0,
 780 , weight(8)|abundance(80)|head_armor(0)|body_armor(46)|leg_armor(14)|difficulty(0) ,imodbits_armor ],
["mandalorian_commando_armor2", "Mandalorian Commando Armor", [("mandalorian_commando_armor2",0)], itp_merchandise| itp_type_body_armor |itp_civilian |itp_covers_legs,0,
 780 , weight(8)|abundance(80)|head_armor(0)|body_armor(46)|leg_armor(14)|difficulty(0) ,imodbits_armor ],
["mandalorian_commando_boots", "Mandalorian Commando Boots", [("mandalorian_commando_boots",0)], itp_merchandise |itp_type_foot_armor | itp_attach_armature|itp_civilian,0,
 180 , weight(2)|abundance(80)|head_armor(0)|body_armor(0)|leg_armor(14)|difficulty(0) ,imodbits_armor ],
["mandalorian_sniper_helmet", "Mandalorian Sniper Helmet", [("mandalorian_sniper_helmet",0)], itp_merchandise| itp_type_head_armor|itp_covers_head|itp_civilian,0,
 270 , weight(2)|abundance(80)|head_armor(20)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_armor ],
["mandalorian_sniper_armor", "Mandalorian Sniper Armor", [("mandalorian_sniper_armor",0)], itp_merchandise| itp_type_body_armor |itp_civilian |itp_covers_legs,0,
 780 , weight(8)|abundance(80)|head_armor(0)|body_armor(46)|leg_armor(14)|difficulty(0) ,imodbits_armor ],
["mandalorian_sniper_armor2", "Mandalorian Sniper Armor", [("mandalorian_sniper_armor2",0)], itp_merchandise| itp_type_body_armor |itp_civilian |itp_covers_legs,0,
 780 , weight(8)|abundance(80)|head_armor(0)|body_armor(46)|leg_armor(14)|difficulty(0) ,imodbits_armor ],
["mandalorian_sniper_armor3", "Mandalorian Sniper Armor", [("mandalorian_sniper_armor3",0)], itp_merchandise| itp_type_body_armor |itp_civilian |itp_covers_legs,0,
 780 , weight(8)|abundance(80)|head_armor(0)|body_armor(46)|leg_armor(14)|difficulty(0) ,imodbits_armor ],
["mandalorian_sniper_boots", "Mandalorian Sniper Boots", [("mandalorian_sniper_boots",0)], itp_merchandise |itp_type_foot_armor | itp_attach_armature|itp_civilian,0,
 180 , weight(2)|abundance(80)|head_armor(0)|body_armor(0)|leg_armor(14)|difficulty(0) ,imodbits_armor ],

# crusader_helmet is start of set 1
["mandalorian_crusader_helmet", "Mandalorian Crusader Helmet", [("mandalorian_crusader_helmet_b",0)], itp_merchandise| itp_type_head_armor|itp_covers_head|itp_civilian,0,
 345 , weight(2)|abundance(80)|head_armor(25)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_armor ],
["mandalorian_neocrusader_helmet", "Mandalorian Neo-Crusader Helmet", [("mandalorian_neocrusader_helmet",0)], itp_merchandise| itp_type_head_armor|itp_covers_head|itp_civilian,0,
 428 , weight(1.5)|abundance(40)|head_armor(30)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_armor ],
["mandalorian_crusader_armor", "Mandalorian Crusader Armor", [("mandalorian_crusader_armor",0)], itp_merchandise| itp_type_body_armor |itp_civilian |itp_covers_legs,0,
 930 , weight(8)|abundance(80)|head_armor(0)|body_armor(52)|leg_armor(18)|difficulty(0) ,imodbits_armor ],
 # ["mandalorian_crusader_armor2", "Mandalorian Crusader Armor", [("mandalorian_crusader_armor2",0)], itp_merchandise| itp_type_body_armor |itp_civilian |itp_covers_legs,0,
 # 930 , weight(8)|abundance(80)|head_armor(0)|body_armor(52)|leg_armor(18)|difficulty(0) ,imodbits_armor ],
 # ["mandalorian_crusader_armor3", "Mandalorian Crusader Armor", [("mandalorian_crusader_armor3",0)], itp_merchandise| itp_type_body_armor |itp_civilian |itp_covers_legs,0,
 # 930 , weight(8)|abundance(80)|head_armor(0)|body_armor(52)|leg_armor(18)|difficulty(0) ,imodbits_armor ],
["mandalorian_crusader_boots", "Mandalorian Crusader Boots", [("mandalorian_crusader_boots",0)], itp_merchandise |itp_type_foot_armor | itp_attach_armature|itp_civilian,0,
 210 , weight(2)|abundance(80)|head_armor(0)|body_armor(0)|leg_armor(16)|difficulty(0) ,imodbits_armor ],
#["mandalorian_crusader_set_end", "Mandalorian Crusader Boots", [("mandalorian_crusader_boots",0)],                itp_type_foot_armor | itp_attach_armature|itp_civilian,0,
# 210 , weight(2)|abundance(80)|head_armor(0)|body_armor(0)|leg_armor(16)|difficulty(0) ,imodbits_armor ],

# deadeye_helmet is start of set 2
["mandalorian_deadeye_helmet", "Mandalorian Deadeye Helmet", [("mandalorian_deadeye_helmet",0)], itp_merchandise| itp_type_head_armor|itp_covers_head|itp_civilian,0,
 345 , weight(2)|abundance(80)|head_armor(25)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_armor ],
["mandalorian_deadeye_armor", "Mandalorian Deadeye Armor", [("mandalorian_deadeye_armor",0)], itp_merchandise| itp_type_body_armor |itp_civilian |itp_covers_legs,0,
 930 , weight(8)|abundance(80)|head_armor(0)|body_armor(52)|leg_armor(18)|difficulty(0) ,imodbits_armor ],
 ["mandalorian_deadeye_armor2", "Mandalorian Deadeye Armor", [("mandalorian_deadeye_armor2",0)], itp_merchandise| itp_type_body_armor |itp_civilian |itp_covers_legs,0,
 930 , weight(8)|abundance(80)|head_armor(0)|body_armor(52)|leg_armor(18)|difficulty(0) ,imodbits_armor ],
 ["mandalorian_deadeye_armor3", "Mandalorian Deadeye Armor", [("mandalorian_deadeye_armor3",0)], itp_merchandise| itp_type_body_armor |itp_civilian |itp_covers_legs,0,
 930 , weight(8)|abundance(80)|head_armor(0)|body_armor(52)|leg_armor(18)|difficulty(0) ,imodbits_armor ],
["mandalorian_deadeye_boots", "Mandalorian Deadeye Boots", [("mandalorian_deadeye_boots",0)], itp_merchandise |itp_type_foot_armor | itp_attach_armature|itp_civilian,0, 
 240 , weight(2)|abundance(80)|head_armor(0)|body_armor(0)|leg_armor(18)|difficulty(0) ,imodbits_armor ],
#["mandalorian_deadeye_set_end", "Mandalorian Deadeye Boots", [("mandalorian_deadeye_boots",0)],                itp_type_foot_armor | itp_attach_armature|itp_civilian,0, 
# 210 , weight(2)|abundance(80)|head_armor(0)|body_armor(0)|leg_armor(16)|difficulty(0) ,imodbits_armor ],

#rare beskar armor
["mandalorian_beskar_helmet", "Mandalorian Beskar Helmet", [("mandalorian_beskar_helmet",0)], itp_merchandise| itp_type_head_armor|itp_covers_head|itp_civilian,0, 
 800 , weight(1.5)|abundance(40)|head_armor(30)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_armor ],
["mandalorian_beskar_armor", "Mandalorian Beskar Armor", [("mandalorian_beskar_armor",0)], itp_merchandise| itp_type_body_armor |itp_civilian |itp_covers_legs,0, 
 1500 , weight(7)|abundance(40)|head_armor(0)|body_armor(60)|leg_armor(22)|difficulty(0) ,imodbits_armor ],
["mandalorian_beskar_boots", "Mandalorian Beskar Boots", [("mandalorian_beskar_boots",0)], itp_merchandise |itp_type_foot_armor | itp_attach_armature|itp_civilian,0, 
 600 , weight(1.5)|abundance(40)|head_armor(0)|body_armor(0)|leg_armor(22)|difficulty(0) ,imodbits_armor ],

#defiler
["defiler_helmet", "Defiler Helmet", [("defiler_helmet",0)], itp_merchandise| itp_type_head_armor|itp_covers_head|itp_civilian,0, 
 325 , weight(2)|abundance(50)|head_armor(22)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_armor ],
["defiler_armor", "Defiler Armor", [("defiler_armor",0)], itp_merchandise| itp_type_body_armor |itp_civilian |itp_covers_legs,0, 
 875 , weight(7)|abundance(50)|head_armor(0)|body_armor(48)|leg_armor(16)|difficulty(0) ,imodbits_armor ],
["defiler_boots", "Defiler Boots", [("defiler_boots",0)], itp_merchandise |itp_type_foot_armor | itp_attach_armature|itp_civilian,0, 
 200 , weight(2)|abundance(50)|head_armor(0)|body_armor(0)|leg_armor(16)|difficulty(0) ,imodbits_armor ], 

#black sun 
["black_sun_helmet", "Black Sun Helmet", [("black_sun_helmet",0)], itp_merchandise| itp_type_head_armor|itp_covers_head|itp_civilian,0, 
 270 , weight(2)|abundance(60)|head_armor(20)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_armor ],
["black_sun_helmet_tan", "Black Sun Helmet", [("black_sun_helmet_tan",0)], itp_merchandise| itp_type_head_armor|itp_covers_head|itp_civilian,0, 
 270 , weight(2)|abundance(60)|head_armor(20)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_armor ],
["black_sun_helmet_teal", "Black Sun Helmet", [("black_sun_helmet_teal",0)], itp_merchandise| itp_type_head_armor|itp_covers_head|itp_civilian,0, 
 270 , weight(2)|abundance(60)|head_armor(20)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_armor ],
["black_sun_helmet_red", "Black Sun Helmet", [("black_sun_helmet_red",0)], itp_merchandise| itp_type_head_armor|itp_covers_head|itp_civilian,0, 
 270 , weight(2)|abundance(60)|head_armor(20)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_armor ],
 
["black_sun_armor", "Black Sun Armor", [("black_sun_armor",0)], itp_merchandise| itp_type_body_armor |itp_civilian |itp_covers_legs,0, 
 780 , weight(6)|abundance(60)|head_armor(0)|body_armor(46)|leg_armor(14)|difficulty(0) ,imodbits_armor ],
["black_sun_armor_tan", "Black Sun Armor", [("black_sun_armor_tan",0)], itp_merchandise| itp_type_body_armor |itp_civilian |itp_covers_legs,0, 
 780 , weight(6)|abundance(60)|head_armor(0)|body_armor(46)|leg_armor(14)|difficulty(0) ,imodbits_armor ],
["black_sun_armor_teal", "Black Sun Armor", [("black_sun_armor_teal",0)], itp_merchandise| itp_type_body_armor |itp_civilian |itp_covers_legs,0, 
 780 , weight(6)|abundance(60)|head_armor(0)|body_armor(46)|leg_armor(14)|difficulty(0) ,imodbits_armor ],
["black_sun_armor_red", "Black Sun Armor", [("black_sun_armor_red",0)], itp_merchandise| itp_type_body_armor |itp_civilian |itp_covers_legs,0, 
 780 , weight(6)|abundance(60)|head_armor(0)|body_armor(46)|leg_armor(14)|difficulty(0) ,imodbits_armor ],

# gamorrean
# ["gamorrean_head", "Gamorrean Head", [("gamorrean_head",0)], itp_unique|itp_type_head_armor|itp_covers_head |itp_civilian ,0, 
 # 75 , weight(4)|abundance(80)|head_armor(10)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth ],
# ["gamorrean_hands","Gamorrean Hands", [("gamorrean_hand_L",0)], itp_unique|itp_type_hand_armor|itp_civilian,0, 
 # 100, weight(2.25)|abundance(80)|body_armor(5)|difficulty(0),imodbits_armor],
# ["gamorrean_body", "Gamorrean Body", [("gamorrean_body",0)], itp_unique| itp_type_body_armor |itp_covers_legs |itp_civilian  ,0, 
 # 200 , weight(7)|abundance(80)|head_armor(0)|body_armor(42)|leg_armor(14)|difficulty(0) ,imodbits_cloth ],
 
#added unique flag so it is not left in the loot after battles, but the player can buy it from the shops if they want (nevermind, this didn't work, need to have separate items for unique vs shop)
["gamorrean_armor", "Gamorrean Armor", [("gamorrean_armor",0)], itp_unique|itp_type_body_armor |itp_covers_legs |itp_civilian  ,0, 
 530 , weight(3)|abundance(40)|head_armor(0)|body_armor(40)|leg_armor(16)|difficulty(0) ,imodbits_cloth ],
#["gamorrean_armor_merch", "Gamorrean Armor", [("gamorrean_armor",0)], itp_merchandise|itp_type_body_armor |itp_covers_legs |itp_civilian  ,0, 
# 530 , weight(3)|abundance(40)|head_armor(0)|body_armor(40)|leg_armor(16)|difficulty(0) ,imodbits_cloth ], 
# ["gamorrean_feet", "Gamorrean Feet", [("gamorrean_feet",0),("gamorrean_feet_inv",ixmesh_inventory)], itp_unique| itp_type_foot_armor  |itp_civilian,0, 
 # 75 , weight(2.25)|abundance(80)|head_armor(0)|body_armor(0)|leg_armor(16)|difficulty(0) ,imodbits_cloth ],

# mon cal
# ["mon_cal_head", "Mon Calamari Head", [("mon_calamari_head",0)], itp_unique|itp_type_head_armor|itp_covers_head |itp_civilian ,0, 
 # 100 , weight(4)|abundance(100)|head_armor(10)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth ],
["moncal_armor", "Mon Calamari Armor", [("moncal_armor",0)], itp_merchandise|itp_type_body_armor |itp_covers_legs |itp_civilian  ,0, 
 410 , weight(6)|abundance(60)|head_armor(0)|body_armor(35)|leg_armor(12)|difficulty(0) ,imodbits_cloth ],
["moncal_armor_2", "Mon Calamari Armor", [("moncal_armor_knight",0)], itp_merchandise|itp_type_body_armor |itp_covers_legs |itp_civilian  ,0, 
 520 , weight(6)|abundance(60)|head_armor(0)|body_armor(42)|leg_armor(16)|difficulty(0) ,imodbits_cloth ], 
["moncal_boots", "Mon Calamari Boots", [("moncal_armor_boots",0)], itp_merchandise |itp_type_foot_armor | itp_attach_armature|itp_civilian,0, 
 145 , weight(1.5)|abundance(60)|head_armor(0)|body_armor(0)|leg_armor(16)|difficulty(0) ,imodbits_cloth ],
["moncal_helmet", "Mon Calamri Helmet", [("moncal_helmet",0)], itp_merchandise| itp_type_head_armor|itp_civilian,0, 
 185 , weight(1.5)|abundance(60)|head_armor(20)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth ], 
 
 
# rodian
#["rodian_head", "Rodian Head", [("rodian_male",0)], itp_unique|itp_type_head_armor|itp_covers_head |itp_civilian ,0, 
# 60 , weight(4)|abundance(100)|head_armor(10)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth ],
 
# twilek
["twilek_armor", "Twi'lek Armor", [("padded_leather",0)], itp_unique| itp_type_body_armor |itp_civilian |itp_covers_legs ,0, 
 480 , weight(6)|abundance(70)|head_armor(0)|body_armor(42)|leg_armor(12)|difficulty(0) ,imodbits_cloth ],

# jawas
["jawa_hood", "Jawa Head", [("jawa_helmet",0)], itp_unique|itp_type_head_armor|itp_covers_head|itp_civilian ,0, 
  40 , weight(2)|abundance(80)|head_armor(6)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth ],
["jawa_robe", "Jawa Robe", [("jawa_robe",0)], itp_unique| itp_type_body_armor |itp_covers_legs |itp_civilian  ,0, 
  370 , weight(2.5)|abundance(80)|head_armor(0)|body_armor(20)|leg_armor(10)|difficulty(0) ,imodbits_cloth ],
#["jawa_robe", "Jawa Robe", [("jawa_robe_skel",0)], itp_unique| itp_type_body_armor |itp_covers_legs |itp_civilian  ,0, 
#  370 , weight(2.5)|abundance(80)|head_armor(0)|body_armor(20)|leg_armor(10)|difficulty(0) ,imodbits_cloth ],  
[ "jawa_boots", "Jawa Boots", [("jawa_boots",0)], itp_unique |itp_type_foot_armor | itp_attach_armature|itp_civilian,0, 
  60 , weight(2)|abundance(80)|head_armor(0)|body_armor(0)|leg_armor(8)|difficulty(0) ,imodbits_cloth ], 
# ["jawa_robe2", "Jawa Robe", [("jawa_robe2",0)], itp_unique| itp_type_body_armor |itp_covers_legs |itp_civilian  ,0, 
 # 150 , weight(3)|abundance(80)|head_armor(0)|body_armor(28)|leg_armor(10)|difficulty(0) ,imodbits_cloth ],
#["jawa_hood", "Jawa Hood", [("jawa_hood_a",0)],itp_type_head_armor|itp_merchandise ,0, 15 , weight(0.1)|abundance(80)|head_armor(5)|body_armor(0)|leg_armor(0) ,imodbits_cloth ],
#["jawa_hood_b", "Jawa Hood B", [("jawa_hood_b",0)],itp_type_head_armor|itp_merchandise ,0, 15 , weight(0.1)|abundance(80)|head_armor(5)|body_armor(0)|leg_armor(0) ,imodbits_cloth ],
 
# tusken raiders
["tusken_helmet", "Tusken Helmet", [("tusken_helmet",0)], itp_merchandise|itp_type_head_armor|itp_covers_head|itp_civilian ,0, 
 60 , weight(2)|abundance(70)|head_armor(8)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_cloth ],
["tusken_armor", "Tusken Armor", [("tusken_armor",0)], itp_merchandise|itp_type_body_armor |itp_covers_legs |itp_civilian  ,0, 
 310 , weight(3)|abundance(70)|head_armor(0)|body_armor(24)|leg_armor(10)|difficulty(0) ,imodbits_cloth ],
#["tusken_body2", "Tusken Armor", [("tusken_body2",0)], itp_unique| itp_type_body_armor |itp_covers_legs |itp_civilian  ,0, 
# 100 , weight(3)|abundance(80)|head_armor(0)|body_armor(24)|leg_armor(10)|difficulty(0) ,imodbits_cloth ],
# ["tusken_boots", "Tusken Boots", [("tusken_boots",0)], itp_unique| itp_type_foot_armor  |itp_civilian,0, 
 # 50 , weight(1.0)|abundance(80)|head_armor(0)|body_armor(0)|leg_armor(10)|difficulty(0) ,imodbits_cloth ],
# ["tusken_gloves","Tusken Gloves", [("tusken_glove_L",0)], itp_unique|itp_type_hand_armor|itp_civilian,0, 
 # 25, weight(0.25)|abundance(80)|body_armor(1)|difficulty(0),imodbits_cloth],

#trandoshan 
["trandoshan_armor", "Trandoshan Armor", [("new_trandoshan_body",0)], itp_merchandise|itp_type_body_armor |itp_covers_legs |itp_civilian  ,0, 
 765 , weight(5)|abundance(70)|head_armor(5)|body_armor(42)|leg_armor(14)|difficulty(0) ,imodbits_armor ], 
 
#added unique flag so it is not left in the loot after battles, but the player can buy it from the shops if they want (nevermind, this didn't work, need to have separate items for unique vs shop)
["geonosian_armor", "Geonosian Armor", [("new_geonosian_body",0)], itp_type_body_armor|itp_attach_armature|itp_covers_head|itp_covers_legs|itp_replaces_helm|itp_civilian, 0, 
 400, weight(10)|abundance(100)|head_armor(5)|body_armor(44)|leg_armor(30)|difficulty(0), imodbits_armor ], 

#["geonosian_armor_merch", "Geonosian Armor", [("geonosian_armor",0)], itp_merchandise| itp_type_body_armor |itp_covers_legs |itp_civilian  ,0, 
# 510 , weight(5)|abundance(50)|head_armor(0)|body_armor(40)|leg_armor(16)|difficulty(0) ,imodbits_cloth ], 
 
["armors_end", "<dummy>", [("_",0)], 0,0,0,0,imodbits_none],

# special arena lightsabers with no strength requirements (this is lightsaber_noise_begin)
["lightsaber_green_arena", "Lightsaber", [("lightsaber_green",0),("lightsaber_greenoff",ixmesh_carry)], itp_type_two_handed_wpn|itp_unique| itp_primary|itp_bonus_against_shield|itp_wooden_parry|itp_wooden_attack, itc_lightsaber|itcf_carry_dagger_front_left,
 1500*lsbr_vluemul , weight(0.5)|abundance(0)|difficulty(0)|spd_rtng(120) | weapon_length(115)|swing_damage(50, blunt) | thrust_damage(35, blunt),imodbits_none ],
["lightsaber_blue_arena", "Lightsaber", [("lightsaber_blue",0),("lightsaber_blueoff",ixmesh_carry)], itp_type_two_handed_wpn|itp_unique| itp_primary|itp_bonus_against_shield|itp_wooden_parry|itp_wooden_attack, itc_lightsaber|itcf_carry_dagger_front_left,
 1500*lsbr_vluemul , weight(0.5)|abundance(0)|difficulty(0)|spd_rtng(120) | weapon_length(115)|swing_damage(50, blunt) | thrust_damage(35, blunt),imodbits_none ],
["lightsaber_yellow_arena", "Lightsaber", [("lightsaber_yellow",0),("lightsaber_yellowoff",ixmesh_carry)], itp_type_two_handed_wpn|itp_unique| itp_primary|itp_bonus_against_shield|itp_wooden_parry|itp_wooden_attack, itc_lightsaber|itcf_carry_dagger_front_left,
 1500*lsbr_vluemul , weight(0.5)|abundance(0)|difficulty(0)|spd_rtng(120) | weapon_length(115)|swing_damage(50, blunt) | thrust_damage(35, blunt),imodbits_none ],
["lightsaber_red_arena", "Lightsaber", [("lightsaber_red",0),("lightsaber_redoff",ixmesh_carry)], itp_type_two_handed_wpn|itp_unique| itp_primary|itp_bonus_against_shield|itp_wooden_parry|itp_wooden_attack, itc_lightsaber|itcf_carry_dagger_front_left,
 1500*lsbr_vluemul , weight(0.5)|abundance(0)|difficulty(0)|spd_rtng(120) | weapon_length(115)|swing_damage(50, blunt) | thrust_damage(35, blunt),imodbits_none ],

# weapons - lightsabers  (abundance is reduced since you can buy them all from the force-sensitive merchant at the trade federation base)
["weapons_begin", "<dummy>", [("_",0)], 0,0,0,0,imodbits_none],
["lightsaber_green", "Lightsaber", [("lightsaber_green",0),("lightsaber_greenoff",ixmesh_carry)], itp_type_two_handed_wpn|itp_merchandise| itp_primary|itp_bonus_against_shield|itp_wooden_parry|itp_wooden_attack, itc_lightsaber|itcf_carry_dagger_front_left,
 900*lsbr_vluemul , weight(0.5)|abundance(30)|difficulty(12)|spd_rtng(120) | weapon_length(115)|swing_damage(75 , pierce) | thrust_damage(75 ,  pierce),imodbits_lightsaber,[],force_fac ],
 #@> SWY - Tried to add a real lightpoint, the game crashes when used: [(ti_on_init_item), [(assign,":scale",2),(store_mul, ":red", 2 * 157, ":scale"),(store_mul, ":green", 2 * 250, ":scale"),(store_mul, ":blue", 2 * 157, ":scale"),(val_div, ":red", 100),(val_div, ":green", 100),(val_div, ":blue", 100),(set_current_color,":red", ":green", ":blue"),(set_position_delta,0,0,0),(add_point_light, 10, 30)])]],
#[(ti_on_init_item), [(position_move_y,pos1,10),(particle_system_add_new,"psys_planet_icon_atmospheric_effect_polution",pos1)])]],

["lightsaber_blue", "Lightsaber", [("lightsaber_blue",0),("lightsaber_blueoff",ixmesh_carry)], itp_type_two_handed_wpn|itp_merchandise| itp_primary|itp_bonus_against_shield|itp_wooden_parry|itp_wooden_attack, itc_lightsaber|itcf_carry_dagger_front_left,
 900*lsbr_vluemul , weight(0.5)|abundance(30)|difficulty(12)|spd_rtng(120) | weapon_length(115)|swing_damage(75 , pierce) | thrust_damage(75 ,  pierce),imodbits_lightsaber,[],force_fac ],
["lightsaber_orange", "Lightsaber", [("lightsaber_orange",0),("lightsaber_orangeoff",ixmesh_carry)], itp_type_two_handed_wpn|itp_merchandise| itp_primary|itp_bonus_against_shield|itp_wooden_parry|itp_wooden_attack, itc_lightsaber|itcf_carry_dagger_front_left,
 900*lsbr_vluemul , weight(0.5)|abundance(10)|difficulty(12)|spd_rtng(120) | weapon_length(115)|swing_damage(75 , pierce) | thrust_damage(75 ,  pierce),imodbits_lightsaber,[],force_fac ],
["lightsaber_purple", "Lightsaber", [("lightsaber_purple",0),("lightsaber_purpleoff",ixmesh_carry)], itp_type_two_handed_wpn|itp_merchandise| itp_primary|itp_bonus_against_shield|itp_wooden_parry|itp_wooden_attack, itc_lightsaber|itcf_carry_dagger_front_left,
 900*lsbr_vluemul , weight(0.5)|abundance(20)|difficulty(12)|spd_rtng(120) | weapon_length(115)|swing_damage(75 , pierce) | thrust_damage(75 ,  pierce),imodbits_lightsaber,[],force_fac ],
["lightsaber_yellow", "Lightsaber", [("lightsaber_yellow",0),("lightsaber_yellowoff",ixmesh_carry)], itp_type_two_handed_wpn|itp_merchandise| itp_primary|itp_bonus_against_shield|itp_wooden_parry|itp_wooden_attack, itc_lightsaber|itcf_carry_dagger_front_left,
 900*lsbr_vluemul , weight(0.5)|abundance(10)|difficulty(12)|spd_rtng(120) | weapon_length(115)|swing_damage(75 , pierce) | thrust_damage(75 ,  pierce),imodbits_lightsaber,[],force_fac ],
["lightsaber_red", "Lightsaber", [("lightsaber_red",0),("lightsaber_redoff",ixmesh_carry)], itp_type_two_handed_wpn|itp_merchandise| itp_primary|itp_bonus_against_shield|itp_wooden_parry|itp_wooden_attack, itc_lightsaber|itcf_carry_dagger_front_left,
 900*lsbr_vluemul , weight(0.5)|abundance(30)|difficulty(12)|spd_rtng(120) | weapon_length(115)|swing_damage(75 , pierce) | thrust_damage(75 ,  pierce),imodbits_lightsaber,[],force_fac ],
# reverse-grip lightsabers  (abundance is reduced since you can buy them all from the force-sensitive merchant at the trade federation base)
["lightsaber_green_reverse", "Reverse Grip Lightsaber", [("lightsaber_green_reverse",0),("lightsaber_greenoff",ixmesh_carry)], itp_type_polearm|itp_merchandise| itp_primary|itp_bonus_against_shield|itp_wooden_parry|itp_wooden_attack, itc_lightsaber_1h|itcf_carry_dagger_front_left,
 1050*lsbr_vluemul , weight(0.5)|abundance(15)|difficulty(14)|spd_rtng(135) | weapon_length(130)|swing_damage(75 , pierce) | thrust_damage(75 ,  pierce),imodbits_lightsaber,[],force_fac ],
["lightsaber_blue_reverse", "Reverse Grip Lightsaber", [("lightsaber_blue_reverse",0),("lightsaber_blueoff",ixmesh_carry)], itp_type_polearm|itp_merchandise| itp_primary|itp_bonus_against_shield|itp_wooden_parry|itp_wooden_attack, itc_lightsaber_1h|itcf_carry_dagger_front_left,
 1050*lsbr_vluemul , weight(0.5)|abundance(15)|difficulty(14)|spd_rtng(135) | weapon_length(130)|swing_damage(75 , pierce) | thrust_damage(75 ,  pierce),imodbits_lightsaber,[],force_fac ],
["lightsaber_orange_reverse", "Reverse Grip Lightsaber", [("lightsaber_orange_reverse",0),("lightsaber_orangeoff",ixmesh_carry)], itp_type_polearm|itp_merchandise| itp_primary|itp_bonus_against_shield|itp_wooden_parry|itp_wooden_attack, itc_lightsaber_1h|itcf_carry_dagger_front_left,
 1050*lsbr_vluemul , weight(0.5)|abundance(5)|difficulty(14)|spd_rtng(135) | weapon_length(130)|swing_damage(75 , pierce) | thrust_damage(75 ,  pierce),imodbits_lightsaber,[],force_fac ],
["lightsaber_purple_reverse", "Reverse Grip Lightsaber", [("lightsaber_purple_reverse",0),("lightsaber_purpleoff",ixmesh_carry)], itp_type_polearm|itp_merchandise| itp_primary|itp_bonus_against_shield|itp_wooden_parry|itp_wooden_attack, itc_lightsaber_1h|itcf_carry_dagger_front_left,
 1050*lsbr_vluemul , weight(0.5)|abundance(5)|difficulty(14)|spd_rtng(135) | weapon_length(130)|swing_damage(75 , pierce) | thrust_damage(75 ,  pierce),imodbits_lightsaber,[],force_fac ],
["lightsaber_yellow_reverse", "Reverse Grip Lightsaber", [("lightsaber_yellow_reverse",0),("lightsaber_yellowoff",ixmesh_carry)], itp_type_polearm|itp_merchandise| itp_primary|itp_bonus_against_shield|itp_wooden_parry|itp_wooden_attack, itc_lightsaber_1h|itcf_carry_dagger_front_left,
 1050*lsbr_vluemul , weight(0.5)|abundance(5)|difficulty(14)|spd_rtng(135) | weapon_length(130)|swing_damage(75 , pierce) | thrust_damage(75 ,  pierce),imodbits_lightsaber,[],force_fac ],
["lightsaber_red_reverse", "Reverse Grip Lightsaber", [("lightsaber_red_reverse",0),("lightsaber_redoff",ixmesh_carry)], itp_type_polearm|itp_merchandise| itp_primary|itp_bonus_against_shield|itp_wooden_parry|itp_wooden_attack, itc_lightsaber_1h|itcf_carry_dagger_front_left,
 1050*lsbr_vluemul , weight(0.5)|abundance(15)|difficulty(14)|spd_rtng(135) | weapon_length(130)|swing_damage(75 , pierce) | thrust_damage(75 ,  pierce),imodbits_lightsaber,[],force_fac ],
# double-bladed lightsaber added itp_two_handed so you cannot use a shield at the same time  (abundance is reduced since you can buy them all from the force-sensitive merchant at the trade federation base)
["lightsaber_blue_double", "Double-Bladed Lightsaber", [("lightsaber_blue_double",0),("lightsaber_blue_doubleoff",ixmesh_carry)], itp_type_polearm|itp_merchandise|itp_two_handed| itp_spear|itp_primary|itp_bonus_against_shield|itp_wooden_parry|itp_wooden_attack, itc_lightsaber_double|itcf_carry_sword_back, 
 1310*lsbr_vluemul , weight(0.8)|abundance(15)|difficulty(14)|spd_rtng(150) | weapon_length(170)|swing_damage(75 , pierce) | thrust_damage(75 ,  pierce),imodbits_lightsaber,[],force_fac ],
["lightsaber_green_double", "Double-Bladed Lightsaber", [("lightsaber_green_double",0),("lightsaber_green_doubleoff",ixmesh_carry)], itp_type_polearm|itp_merchandise|itp_two_handed| itp_spear|itp_primary|itp_bonus_against_shield|itp_wooden_parry|itp_wooden_attack, itc_lightsaber_double|itcf_carry_dagger_front_left, 
 1310*lsbr_vluemul , weight(0.8)|abundance(15)|difficulty(14)|spd_rtng(150) | weapon_length(170)|swing_damage(75 , pierce) | thrust_damage(75 ,  pierce),imodbits_lightsaber,[],force_fac ],
#["lightsaber_greenblue_double", "Double-Bladed Lightsaber", [("lightsaber_greenblue_double",0),("lightsaber_off",ixmesh_carry)], itp_type_polearm|itp_merchandise|itp_two_handed| itp_spear|itp_primary|itp_bonus_against_shield|itp_wooden_parry|itp_wooden_attack, itc_lightsaber_double|itcf_carry_dagger_front_left, 
#1700 , weight(0.8)|abundance(70)|difficulty(16)|spd_rtng(150) | weapon_length(170)|swing_damage(100 , cut) | thrust_damage(75 ,  pierce),imodbits_lightsaber ],
["lightsaber_orange_double", "Double-Bladed Lightsaber", [("lightsaber_orange_double",0),("lightsaber_orange_doubleoff_separate",ixmesh_carry)], itp_type_polearm|itp_merchandise|itp_two_handed| itp_spear|itp_primary|itp_bonus_against_shield|itp_wooden_parry|itp_wooden_attack, itc_lightsaber_double|itcf_carry_dagger_front_left, 
 1310*lsbr_vluemul , weight(0.8)|abundance(5)|difficulty(14)|spd_rtng(150) | weapon_length(170)|swing_damage(75 , pierce) | thrust_damage(75 ,  pierce),imodbits_lightsaber,[],force_fac ],
["lightsaber_purple_double", "Double-Bladed Lightsaber", [("lightsaber_purple_double",0),("lightsaber_purple_doubleoff",ixmesh_carry)], itp_type_polearm|itp_merchandise|itp_two_handed| itp_spear|itp_primary|itp_bonus_against_shield|itp_wooden_parry|itp_wooden_attack, itc_lightsaber_double|itcf_carry_dagger_front_left, 
 1310*lsbr_vluemul , weight(0.8)|abundance(10)|difficulty(14)|spd_rtng(150) | weapon_length(170)|swing_damage(75 , pierce) | thrust_damage(75 ,  pierce),imodbits_lightsaber,[],force_fac ],
["lightsaber_red_double", "Double-Bladed Lightsaber", [("lightsaber_red_double",0),("lightsaber_red_doubleoff",ixmesh_carry)], itp_type_polearm|itp_merchandise|itp_two_handed| itp_spear|itp_primary|itp_bonus_against_shield|itp_wooden_parry|itp_wooden_attack, itc_lightsaber_double|itcf_carry_dagger_front_left, 
 1310*lsbr_vluemul , weight(0.8)|abundance(20)|difficulty(14)|spd_rtng(150) | weapon_length(170)|swing_damage(75 , pierce) | thrust_damage(75 ,  pierce),imodbits_lightsaber,[],force_fac ],
["lightsaber_yellow_double", "Double-Bladed Lightsaber", [("lightsaber_yellow_double",0),("lightsaber_yellow_doubleoff_separate",ixmesh_carry)], itp_type_polearm|itp_merchandise|itp_two_handed| itp_spear|itp_primary|itp_bonus_against_shield|itp_wooden_parry|itp_wooden_attack, itc_lightsaber_double|itcf_carry_dagger_front_left, 
 1310*lsbr_vluemul , weight(0.8)|abundance(5)|difficulty(14)|spd_rtng(150) | weapon_length(170)|swing_damage(75 , pierce) | thrust_damage(75 ,  pierce),imodbits_lightsaber,[],force_fac ],
# two handed lightsabers - added itp_two_handed so you cannot use a shield at the same time (higher speed as a bonus since the blade isn't 'heavy')
["lightsaber_green_2h", "Two Handed Lightsaber", [("lightsaber_green_2h",0),("lightsaber_green_2hoff",ixmesh_carry)], itp_type_two_handed_wpn|itp_merchandise|itp_two_handed| itp_primary|itp_bonus_against_shield|itp_wooden_parry|itp_wooden_attack, itc_lightsaber_2h|itcf_carry_dagger_front_left,
 1195*lsbr_vluemul , weight(0.6)|abundance(15)|difficulty(12)|spd_rtng(135) | weapon_length(130)|swing_damage(90 , pierce) | thrust_damage(90 ,  pierce),imodbits_lightsaber,[],force_fac ],
["lightsaber_blue_2h", "Two Handed Lightsaber", [("lightsaber_blue_2h",0),("lightsaber_blue_2hoff",ixmesh_carry)], itp_type_two_handed_wpn|itp_merchandise|itp_two_handed| itp_primary|itp_bonus_against_shield|itp_wooden_parry|itp_wooden_attack, itc_lightsaber_2h|itcf_carry_dagger_front_left,
 1195*lsbr_vluemul , weight(0.6)|abundance(15)|difficulty(12)|spd_rtng(135) | weapon_length(130)|swing_damage(90 , pierce) | thrust_damage(90 ,  pierce),imodbits_lightsaber,[],force_fac ],
["lightsaber_orange_2h", "Two Handed Lightsaber", [("lightsaber_orange_2h",0),("lightsaber_orange_2hoff",ixmesh_carry)], itp_type_two_handed_wpn|itp_merchandise|itp_two_handed| itp_primary|itp_bonus_against_shield|itp_wooden_parry|itp_wooden_attack, itc_lightsaber_2h|itcf_carry_dagger_front_left,
 1195*lsbr_vluemul , weight(0.6)|abundance(5)|difficulty(12)|spd_rtng(135) | weapon_length(130)|swing_damage(90 , pierce) | thrust_damage(90 ,  pierce),imodbits_lightsaber,[],force_fac ],
["lightsaber_purple_2h", "Two Handed Lightsaber", [("lightsaber_purple_2h",0),("lightsaber_purple_2hoff",ixmesh_carry)], itp_type_two_handed_wpn|itp_merchandise|itp_two_handed| itp_primary|itp_bonus_against_shield|itp_wooden_parry|itp_wooden_attack, itc_lightsaber_2h|itcf_carry_dagger_front_left,
 1195*lsbr_vluemul , weight(0.6)|abundance(10)|difficulty(12)|spd_rtng(135) | weapon_length(130)|swing_damage(90 , pierce) | thrust_damage(90 ,  pierce),imodbits_lightsaber,[],force_fac ],
["lightsaber_yellow_2h", "Two Handed Lightsaber", [("lightsaber_yellow_2h",0),("lightsaber_yellow_2hoff",ixmesh_carry)], itp_type_two_handed_wpn|itp_merchandise|itp_two_handed| itp_primary|itp_bonus_against_shield|itp_wooden_parry|itp_wooden_attack, itc_lightsaber_2h|itcf_carry_dagger_front_left,
 1195*lsbr_vluemul , weight(0.6)|abundance(5)|difficulty(12)|spd_rtng(135) | weapon_length(130)|swing_damage(90 , pierce) | thrust_damage(90 ,  pierce),imodbits_lightsaber,[],force_fac ],
["lightsaber_red_2h", "Two Handed Lightsaber", [("lightsaber_red_2h",0),("lightsaber_red_2hoff",ixmesh_carry)], itp_type_two_handed_wpn|itp_merchandise|itp_two_handed| itp_primary|itp_bonus_against_shield|itp_wooden_parry|itp_wooden_attack, itc_lightsaber_2h|itcf_carry_dagger_front_left,
 1195*lsbr_vluemul , weight(0.6)|abundance(20)|difficulty(12)|spd_rtng(135) | weapon_length(130)|swing_damage(90 , pierce) | thrust_damage(90 ,  pierce),imodbits_lightsaber,[],force_fac ],
# one handed lightsabers (lower speed)
["lightsaber_green_1h", "One Handed Lightsaber", [("lightsaber_green_1h",0),("lightsaber_green_1hoff",ixmesh_carry)], itp_type_one_handed_wpn|itp_merchandise| itp_primary|itp_bonus_against_shield|itp_wooden_parry|itp_wooden_attack, itc_lightsaber_1h|itcf_carry_dagger_front_left,
 605*lsbr_vluemul , weight(0.4)|abundance(15)|difficulty(10)|spd_rtng(105) | weapon_length(100)|swing_damage(60 , pierce) | thrust_damage(60 ,  pierce),imodbits_lightsaber,[],force_fac ],
["lightsaber_blue_1h", "One Handed Lightsaber", [("lightsaber_blue_1h",0),("lightsaber_blue_1hoff",ixmesh_carry)], itp_type_one_handed_wpn|itp_merchandise| itp_primary|itp_bonus_against_shield|itp_wooden_parry|itp_wooden_attack, itc_lightsaber_1h|itcf_carry_dagger_front_left,
 605*lsbr_vluemul , weight(0.4)|abundance(15)|difficulty(10)|spd_rtng(105) | weapon_length(100)|swing_damage(60 , pierce) | thrust_damage(60 ,  pierce),imodbits_lightsaber,[],force_fac ],
["lightsaber_orange_1h", "One Handed Lightsaber", [("lightsaber_orange_1h",0),("lightsaber_orange_1hoff",ixmesh_carry)], itp_type_one_handed_wpn|itp_merchandise| itp_primary|itp_bonus_against_shield|itp_wooden_parry|itp_wooden_attack, itc_lightsaber_1h|itcf_carry_dagger_front_left,
 605*lsbr_vluemul , weight(0.4)|abundance(5)|difficulty(10)|spd_rtng(105) | weapon_length(100)|swing_damage(60 , pierce) | thrust_damage(60 ,  pierce),imodbits_lightsaber,[],force_fac ],
["lightsaber_purple_1h", "One Handed Lightsaber", [("lightsaber_purple_1h",0),("lightsaber_purple_1hoff",ixmesh_carry)], itp_type_one_handed_wpn|itp_merchandise| itp_primary|itp_bonus_against_shield|itp_wooden_parry|itp_wooden_attack, itc_lightsaber_1h|itcf_carry_dagger_front_left,
 605*lsbr_vluemul , weight(0.4)|abundance(10)|difficulty(10)|spd_rtng(105) | weapon_length(100)|swing_damage(60 , pierce) | thrust_damage(60 ,  pierce),imodbits_lightsaber,[],force_fac ],
["lightsaber_yellow_1h", "One Handed Lightsaber", [("lightsaber_yellow_1h",0),("lightsaber_yellow_1hoff",ixmesh_carry)], itp_type_one_handed_wpn|itp_merchandise| itp_primary|itp_bonus_against_shield|itp_wooden_parry|itp_wooden_attack, itc_lightsaber_1h|itcf_carry_dagger_front_left,
 605*lsbr_vluemul , weight(0.4)|abundance(5)|difficulty(10)|spd_rtng(105) | weapon_length(100)|swing_damage(60 , pierce) | thrust_damage(60 ,  pierce),imodbits_lightsaber,[],force_fac ],
["lightsaber_red_1h", "One Handed Lightsaber", [("lightsaber_red_1h",0),("lightsaber_red_1hoff",ixmesh_carry)], itp_type_one_handed_wpn|itp_merchandise| itp_primary|itp_bonus_against_shield|itp_wooden_parry|itp_wooden_attack, itc_lightsaber_1h|itcf_carry_dagger_front_left,
 605*lsbr_vluemul , weight(0.4)|abundance(20)|difficulty(10)|spd_rtng(105) | weapon_length(100)|swing_damage(60 , pierce) | thrust_damage(60 ,  pierce),imodbits_lightsaber,[],force_fac ], 
# lightsaber_pike  (abundance is reduced since you can buy them all from the force-sensitive merchant at the trade federation base)
["lightsaber_green_pike","Lightsaber Pike", [("lightsaber_green_pike",0),("lightsaber_pike_off",ixmesh_carry)], itp_type_polearm|itp_merchandise| itp_spear|itp_primary|itp_penalty_with_shield|itp_wooden_parry|itp_wooden_attack, itc_lightsaber_pike|itcf_carry_spear,
 1040*lsbr_vluemul , weight(1.2)|abundance(10)|difficulty(10)|spd_rtng(120) | weapon_length(150)|swing_damage(75, pierce) | thrust_damage(75,  pierce),imodbits_lightsaber,[],force_fac ],
["lightsaber_blue_pike","Lightsaber Pike", [("lightsaber_blue_pike",0),("lightsaber_pike_off",ixmesh_carry)], itp_type_polearm|itp_merchandise| itp_spear|itp_primary|itp_penalty_with_shield|itp_wooden_parry|itp_wooden_attack, itc_lightsaber_pike|itcf_carry_spear,
 1040*lsbr_vluemul , weight(1.2)|abundance(10)|difficulty(10)|spd_rtng(120) | weapon_length(150)|swing_damage(75, pierce) | thrust_damage(75,  pierce),imodbits_lightsaber,[],force_fac ],
["lightsaber_orange_pike","Lightsaber Pike", [("lightsaber_orange_pike",0),("lightsaber_pike_off",ixmesh_carry)], itp_type_polearm|itp_merchandise| itp_spear|itp_primary|itp_penalty_with_shield|itp_wooden_parry|itp_wooden_attack, itc_lightsaber_pike|itcf_carry_spear,
 1040*lsbr_vluemul , weight(1.2)|abundance(5)|difficulty(10)|spd_rtng(120) | weapon_length(150)|swing_damage(75, pierce) | thrust_damage(75,  pierce),imodbits_lightsaber,[],force_fac ],
["lightsaber_purple_pike","Lightsaber Pike", [("lightsaber_purple_pike",0),("lightsaber_pike_off",ixmesh_carry)], itp_type_polearm|itp_merchandise| itp_spear|itp_primary|itp_penalty_with_shield|itp_wooden_parry|itp_wooden_attack, itc_lightsaber_pike|itcf_carry_spear,
 1040*lsbr_vluemul , weight(1.2)|abundance(5)|difficulty(10)|spd_rtng(120) | weapon_length(150)|swing_damage(75, pierce) | thrust_damage(75,  pierce),imodbits_lightsaber,[],force_fac ],
["lightsaber_yellow_pike","Lightsaber Pike", [("lightsaber_yellow_pike",0),("lightsaber_pike_off",ixmesh_carry)], itp_type_polearm|itp_merchandise| itp_spear|itp_primary|itp_penalty_with_shield|itp_wooden_parry|itp_wooden_attack, itc_lightsaber_pike|itcf_carry_spear,
 1040*lsbr_vluemul , weight(1.2)|abundance(5)|difficulty(10)|spd_rtng(120) | weapon_length(150)|swing_damage(75, pierce) | thrust_damage(75,  pierce),imodbits_lightsaber,[],force_fac ],
["lightsaber_red_pike","Lightsaber Pike", [("lightsaber_red_pike",0),("lightsaber_pike_off",ixmesh_carry)], itp_type_polearm|itp_merchandise| itp_spear|itp_primary|itp_penalty_with_shield|itp_wooden_parry|itp_wooden_attack, itc_lightsaber_pike|itcf_carry_spear,
 1040*lsbr_vluemul , weight(1.2)|abundance(20)|difficulty(10)|spd_rtng(120) | weapon_length(150)|swing_damage(75, pierce) | thrust_damage(75,  pierce),imodbits_lightsaber,[],force_fac ], 
#unique lightsabers
["darth_vader_lightsaber", "Darth Vader's Lightsaber", [("lightsaber_red",0),("lightsaber_redoff",ixmesh_carry)], itp_type_two_handed_wpn|itp_primary|itp_bonus_against_shield|itp_wooden_parry|itp_wooden_attack, itc_lightsaber|itcf_carry_dagger_front_left, 4000 , weight(2.1)|difficulty(14)|spd_rtng(140) | weapon_length(120)|swing_damage(100 , pierce) | thrust_damage(100 ,  pierce),imodbits_none ],
["obi_wan_lightsaber", "Obi-Wan Kenobi's Lightsaber", [("lightsaber_blue",0),("lightsaber_blueoff",ixmesh_carry)], itp_type_two_handed_wpn|itp_primary|itp_bonus_against_shield|itp_wooden_parry|itp_wooden_attack, itc_lightsaber|itcf_carry_dagger_front_left, 4000 , weight(2.1)|difficulty(14)|spd_rtng(140) | weapon_length(120)|swing_damage(125 , pierce) | thrust_damage(100 ,  pierce),imodbits_none ],
["luke_skywalker_lightsaber", "Luke Skywalker's Lightsaber", [("lightsaber_blue",0),("lightsaber_blueoff",ixmesh_carry)], itp_type_two_handed_wpn|itp_primary|itp_bonus_against_shield|itp_wooden_parry|itp_wooden_attack, itc_lightsaber|itcf_carry_dagger_front_left, 4000 , weight(2.1)|difficulty(14)|spd_rtng(140) | weapon_length(120)|swing_damage(125 , pierce) | thrust_damage(100 ,  pierce),imodbits_none ],
["anakin_skywalker_lightsaber", "Anakin Skywalker's Lightsaber", [("lightsaber_blue",0),("lightsaber_blueoff",ixmesh_carry)], itp_type_two_handed_wpn|itp_primary|itp_bonus_against_shield|itp_wooden_parry|itp_wooden_attack, itc_lightsaber|itcf_carry_dagger_front_left, 4000 , weight(2.1)|difficulty(14)|spd_rtng(140) | weapon_length(120)|swing_damage(125 , pierce) | thrust_damage(100 ,  pierce),imodbits_none ],

#["lightsaber_red", "Lightsaber", [("lightsaber_red",0),("lightsaber_redoff",ixmesh_carry)], itp_type_two_handed_wpn|itp_merchandise| itp_primary|itp_bonus_against_shield|itp_wooden_parry|itp_wooden_attack, itc_lightsaber|itcf_carry_dagger_front_left,
# 900 , weight(0.5)|abundance(60)|difficulty(12)|spd_rtng(120) | weapon_length(115)|swing_damage(75 , pierce) | thrust_damage(75 ,  pierce),imodbits_lightsaber ],
["lightsaber_red_multikill","Multi-hit Lightsaber (in development)", [("lightsaber_red",0),("lightsaber_redoff",ixmesh_carry)], itp_type_thrown|itp_unique|itp_primary|itp_bonus_against_shield|itp_wooden_parry|itp_wooden_attack ,itc_lightsaber|itcf_carry_dagger_front_left, 
	3000*lsbr_vluemul , weight(0.5)|abundance(0)|difficulty(0)|spd_rtng(120)|weapon_length(115)|shoot_speed(1)|swing_damage(75,pierce)|thrust_damage(75,pierce)|max_ammo(1),imodbits_none,
	[
	
	#ISSUES - non-player agents won't use it because it is a 'throwing' weapon
	
		(ti_on_weapon_attack,[
							#store the trigger parameters
							#(store_trigger_param_1, ":cur_agent"),		#doesn't seem like it works?
							#(store_trigger_param_2, ":troop_no"),
							#(get_player_agent_no, ":player_agent"),		#this only works if the player is swinging the lightsaber, not other troops, etc.
							#(agent_get_position,pos1,":player_agent"),
							#try and figure out the agent id of the person using the weapon
							(assign,":distance",99999),
							(try_for_agents,":agent"),
								(agent_is_alive,":agent"),
								(agent_is_human,":agent"),
								(agent_get_look_position, pos2, ":agent"),
								(get_distance_between_positions,":dist",pos1,pos2),
								(lt,":dist",":distance"),
								(assign,":cur_agent",":agent"),
								#(agent_get_team,":cur_agent_team", ":cur_agent"),		-> Not used, commented out by Swyter.
								(assign,":distance",":dist"),
							(end_try),							
							#do the attack
							#(agent_get_position,pos1,":cur_agent"),
                            (try_for_agents,":agent"),
								(agent_is_alive,":agent"),
								#(agent_is_human,":agent"),
								(neg|agent_is_ally, ":agent"),
								(agent_get_position, pos2, ":agent"),
								(neg|position_is_behind_position,pos2,pos1),	
								(get_distance_between_positions,":dist",pos1,pos2),
								(lt,":dist",275),
								#(position_move_z,pos2,150),
								#(particle_system_burst, "psys_game_blood", pos2,95),
								#(particle_system_burst, "psys_game_blood_2", pos2,95),
								(store_agent_hit_points,":hp",":agent",1),		# set absolute to 1 to retrieve actual hps, otherwise will return relative hp in range [0..100]
								(store_random_in_range, ":damage", 10, 50),
								(val_sub, ":hp", ":damage"),
								#(val_min, ":hp", 0),
								(agent_set_hit_points,":agent",":hp",1),		# set absolute to 1 if value is absolute, otherwise value will be treated as relative number in range [0..100]
								(agent_deliver_damage_to_agent,":cur_agent",":agent"),
								(agent_play_sound,":agent","snd_metal_hit_low_armor_high_damage"),
								#need to also play sound effect of them getting hurt or dying?  also needs to be specific to their race....
                            (try_end),
							  ]
		),
	]],


["lightsaber_custom", "Lightsaber", [("lightsaber_1h_base",0),("lightsaber_greenoff",ixmesh_carry)], itp_type_two_handed_wpn|itp_merchandise| itp_primary|itp_bonus_against_shield|itp_wooden_parry|itp_wooden_attack, itc_lightsaber|itcf_carry_dagger_front_left,
 900 , weight(0.5)|abundance(30)|difficulty(12)|spd_rtng(120) | weapon_length(115)|swing_damage(75 , pierce) | thrust_damage(75 ,  pierce),imodbits_lightsaber, 
 [(ti_on_init_item, 
  [
    (store_trigger_param_1, ":agent_no"),
    # (gt, ":agent_no", -1),
    (store_trigger_param_2, ":troop_no"),
    (try_begin), 
    	(item_get_slot, ":value", "itm_lightsaber_custom", slot_item_player_slots_begin),
    	(eq, ":value", -1),
    	(store_random_in_range, ":value", 0, 5),
  	(try_end),
    (call_script, "script_init_lightsaber", ":agent_no", ":troop_no", 0, ":value"),
    (cur_item_add_mesh, s1), #submesh 1
    (try_begin), 
    	(item_get_slot, ":value", "itm_lightsaber_custom", slot_item_player_slots_begin + 1),
    	(eq, ":value", -1),
    	(store_random_in_range, ":value", 0, 6),
  	(try_end),
    (call_script, "script_init_lightsaber", ":agent_no", ":troop_no", 1, ":value"),
    (cur_item_add_mesh, s1), #submesh 2
    ])
  ]],

["lightsaber_double_custom", "Double-Bladed Lightsaber", [("lightsaber_double_base",0),("lightsaber_red_doubleoff",ixmesh_carry)], itp_type_polearm|itp_merchandise|itp_two_handed| itp_spear|itp_primary|itp_bonus_against_shield|itp_wooden_parry|itp_wooden_attack, itc_lightsaber_double|itcf_carry_dagger_front_left, 
 1310*lsbr_vluemul , weight(0.8)|abundance(20)|difficulty(14)|spd_rtng(150) | weapon_length(170)|swing_damage(75 , pierce) | thrust_damage(75 ,  pierce),imodbits_lightsaber,
  [(ti_on_init_item, 
  [
    (store_trigger_param_1, ":agent_no"),
    # (gt, ":agent_no", -1),
    (store_trigger_param_2, ":troop_no"),
    (try_begin), 
    	(item_get_slot, ":value", "itm_lightsaber_double_custom", slot_item_player_slots_begin),
    	(eq, ":value", -1),
    	(store_random_in_range, ":value", 0, 3),
  	(try_end),
    (call_script, "script_init_double_lightsaber", ":agent_no", ":troop_no", 0, ":value"),
    (cur_item_add_mesh, s1), #submesh 1
    (try_begin), 
    	(item_get_slot, ":value", "itm_lightsaber_double_custom", slot_item_player_slots_begin + 1),
    	(eq, ":value", -1),
    	(store_random_in_range, ":value", 0, 6),
  	(try_end),
    (call_script, "script_init_double_lightsaber", ":agent_no", ":troop_no", 1, ":value"),
    (cur_item_add_mesh, s1), #submesh 2
    (try_begin), 
    	(item_get_slot, ":value", "itm_lightsaber_double_custom", slot_item_player_slots_begin + 1),
    	(eq, ":value", -1),
    	(store_random_in_range, ":value", 0, 6),
  	(try_end),
    (call_script, "script_init_double_lightsaber", ":agent_no", ":troop_no", 2, ":value"),
    (cur_item_add_mesh, s1), #submesh 3
    ])
  ]],

# unique melee weapons (melee_punch is lightsaber_noise_end)
["melee_punch","_", [("_",0),("ArcTrooperGloves_L",ixmesh_inventory)], itp_unique|itp_type_one_handed_wpn|itp_primary|itp_secondary|itp_no_parry, itc_dagger, 1 , weight(0.1)|abundance(0)|difficulty(0)|spd_rtng(105) | weapon_length(25)|swing_damage(10, blunt) | thrust_damage(10, blunt),imodbits_none ],
# axe
["durasteel_staff", "Durasteel Staff", [("iron_staff",0)], itp_type_polearm|itp_merchandise| itp_spear|itp_primary|itp_penalty_with_shield, itc_staff|itcf_carry_sword_back, 475 , weight(2.5)|abundance(100)|difficulty(0)|spd_rtng(88) | weapon_length(140)|swing_damage(25 , blunt) | thrust_damage(15,  blunt),imodbits_polearm ],
["electro_staff_medium", "Electrostaff", [("electro_staff_medium",0),("electro_staff_medium_off",ixmesh_carry)], itp_type_polearm|itp_merchandise| itp_spear|itp_primary|itp_penalty_with_shield, itc_staff|itcf_carry_sword_back, 450 , weight(2.5)|abundance(100)|difficulty(0)|spd_rtng(105) | weapon_length(120)|swing_damage(30, blunt) | thrust_damage(25 ,  blunt),imodbits_polearm ],
["electro_staff_long", "Electrostaff", [("electro_staff_long",0),("electro_staff_long_off",ixmesh_carry)], itp_type_polearm|itp_merchandise| itp_spear|itp_primary|itp_penalty_with_shield, itc_staff|itcf_carry_sword_back, 575 , weight(3.0)|abundance(100)|difficulty(0)|spd_rtng(95) | weapon_length(140)|swing_damage(40 , blunt) | thrust_damage(35 ,  blunt),imodbits_polearm ],
["gamorrean_axe_1h", "One Handed Gamorrean Axe", [("one_handed_battle_axe_a",0)], itp_type_one_handed_wpn|itp_merchandise| itp_primary|itp_secondary|itp_bonus_against_shield, itc_scimitar|itcf_carry_axe_left_hip, 75 , weight(1.5)|abundance(30)|difficulty(0)|spd_rtng(92) | weapon_length(69)|swing_damage(20, cut) | thrust_damage(0,  pierce),imodbits_axe ],
["gamorrean_axe_2h", "Two Handed Gamorrean Axe", [("two_handed_battle_axe_b",0)], itp_type_two_handed_wpn|itp_merchandise| itp_two_handed|itp_primary|itp_bonus_against_shield, itc_nodachi|itcf_carry_axe_back, 125 , weight(3.0)|abundance(30)|difficulty(0)|spd_rtng(88) | weapon_length(92)|swing_damage(32, cut) | thrust_damage(0,  pierce),imodbits_axe ],
["vibro_axe_medium_1h", "One Handed Vibro-Axe", [("vibro_axe1_1h",0)], itp_type_one_handed_wpn|itp_merchandise| itp_primary|itp_secondary|itp_bonus_against_shield, itc_scimitar|itcf_carry_axe_left_hip, 200 , weight(2.5)|abundance(40)|difficulty(0)|spd_rtng(95) | weapon_length(75)|swing_damage(30, pierce) | thrust_damage(0,  pierce),imodbits_axe ],
["vibro_axe_medium_2h", "Two Handed Vibro-Axe", [("vibro_axe1_2h",0)], itp_type_two_handed_wpn|itp_merchandise| itp_two_handed|itp_primary|itp_bonus_against_shield, itc_nodachi|itcf_carry_axe_back, 300 , weight(3.0)|abundance(40)|difficulty(0)|spd_rtng(92) | weapon_length(95)|swing_damage(35, pierce) | thrust_damage(0,  pierce),imodbits_axe ],
["vibro_axe_long_1h","One Handed Vibro-Axe", [("vibro_axe2_1h",0)], itp_type_one_handed_wpn|itp_merchandise| itp_primary|itp_secondary|itp_bonus_against_shield, itc_scimitar|itcf_carry_axe_left_hip, 250 , weight(2.0)|abundance(40)|difficulty(0)|spd_rtng(97) | weapon_length(75)|swing_damage(32, pierce) | thrust_damage(0,  pierce),imodbits_axe ],
["vibro_axe_long_2h","BD-1 Cutter Vibro-Axe", [("vibro_axe2",0)], itp_type_two_handed_wpn|itp_merchandise| itp_two_handed|itp_primary|itp_secondary|itp_bonus_against_shield, itc_nodachi|itcf_carry_axe_back, 425 , weight(4.5)|abundance(80)|difficulty(0)|spd_rtng(90) | weapon_length(120)|swing_damage(40, pierce) | thrust_damage(0,  pierce),imodbits_axe ],
["tusken_gaffi_staff", "Gaffi Staff", [("gaffi_stick_1",0)], itp_type_polearm|itp_merchandise| itp_spear|itp_primary|itp_penalty_with_shield, itc_staff|itcf_carry_sword_back, 125 , weight(2.5)|abundance(80)|difficulty(0)|spd_rtng(90) | weapon_length(100)|swing_damage(30, blunt) | thrust_damage(25, blunt),imodbits_pick ],
["tusken_gaffi_stick", "Gaffi Stick", [("tusken_gaffi_stick_2",0)], itp_type_two_handed_wpn|itp_merchandise| itp_primary|itp_bonus_against_shield, itc_bastardsword|itcf_carry_sword_back, 100 , weight(2.0)|abundance(80)|difficulty(0)|spd_rtng(100) | weapon_length(80)|swing_damage(25, blunt) | thrust_damage(20, blunt),imodbits_pick ],
["durasteel_mace","Durasteel Mace", [("spiked_mace",0)], itp_type_one_handed_wpn|itp_merchandise| itp_primary, itc_scimitar|itcf_carry_mace_left_hip, 135 , weight(3.5)|abundance(100)|difficulty(0)|spd_rtng(92) | weapon_length(90)|swing_damage(30 , blunt) | thrust_damage(0 ,  blunt),imodbits_pick ],
["baton","Baton", [("baton",0)], itp_type_one_handed_wpn|itp_merchandise| itp_primary|itp_secondary|itp_no_parry, itc_scimitar, 100 , weight(2.0)|abundance(100)|difficulty(0)|spd_rtng(105) | weapon_length(40)|swing_damage(20, blunt) | thrust_damage(0 ,  blunt),imodbits_pick ],
["trandoshan_blade","Trandoshan Blade", [("trandoshan_blade",0)], itp_type_two_handed_wpn|itp_merchandise| itp_primary, itc_bastardsword|itcf_carry_sword_back, 225 , weight(2.0)|abundance(70)|difficulty(0)|spd_rtng(95) | weapon_length(90)|swing_damage(30, cut) | thrust_damage(30,  pierce),imodbits_axe ],
["durasteel_bat","Durasteel Bat", [("durasteel_bat",0)], itp_type_two_handed_wpn|itp_merchandise|itp_two_handed|itp_primary|itp_secondary, itc_nodachi|itcf_carry_sword_back, 125 , weight(3.5)|abundance(80)|difficulty(0)|spd_rtng(94) | weapon_length(96)|swing_damage(30, blunt) | thrust_damage(0, blunt),imodbits_pick ],
["force_pike", "Force Pike", [("force_pike",0)], itp_type_polearm|itp_merchandise|itp_two_handed| itp_spear|itp_primary|itp_bonus_against_shield|itcf_carry_axe_back, itc_lightsaber_double, 775 , weight(3.5)|abundance(100)|difficulty(0)|spd_rtng(100) | weapon_length(140)|swing_damage(30, blunt) | thrust_damage(75, pierce),imodbits_polearm ],
["geonosian_static_pike", "Geonosian Static Pike", [("geonosian_static_pike",0)], itp_type_polearm|itp_merchandise|itp_two_handed| itp_spear|itp_primary|itp_bonus_against_shield|itcf_carry_axe_back, itc_lightsaber_double, 425 , weight(3.0)|abundance(70)|difficulty(0)|spd_rtng(90) | weapon_length(135)|swing_damage(30, blunt) | thrust_damage(30, pierce),imodbits_polearm ],
["pipe1","Pipe", [("pipe1",0)], itp_type_one_handed_wpn|itp_merchandise|itp_primary|itp_secondary|itp_no_parry, itc_dagger, 25 , weight(1.5)|abundance(60)|difficulty(0)|spd_rtng(85) | weapon_length(50)|swing_damage(15, blunt) | thrust_damage(15,  blunt),imodbits_pick ],
["pipe2","Pipe", [("pipe2",0)], itp_type_one_handed_wpn|itp_merchandise|itp_primary|itp_secondary|itp_no_parry, itc_dagger, 25 , weight(1.5)|abundance(60)|difficulty(0)|spd_rtng(85) | weapon_length(50)|swing_damage(15 , blunt) | thrust_damage(15,  blunt),imodbits_pick ],

# swords
#["ryyk_blade", "Ryyk Blade", [("khergit_sword_d",0),("khergit_sword_d_scabbard", ixmesh_carry)], itp_type_one_handed_wpn|itp_merchandise|itp_primary|itp_secondary|itp_bonus_against_shield, itc_scimitar|itcf_carry_sword_back|itcf_show_holster_when_drawn, 350 , weight(3)|abundance(90)|difficulty(0)|spd_rtng(105) | weapon_length(95)|swing_damage(45 , cut),imodbits_sword ],
["ryyk_blade", "Ryyk Blade", [("khergit_sword_d",0)], itp_type_one_handed_wpn|itp_merchandise|itp_primary|itp_secondary|itp_bonus_against_shield, itc_scimitar|itcf_carry_sword_back, 300 , weight(3)|abundance(90)|difficulty(0)|spd_rtng(105) | weapon_length(95)|swing_damage(30,cut)|thrust_damage(30,pierce),imodbits_sword],
["ryyk_kerarthorr", "Ryyk Kerarthorr Blade", [("ryyk_kerarthorr_down",0)], itp_type_one_handed_wpn|itp_merchandise|itp_primary|itp_secondary|itp_bonus_against_shield, itc_dagger, 125 , weight(2.5)|abundance(60)|difficulty(0)|spd_rtng(120) | weapon_length(60)|swing_damage(25,cut)|thrust_damage(25,pierce),imodbits_sword ],
["ryyk_blade_chieftain", "Chieftain Ryyk Blade", [("ryyk_blade_chieftain",0)], itp_type_one_handed_wpn|itp_merchandise|itp_primary|itp_secondary|itp_bonus_against_shield, itc_scimitar|itcf_carry_sword_back, 400 , weight(3.5)|abundance(90)|difficulty(0)|spd_rtng(100) | weapon_length(105)|swing_damage(40,cut)|thrust_damage(40,pierce),imodbits_sword ], 
["sith_sword", "Sith Sword", [("sith_sword",0)], itp_type_two_handed_wpn|itp_merchandise| itp_primary|itp_bonus_against_shield, itc_lightsaber|itcf_carry_sword_back, 475 , weight(2.0)|abundance(20)|difficulty(0)|spd_rtng(110) | weapon_length(105)|swing_damage(40, cut)|thrust_damage(40, pierce),imodbits_sword ],
["combat_knife","Combat Knife", [("CombatKnife",0)], itp_type_one_handed_wpn|itp_merchandise|itp_primary|itp_secondary|itp_no_parry|itp_bonus_against_shield, itc_dagger, 50 , weight(1.0)|abundance(60)|difficulty(0)|spd_rtng(125) | weapon_length(45)|swing_damage(20, cut)|thrust_damage(20,pierce),imodbits_sword ],
["twilek_dagger","Twilek Dagger", [("twilek_dagger",0)], itp_type_one_handed_wpn|itp_merchandise|itp_primary|itp_secondary|itp_no_parry, itc_dagger, 40 , weight(1.0)|abundance(60)|difficulty(0)|spd_rtng(125) | weapon_length(40)|swing_damage(20, cut) | thrust_damage(20 ,  pierce),imodbits_sword ],
["vibro_knuckler","Vibro Knuckler", [("vibro_knuckler",0)], itp_type_one_handed_wpn|itp_merchandise|itp_primary|itp_secondary|itp_no_parry, itc_knuckler, 175 , weight(0.5)|abundance(80)|difficulty(0)|spd_rtng(125) | weapon_length(45)|swing_damage(0, pierce) | thrust_damage(25, pierce),imodbits_sword ],
["vibro_blade1","Vibro Blade", [("vibro_blade1_new",0)], itp_type_one_handed_wpn|itp_merchandise|itp_primary|itp_secondary|itp_no_parry|itp_bonus_against_shield, itc_dagger, 53 , weight(1.25)|abundance(60)|difficulty(0)|spd_rtng(112) | weapon_length(47)|swing_damage(25, pierce) | thrust_damage(25, pierce),imodbits_sword ],
["vibro_blade2","Vibro Blade", [("vibro_blade2_new",0)], itp_type_one_handed_wpn|itp_merchandise|itp_primary|itp_secondary|itp_no_parry|itp_bonus_against_shield, itc_dagger, 53 , weight(1.25)|abundance(60)|difficulty(0)|spd_rtng(112) | weapon_length(47)|swing_damage(25, pierce) | thrust_damage(25, pierce),imodbits_sword ],
["vibro_blade3","Vibro Blade", [("vibro_blade3_new",0)], itp_type_one_handed_wpn|itp_merchandise|itp_primary|itp_secondary|itp_no_parry|itp_bonus_against_shield, itc_dagger, 53 , weight(1.25)|abundance(60)|difficulty(0)|spd_rtng(112) | weapon_length(47)|swing_damage(25, pierce) | thrust_damage(25, pierce),imodbits_sword ],
["vibro_blade4","Vibro Blade", [("vibro_blade4_new",0)], itp_type_one_handed_wpn|itp_merchandise|itp_primary|itp_secondary|itp_no_parry|itp_bonus_against_shield, itc_dagger, 53 , weight(1.25)|abundance(60)|difficulty(0)|spd_rtng(112) | weapon_length(47)|swing_damage(25, pierce) | thrust_damage(25, pierce),imodbits_sword ],
#["vibro_sword1a", "Vibro Sword", [("vibro_sword1a",0)], itp_type_one_handed_wpn|itp_merchandise|itp_primary|itp_bonus_against_shield, itc_longsword|itcf_carry_sword_back, 400 , weight(1.5)|abundance(90)|difficulty(0)|spd_rtng(99) | weapon_length(95)|swing_damage(52 , cut) | thrust_damage(45 ,  pierce),imodbits_sword ], 
["vibro_sword1b", "Vibro Sword", [("vibro_sword1b",0)], itp_type_one_handed_wpn|itp_merchandise|itp_primary|itp_bonus_against_shield, itc_longsword|itcf_carry_sword_back, 415 , weight(1.5)|abundance(80)|difficulty(0)|spd_rtng(99) | weapon_length(95)|swing_damage(35, pierce) | thrust_damage(35,  pierce),imodbits_sword ], 
#["vibro_sword2a","Two Handed Vibro Sword", [("vibro_sword2a",0)], itp_type_two_handed_wpn|itp_merchandise|itp_two_handed|itp_primary|itp_bonus_against_shield, itc_greatsword|itcf_carry_sword_back, 600 , weight(2.75)|abundance(90)|difficulty(0)|spd_rtng(93) | weapon_length(110)|swing_damage(60 , cut) | thrust_damage(55 ,  pierce),imodbits_sword ],
["vibro_sword2b","Two Handed Vibro Sword", [("vibro_sword2b",0)], itp_type_two_handed_wpn|itp_merchandise|itp_two_handed|itp_primary|itp_bonus_against_shield, itc_greatsword|itcf_carry_sword_back, 498 , weight(2.75)|abundance(90)|difficulty(0)|spd_rtng(93) | weapon_length(110)|swing_damage(45, pierce) | thrust_damage(45,  pierce),imodbits_sword ], 
#["vibro_sword3a", "Vibro Sword", [("vibro_sword3a",0)], itp_type_one_handed_wpn|itp_merchandise|itp_primary|itp_bonus_against_shield, itc_longsword|itcf_carry_sword_back, 485 , weight(1.3)|abundance(50)|difficulty(0)|spd_rtng(100) | weapon_length(100)|swing_damage(55 , cut) | thrust_damage(50 ,  pierce),imodbits_sword ], 
#["vibro_sword3b", "Vibro Sword", [("vibro_sword3a",0)], itp_type_one_handed_wpn|itp_merchandise|itp_primary|itp_bonus_against_shield, itc_longsword|itcf_carry_sword_back, 485 , weight(1.3)|abundance(50)|difficulty(0)|spd_rtng(100) | weapon_length(100)|swing_damage(55 , cut) | thrust_damage(50 ,  pierce),imodbits_sword ], 
#["vibro_sword3c", "Vibro Sword", [("vibro_sword3c",0)], itp_type_one_handed_wpn|itp_merchandise|itp_primary|itp_bonus_against_shield, itc_longsword|itcf_carry_sword_back, 485 , weight(1.3)|abundance(50)|difficulty(0)|spd_rtng(100) | weapon_length(100)|swing_damage(55 , cut) | thrust_damage(50 ,  pierce),imodbits_sword ], 
#["vibro_sword3d", "Vibro Sword", [("vibro_sword3d",0)], itp_type_one_handed_wpn|itp_merchandise|itp_primary|itp_bonus_against_shield, itc_longsword|itcf_carry_sword_back, 485 , weight(1.3)|abundance(50)|difficulty(0)|spd_rtng(100) | weapon_length(100)|swing_damage(55 , cut) | thrust_damage(50 ,  pierce),imodbits_sword ], 
["vibro_sword3_gold", "Vibro Sword", [("vibro_sword3a",0)], itp_type_one_handed_wpn|itp_merchandise|itp_primary|itp_bonus_against_shield, itc_longsword|itcf_carry_sword_back, 485 , weight(1.3)|abundance(50)|difficulty(0)|spd_rtng(100) | weapon_length(100)|swing_damage(40 , pierce) | thrust_damage(40,  pierce),imodbits_sword ], 
["vibro_sword3_blue", "Vibro Sword", [("vibro_sword3c",0)], itp_type_one_handed_wpn|itp_merchandise|itp_primary|itp_bonus_against_shield, itc_longsword|itcf_carry_sword_back, 485 , weight(1.3)|abundance(50)|difficulty(0)|spd_rtng(100) | weapon_length(100)|swing_damage(40 , pierce) | thrust_damage(40,  pierce),imodbits_sword ], 
["vibro_sword3_red", "Vibro Sword", [("vibro_sword3d",0)], itp_type_one_handed_wpn|itp_merchandise|itp_primary|itp_bonus_against_shield, itc_longsword|itcf_carry_sword_back, 485 , weight(1.3)|abundance(50)|difficulty(0)|spd_rtng(100) | weapon_length(100)|swing_damage(40 , pierce) | thrust_damage(40,  pierce),imodbits_sword ], 
["weapons_end", "<dummy>", [("_",0)], 0,0,0,0,imodbits_none],

# practice/training/tutorial lightsabers (no merchandise flag)
["tutorial_lightsaber", "Lightsaber", [("lightsaber_yellow",0),("lightsaber_yellowoff",ixmesh_carry)], itp_type_two_handed_wpn| itp_primary|itp_bonus_against_shield|itp_wooden_parry|itp_wooden_attack, itc_lightsaber|itcf_carry_dagger_front_left, 1500 , weight(2.25)|difficulty(0)|spd_rtng(120) | weapon_length(115)|swing_damage(50, pierce) | thrust_damage(35,  pierce),imodbits_none ],
["practice_vibro_axe_medium", "Gamorrean Vibro-Axe", [("vibro_axe1",0)], itp_type_one_handed_wpn| itp_primary|itp_secondary|itp_bonus_against_shield, itc_scimitar|itcf_carry_axe_left_hip, 500 , weight(2.5)|abundance(100)|difficulty(0)|spd_rtng(95) | weapon_length(75)|swing_damage(35, cut) | thrust_damage(0 ,  pierce),imodbits_none ],
["practice_vibro_axe_long","BD-1 Cutter Vibro-Axe", [("vibro_axe2",0)], itp_type_two_handed_wpn| itp_two_handed|itp_primary|itp_secondary|itp_bonus_against_shield, itc_nodachi|itcf_carry_axe_back, 700 , weight(4.5)|difficulty(0)|spd_rtng(90) | weapon_length(110)|swing_damage(40 , cut) | thrust_damage(0 ,  pierce),imodbits_none ], 
["practice_vibro_axe_long_no_attack","BD-1 Cutter Vibro-Axe", [("vibro_axe2",0)],itp_type_polearm|itp_spear|itp_primary|itp_penalty_with_shield,itc_parry_polearm|itcf_carry_sword_back,9, weight(3.5)|spd_rtng(120) | weapon_length(115)|swing_damage(0,blunt) | thrust_damage(0,blunt),imodbits_none],
["practice_vibro_blade","Vibro Blade", [("vibro_blade1",0)], itp_type_one_handed_wpn|itp_primary|itp_secondary|itp_bonus_against_shield, itc_dagger, 175 , weight(1.25)|difficulty(0)|spd_rtng(112) | weapon_length(47)|swing_damage(40 , cut) | thrust_damage(20 ,  pierce),imodbits_none ],
["practice_vibro_sword3a", "Vibro Sword", [("vibro_sword3a",0)], itp_type_one_handed_wpn|itp_primary|itp_bonus_against_shield, itc_longsword|itcf_carry_sword_back, 500 , weight(1.3)|abundance(90)|difficulty(0)|spd_rtng(100) | weapon_length(100)|swing_damage(30, cut) | thrust_damage(20,  pierce),imodbits_none ], 
["practice_vibro_sword2b","Two Handed Vibro Sword", [("vibro_sword2b",0)], itp_type_two_handed_wpn|itp_two_handed|itp_primary|itp_bonus_against_shield, itc_greatsword|itcf_carry_sword_back, 600 , weight(2.75)|abundance(90)|difficulty(0)|spd_rtng(93) | weapon_length(110)|swing_damage(35, cut) | thrust_damage(25,  pierce),imodbits_none ], 
["practice_vibro_sword1b", "Vibro Sword", [("vibro_sword1b",0)], itp_type_one_handed_wpn|itp_primary|itp_bonus_against_shield, itc_longsword|itcf_carry_sword_back, 400 , weight(1.5)|abundance(90)|difficulty(0)|spd_rtng(99) | weapon_length(95)|swing_damage(30, cut) | thrust_damage(20 ,  pierce),imodbits_none ], 

#special items with unique flag(quick battle, etc)
["quick_battle_armor", "Armor", [("jacket_closed_b",0)], itp_unique|itp_type_body_armor|itp_covers_legs |itp_civilian  ,0, 380 , weight(2)|abundance(0)|head_armor(0)|body_armor(32)|leg_armor(14)|difficulty(0) ,imodbits_none ],
["transparent_helmet_armor", "Transparent Helmet with Body Armor", [("_",0),("transparent_helmet_inv",ixmesh_inventory)], itp_unique|itp_type_head_armor|itp_doesnt_cover_hair|itp_civilian,0, 140 , weight(0.25)|abundance(0)|head_armor(15)|body_armor(35)|leg_armor(15)|difficulty(0) ,imodbits_none ], 
["twilek_female_helmet_armor", "Twilek Female Helmet with Body Armor", [("twilekwrap",0)], itp_unique|itp_type_head_armor|itp_doesnt_cover_hair|itp_civilian,0,  500 , weight(1)|abundance(0)|head_armor(15)|body_armor(35)|leg_armor(15)|difficulty(0) ,imodbits_none ],  
["twilek_male_head_bib", "Bib Fortuna Head", [("twilek_head_bib",0)], itp_unique|itp_type_head_armor|itp_covers_head |itp_civilian ,0, 1500 , weight(3)|head_armor(15)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_none ],
["weequay_head_helmet_a", "Weequay Head", [("weequay_head_helmet_a",0)], itp_unique|itp_type_head_armor|itp_covers_head |itp_civilian ,0, 500 , weight(2)|head_armor(5)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_none ],
["weequay_head_helmet_b", "Weequay Head", [("weequay_head_helmet_b",0)], itp_unique|itp_type_head_armor|itp_covers_head |itp_civilian ,0, 500 , weight(2)|head_armor(5)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_none ],
["klatooinian_head_helmet_a", "Klatooinian Head", [("klatooinian_head_helmet_a",0)], itp_unique|itp_type_head_armor|itp_covers_head |itp_civilian ,0, 500 , weight(2)|head_armor(5)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_none ],
["nikto_head_helmet_a", "Nikto Head", [("nikto_head_helmet_a",0)], itp_unique|itp_type_head_armor|itp_covers_head |itp_civilian ,0, 500 , weight(2)|head_armor(5)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_none ],
["nikto_head_helmet_b", "Nikto Head", [("nikto_head_helmet_b",0)], itp_unique|itp_type_head_armor|itp_covers_head |itp_civilian ,0, 500 , weight(2)|head_armor(5)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_none ],
["nikto_head_helmet_c", "Nikto Head", [("nikto_head_helmet_c",0)], itp_unique|itp_type_head_armor|itp_covers_head |itp_civilian ,0, 500 , weight(2)|head_armor(5)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_none ],
["tarkin_head", "Grand Moff Tarkin Head", [("tarkin_head",0)], itp_unique|itp_type_head_armor|itp_covers_head |itp_civilian ,0, 1500 , weight(1)|head_armor(15)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_none ],
["ben_head", "Ben Kenobi Head", [("ben_head",0)], itp_unique|itp_type_head_armor|itp_covers_head |itp_civilian ,0, 1500 , weight(1)|head_armor(15)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_none ],
["leia_head", "Leia Organa Head", [("leia_head",0)], itp_unique|itp_type_head_armor|itp_covers_head |itp_civilian ,0, 1500 , weight(1)|head_armor(15)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_none ],

#["leia_head", "Leia Organa Head", [("leia_head",0)], itp_unique|itp_type_head_armor|itp_covers_head |itp_civilian ,0, 1500 , weight(1)|head_armor(15)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_none ],
["rancor_body_a", "Rancor Body", [("swy_rancor",0)], itp_unique|itp_type_body_armor |itp_covers_legs |itp_civilian  ,0, 1000 , weight(64)|head_armor(35)|body_armor(90)|leg_armor(35)|difficulty(0) ,imodbits_none ],
["rancor_body_b", "Rancor Body", [("swy_rancor_alt",0)], itp_unique|itp_type_body_armor |itp_covers_legs |itp_civilian  ,0, 1000 , weight(64)|head_armor(35)|body_armor(90)|leg_armor(35)|difficulty(0) ,imodbits_none ],
["rancor_body_c", "Rancor Body", [("swy_rancor_mutant",0)], itp_unique|itp_type_body_armor |itp_covers_legs |itp_civilian  ,0, 1000 , weight(64)|head_armor(35)|body_armor(90)|leg_armor(35)|difficulty(0) ,imodbits_none ],
["rancor_attack","_", [("_",0),("ArcTrooperGloves_L",ixmesh_inventory)], itp_unique|itp_type_one_handed_wpn|itp_primary|itp_secondary|itp_bonus_against_shield|itp_no_parry, itc_rancor, 250 , weight(64)|abundance(0)|difficulty(0)|spd_rtng(85) | weapon_length(15)|swing_damage(60, cut) | thrust_damage(45, pierce),imodbits_none ],
["rancor_keeper_armor", "Rancor Keeper Armor", [("rancor_keeper",0)], itp_unique|itp_type_body_armor |itp_covers_legs |itp_civilian  ,0, 500 , weight(20)|head_armor(5)|body_armor(35)|leg_armor(10)|difficulty(0) ,imodbits_none ],
["yoda_armor", "Yoda Armor and Chair", [("yoda",0)], itp_unique|itp_type_body_armor |itp_covers_legs |itp_civilian  ,0, 2000 , weight(40)|head_armor(20)|body_armor(50)|leg_armor(20)|difficulty(0) ,imodbits_none ],
["yoda_lightsaber", "Yoda's Lightsaber", [("lightsaber_green_1h",0),("lightsaber_green_1hoff",ixmesh_carry)], itp_unique|itp_type_one_handed_wpn|itp_primary|itp_bonus_against_shield|itp_wooden_parry|itp_wooden_attack, itc_lightsaber_1h, 605 , weight(0.1)|abundance(0)|difficulty(0)|spd_rtng(105) | weapon_length(100)|swing_damage(75 , pierce) | thrust_damage(75 ,  pierce),imodbits_none ],
["yoda_speeder","Yoda's Transparent Speeder", [("_",0),("force_block_inv",ixmesh_inventory)],  itp_unique|itp_type_horse, 0, 500,abundance(0)|hit_points(40)|body_armor(25)|difficulty(0)|horse_speed(40)|horse_maneuver(50)|horse_charge(5),imodbits_none],
["jabba_armor", "Jabba Armor and Chair", [("jabba",0)], itp_unique|itp_type_body_armor |itp_covers_legs |itp_civilian  ,0, 2000 , weight(80)|head_armor(30)|body_armor(80)|leg_armor(25)|difficulty(0) ,imodbits_none ],
["jabba_attack","Jabba No Attack", [("_",0),("transparent_helmet_inv",ixmesh_inventory)], itp_type_two_handed_wpn|itp_unique|itp_primary, 0, 1 , weight(1)|abundance(0)|difficulty(0)|spd_rtng(40) | weapon_length(25)|swing_damage(0, blunt) | thrust_damage(0, blunt),imodbits_none ],
["jabba_speeder","Jabba's Transparent Speeder", [("_",0),("force_block_inv",ixmesh_inventory)],     itp_unique|itp_type_horse, 0, 500,abundance(0)|hit_points(50)|body_armor(50)|difficulty(0)|horse_speed(30)|horse_maneuver(35)|horse_charge(80),imodbits_none],
["transparent_head", "Transparent Head", [("_",0),("transparent_helmet_inv",ixmesh_inventory)], itp_unique|itp_type_head_armor|itp_covers_head|itp_civilian,0, 1 , weight(0.25)|abundance(0)|head_armor(1)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_none ], 
["transparent_body", "Transparent Body", [("_",0),("transparent_helmet_inv",ixmesh_inventory)], itp_unique|itp_type_body_armor|itp_covers_legs|itp_civilian,0, 1 , weight(0.25)|abundance(0)|head_armor(0)|body_armor(1)|leg_armor(0)|difficulty(0) ,imodbits_none ], 
["transparent_hands", "Transparent Hands", [("_",0),("transparent_helmet_inv",ixmesh_inventory)], itp_unique|itp_type_hand_armor|itp_civilian,0, 1 , weight(0.25)|abundance(0)|head_armor(0)|body_armor(1)|leg_armor(0)|difficulty(0) ,imodbits_none ], 
["transparent_feet", "Transparent Feet", [("_",0),("transparent_helmet_inv",ixmesh_inventory)], itp_unique|itp_type_foot_armor|itp_civilian,0, 1 , weight(0.25)|abundance(0)|head_armor(0)|body_armor(0)|leg_armor(1)|difficulty(0) ,imodbits_none ], 
 
# unique items, no merchandise tag - removed itp_unique flag since that means its un-lootable, instead I gave these to troops so there is a chance they will be dropped after a battle
# some unique items are in other parts of the file (lightsabers had to be between lightsabers_noise_begin, etc)
["darth_vader_helmet", "Darth Vader's Helmet", [("dvader_helm",0)], itp_type_head_armor|itp_civilian|itp_covers_head ,0, 2000 , weight(2)|head_armor(28)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_none ],
["darth_vader_armor", "Darth Vader's Armor",   [("dvader_body",0)], itp_type_body_armor |itp_covers_legs |itp_civilian  ,0, 3000 , weight(6)|head_armor(0)|body_armor(60)|leg_armor(18)|difficulty(0) ,imodbits_none ],
["darth_vader_feet", "Darth Vader's Feet", [("_",0),("transparent_helmet_inv",ixmesh_inventory)], itp_unique|itp_type_foot_armor|itp_civilian,0, 1 , weight(0.25)|abundance(0)|head_armor(0)|body_armor(0)|leg_armor(47)|difficulty(0) ,imodbits_none ],
["princess_leia_outfit", "Princess Leia's Outfit", [("princess_leia_outfit",0)], itp_type_body_armor  |itp_covers_legs|itp_civilian ,0, 1200 , weight(2)|head_armor(0)|body_armor(40)|leg_armor(12)|difficulty(0) ,imodbits_none ],
["princess_leia_blaster", "Princess Leia's DDC Defender", [("DDC_defender",0)], itp_type_pistol|itp_primary|itp_bonus_against_shield,itcf_shoot_pistol|itcf_carry_revolver_right|itcf_reload_pistol, 2000 , weight(1.2)|difficulty(0)|spd_rtng(150) | shoot_speed(170) | thrust_damage(30 ,pierce)|max_ammo(16)|accuracy(95),imodbits_none, [(ti_on_weapon_attack, [(play_sound,"snd_littleblaster"),(position_move_x, pos1,14),(position_move_y, pos1,18)])]],  
["han_solo_outfit", "Han Solo's Outfit", [("vest_open_c",0)], itp_type_body_armor |itp_covers_legs |itp_civilian  ,0, 1200 , weight(2)|head_armor(0)|body_armor(45)|leg_armor(14)|difficulty(0) ,imodbits_none ],
["han_solo_blaster", "Han Solo's DL-44", [("DL44b",0)], itp_type_pistol|itp_primary|itp_bonus_against_shield,itcf_shoot_pistol|itcf_carry_revolver_right|itcf_reload_pistol, 2500 , weight(1.5)|difficulty(0)|spd_rtng(140) | shoot_speed(190) | thrust_damage(35,pierce)|max_ammo(24)|accuracy(96),imodbits_none, [(ti_on_weapon_attack, [(play_sound,"snd_bigblaster19"),(position_move_x, pos1,6),(position_move_y, pos1,8)])]],
#["luke_skywalker_outfit", "Luke Skywalker's Outfit", [("outfit_tan",0)], itp_type_body_armor |itp_covers_legs |itp_civilian  ,0, 1000 , weight(2.5)|head_armor(0)|body_armor(40)|leg_armor(12)|difficulty(0) ,imodbits_none ],
["luke_skywalker_outfit", "Luke Skywalker's Outfit", [("jedi_robe_b",0)], itp_type_body_armor |itp_civilian |itp_covers_legs |itp_civilian,0,  2500 , weight(0.8)|abundance(0)|head_armor(0)|body_armor(55)|leg_armor(18)|difficulty(0) ,imodbits_cloth ],
#["dath_maul_lightsaber", "Darth Maul's Double-Bladed Lightsaber", [("lightsaber_red_double",0),("lightsaber_red_doubleoff",ixmesh_carry)], itp_type_polearm|itp_two_handed| itp_spear|itp_primary|itp_bonus_against_shield|itp_wooden_parry|itp_wooden_attack, itc_lightsaber_double|itcf_carry_quiver_right_vertical, 5000 , weight(3.5)|abundance(100)|difficulty(0)|spd_rtng(115) | weapon_length(155)|swing_damage(120 , cut) | thrust_damage(85 ,  pierce),imodbits_none ],
["chewbacca_bowcaster", "Chewbacca's Bowcaster", [("wookiee_bowcaster",0)], itp_type_crossbow|itp_primary|itp_bonus_against_shield|itp_two_handed,itcf_shoot_crossbow|itcf_carry_crossbow_back|itcf_reload_musket, 3000 , weight(2)|difficulty(0)|spd_rtng(135) | shoot_speed(170) | thrust_damage(45 ,pierce)|max_ammo(24)|accuracy(95),imodbits_none, [(ti_on_weapon_attack, [(play_sound,"snd_bigblaster22"),(position_move_x, pos1,6),(position_move_y, pos1,8)])]],
["chewbacca_ryyk_blade", "Chewbacca's Ryyk Blade", [("ryyk_blade_chieftain",0)], itp_type_one_handed_wpn|itp_primary|itp_secondary|itp_bonus_against_shield, itc_scimitar|itcf_carry_sword_back, 1000 , weight(3.0)|abundance(90)|difficulty(0)|spd_rtng(110) | weapon_length(110)|swing_damage(60, cut),imodbits_none ], 
["boba_fett_armor", "Boba Fett's Armor", [("fettarmour",0)], itp_type_body_armor  |itp_covers_legs|itp_civilian ,0, 2500 , weight(6)|head_armor(0)|body_armor(60)|leg_armor(10)|difficulty(0) ,imodbits_none ],
["boba_fett_helmet", "Boba Fett's Helmet", [("fetthelm",0)], itp_type_head_armor|itp_covers_head|itp_civilian,0, 1800 , weight(2)|head_armor(28)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_none ],
["boba_fett_boots", "Boba Fett's Boots", [("fettboots",0)], itp_type_foot_armor | itp_attach_armature|itp_civilian,0, 434 , weight(2)|head_armor(0)|body_armor(0)|leg_armor(18)|difficulty(0) ,imodbits_none ],
["boba_fett_blaster", "Boba Fett's EE-3", [("EE3",0),("EE3_inventory",ixmesh_inventory)], itp_type_crossbow |itp_primary|itp_bonus_against_shield|itp_two_handed,itcf_shoot_crossbow|itcf_carry_spear|itcf_reload_pistol, 3400 , weight(2.5)|difficulty(0)|spd_rtng(140) | shoot_speed(190) | thrust_damage(50 ,pierce)|max_ammo(32)|accuracy(95),imodbits_none, [(ti_on_weapon_attack, [(play_sound,"snd_bigblaster22"),(position_move_x, pos1,6),(position_move_y, pos1,8)])]], 
#["jango_fett_blaster", "Jango Fett's Westar-34", [("westar",0)], itp_type_pistol|itp_primary|itp_bonus_against_shield,itcf_shoot_pistol|itcf_carry_revolver_right|itcf_reload_pistol, 2400 , weight(1.5)|difficulty(0)|spd_rtng(150) | shoot_speed(170) | thrust_damage(35,pierce)|max_ammo(24)|accuracy(96),imodbits_none, [(ti_on_weapon_attack, [(play_sound,"snd_laser_fire"),(position_move_x, pos1,6),(position_move_y, pos1,8)])]],  
["joruus_lightsaber", "Cbaoth's Lightsaber", [("lightsaber_red",0),("lightsaber_redoff",ixmesh_carry)], itp_type_two_handed_wpn|itp_primary|itp_bonus_against_shield|itp_wooden_parry|itp_wooden_attack, itc_lightsaber|itcf_carry_dagger_front_left, 4000 , weight(2.1)|difficulty(14)|spd_rtng(140) | weapon_length(120)|swing_damage(100 , pierce) | thrust_damage(100 ,  pierce),imodbits_none ], #@>>> Added by Swyter
["dengar_armor", "Dengar's Armor", [("dengarbody",0)], itp_type_body_armor  |itp_covers_legs|itp_civilian ,0, 2500 , weight(6)|head_armor(0)|body_armor(60)|leg_armor(10)|difficulty(0) ,imodbits_none ],
["dengar_helmet", "Dengar's Head Wrapping", [("dengarhat",0)], itp_type_head_armor|itp_civilian,0, 1800 , weight(2)|head_armor(28)|body_armor(0)|leg_armor(0)|difficulty(0) ,imodbits_none ],
["dengar_boots", "Dengar's Boots", [("dengarboots",0)], itp_type_foot_armor | itp_attach_armature|itp_civilian,0, 434 , weight(2)|head_armor(0)|body_armor(0)|leg_armor(18)|difficulty(0) ,imodbits_none ],
["dengar_gloves","Dengar's Gloves", [("dengar_glove_L",0)], itp_type_hand_armor|itp_civilian,0, 300, weight(0.25)|abundance(0)|body_armor(5)|difficulty(0),imodbits_none],
["weequay_vibro_axe","Weequay's Vibro-Axe", [("vibro_axe2",0)], itp_type_two_handed_wpn| itp_two_handed|itp_primary|itp_secondary|itp_bonus_against_shield, itc_nodachi|itcf_carry_axe_back, 3600 , weight(4.5)|difficulty(0)|spd_rtng(110) | weapon_length(115)|swing_damage(70 , cut) | thrust_damage(0 ,  pierce),imodbits_none ],

 
# force powers - added itp_unique so they can't be dropped after a battle (force_shield and force_block are under shields_begin section)
#["force_push","Force Push", [("force_push",0),("force_push_inv",ixmesh_inventory)], itp_type_thrown |itp_merchandise|itp_unique|itp_primary|itp_secondary,itcf_throw_stone, 400 , weight(0.1)|abundance(100)|difficulty(4)|spd_rtng(100) | shoot_speed(180) | thrust_damage(40 , blunt)|max_ammo(16)|weapon_length(8)|accuracy(100),imodbits_none],
#["force_lightning","Force Lightning", [("force_lightning",0)], itp_type_thrown |itp_merchandise|itp_unique|itp_primary|itp_secondary,itcf_throw_stone, 400 , weight(0.1)|abundance(100)|difficulty(4)|spd_rtng(100) | shoot_speed(180) | thrust_damage(40 , pierce)|max_ammo(16)|weapon_length(8)|accuracy(100),imodbits_none],
# negative damage does not work, comment out force heal
#["force_heal","Force Heal", [("force_push",0),("force_push_inv",ixmesh_inventory)], itp_type_thrown |itp_merchandise|itp_primary|itp_secondary,itcf_throw_stone, 500 , weight(0.1)|abundance(100)|difficulty(0)|spd_rtng(100) | shoot_speed(190) | thrust_damage(-40 , blunt)|max_ammo(25)|weapon_length(8)|accuracy(92),imodbits_none],
# accurancy doesn't seem to help?
#force_throw_lightsaber for the troops = low ammo so troops eventually attack+ itcf_throw_stone so it disappears
["force_throw_lightsaber_green",	"Throwing Lightsaber", [("lightsaber_green",0)], itp_type_thrown |itp_unique|itp_primary|itp_secondary|itp_bonus_against_shield|itp_wooden_attack,itcf_throw_stone,900, weight(0.5)|abundance(60)|difficulty(4)|spd_rtng(50) | shoot_speed(35) | thrust_damage(80,pierce)|max_ammo(12)|weapon_length(115)|accuracy(98),imodbits_none, [(ti_on_weapon_attack, [(play_sound,"snd_throw_lightsaber"),(position_move_x, pos1,0),(position_move_y, pos1,0)])], force_fac],
["force_throw_lightsaber_blue",		"Throwing Lightsaber", [("lightsaber_blue",0)], itp_type_thrown |itp_unique|itp_primary|itp_secondary|itp_bonus_against_shield|itp_wooden_attack,itcf_throw_stone,900, weight(0.5)|abundance(60)|difficulty(4)|spd_rtng(50) | shoot_speed(35) | thrust_damage(80,pierce)|max_ammo(12)|weapon_length(115)|accuracy(98),imodbits_none, [(ti_on_weapon_attack, [(play_sound,"snd_throw_lightsaber"),(position_move_x, pos1,0),(position_move_y, pos1,0)])], force_fac],
["force_throw_lightsaber_orange",	"Throwing Lightsaber", [("lightsaber_orange",0)], itp_type_thrown |itp_unique|itp_primary|itp_secondary|itp_bonus_against_shield|itp_wooden_attack,itcf_throw_stone,900, weight(0.5)|abundance(20)|difficulty(4)|spd_rtng(50) | shoot_speed(35) | thrust_damage(80,pierce)|max_ammo(12)|weapon_length(115)|accuracy(98),imodbits_none, [(ti_on_weapon_attack, [(play_sound,"snd_throw_lightsaber"),(position_move_x, pos1,0),(position_move_y, pos1,0)])], force_fac],
["force_throw_lightsaber_purple",	"Throwing Lightsaber", [("lightsaber_purple",0)], itp_type_thrown |itp_unique|itp_primary|itp_secondary|itp_bonus_against_shield|itp_wooden_attack,itcf_throw_stone,900, weight(0.5)|abundance(40)|difficulty(4)|spd_rtng(50) | shoot_speed(35) | thrust_damage(80,pierce)|max_ammo(12)|weapon_length(115)|accuracy(98),imodbits_none, [(ti_on_weapon_attack, [(play_sound,"snd_throw_lightsaber"),(position_move_x, pos1,0),(position_move_y, pos1,0)])], force_fac],
["force_throw_lightsaber_yellow",	"Throwing Lightsaber", [("lightsaber_yellow",0)], itp_type_thrown |itp_unique|itp_primary|itp_secondary|itp_bonus_against_shield|itp_wooden_attack,itcf_throw_stone,900, weight(0.5)|abundance(20)|difficulty(4)|spd_rtng(50) | shoot_speed(35) | thrust_damage(80,pierce)|max_ammo(12)|weapon_length(115)|accuracy(98),imodbits_none, [(ti_on_weapon_attack, [(play_sound,"snd_throw_lightsaber"),(position_move_x, pos1,0),(position_move_y, pos1,0)])], force_fac],
["force_throw_lightsaber_red",		"Throwing Lightsaber", [("lightsaber_red",0)], itp_type_thrown |itp_unique|itp_primary|itp_secondary|itp_bonus_against_shield|itp_wooden_attack,itcf_throw_stone,900, weight(0.5)|abundance(60)|difficulty(4)|spd_rtng(50) | shoot_speed(35) | thrust_damage(80,pierce)|max_ammo(12)|weapon_length(115)|accuracy(98),imodbits_none, [(ti_on_weapon_attack, [(play_sound,"snd_throw_lightsaber"),(position_move_x, pos1,0),(position_move_y, pos1,0)])], force_fac],
#force_throw_lightsaber (merchandise only with high ammo for player)  - #itcf_throw_stone, itcf_throw_knife, itcf_throw_axe
["force_throw_lightsaber_green_merch",	"Throwing Lightsaber", [("lightsaber_green",0)], itp_type_thrown |itp_merchandise|itp_primary|itp_secondary|itp_bonus_against_shield|itp_wooden_attack,itcf_throw_knife,900, weight(0.5)|abundance(60)|difficulty(4)|spd_rtng(50) | shoot_speed(35) | thrust_damage(80,pierce)|max_ammo(99)|weapon_length(115)|accuracy(98),imodbits_none, [(ti_on_weapon_attack, [(play_sound,"snd_throw_lightsaber"),(position_move_x, pos1,0),(position_move_y, pos1,0)])], force_fac],
["force_throw_lightsaber_blue_merch",	"Throwing Lightsaber", [("lightsaber_blue",0)], itp_type_thrown |itp_merchandise|itp_primary|itp_secondary|itp_bonus_against_shield|itp_wooden_attack,itcf_throw_knife,900, weight(0.5)|abundance(60)|difficulty(4)|spd_rtng(50) | shoot_speed(35) | thrust_damage(80,pierce)|max_ammo(99)|weapon_length(115)|accuracy(98),imodbits_none, [(ti_on_weapon_attack, [(play_sound,"snd_throw_lightsaber"),(position_move_x, pos1,0),(position_move_y, pos1,0)])], force_fac],
["force_throw_lightsaber_orange_merch",	"Throwing Lightsaber", [("lightsaber_orange",0)], itp_type_thrown |itp_merchandise|itp_primary|itp_secondary|itp_bonus_against_shield|itp_wooden_attack,itcf_throw_knife,900, weight(0.5)|abundance(20)|difficulty(4)|spd_rtng(50) | shoot_speed(35) | thrust_damage(80,pierce)|max_ammo(99)|weapon_length(115)|accuracy(98),imodbits_none, [(ti_on_weapon_attack, [(play_sound,"snd_throw_lightsaber"),(position_move_x, pos1,0),(position_move_y, pos1,0)])], force_fac],
["force_throw_lightsaber_purple_merch",	"Throwing Lightsaber", [("lightsaber_purple",0)], itp_type_thrown |itp_merchandise|itp_primary|itp_secondary|itp_bonus_against_shield|itp_wooden_attack,itcf_throw_knife,900, weight(0.5)|abundance(40)|difficulty(4)|spd_rtng(50) | shoot_speed(35) | thrust_damage(80,pierce)|max_ammo(99)|weapon_length(115)|accuracy(98),imodbits_none, [(ti_on_weapon_attack, [(play_sound,"snd_throw_lightsaber"),(position_move_x, pos1,0),(position_move_y, pos1,0)])], force_fac],
["force_throw_lightsaber_yellow_merch",	"Throwing Lightsaber", [("lightsaber_yellow",0)], itp_type_thrown |itp_merchandise|itp_primary|itp_secondary|itp_bonus_against_shield|itp_wooden_attack,itcf_throw_knife,900, weight(0.5)|abundance(20)|difficulty(4)|spd_rtng(50) | shoot_speed(35) | thrust_damage(80,pierce)|max_ammo(99)|weapon_length(115)|accuracy(98),imodbits_none, [(ti_on_weapon_attack, [(play_sound,"snd_throw_lightsaber"),(position_move_x, pos1,0),(position_move_y, pos1,0)])], force_fac],
["force_throw_lightsaber_red_merch",		"Throwing Lightsaber", [("lightsaber_red",0)], itp_type_thrown |itp_merchandise|itp_primary|itp_secondary|itp_bonus_against_shield|itp_wooden_attack,itcf_throw_knife,900, weight(0.5)|abundance(60)|difficulty(4)|spd_rtng(50) | shoot_speed(35) | thrust_damage(80,pierce)|max_ammo(99)|weapon_length(115)|accuracy(98),imodbits_none, [(ti_on_weapon_attack, [(play_sound,"snd_throw_lightsaber"),(position_move_x, pos1,0),(position_move_y, pos1,0)])], force_fac],
#force_throw_lightsaber_pike (merch + high ammo since they are not used for troops) - switched to use itcf_throw_stone instead of itcf_throw_javelin since I switched the ready_javelin and release_javelin animations
["force_throw_lightsaber_green_pike", "Throwing Lightsaber Pike", [("lightsaber_green_pike",0),("lightsaber_pike_off", ixmesh_carry)], itp_type_thrown |itp_merchandise|itp_primary|itp_bonus_against_shield|itp_wooden_attack ,itcf_throw_stone|itcf_carry_spear, 1040 , weight(2)|abundance(40)|difficulty(4)|spd_rtng(50) | shoot_speed(35) | thrust_damage(80 ,  pierce)|max_ammo(99)|weapon_length(150),imodbits_none, [(ti_on_weapon_attack, [(play_sound,"snd_throw_lightsaber"),(position_move_x, pos1,0),(position_move_y, pos1,0)])], force_fac],
["force_throw_lightsaber_blue_pike", "Throwing Lightsaber Pike", [("lightsaber_blue_pike",0),("lightsaber_pike_off", ixmesh_carry)], itp_type_thrown |itp_merchandise|itp_primary|itp_bonus_against_shield|itp_wooden_attack ,itcf_throw_stone|itcf_carry_spear, 1040 , weight(2)|abundance(40)|difficulty(4)|spd_rtng(50) | shoot_speed(35) | thrust_damage(80 ,  pierce)|max_ammo(99)|weapon_length(150),imodbits_none, [(ti_on_weapon_attack, [(play_sound,"snd_throw_lightsaber"),(position_move_x, pos1,0),(position_move_y, pos1,0)])], force_fac],
["force_throw_lightsaber_orange_pike", "Throwing Lightsaber Pike", [("lightsaber_orange_pike",0),("lightsaber_pike_off", ixmesh_carry)], itp_type_thrown |itp_merchandise|itp_primary|itp_bonus_against_shield|itp_wooden_attack ,itcf_throw_stone|itcf_carry_spear, 1040 , weight(2)|abundance(10)|difficulty(4)|spd_rtng(50) | shoot_speed(35) | thrust_damage(80 ,  pierce)|max_ammo(99)|weapon_length(150),imodbits_none, [(ti_on_weapon_attack, [(play_sound,"snd_throw_lightsaber"),(position_move_x, pos1,0),(position_move_y, pos1,0)])], force_fac],
["force_throw_lightsaber_purple_pike", "Throwing Lightsaber Pike", [("lightsaber_purple_pike",0),("lightsaber_pike_off", ixmesh_carry)], itp_type_thrown |itp_merchandise|itp_primary|itp_bonus_against_shield|itp_wooden_attack ,itcf_throw_stone|itcf_carry_spear, 1040 , weight(2)|abundance(20)|difficulty(4)|spd_rtng(50) | shoot_speed(35) | thrust_damage(80 ,  pierce)|max_ammo(99)|weapon_length(150),imodbits_none, [(ti_on_weapon_attack, [(play_sound,"snd_throw_lightsaber"),(position_move_x, pos1,0),(position_move_y, pos1,0)])], force_fac],
["force_throw_lightsaber_yellow_pike", "Throwing Lightsaber Pike", [("lightsaber_yellow_pike",0),("lightsaber_pike_off", ixmesh_carry)], itp_type_thrown |itp_merchandise|itp_primary|itp_bonus_against_shield|itp_wooden_attack ,itcf_throw_stone|itcf_carry_spear, 1040 , weight(2)|abundance(10)|difficulty(4)|spd_rtng(50) | shoot_speed(35) | thrust_damage(80 ,  pierce)|max_ammo(99)|weapon_length(150),imodbits_none, [(ti_on_weapon_attack, [(play_sound,"snd_throw_lightsaber"),(position_move_x, pos1,0),(position_move_y, pos1,0)])], force_fac],
["force_throw_lightsaber_red_pike", "Throwing Lightsaber Pike", [("lightsaber_red_pike",0),("lightsaber_pike_off", ixmesh_carry)], itp_type_thrown |itp_merchandise|itp_primary|itp_bonus_against_shield|itp_wooden_attack ,itcf_throw_stone|itcf_carry_spear, 1040 , weight(2)|abundance(40)|difficulty(4)|spd_rtng(50) | shoot_speed(35) | thrust_damage(80 ,  pierce)|max_ammo(99)|weapon_length(150),imodbits_none, [(ti_on_weapon_attack, [(play_sound,"snd_throw_lightsaber"),(position_move_x, pos1,0),(position_move_y, pos1,0)])], force_fac],
["force_throw_lightsaber_red_double", "Throwing Double-Bladed Lightsaber", [("lightsaber_red_double",0),("lightsaber_red_doubleoff", ixmesh_carry)], itp_type_thrown |itp_merchandise|itp_primary|itp_bonus_against_shield ,itcf_throw_stone|itcf_carry_dagger_front_left, 1195 , weight(0.8)|abundance(40)|difficulty(4)|spd_rtng(50) | shoot_speed(35) | thrust_damage(80 ,  pierce)|max_ammo(99)|weapon_length(170),imodbits_none, [(ti_on_weapon_attack, [(play_sound,"snd_throw_lightsaber"),(position_move_x, pos1,0),(position_move_y, pos1,0)])], force_fac],
#other throwing
["twilek_dagger_throwing", "Twilek Throwing Daggers", [("twilek_dagger",0)], itp_type_thrown |itp_merchandise|itp_primary ,itcf_throw_knife, 200 , weight(1.5)|difficulty(0)|spd_rtng(110) | shoot_speed(50) | thrust_damage(24, pierce)|max_ammo(30)|weapon_length(20),imodbits_thrown ],
["discblade", "Discblade", [("tyr_discblade",0)], itp_type_thrown |itp_merchandise|itp_primary ,itcf_throw_knife, 500 , weight(3.5)|difficulty(0)|spd_rtng(110) | shoot_speed(50) | thrust_damage(35, cut)|max_ammo(25)|weapon_length(20),imodbits_thrown ],

# thermal_detonator1 start -------------------------------------------------------------------------------------------------------
#["thermal_detonator1", "Prototype Thermal Detonator", [("thermal_detonator1",0)], itp_type_thrown |itp_merchandise|itp_primary|itp_bonus_against_shield, itcf_carry_pistol_front_left|itcf_shoot_crossbow, 1200 , weight(3.0)|abundance(60)|difficulty(0)|spd_rtng(90) | shoot_speed(50) | thrust_damage(100,pierce)|max_ammo(1)|accuracy(95),imodbits_none,
["thermal_detonator1", "Thermal Detonator", [("thermal_detonator1",0)], itp_type_thrown |itp_unique|itp_primary|itp_bonus_against_shield, itcf_carry_pistol_front_left|itcf_throw_stone, 2000 , weight(3.0)|abundance(60)|difficulty(0)|spd_rtng(90) | shoot_speed(30) | thrust_damage(100,pierce)|max_ammo(5)|accuracy(95),imodbits_none,
  [(ti_on_weapon_attack, [(play_sound,"snd_throw_javelin"),
#Highlander begin--------------------------------------
  (store_current_scene,":scene"),
  (try_begin),
	(neg|is_between,":scene","scn_ship_hangar_imp","scn_space_battle"), #land battle  
	#@->(neg|is_between,":scene","scn_ship_hangar_closed_1a","scn_space_battle"), #land battle
	(call_script,"script_emit_projectile",pos1,30,0,0,1,300,700,600,"psys_projectile_fly_smoke",4,0,-1,1),
  (else_try),
	#ship battle
	(call_script,"script_emit_projectile",pos1,30,0,0,1,300,700,600,"psys_projectile_fly_smoke",4,0,-1,0),
  (try_end),
#Highlander end--------------------------------------

])]],
# thermal_detonator1 end -------------------------------------------------------------------------------------------------------

# thermal_detonator2 start -------------------------------------------------------------------------------------------------------
["thermal_detonator2", "Thermal Detonator", [("thermal_detonator2",0)], itp_type_thrown |itp_unique|itp_primary|itp_bonus_against_shield, itcf_carry_pistol_front_left|itcf_throw_stone, 2000 , weight(3.0)|abundance(60)|difficulty(0)|spd_rtng(90) | shoot_speed(30) | thrust_damage(100,pierce)|max_ammo(5)|accuracy(95),imodbits_none,
  [(ti_on_weapon_attack, [(play_sound,"snd_throw_javelin"),
#Highlander begin--------------------------------------
  (store_current_scene,":scene"),
  (try_begin),
	(neg|is_between,":scene","scn_ship_hangar_imp","scn_space_battle"), #land battle  
	#@->(neg|is_between,":scene","scn_ship_hangar_closed_1a","scn_space_battle"), #land battle
	(call_script,"script_emit_projectile",pos1,30,0,0,1,300,700,600,"psys_projectile_fly_smoke",4,0,-1,1),
  (else_try),
	#ship battle
	(call_script,"script_emit_projectile",pos1,30,0,0,1,300,700,600,"psys_projectile_fly_smoke",4,0,-1,0),
  (try_end),
#Highlander end--------------------------------------

])]],
# thermal_detonator2 end -------------------------------------------------------------------------------------------------------

# thermal_detonator3 start -------------------------------------------------------------------------------------------------------
["thermal_detonator3", "Thermal Detonator", [("thermal_detonator3",0)], itp_type_thrown |itp_unique|itp_primary|itp_bonus_against_shield, itcf_carry_pistol_front_left|itcf_throw_stone, 2000 , weight(3.0)|abundance(60)|difficulty(0)|spd_rtng(90) | shoot_speed(30) | thrust_damage(100,pierce)|max_ammo(5)|accuracy(95),imodbits_none,
  [(ti_on_weapon_attack, [(play_sound,"snd_throw_javelin"),
#Highlander begin--------------------------------------
  (store_current_scene,":scene"),
  (try_begin),
	(neg|is_between,":scene","scn_ship_hangar_imp","scn_space_battle"), #land battle  
	#@->(neg|is_between,":scene","scn_ship_hangar_closed_1a","scn_space_battle"), #land battle
	(call_script,"script_emit_projectile",pos1,30,0,0,1,300,700,600,"psys_projectile_fly_smoke",4,0,-1,1),
  (else_try),
	#ship battle
	(call_script,"script_emit_projectile",pos1,30,0,0,1,300,700,600,"psys_projectile_fly_smoke",4,0,-1,0),
  (try_end),
#Highlander end--------------------------------------

])]],
# thermal_detonator3 end -------------------------------------------------------------------------------------------------------
 
# shields? durasteel_shield = dragon_shield mesh? personal deflector shields ? power shield?  semi-transparent?
["shields_begin","<dummy>", [("_",0)], 0,0,0,0,imodbits_none],
#["energy_shield_small","Small Energy Shield", [("shield_1_yellow",0)], itp_merchandise|itp_type_shield, 0, 300 , weight(0.1)|abundance(100)|hit_points(400)|body_armor(10)|spd_rtng(105)|weapon_length(45),imodbits_none ],
#["energy_shield_medium","Medium Energy Shield", [("shield_2_yellow",0)], itp_merchandise|itp_type_shield, 0, 500 , weight(0.1)|abundance(100)|hit_points(550)|body_armor(20)|spd_rtng(100)|weapon_length(60),imodbits_none ],
#["energy_shield_large","Large Energy Shield", [("shield_3_yellow",0)], itp_merchandise|itp_type_shield, 0, 700 , weight(0.1)|abundance(100)|hit_points(700)|body_armor(30)|spd_rtng(95)|weapon_length(80),imodbits_none ],
["energy_shield_red_small","Small Energy Shield", [("energy_shield_red_small",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, 0, 200 , weight(0.1)|abundance(60)|hit_points(200)|body_armor(10)|spd_rtng(105)|weapon_length(40),imodbits_none ],
["energy_shield_blue_small","Small Energy Shield", [("energy_shield_blue_small",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, 0, 200 , weight(0.1)|abundance(60)|hit_points(200)|body_armor(10)|spd_rtng(105)|weapon_length(40),imodbits_none ],
["energy_shield_green_small","Small Energy Shield", [("energy_shield_green_small",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, 0, 200 , weight(0.1)|abundance(60)|hit_points(200)|body_armor(10)|spd_rtng(105)|weapon_length(40),imodbits_none ],
["energy_shield_yellow_small","Small Energy Shield", [("energy_shield_yellow_small",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, 0, 200 , weight(0.1)|abundance(60)|hit_points(200)|body_armor(10)|spd_rtng(105)|weapon_length(40),imodbits_none ],
["energy_shield_red_medium","Medium Energy Shield", [("energy_shield_red_medium",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, 0, 400 , weight(0.1)|abundance(60)|hit_points(400)|body_armor(20)|spd_rtng(100)|weapon_length(60),imodbits_none ],
["energy_shield_blue_medium","Medium Energy Shield", [("energy_shield_blue_medium",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, 0, 400 , weight(0.1)|abundance(60)|hit_points(400)|body_armor(20)|spd_rtng(100)|weapon_length(60),imodbits_none ],
["energy_shield_green_medium","Medium Energy Shield", [("energy_shield_green_medium",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, 0, 400 , weight(0.1)|abundance(60)|hit_points(400)|body_armor(20)|spd_rtng(100)|weapon_length(60),imodbits_none ],
["energy_shield_yellow_medium","Medium Energy Shield", [("energy_shield_yellow_medium",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, 0, 400 , weight(0.1)|abundance(60)|hit_points(400)|body_armor(20)|spd_rtng(100)|weapon_length(60),imodbits_none ],
["energy_shield_red_large","Large Energy Shield", [("energy_shield_red_large",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, 0, 600 , weight(0.1)|abundance(60)|hit_points(600)|body_armor(30)|spd_rtng(95)|weapon_length(80),imodbits_none ],
["energy_shield_blue_large","Large Energy Shield", [("energy_shield_blue_large",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, 0, 600 , weight(0.1)|abundance(60)|hit_points(600)|body_armor(30)|spd_rtng(95)|weapon_length(80),imodbits_none ],
["energy_shield_green_large","Large Energy Shield", [("energy_shield_green_large",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, 0, 600 , weight(0.1)|abundance(60)|hit_points(600)|body_armor(30)|spd_rtng(95)|weapon_length(80),imodbits_none ],
["energy_shield_yellow_large","Large Energy Shield", [("energy_shield_yellow_large",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, 0, 600 , weight(0.1)|abundance(60)|hit_points(600)|body_armor(30)|spd_rtng(95)|weapon_length(80),imodbits_none ],
["energy_shield_oval","Oval Energy Shield", [("energy_shield_large_v2",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, 0, 800 , weight(0.1)|abundance(60)|hit_points(700)|body_armor(35)|spd_rtng(90)|weapon_length(85),imodbits_none ],
["energy_shield_circle","Circular Energy Shield", [("_",0)], itp_merchandise|itp_type_shield|itp_wooden_parry, 0, 1200, weight(0.1)|abundance(60)|hit_points(800)|body_armor(40)|spd_rtng(85)|weapon_length(90),imodbits_none ],
["durasteel_shield_small", "Small Durasteel Shield", [("shield_dragon",0)], itp_merchandise|itp_type_shield, itcf_carry_round_shield,  250 , weight(4)|abundance(60)|hit_points(300)|body_armor(10)|spd_rtng(75)|weapon_length(40),imodbits_shield ],
#TEST durasteel shield ?
["durasteel_shield_small_2", "Small Durasteel Shield", [("shield_round_e",0)], itp_merchandise|itp_type_shield, itcf_carry_round_shield,  250 , weight(4)|abundance(60)|hit_points(300)|body_armor(10)|spd_rtng(75)|weapon_length(40),imodbits_shield ],
["durasteel_shield_large", "Large Durasteel Shield", [("durasteel_shield",0)], itp_merchandise|itp_type_shield, itcf_carry_kite_shield,  400 , weight(8)|abundance(60)|hit_points(500)|body_armor(25)|spd_rtng(60)|weapon_length(80),imodbits_shield ],
["wookiee_shield_small", "Small Wookiee Shield", [("shield_round_f",0)], itp_merchandise|itp_type_shield, itcf_carry_round_shield,  100 , weight(2)|abundance(80)|hit_points(300)|body_armor(5)|spd_rtng(100)|weapon_length(50),imodbits_shield ],
["wookiee_shield_large",  "Large Wookiee Shield", [("shield_kite_m",0)], itp_merchandise|itp_type_shield, itcf_carry_kite_shield,  150 , weight(3.5)|abundance(80)|hit_points(400)|body_armor(10)|spd_rtng(80)|weapon_length(85),imodbits_shield ],
["shield_bash_begin","<dummy>", [("_",0)], 0,0,0,0,imodbits_none],
["westar_shield", "Westar-34 Shield", [("westar_shield",0)], itp_merchandise|itp_type_shield, 0,  250 , weight(1.5)|abundance(80)|hit_points(150)|body_armor(5)|spd_rtng(100)|weapon_length(15),imodbits_none ],
["ryyk_kerarthorr_shield", "Ryyk Kerarthorr Shield", [("ryyk_kerarthorr_shield",0)], itp_merchandise|itp_type_shield, 0,  200 , weight(2.5)|abundance(60)|hit_points(150)|body_armor(10)|spd_rtng(100)|weapon_length(20),imodbits_none ],
["ryyk_blade_shield", "Ryyk Blade Shield", [("ryyk_blade_shield",0)], itp_merchandise|itp_type_shield, 0,  200 , weight(3)|abundance(80)|hit_points(200)|body_armor(15)|spd_rtng(80)|weapon_length(30),imodbits_none ],

#added itp_unique to the force shields so they can't be dropped after battle
["lightsaber_block_blue", "Lightsaber Shield", [("lightsaber_blue_block",0)], itp_merchandise|itp_type_shield|itp_wooden_parry,0,  800 , weight(0.5)|abundance(80)|hit_points(800)|body_armor(35)|spd_rtng(105)|weapon_length(75),imodbits_none,[], force_fac ],
["lightsaber_block_green", "Lightsaber Shield", [("lightsaber_green_block",0)], itp_merchandise|itp_type_shield|itp_wooden_parry,0,  800 , weight(0.5)|abundance(80)|hit_points(800)|body_armor(35)|spd_rtng(105)|weapon_length(75),imodbits_none,[], force_fac ],
["lightsaber_block_orange", "Lightsaber Shield", [("lightsaber_orange_block",0)], itp_merchandise|itp_type_shield|itp_wooden_parry,0,  800 , weight(0.5)|abundance(40)|hit_points(800)|body_armor(35)|spd_rtng(105)|weapon_length(75),imodbits_none,[], force_fac ],
["lightsaber_block_purple", "Lightsaber Shield", [("lightsaber_purple_block",0)], itp_merchandise|itp_type_shield|itp_wooden_parry,0,  800 , weight(0.5)|abundance(60)|hit_points(800)|body_armor(35)|spd_rtng(105)|weapon_length(75),imodbits_none,[], force_fac ],
["lightsaber_block_red", "Lightsaber Shield", [("lightsaber_red_block",0)], itp_merchandise|itp_type_shield|itp_wooden_parry,0,  800 , weight(0.5)|abundance(80)|hit_points(800)|body_armor(35)|spd_rtng(105)|weapon_length(75),imodbits_none,[], force_fac ],
["lightsaber_block_yellow", "Lightsaber Shield", [("lightsaber_yellow_block",0)], itp_merchandise|itp_type_shield|itp_wooden_parry,0,  800 , weight(0.5)|abundance(40)|hit_points(800)|body_armor(35)|spd_rtng(105)|weapon_length(75),imodbits_none,[], force_fac ],

["shields_end","<dummy>", [("_",0)], 0,0,0,0,imodbits_none],
["force_block", "Force Block", [("_",0),("force_block_inv",ixmesh_inventory)], itp_unique|itp_type_shield|itp_wooden_parry,0,  600, weight(0.1)|abundance(100)|hit_points(600)|body_armor(40)|spd_rtng(110)|weapon_length(60),imodbits_none,[], force_fac ],
["force_shield", "Force Shield", [("_",0),("force_shield_inv",ixmesh_inventory)], itp_unique|itp_type_shield|itp_wooden_parry,0, 800, weight(0.1)|abundance(100)|hit_points(800)|body_armor(50)|spd_rtng(110)|weapon_length(85),imodbits_none,[], force_fac ],
["force_protect","Force Protect", [("_",0),("force_protect_inv",ixmesh_inventory)], itp_unique|itp_type_shield|itp_wooden_parry, 0, 1200, weight(0.1)|abundance(100)|hit_points(1000)|body_armor(60)|spd_rtng(110)|weapon_length(100),imodbits_none,[], force_fac ],
["hero_shield", "Transparent Hero Shield", [("_",0),("force_shield_inv",ixmesh_inventory)], itp_unique|itp_type_shield,0, 800, weight(0.1)|abundance(100)|hit_points(600)|body_armor(40)|spd_rtng(100)|weapon_length(75),imodbits_none ],
["shield_bash_end","<dummy>", [("_",0)], 0,0,0,0,imodbits_none],
 
 # training/practice
#["practice_force_block", "Force Block", [("force_block",0),("force_block_inv",ixmesh_inventory)], itp_type_shield,0,  1000 , weight(0.1)|abundance(100)|hit_points(1000)|body_armor(40)|spd_rtng(120)|weapon_length(60),imodbits_none ],
["practice_energy_shield","Practice Energy Shield", [("energy_shield_yellow_medium",0)], itp_type_shield|itp_wooden_parry, 0, 300 , weight(0.1)|abundance(100)|hit_points(400)|body_armor(10)|spd_rtng(105)|weapon_length(45),imodbits_none ],
["tutorial_energy_shield","Tutorial Energy Shield", [("energy_shield_yellow_medium",0)], itp_type_shield|itp_wooden_parry, 0, 500 , weight(0.1)|abundance(100)|hit_points(1000)|body_armor(20)|spd_rtng(100)|weapon_length(60),imodbits_none ],
["force_throw_lightsaber_t", "Force Throw Lightsaber", [("lightsaber_green",0)], itp_type_thrown|itp_primary|itp_secondary|itp_bonus_against_shield,itcf_throw_stone,1200, weight(2.25)|difficulty(0)|spd_rtng(100) | shoot_speed(150) | thrust_damage(60,pierce)|max_ammo(12)|weapon_length(115)|accuracy(94),imodbits_none,
 [(ti_on_weapon_attack, [(play_sound,"snd_throw_lightsaber"),(position_move_x, pos1,0),(position_move_y, pos1,0)])],force_fac],
["force_throw_lightsaber_tl", "Force Throw Lightsaber", [("lightsaber_green",0)], itp_type_thrown|itp_primary|itp_secondary|itp_bonus_against_shield,itcf_throw_stone,1200, weight(2.25)|difficulty(0)|spd_rtng(100) | shoot_speed(150) | thrust_damage(60,pierce)|max_ammo(150)|weapon_length(115)|accuracy(94),imodbits_none,
 [(ti_on_weapon_attack, [(play_sound,"snd_throw_lightsaber"),(position_move_x, pos1,0),(position_move_y, pos1,0)])],force_fac], 

 # note - you must use itcf_throw_stone or the lightsaber will stay visible on the ground...
#["force_throw_lightsaber_spear", "Force Throw Lightsaber", [("lightsaber_red",0)], itp_type_thrown |itp_merchandise|itp_primary|itp_bonus_against_shield,itcf_throw_javelin,500, weight(2.25)|difficulty(0)|spd_rtng(90) | shoot_speed(30) | thrust_damage(50,pierce)|max_ammo(12)|weapon_length(115),imodbits_none ],
#["force_throw_lightsaber_sidearm", "Force Throw Lightsaber", [("lightsaber_blue",0)], itp_type_thrown |itp_merchandise|itp_primary|itp_bonus_against_shield,itcf_throw_stone,500, weight(2.25)|difficulty(0)|spd_rtng(90) | shoot_speed(30) | thrust_damage(50,pierce)|max_ammo(12)|weapon_length(115),imodbits_none ],
#["force_throw_lightsaber_overhand", "Force Throw Lightsaber", [("lightsaber_green",0)], itp_type_thrown |itp_merchandise|itp_primary|itp_bonus_against_shield,itcf_throw_axe,500, weight(2.25)|difficulty(0)|spd_rtng(90) | shoot_speed(30) | thrust_damage(50,cut)|max_ammo(12)|weapon_length(115),imodbits_none ],

# weapons - ammo
#force power ammo
["force_lightning_ammo","Force Lightning", [("_",0),("lightning",ixmesh_flying_ammo),("lightning",ixmesh_inventory)], itp_type_arrows|itp_unique|itp_bonus_against_shield, 0, 200,weight(0.1)|abundance(80)|weapon_length(95)|thrust_damage(1,blunt)|max_ammo(30),imodbits_none],
["force_push_ammo","Force Push", [("_",0),("f_push",ixmesh_flying_ammo),("f_push",ixmesh_inventory)], itp_type_arrows|itp_unique|itp_bonus_against_shield, 0, 200,weight(0.1)|abundance(80)|weapon_length(95)|thrust_damage(1,blunt)|max_ammo(30),imodbits_none],

#TEST
# ["laser_bolts_green","Plasma Gas Cartridges", [("_",0),("laser_bolt_green",ixmesh_flying_ammo),("laser_bolt_green_cartridges",ixmesh_inventory)], itp_type_bullets|itp_merchandise|itp_bonus_against_shield, 0, 100,weight(0.1)|abundance(100)|weapon_length(60)|thrust_damage(1,pierce)|max_ammo(100),imodbits_ammo],
# ["laser_bolts_red","Plasma Gas Cartridges", [("_",0),("laser_bolt_red",ixmesh_flying_ammo),("laser_bolt_red_cartridges",ixmesh_inventory)], itp_type_bullets|itp_merchandise|itp_bonus_against_shield, 0, 100,weight(0.1)|abundance(100)|weapon_length(60)|thrust_damage(1,pierce)|max_ammo(100),imodbits_ammo],
# ["laser_bolts_orange","Plasma Gas Cartridges", [("_",0),("laser_bolt_orange",ixmesh_flying_ammo),("laser_bolt_orange_cartridges",ixmesh_inventory)], itp_type_bullets|itp_merchandise|itp_bonus_against_shield, 0, 100,weight(0.1)|abundance(80)|weapon_length(60)|thrust_damage(1,pierce)|max_ammo(100),imodbits_ammo],
# ["laser_bolts_yellow","Plasma Gas Cartridges", [("_",0),("laser_bolt_yellow",ixmesh_flying_ammo),("laser_bolt_yellow_cartridges",ixmesh_inventory)], itp_type_bullets|itp_merchandise|itp_bonus_against_shield, 0, 100,weight(0.1)|abundance(80)|weapon_length(60)|thrust_damage(1,pierce)|max_ammo(100),imodbits_ammo],
# ["laser_bolts_blue","Plasma Gas Cartridges", [("_",0),("laser_bolt_blue",ixmesh_flying_ammo),("laser_bolt_blue_cartridges",ixmesh_inventory)], itp_type_bullets|itp_merchandise|itp_bonus_against_shield, 0, 100,weight(0.1)|abundance(60)|weapon_length(60)|thrust_damage(1,pierce)|max_ammo(100),imodbits_ammo],
# ["stun_beam","Stun Beam Cartridges", [("_",0),("stun_beam",ixmesh_flying_ammo),("stun_beam_cartridges",ixmesh_inventory)], itp_type_bullets|itp_merchandise|itp_bonus_against_shield, 0, 100,weight(0.1)|abundance(100)|weapon_length(80)|thrust_damage(1,blunt)|max_ammo(100),imodbits_ammo],
# ["ion_beam","Ion Beam Cartridges", [("_",0),("ion_beam",ixmesh_flying_ammo),("ion_beam_cartridges",ixmesh_inventory)], itp_type_bullets|itp_merchandise|itp_bonus_against_shield, 0, 50,weight(0.1)|abundance(60)|weapon_length(60)|thrust_damage(1,blunt)|max_ammo(80),imodbits_ammo],
# ["sonic_beam","Sonic Beam Cartridges", [("_",0),("ion_beam",ixmesh_flying_ammo),("ion_beam_cartridges",ixmesh_inventory)], itp_type_bullets|itp_merchandise|itp_bonus_against_shield, 0, 50,weight(0.1)|abundance(40)|weapon_length(60)|thrust_damage(1,blunt)|max_ammo(80),imodbits_ammo],
# ["ammo_belt","Ammo Belt", [("_",0),("laser_bolt_yellow",ixmesh_flying_ammo),("ammo_belt",ixmesh_carry),("ammo_belt",ixmesh_inventory)], itp_type_bullets|itp_merchandise|itp_bonus_against_shield, itcf_carry_axe_back, 150,weight(1.5)|abundance(50)|weapon_length(60)|thrust_damage(1,pierce)|max_ammo(150),imodbits_ammo],

# pistol ammo = bullets, main mesh has to be 'transparent' so it doesn't stay visble after hiting somebody
["laser_bolts_green_pistol","Plasma Gas Cartridges", [("_",0),("swy_blasterbolt_green_alpha",ixmesh_flying_ammo),("laser_bolt_green_cartridges_pistol",ixmesh_inventory)], itp_type_bullets|itp_merchandise|itp_bonus_against_shield, 0, 100,weight(0.0)|abundance(100)|weapon_length(60)|thrust_damage(1,pierce)|max_ammo(100),imodbits_ammo],
["laser_bolts_red_pistol","Plasma Gas Cartridges", [("_",0),("swy_blasterbolt_red_alpha",ixmesh_flying_ammo),("laser_bolt_red_cartridges_pistol",ixmesh_inventory)], itp_type_bullets|itp_merchandise|itp_bonus_against_shield, 0, 100,weight(0.0)|abundance(100)|weapon_length(60)|thrust_damage(1,pierce)|max_ammo(100),imodbits_ammo],
["laser_bolts_orange_pistol","Plasma Gas Cartridges", [("_",0),("swy_blasterbolt_orange_alpha",ixmesh_flying_ammo),("laser_bolt_orange_cartridges_pistol",ixmesh_inventory)], itp_type_bullets|itp_merchandise|itp_bonus_against_shield, 0, 100,weight(0.0)|abundance(80)|weapon_length(60)|thrust_damage(1,pierce)|max_ammo(100),imodbits_ammo],
["laser_bolts_yellow_pistol","Plasma Gas Cartridges", [("_",0),("swy_blasterbolt_yellow_alpha",ixmesh_flying_ammo),("laser_bolt_yellow_cartridges_pistol",ixmesh_inventory)], itp_type_bullets|itp_merchandise|itp_bonus_against_shield, 0, 100,weight(0.0)|abundance(80)|weapon_length(60)|thrust_damage(1,pierce)|max_ammo(100),imodbits_ammo],
["laser_bolts_blue_pistol","Plasma Gas Cartridges", [("_",0),("swy_blasterbolt_blue_alpha",ixmesh_flying_ammo),("laser_bolt_blue_cartridges_pistol",ixmesh_inventory)], itp_type_bullets|itp_merchandise|itp_bonus_against_shield, 0, 100,weight(0.0)|abundance(60)|weapon_length(60)|thrust_damage(1,pierce)|max_ammo(100),imodbits_ammo],
["stun_beam_pistol","Stun Beam Cartridges", [("_",0),("stun_beam",ixmesh_flying_ammo),("stun_beam_cartridges_pistol",ixmesh_inventory)], itp_type_bullets|itp_merchandise|itp_bonus_against_shield, 0, 100,weight(0.0)|abundance(100)|weapon_length(80)|thrust_damage(1,blunt)|max_ammo(100),imodbits_ammo],
["ion_beam_pistol","Ion Beam Cartridges", [("_",0),("ion_beam",ixmesh_flying_ammo),("ion_beam_cartridges_pistol",ixmesh_inventory)], itp_type_bullets|itp_merchandise|itp_bonus_against_shield, 0, 50,weight(0.0)|abundance(60)|weapon_length(60)|thrust_damage(1,blunt)|max_ammo(80),imodbits_ammo],
["sonic_beam_pistol","Sonic Beam Cartridges", [("_",0),("sonic_ammo",ixmesh_flying_ammo),("ion_beam_cartridges_pistol",ixmesh_inventory)], itp_type_bullets|itp_merchandise|itp_bonus_against_shield, 0, 50,weight(0.0)|abundance(40)|weapon_length(60)|thrust_damage(1,blunt)|max_ammo(80),imodbits_ammo],
["ammo_belt_pistol","Ammo Belt", [("_",0),("swy_blasterbolt_yellow_alpha",ixmesh_flying_ammo),("ammo_belt",ixmesh_carry),("ammo_belt",ixmesh_inventory)], itp_type_bullets|itp_merchandise|itp_bonus_against_shield, itcf_carry_axe_back, 150,weight(0.0)|abundance(50)|weapon_length(60)|thrust_damage(1,pierce)|max_ammo(150),imodbits_none],
#@>>> Added by Swyter
["disruptor_ammo","Disruptor Ammo for Pistols", [("_",0),("laser_disruptor",ixmesh_flying_ammo),("laser_bolt_blue_cartridges",ixmesh_inventory)], itp_type_bullets|itp_merchandise|itp_bonus_against_shield, 0, 4960,weight(0.09)|abundance(60)|weapon_length(60)|thrust_damage(4,blunt)|max_ammo(160),imodbits_ammo],


# rifle ammo = bolts, main mesh has to be 'transparent' so it doesn't stay visble after hiting somebody
["laser_bolts_green_rifle","Plasma Gas Cartridges", [("_",0),("swy_blasterbolt_green_alpha",ixmesh_flying_ammo),("laser_bolt_green_cartridges",ixmesh_inventory)], itp_type_bolts|itp_merchandise|itp_bonus_against_shield, 0, 100,weight(0.0)|abundance(100)|weapon_length(60)|thrust_damage(1,pierce)|max_ammo(125),imodbits_ammo],
["laser_bolts_red_rifle","Plasma Gas Cartridges", [("_",0),("swy_blasterbolt_red_alpha",ixmesh_flying_ammo),("laser_bolt_red_cartridges",ixmesh_inventory)], itp_type_bolts|itp_merchandise|itp_bonus_against_shield, 0, 100,weight(0.0)|abundance(100)|weapon_length(60)|thrust_damage(1,pierce)|max_ammo(125),imodbits_ammo],
["laser_bolts_orange_rifle","Plasma Gas Cartridges", [("_",0),("swy_blasterbolt_orange_alpha",ixmesh_flying_ammo),("laser_bolt_orange_cartridges",ixmesh_inventory)], itp_type_bolts|itp_merchandise|itp_bonus_against_shield, 0, 100,weight(0.0)|abundance(80)|weapon_length(60)|thrust_damage(1,pierce)|max_ammo(125),imodbits_ammo],
["laser_bolts_yellow_rifle","Plasma Gas Cartridges", [("_",0),("swy_blasterbolt_yellow_alpha",ixmesh_flying_ammo),("laser_bolt_yellow_cartridges",ixmesh_inventory)], itp_type_bolts|itp_merchandise|itp_bonus_against_shield, 0, 100,weight(0.0)|abundance(80)|weapon_length(60)|thrust_damage(1,pierce)|max_ammo(125),imodbits_ammo],
["laser_bolts_blue_rifle","Plasma Gas Cartridges", [("_",0),("swy_blasterbolt_blue_alpha",ixmesh_flying_ammo),("laser_bolt_blue_cartridges",ixmesh_inventory)], itp_type_bolts|itp_merchandise|itp_bonus_against_shield, 0, 100,weight(0.0)|abundance(60)|weapon_length(60)|thrust_damage(1,pierce)|max_ammo(125),imodbits_ammo],
["stun_beam_rifle","Stun Beam Cartridges", [("_",0),("stun_beam",ixmesh_flying_ammo),("stun_beam_cartridges",ixmesh_inventory)], itp_type_bolts|itp_merchandise|itp_bonus_against_shield, 0, 100,weight(0.0)|abundance(100)|weapon_length(80)|thrust_damage(1,blunt)|max_ammo(125),imodbits_ammo],
["ion_beam_rifle","Ion Beam Cartridges", [("_",0),("ion_beam",ixmesh_flying_ammo),("ion_beam_cartridges",ixmesh_inventory)], itp_type_bolts|itp_merchandise|itp_bonus_against_shield, 0, 50,weight(0.0)|abundance(60)|weapon_length(60)|thrust_damage(1,blunt)|max_ammo(100),imodbits_ammo],
["sonic_beam_rifle","Sonic Beam Cartridges", [("_",0),("sonic_ammo",ixmesh_flying_ammo),("ion_beam_cartridges",ixmesh_inventory)], itp_type_bolts|itp_merchandise|itp_bonus_against_shield, 0, 50,weight(0.0)|abundance(40)|weapon_length(60)|thrust_damage(1,blunt)|max_ammo(100),imodbits_ammo],
["ammo_belt_rifle","Ammo Belt", [("_",0),("swy_blasterbolt_yellow_alpha",ixmesh_flying_ammo),("ammo_belt",ixmesh_carry),("ammo_belt",ixmesh_inventory)], itp_type_bolts|itp_merchandise|itp_bonus_against_shield, itcf_carry_axe_back, 150,weight(0.0)|abundance(50)|weapon_length(60)|thrust_damage(1,pierce)|max_ammo(175),imodbits_none],
#@>>> Added by Swyter
["disruptor_ammo_rifle","Disruptor Ammo for Rifles", [("_",0),("laser_disruptor",ixmesh_flying_ammo),("laser_bolt_blue_cartridges",ixmesh_inventory)], itp_type_bolts|itp_merchandise|itp_bonus_against_shield, 0, 4960,weight(0.09)|abundance(60)|weapon_length(60)|thrust_damage(4,blunt)|max_ammo(160),imodbits_ammo],

# practice/training
["laser_bolts_training_pistol","Laser Bolts", [("_",0),("swy_blasterbolt_yellow_alpha",ixmesh_flying_ammo),("laser_bolt_yellow_cartridges",ixmesh_inventory)], itp_unique|itp_type_bullets|itp_bonus_against_shield, 0, 500,weight(0.0)|abundance(100)|weapon_length(5)|thrust_damage(1,pierce)|max_ammo(12),imodbits_none],
["laser_bolts_training_rifle","Laser Bolts", [("_",0),("swy_blasterbolt_yellow_alpha",ixmesh_flying_ammo),("laser_bolt_yellow_cartridges",ixmesh_inventory)], itp_unique|itp_type_bolts|itp_bonus_against_shield, 0, 500,weight(0.0)|abundance(100)|weapon_length(5)|thrust_damage(1,pierce)|max_ammo(12),imodbits_none],

#force powers (ranged weapon)
#["force_power_ls_1","Initiate Force Powers", [("_",0),("force_powers_ls",ixmesh_inventory)], itp_type_bow|itp_unique|itp_primary,itcf_shoot_pistol, 500 , weight(0.1)|abundance(80)|difficulty(2)|spd_rtng(80) | shoot_speed(80) | thrust_damage(30, blunt)|max_ammo(50)|accuracy(85),imodbits_none,
["force_power_ls_1","Initiate Force Powers", [("_",0),("force_powers_ls",ixmesh_inventory)], itp_type_bow|itp_unique|itp_primary,itcf_shoot_bow, 500 , weight(0.1)|abundance(80)|difficulty(2)|spd_rtng(80) | shoot_speed(80) | thrust_damage(30, blunt)|max_ammo(50)|accuracy(85),imodbits_none,
 [(ti_on_weapon_attack, [(play_sound,"snd_force_push"),(position_move_x, pos1,0),(position_move_y, pos1,0)])]],
["force_power_ls_2","Apprentice Force Powers", [("_",0),("force_powers_ls",ixmesh_inventory)], itp_type_bow|itp_unique|itp_primary,itcf_shoot_pistol, 1000 , weight(0.1)|abundance(70)|difficulty(4)|spd_rtng(100) | shoot_speed(100) | thrust_damage(40, blunt)|max_ammo(50)|accuracy(90),imodbits_none,
 [(ti_on_weapon_attack, [(play_sound,"snd_force_push"),(position_move_x, pos1,0),(position_move_y, pos1,0)])]],
["force_power_ls_3","Knight Force Powers", [("_",0),("force_powers_ls",ixmesh_inventory)], itp_type_bow|itp_unique|itp_primary,itcf_shoot_pistol, 1500 , weight(0.1)|abundance(60)|difficulty(5)|spd_rtng(120) | shoot_speed(120) | thrust_damage(50, blunt)|max_ammo(50)|accuracy(95),imodbits_none,
 [(ti_on_weapon_attack, [(play_sound,"snd_force_push"),(position_move_x, pos1,0),(position_move_y, pos1,0)])]],
["force_power_ls_4","Master Force Powers", [("_",0),("force_powers_ls",ixmesh_inventory)], itp_type_bow|itp_unique|itp_primary,itcf_shoot_pistol, 2000 , weight(0.1)|abundance(50)|difficulty(6)|spd_rtng(140) | shoot_speed(140) | thrust_damage(60, blunt)|max_ammo(50)|accuracy(100),imodbits_none,
 [(ti_on_weapon_attack, [(play_sound,"snd_force_push"),(position_move_x, pos1,0),(position_move_y, pos1,0)])]], 
["force_power_ds_1","Initiate Force Powers", [("_",0),("force_powers_ds",ixmesh_inventory)], itp_type_bow|itp_unique|itp_primary,itcf_shoot_pistol, 500 , weight(0.1)|abundance(80)|difficulty(2)|spd_rtng(80) | shoot_speed(80) | thrust_damage(30, pierce)|max_ammo(50)|accuracy(85),imodbits_none,
 [(ti_on_weapon_attack, [(play_sound,"snd_force_lightning"),(position_move_x, pos1,0),(position_move_y, pos1,0)])]],
["force_power_ds_2","Apprentice Force Powers", [("_",0),("force_powers_ds",ixmesh_inventory)], itp_type_bow|itp_unique|itp_primary,itcf_shoot_pistol, 1000 , weight(0.1)|abundance(70)|difficulty(4)|spd_rtng(100) | shoot_speed(100) | thrust_damage(40, pierce)|max_ammo(50)|accuracy(90),imodbits_none,
 [(ti_on_weapon_attack, [(play_sound,"snd_force_lightning"),(position_move_x, pos1,0),(position_move_y, pos1,0)])]],
["force_power_ds_3","Knight Force Powers", [("_",0),("force_powers_ds",ixmesh_inventory)], itp_type_bow|itp_unique|itp_primary,itcf_shoot_pistol, 1500 , weight(0.1)|abundance(60)|difficulty(5)|spd_rtng(120) | shoot_speed(120) | thrust_damage(50, pierce)|max_ammo(50)|accuracy(95),imodbits_none,
 [(ti_on_weapon_attack, [(play_sound,"snd_force_lightning"),(position_move_x, pos1,0),(position_move_y, pos1,0)])]],
["force_power_ds_4","Master Force Powers", [("_",0),("force_powers_ds",ixmesh_inventory)], itp_type_bow|itp_unique|itp_primary,itcf_shoot_pistol, 2000 , weight(0.1)|abundance(50)|difficulty(6)|spd_rtng(140) | shoot_speed(140) | thrust_damage(60, pierce)|max_ammo(50)|accuracy(100),imodbits_none,
 [(ti_on_weapon_attack, [(play_sound,"snd_force_lightning"),(position_move_x, pos1,0),(position_move_y, pos1,0)])]], 
#force powers (inventory items)
 ["force_jump","Force Jump", [("force_push_inv",0)], itp_unique|itp_type_goods, 0,3000,weight(0.1)|abundance(35),imodbits_none],  
 
## STAR WARS CONQUEST >
## R I F L E S   &   B L A S T E R S
## section improved by Swyter

# two handed blasters (ie. musket)  - added itp_two_handed_wpn so you cannot use a shield at the same time
# NOTE - use itcf_reload_mask instead of reload_pistol or reload_musket so it uses the crossbow reload noise

["ranged_weapons_begin","<dummy>", [("_",0)], 0,0,0,0,imodbits_none],

#removed merch flag since there are two a280's
["a280", "A-280", [("A280",0),("A280_inventory",ixmesh_inventory)], itp_type_crossbow|itp_two_handed|itp_primary|itp_bonus_against_shield,itcf_shoot_crossbow|itcf_carry_spear|itcf_reload_musket, 
	1300 , weight(6.7)|abundance(100)|difficulty(0)|spd_rtng(110) | shoot_speed(180) | thrust_damage(45 ,pierce)|max_ammo(30)|accuracy(93),imodbits_gun,
	[(ti_on_weapon_attack, [(play_sound,"snd_laser_fire"),(position_move_x, pos1,12),(position_move_y, pos1,15),]
	+#<muzzleflare system>#
	muzzleflare_system,
	#</muzzleflare system>#
	)]],
["a280_crouch", "A-280", [("A280",0),("A280_inventory",ixmesh_inventory)], itp_type_crossbow|itp_two_handed |itp_merchandise|itp_primary|itp_bonus_against_shield,itcf_shoot_musket|itcf_carry_spear|itcf_reload_musket, 
	1300 , weight(6.7)|abundance(100)|difficulty(0)|spd_rtng(110) | shoot_speed(180) | thrust_damage(45 ,pierce)|max_ammo(30)|accuracy(93),imodbits_gun,
	[(ti_on_weapon_attack, [(play_sound,"snd_laser_fire"),(position_move_x, pos1,12),(position_move_y, pos1,15)]
	+#<muzzleflare system>#
	muzzleflare_system,
	#</muzzleflare system>#
	)]],
["a280_stun", "Stun A-280", [("A280",0),("A280_inventory",ixmesh_inventory)], itp_type_crossbow|itp_two_handed |itp_primary|itp_bonus_against_shield,itcf_shoot_musket|itcf_carry_spear|itcf_reload_musket, 
	1300 , weight(6.7)|abundance(80)|difficulty(0)|spd_rtng(110) | shoot_speed(180) | thrust_damage(45 ,blunt)|max_ammo(30)|accuracy(93),imodbits_gun,
	[(ti_on_weapon_attack, [(play_sound,"snd_stunblaster"),(position_move_x, pos1,12),(position_move_y, pos1,15)]
	+#<muzzleflare system>#
	muzzleflare_system,
	#</muzzleflare system>#
	)]], 
#removed merch flag since there are two a295's
["a295", "A-295", [("A295",0),("A295_inventory",ixmesh_inventory)], itp_type_crossbow|itp_two_handed|itp_primary|itp_bonus_against_shield,itcf_shoot_crossbow|itcf_carry_spear|itcf_reload_musket, 
	1280 , weight(6.3)|abundance(100)|difficulty(0)|spd_rtng(120) | shoot_speed(180) | thrust_damage(48, pierce)|max_ammo(30)|accuracy(94),imodbits_gun,
	[(ti_on_weapon_attack, [(play_sound,"snd_laser_fire"),(position_move_x, pos1,12),(position_move_y, pos1,15)]
	+#<muzzleflare system>#
	muzzleflare_system,
	#</muzzleflare system>#
	)]],
["a295_crouch", "A-295", [("A295",0),("A295_inventory",ixmesh_inventory)], itp_type_crossbow|itp_two_handed |itp_merchandise|itp_primary|itp_bonus_against_shield,itcf_shoot_musket|itcf_carry_spear|itcf_reload_musket, 
	1280 , weight(6.3)|abundance(100)|difficulty(0)|spd_rtng(120) | shoot_speed(180) | thrust_damage(48, pierce)|max_ammo(30)|accuracy(94),imodbits_gun,
	[(ti_on_weapon_attack, [(play_sound,"snd_laser_fire"),(position_move_x, pos1,12),(position_move_y, pos1,15)]
	+#<muzzleflare system>#
	muzzleflare_system,
	#</muzzleflare system>#
	)]],
["a295_stun", "Stun A-295", [("A295",0),("A295_inventory",ixmesh_inventory)], itp_type_crossbow|itp_two_handed |itp_primary|itp_bonus_against_shield,itcf_shoot_musket|itcf_carry_spear|itcf_reload_musket,
	1280 , weight(6.3)|abundance(80)|difficulty(0)|spd_rtng(120) | shoot_speed(180) | thrust_damage(48 ,blunt)|max_ammo(30)|accuracy(94),imodbits_gun,
	[(ti_on_weapon_attack, [(play_sound,"snd_stunblaster"),(position_move_x, pos1,12),(position_move_y, pos1,15)]
	+#<muzzleflare system>#
	muzzleflare_system,
	#</muzzleflare system>#
	)]], 	
#["mandalorian_heavy_blaster", "Mandalorian Heavy Blaster", [("mandalorian_heavy_blaster",0),("mandalorian_heavy_blaster_inventory",ixmesh_inventory)], itp_type_crossbow|itp_two_handed |itp_merchandise|itp_primary|itp_bonus_against_shield,itcf_shoot_crossbow|itcf_carry_sword_back|itcf_reload_musket,
["mandalorian_heavy_blaster", "Mandalorian Heavy Blaster", [("mandalorian_heavy_blaster",0),("mandalorian_heavy_blaster_inventory",ixmesh_inventory)], itp_type_crossbow|itp_two_handed |itp_merchandise|itp_primary|itp_bonus_against_shield,itcf_shoot_crossbow|itcf_carry_spear|itcf_reload_musket,
	1300 , weight(5.2)|abundance(70)|difficulty(0)|spd_rtng(120) | shoot_speed(180) | thrust_damage(48 ,pierce)|max_ammo(30)|accuracy(94),imodbits_gun,
	[(ti_on_weapon_attack, [(play_sound,"snd_laser_fire"),(position_move_x, pos1,14),(position_move_y, pos1,18)]
	+#<muzzleflare system>#
	muzzleflare_system,
	#</muzzleflare system>#
	)]], 
["corellian_destroyer_blaster", "Corellian Destroyer Blaster", [("corellian_destroyer_blaster",0),("corellian_destroyer_blaster_inventory",ixmesh_inventory)], itp_type_crossbow|itp_two_handed |itp_merchandise|itp_primary|itp_bonus_against_shield,itcf_shoot_musket|itcf_carry_spear|itcf_reload_musket, 
	1250 , weight(5.6)|abundance(70)|difficulty(0)|spd_rtng(120) | shoot_speed(180) | thrust_damage(45 ,pierce)|max_ammo(30)|accuracy(93),imodbits_gun,
	[(ti_on_weapon_attack, [(play_sound,"snd_laser_fire"),(position_move_x, pos1,14),(position_move_y, pos1,18)]
	+#<muzzleflare system>#
	muzzleflare_system,
	#</muzzleflare system>#
	)]], 
["dlt19", "DLT-19", [("DLT19",0),("DLT19_inventory",ixmesh_inventory)], itp_type_crossbow|itp_two_handed |itp_merchandise|itp_primary|itp_bonus_against_shield,itcf_shoot_musket|itcf_carry_spear|itcf_reload_musket, 
	600 , weight(3.5)|abundance(100)|difficulty(0)|spd_rtng(80) | shoot_speed(170) | thrust_damage(90 ,pierce)|max_ammo(6)|accuracy(97),imodbits_gun,
	[(ti_on_weapon_attack, [(play_sound,"snd_bigblaster01"),(position_move_x, pos1,4),(position_move_y, pos1,5)]
	+#<muzzleflare system>#
	muzzleflare_system,
	#</muzzleflare system>#
	)]],
["dlt19_scope", "DLT-19 with Scope", [("DLT19_scope",0),("DLT19_scope_inventory",ixmesh_inventory)], itp_type_crossbow|itp_two_handed |itp_merchandise|itp_primary|itp_bonus_against_shield,itcf_shoot_musket|itcf_carry_spear|itcf_reload_musket, 
	690 , weight(3.5)|abundance(70)|difficulty(0)|spd_rtng(90) | shoot_speed(190) | thrust_damage(90 ,pierce)|max_ammo(12)|accuracy(96),imodbits_gun,
	[(ti_on_weapon_attack, [(play_sound,"snd_bigblaster01"),(position_move_x, pos1,4),(position_move_y, pos1,5)]
	+#<muzzleflare system>#
	muzzleflare_system,
	#</muzzleflare system>#
	)]], 
["dlt20a", "DLT-20A", [("DLT20A",0),("DLT20A_inventory",ixmesh_inventory)], itp_type_crossbow|itp_two_handed |itp_merchandise|itp_primary|itp_has_bayonet|itp_bonus_against_shield,itcf_shoot_crossbow|itcf_carry_spear|itcf_reload_musket, 
  1300 , weight(6.7)|abundance(100)|difficulty(0)|spd_rtng(100) | shoot_speed(190) | thrust_damage(55 ,cut)|max_ammo(30)|accuracy(97),imodbits_gun,
  [(ti_on_init_item, [(item_set_slot, "itm_dlt20a", slot_item_sound,"snd_bigblaster01"),]
  +#<muzzleflare system>#
  muzzleflare_system,
  #</muzzleflare system>#
  )]], 
["e17d", "E-17d", [("uio0000_E-17d",0),("uio0000_E-17d_inv",ixmesh_inventory)], itp_type_crossbow|itp_two_handed |itp_merchandise|itp_primary|itp_bonus_against_shield,itcf_shoot_musket|itcf_carry_spear|itcf_reload_musket, 
	735 , weight(3.72)|abundance(90)|difficulty(0)|spd_rtng(70) | shoot_speed(170) | thrust_damage(88 ,pierce)|max_ammo(5)|accuracy(110),imodbits_gun,
	[(ti_on_weapon_attack, [(play_sound,"snd_bigblaster01"),(position_move_x, pos1,4),(position_move_y, pos1,5)]
	+#<muzzleflare system>#
	muzzleflare_system,
	#</muzzleflare system>#
	)]],
#TEST - DC15a particle effects
# ["dc15a", "DC-15A", [("DC15A",0)], itp_type_crossbow|itp_two_handed |itp_merchandise|itp_primary|itp_bonus_against_shield,itcf_shoot_crossbow|itcf_carry_sword_back|itcf_reload_musket, 
	# 435 , weight(3.5)|abundance(100)|difficulty(0)|spd_rtng(90) | shoot_speed(190) | thrust_damage(60 ,pierce)|max_ammo(10)|accuracy(96),imodbits_gun,
	# [(ti_on_weapon_attack, [(play_sound,"snd_bigblaster01"),(position_move_x, pos1,4),(position_move_y, pos1,5),(particle_system_burst, "psys_blaster_smoke", pos1, 15)])]], 
#["dc15a", "DC-15A", [("DC15A",0)], itp_type_crossbow|itp_two_handed |itp_merchandise|itp_primary|itp_bonus_against_shield,itcf_shoot_musket|itcf_carry_spear|itcf_reload_musket, 
#removed merch flag since there are two dc15a's
["dc17m", "DC-17M", [("dc17m",0),("dc17m_inv",ixmesh_inventory)], itp_type_crossbow|itp_two_handed|itp_primary|itp_bonus_against_shield,itcf_shoot_crossbow|itcf_carry_spear|itcf_reload_musket, 
	985 , weight(4.8)|abundance(80)|difficulty(0)|spd_rtng(90) | shoot_speed(200) | thrust_damage(36 ,pierce)|max_ammo(999)|accuracy(94),imodbits_gun,
	[(ti_on_weapon_attack, [(play_sound,"snd_bigblaster01"),(position_move_x, pos1,4),(position_move_y, pos1,5)]
	+#<muzzleflare system>#
	muzzleflare_system,
	#</muzzleflare system>#
	)]],
["dc15a", "DC-15A", [("DC15A",0),("DC15A_inv",ixmesh_inventory)], itp_type_crossbow|itp_two_handed|itp_primary|itp_bonus_against_shield|itp_has_bayonet,itcf_shoot_crossbow|itcf_carry_spear|itcf_reload_musket, 
  1385 , weight(6.8)|abundance(100)|difficulty(0)|spd_rtng(90) | shoot_speed(190) | thrust_damage(60 ,cut)|max_ammo(500)|accuracy(96),imodbits_gun,
  [(ti_on_init_item, [(item_set_slot, "itm_dc15a", slot_item_sound,"snd_bigblaster01"),]
  +#<muzzleflare system>#
  muzzleflare_system,
  #</muzzleflare system>#
  )]],


["dc15a_hip", "DC-15A", [("DC15A",0),("DC15A_inv",ixmesh_inventory)], itp_type_crossbow|itp_two_handed|itp_primary|itp_bonus_against_shield|itp_has_bayonet,itcf_throw_javelin|itcf_carry_spear|itcf_reload_musket, 
  1385 , weight(6.8)|abundance(100)|difficulty(0)|spd_rtng(90) | shoot_speed(190) | thrust_damage(60 ,cut)|max_ammo(500)|accuracy(96),imodbits_gun,
  [(ti_on_init_item, [(item_set_slot, "itm_dc15a_hip", slot_item_sound,"snd_bigblaster01"),]
  +#<muzzleflare system>#
  muzzleflare_system,
  #</muzzleflare system>#
  )]],
    
["dc15a_hip2", "DC-15A", [("DC15A_javelin",0),("DC15A_inv",ixmesh_inventory)], itp_type_crossbow|itp_two_handed |itp_merchandise|itp_primary|itp_has_bayonet|itp_bonus_against_shield,itcf_throw_javelin|itcf_carry_quiver_back|itcf_reload_musket, 
  1385 , weight(6.8)|abundance(100)|difficulty(0)|spd_rtng(90) | shoot_speed(190) | thrust_damage(60 ,cut)|max_ammo(500)|accuracy(96),imodbits_gun,
  [(ti_on_init_item, [(item_set_slot, "itm_dc15a_hip2", slot_item_sound,"snd_bigblaster01"),]
  +#<muzzleflare system>#
  muzzleflare_system,
  #</muzzleflare system>#
  )]],

["dc15a_stun", "DC-15A", [("DC15A",0),("DC15A_inv",ixmesh_inventory)], itp_type_crossbow|itp_two_handed|itp_primary|itp_bonus_against_shield,itcf_shoot_crossbow|itcf_carry_spear|itcf_reload_musket, 
  1385 , weight(6.8)|abundance(100)|difficulty(0)|spd_rtng(90) | shoot_speed(190) | thrust_damage(60 ,pierce)|max_ammo(500)|accuracy(96),imodbits_gun,
  [(ti_on_weapon_attack, [(play_sound,"snd_bigblaster01"),(position_move_x, pos1,4),(position_move_y, pos1,5)]
  +#<muzzleflare system>#
  muzzleflare_system,
  #</muzzleflare system>#
  )]],

#["dc15s", "DC-15S", [("DC15S",0)], itp_type_crossbow|itp_two_handed |itp_merchandise|itp_primary|itp_bonus_against_shield,itcf_shoot_crossbow|itcf_carry_quiver_front_right|itcf_reload_musket, 
#["dc15s", "DC-15S", [("DC15S",0)], itp_type_crossbow|itp_two_handed |itp_merchandise|itp_primary|itp_bonus_against_shield,itcf_shoot_crossbow|itcf_carry_spear|itcf_reload_musket, 
["dc15s", "DC-15S", [("DC15S",0),("DC15S_inventory",ixmesh_inventory)], itp_type_crossbow|itp_two_handed |itp_merchandise|itp_primary|itp_has_bayonet|itp_bonus_against_shield,itcf_shoot_crossbow|itcf_carry_spear|itcf_reload_pistol, 
  987 , weight(4.62)|abundance(100)|difficulty(0)|spd_rtng(120) | shoot_speed(150) | thrust_damage(35 ,cut)|max_ammo(500)|accuracy(94),imodbits_gun,
  [(ti_on_init_item, [(item_set_slot, "itm_dc15s", slot_item_sound,"snd_laser_fire"),]
  +#<muzzleflare system>#
  muzzleflare_system,
  #</muzzleflare system>#
  )]], 
["trandoshan_acp_array_gun", "Trandoshan ACP Array Gun", [("trandoshan_acp_array_gun_javelin",0),("trandoshan_acp_array_gun_inventory",ixmesh_inventory)], itp_type_crossbow|itp_two_handed |itp_merchandise|itp_primary|itp_bonus_against_shield,itcf_throw_javelin|itcf_carry_quiver_back|itcf_reload_pistol, 
	883 , weight(4.52)|abundance(70)|difficulty(0)|spd_rtng(100) | shoot_speed(170) | thrust_damage(65 ,pierce)|max_ammo(8)|accuracy(79),imodbits_gun,
	[(ti_on_weapon_attack, [(play_sound,"snd_laser_fire"),(position_move_x, pos1,14),(position_move_y, pos1,18)]
	+#<muzzleflare system>#
	muzzleflare_system,
	#</muzzleflare system>#
	)]], 
["trandoshan_stun_gun", "Trandoshan Stun Gun", [("trandoshan_stun_gun",0),("trandoshan_stun_gun_inventory",ixmesh_inventory)], itp_type_crossbow|itp_two_handed |itp_merchandise|itp_primary|itp_bonus_against_shield,itcf_shoot_musket|itcf_carry_spear|itcf_reload_musket, 
	295 , weight(3.5)|abundance(70)|difficulty(0)|spd_rtng(90) | shoot_speed(170) | thrust_damage(40 ,blunt)|max_ammo(12)|accuracy(65),imodbits_gun,
	[(ti_on_weapon_attack, [(play_sound,"snd_stunblaster"),(position_move_x, pos1,14),(position_move_y, pos1,18)]
	+#<muzzleflare system>#
	muzzleflare_system,
	#</muzzleflare system>#
	)]],  
["quicksnap_36t", "QuickSnap 36T", [("QuickSnap_36T_carabine",0),("QuickSnap_36T_carabine_inventory",ixmesh_inventory)], itp_type_crossbow|itp_has_bayonet|itp_two_handed |itp_merchandise|itp_primary|itp_bonus_against_shield,itcf_shoot_crossbow|itcf_carry_spear|itcf_reload_pistol, 
  305 , weight(2.23)|abundance(70)|difficulty(0)|spd_rtng(100) | shoot_speed(170) | thrust_damage(36 ,cut)|max_ammo(100)|accuracy(93),imodbits_gun,
  [(ti_on_init_item, [(item_set_slot, "itm_quicksnap_36t", slot_item_sound,"snd_laser_fire"),]
  +#<muzzleflare system>#
  muzzleflare_system,
  #</muzzleflare system>#
  )]],
["bothan_bola_carabine", "Bothan Bola Carabine", [("bothan_bola_carabine",0),("bothan_bola_carabine_inventory",ixmesh_inventory)], itp_type_crossbow|itp_two_handed |itp_merchandise|itp_primary|itp_bonus_against_shield,itcf_shoot_musket|itcf_carry_spear|itcf_reload_musket, 
	305 , weight(2.5)|abundance(70)|difficulty(0)|spd_rtng(80) | shoot_speed(170) | thrust_damage(42 ,pierce)|max_ammo(16)|accuracy(95),imodbits_gun,
	[(ti_on_weapon_attack, [(play_sound,"snd_bigblaster01"),(position_move_x, pos1,14),(position_move_y, pos1,18)]
	+#<muzzleflare system>#
	muzzleflare_system,
	#</muzzleflare system>#
	)]], 
["ee3", "EE-3", [("EE3",0),("EE3_inventory",ixmesh_inventory)], itp_type_crossbow|itp_two_handed |itp_merchandise|itp_primary|itp_has_bayonet|itp_bonus_against_shield,itcf_shoot_crossbow|itcf_carry_spear|itcf_reload_pistol, 
  975 , weight(6.57)|abundance(100)|difficulty(0)|spd_rtng(100) | shoot_speed(170) | thrust_damage(36 ,cut)|max_ammo(30)|accuracy(96),imodbits_gun,
  [(ti_on_init_item, [(item_set_slot, "itm_ee3", slot_item_sound,"snd_bigblaster22"),]
  +#<muzzleflare system>#
  muzzleflare_system,
  #</muzzleflare system>#
  )]], 
["ee3_stun", "Stun EE-3", [("EE3",0),("EE3_inventory",ixmesh_inventory)], itp_type_crossbow|itp_two_handed |itp_primary|itp_bonus_against_shield,itcf_shoot_crossbow|itcf_carry_spear|itcf_reload_pistol, 
	875 , weight(6.57)|abundance(80)|difficulty(0)|spd_rtng(100) | shoot_speed(170) | thrust_damage(36 ,blunt)|max_ammo(30)|accuracy(96),imodbits_gun,
	[(ti_on_weapon_attack, [(play_sound,"snd_stunblaster"),(position_move_x, pos1,14),(position_move_y, pos1,18)]
	+#<muzzleflare system>#
	muzzleflare_system,
	#</muzzleflare system>#
	)]],  
["mg15", "RT-97C", [("MG15",0),("MG15_inventory",ixmesh_inventory)], itp_type_crossbow|itp_two_handed |itp_merchandise|itp_primary|itp_has_bayonet|itp_bonus_against_shield,itcf_shoot_musket|itcf_carry_spear|itcf_reload_musket, 
  2000 , weight(6.43)|abundance(100)|difficulty(0)|spd_rtng(90) | shoot_speed(180) | thrust_damage(47 ,cut)|max_ammo(500)|accuracy(97),imodbits_gun,
  [(ti_on_init_item, [(item_set_slot, "itm_mg15", slot_item_sound,"snd_laser_fire"),]
  +#<muzzleflare system>#
  muzzleflare_system,
  #</muzzleflare system>#
  )]],  
#used itcf_throw_javelin for e5 so it is fired from the hip
["e5", "E-5", [("e5_new_javelin",0),("e5_new_inventory",ixmesh_inventory)], itp_type_crossbow|itp_two_handed |itp_merchandise|itp_primary|itp_has_bayonet|itp_bonus_against_shield,itcf_throw_javelin|itcf_carry_quiver_back|itcf_reload_pistol, 
  900 , weight(2.2)|abundance(70)|difficulty(0)|spd_rtng(100) | shoot_speed(150) | thrust_damage(32 ,cut)|max_ammo(500)|accuracy(94),imodbits_gun,
  [(ti_on_init_item, [(item_set_slot, "itm_e5", slot_item_sound,"snd_e5"),]
  +#<muzzleflare system>#
  muzzleflare_system,
  #</muzzleflare system>#
  )]],  
#SW - now using itcf_throw_javelin for e11(itcf_shoot_javelin doesn't work, had to rotate the mesh as well) 
#["e11", "E-11", [("e11_new_javelin",0),("e11_new_inventory",ixmesh_inventory)], itp_type_crossbow|itp_two_handed |itp_merchandise|itp_primary|itp_bonus_against_shield,itcf_throw_javelin|itcf_carry_spear|itcf_reload_pistol, 
#removed merch flag since there are two e11's
["e11", "E-11", [("e11_new",0),("e11_new_inventory",ixmesh_inventory)], itp_type_crossbow|itp_two_handed|itp_primary|itp_has_bayonet|itp_bonus_against_shield,itcf_shoot_crossbow|itcf_carry_spear|itcf_reload_pistol, 
  1000 , weight(4.5)|abundance(100)|difficulty(0)|spd_rtng(110) | shoot_speed(160) | thrust_damage(36 ,cut)|max_ammo(100)|accuracy(92),imodbits_gun,
  [(ti_on_init_item, [(item_set_slot, "itm_e11", slot_item_sound,"snd_bigblaster15_variant"),]
  +#<muzzleflare system>#
  muzzleflare_system,
  #</muzzleflare system>#
  )]], 

["e11_hip", "E-11", [("e11_new_javelin",0),("e11_new_inventory",ixmesh_inventory)], itp_type_crossbow|itp_two_handed |itp_merchandise|itp_primary|itp_has_bayonet|itp_bonus_against_shield,itcf_throw_javelin|itcf_carry_quiver_back|itcf_reload_pistol, 
  1000 , weight(4.5)|abundance(100)|difficulty(0)|spd_rtng(110) | shoot_speed(160) | thrust_damage(36 ,cut)|max_ammo(100)|accuracy(92),imodbits_gun,
  [(ti_on_init_item, [(item_set_slot, "itm_e11_hip", slot_item_sound,"snd_bigblaster15_variant"),]
  +#<muzzleflare system>#
  muzzleflare_system,
  #</muzzleflare system>#
  )]], 
#["lightsaber_blue", "Lightsaber", [("lightsaber_blue",0),("lightsaber_blueoff",ixmesh_carry)], itp_type_two_handed_wpn|itp_merchandise| itp_primary|itp_bonus_against_shield|itp_wooden_parry|itp_wooden_attack, itc_lightsaber|itcf_carry_dagger_front_left,
# 900 , weight(0.5)|abundance(80)|difficulty(14)|spd_rtng(120) | weapon_length(115)|swing_damage(75 , pierce) | thrust_damage(75 ,  pierce),imodbits_lightsaber ],
#["e11", "E-11", [("e11_new",0),("lightsaber_blue", ixmesh_carry)], itp_type_crossbow|itp_two_handed |itp_merchandise|itp_primary|itp_bonus_against_shield,itcf_shoot_crossbow|itcf_carry_revolver_right|itcf_reload_musket, 
#["e11", "E-11", [("e11_new",0),("lightsaber_blue", ixmesh_carry)], itp_type_musket|itp_two_handed|itp_merchandise|itp_primary|itp_bonus_against_shield,itcf_shoot_crossbow|itcf_carry_sword_back,
#	310 , weight(2)|abundance(100)|difficulty(0)|spd_rtng(110) | shoot_speed(160) | thrust_damage(36 ,pierce)|max_ammo(16)|accuracy(94),imodbits_gun,
#	[(ti_on_weapon_attack, [(play_sound,"snd_bigblaster15"),(position_move_x, pos1,12),(position_move_y, pos1,15)])]], 	
#SW - now using itcf_throw_javelin for e11(itcf_shoot_javelin doesn't work, had to rotate the mesh as well) 
["e11_stun", "Stun E-11", [("e11_new_javelin",0),("e11_new_inventory",ixmesh_inventory)], itp_type_crossbow |itp_has_bayonet|itp_two_handed|itp_primary|itp_bonus_against_shield,itcf_throw_javelin|itcf_carry_spear|itcf_reload_pistol, 
  1000 , weight(4.5)|abundance(80)|difficulty(0)|spd_rtng(110) | shoot_speed(160) | thrust_damage(36 ,blunt)|max_ammo(100)|accuracy(94),imodbits_gun,
  [(ti_on_init_item, [(item_set_slot, "itm_e11_stun", slot_item_sound,"snd_stunblaster"),]
  +#<muzzleflare system>#
  muzzleflare_system,
  #</muzzleflare system>#
  )]], 
["wookiee_bowcaster", "Bowcaster", [("wookiee_bowcaster",0)], itp_type_crossbow|itp_two_handed |itp_merchandise|itp_primary|itp_bonus_against_shield,itcf_shoot_crossbow|itcf_carry_crossbow_back|itcf_reload_musket, 
	900 , weight(6.3)|abundance(100)|difficulty(0)|spd_rtng(120) | shoot_speed(160) | thrust_damage(50 ,pierce)|max_ammo(35)|accuracy(94),imodbits_gun,
	[(ti_on_weapon_attack, [(play_sound,"snd_bigblaster22"),(position_move_x, pos1,6),(position_move_y, pos1,8)]
	+#<muzzleflare system>#
	muzzleflare_system,
	#</muzzleflare system>#
	)]],
["kashyyyk_long_gun", "Kashyyyk Long Gun", [("kashyyyk_long_gun",0),("kashyyyk_long_gun_inventory",ixmesh_inventory)], itp_type_crossbow|itp_two_handed |itp_merchandise|itp_primary|itp_bonus_against_shield|itp_cant_reload_on_horseback,itcf_shoot_musket|itcf_carry_spear|itcf_reload_mask, 
	2000 , weight(8.7)|abundance(70)|difficulty(0)|spd_rtng(85) | shoot_speed(190) | thrust_damage(100 ,pierce)|max_ammo(10)|accuracy(82),imodbits_gun,
	[(ti_on_weapon_attack, [(play_sound,"snd_bigblaster22"),(position_move_x, pos1,18),(position_move_y, pos1,22)]
	+#<muzzleflare system>#
	muzzleflare_system,
	#</muzzleflare system>#
	)]],	
["tusken_rifle", "Tusken Cycler Rifle", [("tusken_rifle",0),("tusken_rifle_inventory",ixmesh_inventory)], itp_type_crossbow|itp_two_handed |itp_merchandise|itp_primary|itp_bonus_against_shield,itcf_shoot_musket|itcf_carry_spear|itcf_reload_musket, 
	910 , weight(5.35)|abundance(70)|difficulty(0)|spd_rtng(80) | shoot_speed(170) | thrust_damage(35 ,pierce)|max_ammo(15)|accuracy(93),imodbits_gun,
	[(ti_on_weapon_attack, [(play_sound,"snd_laser_fire"),(position_move_x, pos1,14),(position_move_y, pos1,18)]
	+#<muzzleflare system>#
	muzzleflare_system,
	#</muzzleflare system>#
	)]],   
["geonosian_sonic_rifle", "Geonosian Sonic Rifle", [("geonosian_sonic_rifle_javelin",0),("geonosian_sonic_rifle_inventory",ixmesh_inventory)], itp_type_crossbow|itp_two_handed |itp_merchandise|itp_primary|itp_bonus_against_shield,itcf_throw_javelin|itcf_carry_quiver_back|itcf_reload_musket, 
	931 , weight(3.0)|abundance(70)|difficulty(0)|spd_rtng(90) | shoot_speed(145) | thrust_damage(55 ,blunt)|max_ammo(50)|accuracy(95),imodbits_gun,
	[(ti_on_weapon_attack, [(play_sound,"snd_sonicblaster"),(position_move_x, pos1,14),(position_move_y, pos1,18)]
	+#<muzzleflare system>#
	muzzleflare_system,
	#</muzzleflare system>#
	)]], 
["t21", "T-21", [("T21",0),("T21_inventory",ixmesh_inventory)], itp_type_crossbow|itp_two_handed |itp_merchandise|itp_primary|itp_bonus_against_shield,itcf_shoot_musket|itcf_carry_spear|itcf_reload_musket, 
	2000 , weight(4.5)|abundance(60)|difficulty(0)|spd_rtng(80) | shoot_speed(170) | thrust_damage(65 ,pierce)|max_ammo(30)|accuracy(96),imodbits_gun,
	[(ti_on_weapon_attack, [(play_sound,"snd_bigblaster01"),(position_move_x, pos1,4),(position_move_y, pos1,5)]
	+#<muzzleflare system>#
	muzzleflare_system,
	#</muzzleflare system>#
	)]], 
#["msg90", "MSG-90", [("msg90_no_dipod",0)], itp_type_crossbow|itp_two_handed |itp_merchandise|itp_primary|itp_bonus_against_shield,itcf_shoot_crossbow|itcf_carry_sword_back|itcf_reload_musket, 440 , weight(4.0)|abundance(60)|difficulty(0)|spd_rtng(80) | shoot_speed(200) | thrust_damage(70 ,pierce)|max_ammo(6)|accuracy(98),imodbits_gun,
# [(ti_on_weapon_attack, [(play_sound,"snd_bigblaster01"),(position_move_x, pos1,4),(position_move_y, pos1,5)])]], 
["senate_rifle", "Security Guard Rifle", [("senate_rifle",0),("senate_rifle_inventory",ixmesh_inventory)], itp_type_crossbow|itp_two_handed |itp_merchandise|itp_primary|itp_bonus_against_shield,itcf_shoot_crossbow|itcf_carry_spear|itcf_reload_musket, 
	500 , weight(3.4)|abundance(70)|difficulty(0)|spd_rtng(100) | shoot_speed(170) | thrust_damage(40 ,pierce)|max_ammo(14)|accuracy(96),imodbits_gun,
	[(ti_on_weapon_attack, [(play_sound,"snd_bigblaster01"),(position_move_x, pos1,6),(position_move_y, pos1,8)]
	+#<muzzleflare system>#
	muzzleflare_system,
	#</muzzleflare system>#
	)]],  
["kisteer_1284", "KiSteer 1284", [("kisteer_1284",0),("kisteer_1284_inventory",ixmesh_inventory)], itp_type_crossbow|itp_two_handed |itp_merchandise|itp_primary|itp_bonus_against_shield,itcf_shoot_musket|itcf_carry_spear|itcf_reload_musket, 
	130 , weight(2.5)|abundance(70)|difficulty(0)|spd_rtng(80) | shoot_speed(120) | thrust_damage(32 ,blunt)|max_ammo(10)|accuracy(97),imodbits_gun,
	[(ti_on_weapon_attack, [(play_sound,"snd_bigblaster01"),(position_move_x, pos1,6),(position_move_y, pos1,8)]
	+#<muzzleflare system>#
	muzzleflare_system,
	#</muzzleflare system>#
	)]],  
["ion_blaster", "Ion Blaster", [("ion_blaster",0),("ion_blaster_inventory",ixmesh_inventory)], itp_type_crossbow|itp_two_handed |itp_merchandise|itp_primary|itp_bonus_against_shield,itcf_shoot_crossbow|itcf_carry_spear|itcf_reload_pistol, 
	130 , weight(2.5)|abundance(70)|difficulty(0)|spd_rtng(70) | shoot_speed(120) | thrust_damage(32 ,blunt)|max_ammo(10)|accuracy(88),imodbits_gun,
	[(ti_on_weapon_attack, [(play_sound,"snd_ionblaster"),(position_move_x, pos1,14),(position_move_y, pos1,18)]
	+#<muzzleflare system>#
	muzzleflare_system,
	#</muzzleflare system>#
	)]], 
  
#@> Added by Swyter...
["heavy_repeater", "Imperial Heavy Repeater", [("HeavyRepeater",0),("HeavyRepeater_inv",ixmesh_inventory),("HeavyRepeater_carried",ixmesh_carry)], itp_type_crossbow|itp_has_bayonet|itp_two_handed|itp_merchandise|itp_primary|itp_bonus_against_shield,itcf_throw_javelin|itcf_carry_quiver_back|itcf_reload_pistol,
  1500 , weight(4.68)|abundance(100)|difficulty(0)|spd_rtng(120) | shoot_speed(169) | thrust_damage(36 ,cut)|max_ammo(400)|accuracy(94),imodbits_gun,
  [(ti_on_init_item, [(item_set_slot, "itm_heavy_repeater", slot_item_sound,"snd_heavyrepeater"),]
  +#<muzzleflare system>#
  muzzleflare_system,
  #</muzzleflare system>#
  )]],
["storm_rifle", "StormTrooper Rifle", [("uio0000_stormtrooperrifle",0),("uio0000_stormtrooperrifle_inv",ixmesh_inventory)], itp_type_crossbow|itp_has_bayonet|itp_two_handed|itp_merchandise|itp_primary|itp_bonus_against_shield,itcf_shoot_crossbow|itcf_carry_spear|itcf_reload_musket, 
  871 , weight(3.4)|abundance(70)|difficulty(0)|spd_rtng(85) | shoot_speed(170) | thrust_damage(47 ,cut)|max_ammo(30)|accuracy(94),imodbits_gun,
  [(ti_on_init_item, [(item_set_slot, "itm_storm_rifle", slot_item_sound,"snd_stormrifle"),]
  +#<muzzleflare system>#
  muzzleflare_system,
  #</muzzleflare system>#
  )]],  

 # ONE HANDED BLASTERS (ie. pistol)
["dh17", "DH-17", [("DH17",0)], itp_type_pistol |itp_merchandise|itp_primary|itp_bonus_against_shield,itcf_shoot_pistol|itcf_carry_revolver_right|itcf_reload_pistol, 
	550 , weight(1.24)|abundance(100)|difficulty(0)|spd_rtng(110) | shoot_speed(160) | thrust_damage(36 ,pierce)|max_ammo(500)|accuracy(88),imodbits_gun,
	[(ti_on_weapon_attack, [(play_sound,"snd_dh17"),(position_move_x, pos1,12),(position_move_y, pos1,15)]
	)]],
["dh17_stun", "Stun DH-17", [("DH17",0)], itp_type_pistol |itp_primary|itp_bonus_against_shield,itcf_shoot_pistol|itcf_carry_revolver_right|itcf_reload_pistol, 
	550 , weight(1.24)|abundance(80)|difficulty(0)|spd_rtng(110) | shoot_speed(160) | thrust_damage(36 ,blunt)|max_ammo(500)|accuracy(88),imodbits_gun,
	[(ti_on_weapon_attack, [(play_sound,"snd_stunblaster"),(position_move_x, pos1,12),(position_move_y, pos1,15)]
	)]], 

["se14r", "SE-14R", [("se_14r",0)], itp_type_pistol |itp_merchandise|itp_primary|itp_bonus_against_shield,itcf_shoot_pistol|itcf_carry_revolver_right|itcf_reload_pistol, 
	410 , weight(2)|abundance(100)|difficulty(0)|spd_rtng(110) | shoot_speed(160) | thrust_damage(36 ,pierce)|max_ammo(16)|accuracy(88),imodbits_gun,
	[(ti_on_weapon_attack, [(play_sound,"snd_bigblaster19"),(position_move_x, pos1,12),(position_move_y, pos1,15)]
	)]],	
["dl44a", "DL-44", [("DL44a",0)], itp_type_pistol |itp_merchandise|itp_primary|itp_bonus_against_shield,itcf_shoot_pistol|itcf_carry_revolver_right|itcf_reload_pistol, 
	750 , weight(1.5)|abundance(100)|difficulty(0)|spd_rtng(120) | shoot_speed(140) | thrust_damage(26,pierce)|max_ammo(25)|accuracy(87),imodbits_gun,
	[(ti_on_weapon_attack, [(play_sound,"snd_bigblaster19"),(position_move_x, pos1,12),(position_move_y, pos1,15)]
	)]],
["dl44a_stun", "Stun DL-44", [("DL44a",0)], itp_type_pistol |itp_primary|itp_bonus_against_shield,itcf_shoot_pistol|itcf_carry_revolver_right|itcf_reload_pistol, 
	750 , weight(1.5)|abundance(80)|difficulty(0)|spd_rtng(120) | shoot_speed(140) | thrust_damage(26,blunt)|max_ammo(25)|accuracy(87),imodbits_gun,
	[(ti_on_weapon_attack, [(play_sound,"snd_stunblaster"),(position_move_x, pos1,12),(position_move_y, pos1,15)]
	)]], 
["dl44b", "Modified DL-44", [("DL44b",0)], itp_type_pistol |itp_merchandise|itp_primary|itp_bonus_against_shield,itcf_shoot_pistol|itcf_carry_revolver_right|itcf_reload_pistol, 
	860 , weight(1.6)|abundance(70)|difficulty(0)|spd_rtng(140) | shoot_speed(160) | thrust_damage(32,pierce)|max_ammo(25)|accuracy(89),imodbits_gun,
	[(ti_on_weapon_attack, [(play_sound,"snd_bigblaster19"),(position_move_x, pos1,4),(position_move_y, pos1,5)]
	)]], 
#removed the carry flag from the q2 since its typically a small hidden weapon
["q2", "Q2", [("Q2",0)], itp_type_pistol |itp_merchandise|itp_primary|itp_bonus_against_shield,itcf_shoot_pistol|itcf_reload_pistol, 
	300 , weight(0.51)|abundance(100)|difficulty(0)|spd_rtng(120) | shoot_speed(140) | thrust_damage(24 ,pierce)|max_ammo(6)|accuracy(85),imodbits_gun,
	[(ti_on_weapon_attack, [(play_sound,"snd_littleblaster"),(position_move_x, pos1,14),(position_move_y, pos1,18)]
	)]], 
["q2_stun", "Stun Q2", [("Q2",0)], itp_type_pistol |itp_primary|itp_bonus_against_shield,itcf_shoot_pistol|itcf_carry_revolver_right|itcf_reload_pistol, 
	300 , weight(0.51)|abundance(80)|difficulty(0)|spd_rtng(120) | shoot_speed(140) | thrust_damage(24 ,blunt)|max_ammo(6)|accuracy(85),imodbits_gun,
	[(ti_on_weapon_attack, [(play_sound,"snd_stunblaster"),(position_move_x, pos1,14),(position_move_y, pos1,18)]
	)]],  
["elg3a", "ELG-3A", [("ELG_3A",0)], itp_type_pistol |itp_merchandise|itp_primary|itp_bonus_against_shield,itcf_shoot_pistol|itcf_carry_revolver_right|itcf_reload_pistol, 
	500 , weight(0.51)|abundance(80)|difficulty(0)|spd_rtng(125) | shoot_speed(150) | thrust_damage(29 ,pierce)|max_ammo(100)|accuracy(88),imodbits_gun,
	[(ti_on_weapon_attack, [(play_sound,"snd_littleblaster"),(position_move_x, pos1,14),(position_move_y, pos1,18)]
	)]], 
["elg3a_stun", "Stun ELG-3A", [("ELG_3A",0)], itp_type_pistol |itp_primary|itp_bonus_against_shield,itcf_shoot_pistol|itcf_carry_revolver_right|itcf_reload_pistol, 
	500 , weight(0.51)|abundance(60)|difficulty(0)|spd_rtng(125) | shoot_speed(150) | thrust_damage(29 ,blunt)|max_ammo(100)|accuracy(88),imodbits_gun,
	[(ti_on_weapon_attack, [(play_sound,"snd_stunblaster"),(position_move_x, pos1,14),(position_move_y, pos1,18)]
	)]],	
["scout_trooper_pistol", "Scout Trooper Pistol", [("scout_trooper_pistol",0)], itp_type_pistol |itp_merchandise|itp_primary|itp_bonus_against_shield,itcf_shoot_pistol|itcf_carry_revolver_right|itcf_reload_pistol, 
	595 , weight(1.5)|abundance(100)|difficulty(0)|spd_rtng(130) | shoot_speed(150) | thrust_damage(28 ,pierce)|max_ammo(14)|accuracy(90),imodbits_gun,
	[(ti_on_weapon_attack, [(play_sound,"snd_littleblaster"),(position_move_x, pos1,14),(position_move_y, pos1,18)]
	)]], 
["ddc_defender", "DDC Defender", [("DDC_defender",0)], itp_type_pistol |itp_merchandise|itp_primary|itp_bonus_against_shield,itcf_shoot_pistol|itcf_carry_revolver_right|itcf_reload_pistol, 
	347 , weight(1.17)|abundance(100)|difficulty(0)|spd_rtng(130) | shoot_speed(140) | thrust_damage(24 ,pierce)|max_ammo(100)|accuracy(90),imodbits_gun,
	[(ti_on_weapon_attack, [(play_sound,"snd_littleblaster"),(position_move_x, pos1,12),(position_move_y, pos1,15)]
	)]],  
["geonosian_sonic_pistol", "Geonosian Sonic Pistol", [("geonosian_sonic_pistol",0)], itp_type_pistol |itp_merchandise|itp_primary|itp_bonus_against_shield,itcf_shoot_pistol|itcf_carry_revolver_right|itcf_reload_pistol, 
	772 , weight(1.5)|abundance(70)|difficulty(0)|spd_rtng(90) | shoot_speed(150) | thrust_damage(36 ,blunt)|max_ammo(10)|accuracy(89),imodbits_gun,
	[(ti_on_weapon_attack, [(play_sound,"snd_sonicblaster"),(position_move_x, pos1,14),(position_move_y, pos1,18)]
	)]],   
["dl18", "DL-18", [("dl18",0)], itp_type_pistol |itp_merchandise|itp_primary|itp_bonus_against_shield,itcf_shoot_pistol|itcf_carry_revolver_right|itcf_reload_pistol, 
	500 , weight(1.13)|abundance(100)|difficulty(0)|spd_rtng(120) | shoot_speed(130) | thrust_damage(22 ,pierce)|max_ammo(100)|accuracy(89),imodbits_gun,
	[(ti_on_weapon_attack, [(play_sound,"snd_laser_fire"),(position_move_x, pos1,7),(position_move_y, pos1,9)]
	)]],  
["westar", "Westar-34", [("westar",0)], itp_type_pistol |itp_merchandise|itp_primary|itp_bonus_against_shield,itcf_shoot_pistol|itcf_carry_revolver_right|itcf_reload_pistol, 
	1300 , weight(1.5)|abundance(40)|difficulty(0)|spd_rtng(130) | shoot_speed(140) | thrust_damage(40 ,pierce)|max_ammo(20)|accuracy(90),imodbits_gun,
	[(ti_on_weapon_attack, [(play_sound,"snd_westar"),(position_move_x, pos1,7),(position_move_y, pos1,9)]
	)]],  
["westar_stun", "Stun Westar-34", [("westar",0)], itp_type_pistol |itp_primary|itp_bonus_against_shield,itcf_shoot_pistol|itcf_carry_revolver_right|itcf_reload_pistol, 
	1300 , weight(1.5)|abundance(40)|difficulty(0)|spd_rtng(130) | shoot_speed(140) | thrust_damage(40 ,blunt)|max_ammo(20)|accuracy(90),imodbits_gun,
	[(ti_on_weapon_attack, [(play_sound,"snd_westar"),(position_move_x, pos1,17),(position_move_y, pos1,9)]
	)]],    
["ion_pistol", "Ion Pistol", [("ion_pistol",0)], itp_type_pistol |itp_merchandise|itp_primary|itp_bonus_against_shield,itcf_shoot_pistol|itcf_carry_revolver_right|itcf_reload_pistol, 
	800 , weight(3.1)|abundance(70)|difficulty(0)|spd_rtng(60) | shoot_speed(120) | thrust_damage(36,blunt)|max_ammo(15)|accuracy(85),imodbits_gun,
	[(ti_on_weapon_attack, [(play_sound,"snd_ionblaster"),(position_move_x, pos1,14),(position_move_y, pos1,18)]
	)]], 
#["trandoshan_supressor", "Trandoshan Supressor", [("trandoshan_supressor",0)], itp_type_pistol |itp_merchandise|itp_primary|itp_bonus_against_shield,itcf_shoot_pistol|itcf_carry_revolver_right|itcf_reload_pistol, 
["trandoshan_supressor", "Trandoshan Supressor", [("trandoshan_supressor",0)], itp_type_pistol |itp_merchandise|itp_primary|itp_bonus_against_shield,itcf_shoot_pistol|itcf_carry_quiver_right_vertical|itcf_reload_pistol, 
	795 , weight(1.5)|abundance(70)|difficulty(0)|spd_rtng(110) | shoot_speed(150) | thrust_damage(32,blunt)|max_ammo(10)|accuracy(90),imodbits_gun,
	[(ti_on_weapon_attack, [(play_sound,"snd_stunblaster"),(position_move_x, pos1,10),(position_move_y, pos1,14)]
	)]],    
["wrist_blaster", "Wrist Mounted Blaster", [("_",0),("wrist_blaster",ixmesh_inventory)], itp_merchandise|itp_type_pistol|itp_primary|itp_bonus_against_shield,itcf_shoot_pistol|itcf_reload_pistol, 
	500 , weight(1.3)|abundance(60)|difficulty(0)|spd_rtng(105) | shoot_speed(135) | thrust_damage(35,pierce)|max_ammo(24)|accuracy(90),imodbits_none,
	[(ti_on_weapon_attack, [(play_sound,"snd_laser_fire"),(position_move_x, pos1,0),(position_move_y, pos1,0)]
	)]],

["ranged_weapons_end", "<dummy>", [("_",0)], 0,0,0,0,imodbits_none],
 
# practice/training
["practice_dl44", "DL-44", [("DL44a",0)], itp_type_pistol|itp_primary|itp_bonus_against_shield,itcf_shoot_pistol|itcf_carry_revolver_right|itcf_reload_pistol, 300 , weight(1.5)|abundance(100)|difficulty(0)|spd_rtng(120) | shoot_speed(140) | thrust_damage(26,pierce)|max_ammo(12)|accuracy(90),imodbits_gun,
 [(ti_on_weapon_attack, [(play_sound,"snd_bigblaster19"),(position_move_x, pos1,14),(position_move_y, pos1,18)])]], 
["dl44a_training", "DL-44", [("DL44a",0)], itp_type_pistol |itp_primary|itp_bonus_against_shield,itcf_shoot_pistol|itcf_carry_revolver_right|itcf_reload_pistol, 300 , weight(1.5)|abundance(100)|difficulty(0)|spd_rtng(120) | shoot_speed(140) | thrust_damage(26,pierce)|max_ammo(1)|accuracy(92),imodbits_gun,
  [(ti_on_weapon_attack, [(play_sound,"snd_bigblaster19"),(position_move_x, pos1,14),(position_move_y, pos1,18)])]], 
["dlt19_training", "DLT-19 with Scope", [("DLT19_scope",0),("DLT19_scope_inventory",ixmesh_inventory)], itp_type_crossbow|itp_two_handed |itp_primary|itp_bonus_against_shield,itcf_shoot_crossbow|itcf_carry_spear|itcf_reload_pistol, 500 , weight(3.5)|abundance(100)|difficulty(0)|spd_rtng(90) | shoot_speed(190) | thrust_damage(60 ,pierce)|max_ammo(1)|accuracy(96),imodbits_gun,
 [(ti_on_weapon_attack, [(play_sound,"snd_laser_fire"),(position_move_x, pos1,14),(position_move_y, pos1,18)])]], 

#Heavy Weapons start ---------------------------------------------------------------------------
#["heavy_weapons_ammo","Heavy Weapons Ammo", [("_",0),("_",ixmesh_flying_ammo),("rpg_rocket", ixmesh_inventory)], itp_type_bolts|itp_merchandise,0, 100,weight(2.25)|abundance(90)|weapon_length(10)|thrust_damage(1,pierce)|max_ammo(40),imodbits_ammo],
["heavy_weapons_ammo","Heavy Weapons Ammo", [("_",0),("_",ixmesh_flying_ammo),("player_chest_sw", ixmesh_inventory)], itp_type_bolts|itp_unique,0, 100,weight(2.25)|abundance(90)|weapon_length(10)|thrust_damage(1,pierce)|max_ammo(12),imodbits_ammo],
##RPG start ---------------------------------------------------------------------------
#["rocket_launcher", "Prototype RDP-12 Rocket Launcher", [("rpg",0)], itp_type_crossbow|itp_merchandise|itp_primary|itp_bonus_against_shield|itp_two_handed ,itcf_shoot_musket|itcf_carry_spear, 3000 , weight(10.0)|abundance(90)|difficulty(0)|spd_rtng(60) | shoot_speed(160) | thrust_damage(150 ,pierce)|max_ammo(1)|accuracy(95),imodbits_none,
#["rocket_launcher", "RDP-12 Rocket Launcher (in development)", [("rpg",0),("rpg_inventory",ixmesh_inventory)], itp_type_crossbow|itp_unique|itp_primary|itp_bonus_against_shield|itp_two_handed|itp_cant_reload_on_horseback,itcf_shoot_musket|itcf_carry_spear|itcf_reload_mask, 4000 , weight(10.0)|abundance(90)|difficulty(0)|spd_rtng(60) | shoot_speed(160) | thrust_damage(150 ,pierce)|max_ammo(1)|accuracy(95),imodbits_none,
# [(ti_on_weapon_attack, [(play_sound,"snd_rocket_fire"),(position_move_x, pos1,27),(position_move_y, pos1,100),(particle_system_burst, "psys_rocket_forward_smoke", pos1, 15),(particle_system_burst, "psys_rocket_backward_smoke", pos1, 15), 
#  
##Highlander begin--------------------------------------
#  (store_current_scene,":scene"),
#  (try_begin),
#		(neg|is_between,":scene","scn_ship_hangar_imp","scn_space_battle"), #land battle  
#	#@->(neg|is_between,":scene","scn_ship_hangar_closed_1a","scn_space_battle"), #land battle
#	
#	(call_script,"script_emit_projectile",
#	pos1,#the position from where the projectile is emitted. Usually pos1 in the item triggers
#	100,#projectile speed in m/s when emitted
#	0,#Damage when the projectile itself hits an agent: Isn't needed for explosives. Use 0 here.
#	0,#bounce effect: Doesn't work, yet. Use 0 here.
#	1,#explosive: Should the projectile explode? Make sense for explosives. ;)
#	500, #explosion countdown. In 1/100 sec. 300 means in 3 seconds after shooting this projectile detonates (if it doesn't detonate before). Use a high number like 10000, if you don't want this feature.
#	1000,#explosion area:	/ The damage an agent receives when the projectile detonates will be generated the following way:
#	900,#explosion damage:	\ damage = (explosion area - distance_to_explosion) * explosion damage / explosion area
#	"psys_projectile_fly_smoke", # particle system: which particle system should be attached to the projectile? -1 = none.
#	4, #Unused
#	1, #Explode on ground hit: Should the projectile detonate, if it hits the ground?
#	-1,#Put a scene prop ID here, if you want it to follow the projectile. The scene props NEED to be placed in the scene, if it should work. -1 for no scene prop.
#	1 #check_collision: Set it to 1 in outdoors, 0 in interiors.
#	),
#	
#  (else_try),
#	#ship battle
#	(call_script,"script_emit_projectile",pos1,100,0,0,1,500,1000,900,"psys_projectile_fly_smoke",4,1,-1,0),
#  (try_end),
##Highlander end--------------------------------------
# ])]],
#
#
##RPG end ---------------------------------------------------------------------------

#["flame_ammo","Flamethrower Ammmo", [("_",0),("arrow",ixmesh_inventory)], itp_type_arrows|itp_merchandise|itp_bonus_against_shield, 0, 500,weight(4)|abundance(100)|weapon_length(60)|thrust_damage(1,pierce)|max_ammo(80),imodbits_none],

# Flame Rifle Start ----------------------------------------------------------------- (do not give a reload flag so it uses the crossbow reload sound effect)
# SW - concept below from Magic Mod: Curtain of Fire - http://forums.taleworlds.net/index.php/topic,30512.msg784362.html
["flame_rifle","CR-24 Flame Rifle (in development)", [("cr24_flame_rifle",0),("cr24_flame_rifle_inventory",ixmesh_inventory)],itp_type_crossbow |itp_unique|itp_primary|itp_bonus_against_shield|itp_two_handed,itcf_shoot_crossbow|itcf_carry_spear|itcf_reload_mask, 
	3200 , weight(4)|abundance(60)|spd_rtng(89) | shoot_speed(160) | thrust_damage(120, pierce)|max_ammo(6)|accuracy(95)|weapon_length(10),imodbits_none,
	[(ti_on_weapon_attack, [
						 (try_for_range,reg5,1,500),
                            (particle_system_burst, "psys_torch_fire", pos1, 15),
							(position_move_y,pos1,10),
                            (copy_position,pos2,pos1),
                            (position_set_z_to_ground_level, pos2),
                            (get_distance_between_positions,":dist",pos1,pos2),
                            (lt,":dist",10),
							(particle_system_burst, "psys_cooking_fire_1", pos1, 25),
							(particle_system_burst, "psys_cooking_smoke", pos1, 10),
							(play_sound,"snd_flame_fire"),
							(get_player_agent_no, ":player_agent"),  #SW modified
                            (try_for_agents,":agent"),
                               (agent_get_position,pos2,":agent"),
                               (get_distance_between_positions,":dist",pos1,pos2),
                               (lt,":dist",300),
                               (agent_set_hit_points,":agent",0,0),
                               #(agent_deliver_damage_to_agent,":agent",":agent"),	#SW modified
							   (agent_deliver_damage_to_agent,":player_agent",":agent"),
                            (end_try),
                            (scene_prop_get_instance,":instance", "spr_explosion", 0),
                            (position_copy_origin,pos2,pos1),
                            (prop_instance_set_position,":instance",pos2),
                            (position_move_z,pos2,1000),
                            (prop_instance_animate_to_position,":instance",pos2,175),
                            (assign,reg5,1000),
                          (end_try),],)]],
# Concussion Rifle Start -----------------------------------------------------------------
# SW - concept below from Magic Mod: Curtain of Fire - http://forums.taleworlds.net/index.php/topic,30512.msg784362.html
 ["concussion_rifle","W-90 Concussion Rifle (in development)", [("DLT19",0),("DLT19_inventory",ixmesh_inventory)],itp_type_crossbow |itp_unique|itp_primary|itp_bonus_against_shield|itp_two_handed,itcf_shoot_crossbow|itcf_carry_spear|itcf_reload_mask, 
	3200 , weight(4)|abundance(60)|spd_rtng(89) | shoot_speed(160) | thrust_damage(100, blunt)|max_ammo(8)|weapon_length(10),imodbits_none,
 [(ti_on_weapon_attack, [
						 (try_for_range,reg5,1,500),
                            (particle_system_burst, "psys_food_steam", pos1, 15),
                            (position_move_y,pos1,10),
                            (copy_position,pos2,pos1),
                            (position_set_z_to_ground_level, pos2),
                            (get_distance_between_positions,":dist",pos1,pos2),
                            (lt,":dist",10),
							(particle_system_burst, "psys_gourd_piece_2", pos1, 2),
							(play_sound,"snd_concussion_fire"),
							(get_player_agent_no, ":player_agent"),  #SW modified
                            (try_for_agents,":agent"),
                               (agent_get_position,pos2,":agent"),
                               (get_distance_between_positions,":dist",pos1,pos2),
                               (lt,":dist",300),
                               (agent_set_hit_points,":agent",1,0),
                               #(agent_set_hit_points,":agent",0,1),							   
                               #(agent_deliver_damage_to_agent,":agent",":agent"),	#SW modified
							   (agent_deliver_damage_to_agent,":player_agent",":agent"),
                            (end_try),
                            (scene_prop_get_instance,":instance", "spr_explosion", 0),
                            (position_copy_origin,pos2,pos1),
                            (prop_instance_set_position,":instance",pos2),
                            (position_move_z,pos2,1000),
                            (prop_instance_animate_to_position,":instance",pos2,175),
                            (assign,reg5,1000),
                          (end_try),],)]],						  
#------------------------------------------------------------------------------------------
# SW - concept below from Magic Mod: Curtain of Fire - http://forums.taleworlds.net/index.php/topic,30512.msg784362.html
# ["medpac","Medpac", [("_",0),("life_support_pack", ixmesh_inventory)], itp_type_thrown |itp_merchandise|itp_primary ,itcf_throw_stone, 
	# 1000 , weight(1)|abundance(90)|difficulty(0)|spd_rtng(90) | shoot_speed(30) | thrust_damage(1,  blunt)|max_ammo(1)|weapon_length(1),imodbits_none,
	# [(ti_on_weapon_attack, [(assign,":distance",99999),
							# (try_for_agents,":agent"),
                              # (agent_is_alive,":agent"),
                              # (agent_is_human,":agent"),
                              # (agent_get_look_position, pos2, ":agent"),
                              # (get_distance_between_positions,":dist",pos1,pos2),
                              # (lt,":dist",":distance"),
                              # (assign,":chosen",":agent"),
                              # (assign,":distance",":dist"),
                            # (end_try),
							# (agent_set_hit_points,":chosen",100,0),],)]],
# #------------------------------------------------------------------------------------------							
# # SW - concept below from Magic Mod: Curtain of Fire - http://forums.taleworlds.net/index.php/topic,30512.msg784362.html
# ["medpac_adv","Advanced Medpac", [("_",0),("life_support_pack", ixmesh_inventory)], itp_type_thrown |itp_merchandise|itp_primary ,itcf_throw_stone, 
	# 4000 , weight(1)|abundance(75)|difficulty(0)|spd_rtng(90) | shoot_speed(30) | thrust_damage(1,  blunt)|max_ammo(3)|weapon_length(1),imodbits_none,
	# [(ti_on_weapon_attack, [(assign,":distance",99999),
						# (try_for_agents,":agent"),
                              # (agent_is_alive,":agent"),
                              # (agent_is_human,":agent"),
                              # (agent_get_look_position, pos2, ":agent"),
                              # (get_distance_between_positions,":dist",pos1,pos2),
                              # (lt,":dist",":distance"),
                              # (assign,":chosen",":agent"),
                              # (assign,":distance",":dist"),
                            # (end_try),
							# (agent_set_hit_points,":chosen",100,0),],)]],
#------------------------------------------------------------------------------------------
# SW - concept below from Magic Mod: Curtain of Fire - http://forums.taleworlds.net/index.php/topic,30512.msg784362.html
["force_kill","Force Kill", [("_",0),("force_kill_inv", ixmesh_inventory)], itp_type_thrown|itp_unique|itp_two_handed|itp_primary ,itc_scimitar, 
	6000 , weight(0.1)|abundance(60)|difficulty(0)|spd_rtng(50) | shoot_speed(5) | thrust_damage(100,pierce)|max_ammo(1)|weapon_length(8),imodbits_none,
	[
		(ti_on_weapon_attack, [(
							 assign,":distance",99999),
                             #(particle_system_burst, "psys_game_blood", pos1, 45), #SW modified
                             #(particle_system_burst, "psys_game_blood_2", pos1, 45), #SW modified
							 (get_player_agent_no, ":player_agent"),
							 (try_for_agents,":agent"),
								(agent_is_alive,":agent"),
								(agent_is_human,":agent"),
								(agent_get_look_position, pos2, ":agent"),
								(get_distance_between_positions,":dist",pos1,pos2),
								(lt,":dist",":distance"),
								(assign,":chosen",":agent"),
								(assign,":distance",":dist"),
								(agent_get_team  ,":team", ":chosen"),
							 (end_try),
                             (try_for_agents,":agent"),
								(agent_is_alive,":agent"),
								(agent_is_human,":agent"), #SW modified
								(neq, ":agent", ":player_agent"), #SW modified
								(neq,":agent",":chosen"),
								(agent_get_team  ,":team2", ":agent"),
								(neq,":team",":team2"),
								(agent_get_position, pos2, ":agent"),
								(agent_get_position,pos1,":chosen"),
								(get_distance_between_positions,":dist",pos1,pos2),
								(lt,":dist",350),
									(position_move_z,pos2,150),
									(particle_system_burst, "psys_game_blood", pos2,95),
									(particle_system_burst, "psys_game_blood_2", pos2,95),
									(play_sound,"snd_metal_hit_low_armor_high_damage"),
									(agent_set_hit_points,":agent",0,0),
									#(agent_deliver_damage_to_agent,":agent",":agent"), #SW modified
									(agent_deliver_damage_to_agent,":player_agent",":agent"),
									#SW - decrease player health
									(store_agent_hit_points,":hp",":player_agent",1),
									(store_random_in_range, ":random", 3, 6),
									(val_sub,":hp",":random"),
									(try_begin),
										(le, ":hp", 0),
										(agent_set_hit_points,":player_agent",0,0),
									(else_try),
										(agent_set_hit_points,":player_agent",":hp",1),
									(try_end),
									(agent_deliver_damage_to_agent,":player_agent",":player_agent"),
                              (end_try),
					],)]],
#------------------------------------------------------------------------------------------
["force_choke","Force Choke", [("_",0),("force_kill_inv", ixmesh_inventory)], itp_type_thrown|itp_unique|itp_two_handed|itp_primary ,itc_scimitar, 
	5000 , weight(0.1)|abundance(60)|difficulty(0)|spd_rtng(50) | shoot_speed(5) |thrust_damage(15,blunt)|max_ammo(1)|weapon_length(8),imodbits_none,
	[
		(ti_on_weapon_attack, [
					(
							assign,":distance",99999),
                            #(particle_system_burst, "psys_game_blood", pos1, 45), #SW modified
                            #(particle_system_burst, "psys_game_blood_2", pos1, 45), #SW modified
							(get_player_agent_no, ":player_agent"),
							(try_for_agents,":agent"),
								(agent_is_alive,":agent"),
								(agent_is_human,":agent"),
								(agent_get_look_position, pos2, ":agent"),
								(get_distance_between_positions,":dist",pos1,pos2),
								(lt,":dist",":distance"),
								(assign,":chosen",":agent"),
								(assign,":distance",":dist"),
								(agent_get_team  ,":team", ":chosen"),
							(end_try),
                            (try_for_agents,":agent"),
								(agent_is_alive,":agent"),
								(agent_is_human,":agent"), #SW modified
								(neq, ":agent", ":player_agent"), #SW modified
								(neq,":agent",":chosen"),
								(agent_get_team  ,":team2", ":agent"),
								(neq,":team",":team2"),
								(agent_get_position, pos2, ":agent"),
								(agent_get_position,pos1,":chosen"),
								(get_distance_between_positions,":dist",pos1,pos2),
								(lt,":dist",500),	#SW - increased distance from 350
								#(position_move_z,pos2,150),
								#(particle_system_burst, "psys_game_blood", pos2,95),
								#(particle_system_burst, "psys_game_blood_2", pos2,95),
								#(play_sound,"snd_metal_hit_low_armor_high_damage"),
								#SW - modified to knock down agents
								(agent_play_sound,":player_agent","snd_force_push"),								
								(store_random_in_range, ":rand", 0, 100),
								(try_begin),
									(lt, ":rand", 35),
									#(agent_set_animation, ":agent", "anim_force_unsuccessful"),
									(agent_set_animation, ":agent", "anim_force_choke"),
									(store_random_in_range, ":hp_loss", 4, 6),
								(else_try),
									#(agent_set_animation, ":agent", "anim_force_crouch"),
									(agent_set_animation, ":agent", "anim_force_choke"),
									(store_random_in_range, ":hp_loss", 6, 10),
								(try_end),								
								(store_agent_hit_points,":hp",":agent",1),
								(val_sub,":hp",":hp_loss"),
								(agent_set_hit_points,":agent",":hp",1),
								(agent_deliver_damage_to_agent,":player_agent",":agent"),
                              (end_try),
					],)]],
#------------------------------------------------------------------------------------------------------------------------------------------
["force_knockdown","Force Knockdown", [("_",0),("force_stun_inv", ixmesh_inventory)], itp_type_thrown|itp_unique|itp_two_handed|itp_primary ,itc_force_power, 
	6000 , weight(0.1)|abundance(60)|difficulty(0)|spd_rtng(50) | shoot_speed(5) |thrust_damage(15,blunt)|max_ammo(1)|weapon_length(8),imodbits_none,
	[
		(ti_on_weapon_attack, [
					(
							assign,":distance",99999),
                            #(particle_system_burst, "psys_game_blood", pos1, 45), #SW modified
                            #(particle_system_burst, "psys_game_blood_2", pos1, 45), #SW modified
							(get_player_agent_no, ":player_agent"),
							(try_for_agents,":agent"),
								(agent_is_alive,":agent"),
								(agent_is_human,":agent"),
								(agent_get_look_position, pos2, ":agent"),
								(get_distance_between_positions,":dist",pos1,pos2),
								(lt,":dist",":distance"),
								(assign,":chosen",":agent"),
								(assign,":distance",":dist"),
								(agent_get_team  ,":team", ":chosen"),
							(end_try),
                            (try_for_agents,":agent"),
								(agent_is_alive,":agent"),
								(agent_is_human,":agent"), #SW modified
								(neq, ":agent", ":player_agent"), #SW modified
								(neq,":agent",":chosen"),
								(agent_get_team  ,":team2", ":agent"),
								(neq,":team",":team2"),
								(agent_get_position, pos2, ":agent"),
								(agent_get_position,pos1,":chosen"),
								(get_distance_between_positions,":dist",pos1,pos2),
								(lt,":dist",500),	#SW - increased distance from 350
								#(position_move_z,pos2,150),
								#(particle_system_burst, "psys_game_blood", pos2,95),
								#(particle_system_burst, "psys_game_blood_2", pos2,95),
								#(play_sound,"snd_metal_hit_low_armor_high_damage"),
								#SW - modified to knock down agents
								(agent_play_sound,":player_agent","snd_force_push"),								
								(store_random_in_range, ":rand", 0, 100),
								(try_begin),
									(lt, ":rand", 35),
									#(agent_set_animation, ":agent", "anim_force_crouch"),
									(agent_set_animation, ":agent", "anim_force_push"),
									(agent_set_animation, ":agent", "anim_force_knocked"),
									(store_random_in_range, ":hp_loss", 4, 6),
								(else_try),
									#(agent_set_animation, ":agent", "anim_force_knocked"),
									(agent_set_animation, ":agent", "anim_force_push"),
									(agent_set_animation, ":agent", "anim_force_knocked"),
									(store_random_in_range, ":hp_loss", 6, 10),
								(try_end),								
								(store_agent_hit_points,":hp",":agent",1),
								(val_sub,":hp",":hp_loss"),
								(agent_set_hit_points,":agent",":hp",1),
								(agent_deliver_damage_to_agent,":player_agent",":agent"),
                              (end_try),
					],)]],
#------------------------------------------------------------------------------------------------------------------------------------------
["force_stun","Force Stun", [("_",0),("force_stun_inv", ixmesh_inventory)], itp_type_thrown|itp_unique|itp_two_handed|itp_primary ,itc_force_power, 
	5000 , weight(0.1)|abundance(60)|difficulty(0)|spd_rtng(50) | shoot_speed(5) |thrust_damage(15,blunt)|max_ammo(1)|weapon_length(8),imodbits_none,
	[
		(ti_on_weapon_attack, [
					(
							assign,":distance",99999),
                            #(particle_system_burst, "psys_game_blood", pos1, 45), #SW modified
                            #(particle_system_burst, "psys_game_blood_2", pos1, 45), #SW modified
							(get_player_agent_no, ":player_agent"),
							(try_for_agents,":agent"),
								(agent_is_alive,":agent"),
								(agent_is_human,":agent"),
								(agent_get_look_position, pos2, ":agent"),
								(get_distance_between_positions,":dist",pos1,pos2),
								(lt,":dist",":distance"),
								(assign,":chosen",":agent"),
								(assign,":distance",":dist"),
								(agent_get_team  ,":team", ":chosen"),
							(end_try),
                            (try_for_agents,":agent"),
								(agent_is_alive,":agent"),
								(agent_is_human,":agent"), #SW modified
								(neq, ":agent", ":player_agent"), #SW modified
								(neq,":agent",":chosen"),
								(agent_get_team  ,":team2", ":agent"),
								(neq,":team",":team2"),
								(agent_get_position, pos2, ":agent"),
								(agent_get_position,pos1,":chosen"),
								(get_distance_between_positions,":dist",pos1,pos2),
								(lt,":dist",500),	#SW - increased distance from 350
								#(position_move_z,pos2,150),
								#(particle_system_burst, "psys_game_blood", pos2,95),
								#(particle_system_burst, "psys_game_blood_2", pos2,95),
								#(play_sound,"snd_metal_hit_low_armor_high_damage"),
								#SW - modified to knock down agents
								(agent_play_sound,":player_agent","snd_force_push"),								
								(store_random_in_range, ":rand", 0, 100),
								(try_begin),
									(lt, ":rand", 35),
									(agent_set_animation, ":agent", "anim_force_mini_stun"),
									(store_random_in_range, ":hp_loss", 4, 6),
								(else_try),
									(agent_set_animation, ":agent", "anim_force_stun"),
									(store_random_in_range, ":hp_loss", 6, 10),
								(try_end),								
								(store_agent_hit_points,":hp",":agent",1),
								(val_sub,":hp",":hp_loss"),
								(agent_set_hit_points,":agent",":hp",1),
								(agent_deliver_damage_to_agent,":player_agent",":agent"),
                              (end_try),
					],)]],
#------------------------------------------------------------------------------------------------------------------------------------------
							
# mounts
["horses_begin","<dummy>", [("_",0)], 0,0,0,0,imodbits_none],
# since gallop animation was removed for speeder kaaduu, dewback, and horses are not longer possible
#["kaadu1","Kaadu", [("kaadu_a",0)], itp_merchandise|itp_type_horse, 0, 1000,abundance(110)|hit_points(70)|body_armor(25)|difficulty(2)|horse_speed(42)|horse_maneuver(38)|horse_charge(10),imodbits_horse_basic],
#["kaadu2","Kaadu", [("kaadu_b",0)], itp_merchandise|itp_type_horse, 0, 1000,abundance(110)|hit_points(70)|body_armor(25)|difficulty(2)|horse_speed(42)|horse_maneuver(38)|horse_charge(10),imodbits_horse_basic],
#SW - green lizard (ie. dewback) from Fantasy Mod and courtesy of Highelf
#["dewback","Dewback", [("dewback",0)], itp_merchandise|itp_type_horse, 0, 1200,abundance(110)|hit_points(100)|body_armor(35)|difficulty(2)|horse_speed(38)|horse_maneuver(35)|horse_charge(15),imodbits_horse_basic],
["speeder","Civilian 74-Z Speeder Bike", [("speeder_a",0)],                        itp_merchandise|itp_type_horse, 0, 1000,abundance(100)|hit_points(30)|body_armor(0)|difficulty(0)|horse_speed(65)|horse_maneuver(45)|horse_charge(15),imodbits_speeder_basic],
["speeder_rebel","Military 74-Z Speeder Bike", [("speeder_b",0)],               itp_merchandise|itp_type_horse, 0, 1500,abundance(90)|hit_points(40)|body_armor(10)|difficulty(1)|horse_speed(75)|horse_maneuver(55)|horse_charge(20),imodbits_speeder],
["speeder_imperial","Military Z4-Z Speeder Bike", [("speeder_e",0)],      itp_merchandise|itp_type_horse, 0, 1500,abundance(90)|hit_points(40)|body_armor(10)|difficulty(1)|horse_speed(75)|horse_maneuver(55)|horse_charge(20),imodbits_speeder],
["speeder_hutt","Military Z4-Z Speeder Bike", [("speeder_d",0)],              itp_merchandise|itp_type_horse, 0, 1500,abundance(90)|hit_points(40)|body_armor(10)|difficulty(1)|horse_speed(75)|horse_maneuver(55)|horse_charge(20),imodbits_speeder],
["speeder_shadow","Shadow 74-Z Speeder Bike", [("speeder_c",0)], itp_merchandise|itp_type_horse, 0, 2000,abundance(80)|hit_points(60)|body_armor(30)|difficulty(2)|horse_speed(85)|horse_maneuver(65)|horse_charge(25),imodbits_speeder],
#["swoop_bike","Swoop Bike", [("swoop_bike",0)], itp_merchandise|itp_type_horse, 0, 2500,abundance(100)|hit_points(120)|body_armor(60)|difficulty(2)|horse_speed(65)|horse_maneuver(65)|horse_charge(20),imodbits_speeder],
["speeder_fc20","FC-20 Speeder Bike", [("speeder_fc20",0)], itp_merchandise|itp_type_horse, 0, 2500,abundance(60)|hit_points(60)|body_armor(20)|difficulty(2)|horse_speed(95)|horse_maneuver(80)|horse_charge(15),imodbits_speeder],
["horus_winged_cruiser","Horus Winged Cruiser", [("a_horus",0)], itp_merchandise|itp_type_horse, 0, 2000,abundance(70)|hit_points(65)|body_armor(35)|difficulty(2)|horse_speed(75)|horse_maneuver(60)|horse_charge(30),imodbits_speeder],
#["speeder_sparrow","Sparrow Speeder", [("speeder_sparrow",0),("speeder_sparrow_inv",ixmesh_inventory)], itp_merchandise|itp_type_horse, 0, 2000,abundance(70)|hit_points(60)|body_armor(30)|difficulty(2)|horse_speed(80)|horse_maneuver(60)|horse_charge(25),imodbits_speeder],
#["pod_racer","Pod Racer", [("pod_racer",0)], itp_merchandise|itp_type_horse, 0, 3000,abundance(60)|hit_points(20)|body_armor(0)|difficulty(3)|horse_speed(125)|horse_maneuver(75)|horse_charge(10),imodbits_speeder],
#["swoop_bike","Swoop Bike", [("swoop_bike",0)], itp_merchandise|itp_type_horse, 0, 2500,abundance(60)|hit_points(25)|body_armor(0)|difficulty(3)|horse_speed(115)|horse_maneuver(75)|horse_charge(10),imodbits_speeder],
["speeder_dagger","Bladed 74-Z Speeder Bike", [("speeder_dagger",0)],                        itp_merchandise|itp_type_horse, 0, 2000,abundance(70)|hit_points(45)|body_armor(10)|difficulty(2)|horse_speed(75)|horse_maneuver(65)|horse_charge(35),imodbits_speeder],
#["power_chair","Power Chair", [("power_chair",0)],                        itp_merchandise|itp_type_horse, 0, 500,abundance(50)|hit_points(20)|body_armor(0)|difficulty(0)|horse_speed(45)|horse_maneuver(35)|horse_charge(10),imodbits_speeder_basic],
["horses_end","<dummy>", [("_",0)], 0,0,0,0,imodbits_none],

#practice/training (no merchandise flag)
#["practice_dewback","Dewback", [("dewback",0)], itp_type_horse, 0, 1200,abundance(110)|hit_points(100)|body_armor(35)|difficulty(0)|horse_speed(38)|horse_maneuver(35)|horse_charge(15),imodbits_horse_basic],
["practice_speeder","Civilian 74-Z Speeder Bike", [("speeder_a",0)], itp_unique|itp_type_horse, 0, 1000,abundance(0)|hit_points(30)|body_armor(0)|difficulty(0)|horse_speed(50)|horse_maneuver(45)|horse_charge(15),imodbits_none],
["arena_speeder","Civilian 74-Z Speeder Bike", [("speeder_a",0)],    itp_unique|itp_type_horse, 0, 1000,abundance(0)|hit_points(30)|body_armor(0)|difficulty(0)|horse_speed(50)|horse_maneuver(45)|horse_charge(15),imodbits_none],
#testing
#["rebel_transport","Rebel Transport", [("rebel_transport",0)], itp_merchandise|itp_type_horse, 0, 5,abundance(180)|hit_points(100)|body_armor(35)|difficulty(2)|horse_speed(38)|horse_maneuver(35)|horse_charge(15),imodbits_horse_basic],
#["z95","Z-95 Headhunter", [("z95",0)],                                   itp_type_horse, 0, 4000,abundance(60)|hit_points(200)|body_armor(100)|difficulty(2)|horse_speed(70)|horse_maneuver(60)|horse_charge(80),imodbits_speeder],
#["motor_bike","Motor Bike", [("motor_bike",0)], itp_merchandise|itp_type_horse, 0, 3000,abundance(60)|hit_points(30)|body_armor(0)|difficulty(0)|horse_speed(120)|horse_maneuver(75)|horse_charge(10),imodbits_speeder],


# ["bf2_stormie", "bf2_stormie", [("bf2_stormtrooper_rigged",0)], itp_covers_head|itp_unique|itp_type_body_armor|itp_covers_legs|itp_civilian,0,
  # 3000, weight(55)|abundance(0)|head_armor(30)|body_armor(70)|leg_armor(30)|difficulty(0) ,imodbits_none ],
# ["tfu_stormie", "tfu_stormie", [("tfu_stormtrooper",0)], itp_covers_head|itp_unique|itp_type_body_armor|itp_covers_legs|itp_civilian,0,
  # 3000, weight(55)|abundance(0)|head_armor(30)|body_armor(70)|leg_armor(30)|difficulty(0) ,imodbits_none ],
	#################
	# Autoloot: Need this dummy item here to mark end of file
	#######
	["items_end","<dummy>", [("_",0)], 0,0,0,0,imodbits_none],

]