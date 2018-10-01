# S T A R   W A R S   C O N Q U E S T   M O D U L E   S Y S T E M 
# / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /
# By Taleworlds, HokieBT, MartinF and Swyter - Do not use/copy without permission

from header_common import *
from header_parties import *
from ID_troops import *
from ID_factions import *
from ID_map_icons import *

pmf_is_prisoner = 0x0001

####################################################################################################################
#  Each party template record contains the following fields:
#  1) Party-template id: used for referencing party-templates in other files.
#     The prefix pt_ is automatically added before each party-template id.
#  2) Party-template name.
#  3) Party flags. See header_parties.py for a list of available flags
#  4) Menu. ID of the menu to use when this party is met. The value 0 uses the default party encounter system.
#  5) Faction
#  6) Personality. See header_parties.py for an explanation of personality flags.
#  7) List of stacks. Each stack record is a tuple that contains the following fields:
#    7.1) Troop-id. 
#    7.2) Minimum number of troops in the stack. 
#    7.3) Maximum number of troops in the stack. 
#    7.4) Member flags(optional). Use pmf_is_prisoner to note that this member is a prisoner.
#     Note: There can be at most 6 stacks.
####################################################################################################################


party_templates = [
  ("none","<none>",icon_shuttle,0,fac_commoners,merchant_personality,[]),
  ("rescued_prisoners","Rescued Prisoners",icon_civilian_cruiser,0,fac_commoners,merchant_personality,[]),
  ("enemy","Enemy",icon_mercenary_fighter,0,fac_enemy,merchant_personality,[]),
  ("hero_party","Hero Party",icon_civilian_transport,0,fac_commoners,merchant_personality,[]),
####################################################################################################################
# Party templates before this point are hard-wired into the game and should not be changed. 
####################################################################################################################
##  ("old_garrison","Old Garrison",icon_vaegir_knight,0,fac_neutral,merchant_personality,[]),
  ("minorplanet_defenders","Colonial Defenders",icon_shuttle,0,fac_commoners,merchant_personality,[(trp_farmer,5,10),(trp_civilian,5,10),(trp_peasant_woman,0,4)]),
  ("cattle_herd","Nerf Herd",icon_shuttle|carries_goods(10),0,fac_neutral,merchant_personality,[(trp_cattle,80,120)]),

##  ("vaegir_nobleman","Vaegir Nobleman",icon_vaegir_knight|carries_goods(10)|pf_quest_party,0,fac_commoners,merchant_personality,[(trp_nobleman,1,1),(trp_vaegir_knight,2,6),(trp_vaegir_horseman,4,12)]),
##  ("swadian_nobleman","Swadian Nobleman",icon_gray_knight|carries_goods(10)|pf_quest_party,0,fac_commoners,merchant_personality,[(trp_nobleman,1,1),(trp_swadian_knight,2,6),(trp_swadian_man_at_arms,4,12)]),
# Ryan BEGIN
  #("jawas","Jawas",icon_tusken|carries_goods(8),0,fac_outlaws,bandit_personality,[(trp_jawa,12,24)]),
  ("jawas","Jawas",icon_jawa_ship|carries_goods(8),0,fac_outlaws,bandit_personality,[(trp_jawa,8,16),(trp_jawa_2,5,10),(trp_jawa_3,2,4),(trp_r2series,0,1,pmf_is_prisoner),(trp_3poseries,0,1,pmf_is_prisoner)]),  
  
# Ryan END
#SW - switched bountyhunters to Trandoshan Slavers
##  ("peasant","Peasant",icon_peasant,0,fac_commoners,merchant_personality,[(trp_farmer,1,6),(trp_peasant_woman,0,7)]),
#  ("black_khergit_raiders","Black Khergit Raiders",icon_khergit_horseman_b|carries_goods(2),0,fac_black_khergits,bandit_personality,[(trp_black_khergit_guard,1,10),(trp_black_khergit_horseman,5,5)]),

  ("bountyhunters","Trandoshan Slavers",icon_tran_slaver,0,fac_bountyhunters,soldier_personality,[(trp_bountyhunter,25,50),(trp_wookiee,0,1,pmf_is_prisoner)]),
  ("night_fang_pirates","Night Fangs Pirates",icon_mercenary_shuttle|carries_goods(2),0,fac_outlaws,bandit_personality,[(trp_steppe_bandit,5,25),(trp_steppe_bandit_female,4,8),(trp_trandoshan,1,5),(trp_twilek,1,5),(trp_twilek_female1,0,1,pmf_is_prisoner)]),
  ("blazing_claw_pirates","Blazing Claw Pirates",icon_mercenary_fighter|carries_goods(2),0,fac_blazing_claw_pirates,bandit_personality,[(trp_blazing_claw_pirate,5,25),(trp_blazing_claw_pirate_female,4,8),(trp_rodian,1,5),(trp_sullustan_1,1,5),(trp_twilek_female1,0,1,pmf_is_prisoner)]),
  ("tusken_raiders","Tusken Raiders",icon_mercenary_raider_brown|carries_goods(2),0,fac_outlaws,bandit_personality,[(trp_tusken_1,10,25),(trp_tusken_2,5,10)]),  
  ("black_sun_pirates","Black Sun Pirates",icon_starchaser|carries_goods(2),0,fac_black_sun_pirates,bandit_personality,[(trp_black_sun_pirate_1,10,20),(trp_black_sun_pirate_2,5,10),(trp_black_sun_pirate_3,5,10),(trp_black_sun_pirate_4,2,15),(trp_twilek_female1,0,1,pmf_is_prisoner)]),
  
#SW - new outlaw party templates with Imperial Troops (nevermind, back to regular bandits)
#  ("steppe_bandits","Imperial Scouts",icon_axeman|carries_goods(2),0,fac_outlaws,bandit_personality,[(trp_imperial_stormtrooper_mounted,8,15),(trp_imperial_scout_trooper,10,20)]),
#  ("blazing_claw_pirates","Imperial War Party",icon_axeman|carries_goods(2),0,fac_blazing_claw_pirates,bandit_personality,[(trp_imperial_stormtrooper,20,30),(trp_imperial_scout_trooper,10,15),(trp_sith_apprentice,5,10),(trp_sith_master,5,10)]),
#  ("black_sun_pirates","Imperial Raiders",icon_axeman|carries_goods(2),0,fac_black_sun_pirates,bandit_personality,[(trp_imperial_trooper,5,20),(trp_imperial_recruit,5,30)]),
#  ("tusken_raiders","Imperial Patrol",icon_axeman|carries_goods(2),0,fac_outlaws,bandit_personality,[(trp_imperial_stormtrooper,5,20),(trp_imperial_trooper,5,10),(trp_imperial_scout_trooper,5,10),(trp_sith_apprentice,2,4),(trp_sith_master,2,4)]),

  ("deserters","Deserters",icon_tran_slaver|carries_goods(3),0,fac_deserters,bandit_personality,[]),
 #SW - #MF added some new templates
  ("galacticempire_escort", "Patrol Fleet", icon_tran_slaver|carries_goods(2)|pf_show_faction|pf_default_behavior,0,fac_commoners,aggressiveness_10|courage_12, [(trp_farmer,1,1)]),
  #("independent_traders", "Trade Federation Convoy",icon_bulk_frigate|carries_goods(20)|pf_quest_party,0,fac_commoners,escorted_merchant_personality,[(trp_caravan_master,1,1),(trp_b1series,15,30),(trp_b2series,5,10)]),
  ("independent_traders", "Merchant Convoy",icon_bulk_freighter|carries_goods(20)|pf_quest_party,0,fac_commoners,escorted_merchant_personality,[(trp_caravan_master,1,1),(trp_b1series,1,10),(trp_oom_series_command,1,1),(trp_security_guard,10,20)]),
  #SW - removed pf_auto_remove_in_town
  #("merchant_caravan","Merchant Freighter",icon_freighter|carries_goods(20)|pf_auto_remove_in_town|pf_quest_party,0,fac_commoners,escorted_merchant_personality,[(trp_caravan_master,1,1),(trp_hired_guard,5,25)]),
  ("merchant_caravan","Merchant Freighter",icon_freighter|carries_goods(20)|pf_quest_party,0,fac_commoners,escorted_merchant_personality,[(trp_caravan_master,1,1),(trp_security_guard,15,30)]),  
  ("miningvessel", "Mining Vessel",icon_y8_mining|carries_goods(30)|pf_quest_party,0,fac_commoners,miningvessel_personality,[(trp_asteroid_miner,10,20),(trp_b1series,2,5)]),
  ("troublesome_bandits","Troublesome Bandits",icon_tran_slaver|carries_goods(9)|pf_quest_party,0,fac_outlaws,bandit_personality,[(trp_bandit,15,55)]),
  #SW - removed pf_auto_remove_in_town
  #("bandits_awaiting_ransom","Bandits Awaiting Ransom",icon_axeman|carries_goods(9)|pf_auto_remove_in_town|pf_quest_party,0,fac_neutral,bandit_personality,[(trp_bandit,24,58),(trp_kidnapped_girl,1,1,pmf_is_prisoner)]),
  ("bandits_awaiting_ransom","Bandits Awaiting Ransom",icon_tran_slaver|carries_goods(9)|pf_quest_party,0,fac_neutral,bandit_personality,[(trp_bandit,25,65),(trp_kidnapped_girl,1,1,pmf_is_prisoner)]),  
  ("kidnapped_girl","Kidnapped Girl",icon_shuttle|pf_quest_party,0,fac_neutral,merchant_personality,[(trp_kidnapped_girl,1,1)]),

##  ("farmers","Farmers",icon_peasant,0,fac_innocents,merchant_personality,[(trp_farmer,11,22),(trp_peasant_woman,16,44)]),
  ("minorplanet_farmers","Colonial Farmers",icon_civilian_transport,0,fac_innocents,merchant_personality,[(trp_farmer,6,12),(trp_peasant_woman,4,8)]),
##  ("refugees","Refugees",icon_woman_b,0,fac_innocents,merchant_personality,[(trp_refugee,19,48)]),
##  ("dark_hunters","Dark Hunters",icon_gray_knight,0,fac_dark_knights,soldier_personality,[(trp_dark_knight,4,42),(trp_dark_hunter,13,25)]),

  ("spy_partners", "Unremarkable Travellers", icon_tran_slaver|carries_goods(3)|pf_default_behavior|pf_quest_party,0,fac_neutral,merchant_personality,[(trp_spy_partner,1,1),(trp_security_guard,5,10)]),
  ("runaway_serfs","Runaway Slaves",icon_civilian_cruiser|carries_goods(8)|pf_default_behavior|pf_quest_party,0,fac_neutral,merchant_personality,[(trp_farmer,6,10), (trp_peasant_woman,3,3)]),
  ("spy", "Ordinary Colonist", icon_tran_slaver|carries_goods(3)|pf_default_behavior|pf_quest_party,0,fac_neutral,merchant_personality,[(trp_spy,1,1)]),
  ("sacrificed_messenger", "Sacrificed Messenger", icon_tran_slaver|carries_goods(3)|pf_default_behavior|pf_quest_party,0,fac_neutral,merchant_personality,[]),
##  ("conspirator", "Conspirators", icon_gray_knight|carries_goods(8)|pf_default_behavior|pf_quest_party,0,fac_neutral,merchant_personality,[(trp_conspirator,3,4)]),
##  ("conspirator_leader", "Conspirator Leader", icon_gray_knight|carries_goods(8)|pf_default_behavior|pf_quest_party,0,fac_neutral,merchant_personality,[(trp_conspirator_leader,1,1)]),
##  ("peasant_rebels", "Peasant Rebels", icon_peasant,0,fac_peasant_rebels,bandit_personality,[(trp_peasant_rebel,33,97)]),
##  ("noble_refugees", "Noble Refugees", icon_gray_knight|carries_goods(12)|pf_quest_party,0,fac_noble_refugees,merchant_personality,[(trp_noble_refugee,3,5),(trp_noble_refugee_woman,5,7)]),

  ("forager_party","Foraging Party",icon_tran_slaver|carries_goods(5)|pf_show_faction,0,fac_commoners,merchant_personality,[]),
  ("scout_party","Scouts",icon_tran_slaver|carries_goods(1)|pf_show_faction,0,fac_commoners,bandit_personality,[]),
  ("patrol_party","Patrol",icon_tran_slaver|carries_goods(2)|pf_show_faction,0,fac_commoners,soldier_personality,[]),
#  ("war_party", "War Party",icon_gray_knight|carries_goods(3),0,fac_commoners,soldier_personality,[]),
  ("messenger_party","Messenger",icon_tran_slaver|pf_show_faction,0,fac_commoners,merchant_personality,[]),
  ("raider_party","Raiders",icon_tran_slaver|carries_goods(16)|pf_quest_party,0,fac_commoners,bandit_personality,[]),
  ("raider_captives","Raider Captives",0,0,fac_commoners,0,[(trp_peasant_woman,6,30,pmf_is_prisoner)]),
  ("faction_caravan_party","Freighters",icon_freighter|carries_goods(25)|pf_show_faction,0,fac_commoners,merchant_personality,[(trp_caravan_master,1,1),(trp_security_guard,12,40)]),
  ("prisoner_train_party","Prisoner Train",icon_bulk_freighter|carries_goods(5)|pf_show_faction,0,fac_commoners,merchant_personality,[]),
  ("default_prisoners","Default Prisoners",0,0,fac_commoners,0,[(trp_bandit,5,10,pmf_is_prisoner)]),
##  ("merchant_party","Merchant",icon_mule|carries_goods(25)|pf_show_faction,0,fac_merchants,merchant_personality,[(trp_caravan_guard,12,40)]),
##  ("merchant_party_reinforcement","Merchant Party Reinforcement",icon_mule|carries_goods(25),0,fac_merchants,merchant_personality,[(trp_caravan_guard,6,20)]),

# Caravans

#SW - modified center_reinforcements
  ("center_reinforcements","Reinforcements",icon_tran_slaver|carries_goods(16),0,fac_commoners,soldier_personality,[(trp_townsman,5,15),(trp_civilian,5,15),(trp_farmer,5,15)]),
  
  ("faction_hero_party","War Party",icon_player|pf_show_faction|pf_default_behavior,0,fac_commoners,soldier_personality,[]),
  


# Reinforcements
#  ("default_reinforcements_a","default_reinforcements_a",0,0,fac_commoners,0,[(trp_caravan_guard,1,10),(trp_watchman,3,16),(trp_farmer,9,24)]),
#  ("default_reinforcements_b","default_reinforcements_b",0,0,fac_commoners,0,[(trp_mercenary,1,7),(trp_caravan_guard,3,10),(trp_watchman,3,15)]),
#  ("default_reinforcements_c","default_reinforcements_c",0,0,fac_commoners,0,[(trp_hired_blade,1,7),(trp_mercenary,3,10),(trp_caravan_guard,3,15)]),

#SW - modified faction 1 reinforcements (empire = 6-13 troops)
  ("galacticempire_reinforcements_a", "<galacticempire_reinforcements_a>", 0, 0, fac_commoners, 0, [(trp_imperial_recruit,2,3),(trp_imperial_army_trooper,4,10)]),
  ("galacticempire_reinforcements_b", "<galacticempire_reinforcements_b>", 0, 0, fac_commoners, 0, [(trp_imperial_stormtrooper,6,13)]),
  ("galacticempire_reinforcements_c", "<galacticempire_reinforcements_c>", 0, 0, fac_commoners, 0, [(trp_sith_hopeful,1,2),(trp_chiss_1,1,2),(trp_imperial_stormtrooper,1,2)]),

#SW - modified faction 2 reinforcements (rebel = 5-12 troops)
  ("rebelalliance_reinforcements_a", "<rebelalliance_reinforcements_a>", 0, 0, fac_commoners, 0, [(trp_rebel_recruit,2,3),(trp_rebel_cadet,3,9)]),		#rebels have 1 less for min & max
  ("rebelalliance_reinforcements_b", "<rebelalliance_reinforcements_b>", 0, 0, fac_commoners, 0, [(trp_rebel_trooper,3,8),(trp_wookiee,1,2),(trp_moncal_1,1,2)]),	#rebels have 1 less for min & max
  ("rebelalliance_reinforcements_c", "<rebelalliance_reinforcements_c>", 0, 0, fac_commoners, 0, [(trp_jedi_hopeful,1,2),(trp_sullustan_1,1,2),(trp_bothan,1,2)]),	#rebels are equal for this reinforcement
#SW - modified faction 3 reinforcements (hutt = 5-12 troops)
   ("huttcartel_reinforcements_a", "<huttcartel_reinforcements_a>", 0, 0, fac_commoners, 0, [(trp_hutt_militia,2,3),(trp_hutt_mercenary,2,6),(trp_gamorrean,1,3),(trp_twilek_female1,0,1,pmf_is_prisoner)]),
   ("huttcartel_reinforcements_b", "<huttcartel_reinforcements_b>", 0, 0, fac_commoners, 0, [(trp_hutt_guard,2,5),(trp_trandoshan,1,2),(trp_rodian,1,2),(trp_twilek,1,3),(trp_twilek_female1,0,1,pmf_is_prisoner)]),
   ("huttcartel_reinforcements_c", "<huttcartel_reinforcements_c>", 0, 0, fac_commoners, 0, [(trp_mandalorian,1,1),(trp_gamorrean,1,2),(trp_hutt_skiff_guard,1,1),(trp_ig88,0,1),(trp_rancor,0,1)]),

  #SW - commented out faction 4 & 5 reinforcements  
  # ("faction_4_reinforcements_a", "faction_4_reinforcements_a", 0, 0, fac_commoners, 0, [(trp_nord_footman,2,6),(trp_nord_recruit,4,7)]),
  # ("faction_4_reinforcements_b", "faction_4_reinforcements_b", 0, 0, fac_commoners, 0, [(trp_mercenary_crossbowman,2,4),(trp_nord_footman,4,7)]),
  # ("faction_4_reinforcements_c", "faction_4_reinforcements_c", 0, 0, fac_commoners, 0, [(trp_nord_warrior,3,6)]),

  # ("faction_5_reinforcements_a", "faction_5_reinforcements_a", 0, 0, fac_commoners, 0, [(trp_rhodok_spearman,2,6),(trp_rhodok_tribesman,4,7)]),
  # ("faction_5_reinforcements_b", "faction_5_reinforcements_b", 0, 0, fac_commoners, 0, [(trp_rhodok_trained_crossbowman,2,6),(trp_rhodok_crossbowman,4,7)]),
  # ("faction_5_reinforcements_c", "faction_5_reinforcements_c", 0, 0, fac_commoners, 0, [(trp_rhodok_sergeant,3,6)]),

#SW - Culture specific reinforcements
  ("faction_human_reinforcements_a", "<faction_human_reinforcements_a>", 0, 0, fac_commoners, 0, [(trp_civilian,6,12)]),
  ("faction_human_reinforcements_b", "<faction_human_reinforcements_b>", 0, 0, fac_commoners, 0, [(trp_civilian,3,6),(trp_militia,2,4),(trp_thug,1,2)]),
  ("faction_human_reinforcements_c", "<faction_human_reinforcements_c>", 0, 0, fac_commoners, 0, [(trp_militia,2,4),(trp_thug,2,4)]),  
  ("faction_wookiee_reinforcements_a", "<faction_wookiee_reinforcements_a>", 0, 0, fac_commoners, 0, [(trp_wookiee,6,12)]),
  ("faction_wookiee_reinforcements_b", "<faction_wookiee_reinforcements_b>", 0, 0, fac_commoners, 0, [(trp_wookiee,3,6),(trp_wookiee_warrior,3,6)]),
  ("faction_wookiee_reinforcements_c", "<faction_wookiee_reinforcements_c>", 0, 0, fac_commoners, 0, [(trp_wookiee_marksman,2,4),(trp_wookiee_berserker,2,4)]),
  ("faction_mandalorian_reinforcements_a", "<faction_mandalorian_reinforcements_a>", 0, 0, fac_commoners, 0, [(trp_mandalorian,6,12)]),
  ("faction_mandalorian_reinforcements_b", "<faction_mandalorian_reinforcements_b>", 0, 0, fac_commoners, 0, [(trp_mandalorian,3,6),(trp_mandalorian_soldier,3,6)]),
  ("faction_mandalorian_reinforcements_c", "<faction_mandalorian_reinforcements_c>", 0, 0, fac_commoners, 0, [(trp_mandalorian_commando,2,4),(trp_mandalorian_sniper,2,4)]),  
  ("faction_clone_reinforcements_a", "<faction_clone_reinforcements_a>", 0, 0, fac_commoners, 0, [(trp_clone_trooper_1,6,12)]),
  ("faction_clone_reinforcements_b", "<faction_clone_reinforcements_b>", 0, 0, fac_commoners, 0, [(trp_clone_trooper_2,5,9),(trp_arc_trooper_2,1,3)]),
  ("faction_clone_reinforcements_c", "<faction_clone_reinforcements_c>", 0, 0, fac_commoners, 0, [(trp_clone_trooper_3,3,6),(trp_arc_trooper_3,1,2)]),
  ("faction_trandoshan_reinforcements_a", "<faction_trandoshan_reinforcements_a>", 0, 0, fac_commoners, 0, [(trp_trandoshan,6,12)]),
  ("faction_trandoshan_reinforcements_b", "<faction_trandoshan_reinforcements_b>", 0, 0, fac_commoners, 0, [(trp_trandoshan,3,6),(trp_trandoshan_warrior,3,6)]),
  ("faction_trandoshan_reinforcements_c", "<faction_trandoshan_reinforcements_c>", 0, 0, fac_commoners, 0, [(trp_trandoshan_hunter,2,4),(trp_trandoshan_bounty_hunter,2,4)]),
  ("faction_droid_reinforcements_a", "<faction_clone_reinforcements_a>", 0, 0, fac_commoners, 0, [(trp_oom_series_security,6,12)]),
  ("faction_droid_reinforcements_b", "<faction_clone_reinforcements_b>", 0, 0, fac_commoners, 0, [(trp_oom_series_security,5,9),(trp_oom_series_marine,1,3)]),
  ("faction_droid_reinforcements_c", "<faction_clone_reinforcements_c>", 0, 0, fac_commoners, 0, [(trp_bxseries_commando,3,6),(trp_b2series_enhanced,1,2)]),    
  
##  ("galacticempire_reinforcements_a", "galacticempire_reinforcements_a", 0, 0, fac_commoners, 0, [(trp_swadian_footman,3,7),(trp_swadian_skirmisher,5,10),(trp_swadian_militia,11,26)]),
##  ("galacticempire_reinforcements_b", "galacticempire_reinforcements_b", 0, 0, fac_commoners, 0, [(trp_swadian_man_at_arms,5,10),(trp_swadian_infantry,5,10),(trp_swadian_crossbowman,3,8)]),
##  ("galacticempire_reinforcements_c", "galacticempire_reinforcements_c", 0, 0, fac_commoners, 0, [(trp_swadian_knight,2,6),(trp_swadian_sergeant,2,5),(trp_swadian_sharpshooter,2,5)]),
##
##  ("rebelalliance_reinforcements_a", "rebelalliance_reinforcements_a", 0, 0, fac_commoners, 0, [(trp_vaegir_veteran,3,7),(trp_vaegir_skirmisher,5,10),(trp_vaegir_footman,11,26)]),
##  ("rebelalliance_reinforcements_b", "rebelalliance_reinforcements_b", 0, 0, fac_commoners, 0, [(trp_vaegir_horseman,4,9),(trp_vaegir_infantry,5,10),(trp_vaegir_archer,3,8)]),
##  ("rebelalliance_reinforcements_c", "rebelalliance_reinforcements_c", 0, 0, fac_commoners, 0, [(trp_vaegir_knight,3,7),(trp_vaegir_guard,2,5),(trp_vaegir_marksman,2,5)]),
##
##  ("huttcartel_reinforcements_a", "huttcartel_reinforcements_a", 0, 0, fac_commoners, 0, [(trp_khergit_horseman,3,7),(trp_khergit_skirmisher,5,10),(trp_khergit_tribesman,11,26)]),
##  ("huttcartel_reinforcements_b", "huttcartel_reinforcements_b", 0, 0, fac_commoners, 0, [(trp_khergit_veteran_horse_archer,4,9),(trp_khergit_horse_archer,5,10),(trp_khergit_horseman,3,8)]),
##  ("huttcartel_reinforcements_c", "huttcartel_reinforcements_c", 0, 0, fac_commoners, 0, [(trp_khergit_lancer,3,7),(trp_khergit_veteran_horse_archer,2,5),(trp_khergit_horse_archer,2,5)]),
##
##  ("faction_4_reinforcements_a", "faction_4_reinforcements_a", 0, 0, fac_commoners, 0, [(trp_nord_trained_footman,3,7),(trp_nord_footman,5,10),(trp_nord_recruit,11,26)]),
##  ("faction_4_reinforcements_b", "faction_4_reinforcements_b", 0, 0, fac_commoners, 0, [(trp_nord_veteran,4,9),(trp_nord_warrior,5,10),(trp_nord_footman,3,8)]),
##  ("faction_4_reinforcements_c", "faction_4_reinforcements_c", 0, 0, fac_commoners, 0, [(trp_nord_champion,1,3),(trp_nord_veteran,2,5),(trp_nord_warrior,2,5)]),
##
##  ("faction_5_reinforcements_a", "faction_5_reinforcements_a", 0, 0, fac_commoners, 0, [(trp_rhodok_spearman,3,7),(trp_rhodok_crossbowman,5,10),(trp_rhodok_tribesman,11,26)]),
##  ("faction_5_reinforcements_b", "faction_5_reinforcements_b", 0, 0, fac_commoners, 0, [(trp_rhodok_trained_spearman,4,9),(trp_rhodok_spearman,5,10),(trp_rhodok_crossbowman,3,8)]),
##  ("faction_5_reinforcements_c", "faction_5_reinforcements_c", 0, 0, fac_commoners, 0, [(trp_rhodok_sergeant,3,7),(trp_rhodok_veteran_spearman,2,5),(trp_rhodok_veteran_crossbowman,2,5)]),

("jedi_tests", "Wild Jedi", icon_tran_slaver,0, fac_deserters, soldier_personality, [(trp_jedi_warrior_master, 1,1)]),

] 
