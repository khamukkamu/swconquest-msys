# S T A R   W A R S   C O N Q U E S T   M O D U L E   S Y S T E M 
# / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /
# By Taleworlds, HokieBT, MartinF and Swyter - Do not use/copy without permission

from header_game_menus import *
from header_parties import *
from header_items import *
from header_mission_templates import *
from header_music import *
from header_terrain_types import *
from module_constants import *
#SW - had to add header_terrain_types due to using rt_steppe in lead_charge
from header_terrain_types import *
#SW - had to add head_troops due to switching the star character menu to use the tf_skin flags
#from header_troops import *

####################################################################################################################
#  (menu-id, menu-flags, menu_text, mesh-name, [<operations>], [<options>]),
#
#   Each game menu is a tuple that contains the following fields:
#  
#  1) Game-menu id (string): used for referencing game-menus in other files.
#     The prefix menu_ is automatically added before each game-menu-id
#
#  2) Game-menu flags (int). See header_game_menus.py for a list of available flags.
#     You can also specify menu text color here, with the menu_text_color macro
#  3) Game-menu text (string).
#  4) mesh-name (string). Not currently used. Must be the string "none"
#  5) Operations block (list). A list of operations. See header_operations.py for reference.
#     The operations block is executed when the game menu is activated.
#  6) List of Menu options (List).
#     Each menu-option record is a tuple containing the following fields:
#   6.1) Menu-option-id (string) used for referencing game-menus in other files.
#        The prefix mno_ is automatically added before each menu-option.
#   6.2) Conditions block (list). This must be a valid operation block. See header_operations.py for reference. 
#        The conditions are executed for each menu option to decide whether the option will be shown to the player or not.
#   6.3) Menu-option text (string).
#   6.4) Consequences block (list). This must be a valid operation block. See header_operations.py for reference. 
#        The consequences are executed for the menu option that has been selected by the player.
#
#
# Note: The first Menu is the initial character creation menu.
####################################################################################################################
##
###@> SWY 0.9.0.3 Change color of every menu, from black to HEX 000d2c (dark blue)
##
##  menu_text_color(0xFF000000)  >  menu_text_color(0xFF000d2c)
##
game_menus = [
#This needs to be the first window!!!
  (
    "start_game_1",menu_text_color(0xFF000d2c)|mnf_disable_all_keys,
    #"A long time ago, in a galaxy far, far away...^^Welcome, to Star Wars Calradia, a mod for Mount&Blade.^^Before you can start playing the game you must create a character. To begin, select your character's gender.",
	#"A long time ago, in a galaxy far, far away...^^Welcome, to Star Wars Calradia, a mod for Mount&Blade. Before you can start playing the game you must create a character.^^You were born on the planet Zolan, home to a humanoid species known as Clawdites, but often referred to as Changelings. As one of the few shape-shifting species in the galaxy you can choose what form to begin your adventure as...",
	"A long time ago, in a galaxy far, far away...^^Welcome, to Star Wars: Conquest, a mod for Mount&Blade. Before you can start playing the game you must create a character. Please choose your race:",
    "none",
    [],
#SW BSG integration test
#BSG
    [
	  # ("space_prop_adding",[],"Space Prop Adding",
       # [
           # #(troop_set_type,"trp_player",0),
		   # (troop_set_type,"trp_player_inactive",0),
           # (assign,"$character_gender",0),
           # (modify_visitors_at_site, "scn_space_battle"),
           # #(set_visitor, 0, "trp_player"),  
		   # (set_visitor, 0, "trp_player_inactive"),  
           # (troop_add_item, "trp_player","itm_stun_beam",0),
           # #(troop_equip_items, "trp_player"),
		   # (troop_equip_items, "trp_player_inactive"),
           
           # (set_jump_mission,"mt_space_prop"),
    # #       (jump_to_menu, "mnu_space_battle_end"),
           # (jump_to_scene,"scn_space_battle"),
           # #(change_screen_mission),
		   # (change_screen_mission)],"Door to the tavern."),
        # #]   
       # #),
      # ("space_sim",[],"Space Sim",
       # [         
           # (set_jump_mission,"mt_space_battle"),
    # #       (jump_to_menu, "mnu_space_battle_end"),
           # (jump_to_scene,"scn_space_battle"),
           # #(change_screen_mission),
		   # (change_screen_mission)],"Door to the tavern."),
        # #]   
       # #),		

      # ("space_entry",[],"Space Sim Entry",
       # [         
           # #(set_jump_mission,"mt_space_battle"),
		   # #(set_jump_mission,"mt_town_default"),
		   # (set_jump_mission,"mt_visit_town_castle"),
		   # #(set_jump_mission,"mt_space_prop"),
    # #       (jump_to_menu, "mnu_space_battle_end"),
# #           (jump_to_scene,"scn_space_battle"),
			# (jump_to_scene,"scn_space_battle_entry"),
           # #(change_screen_mission),
		   # (change_screen_mission)],"Door to the tavern."),
		   
        # #]   
       # #),			

############## MF for testing start ####################
("start_mod",[

		#New Cheat protection system by Swyter
		(mouse_get_position, pos2),
		(position_get_y,":y",pos2),
		(le,":y",1),

],"Quick Character (for mod testing)",
      #("start_mod",[(eq,1,1),],"Quick Character (for mod testing)",
        [
            (troop_set_type,"trp_player",0),
            (assign,"$character_gender",tf_male),
			(assign, "$cheat_mode", 1),
	 (troop_raise_attribute, "trp_player",ca_intelligence,-60), #so you dont need to wait time picking extra skills   
     (troop_clear_inventory, "trp_player"),
     (troop_raise_attribute, "trp_player", ca_strength, -100),
     (troop_raise_attribute, "trp_player", ca_agility, -100),
     (troop_raise_attribute, "trp_player", ca_charisma, -100),
     (troop_raise_attribute, "trp_player", ca_intelligence, -100),
     (troop_raise_skill, "trp_player", skl_shield, -100),
     (troop_raise_skill, "trp_player", skl_athletics, -100),
     (troop_raise_skill, "trp_player", skl_riding, -100),
     (troop_raise_skill, "trp_player", skl_power_strike, -100),
     (troop_raise_skill, "trp_player", skl_power_throw, -100),
     (troop_raise_skill, "trp_player", skl_weapon_master, -100),
     (troop_raise_skill, "trp_player", skl_horse_archery, -100),
     (troop_raise_skill, "trp_player", skl_ironflesh, -100),
     (troop_raise_proficiency_linear, "trp_player", wpt_one_handed_weapon, -100),
     (troop_raise_proficiency_linear, "trp_player", wpt_two_handed_weapon, -100),
     (troop_raise_proficiency_linear, "trp_player", wpt_polearm, -100),
     (troop_raise_proficiency_linear, "trp_player", wpt_archery, -100),
     (troop_raise_proficiency_linear, "trp_player", wpt_crossbow, -100),
     (troop_raise_proficiency_linear, "trp_player", wpt_throwing, -100),
	#SW - added firearm proficiency
     (troop_raise_proficiency_linear, "trp_player", wpt_firearm, -100),	 	
	 
			(change_screen_map),			
            (change_screen_return, 0),
       ]
	 ),
############## MF for testing end ####################   

	   
#---------------------------------------------------------------

      ("race_male",[],"Human Male",
       [
           (troop_set_type,"trp_player",tf_male),
           (assign,"$character_gender",tf_male),
           (jump_to_menu,"mnu_start_character_0"),
        ]
       ),
      ("race_female",[],"Human Female",
       [
           (troop_set_type,"trp_player",tf_female),
           (assign,"$character_gender",tf_female),
           (jump_to_menu,"mnu_start_character_0")
        ]
       ),
	   #------------------------------------------------------
	   #SW - new races	   
      ("race_twilek",[],"Twilek Male",
       [
           (troop_set_type,"trp_player",tf_twilek),
           (assign,"$character_gender",tf_male),
           (jump_to_menu,"mnu_start_character_0"),
        ]
       ),
      ("race_twilek_female",[],"Twilek Female",
       [
           (troop_set_type,"trp_player",tf_twilek_female),
           (assign,"$character_gender",tf_female),
           (jump_to_menu,"mnu_start_character_0"),
        ]
       ),	   
      ("race_rodian",[],"Rodian",
       [
           (troop_set_type,"trp_player",tf_rodian),
           (assign,"$character_gender",tf_male),
           (jump_to_menu,"mnu_start_character_0"),
        ]
       ),
      ("race_moncal",[],"Mon Calamari",
       [
           (troop_set_type,"trp_player",tf_moncal),
           (assign,"$character_gender",tf_male),
           (jump_to_menu,"mnu_start_character_0"),
        ]
       ),
      ("race_trandoshan",[],"Trandoshan",
       [
           (troop_set_type,"trp_player",tf_trandoshan),
           (assign,"$character_gender",tf_male),
           (jump_to_menu,"mnu_start_character_0"),
        ]
       ),
      ("race_droid",[],"Droid",
       [
           (troop_set_type,"trp_player",tf_droid),
           (assign,"$character_gender",tf_male),
           (jump_to_menu,"mnu_start_character_0"),
        ]
       ),
      # ("start_weequay",[],"Weequay",
       # [
           # (troop_set_type,"trp_player",tf_weequay),
           # (assign,"$character_gender",tf_male),
           # (jump_to_menu,"mnu_start_character_0"),
        # ]
       # ),	   
      ("race_wookiee",[],"Wookiee",
       [
           (troop_set_type,"trp_player",tf_wookiee),
           (assign,"$character_gender",tf_male),
           (jump_to_menu,"mnu_start_character_0"),
        ]
       ),
      ("race_sullustan",[],"Sullustan",
       [
           (troop_set_type,"trp_player",tf_sullustan),
           (assign,"$character_gender",tf_male),
           (jump_to_menu,"mnu_start_character_0"),
        ]
       ),
      # ("start_chiss_female",[],"Chiss Female",
       # [
           # (troop_set_type,"trp_player",tf_chiss_female),
           # (assign,"$character_gender",tf_female),
           # (jump_to_menu,"mnu_start_character_0"),
        # ]
       # ),	   
      ("race_gamorrean",[],"Gamorrean",
       [
           (troop_set_type,"trp_player",tf_gamorrean),
           (assign,"$character_gender",tf_male),
           (jump_to_menu,"mnu_start_character_0"),
        ]
       ),
      ("race_bothan",[],"Bothan",
       [
           (troop_set_type,"trp_player",tf_bothan),
           (assign,"$character_gender",tf_male),
           (jump_to_menu,"mnu_start_character_0"),
        ]
       ),
      ("race_geonosian",[],"Geonosian",
       [
           (troop_set_type,"trp_player",tf_geonosian),
           (assign,"$character_gender",tf_male),
           (jump_to_menu,"mnu_start_character_0"),
        ]
       ),
      # ("start_clone",[],"Jango Fett Clone",
       # [
           # (troop_set_type,"trp_player",tf_clone),
           # (assign,"$character_gender",tf_male),
           # (jump_to_menu,"mnu_start_character_0"),
        # ]
       # ),	   
       ("race_jawa",[],"Jawa",
       [
           (troop_set_type,"trp_player",tf_jawa),
           (assign,"$character_gender",tf_male),
           (jump_to_menu,"mnu_start_character_0"),
        ]
       ),
      ("race_tusken",[],"Tusken",
       [
           (troop_set_type,"trp_player",tf_tusken),
           (assign,"$character_gender",tf_male),
           (jump_to_menu,"mnu_start_character_0"),
        ]
       ),	   
	   #------------------------------------------------------	   	   
      ("go_back",[],"Go back",
       [(change_screen_quit),
        ]
       ),

      ]
  ),
#This needs to be the second window!!!
  (
    "start_phase_2",menu_text_color(0xFF000d2c)|mnf_disable_all_keys,
#    "During your travels, you come accross a group of wandering men looking for a leader. You...",
#
    # "You arrive at Calradia, a land torn between rival factions battling each other for supremacy,\
 # a haven for knights and mercenaries, cutthroats and adventurers, all willing to risk their lives in pursuit of fortune, power, or glory...\
 # In this land which holds great dangers and even greater opportunities, you will leave your past behind and start a new life.\
 # Now, on a rise above a distant training field, you feel that you hold the key of your destiny in your hands, free to choose as you will,\
 # and that whatever course you take, great adventures await you.",
   "It is a period of civil war... The Galactic Empire is in constant battle with the Rebel Alliance while the Hutt Cartel looks for opportunities to make money and expand their area of rule.  Whatever course you take a great adventure awaits you.", 
    "none",
    [],
    [
      ("continue_3dot",[],"Continue...",
       [
         (call_script, "script_get_player_party_morale_values"),
         (party_set_morale, "p_main_party", reg0),
         (change_screen_return),
        ]
       ),
##      ("lead_them",[],"...convince them to follow you, promising riches and glory.",
##       [
##           (party_add_members, "p_main_party", "trp_civilian", 5),
##           (change_screen_return),
##        ]
##       ),
##      ("let_them_go",[],"...wish them good luck and go the other way.",
##       [
##           (change_screen_return),
##        ]
##       ),
	  #SW - tutorial_cheat
      ("tutorial_cheat",[		
	    #New Cheat protection system by Swyter
		(mouse_get_position, pos2),
		(position_get_y,":y",pos2),
		(le,":y",1),],"CHEAT!",  #disabled menu
	  #("tutorial_cheat",[(eq,1,1)],"CHEAT!", #enabled
       [
         (change_screen_return),
         (assign, "$cheat_mode", 1),
         (set_show_messages, 0),
         (add_xp_to_troop, 15000, "trp_player"),
         (troop_raise_skill, "trp_player", skl_leadership, 7),
         (troop_raise_skill, "trp_player", skl_prisoner_management, 5),
		 #SW - modified cheat menu to have generic troops
         (party_add_members, "p_main_party", "trp_security_guard", 10),
         (party_add_members, "p_main_party", "trp_security_guard", 10),
         (party_add_members, "p_main_party", "trp_security_guard", 10),
         (party_add_members, "p_main_party", "trp_security_guard", 10),

		 #SW - commented out extra items, added vibro_blade and lightsaber
         (troop_add_item, "trp_player","itm_vibro_blade3",0),
         (troop_add_item, "trp_player","itm_lightsaber_yellow",0),
		 
         # (troop_add_item, "trp_player","itm_pike",0),
         # (troop_add_item, "trp_player","itm_light_crossbow",0),
         # (troop_add_item, "trp_player","itm_tab_shield_pavise_a",0),
         # (troop_add_item, "trp_player","itm_heavy_crossbow",0),
         # (troop_add_item, "trp_player","itm_tribal_warrior_outfit",0),
         
         # (troop_add_item, "trp_player","itm_sword_two_handed_a",0),
         # (troop_add_item, "trp_player","itm_sword_two_handed_a",0),
         # (troop_add_item, "trp_player","itm_sword_two_handed_b",0),

         # (troop_add_item, "trp_player","itm_arena_armor_white",0),
         # (troop_add_item, "trp_player","itm_arena_armor_red",0),
         # (troop_add_item, "trp_player","itm_arena_armor_green",0),        
         # (troop_add_item, "trp_player","itm_arena_armor_blue",0),
         # (troop_add_item, "trp_player","itm_arena_armor_yellow",0),

         # (troop_add_item, "trp_player","itm_mace_1",0),
         # (troop_add_item, "trp_player","itm_mace_2",0),
         # (troop_add_item, "trp_player","itm_mace_3",0),
         # (troop_add_item, "trp_player","itm_mace_4",0),
         # (troop_add_item, "trp_player","itm_club_with_spike_head",0),

         # (troop_add_item, "trp_player","itm_great_axe",0),
         # (troop_add_item, "trp_player","itm_shortened_military_scythe",0),

         # (troop_add_item, "trp_player","itm_bastard_sword_a",0),
         # (troop_add_item, "trp_player","itm_bastard_sword_b",0),
         # (troop_add_item, "trp_player","itm_tab_shield_small_round_a",0),
         # (troop_add_item, "trp_player","itm_tab_shield_small_round_b",0),
                 
         # (troop_add_item, "trp_player","itm_heraldic_mail_with_surcoat",0),
         # (troop_add_item, "trp_player","itm_sword_khergit_1",0),
         # (troop_add_item, "trp_player","itm_sword_khergit_2",0),
         # (troop_add_item, "trp_player","itm_sword_khergit_3",0),
         # (troop_add_item, "trp_player","itm_sword_khergit_4",0),
 
         # (troop_add_item, "trp_player","itm_arena_shield_red",0),
         # (troop_add_item, "trp_player","itm_arena_shield_yellow",0),
         # (troop_add_item, "trp_player","itm_arena_shield_blue",0),
         # (troop_add_item, "trp_player","itm_arena_shield_green",0),
          
         # (troop_add_item, "trp_player","itm_tourney_helm_yellow",0),
         # (troop_add_item, "trp_player","itm_tourney_helm_white",0),
         # (troop_add_item, "trp_player","itm_tourney_helm_red",0),
         # (troop_add_item, "trp_player","itm_tourney_helm_green",0),
         # (troop_add_item, "trp_player","itm_tourney_helm_blue",0),
          

         # (troop_add_item, "trp_player","itm_steppe_helmet_white",0),       
         # (troop_add_item, "trp_player","itm_steppe_helmet_red",0),
         # (troop_add_item, "trp_player","itm_steppe_helmet_green",0),
         # (troop_add_item, "trp_player","itm_steppe_helmet_blue",0),
         # (troop_add_item, "trp_player","itm_steppe_helmet_yellow",0), 

         # (troop_add_item, "trp_player","itm_arena_tunic_white",0),
         # (troop_add_item, "trp_player","itm_arena_tunic_red",0),
         # (troop_add_item, "trp_player","itm_arena_tunic_green",0),        
         # (troop_add_item, "trp_player","itm_arena_tunic_blue",0),
         # (troop_add_item, "trp_player","itm_arena_tunic_yellow",0),
                 
         (set_show_messages, 1),

         (try_for_range, ":cur_place", scenes_begin, scenes_end),
           (scene_set_slot, ":cur_place", slot_scene_visited, 1),
         (try_end),
         (call_script, "script_get_player_party_morale_values"),
         (party_set_morale, "p_main_party", reg0),
         ]),
    ]
  ),
# This needs to be the third window!!!  
  (
    "start_game_3",menu_text_color(0xFF000d2c)|mnf_disable_all_keys,
    "Choose your scenario:",
    "none",
    [
      #Default banners
      (troop_set_slot, "trp_banner_background_color_array", 126, 0xFF212221),
      (troop_set_slot, "trp_banner_background_color_array", 127, 0xFF212221),
      (troop_set_slot, "trp_banner_background_color_array", 128, 0xFF2E3B10),
      (troop_set_slot, "trp_banner_background_color_array", 129, 0xFF425D7B),
      (troop_set_slot, "trp_banner_background_color_array", 130, 0xFF394608),
      ],
    [
	  #SW - modified custom battle name
	  #("custom_battle_scenario_1",[], "Defend the village from Imperials",
##      ("custom_battle_scenario_2",[],"Siege Attack 1",
##       [
##           (assign, "$g_custom_battle_scenario", 1),
##           (jump_to_menu, "mnu_custom_battle_2"),
##
##        ]
##       ),
	  #SW - modified custom battle name	   
       ("custom_battle_scenario_4",[],"Tusken Raider Attack",
       [
           (assign, "$g_custom_battle_scenario", 2),
           (jump_to_menu, "mnu_custom_battle_2"),
        ]
       ),
	  #SW - modified custom battle name	   
      ("custom_battle_scenario_6",[],"Attack on the Yavin IV Shrine",
       [
           (assign, "$g_custom_battle_scenario", 4),
           (jump_to_menu, "mnu_custom_battle_2"),

        ]
       ),
	  #SW - modified custom battle name	   
       ("custom_battle_scenario_8",[],"Assault the Imperial Spaceship",
       [
           (assign, "$g_custom_battle_scenario", 8),
           (jump_to_menu, "mnu_custom_battle_2"),
        ]
       ),	 
	  #SW - added menu for custom battle mod
	  ("custom_battle",[],"Start a Custom Battle",
	   [
		  (assign, "$g_custom_battle_location", 0),
		  (jump_to_menu, "mnu_custom_battle_config_1"),
	   ]
	  ),
	 # Quick Scene Chooser integration - http://forums.taleworlds.net/index.php/topic,51851.0.html
	("choose_scene",[
		#New Cheat protection system by Swyter
		(mouse_get_position, pos2),
		(position_get_y,":y",pos2),
		(le,":y",1),],
	
	"Scene Chooser (for development use)",
		[(jump_to_menu, "mnu_choose_scenes_0"),]
	),
	# End of Quick Scene Chooser
      ("go_back",[],"Go back",
       [(change_screen_quit),
        ]
       ),
    ]
  ),

# This needs to be the fourth window!!!
  (
    "tutorial",menu_text_color(0xFF000d2c)|mnf_disable_all_keys,
    "You approach a field where the locals are training with weapons. The distant twang of laser blasters coupled with the metallic clashes of vibroblades can be heard. You can practice here to improve your combat skills.",
    "none",
    [(set_passage_menu, "mnu_tutorial"),
     (try_begin),
       (eq, "$tutorial_1_finished", 1),
       (str_store_string, s1, "str_finished"),
     (else_try),
       (str_store_string, s1, "str_empty_string"),
     (try_end),
     (try_begin),
       (eq, "$tutorial_2_finished", 1),
       (str_store_string, s2, "str_finished"),
     (else_try),
       (str_store_string, s2, "str_empty_string"),
     (try_end),
     (try_begin),
       (eq, "$tutorial_3_finished", 1),
       (str_store_string, s3, "str_finished"),
     (else_try),
       (str_store_string, s3, "str_empty_string"),
     (try_end),
     (try_begin),
       (eq, "$tutorial_4_finished", 1),
       (str_store_string, s4, "str_finished"),
     (else_try),
       (str_store_string, s4, "str_empty_string"),
     (try_end),
     (try_begin),
       (eq, "$tutorial_5_finished", 1),
       (str_store_string, s5, "str_finished"),
     (else_try),
       (str_store_string, s5, "str_empty_string"),
     (try_end),
        ],
    [
      ("tutorial_1",[],"Tutorial #1: Basic movement and weapon selection. {s1}",[
           (modify_visitors_at_site,"scn_tutorial_1"),(reset_visitors,0),
           (set_jump_mission,"mt_tutorial_1"),
           (jump_to_scene,"scn_tutorial_1"),(change_screen_mission)]),
      ("tutorial_2",[],"Tutorial #2: Fighting with a shield. {s2}",[
           (modify_visitors_at_site,"scn_tutorial_2"),(reset_visitors,0),
           (set_visitor,1,"trp_tutorial_maceman"),
           (set_visitor,2,"trp_tutorial_archer"),
           (set_jump_mission,"mt_tutorial_2"),
           (jump_to_scene,"scn_tutorial_2"),(change_screen_mission)]),
      ("tutorial_3",[],"Tutorial #3: Fighting without a shield. {s3}",[
           (modify_visitors_at_site,"scn_tutorial_3"),(reset_visitors,0),
           (set_visitor,1,"trp_tutorial_maceman"),
           (set_visitor,2,"trp_tutorial_swordsman"),
           (set_jump_mission,"mt_tutorial_3"),
           (jump_to_scene,"scn_tutorial_3"),(change_screen_mission)]),
      ("tutorial_3b",[(eq,0,1)],"Tutorial 3 b",[(try_begin),
                                                  (ge, "$tutorial_3_state", 12),
                                                  (modify_visitors_at_site,"scn_tutorial_3"),(reset_visitors,0),
                                                  (set_visitor,1,"trp_tutorial_maceman"),
                                                  (set_visitor,2,"trp_tutorial_swordsman"),
                                                  (set_jump_mission,"mt_tutorial_3_2"),
                                                  (jump_to_scene,"scn_tutorial_3"),
                                                  (change_screen_mission),
                                                (else_try),
                                                  (display_message,"str_door_locked",0xFFFFAAAA),
                                                (try_end)], "next level"),
      #SW - modified tutorial_4 name
	  ("tutorial_4",[],"Tutorial #4: Riding a speeder bike. {s4}",[
           (modify_visitors_at_site,"scn_tutorial_4"),(reset_visitors,0),
           (set_jump_mission,"mt_tutorial_4"),
           (jump_to_scene,"scn_tutorial_4"),(change_screen_mission)]),
      ("tutorial_5",[(eq,1,0)],"Tutorial #5: Commanding a band of soldiers. {s5}",[
           (modify_visitors_at_site,"scn_tutorial_5"),(reset_visitors,0),
           (set_visitor,0,"trp_player"),
		   #SW - modified troops
           (set_visitor,1,"trp_security_guard"),
           (set_visitor,2,"trp_security_guard"),
           (set_visitor,3,"trp_security_guard"),
           (set_visitor,4,"trp_security_guard"),
           (set_jump_mission,"mt_tutorial_5"),
           (jump_to_scene,"scn_tutorial_5"),(change_screen_mission)]),

      ("go_back_dot",[],"Go back.",
       [(change_screen_quit),
        ]
       ),
    ]
  ),

# This needs to be the fifth window!!!  
  ("reports",menu_text_color(0xFF000d2c),
   "Character Renown: {reg5}^Honor Rating: {reg6}^Party Morale: {reg8}^Party Size Limit: {reg7}^",
   "none",
   [(call_script, "script_game_get_party_companion_limit"),
    (assign, ":party_size_limit", reg0),
    (troop_get_slot, ":renown", "trp_player", slot_troop_renown),
    (assign, reg5, ":renown"),
    (assign, reg6, "$player_honor"),
    (assign, reg7, ":party_size_limit"),
    (party_get_morale, reg8, "p_main_party"),
   ],
    [
      ("cheat_faction_orders",[(eq,"$cheat_mode",1)],"Cheat: Faction orders.",
       [(jump_to_menu, "mnu_faction_orders"),
        ]
       ),
      ("view_faction_troop_trees",[],"Review Troop Trees.",
       [(start_presentation, "prsnt_troop_tree"),
        ]
       ),
      ("view_character_report",[],"View character report.",
       [(jump_to_menu, "mnu_character_report"),
        ]
       ),
      ("view_party_size_report",[],"View party size report.",
       [(jump_to_menu, "mnu_party_size_report"),
        ]
       ),
      ("view_morale_report",[],"View party morale report.",
       [(jump_to_menu, "mnu_morale_report"),
        ]
       ),
#NPC companion changes begin
##      ("view_party_preferences",[],"View party management preferences.",
##       [(jump_to_menu, "mnu_party_preferences"),
##        ]
##       ),

      ("view_npc_status",[(eq,"$cheat_mode",1)],"NPC status check.",
       [
        (try_for_range, ":npc", companions_begin, companions_end),
            (main_party_has_troop, ":npc"),
            (str_store_troop_name, 4, ":npc"),
            (troop_get_slot, reg3, ":npc", slot_troop_morality_state),
            (troop_get_slot, reg4, ":npc", slot_troop_2ary_morality_state),
            (troop_get_slot, reg5, ":npc", slot_troop_personalityclash_state),    
            (troop_get_slot, reg6, ":npc", slot_troop_personalityclash2_state),    
            (troop_get_slot, reg7, ":npc", slot_troop_personalitymatch_state),    
            (display_message, "@{s4}: M{reg3}, 2M{reg4}, PC{reg5}, 2PC{reg6}, PM{reg7}"),
        (try_end),
        ]
       ),
#NPC companion changes end

#SW - integration companions_overview 
#########JEDEDIAH Q START ######################################################
     ("Companions_overview",[],"Companions overview.",
      [
	(assign, "$jq_in_market_menu", 0), # player is not in market menu
#Exit if no companions 
	(assign, ":heroes_in_party", 0),
	(try_for_range, reg3, companions_begin, companions_end),
   	(main_party_has_troop, reg3),
	(val_add, ":heroes_in_party", 1),
	 (try_end),
	#(display_message, "@ {reg3}"),
	    (try_begin),
	 	(eq, ":heroes_in_party", 0),
		(display_message,"@No companions in party!",0xFFFF0000),
	(else_try),
	(start_presentation, "prsnt_jq_companions_quickview"),
     	(try_end),
       ]
     ),
#########JEDEDIAH Q END #############################################

      ("view_faction_relations_report",[],"View faction relations report.",
       [(jump_to_menu, "mnu_faction_relations_report"),
        ]
       ),
      ("resume_travelling",[],"Resume travelling.",
       [(change_screen_return),
        ]
       ),
      ]
  ),
  
  (
    #SW - Modified many things about the Quick Battles (items, troops, player stats, etc)  
    "custom_battle_2",menu_text_color(0xFF000d2c)|mnf_disable_all_keys,
    "{s16}",
    "none",
    [
     (assign, "$g_battle_result", 0),
     (set_show_messages, 0),

     (troop_clear_inventory, "trp_player"),
     (troop_raise_attribute, "trp_player", ca_strength, -1000),
     (troop_raise_attribute, "trp_player", ca_agility, -1000),
     (troop_raise_attribute, "trp_player", ca_charisma, -1000),
     (troop_raise_attribute, "trp_player", ca_intelligence, -1000),
     (troop_raise_skill, "trp_player", skl_shield, -1000),
     (troop_raise_skill, "trp_player", skl_athletics, -1000),
     (troop_raise_skill, "trp_player", skl_riding, -1000),
     (troop_raise_skill, "trp_player", skl_power_strike, -1000),
     (troop_raise_skill, "trp_player", skl_power_throw, -1000),
     (troop_raise_skill, "trp_player", skl_weapon_master, -1000),
     (troop_raise_skill, "trp_player", skl_horse_archery, -1000),
     (troop_raise_skill, "trp_player", skl_ironflesh, -1000),
     (troop_raise_proficiency_linear, "trp_player", wpt_one_handed_weapon, -10000),
     (troop_raise_proficiency_linear, "trp_player", wpt_two_handed_weapon, -10000),
     (troop_raise_proficiency_linear, "trp_player", wpt_polearm, -10000),
     (troop_raise_proficiency_linear, "trp_player", wpt_archery, -10000),
     (troop_raise_proficiency_linear, "trp_player", wpt_crossbow, -10000),
     (troop_raise_proficiency_linear, "trp_player", wpt_throwing, -10000),
	#SW - added firearm proficiency
     (troop_raise_proficiency_linear, "trp_player", wpt_firearm, -10000),	 	 

     (reset_visitors),
##   Scene 1 Start "Shalow Lake War"
     (try_begin), #--> Tusken Raider Attack
       (eq, "$g_custom_battle_scenario", 2),
       (assign, "$g_player_troop", "trp_quick_battle_player"),
       (set_player_troop, "$g_player_troop"),
     
       (troop_raise_attribute, "$g_player_troop", ca_strength, 12),
       (troop_raise_attribute, "$g_player_troop", ca_agility, 9),
       (troop_raise_attribute, "$g_player_troop", ca_charisma, 5),
       (troop_raise_attribute, "$g_player_troop", ca_intelligence, 5),
       (troop_raise_skill, "$g_player_troop", skl_shield, 3),
       (troop_raise_skill, "$g_player_troop", skl_athletics, 2),
       (troop_raise_skill, "$g_player_troop", skl_riding, 3),
       (troop_raise_skill, "$g_player_troop", skl_power_strike, 4),
       (troop_raise_skill, "$g_player_troop", skl_power_draw, 5),
       (troop_raise_skill, "$g_player_troop", skl_weapon_master, 4),    
       (troop_raise_skill, "$g_player_troop", skl_ironflesh, 6),
       (troop_raise_proficiency_linear, "$g_player_troop", wpt_one_handed_weapon, 200),
	     (troop_raise_proficiency_linear, "$g_player_troop", wpt_two_handed_weapon, 200),
       (troop_raise_proficiency_linear, "$g_player_troop", wpt_polearm, 20),
       (troop_raise_proficiency_linear, "$g_player_troop", wpt_crossbow, 200),
       (troop_raise_proficiency_linear, "$g_player_troop", wpt_throwing, 10),
	     (troop_raise_proficiency_linear, "$g_player_troop", wpt_archery, 10),
       #SW - added firearm proficiency to quick battles
	     (troop_raise_proficiency_linear, "$g_player_troop", wpt_firearm, 200),
	   
       (assign, "$g_custom_battle_scene", "scn_quick_battle_4"),
       (modify_visitors_at_site, "$g_custom_battle_scene"),
       (set_visitor, 0, "$g_player_troop"),
     
       (troop_clear_inventory, "$g_player_troop"),
	     #SW - modified items for quick battles
       (troop_add_item, "trp_player","itm_leather_boots",0),
       (troop_add_item, "trp_player","itm_quick_battle_armor",0),
       (troop_add_item, "trp_player","itm_leather_gloves",0),
       (troop_add_item, "trp_player","itm_lightsaber_blue",0),
       (troop_add_item, "trp_player","itm_laser_bolts_yellow_rifle",0),
       (troop_add_item, "trp_player","itm_a295",0),
       (troop_add_item, "trp_player","itm_energy_shield_yellow_medium",0),	   
       (troop_equip_items, "$g_player_troop"),
## US     
       (set_visitors, 1, "trp_quick_battle_farmer", 10),
       (set_visitors, 2, "trp_quick_battle_farmer", 7),
       (set_visitors, 3, "trp_quick_battle_farmer", 4),
       (set_visitors, 4, "trp_quick_battle_farmer", 10),
       (set_visitors, 5, "trp_quick_battle_farmer", 4),
       (set_visitors, 6, "trp_quick_battle_farmer", 7),
       (set_visitors, 7, "trp_quick_battle_farmer", 5),
       (set_visitors, 8, "trp_quick_battle_farmer", 5),

## ENEMY
       (set_visitors, 16, "trp_tusken_1", 15*.7),
       (set_visitors, 17, "trp_tusken_1", 25*.6),
       (set_visitors, 18, "trp_tusken_1", 15*.7),
       (set_visitors, 19, "trp_tusken_1", 25*.6),
       (set_visitors, 20, "trp_tusken_1", 20*.7),
       (str_store_string, s16, "str_custom_battle_3"),
	   
##   Scene 5 START
     (else_try),  #--> Attack on the Yavin IV Shrine
       (eq, "$g_custom_battle_scenario", 4),

##       (assign, "$g_custom_battle_scene", "scn_quick_battle_6"),
       (assign, "$g_custom_battle_scene", "scn_quick_battle_7"),
     
#   Player Wear
       (assign, "$g_player_troop", "trp_quick_battle_player"),
       (set_player_troop, "$g_player_troop"),
     
       (modify_visitors_at_site, "$g_custom_battle_scene"),
       (set_visitor, 0, "$g_player_troop"),

       (set_visitors, 1, "trp_imperial_stormtrooper_officer", 6),
       (set_visitors, 2, "trp_imperial_stormtrooper", 8),
       (set_visitors, 3, "trp_imperial_stormtrooper", 8),
       (set_visitors, 4, "trp_imperial_scout_trooper", 6),
       (set_visitors, 5, "trp_sith_knight", 2),
       (set_visitors, 6, "trp_imperial_stormtrooper", 8),

## ENEMY
       (set_visitors, 11, "trp_rebel_trooper", 2),
       (set_visitors, 12, "trp_rebel_trooper", 3),
       (set_visitors, 13, "trp_rebel_trooper", 4),
       (set_visitors, 14, "trp_rebel_commando", 5),
       (set_visitors, 16, "trp_jedi_guardian", 2),
       (set_visitors, 17, "trp_rebel_honor_guard", 4),
       (set_visitors, 18, "trp_rebel_commando", 2),
       (set_visitors, 19, "trp_rebel_trooper", 4),
       (set_visitors, 20, "trp_rebel_trooper", 3),
       (set_visitors, 21, "trp_rebel_commando", 3),
       (set_visitors, 22, "trp_rebel_trooper", 3),
       (set_visitors, 23, "trp_rebel_trooper", 4),
       (str_store_string, s16, "str_custom_battle_5"),

     (else_try),  #--> Assault the Imperial Spaceship
       (eq, "$g_custom_battle_scenario", 8),
       (assign, "$g_player_troop", "trp_quick_battle_player"),
       (set_player_troop, "$g_player_troop"),
     
       (troop_raise_attribute, "$g_player_troop", ca_strength, 12),
       (troop_raise_attribute, "$g_player_troop", ca_agility, 9),
       (troop_raise_attribute, "$g_player_troop", ca_charisma, 5),
       (troop_raise_attribute, "$g_player_troop", ca_intelligence, 5),
       (troop_raise_skill, "$g_player_troop", skl_shield, 3),
       (troop_raise_skill, "$g_player_troop", skl_athletics, 2),
       (troop_raise_skill, "$g_player_troop", skl_riding, 3),
       (troop_raise_skill, "$g_player_troop", skl_power_strike, 4),
       (troop_raise_skill, "$g_player_troop", skl_power_draw, 5),
       (troop_raise_skill, "$g_player_troop", skl_weapon_master, 4),    
       (troop_raise_skill, "$g_player_troop", skl_ironflesh, 6),
       (troop_raise_proficiency_linear, "$g_player_troop", wpt_one_handed_weapon, 200),
       (troop_raise_proficiency_linear, "$g_player_troop", wpt_two_handed_weapon, 200),
       (troop_raise_proficiency_linear, "$g_player_troop", wpt_polearm, 20),
       (troop_raise_proficiency_linear, "$g_player_troop", wpt_crossbow, 200),
       (troop_raise_proficiency_linear, "$g_player_troop", wpt_throwing, 10),
	     (troop_raise_proficiency_linear, "$g_player_troop", wpt_archery, 10),
		  #SW - added firearm proficiency to quick battles
       (troop_raise_proficiency_linear, "$g_player_troop", wpt_firearm, 200),
	   
       (assign, "$g_custom_battle_scene", "scn_quick_battle_8"),
       (modify_visitors_at_site, "$g_custom_battle_scene"),
       (set_visitor, 0, "$g_player_troop"),
     
       (troop_clear_inventory, "$g_player_troop"),
	   #SW - modified items for quick battles
       (troop_add_item, "trp_player","itm_laser_bolts_orange_pistol",0),
       (troop_add_item, "trp_player","itm_han_solo_blaster",0),
       (troop_add_item, "trp_player","itm_energy_shield_yellow_medium",0),	  
       
       (troop_equip_items, "$g_player_troop"),
## US     
       (set_visitors, 1, "trp_rebel_commando", 6),
## ENEMY
       (set_visitors, 2, "trp_imperial_stormtrooper_officer", 2),
       (set_visitors, 3, "trp_imperial_stormtrooper", 2),
       (set_visitors, 4, "trp_imperial_stormtrooper", 2),
       (set_visitors, 5, "trp_imperial_stormtrooper", 1),
       (set_visitors, 6, "trp_imperial_stormtrooper", 1),
       (set_visitors, 7, "trp_imperial_stormtrooper", 4),
       (set_visitors, 8, "trp_imperial_stormtrooper", 1),
       (set_visitors, 9, "trp_imperial_stormtrooper", 4),
       (set_visitors, 10, "trp_imperial_stormtrooper", 5),
       (set_visitors, 11, "trp_imperial_stormtrooper", 6),
       (set_visitors, 12, "trp_imperial_stormtrooper", 1),
       (set_visitors, 13, "trp_imperial_stormtrooper", 3),
       (set_visitors, 14, "trp_imperial_stormtrooper", 3),
       (set_visitors, 15, "trp_imperial_stormtrooper", 3),
       (set_visitors, 16, "trp_imperial_stormtrooper", 2),
       (set_visitors, 17, "trp_imperial_stormtrooper", 2),
       (set_visitors, 18, "trp_imperial_stormtrooper", 1),
       (set_visitors, 19, "trp_imperial_stormtrooper", 1),
       (set_visitors, 20, "trp_imperial_stormtrooper_officer", 4),
       (set_visitors, 21, "trp_imperial_stormtrooper", 4),
       (str_store_string, s16, "str_custom_battle_8"),
     (try_end),
     (set_show_messages, 1),
     ],
    
    [
      ("custom_battle_go",[],"Start.",
       [(try_begin),
          (eq, "$g_custom_battle_scenario", 2),
          (set_jump_mission,"mt_custom_battle_siege"),
	      (else_try),
          (eq, "$g_custom_battle_scenario", 8),
          (set_jump_mission,"mt_custom_battle_siege_8"),	  
        (else_try),
          (eq, "$g_custom_battle_scenario", 4),
          (set_jump_mission,"mt_custom_battle_5"),
        (else_try),
          (set_jump_mission,"mt_custom_battle"),
        (try_end),
        (jump_to_menu, "mnu_custom_battle_end"),
        (jump_to_scene,"$g_custom_battle_scene"),
        (change_screen_mission),
        ]
       ),
      ("cancel_dot",[],"Cancel.",
       [(jump_to_menu, "mnu_start_game_3"),
        ]
       ),
    ]
  ),


  (
    "custom_battle_end",menu_text_color(0xFF000d2c)|mnf_disable_all_keys,
    "The battle is over. {s1} Your side killed {reg5} enemies and lost {reg6} troops over the battle. You personally slew {reg7} adversaries in the fighting.",
    "none",
    [(music_set_situation, 0),
     (assign, reg5, "$g_custom_battle_team2_death_count"),
     (assign, reg6, "$g_custom_battle_team1_death_count"),
     (get_player_agent_kill_count, ":kill_count"),
     (get_player_agent_kill_count, ":wound_count", 1),
     (store_add, reg7, ":kill_count", ":wound_count"),
     (try_begin),
       (eq, "$g_battle_result", 1),
       (str_store_string, s1, "str_battle_won"),
     (else_try),
       (str_store_string, s1, "str_battle_lost"),
     (try_end),],
    [
      ("continue_dot",[],"Continue.",
       [(change_screen_quit),
        ]
       ),
    ]
  ),
#-------------------------------------------------------------------------------------------------
#SW - new quick start menu
  (
    "start_character_0",menu_text_color(0xFF000d2c)|mnf_disable_all_keys,
    "You spent your early years traveling around the galaxy with your parents. Your father was...",
    "none",
    [
	#(start_presentation, "prsnt_class_selection"),
    (str_clear,s10),
    (str_clear,s11),
    (str_clear,s12),
    (str_clear,s13),
    (str_clear,s14),
    (str_clear,s15),
    ],
    [
    ("start_quick_ambassador",[],"A ambassador.",[
      (assign,"$background_type",cb0_ambassador),
      (assign, reg3, "$character_gender"),
      #(str_store_string,s10,"@string not used"),
	  #(str_store_string,s13,"@You decide it is now time to leave your family and seek you own fortune."),
	(jump_to_menu,"mnu_start_character_faction"),
    ]),
    ("start_quick_merchant",[],"A merchant.",[
      (assign,"$background_type",cb0_merchant),
      (assign, reg3, "$character_gender"),
      #(str_store_string,s10,"@string not used"),
	  #(str_store_string,s13,"@You decide it is now time to leave your family and seek you own fortune."),	  
	(jump_to_menu,"mnu_start_character_faction"),
    ]),
    ("start_quick_soldier",[],"A soldier.",[
      (assign,"$background_type",cb0_soldier),
      (assign, reg3, "$character_gender"),
      #(str_store_string,s10,"@string not used"),
	  #(str_store_string,s13,"@You decide it is now time to leave your family and seek you own fortune."),	  
	(jump_to_menu,"mnu_start_character_faction"),
    ]),
    ("start_quick_smuggler",[],"A smuggler.",[
      (assign,"$background_type",cb0_smuggler),
      (assign, reg3, "$character_gender"),
      #(str_store_string,s10,"@string not used"),
	  #(str_store_string,s13,"@You decide it is now time to leave your family and seek you own fortune."),	  
	(jump_to_menu,"mnu_start_character_faction"),
    ]),
    ("start_quick_hunter",[],"A bounty hunter.",[
      (assign,"$background_type",cb0_hunter),
      (assign, reg3, "$character_gender"),
      #(str_store_string,s10,"@string not used"),
	  #(str_store_string,s13,"@You decide it is now time to leave your family and seek you own fortune."),	  
	(jump_to_menu,"mnu_start_character_faction"),
    ]),
    ("start_quick_forcesensitive",[],"A force-sensitive warrior.",[
      (assign,"$background_type",cb0_forcesensitive),
      (assign, reg3, "$character_gender"),
      #(str_store_string,s10,"@string not used"),
	  #(str_store_string,s13,"@You decide it is now time to leave your family and seek you own fortune."),	  
	(jump_to_menu,"mnu_start_character_faction"),
    ]),
    ("go_back",[],"Go back",
     [(jump_to_menu,"mnu_start_game_1"),
    ]),
    ]
  ),

#------------------------------------------------------------------------------------------------
  (
    "start_character_faction",menu_text_color(0xFF000d2c)|mnf_disable_all_keys,
    "As you grew older you decided to...",
    "none",
    [
    #(str_clear,s10),
    #(str_clear,s11),
    #(str_clear,s12),
    #(str_clear,s13),
    #(str_clear,s14),
    #(str_clear,s15),
	(start_presentation, "prsnt_faction_selection"),
    ],
    [
    ("start_quick_faction1",[],"Join the Galactic Empire.",[
	  (str_store_string,s13,"@After visiting the recruiting center you were accepted into the army and spent several months training at the Imperial Academy. As your last task before graduation you were given a small ship and sent to Coruscant to pledge your loyalty before Emperor Palpatine himself."),
      (assign,"$faction_choice",cb0_empire),		
	(jump_to_menu,"mnu_choose_skill"),
    ]),
    ("start_quick_faction2",[],"Join the Rebel Alliance.",[
	  (str_store_string,s13,"@Using some of your local contacts you eventually arranged a meeting with a rebel commander. After working with his unit for several months you have been given a small ship and sent to Yavin IV to pledge your loyalty before Mon Mothma herself."),
      (assign,"$faction_choice",cb0_rebel),
	(jump_to_menu,"mnu_choose_skill"),
    ]),
    ("start_quick_faction3",[],"Join the Hutt Cartel.",[
	  (str_store_string,s13,"@You spent several months doing random jobs for the local crime lord. Thievery and murder became a common part of your life and you developed enough of a reputation that you were given a small ship and sent to Tatooine to pledge your loyalty before Jabba the Hutt."),	  
      (assign,"$faction_choice",cb0_hutt),	  
	(jump_to_menu,"mnu_choose_skill"),
    ]),
    ("start_quick_other",[],"Remain Independent.",[
	  (str_store_string,s13,"@You decide it is now time to leave your family and seek you own fortune."),
      (assign,"$faction_choice",cb0_independent),	  	  
	(jump_to_menu,"mnu_choose_skill"),
    ]),
    ("go_back",[],"Go back",
     [(jump_to_menu,"mnu_start_character_0"),
    ]),
    ]
  ),
  
#-------------------------------------------------------------------------------------------------
  # (
    # "start_character_1",menu_text_color(0xFF000d2c)|mnf_disable_all_keys,
    # "You were born a long time ago, in a galaxy far, far away. Your father was...",
    # "none",
    # [
    # (str_clear,s10),
    # (str_clear,s11),
    # (str_clear,s12),
    # (str_clear,s13),
    # (str_clear,s14),
    # (str_clear,s15),
    # ],
    # [
    # ("start_noble",[],"An impoverished ambassador.",[
      # (assign,"$background_type",cb_noble),
      # (assign, reg3, "$character_gender"),
      # (str_store_string,s10,"@You came into the world a {reg3?daughter:son} of declining nobility,\
 # owning only the house in which they lived. However, despite your family's hardships,\
 # they afforded you a good education and trained you from childhood for the rigors of aristocracy and life at court."),
	# (jump_to_menu,"mnu_start_character_2"),
    # ]),
    # ("start_merchant",[],"A travelling merchant.",[
      # (assign,"$background_type",cb_merchant),
      # (assign, reg3, "$character_gender"),
      # (str_store_string,s10,"@You were born the {reg3?daughter:son} of travelling merchants,\
 # always moving from place to place in search of a profit. Although your parents were wealthier than most\
 # and educated you as well as they could, you found little opportunity to make friends on the road,\
 # living mostly for the moments when you could sell something to somebody."),
	# (jump_to_menu,"mnu_start_character_2"),
    # ]),
    # ("start_guard",[],"A veteran soldier.",[
      # (assign,"$background_type",cb_guard),
      # (assign, reg3, "$character_gender"),
      # (str_store_string,s10,"@As a child, your family scrabbled out a meagre living from your father's wages\
 # as a guardsman to the local garrison. It was not an easy existence, and you were too poor to get much of an\
 # education. You learned mainly how to defend yourself on the streets, with or without a weapon in hand."),
	# (jump_to_menu,"mnu_start_character_2"),
    # ]),
    # # ("start_forester",[],"A hunter.",[
      # # (assign,"$background_type",cb_forester),
      # # (assign, reg3, "$character_gender"),
      # # (str_store_string,s11,"@{reg3?daughter:son}"),
      # # (str_store_string,s10,"@You were the {reg3?daughter:son} of a family who lived off the woods,\
 # # doing whatever they needed to make ends meet. Hunting, woodcutting, making arrows,\
 # # even a spot of poaching whenever things got tight. Winter was never a good time for your family\
 # # as the cold took animals and people alike, but you always lived to see another dawn,\
 # # though your brothers and sisters might not be so fortunate."),
	# # (jump_to_menu,"mnu_start_character_2"),
    # # ]),
    # # ("start_nomad",[],"A steppe nomad.",[
      # # (assign,"$background_type",cb_nomad),
      # # (assign, reg3, "$character_gender"),
      # # (str_store_string,s11,"@{reg3?daughter:son}"),
      # # (str_store_string,s10,"@You were a child of the steppe, born to a tribe of wandering nomads who lived\
 # # in great camps throughout the arid grasslands.\
 # # Like the other tribesmen, your family revered horses above almost everything else, and they taught you\
 # # how to ride almost before you learned how to walk. "),
	# # (jump_to_menu,"mnu_start_character_2"),
    # # ]),
    # ("start_thief",[],"A smuggler.",[
      # (assign,"$background_type",cb_thief),
      # (assign, reg3, "$character_gender"),
      # (str_store_string,s10,"@As the {reg3?daughter:son} of a smuggler, you had very little 'formal' education.\
 # Instead you were out on the street, begging until you learned how to cut purses, cutting purses\
 # until you learned how to pick locks, all the way through your childhood.\
 # Still, these long years made you streetwise and sharp to the secrets of cities and shadowy backways."),
	# (jump_to_menu,"mnu_start_character_2"),
    # ]),
# ##    ("start_priest",[],"Priests.",[
# ##      (assign,"$background_type",cb_priest),
# ##      (assign, reg3, "$character_gender"),
# ##      (str_store_string,s10,"@A {reg3?daughter:son} that nobody wanted, you were left to the church as a baby,\
# ## a foundling raised by the priests and nuns to their own traditions.\
# ## You were only one of many other foundlings and orphans, but you nonetheless received a lot of attention\
# ## as well as many years of study in the church library and before the altar. They taught you many things.\
# ## Gradually, faith became such a part of your life that it was no different from the blood coursing through your veins."),
# ##	(jump_to_menu,"mnu_start_character_2"),
# ##    ]),
    # ("go_back",[],"Go back",
     # [(jump_to_menu,"mnu_start_game_1"),
    # ]),
    # ]
  # ),
  # (
    # "start_character_2",menu_text_color(0xFF000d2c),
    # "{s10}^^ You started to learn about the world almost as soon as you could walk and talk. You spent your early life as...",
    # "none",
    # [],
    # [
      # ("page",[
          # ],"A page at a nobleman's court.",[
      # (assign,"$background_answer_2", cb2_page),
      # (assign, reg3, "$character_gender"),
      # (str_store_string,s11,"@As a {reg3?girl:boy} growing out of childhood,\
 # you were sent to live in the court of one of the nobles of the land.\
 # There, your first lessons were in humility, as you waited upon the lords and ladies of the household.\
 # But from their chess games, their gossip, even the poetry of great deeds and courtly love, you quickly began to learn about the adult world of conflict\
 # and competition. You also learned from the rough games of the other children, who battered at each other with sticks in imitation of their elders' swords."),
	# (jump_to_menu,"mnu_start_character_3"),
    # ]),
      # ("apprentice",[
          # ],"A craftsman's apprentice.",[
      # (assign,"$background_answer_2", cb2_apprentice),
      # (assign, reg3, "$character_gender"),
      # (str_store_string,s11,"@As a {reg3?girl:boy} growing out of childhood,\
 # you apprenticed with a local craftsman to learn a trade. After years of hard work and study under your\
 # new master, he promoted you to journeyman and employed you as a fully paid craftsman for as long as\
 # you wished to stay."),
	# (jump_to_menu,"mnu_start_character_3"),
    # ]),
      # ("stockboy",[
          # ],"A shop assistant.",[
      # (assign,"$background_answer_2",cb2_merchants_helper),
      # (assign, reg3, "$character_gender"),
      # (str_store_string,s11,"@As a {reg3?girl:boy} growing out of childhood,\
 # you apprenticed to a wealthy merchant, picking up the trade over years of working shops and driving caravans.\
 # You soon became adept at the art of buying low, selling high, and leaving the customer thinking they'd\
 # got the better deal."),
	# (jump_to_menu,"mnu_start_character_3"),
    # ]),
      # ("urchin",[
          # ],"A street urchin.",[
      # (assign,"$background_answer_2",cb2_urchin),
      # (assign, reg3, "$character_gender"),
      # (str_store_string,s11,"@As a {reg3?girl:boy} growing out of childhood,\
 # you took to the streets, doing whatever you must to survive.\
 # Begging, thieving and working for gangs to earn your bread, you lived from day to day in this violent world,\
 # always one step ahead of the law and those who wished you ill."),
	# (jump_to_menu,"mnu_start_character_3"),
    # ]),
      # # ("nomad",[
          # # ],"A steppe child.",[
      # # (assign,"$background_answer_2",cb2_steppe_child),
      # # (assign, reg3, "$character_gender"),
      # # (str_store_string,s11,"@As a {reg3?girl:boy} growing out of childhood,\
 # # you rode the great steppes on a horse of your own, learning the ways of the grass and the desert.\
 # # Although you sometimes went hungry, you became a skillful hunter and pathfinder in this trackless country.\
 # # Your body too started to harden with muscle as you grew into the life of a nomad {reg3?woman:man}."),
	# # (jump_to_menu,"mnu_start_character_3"),
    # # ]),
      
# ##      ("mummer",[],"Mummer.",[
# ##      (assign,"$background_answer_2",5),
# ##      (assign, reg3, "$character_gender"),
# ##      (str_store_string,s13,"@{reg3?woman:man}"),
# ##      (str_store_string,s12,"@{reg3?girl:boy}"),
# ##      (str_store_string,s11,"@As a {s12} growing out of childhood,\
# ## you attached yourself to a troupe of wandering entertainers, going from town to town setting up mummer's\
# ## shows. It was a life of hard work, selling, begging and stealing your living from the punters who flocked\
# ## to watch your antics. Over time you became a performer well capable of attracting a crowd."),
# ##	(jump_to_menu,"mnu_start_character_3"),
# ##    ]),
# ##      ("courtier",[],"Courtier.",[
# ##      (assign,"$background_answer_2",6),
# ##      (assign, reg3, "$character_gender"),
# ##      (str_store_string,s13,"@{reg3?woman:man}"),
# ##      (str_store_string,s12,"@{reg3?girl:boy}"),
# ##      (str_store_string,s11,"@As a {s12} growing out of childhood,\
# ## you spent much of your life at court, inserting yourself into the tightly-knit circles of nobility.\
# ## With the years you became more and more involved with the politics and intrigue demanded of a high-born {s13}.\
# ## You could not afford to remain a stranger to backstabbing and political violence, even if you wanted to."),
# ##	(jump_to_menu,"mnu_start_character_3"),
# ##    ]),
# ##      ("noble",[],"Noble in training.",[
# ##      (assign,"$background_answer_2",7),
# ##      (assign, reg3, "$character_gender"),
# ##      (str_store_string,s13,"@{reg3?woman:man}"),
# ##      (str_store_string,s12,"@{reg3?girl:boy}"),
# ##      (try_begin),
# ##      (eq,"$character_gender",tf_male),
# ##      (str_store_string,s11,"@As a {s12} growing out of childhood,\
# ## you were trained and educated to perform the duties and wield the rights of a noble landowner.\
# ## The managing of taxes and rents were equally important in your education as diplomacy and even\
# ## personal defence. You learned everything you needed to become a lord of your own hall."),
# ##      (else_try),
# ##      (str_store_string,s11,"@As a {s12} growing out of childhood,\
# ## you were trained and educated to the duties of a noble {s13}. You learned much about the household arts,\
# ## but even more about diplomacy and decorum, and all the things that a future husband might choose to speak of.\
# ## Truly, you became every inch as shrewd as any lord, though it would be rude to admit it aloud."),
# ##      (try_end),
# ##	(jump_to_menu,"mnu_start_character_3"),
# ##    ]),
# ##      ("acolyte",[],"Cleric acolyte.",[
# ##    (assign,"$background_answer_2",8),
# ##      (assign, reg3, "$character_gender"),
# ##      (str_store_string,s13,"@{reg3?woman:man}"),
# ##      (str_store_string,s12,"@{reg3?girl:boy}"),
# ##      (str_store_string,s11,"@As a {s12} growing out of childhood,\
# ## you became an acolyte in the church, the lowest rank on the way to priesthood.\
# ## Years of rigorous learning and hard work followed. You were one of several acolytes,\
# ## performing most of the menial labour in the church in addition to being trained for more holy tasks.\
# ## On the night of your adulthood you were allowed to conduct your first service.\
# ## After that you were no longer an acolyte {s12}, but a {s13} waiting to take your vows into the service of God."),
# ##	(jump_to_menu,"mnu_start_character_3"),
# ##    ]),
      # ("go_back",[],"Go back.",
     # [(jump_to_menu,"mnu_start_character_1"),
    # ]),
    # ]
  # ),
  # (
    # "start_character_3",menu_text_color(0xFF000d2c)|mnf_disable_all_keys,
    # "{s11}^^ Then, as a young adult, life changed as it always does. You became...",
    # "none",
    # [(assign, reg3, "$character_gender"),],
    # [
# ##      ("bravo",[],"A travelling bravo.",[
# ##        (assign,"$background_answer_3",1),
# ##      (str_store_string,s14,"@{reg3?daughter:man}"),
# ##      (str_store_string,s13,"@{reg3?woman:man}"),
# ##      (str_store_string,s12,"@Though the distinction felt sudden to you,\
# ## somewhere along the way you had become a {s13}, and the whole world seemed to change around you.\
# ## You left your old life behind to travel the roads as a mercenary, a bravo, guarding caravans for coppers\
# ## or bashing in heads for silvers. You became a {s14} of the open road, working with bandits as often as against.\
# ## Going from fight to fight, you grew experienced at battle, and you learned what it was to kill."),
# ##	(jump_to_menu,"mnu_start_character_4"),
# ##        ]),
# ##      ("merc",[],"A sellsword in foreign lands.",[
# ##        (assign,"$background_answer_3",2),
# ##      (str_store_string,s14,"@{reg3?daughter:man}"),
# ##      (str_store_string,s13,"@{reg3?woman:man}"),
# ##      (str_store_string,s12,"@Though the distinction felt sudden to you,\
# ## somewhere along the way you had become a {s13}, and the whole world seemed to change around you.\
# ## You signed on with a mercenary company and travelled far from your home. The life you found was rough and\
# ## ready, marching to the beat of strange drums and learning unusual ways of fighting.\
# ## There were men who taught you how to wield any weapon you desired, and plenty of battles to hone your skills.\
# ## You were one of the charmed few who survived through every campaign in which you marched."),
# ##	(jump_to_menu,"mnu_start_character_4"),
# ##        ]),

      # ("squire",[(eq,"$character_gender",tf_male)],"A squire.",[
        # (assign,"$background_answer_3",cb3_squire),
      # (str_store_string,s14,"@{reg3?daughter:man}"),
      # (str_store_string,s12,"@Though the distinction felt sudden to you,\
 # somewhere along the way you had become a {reg3?woman:man}, and the whole world seemed to change around you.\
 # When you were named squire to a noble at court, you practiced long hours with weapons,\
 # learning how to deal out hard knocks and how to take them, too.\
 # You were instructed in your obligations to your lord, and of your duties to those who might one day be your vassals.\
 # But in addition to learning the chivalric ideal, you also learned about the less uplifting side\
 # -- old warriors' stories of ruthless power politics, of betrayals and usurpations,\
 # of men who used guile as well as valor to achieve their aims."),
	# (jump_to_menu,"mnu_start_character_4"),
        # ]),
      # ("lady",[(eq,"$character_gender",tf_female)],"A lady-in-waiting.",[
        # (assign,"$background_answer_3",cb3_lady_in_waiting),
      # (str_store_string,s14,"@{reg3?daughter:man}"),
      # (str_store_string,s13,"@{reg3?woman:man}"),
      # (str_store_string,s12,"@Though the distinction felt sudden to you,\
 # somewhere along the way you had become a {s13}, and the whole world seemed to change around you.\
 # You joined the tightly-knit circle of women at court, ladies who all did proper ladylike things,\
 # the wives and mistresses of noble men as well as maidens who had yet to find a husband.\
 # However, even here you found politics at work as the ladies schemed for prominence and fought each other\
 # bitterly to catch the eye of whatever unmarried man was in fashion at court.\
 # You soon learned ways of turning these situations and goings-on to your advantage. With it came the\
 # realisation that you yourself could wield great influence in the world, if only you applied yourself\
 # with a little bit of subtlety."),
	# (jump_to_menu,"mnu_start_character_4"),
        # ]),
      # ("troubadour",[],"A troubadour.",[
        # (assign,"$background_answer_3",cb3_troubadour),
      # (str_store_string,s14,"@{reg3?daughter:man}"),
      # (str_store_string,s13,"@{reg3?woman:man}"),
      # (str_store_string,s12,"@Though the distinction felt sudden to you,\
 # somewhere along the way you had become a {s13}, and the whole world seemed to change around you.\
 # You set out on your own with nothing except the instrument slung over your back and your own voice.\
 # It was a poor existence, with many a hungry night when people failed to appreciate your play,\
 # but you managed to survive on your music alone. As the years went by you became adept at playing the\
 # drunken crowds in your cantinas, and even better at talking anyone out of anything you wanted."),
	# (jump_to_menu,"mnu_start_character_4"),
        # ]),
      # ("student",[],"A university student.",[
        # (assign,"$background_answer_3",cb3_student),
      # (str_store_string,s12,"@Though the distinction felt sudden to you,\
 # somewhere along the way you had become a {reg3?woman:man}, and the whole world seemed to change around you.\
 # You found yourself as a student in the university of one of the great cities,\
 # where you studied theology, philosophy, and medicine.\
 # But not all your lessons were learned in the lecture halls.\
 # You may or may not have joined in with your fellows as they roamed the alleys in search of wine, women, and a good fight.\
 # However, you certainly were able to observe how a broken jaw is set,\
 # or how an angry townsman can be persuaded to set down his club and accept cash compensation for the destruction of his shop."),
	# (jump_to_menu,"mnu_start_character_4"),
        # ]),
      # ("peddler",[],"A goods peddler.",[
        # (assign,"$background_answer_3",cb3_peddler),
      # (str_store_string,s14,"@{reg3?daughter:man}"),
      # (str_store_string,s13,"@{reg3?woman:man}"),
      # (str_store_string,s12,"@Though the distinction felt sudden to you,\
 # somewhere along the way you had become a {s13}, and the whole world seemed to change around you.\
 # Heeding the call of the open road, you travelled from planet to planet buying and selling what you could.\
 # It was not a rich existence, but you became a master at haggling even the most miserly elders into\
 # giving you a good price. Soon, you knew, you would be well-placed to start your own trading empire..."),
	# (jump_to_menu,"mnu_start_character_4"),
        # ]),
      # ("craftsman",[],"A smith.",[
        # (assign,"$background_answer_3", cb3_craftsman),
      # (str_store_string,s14,"@{reg3?daughter:man}"),
      # (str_store_string,s13,"@{reg3?woman:man}"),
      # (str_store_string,s12,"@Though the distinction felt sudden to you,\
 # somewhere along the way you had become a {s13}, and the whole world seemed to change around you.\
 # You pursued a career as a smith, crafting items of function and beauty out of simple metal.\
 # As time wore on you became a master of your trade, and fine work started to fetch fine prices.\
 # With food in your belly and logs on your fire, you could take pride in your work and your growing reputation."),
	# (jump_to_menu,"mnu_start_character_4"),
        # ]),
      # ("poacher",[],"A game poacher.",[
        # (assign,"$background_answer_3", cb3_poacher),
      # (str_store_string,s14,"@{reg3?daughter:man}"),
      # (str_store_string,s13,"@{reg3?woman:man}"),
      # (str_store_string,s12,"@Though the distinction felt sudden to you,\
 # somewhere along the way you had become a {s13}, and the whole world seemed to change around you.\
 # Dissatisfied with common men's desperate scrabble for coin, you took to your local lord's own forests\
 # and decided to help yourself to its bounty, laws be damned. You hunted stags, boars and geese and sold\
 # the precious meat under the table. You cut down trees right under the watchmen's noses and turned them into\
 # firewood that warmed many freezing homes during winter. All for a few silvers, of course."),
	# (jump_to_menu,"mnu_start_character_4"),
        # ]),
# ##      ("preacher",[],"Itinerant preacher.",[
# ##        (assign,"$background_answer_3",6),
# ##      (str_store_string,s14,"@{reg3?daughter:man}"),
# ##      (str_store_string,s13,"@{reg3?woman:man}"),
# ##      (str_store_string,s12,"@Though the distinction felt sudden to you,\
# ## somewhere along the way you had become a {s13}, and the whole world seemed to change around you.\
# ## You packed your few belongings and went out into the world to spread the word of God. You preached to\
# ## anyone who would listen, and impressed many with the passion of your sermons. Though you had taken a vow\
# ## to remain in poverty through your itinerant years, you never lacked for food, drink or shelter; the\
# ## hospitality of the peasantry was always generous to a rising {s13} of God."),
# ##	(jump_to_menu,"mnu_start_character_4"),
# ##        ]),
      # ("go_back",[],"Go back.",
       # [(jump_to_menu,"mnu_start_character_2"),
        # ]
       # ),
    # ]
  # ),

  # (
    # "start_character_4",menu_text_color(0xFF000d2c)|mnf_disable_all_keys,
    # "{s12}^^But soon everything changed and you decided to strike out on your own as an adventurer. What made you take this decision was...",
    # #Finally, what made you decide to strike out on your own as an adventurer?",
    # "none",
    # [],
    # [
      # ("revenge",[],"Personal revenge.",[
        # (assign,"$background_answer_4", cb4_revenge),
      # (str_store_string,s13,"@Only you know exactly what caused you to give up your old life and become an adventurer.\
 # Still, it was not a difficult choice to leave, with the rage burning brightly in your heart.\
 # You want vengeance. You want justice. What was done to you cannot be undone,\
 # and these debts can only be paid in blood..."),
        # (jump_to_menu,"mnu_choose_skill"),
        # ]),
      # ("death",[],"The loss of a loved one.",[
        # (assign,"$background_answer_4",cb4_loss),
      # (str_store_string,s13,"@Only you know exactly what caused you to give up your old life and become an adventurer.\
 # All you can say is that you couldn't bear to stay, not with the memories of those you loved so close and so\
 # painful. Perhaps your new life will let you forget,\
 # or honour the name that you can no longer bear to speak..."),
        # (jump_to_menu,"mnu_choose_skill"),
        # ]),
      # ("wanderlust",[],"Wanderlust.",[
        # (assign,"$background_answer_4",cb4_wanderlust),
      # (str_store_string,s13,"@Only you know exactly what caused you to give up your old life and become an adventurer.\
 # You're not even sure when your home became a prison, when the familiar became mundane, but your dreams of\
 # wandering have taken over your life. Whether you yearn for some faraway place or merely for the open road and the\
 # freedom to travel, you could no longer bear to stay in the same place. You simply went and never looked back..."),
        # (jump_to_menu,"mnu_choose_skill"),
        # ]),
# ##      ("fervor",[],"Religious fervor.",[
# ##        (assign,"$background_answer_4",4),
# ##      (str_store_string,s13,"@Only you know exactly what caused you to give up your old life and become an adventurer.\
# ## Regardless, the intense faith burning in your soul would not let you find peace in any single place.\
# ## There were others in the world, souls to be washed in the light of God. Now you preach wherever you go,\
# ## seeking to bring salvation and revelation to the masses, be they faithful or pagan. They will all know the\
# ## glory of God by the time you're done..."),
# ##        (jump_to_menu,"mnu_choose_skill"),
# ##        ]),
      # ("disown",[],"Being forced out of your home.",[
        # (assign,"$background_answer_4",cb4_disown),
      # (str_store_string,s13,"@Only you know exactly what caused you to give up your old life and become an adventurer.\
 # However, you know you cannot go back. There's nothing to go back to. Whatever home you may have had is gone\
 # now, and you must face the fact that you're out in the wide wide world. Alone to sink or swim..."),
        # (jump_to_menu,"mnu_choose_skill"),
        # ]),
     # ("greed",[],"Lust for money and power.",[
        # (assign,"$background_answer_4",cb4_greed),
      # (str_store_string,s13,"@Only you know exactly what caused you to give up your old life and become an adventurer.\
 # To everyone else, it's clear that you're now motivated solely by personal gain.\
 # You want to be rich, powerful, respected, feared.\
 # You want to be the one whom others hurry to obey.\
 # You want people to know your name, and tremble whenever it is spoken.\
 # You want everything, and you won't let anyone stop you from having it..."),
        # (jump_to_menu,"mnu_choose_skill"),
        # ]),
      # ("go_back",[],"Go back.",
       # [(jump_to_menu,"mnu_start_character_3"),
        # ]
       # ),
    # ]
  # ),
  (
    "choose_skill",menu_text_color(0xFF000d2c)|mnf_disable_all_keys,
    "{s13}",
    "none",
    [(assign,"$current_string_reg",10)],
    [
##      ("start_swordsman",[],"Swordsmanship.",[
##        (assign, "$starting_skill", 1),
##        (str_store_string, s14, "@You are particularly talented at swordsmanship."),
##        (jump_to_menu,"mnu_past_life_explanation"),
##        ]),
##      ("start_archer",[],"Archery.",[
##        (assign, "$starting_skill", 2),
##        (str_store_string, s14, "@You are particularly talented at archery."),
##        (jump_to_menu,"mnu_past_life_explanation"),
##        ]),
##      ("start_medicine",[],"Medicine.",[
##        (assign, "$starting_skill", 3),
##        (str_store_string, s14, "@You are particularly talented at medicine."),
##        (jump_to_menu,"mnu_past_life_explanation"),
##        ]),
      ("begin_adventuring",[],"Start to navigate the Galaxy.",[
           (set_show_messages, 0),
           (try_begin),
             (eq,"$character_gender",0),
             (troop_raise_attribute, "trp_player",ca_strength,1),
             (troop_raise_attribute, "trp_player",ca_agility,1),
           (else_try),
		     (troop_raise_attribute, "trp_player",ca_strength,1),
             (troop_raise_attribute, "trp_player",ca_agility,1),
           (try_end),

           (troop_raise_attribute, "trp_player",ca_strength,1),
           (troop_raise_attribute, "trp_player",ca_agility,1),
           (troop_raise_attribute, "trp_player",ca_charisma,1),
		   (troop_raise_attribute, "trp_player",ca_intelligence,1),
           
           (troop_raise_skill, "trp_player","skl_leadership",1),
           (troop_raise_skill, "trp_player","skl_tactics",1),		   
           (troop_raise_skill, "trp_player","skl_riding",1),
		   (troop_raise_skill, "trp_player","skl_horse_archery",1),
		   (troop_raise_skill, "trp_player","skl_shield",1),
		   (troop_raise_skill, "trp_player","skl_ironflesh",1),		   
		   (troop_raise_skill, "trp_player","skl_athletics",1),		   		   
		   (troop_raise_skill, "trp_player","skl_weapon_master",5),
		   
##           (try_begin),
##             (eq, "$starting_skill", 1),
##             (troop_raise_attribute, "trp_player",ca_agility,1),
##             (troop_raise_attribute, "trp_player",ca_strength,1),
##             (troop_raise_skill, "trp_player",skl_power_strike,2),
##             (troop_raise_proficiency, "trp_player",menu_text_color(0xFF000d2c),30),
##             (troop_raise_proficiency, "trp_player",1,20),
##           (else_try),
##             (eq, "$starting_skill", 2),
##             (troop_raise_attribute, "trp_player",ca_strength,2),
##             (troop_raise_skill, "trp_player",skl_power_draw,2),
##             (troop_raise_proficiency, "trp_player",3,50),
##           (else_try),
##             (troop_raise_attribute, "trp_player",ca_intelligence,1),
##             (troop_raise_attribute, "trp_player",ca_charisma,1),
##             (troop_raise_skill, "trp_player",skl_first_aid,1),
##             (troop_raise_skill, "trp_player",skl_wound_treatment,1),
##             (troop_add_item, "trp_player","itm_winged_mace",0),
##             (troop_raise_proficiency, "trp_player",menu_text_color(0xFF000d2c),15),
##             (troop_raise_proficiency, "trp_player",1,15),
##             (troop_raise_proficiency, "trp_player",2,15),
##           (try_end),


      #swy-- jawas get special jawa robes, unattainable in any other way
     (try_begin),
       (troop_get_type, ":character_race", "trp_player"),
       (eq,             ":character_race",  tf_jawa),
       # --
       (troop_add_item, "trp_player", "itm_jawa_hood",  0),
       (troop_add_item, "trp_player", "itm_jawa_robe",  0),
       (troop_add_item, "trp_player", "itm_jawa_boots", 0),
     (try_end),

#---------------------------------------------------
#SW - new classes (commented out old ones below)
      (try_begin),
        (eq,"$background_type",cb0_ambassador),
        (eq,"$character_gender",tf_male),
        (troop_raise_attribute, "trp_player",ca_intelligence,2),
        (troop_raise_attribute, "trp_player",ca_charisma,2),
        (troop_raise_proficiency, "trp_player",wpt_one_handed_weapon,20),
        (troop_raise_proficiency, "trp_player",wpt_two_handed_weapon,20),

        (troop_add_item, "trp_player","itm_energy_shield_yellow_small",imod_battered),
		(troop_add_item, "trp_player","itm_leather_boots",0),
		(troop_add_item, "trp_player","itm_rich_outfit",0),
		(troop_add_item, "trp_player","itm_westar",0),
		(troop_add_item, "trp_player","itm_laser_bolts_yellow_pistol",0),
		(troop_add_item, "trp_player","itm_vibro_blade1",0),
		(troop_add_item, "trp_player","itm_speeder",0),
		(troop_add_item, "trp_player","itm_dried_meat",0),
		
        (troop_set_slot, "trp_player", slot_troop_renown, 200),
        (call_script, "script_change_player_honor", 3),
        (troop_add_gold, "trp_player", 200),
      (else_try),
        (eq,"$background_type",cb0_ambassador),
        (eq,"$character_gender",tf_female),
        (troop_raise_attribute, "trp_player",ca_intelligence,2),
        (troop_raise_attribute, "trp_player",ca_charisma,2),
        (troop_raise_proficiency, "trp_player",wpt_one_handed_weapon,20),
        (troop_raise_proficiency, "trp_player",wpt_two_handed_weapon,20),

        (troop_add_item, "trp_player","itm_energy_shield_yellow_small",imod_battered),
		(troop_add_item, "trp_player","itm_leather_boots",0),
		(troop_add_item, "trp_player","itm_dress_red",0),
		(troop_add_item, "trp_player","itm_westar",0),
		(troop_add_item, "trp_player","itm_laser_bolts_yellow_pistol",0),
		(troop_add_item, "trp_player","itm_vibro_blade1",0),
		(troop_add_item, "trp_player","itm_speeder",0),
		(troop_add_item, "trp_player","itm_dried_meat",0),
		
        (troop_set_slot, "trp_player", slot_troop_renown, 200),
        (call_script, "script_change_player_honor", 3),
        (troop_add_gold, "trp_player", 200),
      (else_try),
        (eq,"$background_type",cb0_merchant),
        (eq,"$character_gender",tf_male),
        (troop_raise_attribute, "trp_player",ca_intelligence,1),
        (troop_raise_attribute, "trp_player",ca_charisma,2),
		(troop_raise_attribute, "trp_player",ca_strength,1),
        (troop_raise_proficiency, "trp_player",wpt_one_handed_weapon,20),
        (troop_raise_proficiency, "trp_player",wpt_firearm,20),

        (troop_add_item, "trp_player","itm_black_boots",0),
		(troop_add_item, "trp_player","itm_vest_closed_a",0),
		(troop_add_item, "trp_player","itm_q2",0),
		(troop_add_item, "trp_player","itm_laser_bolts_yellow_pistol",0),
		(troop_add_item, "trp_player","itm_vibro_blade1",0),
		(troop_add_item, "trp_player","itm_speeder",0),
		(troop_add_item, "trp_player","itm_dried_meat",0),
		
        (troop_set_slot, "trp_player", slot_troop_renown, 100),
        (call_script, "script_change_player_honor", 3),
        (troop_add_gold, "trp_player", 300),
      (else_try),
        (eq,"$background_type",cb0_merchant),
        (eq,"$character_gender",tf_female),
        (troop_raise_attribute, "trp_player",ca_intelligence,1),
        (troop_raise_attribute, "trp_player",ca_charisma,2),
		(troop_raise_attribute, "trp_player",ca_strength,1),
        (troop_raise_proficiency, "trp_player",wpt_one_handed_weapon,20),
        (troop_raise_proficiency, "trp_player",wpt_firearm,20),

        (troop_add_item, "trp_player","itm_black_boots",0),
		(troop_add_item, "trp_player","itm_dress_green",0),
		(troop_add_item, "trp_player","itm_q2",0),
		(troop_add_item, "trp_player","itm_laser_bolts_yellow_pistol",0),
		(troop_add_item, "trp_player","itm_vibro_blade1",0),
		(troop_add_item, "trp_player","itm_speeder",0),
		(troop_add_item, "trp_player","itm_dried_meat",0),
		
        (troop_set_slot, "trp_player", slot_troop_renown, 100),
        (call_script, "script_change_player_honor", 3),
        (troop_add_gold, "trp_player", 300),
      (else_try),
        (eq,"$background_type",cb0_soldier),
        (eq,"$character_gender",tf_male),
        (troop_raise_attribute, "trp_player",ca_agility,2),
		(troop_raise_attribute, "trp_player",ca_strength,2),
        (troop_raise_proficiency, "trp_player",wpt_one_handed_weapon,10),
        (troop_raise_proficiency, "trp_player",wpt_firearm,30),

        (troop_add_item, "trp_player","itm_black_boots",0),
		(troop_add_item, "trp_player","itm_vest_closed_b",0),
		(troop_add_item, "trp_player","itm_a280",0),
		(troop_add_item, "trp_player","itm_laser_bolts_yellow_rifle",0),
		(troop_add_item, "trp_player","itm_vibro_blade1",0),
		(troop_add_item, "trp_player","itm_speeder",0),
		(troop_add_item, "trp_player","itm_dried_meat",0),
		
        (troop_set_slot, "trp_player", slot_troop_renown, 50),
        (call_script, "script_change_player_honor", 3),
        (troop_add_gold, "trp_player", 100),
      (else_try),
        (eq,"$background_type",cb0_soldier),
        (eq,"$character_gender",tf_female),
        (troop_raise_attribute, "trp_player",ca_agility,2),
		(troop_raise_attribute, "trp_player",ca_strength,2),
        (troop_raise_proficiency, "trp_player",wpt_one_handed_weapon,10),
        (troop_raise_proficiency, "trp_player",wpt_firearm,30),

        (troop_add_item, "trp_player","itm_leather_boots",0),
		(troop_add_item, "trp_player","itm_blue_dress",0),
		(troop_add_item, "trp_player","itm_a280",0),
		(troop_add_item, "trp_player","itm_laser_bolts_yellow_rifle",0),
		(troop_add_item, "trp_player","itm_vibro_blade1",0),
		(troop_add_item, "trp_player","itm_speeder",0),
		(troop_add_item, "trp_player","itm_dried_meat",0),
		
        (troop_set_slot, "trp_player", slot_troop_renown, 50),
        (call_script, "script_change_player_honor", 3),
        (troop_add_gold, "trp_player", 100),
      (else_try),
        (eq,"$background_type",cb0_smuggler),
        (eq,"$character_gender",tf_male),
        (troop_raise_attribute, "trp_player",ca_intelligence,1),
        (troop_raise_attribute, "trp_player",ca_charisma,2),		
        (troop_raise_attribute, "trp_player",ca_agility,1),
        (troop_raise_proficiency, "trp_player",wpt_one_handed_weapon,20),
        (troop_raise_proficiency, "trp_player",wpt_firearm,20),

        (troop_add_item, "trp_player","itm_black_boots",0),
		(troop_add_item, "trp_player","itm_vest_open_b",0),
		(troop_add_item, "trp_player","itm_dl44a",0),
		(troop_add_item, "trp_player","itm_laser_bolts_yellow_pistol",0),
		(troop_add_item, "trp_player","itm_vibro_blade1",0),
		(troop_add_item, "trp_player","itm_speeder",0),
		(troop_add_item, "trp_player","itm_dried_meat",0),
		
        (troop_set_slot, "trp_player", slot_troop_renown, 25),
        (call_script, "script_change_player_honor", 3),
        (troop_add_gold, "trp_player", 100),
      (else_try),
        (eq,"$background_type",cb0_smuggler),
        (eq,"$character_gender",tf_female),
        (troop_raise_attribute, "trp_player",ca_intelligence,1),
        (troop_raise_attribute, "trp_player",ca_charisma,2),		
        (troop_raise_attribute, "trp_player",ca_agility,1),
        (troop_raise_proficiency, "trp_player",wpt_one_handed_weapon,20),
        (troop_raise_proficiency, "trp_player",wpt_firearm,20),

        (troop_add_item, "trp_player","itm_leather_boots",0),
		(troop_add_item, "trp_player","itm_dress",0),
		(troop_add_item, "trp_player","itm_dl44a",0),
		(troop_add_item, "trp_player","itm_laser_bolts_yellow_pistol",0),
		(troop_add_item, "trp_player","itm_vibro_blade1",0),
		(troop_add_item, "trp_player","itm_speeder",0),
		(troop_add_item, "trp_player","itm_dried_meat",0),
		
        (troop_set_slot, "trp_player", slot_troop_renown, 25),
        (call_script, "script_change_player_honor", 3),
        (troop_add_gold, "trp_player", 100),
      (else_try),
        (eq,"$background_type",cb0_hunter),
        (eq,"$character_gender",tf_male),
        (troop_raise_attribute, "trp_player",ca_intelligence,1),
        (troop_raise_attribute, "trp_player",ca_agility,1),
		(troop_raise_attribute, "trp_player",ca_strength,2),
        (troop_raise_proficiency, "trp_player",wpt_one_handed_weapon,10),
        (troop_raise_proficiency, "trp_player",wpt_firearm,30),

        (troop_add_item, "trp_player","itm_black_boots",0),
		(troop_add_item, "trp_player","itm_vest_closed_c",0),
		(troop_add_item, "trp_player","itm_westar",0),
		(troop_add_item, "trp_player","itm_westar_shield",0),
		(troop_add_item, "trp_player","itm_laser_bolts_yellow_pistol",0),
		(troop_add_item, "trp_player","itm_vibro_blade1",0),
		(troop_add_item, "trp_player","itm_speeder",0),
		(troop_add_item, "trp_player","itm_dried_meat",0),
		
        (troop_set_slot, "trp_player", slot_troop_renown, 25),
        (call_script, "script_change_player_honor", 3),
        (troop_add_gold, "trp_player", 100),
      (else_try),
        (eq,"$background_type",cb0_hunter),
        (eq,"$character_gender",tf_female),
        (troop_raise_attribute, "trp_player",ca_intelligence,1),
        (troop_raise_attribute, "trp_player",ca_agility,1),
		(troop_raise_attribute, "trp_player",ca_strength,2),
        (troop_raise_proficiency, "trp_player",wpt_one_handed_weapon,10),
        (troop_raise_proficiency, "trp_player",wpt_firearm,30),

        (troop_add_item, "trp_player","itm_black_boots",0),
		(troop_add_item, "trp_player","itm_dress_blue",0),
		(troop_add_item, "trp_player","itm_westar",0),
		(troop_add_item, "trp_player","itm_westar_shield",0),
		(troop_add_item, "trp_player","itm_laser_bolts_yellow_pistol",0),
		(troop_add_item, "trp_player","itm_vibro_blade1",0),
		(troop_add_item, "trp_player","itm_speeder",0),
		(troop_add_item, "trp_player","itm_dried_meat",0),
		
        (troop_set_slot, "trp_player", slot_troop_renown, 25),
        (call_script, "script_change_player_honor", 3),
        (troop_add_gold, "trp_player", 100),
      (else_try),
        (eq,"$background_type",cb0_forcesensitive),
        (eq,"$character_gender",tf_male),
        #(troop_raise_attribute, "trp_player",ca_agility,3),
		(troop_raise_attribute, "trp_player",ca_strength,4),	# had to give 12 strength to guarantee they could use the 1h lightsaber
        (troop_raise_proficiency, "trp_player",wpt_one_handed_weapon,20),
        (troop_raise_proficiency, "trp_player",wpt_archery,20),
		(troop_raise_skill, "trp_player","skl_power_draw",1),

        (troop_add_item, "trp_player","itm_leather_boots",0),
		(troop_add_item, "trp_player","itm_tunic_green",0),
		(troop_add_item, "trp_player","itm_lightsaber_blue_1h",imod_chipped),
		(troop_add_item, "trp_player","itm_force_block",0),
		#(troop_add_item, "trp_player","itm_force_push",0),		#they don't have the skill to use
		(troop_add_item, "trp_player","itm_speeder",0),
		(troop_add_item, "trp_player","itm_dried_meat",0),
		
        (troop_set_slot, "trp_player", slot_troop_renown, 50),
        (call_script, "script_change_player_honor", 3),
        (troop_add_gold, "trp_player", 100),
      (else_try),
        (eq,"$background_type",cb0_forcesensitive),
        (eq,"$character_gender",tf_female),
        #(troop_raise_attribute, "trp_player",ca_agility,3),
		(troop_raise_attribute, "trp_player",ca_strength,4),	# had to give 12 strength to guarantee they could use the 1h lightsaber
        (troop_raise_proficiency, "trp_player",wpt_one_handed_weapon,20),
        (troop_raise_proficiency, "trp_player",wpt_archery,20),
		(troop_raise_skill, "trp_player","skl_power_draw",1),

        (troop_add_item, "trp_player","itm_leather_boots",0),
		(troop_add_item, "trp_player","itm_dress",0),
		(troop_add_item, "trp_player","itm_lightsaber_yellow_1h",imod_chipped),
		(troop_add_item, "trp_player","itm_force_block",0),
		#(troop_add_item, "trp_player","itm_force_push",0),
		(troop_add_item, "trp_player","itm_speeder",0),
		(troop_add_item, "trp_player","itm_dried_meat",0),
		
        (troop_set_slot, "trp_player", slot_troop_renown, 50),
        (call_script, "script_change_player_honor", 3),
        (troop_add_gold, "trp_player", 100),
      (try_end),		
#------------------------------------------------------
	  
        # (eq,"$background_type",cb_noble),
        # (eq,"$character_gender",tf_male),
        # (troop_raise_attribute, "trp_player",ca_intelligence,1),
        # (troop_raise_attribute, "trp_player",ca_charisma,2),
        # (troop_raise_skill, "trp_player",skl_weapon_master,1),
        # (troop_raise_skill, "trp_player",skl_power_strike,1),
        # (troop_raise_skill, "trp_player",skl_riding,1),
        # (troop_raise_skill, "trp_player",skl_tactics,1),
        # (troop_raise_skill, "trp_player",skl_leadership,1),
        # (troop_raise_proficiency, "trp_player",wpt_one_handed_weapon,10),
        # (troop_raise_proficiency, "trp_player",wpt_two_handed_weapon,10),
        # (troop_raise_proficiency, "trp_player",wpt_polearm,10),

        # (troop_add_item, "trp_player","itm_energy_shield_yellow_small",imod_battered),
        # (troop_set_slot, "trp_player", slot_troop_renown, 100),
        # (call_script, "script_change_player_honor", 3),

           
# ##        (troop_add_item, "trp_player","itm_red_gambeson",imod_plain),
# ##        (troop_add_item, "trp_player","itm_sword",imod_plain),
# ##        (troop_add_item, "trp_player","itm_dagger",imod_balanced),
# ##        (troop_add_item, "trp_player","itm_woolen_hose",0),
# ##        (troop_add_item, "trp_player","itm_dried_meat",0),
# ##        (troop_add_item, "trp_player","itm_saddle_horse",imod_plain),
        # (troop_add_gold, "trp_player", 100),
      # (else_try),
        # (eq,"$background_type",cb_noble),
        # (eq,"$character_gender",tf_female),
        # (troop_raise_attribute, "trp_player",ca_intelligence,2),
        # (troop_raise_attribute, "trp_player",ca_charisma,1),
        # (troop_raise_skill, "trp_player",skl_wound_treatment,1),
        # (troop_raise_skill, "trp_player",skl_riding,2),
        # (troop_raise_skill, "trp_player",skl_first_aid,1),
        # (troop_raise_skill, "trp_player",skl_leadership,1),
        # (troop_raise_proficiency, "trp_player",wpt_one_handed_weapon,20),

        # (troop_set_slot, "trp_player", slot_troop_renown, 50),
        # (troop_add_item, "trp_player","itm_energy_shield_yellow_small",imod_battered),
           
# ##        (troop_add_item, "trp_player","itm_dress",imod_sturdy),
# ##        (troop_add_item, "trp_player","itm_dagger",imod_watered_steel),
# ##        (troop_add_item, "trp_player","itm_woolen_hose",0),
# ##        (troop_add_item, "trp_player","itm_hunting_crossbow",0),
# ##        (troop_add_item, "trp_player","itm_bolts",0),
# ##        (troop_add_item, "trp_player","itm_smoked_fish",0),
# ##        (troop_add_item, "trp_player","itm_courser",imod_spirited),
        # (troop_add_gold, "trp_player", 100),
      # (else_try),
        # (eq,"$background_type",cb_merchant),
        # (troop_raise_attribute, "trp_player",ca_intelligence,2),
        # (troop_raise_attribute, "trp_player",ca_charisma,1),
        # (troop_raise_skill, "trp_player",skl_riding,1),
        # (troop_raise_skill, "trp_player",skl_leadership,1),
        # (troop_raise_skill, "trp_player",skl_trade,2),
        # (troop_raise_skill, "trp_player",skl_inventory_management,1),
        # (troop_raise_proficiency, "trp_player",wpt_two_handed_weapon,10),
           
# ##        (troop_add_item, "trp_player","itm_leather_jacket",0),
# ##        (troop_add_item, "trp_player","itm_leather_boots",0),
# ##        (troop_add_item, "trp_player","itm_fur_hat",0),
# ##        (troop_add_item, "trp_player","itm_dagger",0),
# ##        (troop_add_item, "trp_player","itm_hunting_crossbow",0),
# ##        (troop_add_item, "trp_player","itm_bolts",0),
# ##        (troop_add_item, "trp_player","itm_smoked_fish",0),
# ##        (troop_add_item, "trp_player","itm_saddle_horse",0),
# ##        (troop_add_item, "trp_player","itm_sumpter_horse",0),
# ##        (troop_add_item, "trp_player","itm_salt",0),
# ##        (troop_add_item, "trp_player","itm_salt",0),
# ##        (troop_add_item, "trp_player","itm_salt",0),
# ##        (troop_add_item, "trp_player","itm_pottery",0),
# ##        (troop_add_item, "trp_player","itm_pottery",0),
           
        # (troop_add_gold, "trp_player", 250),
        # (troop_set_slot, "trp_player", slot_troop_renown, 20),
      # (else_try),
        # (eq,"$background_type",cb_guard),
        # (troop_raise_attribute, "trp_player",ca_strength,1),
        # (troop_raise_attribute, "trp_player",ca_agility,1),
        # (troop_raise_attribute, "trp_player",ca_charisma,1),
        # (troop_raise_skill, "trp_player","skl_ironflesh",1),
        # (troop_raise_skill, "trp_player","skl_power_strike",1),
        # (troop_raise_skill, "trp_player","skl_weapon_master",1),
        # (troop_raise_skill, "trp_player","skl_leadership",1),
        # (troop_raise_skill, "trp_player","skl_trainer",1),
        # (troop_raise_proficiency, "trp_player",wpt_one_handed_weapon,10),
        # (troop_raise_proficiency, "trp_player",wpt_two_handed_weapon,15),
        # (troop_raise_proficiency, "trp_player",wpt_polearm,20),
        # (troop_raise_proficiency, "trp_player",wpt_throwing,10),
        # (troop_add_item, "trp_player","itm_energy_shield_yellow_small",imod_battered),
           
# ##        (troop_add_item, "trp_player","itm_leather_jerkin",imod_ragged),
# ##        (troop_add_item, "trp_player","itm_skullcap",imod_rusty),
# ##        (troop_add_item, "trp_player","itm_spear",0),
# ##        (troop_add_item, "trp_player","itm_arming_sword",imod_chipped),
# ##        (troop_add_item, "trp_player","itm_hunting_crossbow",0),
# ##        (troop_add_item, "trp_player","itm_hunter_boots",0),
# ##        (troop_add_item, "trp_player","itm_leather_gloves",imod_ragged),
# ##        (troop_add_item, "trp_player","itm_bolts",0),
# ##        (troop_add_item, "trp_player","itm_smoked_fish",0),
# ##        (troop_add_item, "trp_player","itm_saddle_horse",imod_swaybacked),
        # (troop_add_gold, "trp_player", 50),
        # (troop_set_slot, "trp_player", slot_troop_renown, 10),
      # (else_try),
        # (eq,"$background_type",cb_forester),
        # (troop_raise_attribute, "trp_player",ca_strength,1),
        # (troop_raise_attribute, "trp_player",ca_agility,2),
        # (troop_raise_skill, "trp_player","skl_power_draw",1),
        # (troop_raise_skill, "trp_player","skl_tracking",1),
        # (troop_raise_skill, "trp_player","skl_pathfinding",1),
        # (troop_raise_skill, "trp_player","skl_spotting",1),
        # (troop_raise_skill, "trp_player","skl_athletics",1),
        # (troop_raise_proficiency, "trp_player",wpt_two_handed_weapon,10),
        # (troop_raise_proficiency, "trp_player",wpt_archery,30),
# ##        (troop_add_item, "trp_player","itm_short_bow",imod_bent),
# ##        (troop_add_item, "trp_player","itm_arrows",0),
# ##        (troop_add_item, "trp_player","itm_axe",imod_chipped),
# ##        (troop_add_item, "trp_player","itm_rawhide_coat",0),
# ##        (troop_add_item, "trp_player","itm_hide_boots",0),
# ##        (troop_add_item, "trp_player","itm_dried_meat",0),
# ##        (troop_add_item, "trp_player","itm_sumpter_horse",imod_heavy),
# ##        (troop_add_item, "trp_player","itm_furs",0),
        # (troop_add_gold, "trp_player", 30),
      # (else_try),
        # (eq,"$background_type",cb_nomad),
        # (eq,"$character_gender",tf_male),
        # (troop_raise_attribute, "trp_player",ca_strength,1),
        # (troop_raise_attribute, "trp_player",ca_agility,1),
        # (troop_raise_attribute, "trp_player",ca_intelligence,1),
        # (troop_raise_skill, "trp_player","skl_power_draw",1),
        # (troop_raise_skill, "trp_player","skl_horse_archery",1),
        # (troop_raise_skill, "trp_player","skl_pathfinding",1),
        # (troop_raise_skill, "trp_player","skl_riding",2),
        # (troop_raise_proficiency, "trp_player",wpt_one_handed_weapon,10),
        # (troop_raise_proficiency, "trp_player",wpt_archery,30),
        # (troop_raise_proficiency, "trp_player",wpt_throwing,10),
        # (troop_add_item, "trp_player","itm_energy_shield_yellow_small",imod_battered),
# ##        (troop_add_item, "trp_player","itm_javelin",imod_bent),
# ##        (troop_add_item, "trp_player","itm_sword_khergit_1",imod_rusty),
# ##        (troop_add_item, "trp_player","itm_nomad_armor",0),
# ##        (troop_add_item, "trp_player","itm_hide_boots",0),
# ##        (troop_add_item, "trp_player","itm_horse_meat",0),
# ##        (troop_add_item, "trp_player","itm_steppe_horse",0),
        # (troop_add_gold, "trp_player", 15),
        # (troop_set_slot, "trp_player", slot_troop_renown, 10),
      # (else_try),
        # (eq,"$background_type",cb_nomad),
        # (eq,"$character_gender",tf_female),
        # (troop_raise_attribute, "trp_player",ca_strength,1),
        # (troop_raise_attribute, "trp_player",ca_agility,1),
        # (troop_raise_attribute, "trp_player",ca_intelligence,1),
        # (troop_raise_skill, "trp_player","skl_wound_treatment",1),
        # (troop_raise_skill, "trp_player","skl_first_aid",1),
        # (troop_raise_skill, "trp_player","skl_pathfinding",1),
        # (troop_raise_skill, "trp_player","skl_riding",2),
        # (troop_raise_proficiency, "trp_player",wpt_one_handed_weapon,5),
        # (troop_raise_proficiency, "trp_player",wpt_archery,20),
        # (troop_raise_proficiency, "trp_player",wpt_throwing,5),
        # (troop_add_item, "trp_player","itm_energy_shield_yellow_small",imod_battered),
# ##        (troop_add_item, "trp_player","itm_javelin",imod_bent),
# ##        (troop_add_item, "trp_player","itm_sickle",imod_plain),
# ##        (troop_add_item, "trp_player","itm_nomad_armor",0),
# ##        (troop_add_item, "trp_player","itm_hide_boots",0),
# ##        (troop_add_item, "trp_player","itm_steppe_horse",0),
# ##        (troop_add_item, "trp_player","itm_grain",0),
        # (troop_add_gold, "trp_player", 20),
      # (else_try),
        # (eq,"$background_type",cb_thief),
        # (troop_raise_attribute, "trp_player",ca_agility,3),
        # (troop_raise_skill, "trp_player","skl_athletics",2),
        # (troop_raise_skill, "trp_player","skl_power_throw",1),
        # (troop_raise_skill, "trp_player","skl_inventory_management",1),
        # (troop_raise_skill, "trp_player","skl_looting",1),
        # (troop_raise_proficiency, "trp_player",wpt_one_handed_weapon,20),
        # (troop_raise_proficiency, "trp_player",wpt_throwing,20),
        # (troop_add_item, "trp_player","itm_vibro_blade1",0),   #SW - used to be throwing_knives
# ##        (troop_add_item, "trp_player","itm_stones",0),
# ##        (troop_add_item, "trp_player","itm_cudgel",imod_plain),
# ##        (troop_add_item, "trp_player","itm_dagger",imod_rusty),
# ##        (troop_add_item, "trp_player","itm_shirt",imod_tattered),
# ##        (troop_add_item, "trp_player","itm_black_hood",imod_tattered),
# ##        (troop_add_item, "trp_player","itm_wrapping_boots",imod_ragged),
        # (troop_add_gold, "trp_player", 25),
# ##      (else_try),
# ##        (eq,"$background_type",cb_priest),
# ##        (troop_raise_attribute, "trp_player",ca_strength,1),
# ##        (troop_raise_attribute, "trp_player",ca_intelligence,2),
# ##        (troop_raise_attribute, "trp_player",ca_charisma,1),
# ##        (troop_raise_skill, "trp_player",skl_wound_treatment,1),
# ##        (troop_raise_skill, "trp_player",skl_leadership,1),
# ##        (troop_raise_skill, "trp_player",skl_prisoner_management,1),
# ##        (troop_raise_proficiency, "trp_player",menu_text_color(0xFF000d2c),10),
# ##        (troop_add_item, "trp_player","itm_robe",0),
# ##        (troop_add_item, "trp_player","itm_wrapping_boots",0),
# ##        (troop_add_item, "trp_player","itm_club",0),
# ##        (troop_add_item, "trp_player","itm_smoked_fish",0),
# ##        (troop_add_item, "trp_player","itm_sumpter_horse",0),
# ##        (troop_add_gold, "trp_player", 10),
# ##        (troop_set_slot, "trp_player", slot_troop_renown, 10),
      # (try_end),

    # (try_begin),
        # (eq,"$background_answer_2",cb2_page),
        # (troop_raise_attribute, "trp_player",ca_charisma,1),
        # (troop_raise_attribute, "trp_player",ca_strength,1),
        # (troop_raise_skill, "trp_player","skl_power_strike",1),
        # (troop_raise_skill, "trp_player","skl_persuasion",1),
        # (troop_raise_proficiency, "trp_player",wpt_one_handed_weapon,15),
        # (troop_raise_proficiency, "trp_player",wpt_polearm,5),
    # (else_try),
        # (eq,"$background_answer_2",cb2_apprentice),
        # (troop_raise_attribute, "trp_player",ca_intelligence,1),
        # (troop_raise_attribute, "trp_player",ca_strength,1),
        # (troop_raise_skill, "trp_player","skl_engineer",1),
        # (troop_raise_skill, "trp_player","skl_trade",1),
    # (else_try),
        # (eq,"$background_answer_2",cb2_urchin),
        # (troop_raise_attribute, "trp_player",ca_agility,1),
        # (troop_raise_attribute, "trp_player",ca_intelligence,1),
        # (troop_raise_skill, "trp_player","skl_spotting",1),
        # (troop_raise_skill, "trp_player","skl_looting",1),
        # (troop_raise_proficiency, "trp_player",wpt_one_handed_weapon,15),
        # (troop_raise_proficiency, "trp_player",wpt_throwing,5),
    # (else_try),
        # (eq,"$background_answer_2",cb2_steppe_child),
        # (troop_raise_attribute, "trp_player",ca_strength,1),
        # (troop_raise_attribute, "trp_player",ca_agility,1),
        # (troop_raise_skill, "trp_player","skl_horse_archery",1),
        # (troop_raise_skill, "trp_player","skl_power_throw",1),
        # (troop_raise_proficiency, "trp_player",wpt_archery,15),
        # (call_script,"script_change_troop_renown", "trp_player", 5),
    # (else_try),
        # (eq,"$background_answer_2",cb2_merchants_helper),
        # (troop_raise_attribute, "trp_player",ca_intelligence,1),
        # (troop_raise_attribute, "trp_player",ca_charisma,1),
        # (troop_raise_skill, "trp_player","skl_inventory_management",1),
        # (troop_raise_skill, "trp_player","skl_trade",1),
# ##	(else_try),
# ##        (eq,"$background_answer_2",5),
# ##        (troop_raise_attribute, "trp_player",ca_intelligence,1),
# ##        (troop_raise_attribute, "trp_player",ca_charisma,1),
# ##        (troop_raise_skill, "trp_player",skl_leadership,1),
# ##        (troop_raise_skill, "trp_player",skl_athletics,1),
# ##        (troop_raise_skill, "trp_player",skl_riding,1),
# ##        (troop_raise_proficiency, "trp_player",1,5),
# ##        (troop_raise_proficiency, "trp_player",2,5),
# ##        (call_script,"script_change_troop_renown", "trp_player", 15),
# ##	(else_try),
# ##        (eq,"$background_answer_2",6),
# ##        (troop_raise_attribute, "trp_player",ca_charisma,3),
# ##        (troop_raise_attribute, "trp_player",ca_agility,1),
# ##        (troop_raise_skill, "trp_player",skl_weapon_master,1),
# ##        (troop_raise_proficiency, "trp_player",menu_text_color(0xFF000d2c),15),
# ##        (troop_raise_proficiency, "trp_player",2,10),
# ##        (troop_raise_proficiency, "trp_player",4,10),
# ##        (call_script,"script_change_troop_renown", "trp_player", 20),
# ##	(else_try),
# ##        (eq,"$background_answer_2",7),
# ##        (troop_raise_attribute, "trp_player",ca_intelligence,1),
# ##        (troop_raise_attribute, "trp_player",ca_charisma,2),
# ##        (troop_raise_skill, "trp_player",skl_leadership,1),
# ##        (troop_raise_skill, "trp_player",skl_tactics,1),
# ##        (troop_raise_proficiency, "trp_player",menu_text_color(0xFF000d2c),10),
# ##        (troop_raise_proficiency, "trp_player",1,10),
# ##        (call_script,"script_change_troop_renown", "trp_player", 15),
# ##	(else_try),
# ##        (eq,"$background_answer_2",8),
# ##        (troop_raise_attribute, "trp_player",ca_agility,1),
# ##        (troop_raise_attribute, "trp_player",ca_intelligence,1),
# ##        (troop_raise_attribute, "trp_player",ca_charisma,1),
# ##        (troop_raise_skill, "trp_player",skl_leadership,1),
# ##        (troop_raise_skill, "trp_player",skl_surgery,1),
# ##        (troop_raise_skill, "trp_player",skl_first_aid,1),
# ##        (troop_raise_proficiency, "trp_player",2,10),
# ##        (call_script,"script_change_troop_renown", "trp_player", 5),
	# (try_end),

	# (try_begin),
# ##        (eq,"$background_answer_3",1),
# ##        (troop_raise_attribute, "trp_player",ca_strength,1),
# ##        (troop_raise_skill, "trp_player",skl_power_strike,1),
# ##        (troop_raise_skill, "trp_player",skl_shield,1),
# ##        (troop_add_gold, "trp_player", 10),
# ##        (try_begin),
# ##        (this_or_next|player_has_item,"itm_sword"),
# ##        (troop_has_item_equipped,"trp_player","itm_sword"),
# ##        (troop_remove_item, "trp_player","itm_sword"),
# ##        (try_end),
# ##        (try_begin),
# ##        (this_or_next|player_has_item,"itm_arming_sword"),
# ##        (troop_has_item_equipped,"trp_player","itm_arming_sword"),
# ##        (troop_remove_item, "trp_player","itm_arming_sword"),
# ##        (try_end),
# ##        (troop_add_item, "trp_player","itm_short_sword",0),
# ##        (troop_add_item, "trp_player","itm_wooden_shield",imod_battered),
# ##        (troop_raise_proficiency, "trp_player",menu_text_color(0xFF000d2c),10),
# ##        (troop_raise_proficiency, "trp_player",4,10),
# ##    (else_try),
# ##        (eq,"$background_answer_3",2),
# ##        (troop_raise_attribute, "trp_player",ca_agility,1),
# ##        (troop_raise_skill, "trp_player",skl_weapon_master,1),
# ##        (troop_raise_skill, "trp_player",skl_shield,1),
# ##        (try_begin),
# ##        (this_or_next|player_has_item,"itm_hide_boots"),
# ##        (troop_has_item_equipped,"trp_player","itm_hide_boots"),
# ##        (troop_remove_item, "trp_player","itm_hide_boots"),
# ##        (try_end),
# ##        (troop_add_item, "trp_player","itm_khergit_guard_helmet",imod_crude),
# ##        (troop_add_item, "trp_player","itm_mail_chausses",imod_crude),
# ##        (troop_add_item, "trp_player","itm_sword_khergit_1",imod_plain),
# ##        (troop_add_gold, "trp_player", 20),
# ##        (troop_raise_proficiency, "trp_player",2,20),
# ##    (else_try),
        # (eq,"$background_answer_3",cb3_poacher),
        # (troop_raise_attribute, "trp_player",ca_strength,1),
        # (troop_raise_attribute, "trp_player",ca_agility,1),
        # (troop_raise_skill, "trp_player","skl_power_draw",1),
        # (troop_raise_skill, "trp_player","skl_tracking",1),
        # (troop_raise_skill, "trp_player","skl_spotting",1),
        # (troop_raise_skill, "trp_player","skl_athletics",1),
        # (troop_add_gold, "trp_player", 10),
        # (troop_raise_proficiency, "trp_player",wpt_polearm,10),
        # (troop_raise_proficiency, "trp_player",wpt_archery,35),
           
        # (troop_add_item, "trp_player","itm_durasteel_staff",imod_chipped),
        # (troop_add_item, "trp_player","itm_tunic_green",0),
        # (troop_add_item, "trp_player","itm_leather_boots",0),
        # (troop_add_item, "trp_player","itm_westar",0),
        # (troop_add_item, "trp_player","itm_laser_bolts_yellow",0),
        # (troop_add_item, "trp_player","itm_speeder",0),
        # (troop_add_item, "trp_player","itm_dried_meat",0),
        # (troop_add_item, "trp_player","itm_dried_meat",0),
        # (troop_add_item, "trp_player","itm_furs",0),
        # (troop_add_item, "trp_player","itm_furs",0),
    # (else_try),
        # (eq,"$background_answer_3",cb3_craftsman),
        # (troop_raise_attribute, "trp_player",ca_strength,1),
        # (troop_raise_attribute, "trp_player",ca_intelligence,1),

        # (troop_raise_skill, "trp_player","skl_weapon_master",1),
        # (troop_raise_skill, "trp_player","skl_engineer",1),
        # (troop_raise_skill, "trp_player","skl_tactics",1),
        # (troop_raise_skill, "trp_player","skl_trade",1),

        # (troop_raise_proficiency, "trp_player",wpt_one_handed_weapon,15),
        # (troop_add_gold, "trp_player", 100),


        # (troop_add_item, "trp_player","itm_leather_boots",imod_ragged),
        # (troop_add_item, "trp_player","itm_tunic_green",0),
           
        # (troop_add_item, "trp_player","itm_vibro_blade3", imod_balanced),
        # (troop_add_item, "trp_player","itm_dlt19",0),
        # (troop_add_item, "trp_player","itm_laser_bolts_yellow",0),
           
        # (troop_add_item, "trp_player","itm_tools",0),
        # (troop_add_item, "trp_player","itm_speeder",0),
        # (troop_add_item, "trp_player","itm_smoked_fish",0),
    # (else_try),
        # (eq,"$background_answer_3",cb3_peddler),
        # (troop_raise_attribute, "trp_player",ca_charisma,1),
        # (troop_raise_attribute, "trp_player",ca_intelligence,1),
        # (troop_raise_skill, "trp_player","skl_riding",1),
        # (troop_raise_skill, "trp_player","skl_trade",1),
        # (troop_raise_skill, "trp_player","skl_pathfinding",1),
        # (troop_raise_skill, "trp_player","skl_inventory_management",1),
           
        # (troop_add_item, "trp_player","itm_leather_gloves",imod_plain),
        # (troop_add_gold, "trp_player", 90),
        # (troop_raise_proficiency, "trp_player",wpt_polearm,15),
           
        # (troop_add_item, "trp_player","itm_tunic_green",0),
        # (troop_add_item, "trp_player","itm_leather_boots",imod_ragged),
        # #(troop_add_item, "trp_player","itm_fur_hat",0),
        # (troop_add_item, "trp_player","itm_durasteel_staff",0),
        # (troop_add_item, "trp_player","itm_dlt19",0),
        # (troop_add_item, "trp_player","itm_laser_bolts_yellow",0),
        # (troop_add_item, "trp_player","itm_speeder",0),
        # (troop_add_item, "trp_player","itm_speeder",0),
           
        # (troop_add_item, "trp_player","itm_linen",0),
        # (troop_add_item, "trp_player","itm_pottery",0),
        # (troop_add_item, "trp_player","itm_wool",0),
        # (troop_add_item, "trp_player","itm_wool",0),
        # (troop_add_item, "trp_player","itm_smoked_fish",0),
# ##    (else_try),
# ##        (eq,"$background_answer_3",6),
# ##        (troop_raise_attribute, "trp_player",ca_strength,1),
# ##        (troop_raise_attribute, "trp_player",ca_charisma,1),
# ##        (troop_raise_skill, "trp_player",skl_shield,1),
# ##        (troop_raise_skill, "trp_player",skl_wound_treatment,1),
# ##        (troop_raise_skill, "trp_player",skl_first_aid,1),
# ##        (troop_raise_skill, "trp_player",skl_surgery,1),
# ##        (troop_add_item, "trp_player","itm_leather_gloves",imod_ragged),
# ##        (troop_add_item, "trp_player","itm_quarter_staff",imod_heavy),
# ##        (troop_add_item, "trp_player","itm_black_hood",0),
# ##        (troop_add_gold, "trp_player", 10),
# ##        (troop_raise_proficiency, "trp_player",2,20),
    # (else_try),
        # (eq,"$background_answer_3",cb3_troubadour),
        # (troop_raise_attribute, "trp_player",ca_charisma,2),
           
        # (troop_raise_skill, "trp_player","skl_weapon_master",1),
        # (troop_raise_skill, "trp_player","skl_persuasion",1),
        # (troop_raise_skill, "trp_player","skl_leadership",1),
        # (troop_raise_skill, "trp_player","skl_pathfinding",1),
           
        # (troop_add_gold, "trp_player", 80),
        # (troop_raise_proficiency, "trp_player",wpt_one_handed_weapon,25),
        # (troop_raise_proficiency, "trp_player",wpt_crossbow,10),

        # (troop_add_item, "trp_player","itm_tunic_green",imod_sturdy),
        # (troop_add_item, "trp_player","itm_leather_boots",imod_ragged),
        # (troop_add_item, "trp_player","itm_vibro_blade3", imod_rusty),
        # (troop_add_item, "trp_player","itm_dlt19", 0),
        # (troop_add_item, "trp_player","itm_laser_bolts_yellow", 0),
        # (troop_add_item, "trp_player","itm_speeder",0),
        # (troop_add_item, "trp_player","itm_smoked_fish",0),
    # (else_try),
        # (eq,"$background_answer_3",cb3_squire),
        # (troop_raise_attribute, "trp_player",ca_strength,1),
        # (troop_raise_attribute, "trp_player",ca_agility,1),
        # (troop_raise_skill, "trp_player","skl_riding",1),
        # (troop_raise_skill, "trp_player","skl_weapon_master",1),
        # (troop_raise_skill, "trp_player","skl_power_strike",1),
        # (troop_raise_skill, "trp_player","skl_leadership",1),

        # (troop_add_gold, "trp_player", 20),
        # (troop_raise_proficiency, "trp_player",wpt_one_handed_weapon,30),
        # (troop_raise_proficiency, "trp_player",wpt_two_handed_weapon,30),
        # (troop_raise_proficiency, "trp_player",wpt_polearm,30),
        # (troop_raise_proficiency, "trp_player",wpt_archery,10),
        # (troop_raise_proficiency, "trp_player",wpt_crossbow,10),
        # (troop_raise_proficiency, "trp_player",wpt_throwing,10),

        # (troop_add_item, "trp_player","itm_tunic_green",imod_ragged),
        # (troop_add_item, "trp_player","itm_leather_boots",imod_tattered),
           
        # (troop_add_item, "trp_player","itm_vibro_blade3", imod_rusty),
        # (troop_add_item, "trp_player","itm_dlt19",0),
        # (troop_add_item, "trp_player","itm_laser_bolts_yellow",0),
        # (troop_add_item, "trp_player","itm_speeder",0),
        # (troop_add_item, "trp_player","itm_smoked_fish",0),
    # (else_try),
        # (eq,"$background_answer_3",cb3_lady_in_waiting),
        # (eq,"$character_gender",tf_female),
        # (troop_raise_attribute, "trp_player",ca_intelligence,1),
        # (troop_raise_attribute, "trp_player",ca_charisma,1),
           
        # (troop_raise_skill, "trp_player","skl_persuasion",2),
        # (troop_raise_skill, "trp_player","skl_riding",1),
        # (troop_raise_skill, "trp_player","skl_wound_treatment",1),
           
        # (troop_add_item, "trp_player","itm_vibro_blade3", 0),
        # (troop_add_item, "trp_player","itm_dlt19",0),
        # (troop_add_item, "trp_player","itm_laser_bolts_yellow",0),
        # (troop_add_item, "trp_player","itm_speeder", 0),
        # (troop_add_item, "trp_player","itm_woolen_hood",imod_sturdy),
        # (troop_add_item, "trp_player","itm_woolen_dress",imod_sturdy),
        # (troop_add_gold, "trp_player", 100),
        # (troop_raise_proficiency, "trp_player",wpt_one_handed_weapon,10),
        # (troop_raise_proficiency, "trp_player",wpt_crossbow,15),
        # (troop_add_item, "trp_player","itm_smoked_fish",0),
    # (else_try),
        # (eq,"$background_answer_3",cb3_student),
        # (troop_raise_attribute, "trp_player",ca_intelligence,2),
           
        # (troop_raise_skill, "trp_player","skl_weapon_master",1),
        # (troop_raise_skill, "trp_player","skl_surgery",1),
        # (troop_raise_skill, "trp_player","skl_wound_treatment",1),
        # (troop_raise_skill, "trp_player","skl_persuasion",1),
           
        # (troop_add_gold, "trp_player", 80),
        # (troop_raise_proficiency, "trp_player",wpt_one_handed_weapon,20),
        # (troop_raise_proficiency, "trp_player",wpt_crossbow,20),

        # (troop_add_item, "trp_player","itm_linen_tunic",imod_sturdy),
        # (troop_add_item, "trp_player","itm_woolen_hose",0),
        # (troop_add_item, "trp_player","itm_vibro_blade3", imod_rusty),
        # (troop_add_item, "trp_player","itm_dlt19", 0),
        # (troop_add_item, "trp_player","itm_laser_bolts_yellow", 0),
        # (troop_add_item, "trp_player","itm_speeder",0),
        # (troop_add_item, "trp_player","itm_smoked_fish",0),
        # (store_random_in_range, ":book_no", books_begin, books_end),
        # (troop_add_item, "trp_player",":book_no",0),
    # (try_end),

      # (try_begin),
        # (eq,"$background_answer_4",cb4_revenge),
        # (troop_raise_attribute, "trp_player",ca_strength,2),
        # (troop_raise_skill, "trp_player","skl_power_strike",1),
      # (else_try),
        # (eq,"$background_answer_4",cb4_loss),
        # (troop_raise_attribute, "trp_player",ca_charisma,2),
        # (troop_raise_skill, "trp_player","skl_ironflesh",1),
      # (else_try),
        # (eq,"$background_answer_4",cb4_wanderlust),
        # (troop_raise_attribute, "trp_player",ca_agility,2),
        # (troop_raise_skill, "trp_player","skl_pathfinding",1),
# ##        (else_try),
# ##        (eq,"$background_answer_4",4),
# ##        (troop_raise_attribute, "trp_player",ca_charisma,1),
# ##        (troop_raise_skill, "trp_player",skl_wound_treatment,1),
# ##        (troop_raise_proficiency, "trp_player",5,10),
      # (else_try),
        # (eq,"$background_answer_4",cb4_disown),
        # (troop_raise_attribute, "trp_player",ca_strength,1),
        # (troop_raise_attribute, "trp_player",ca_intelligence,1),
        # (troop_raise_skill, "trp_player","skl_weapon_master",1),
      # (else_try),
        # (eq,"$background_answer_4",cb4_greed),
        # (troop_raise_attribute, "trp_player",ca_agility,1),
        # (troop_raise_attribute, "trp_player",ca_intelligence,1),
        # (troop_raise_skill, "trp_player","skl_looting",1),
      # (try_end),

		#SW - added faction specific changes
		(try_begin),
			(eq, "$faction_choice", cb0_empire),
			(call_script, "script_change_player_relation_with_faction", "fac_galacticempire", 25),
			(troop_set_slot, "trp_player", slot_troop_renown, 250),		# may be necessary so you aren't hired as a merc when you join the faction
			#(troop_set_faction, "trp_player", "fac_galacticempire"),
			#(call_script, "script_player_join_faction", "fac_galacticempire"),
			(party_set_icon, "p_main_party", "icon_tie_fighter"),
			(party_add_members, "p_main_party", "trp_imperial_recruit", 5),
			(call_script, "script_troop_add_gold","trp_player", 500),	
			
			#Fix the starting equipment
			(troop_set_inventory_slot, "trp_player",4,-1),	#ek_head
			(troop_set_inventory_slot, "trp_player",5,-1),	#ek_body
			(troop_set_inventory_slot, "trp_player",6,-1),	#ek_foot
			(troop_set_inventory_slot, "trp_player",7,-1),	#ek_gloves
			#add items
			(troop_add_item, "trp_player","itm_imperial_trooper_armor",0),
			(troop_add_item, "trp_player","itm_black_boots",0),
			(troop_add_item, "trp_player","itm_imperial_hat_black",0),
			(troop_add_item, "trp_player","itm_laser_bolts_red_rifle",0),
			(troop_add_item, "trp_player","itm_e11",0),
			(troop_add_item, "trp_player","itm_protein_pack",0),
			(troop_add_item, "trp_player","itm_carbohydrate_pack",0),
			#equip the items
			(troop_equip_items, "trp_player"),
			
			(party_relocate_near_party, "p_main_party", "p_coruscant", 5),
			#change the culture to empire
			(call_script, "script_change_culture_empire"),
		(else_try),
			(eq, "$faction_choice", cb0_rebel),
			(call_script, "script_change_player_relation_with_faction", "fac_rebelalliance", 25),
			(troop_set_slot, "trp_player", slot_troop_renown, 250),		# may be necessary so you aren't hired as a merc when you join the faction			
			#(troop_set_faction, "trp_player", "fac_rebelalliance"),
			#(call_script, "script_player_join_faction", "fac_rebelalliance"),
			(party_set_icon, "p_main_party", "icon_a_wing"),
			(party_add_members, "p_main_party", "trp_rebel_recruit", 5),
			(call_script, "script_troop_add_gold","trp_player", 250),
			
			#Fix the starting equipment
			(troop_set_inventory_slot, "trp_player",4,-1),	#ek_head
			(troop_set_inventory_slot, "trp_player",5,-1),	#ek_body
			(troop_set_inventory_slot, "trp_player",6,-1),	#ek_foot
			(troop_set_inventory_slot, "trp_player",7,-1),	#ek_gloves
			#add items
			(troop_add_item, "trp_player","itm_rebel_technician_armor",0),
			(troop_add_item, "trp_player","itm_black_boots",0),
			(troop_add_item, "trp_player","itm_rebel_technician_helmet",0),
			(troop_add_item, "trp_player","itm_laser_bolts_green_pistol",0),
			(troop_add_item, "trp_player","itm_dh17",0),
			(troop_add_item, "trp_player","itm_protein_pack",0),
			(troop_add_item, "trp_player","itm_carbohydrate_pack",0),
			#equip the items
			(troop_equip_items, "trp_player"),
			
			(party_relocate_near_party, "p_main_party", "p_yavin_iv", 5),
			#change the culture to rebel
			(call_script, "script_change_culture_rebel"),			
		(else_try),
			(eq, "$faction_choice", cb0_hutt),
			(call_script, "script_change_player_relation_with_faction", "fac_huttcartel", 25),
			(troop_set_slot, "trp_player", slot_troop_renown, 250),		# may be necessary so you aren't hired as a merc when you join the faction			
			#(troop_set_faction, "trp_player", "fac_huttcartel"),
			#(call_script, "script_player_join_faction", "fac_huttcartel"),
			(party_set_icon, "p_main_party", "icon_hutt_patrol"),
			(party_add_members, "p_main_party", "trp_hutt_militia", 5), 
			(call_script, "script_troop_add_gold","trp_player", 250),
			
			#Fix the starting equipment
			(troop_set_inventory_slot, "trp_player",4,-1),	#ek_head
			(troop_set_inventory_slot, "trp_player",5,-1),	#ek_body
			(troop_set_inventory_slot, "trp_player",6,-1),	#ek_foot
			(troop_set_inventory_slot, "trp_player",7,-1),	#ek_gloves
			#add items
			(troop_add_item, "trp_player","itm_skiff_guard_armor_white",0),
			(troop_add_item, "trp_player","itm_leather_boots",0),
			(troop_add_item, "trp_player","itm_laser_bolts_orange_pistol",0),
			(troop_add_item, "trp_player","itm_skiff_guard_helmet",0),
			(troop_add_item, "trp_player","itm_dl18",0),
			(troop_add_item, "trp_player","itm_vibro_axe_long_1h",0),
			(troop_add_item, "trp_player","itm_protein_pack",0),
			(troop_add_item, "trp_player","itm_carbohydrate_pack",0),
			#equip the items
			(troop_equip_items, "trp_player"),
			
			(party_relocate_near_party, "p_main_party", "p_tatooine", 5),
			#change the culture to hutt
			(call_script, "script_change_culture_hutt"),							
		(else_try),
			(troop_set_slot, "trp_player", slot_troop_renown, 50),
			(call_script, "script_troop_add_gold","trp_player", 100),
			
			#Fix the starting equipment
			(troop_add_item, "trp_player","itm_protein_pack",0),
			(troop_add_item, "trp_player","itm_carbohydrate_pack",0),
			
			(party_relocate_near_party, "p_main_party", "p_shipyard_trade_federation", 10),	#trade federation base
			#change the culture to human
			(call_script, "script_change_culture_human"),				
		(try_end),
			
           (try_begin),
		   #SW - modified background_type
             (eq, "$background_type", cb0_ambassador),
             (jump_to_menu, "mnu_auto_return"),
#normal_banner_begin
             (start_presentation, "prsnt_banner_selection"),
#custom_banner_begin
#             (start_presentation, "prsnt_custom_banner"),
           (else_try),
             (change_screen_return, 0),
           (try_end),
           (set_show_messages, 1),
        ]),
      ("go_back_dot",[],"Go back.",[
        #(jump_to_menu,"mnu_start_character_4"),
		(jump_to_menu,"mnu_start_character_faction"),
        ]),
    ]
  ),

  (
    "past_life_explanation",menu_text_color(0xFF000d2c)|mnf_disable_all_keys,
    "{s3}",
    "none",
    [
     (try_begin),
       (gt,"$current_string_reg",14),
       (assign,"$current_string_reg",10),
     (try_end),
     (str_store_string_reg,s3,"$current_string_reg"),
     (try_begin),
       (ge,"$current_string_reg",14),
       (str_store_string,s5,"@Back to the beginning..."),
     (else_try),
       (str_store_string,s5,"@View next segment..."),
     (try_end),
     ],
    [
      ("view_next",[],"{s5}",[
        (val_add,"$current_string_reg",1),
        (jump_to_menu, "mnu_past_life_explanation"),
        ]),
      ("continue_3dot",[],"Continue...",
       [
        ]),
      ("go_back_dot",[],"Go back.",[
        (jump_to_menu, "mnu_choose_skill"),
        ]),
    ]
  ),

  (
    "auto_return",menu_text_color(0xFF000d2c),
    "This menu automatically returns to caller.",
    "none",
    [(change_screen_return, 0)],
    [
    ]
  ),
  ("morale_report",menu_text_color(0xFF000d2c),
   "{s1}",
   "none",
   [(call_script, "script_get_player_party_morale_values"),
    (assign, ":target_morale", reg0),
    (assign, reg1, "$g_player_party_morale_modifier_party_size"),
    (try_begin),
      (gt, reg1, 0),
      (str_store_string, s2, "@ -"),
    (else_try),
      (str_store_string, s2, "@ "),
    (try_end),

    (assign, reg2, "$g_player_party_morale_modifier_leadership"),
    (try_begin),
      (gt, reg2, 0),
      (str_store_string, s3, "@ +"),
    (else_try),
      (str_store_string, s3, "@ "),
    (try_end),

    (try_begin),
      (gt, "$g_player_party_morale_modifier_no_food", 0),
      (assign, reg7, "$g_player_party_morale_modifier_no_food"),
      (str_store_string, s5, "@^No food:  -{reg7}"),
    (else_try),
      (str_store_string, s5, "@ "),
    (try_end),
    (assign, reg3, "$g_player_party_morale_modifier_food"),
    (try_begin),
      (gt, reg3, 0),
      (str_store_string, s4, "@ +"),
    (else_try),
      (str_store_string, s4, "@ "),
    (try_end),

    (try_begin),
      (gt, "$g_player_party_morale_modifier_debt", 0),
      (assign, reg6, "$g_player_party_morale_modifier_debt"),
      (str_store_string, s6, "@^Wage debt:  -{reg6}"),
    (else_try),
      (str_store_string, s6, "@ "),
    (try_end),

    (party_get_morale, reg5, "p_main_party"),
    (store_sub, reg4, reg5, ":target_morale"),
    (try_begin),
      (gt, reg4, 0),
      (str_store_string, s7, "@ +"),
    (else_try),
      (str_store_string, s7, "@ "),
    (try_end),
    (str_store_string, s1, "@Current party morale is {reg5}.^Current party morale modifiers are:^^Base morale:  +50^Party size: {s2}{reg1}^Leadership: {s3}{reg2}^Food variety: {s4}{reg3}{s5}{s6}^Recent events: {s7}{reg4}^TOTAL:  {reg5}"),
    ],
    [
      ("continue_3dot",[],"Continue...",
       [(jump_to_menu, "mnu_reports"),
        ]
       ),
      ]
  ),

  ("faction_orders",menu_text_color(0xFF000d2c),
   "{s9}",
   "none",
   [
     (str_clear, s9),
     (store_current_hours, ":cur_hours"),
     (try_for_range, ":faction_no", factions_begin, factions_end),
       (faction_slot_eq, ":faction_no", slot_faction_state, sfs_active),
       (neq, ":faction_no", "fac_player_supporters_faction"),
       (faction_get_slot, ":faction_ai_state", ":faction_no", slot_faction_ai_state),
       (faction_get_slot, ":faction_ai_object", ":faction_no", slot_faction_ai_object),
       (faction_get_slot, ":faction_marshall", ":faction_no", slot_faction_marshall),
       (faction_get_slot, ":faction_ai_last_offensive_time", ":faction_no", slot_faction_ai_last_offensive_time),
       (faction_get_slot, ":faction_ai_offensive_max_followers", ":faction_no", slot_faction_ai_offensive_max_followers),
       (str_store_faction_name, s10, ":faction_no"),
       (store_sub, reg1, ":cur_hours", ":faction_ai_last_offensive_time"),
       (assign, reg2, ":faction_ai_offensive_max_followers"),
       (try_begin),
         (eq, ":faction_ai_state", sfai_default),
         (str_store_string, s11, "@Defending"),
       (else_try),
         (eq, ":faction_ai_state", sfai_gathering_army),
         (str_store_string, s11, "@Gathering army"),
       (else_try),
         (eq, ":faction_ai_state", sfai_attacking_center),
         (str_store_party_name, s11, ":faction_ai_object"),
         (str_store_string, s11, "@Besieging {s11}"),
       (else_try),
         (eq, ":faction_ai_state", sfai_raiding_village),
         (str_store_party_name, s11, ":faction_ai_object"),
         (str_store_string, s11, "@Raiding {s11}"),
       (else_try),
         (eq, ":faction_ai_state", sfai_attacking_enemy_army),
         (str_store_party_name, s11, ":faction_ai_object"),
         (str_store_string, s11, "@Attacking enemies around {s11}"),
       (try_end),
       (str_store_faction_name, s10, ":faction_no"),
       (try_begin),
         (lt, ":faction_marshall", 0),
         (str_store_string, s12, "@No one"),
       (else_try),
         (str_store_troop_name, s12, ":faction_marshall"),
       (try_end),
       (str_store_string, s9, "@{s9}{s10}^Current state: {s11}^Marshall: {s12}^Since the last offensive: {reg1} hours^Offensive maximum followers: {reg2}^^"),
     (try_end),
     (try_begin),
       (neg|is_between, "$g_cheat_selected_faction", factions_begin, factions_end),
       (call_script, "script_get_next_active_faction", factions_end),
       (assign, "$g_cheat_selected_faction", reg0),
     (try_end),
     (str_store_faction_name, s10, "$g_cheat_selected_faction"),
     (str_store_string, s9, "@Selected faction is: {s10}^^{s9}"),
    ],
    [
      ("faction_orders_next_faction", [],"Select next faction.",
       [
         (call_script, "script_get_next_active_faction", "$g_cheat_selected_faction"),
         (assign, "$g_cheat_selected_faction", reg0),
         (jump_to_menu, "mnu_faction_orders"),
        ]
       ),
      ("faction_orders_defend", [],"Force defend.",
       [
         (faction_set_slot, "$g_cheat_selected_faction", slot_faction_ai_state, sfai_default),
         (faction_set_slot, "$g_cheat_selected_faction", slot_faction_ai_object, -1),
         (jump_to_menu, "mnu_faction_orders"),
        ]
       ),
      ("faction_orders_gather", [],"Force gather army.",
       [
         (store_current_hours, ":cur_hours"),
         (faction_set_slot, "$g_cheat_selected_faction", slot_faction_ai_state, sfai_gathering_army),
         (faction_set_slot, "$g_cheat_selected_faction", slot_faction_ai_last_offensive_time, ":cur_hours"),
         (faction_set_slot, "$g_cheat_selected_faction", slot_faction_ai_offensive_max_followers, 1),
         (faction_set_slot, "$g_cheat_selected_faction", slot_faction_ai_object, -1),
         (jump_to_menu, "mnu_faction_orders"),
        ]
       ),
      ("faction_orders_increase_time", [],"Increase last offensive time by 24 hours.",
       [
         (faction_get_slot, ":faction_ai_last_offensive_time", "$g_cheat_selected_faction", slot_faction_ai_last_offensive_time),
         (val_sub, ":faction_ai_last_offensive_time", 24),
         (faction_set_slot, "$g_cheat_selected_faction", slot_faction_ai_last_offensive_time, ":faction_ai_last_offensive_time"),
         (jump_to_menu, "mnu_faction_orders"),
        ]
       ),
      ("faction_orders_rethink", [],"Force rethink.",
       [
         (call_script, "script_init_ai_calculation"),
         (call_script, "script_decide_faction_ai", "$g_cheat_selected_faction"),
         (jump_to_menu, "mnu_faction_orders"),
        ]
       ),
      ("faction_orders_rethink_all", [],"Force rethink for all factions.",
       [
         (call_script, "script_recalculate_ais"),
         (jump_to_menu, "mnu_faction_orders"),
        ]
       ),
      ("go_back_dot",[],"Go back.",
       [(jump_to_menu, "mnu_reports"),
        ]
       ),
      ]
  ),

  
  ("character_report",menu_text_color(0xFF000d2c),
   "{s9}",
   "none",
   [(try_begin),
      (gt, "$g_player_reading_book", 0),
      (player_has_item, "$g_player_reading_book"),
      (str_store_item_name, s8, "$g_player_reading_book"),
	  #SW - modified reading menu
      (str_store_string, s9, "@You are currently viewing {s8}."),
    (else_try),
      (assign, "$g_player_reading_book", 0),
	  #SW - modified reading menu
      (str_store_string, s9, "@You are not viewing any holocrons."),
    (try_end),
    (assign, ":num_friends", 0),
    (assign, ":num_enemies", 0),
    (str_store_string, s6, "@none"),
    (str_store_string, s8, "@none"),
    (try_for_range, ":troop_no", faction_heroes_begin, faction_heroes_end),
      (call_script, "script_troop_get_player_relation", ":troop_no"),
      (assign, ":player_relation", reg0),
      #(troop_get_slot, ":player_relation", ":troop_no", slot_troop_player_relation),
      (try_begin),
        (gt, ":player_relation", 20),
        (try_begin),
          (eq, ":num_friends", 0),
          (str_store_troop_name, s8, ":troop_no"),
        (else_try),
          (eq, ":num_friends", 1),
          (str_store_troop_name, s7, ":troop_no"),
          (str_store_string, s8, "@{s7} and {s8}"),
        (else_try),
          (str_store_troop_name, s7, ":troop_no"),
          (str_store_string, s8, "@{s7}, {s8}"),
        (try_end),
        (val_add, ":num_friends", 1),
      (else_try),
        (lt, ":player_relation", -20),
        (try_begin),
          (eq, ":num_enemies", 0),
          (str_store_troop_name, s6, ":troop_no"),
        (else_try),
          (eq, ":num_enemies", 1),
          (str_store_troop_name, s5, ":troop_no"),
          (str_store_string, s6, "@{s5} and {s6}"),
        (else_try),
          (str_store_troop_name, s5, ":troop_no"),
          (str_store_string, s6, "@{s5}, {s6}"),
        (try_end),
        (val_add, ":num_enemies", 1),
      (try_end),
    (try_end),
    (assign, reg3, "$player_honor"),
    (troop_get_slot, reg2, "trp_player", slot_troop_renown),
    (str_store_string, s9, "@Renown: {reg2}.^Honour rating: {reg3}.^Friends: {s8}.^Enemies: {s6}.^{s9}"),

    (call_script, "script_get_number_of_hero_centers", "trp_player"),
    (assign, ":no_centers", reg0),
    (try_begin),
      (gt, ":no_centers", 0),
      (try_for_range, ":i_center", 0, ":no_centers"),
        (call_script, "script_troop_get_leaded_center_with_index", "trp_player", ":i_center"),
        (assign, ":cur_center", reg0),
        (try_begin),
          (eq, ":i_center", 0),
          (str_store_party_name, s8, ":cur_center"),
        (else_try),
          (eq, ":i_center", 1),
          (str_store_party_name, s7, ":cur_center"),
          (str_store_string, s8, "@{s7} and {s8}"),
        (else_try),
          (str_store_party_name, s7, ":cur_center"),
          (str_store_string, s8, "@{s7}, {s8}"),
        (try_end),
      (try_end),
      (str_store_string, s9, "@Your estates are: {s8}.^{s9}"),
    (try_end),
    (try_begin),
      (gt, "$players_faction", 0),
      (str_store_faction_name, s8, "$players_faction"),
      (str_store_string, s9, "@You are a lord of {s8}.^{s9}"),
    (try_end),
    ],
    [
      ("continue_3dot",[],"Continue...",
       [(jump_to_menu, "mnu_reports"),
        ]
       ),
      ]
  ),

  ("party_size_report",menu_text_color(0xFF000d2c),
   "{s1}",
   "none",
   [(call_script, "script_game_get_party_companion_limit"),
    (assign, ":party_size_limit", reg0),

    (store_skill_level, ":leadership", "skl_leadership", "trp_player"),
    (val_mul, ":leadership", 5),
    (store_attribute_level, ":charisma", "trp_player", ca_charisma),

    (troop_get_slot, ":renown", "trp_player", slot_troop_renown),
    (val_div, ":renown", 25),
    (try_begin),
      (gt, ":leadership", 0),
      (str_store_string, s2, "@ +"),
    (else_try),
      (str_store_string, s2, "@ "),
    (try_end),
    (try_begin),
      (gt, ":charisma", 0),
      (str_store_string, s3, "@ +"),
    (else_try),
      (str_store_string, s3, "@ "),
    (try_end),
    (try_begin),
      (gt, ":renown", 0),
      (str_store_string, s4, "@ +"),
    (else_try),
      (str_store_string, s4, "@ "),
    (try_end),
    (assign, reg5, ":party_size_limit"),
    (assign, reg1, ":leadership"),
    (assign, reg2, ":charisma"),
    (assign, reg3, ":renown"),
    (str_store_string, s1, "@Current party size limit is {reg5}.^Current party size modifiers are:^^Base size:  +10^Leadership: {s2}{reg1}^Charisma: {s3}{reg2}^Renown: {s4}{reg3}^TOTAL:  {reg5}"),
    ],
    [
      ("continue_3dot",[],"Continue...",
       [(jump_to_menu, "mnu_reports"),
        ]
       ),
      ]
  ),

  ("faction_relations_report",menu_text_color(0xFF000d2c),
   "{s1}",
   "none",
   [(str_clear, s2),
    (try_for_range, ":cur_faction", factions_begin, factions_end),
      (faction_slot_eq, ":cur_faction", slot_faction_state, sfs_active),
      (neq, ":cur_faction", "fac_player_supporters_faction"),
      (store_relation, ":cur_relation", "fac_player_supporters_faction", ":cur_faction"),
      (try_begin),
        (ge, ":cur_relation", 90),
        (str_store_string, s3, "@Loyal"),
      (else_try),
        (ge, ":cur_relation", 80),
        (str_store_string, s3, "@Devoted"),
      (else_try),
        (ge, ":cur_relation", 70),
        (str_store_string, s3, "@Fond"),
      (else_try),
        (ge, ":cur_relation", 60),
        (str_store_string, s3, "@Gracious"),
      (else_try),
        (ge, ":cur_relation", 50),
        (str_store_string, s3, "@Friendly"),
      (else_try),
        (ge, ":cur_relation", 40),
        (str_store_string, s3, "@Supportive"),
      (else_try),
        (ge, ":cur_relation", 30),
        (str_store_string, s3, "@Favorable"),
      (else_try),
        (ge, ":cur_relation", 20),
        (str_store_string, s3, "@Cooperative"),
      (else_try),
        (ge, ":cur_relation", 10),
        (str_store_string, s3, "@Accepting"),
      (else_try),
        (ge, ":cur_relation", 0),
        (str_store_string, s3, "@Indifferent"),
      (else_try),
        (ge, ":cur_relation", -10),
        (str_store_string, s3, "@Suspicious"),
      (else_try),
        (ge, ":cur_relation", -20),
        (str_store_string, s3, "@Grumbling"),
      (else_try),
        (ge, ":cur_relation", -30),
        (str_store_string, s3, "@Hostile"),
      (else_try),
        (ge, ":cur_relation", -40),
        (str_store_string, s3, "@Resentful"),
      (else_try),
        (ge, ":cur_relation", -50),
        (str_store_string, s3, "@Angry"),
      (else_try),
        (ge, ":cur_relation", -60),
        (str_store_string, s3, "@Hateful"),
      (else_try),
        (ge, ":cur_relation", -70),
        (str_store_string, s3, "@Revengeful"),
      (else_try),
        (str_store_string, s3, "@Vengeful"),
      (try_end),
      (str_store_faction_name, s4, ":cur_faction"),
      (assign, reg1, ":cur_relation"),
      (str_store_string, s2, "@{s2}^{s4}: {reg1} ({s3})"),
    (try_end),
    (str_store_string, s1, "@Your relation with the factions are:^{s2}"),
    ],
    [
      ("continue_3dot",[],"Continue...",
       [(jump_to_menu, "mnu_reports"),
        ]
       ),
      ]
  ),


  ("camp",menu_text_color(0xFF000d2c)|mnf_scale_picture,
   #"You set up camp. What do you want to do?",
   "It's {s1} on day {reg0} of your adventure.^^{s9}^^What do you want to do?",
   "none",
   [
#SW - from Jed_Q   
########################################################################################   
	(store_current_day, reg0),
	(store_time_of_day, reg1),

(try_begin),
   (is_between, reg1, 1, 4),
 (str_store_string, s1, "@late night"),
    (else_try),
	(is_between, reg1, 4, 6),
 	(str_store_string, s1, "@dawn"),
    	(else_try),
		(is_between, reg1, 6, 8),
 		(str_store_string, s1, "@early morning"),
    		(else_try),
			(is_between, reg1, 8, 11),
 			(str_store_string, s1, "@morning"),
    			(else_try),
				(is_between, reg1, 11, 13),
 				(str_store_string, s1, "@noon"),
    				(else_try),
					(is_between, reg1, 13, 16),
 					(str_store_string, s1, "@afternoon"),
    					(else_try),
						(is_between, reg1, 16, 18),
 						(str_store_string, s1, "@late afternoon"),
   		 				(else_try),
							(is_between, reg1, 18, 20),
 							(str_store_string, s1, "@dusk"),
   		 					(else_try),
								(is_between, reg1, 20, 23),
 								(str_store_string, s1, "@evening"),
   		 						(else_try),
									(str_store_string, s1, "@midnight"),
        (try_end),


 (try_begin),
      (gt, "$g_player_reading_book", 0),
      (player_has_item, "$g_player_reading_book"),
      (str_store_item_name, s8, "$g_player_reading_book"),
      (str_store_string, s9, "@You are currently viewing {s8}."),
 (item_get_slot, ":progress", "$g_player_reading_book", slot_item_book_reading_progress),
(val_div, ":progress", 10),
 (assign, reg2, ":progress"),

     (str_store_string, s9, "@You are currently viewing {s8} ({reg2}%)."),
    (else_try),
      (assign, "$g_player_reading_book", 0),
      (str_store_string, s9, "@You are not viewing any holocrons."),
   (try_end),
########################################################################################   
   
     (assign, "$g_player_icon_state", pis_normal),
     (set_background_mesh, "mesh_pic_camp"),
    ],
    [
      ("camp_action",[],"Take an action.",
       [(jump_to_menu, "mnu_camp_action"),
        ]
       ),
#Own faction start------------------------------
      ("camp_own_faction",
       [
      (faction_slot_eq,"fac_player_supporters_faction",slot_faction_leader,"trp_player"),
       ], "Faction Management options.",		#SW - modified
       [(jump_to_menu, "mnu_own_faction"),
        ],
       ),
#Own faction end------------------------------		   	   
###################################################################################
# Autoloot: Allow item management from camp
###################################################################################
	("camp_manage_inventory",
		[],
		"Manage your party's inventory.",
		[
			(troop_clear_inventory, "trp_temp_troop"),
			(assign, "$return_menu", "mnu_camp"),
			(assign, "$inventory_menu_offset", 0),
			(jump_to_menu, "mnu_manage_loot_pool")
		]
	),
###################################################################################
# End Autoloot
###################################################################################
	   
      ("wait_here",[],"Wait here for some time.",
       [
           (assign,"$g_camp_mode", 1),
#           (assign,"$auto_menu","mnu_camp"),
           (assign, "$g_player_icon_state", pis_camping),
           (rest_for_hours_interactive, 24 * 7, 5, 1), #rest while attackable
           (change_screen_return),
        ]
       ),
      ("walk_around_menu",
		[
			#(neq,"$cheat_mode",-1),#if cheats disabled with loader... (doesn't seem to work correctly)
	    ]
		,"Walk around the ship.",
        [
			(jump_to_menu, "mnu_walk_around_choose"),
        ]
       ),	   	   
      ("configuration_menu",
		[
			#(neq,"$cheat_mode",-1),#if cheats disabled with loader... (doesn't seem to work correctly)
	    ]
		,"SWC Configuration Menu.",
        [
			(jump_to_menu, "mnu_camp_configuration"),
        ]
       ),	   
      ("cheat_menu",
		[
		#(neq,"$cheat_mode",-1),#if cheats disabled with loader... (doesn't seem to work correctly)
		
		#New Cheat protection system by Swyter -- seems that people like cheating, what a surprise. re-enabling :)
		#(mouse_get_position, pos2),
		#(position_get_y,":y",pos2),
		#(le,":y",1),
	    ]
		,"Modding/Cheat Menu (for development use).",
        [
		(jump_to_menu, "mnu_camp_cheat"),
        ]
       ),
################################################################	   
      ("resume_travelling",[],"Resume travelling.",
       [
           (change_screen_return),
        ]
       ),
      ]
  ),

  ("walk_around_choose",menu_text_color(0xFF000d2c),
   "What area of the ship do you want to walk around?",
   "none",
   [],
    [
	("walk_around_passenger_quarters",
      [],"The passenger quarters.",
	  [
		(assign,":player_entry_point",25),
		(call_script, "script_walk_around_ship", ":player_entry_point"),
	  ]
    ),
	("walk_around_cargo_hold",
      [],"The cargo hold.",
	  [
		(assign,":player_entry_point",26),
		(call_script, "script_walk_around_ship", ":player_entry_point"),
	  ]
    ),
	("walk_around_shooting_range",
      [],"The shooting range.",
	  [
		(assign,":player_entry_point",29),
		(call_script, "script_walk_around_ship", ":player_entry_point"),
	  ]
    ),		
	("walk_around_medical_bay",
      [],"The medical bay.",
	  [
		(assign,":player_entry_point",28),
		(call_script, "script_walk_around_ship", ":player_entry_point"),
	  ]
    ),	
	("walk_around_command_bridge",
      [],"The command bridge.",
	  [
		(assign,":player_entry_point",27),
		(call_script, "script_walk_around_ship", ":player_entry_point"),
	  ]
    ),
	("go_back_dot",
      [],"Go back.",
	  [
		#SW - autoloot - must switch back to 0 so other dialogs don't break
        (assign,"$g_camp_talk",0),
		(assign,"$g_walk_around_ship",0),
		(jump_to_menu, "mnu_camp"),
	  ]
    ),	
	]
  ),
  
#Own faction start------------------------------
  ("own_faction",menu_text_color(0xFF000d2c),
   "Choose an action:",
   "none",
   [
     ],
    [
      ("recruit_lords",
      [
       (assign,":num_lords",0),
       (try_for_range,":lord",reserved_knight_begin,reserved_knight_end),	#SW modified
         (troop_slot_eq, ":lord", slot_troop_occupation, slto_faction_hero),
         (val_add,":num_lords",1),
       (try_end),
       (assign,reg1,":num_lords"),
      ],"Recruit a new commander. Your faction currently has {reg1} generals.",	#SW modified
       [
		#(try_begin),
		#	(eq, "$culture_selected",1),	#culture has already been selected
	   
		       (assign,":num_centers",0),
		       (try_for_range, ":center_no", walled_centers_begin, walled_centers_end),
		         (store_faction_of_party, ":center_faction", ":center_no"),
		         (eq, ":center_faction", "fac_player_supporters_faction"),
		         (val_add,":num_centers",1),
		       (try_end),
		       (assign,":num_lords",0),
		       (try_for_range,":lord",reserved_knight_begin,reserved_knight_end),	#SW modified
		         (troop_slot_eq, ":lord", slot_troop_occupation, slto_faction_hero),
		         (val_add,":num_lords",1),
		       (try_end),
		       (try_begin),
		       (lt,":num_lords",":num_centers"),
		       (assign,":stop",0),
		       (try_for_range,":lord",reserved_knight_begin,reserved_knight_end),	#SW modified
			 (neq,":stop",1),
		         (neg|troop_slot_eq, ":lord", slot_troop_occupation, slto_faction_hero),
			 (assign,":cur_lord",":lord"),
			 (assign,":stop",1),
		       (try_end),
		       (neq,":stop",0),
		       (troop_set_slot,":cur_lord",slot_troop_change_to_faction,"fac_player_supporters_faction"),
		       (troop_set_slot,":cur_lord",slot_troop_occupation, slto_faction_hero),
		       (troop_set_slot, ":cur_lord", slot_troop_wealth, 6000),
			   #SW - I set this for all reserved_knights when you choose a culture
		       #(faction_get_slot, ":player_culture", "fac_player_supporters_faction", slot_faction_culture),
		       #(troop_set_slot, ":cur_lord", slot_troop_original_faction,":player_culture"),
		       (jump_to_menu,"mnu_own_faction"),
		       (else_try),
		         #(display_message,"@Too little territory for new commanders!"),
				 (display_message,"@You don't have enough territory for a new commander!"),
		       (try_end),
		#(else_try),
		#		(display_message,"@You must choose a culture first!"),
		#(try_end),
        ]
       ),
      ("give_territory",
      [],"Manage your territories.",	#SW modified
       [
       (assign,"$fief_no",0),
       (assign,"$cur_lord_no",0),
       (jump_to_menu,"mnu_manage_fiefs"),
       ]),
      ("change_culture",
      [],"Change your faction's culture.",
       [
       (assign,"$fief_no",0),
       (jump_to_menu,"mnu_change_culture"),
       ]),

      ("change_faction_name",[],"Change your faction's name.",
       [
		#(try_begin),
		#	(eq, "$culture_selected",1),	#culture has already been selected
			(start_presentation, "prsnt_typer"),	# name modified inside the presentation
		#(else_try),
		#	(display_message,"@You must choose a culture first!"),
		#(try_end),
        ]
       ),	   
	   
      ("back_to_camp",[],"Back to camp menu.",
       [(jump_to_menu, "mnu_camp"),
        ]
       ),
      ]
  ),
]

def fill_faction_cultures(factions, code):
  array = [];
  for faction in factions:
    for line in code:
      line = list(line)
      line[1] = faction
      array.append(tuple(line))
  return array

game_menus += [
  ("change_culture",menu_text_color(0xFF000d2c),
   "Choose a culture:^^^The culture of your Faction determine the guards in your territories, the type of recruits from your planets, and the soldiers in your commanders' armies.",	#SW - modified
   "none",
   [],
    [

  #SW - empire culture
  ("galactic_empire", [], "Galactic Empire culture",
    [
      #change the culture to empire
      (call_script, "script_change_culture_empire"),

      (display_message, "@Player Faction culture is now Galactic Empire."),
      (jump_to_menu, "mnu_own_faction"),
    ]
	),

  #SW - rebel culture
  ("rebel_alliance", [], "Rebel Alliance culture",
    [
      #change the culture to rebel
      (call_script, "script_change_culture_rebel"),

      (display_message, "@Player Faction culture is now Rebel Alliance."),
      (jump_to_menu, "mnu_own_faction"),
    ]
  ),

    #SW - hutt culture
  ("hutt_cartel", [], "Hutt Cartel culture",
    [
      #change the culture to hutt
      (call_script, "script_change_culture_hutt"),

      (display_message, "@Player Faction culture is now Hutt Cartel."),
      (jump_to_menu, "mnu_own_faction"),
    ]
  ),
  
  #TEST
  #############################################################################################################
  #SW - new human culture
  ("human", [], "Human culture",
    [
      #change the culture to human
      (call_script, "script_change_culture_human"),

      (display_message, "@Player Faction culture is now Human."),
      (jump_to_menu, "mnu_own_faction"),
    ]
  ),
  #############################################################################################################
  ("wookiee", [], "Wookiee culture",	#SW modified
    [
      #just re-use an original culture ? shouldn't it be fac_culture_3 instead of fac_huttcartel ?
      (faction_set_slot, "fac_player_supporters_faction", slot_faction_culture, "fac_culture_4"),

      #do this because we set the recruited knights original faction to fac_neutral
      ] + fill_faction_cultures(["fac_player_supporters_faction", "fac_neutral"], [
        
      (faction_set_slot, '__cur_faction', slot_faction_deserter_troop,           "trp_wookiee_deserter"),
      (faction_set_slot, '__cur_faction', slot_faction_messenger_troop,          "trp_wookiee_messenger"),
      (faction_set_slot, '__cur_faction', slot_faction_guard_troop,              "trp_wookiee_warrior"),
      (faction_set_slot, '__cur_faction', slot_faction_prison_guard_troop,       "trp_wookiee_berserker"),
      (faction_set_slot, '__cur_faction', slot_faction_spacestation_guard_troop, "trp_bacca_warrior"),
      
      (faction_set_slot, '__cur_faction', slot_faction_reinforcements_a,         "pt_faction_wookiee_reinforcements_a"),
      (faction_set_slot, '__cur_faction', slot_faction_reinforcements_b,         "pt_faction_wookiee_reinforcements_b"),
      (faction_set_slot, '__cur_faction', slot_faction_reinforcements_c,         "pt_faction_wookiee_reinforcements_c"),		  
      
      (faction_set_slot, '__cur_faction', slot_faction_tier_1_troop,             "trp_wookiee"),
      (faction_set_slot, '__cur_faction', slot_faction_tier_2_troop,             "trp_wookiee_warrior"),
      (faction_set_slot, '__cur_faction', slot_faction_tier_3_troop,             "trp_wookiee_marksman"),
      (faction_set_slot, '__cur_faction', slot_faction_tier_4_troop,             "trp_wookiee_sharpshooter"),
      (faction_set_slot, '__cur_faction', slot_faction_tier_5_troop,             "trp_bacca_warrior"),
      
      (faction_set_slot, '__cur_faction', slot_faction_patrol_unit_1,            "trp_wookiee"),
      (faction_set_slot, '__cur_faction', slot_faction_patrol_unit_2,            "trp_wookiee_warrior"),
      (faction_set_slot, '__cur_faction', slot_faction_patrol_unit_3,            "trp_wookiee_marksman")
          
      ]) + [
      
      (try_for_range,":knight", reserved_knight_begin, reserved_knight_end), #SW modified
        (troop_set_slot, ":knight", slot_troop_original_faction, "fac_neutral"),

        #new culture specific troops
      
        #clear any inventory
        (troop_clear_inventory, ":knight"),
        
        #remove all equipment
        (try_for_range, ":slot_no", 0, 9),
          (troop_set_inventory_slot, ":knight", ":slot_no", -1),
        (try_end),
        
        #change race
        (troop_set_type, ":knight", tf_wookiee),
        
        #add equipment
        (troop_add_item, ":knight", "itm_transparent_helmet_armor", 0),
        (troop_add_item, ":knight", "itm_ryyk_blade_chieftain",     0),
        (troop_add_item, ":knight", "itm_wookiee_shield_large",     0),			
        (troop_add_item, ":knight", "itm_wookiee_bowcaster",        0),
        (troop_add_item, ":knight", "itm_laser_bolts_green_rifle",  0),
    #   (troop_add_item, ":knight", "itm_speeder",                  0),
        (troop_add_item, ":knight", "itm_wookiee_fur",              0),
        
        #random equipment
        (store_random_in_range, ":rand", 0, 2),
        (try_begin),
          (eq, ":rand", 0),
          (troop_add_item, ":knight", "itm_wookiee_armor1", 0),
        (else_try),
          (troop_add_item, ":knight", "itm_wookiee_armor2", 0),
        (try_end),
        
        #equip items
        (troop_equip_items, ":knight"),
      (try_end),

      (display_message, "@Player Faction culture is now Wookiee."),
      (jump_to_menu, "mnu_own_faction"),	  
    ]
  ),
  #############################################################################################################	
  #SW - new mandalorian culture
  ("mandalorian", [], "Mandalorian culture",
    [
      #just re-use an original culture ? shouldn't it be fac_culture_3 instead of fac_huttcartel ?
      (faction_set_slot, "fac_player_supporters_faction", slot_faction_culture, "fac_culture_5"),

      #do this because we set the recruited knights original faction to fac_neutral
      ] + fill_faction_cultures(["fac_player_supporters_faction", "fac_neutral"], [
        
      (faction_set_slot, '__cur_faction', slot_faction_deserter_troop,           "trp_mandalorian_deserter"),
      (faction_set_slot, '__cur_faction', slot_faction_messenger_troop,          "trp_mandalorian_messenger"),
      (faction_set_slot, '__cur_faction', slot_faction_guard_troop,              "trp_mandalorian_soldier"),
      (faction_set_slot, '__cur_faction', slot_faction_prison_guard_troop,       "trp_mandalorian_commando"),
      (faction_set_slot, '__cur_faction', slot_faction_spacestation_guard_troop, "trp_mandalorian_crusader"),
      
      (faction_set_slot, '__cur_faction', slot_faction_reinforcements_a,         "pt_faction_mandalorian_reinforcements_a"),
      (faction_set_slot, '__cur_faction', slot_faction_reinforcements_b,         "pt_faction_mandalorian_reinforcements_b"),
      (faction_set_slot, '__cur_faction', slot_faction_reinforcements_c,         "pt_faction_mandalorian_reinforcements_c"),		  
      
      (faction_set_slot, '__cur_faction', slot_faction_tier_1_troop,             "trp_mandalorian"),
      (faction_set_slot, '__cur_faction', slot_faction_tier_2_troop,             "trp_mandalorian_soldier"),
      (faction_set_slot, '__cur_faction', slot_faction_tier_3_troop,             "trp_mandalorian_sniper"),
      (faction_set_slot, '__cur_faction', slot_faction_tier_4_troop,             "trp_mandalorian_commando"),
      (faction_set_slot, '__cur_faction', slot_faction_tier_5_troop,             "trp_mandalorian_deadeye"),
      
      (faction_set_slot, '__cur_faction', slot_faction_patrol_unit_1,            "trp_mandalorian"),
      (faction_set_slot, '__cur_faction', slot_faction_patrol_unit_2,            "trp_mandalorian_soldier"),
      (faction_set_slot, '__cur_faction', slot_faction_patrol_unit_3,            "trp_mandalorian_commando")
          
      ]) + [

      (try_for_range,":knight", reserved_knight_begin, reserved_knight_end),	#SW modified
        (troop_set_slot, ":knight", slot_troop_original_faction, "fac_neutral"),
			
        #new culture specific troops
      
        #clear any inventory
        (troop_clear_inventory, ":knight"),
        
        #remove all equipment
        (try_for_range, ":slot_no", 0, 9),
          (troop_set_inventory_slot, ":knight",":slot_no", -1),
        (try_end),
      
        #change race
        
        #unisex troops -- let's not be misogynistic :)
        (store_random_in_range, ":rand", 0, 2),
        (try_begin),
          (eq, ":rand", 0),
          (troop_set_type, ":knight", tf_female),
        (else_try),
          (troop_set_type, ":knight", tf_male),
        (try_end),
      
        #add equipment
        (troop_add_item, ":knight", "itm_grey_gloves",                      0),			
        (troop_add_item, ":knight", "itm_combat_knife",                     0),
        (troop_add_item, ":knight", "itm_laser_bolts_orange_rifle",         0),
        (troop_add_item, ":knight", "itm_mandalorian_heavy_blaster",        0),
        (troop_add_item, ":knight", "itm_westar_shield",                    0),
    #   (troop_add_item, ":knight", "itm_speeder",                          0),
        
        #random equipment
        (store_random_in_range, ":rand", 0, 4),
        (try_begin),
          (eq, ":rand", 0),
          (troop_add_item, ":knight", "itm_mandalorian_crusader_helmet",    0),
          (troop_add_item, ":knight", "itm_mandalorian_crusader_armor",     0),
          (troop_add_item, ":knight", "itm_mandalorian_crusader_boots",     0),				
        (else_try),
          (eq, ":rand", 1),
          (troop_add_item, ":knight", "itm_mandalorian_neocrusader_helmet", 0),
          (troop_add_item, ":knight", "itm_mandalorian_crusader_armor",     0),
          (troop_add_item, ":knight", "itm_mandalorian_crusader_boots",     0),
        (else_try),
          (eq, ":rand", 2),
          (troop_add_item, ":knight", "itm_mandalorian_commando_helmet",    0),
          (troop_add_item, ":knight", "itm_mandalorian_commando_armor",     0),
          (troop_add_item, ":knight", "itm_mandalorian_commando_boots",     0),
        (else_try),
          (troop_add_item, ":knight", "itm_mandalorian_sniper_helmet",      0),
          (troop_add_item, ":knight", "itm_mandalorian_sniper_armor",       0),
          (troop_add_item, ":knight", "itm_mandalorian_sniper_boots",       0),				
        (try_end),
        
        #equip items
        (troop_equip_items, ":knight"),
      (try_end),
	  
      (display_message, "@Player Faction culture is now Mandalorian."),
      (jump_to_menu, "mnu_own_faction"),
    ]
  ),

  #############################################################################################################
  #SW - new clone culture
  ("clone", [], "Clone culture",
    [
      #just re-use an original culture ? shouldn't it be fac_culture_3 instead of fac_huttcartel ?
      (faction_set_slot, "fac_player_supporters_faction", slot_faction_culture, "fac_culture_6"),

      #do this because we set the recruited knights original faction to fac_neutral
      ] + fill_faction_cultures(["fac_player_supporters_faction", "fac_neutral"], [
        
      (faction_set_slot, '__cur_faction', slot_faction_deserter_troop,           "trp_clone_deserter"),
      (faction_set_slot, '__cur_faction', slot_faction_messenger_troop,          "trp_clone_messenger"),
      (faction_set_slot, '__cur_faction', slot_faction_guard_troop,              "trp_clone_trooper_1"),
      (faction_set_slot, '__cur_faction', slot_faction_prison_guard_troop,       "trp_arc_trooper_3"),
      (faction_set_slot, '__cur_faction', slot_faction_spacestation_guard_troop, "trp_arc_trooper_4"),
      
      (faction_set_slot, '__cur_faction', slot_faction_reinforcements_a,         "pt_faction_clone_reinforcements_a"),
      (faction_set_slot, '__cur_faction', slot_faction_reinforcements_b,         "pt_faction_clone_reinforcements_b"),
      (faction_set_slot, '__cur_faction', slot_faction_reinforcements_c,         "pt_faction_clone_reinforcements_c"),
      
      (faction_set_slot, '__cur_faction', slot_faction_tier_1_troop,             "trp_clone_trooper_1"),
      (faction_set_slot, '__cur_faction', slot_faction_tier_2_troop,             "trp_clone_trooper_2"),
      (faction_set_slot, '__cur_faction', slot_faction_tier_3_troop,             "trp_clone_trooper_3"),
      (faction_set_slot, '__cur_faction', slot_faction_tier_4_troop,             "trp_clone_trooper_4"),
      (faction_set_slot, '__cur_faction', slot_faction_tier_5_troop,             "trp_clone_trooper_5"),
      
      (faction_set_slot, '__cur_faction', slot_faction_patrol_unit_1,            "trp_clone_trooper_1"),
      (faction_set_slot, '__cur_faction', slot_faction_patrol_unit_2,            "trp_clone_trooper_2"),
      (faction_set_slot, '__cur_faction', slot_faction_patrol_unit_3,            "trp_clone_trooper_3")

      ]) + [

      (try_for_range,":knight", reserved_knight_begin, reserved_knight_end),	#SW modified
        (troop_set_slot, ":knight", slot_troop_original_faction, "fac_neutral"),

        #new culture specific troops
        
        #clear any inventory
        (troop_clear_inventory, ":knight"),
        
        #remove all equipment
        (try_for_range, ":slot_no", 0, 9),
          (troop_set_inventory_slot, ":knight", ":slot_no", -1),
        (try_end),
        
        #change race
        (troop_set_type, ":knight", tf_male),
        
        #add equipment
     #  (troop_add_item, ":knight", "itm_darkgrey_gloves",               0),	
        (troop_add_item, ":knight", "itm_combat_knife",                  0),
        (troop_add_item, ":knight", "itm_laser_bolts_blue_rifle",        0),
        (troop_add_item, ":knight", "itm_clone_trooper_boots",           0),
     #  (troop_add_item, ":knight", "itm_speeder",                       0),
     
        #random equipment
        (store_random_in_range, ":rand", 0, 4),
        
        (try_begin),
          (eq, ":rand", 0),
          (troop_add_item, ":knight", "itm_clone_trooper_helmet_green",  0),
          (troop_add_item, ":knight", "itm_arc_trooper_armor_green",     0),
          (troop_add_item, ":knight", "itm_clone_trooper_gloves_green",  0),
          (troop_add_item, ":knight", "itm_dc15s",                       0),
        (else_try),
          (eq, ":rand", 1),
          (troop_add_item, ":knight", "itm_clone_trooper_helmet_blue",   0),
          (troop_add_item, ":knight", "itm_arc_trooper_armor_blue",      0),
          (troop_add_item, ":knight", "itm_clone_trooper_gloves_blue",   0),
          (troop_add_item, ":knight", "itm_dc15a",                       0),
        (else_try),
          (eq, ":rand", 2),
          (troop_add_item, ":knight", "itm_clone_trooper_helmet_red",    0),
          (troop_add_item, ":knight", "itm_arc_trooper_armor_red",       0),
          (troop_add_item, ":knight", "itm_clone_trooper_gloves_red",    0),
          (troop_add_item, ":knight", "itm_dc15a",                       0),
        (else_try),
          (troop_add_item, ":knight", "itm_clone_trooper_helmet_yellow", 0),
          (troop_add_item, ":knight", "itm_arc_trooper_armor_yellow",    0),
          (troop_add_item, ":knight", "itm_clone_trooper_gloves_yellow", 0),
          (troop_add_item, ":knight", "itm_dc15a",                       0),
        (try_end),			
        #equip items
        (troop_equip_items, ":knight"),
      (try_end),

      (display_message, "@Player Faction culture is now Clone."),
      (jump_to_menu, "mnu_own_faction"),
    ]
  ),

  #############################################################################################################	
  #swy-- new CIS culture
  ("droid", [], "Droid culture",
    [
      #just re-use an original culture ? shouldn't it be fac_culture_3 instead of fac_huttcartel ?
      #(faction_set_slot, "fac_player_supporters_faction", slot_faction_culture, "fac_culture_8"),

      #do this because we set the recruited knights original faction to fac_neutral
      ] + fill_faction_cultures(["fac_player_supporters_faction", "fac_neutral"], [
        
      (faction_set_slot, '__cur_faction', slot_faction_deserter_troop,           "trp_droid_deserter"),
      (faction_set_slot, '__cur_faction', slot_faction_messenger_troop,          "trp_droid_messenger"),
      (faction_set_slot, '__cur_faction', slot_faction_guard_troop,              "trp_oom_series_security"),
      (faction_set_slot, '__cur_faction', slot_faction_prison_guard_troop,       "trp_oom_series_security"),
      (faction_set_slot, '__cur_faction', slot_faction_spacestation_guard_troop, "trp_oom_series_marine"),
      
      (faction_set_slot, '__cur_faction', slot_faction_reinforcements_a,         "pt_faction_droid_reinforcements_a"),
      (faction_set_slot, '__cur_faction', slot_faction_reinforcements_b,         "pt_faction_droid_reinforcements_b"),
      (faction_set_slot, '__cur_faction', slot_faction_reinforcements_c,         "pt_faction_droid_reinforcements_c"),
      
      (faction_set_slot, '__cur_faction', slot_faction_tier_1_troop,             "trp_b1series"),
      (faction_set_slot, '__cur_faction', slot_faction_tier_2_troop,             "trp_b1series_assassin"),
      (faction_set_slot, '__cur_faction', slot_faction_tier_3_troop,             "trp_b2series"),
      (faction_set_slot, '__cur_faction', slot_faction_tier_4_troop,             "trp_bxseries_commando"),
      (faction_set_slot, '__cur_faction', slot_faction_tier_5_troop,             "trp_b2series_enhanced"),
      
      (faction_set_slot, '__cur_faction', slot_faction_patrol_unit_1,            "trp_b1series"),
      (faction_set_slot, '__cur_faction', slot_faction_patrol_unit_2,            "trp_oom_series_marine"),
      (faction_set_slot, '__cur_faction', slot_faction_patrol_unit_3,            "trp_b2series")

      ]) + [

      (try_for_range,":knight", reserved_knight_begin, reserved_knight_end),	#SW modified
        (troop_set_slot, ":knight", slot_troop_original_faction, "fac_neutral"),

        #new culture specific troops
        
        #clear any inventory
        (troop_clear_inventory, ":knight"),
        
        #remove all equipment
        (try_for_range, ":slot_no", 0, 9),
          (troop_set_inventory_slot, ":knight", ":slot_no", -1),
        (try_end),
        
        #change race
        (troop_set_type, ":knight", tf_battledroid),
        
        #add equipment
        (troop_add_item, ":knight", "itm_droid_parts",                   0),
        (troop_add_item, ":knight", "itm_vibro_blade1",                  0),
        (troop_add_item, ":knight", "itm_vibro_blade2",                  0),
        (troop_add_item, ":knight", "itm_laser_bolts_red_rifle",         0),
        (troop_add_item, ":knight", "itm_laser_bolts_red_rifle",         0),
		    (troop_add_item, ":knight", "itm_transparent_droid_head",        0),
		    (troop_add_item, ":knight", "itm_transparent_droid_hands",       0),
		    (troop_add_item, ":knight", "itm_transparent_droid_feet",		     0),
     #  (troop_add_item, ":knight", "itm_speeder",                       0),
     
        #random equipment
        (store_random_in_range, ":rand", 0, 4),
        
        (try_begin),
          (eq, ":rand", 0), # bxseries_commando
          (troop_add_item, ":knight", "itm_bxseries_body",               0),
          (troop_add_item, ":knight", "itm_dlt19",                       0),
          (troop_add_item, ":knight", "itm_vibro_blade1",                0),
          (troop_add_item, ":knight", "itm_vibro_blade2",                0),
        (else_try),
          (eq, ":rand", 1), # oom_series_command
          (troop_add_item, ":knight", "itm_oomseries_command_body",      0),
          (troop_add_item, ":knight", "itm_e5",                          0),
          (troop_add_item, ":knight", "itm_vibro_blade1",                0),
          (troop_add_item, ":knight", "itm_vibro_blade2",                0),
        (else_try),
          (eq, ":rand", 2), # b2series_enhanced
          (troop_add_item, ":knight", "itm_b2series_body_enhanced",      0),
          (troop_add_item, ":knight", "itm_b2series_blaster",            0),
          (troop_add_item, ":knight", "itm_b2series_attack",             0),
          (troop_add_item, ":knight", "itm_b2series_blaster",            0),
        (else_try),         # oom_series_marine
          (troop_add_item, ":knight", "itm_oomseries_marine_body",       0),
          (troop_add_item, ":knight", "itm_e5",                          0),
          (troop_add_item, ":knight", "itm_vibro_blade1",                0),
          (troop_add_item, ":knight", "itm_vibro_blade2",                0),
        (try_end),			
        #equip items
        (troop_equip_items, ":knight"),
      (try_end),

      (display_message, "@Player Faction culture is now Droid."),
      (jump_to_menu, "mnu_own_faction"),
    ]
  ),
  
  #########################################################################################
  #SW - new trandoshan culture
    ("trandoshan", [], "Trandoshan culture",
    [
      #just re-use an original culture ? shouldn't it be fac_culture_3 instead of fac_huttcartel ?
      (faction_set_slot, "fac_player_supporters_faction", slot_faction_culture, "fac_culture_7"),
    
      #do this because we set the recruited knights original faction to fac_neutral
      ] + fill_faction_cultures(["fac_player_supporters_faction", "fac_neutral"], [

      (faction_set_slot, '__cur_faction', slot_faction_deserter_troop,           "trp_trandoshan_deserter"),
      (faction_set_slot, '__cur_faction', slot_faction_messenger_troop,          "trp_trandoshan_messenger"),
      (faction_set_slot, '__cur_faction', slot_faction_guard_troop,              "trp_trandoshan_warrior"),
      (faction_set_slot, '__cur_faction', slot_faction_prison_guard_troop,       "trp_trandoshan_hunter"),
      (faction_set_slot, '__cur_faction', slot_faction_spacestation_guard_troop, "trp_trandoshan_bounty_hunter"),
      
      (faction_set_slot, '__cur_faction', slot_faction_reinforcements_a,         "pt_faction_trandoshan_reinforcements_a"),
      (faction_set_slot, '__cur_faction', slot_faction_reinforcements_b,         "pt_faction_trandoshan_reinforcements_b"),
      (faction_set_slot, '__cur_faction', slot_faction_reinforcements_c,         "pt_faction_trandoshan_reinforcements_c"),
      
      (faction_set_slot, '__cur_faction', slot_faction_tier_1_troop,             "trp_trandoshan"),
      (faction_set_slot, '__cur_faction', slot_faction_tier_2_troop,             "trp_trandoshan_warrior"),
      (faction_set_slot, '__cur_faction', slot_faction_tier_3_troop,             "trp_trandoshan_hunter"),
      (faction_set_slot, '__cur_faction', slot_faction_tier_4_troop,             "trp_trandoshan_bounty_hunter"),
      (faction_set_slot, '__cur_faction', slot_faction_tier_5_troop,             "trp_trandoshan_bounty_hunter"),
      
      (faction_set_slot, '__cur_faction', slot_faction_patrol_unit_1,            "trp_trandoshan"),
      (faction_set_slot, '__cur_faction', slot_faction_patrol_unit_2,            "trp_trandoshan_warrior"),
      (faction_set_slot, '__cur_faction', slot_faction_patrol_unit_3,            "trp_trandoshan_hunter")

      ]) + [

      (try_for_range,":knight",reserved_knight_begin,reserved_knight_end), #SW modified
        (troop_set_slot, ":knight", slot_troop_original_faction, "fac_neutral"),
        
        #new culture specific troops
        
        #clear any inventory
        (troop_clear_inventory, ":knight"),
        
        #remove all equipment
        (try_for_range, ":slot_no", 0, 9),
          (troop_set_inventory_slot, ":knight", ":slot_no", -1),
        (try_end),
        
        #change race
        
        #unitrandosanex troops -- let's not be misogynistic :) :)
        (store_random_in_range, ":rand", 0, 4),
        (try_begin),
          (ge, ":rand", 0),
          (troop_set_type, ":knight", tf_trandoshan),
        (else_try),
          (troop_set_type, ":knight", tf_male),
        (try_end),
        
        #add equipment
        (troop_add_item, ":knight", "itm_transparent_helmet",        0),
        (troop_add_item, ":knight", "itm_trandoshan_blade",          0),
        (troop_add_item, ":knight", "itm_laser_bolts_orange_rifle",  0),
        (troop_add_item, ":knight", "itm_trandoshan_acp_array_gun",  0),
    #   (troop_add_item, ":knight", "itm_speeder",                   0),
    
        #random equipment
        (store_random_in_range, ":rand", 0, 3),
        (try_begin),
          (eq, ":rand", 0),
          (troop_add_item, ":knight","itm_trandoshan_flight_suit",   0),
        (else_try),
          (troop_add_item, ":knight","itm_trandoshan_armor",         0),
        (try_end),		
        
        #equip items
        (troop_equip_items, ":knight"),
      (try_end),

      (display_message, "@Player Faction culture is now Trandoshan."),
      (jump_to_menu, "mnu_own_faction"),
    ]
	),	
	
	#########################################################################################
  
  ("back_to_faction_manag",[],"Back to faction management menu.",
    [
      (jump_to_menu, "mnu_own_faction"),
    ]
  ),
  
  ]),
#############################################################################################################		  
  ("manage_fiefs",menu_text_color(0xFF000d2c),
   "Choose a territory ({reg1} to {reg2}):",	#SW modified
   "none",
   [
   (assign,reg1,"$fief_no"),
   (assign,reg2,reg1),
   (val_add,reg2,2),
     ],
    [
      ("fief_1",[
       (assign,":num_centers",0),
       (assign,":cur_fief",-1),
       (try_for_range, ":center_no", walled_centers_begin, walled_centers_end),
         (store_faction_of_party, ":center_faction", ":center_no"),
         (eq, ":center_faction", "fac_player_supporters_faction"),
	 (val_sub,":num_centers","$fief_no"),
	 (val_sub,":num_centers",0),
	 (try_begin),
	 (eq,":num_centers",0),
	 (assign,":cur_fief",":center_no"),
	 (try_end),
	 (val_add,":num_centers","$fief_no"),
	 (val_add,":num_centers",0),
         (val_add,":num_centers",1),
       (try_end),
       (ge,":cur_fief",0),
       (party_get_slot, ":lord", ":cur_fief", slot_mainplanet_lord),
       (str_store_party_name,s2,":cur_fief"),
       (str_store_troop_name,s3,":lord"),
       (str_store_string,s1,"@{s2}, belongs to {s3}"),
      ],"{s1}",
       [
       (assign,":num_centers",0),
       (assign,"$fief_to_give",-1),
       (try_for_range, ":center_no", walled_centers_begin, walled_centers_end),
         (store_faction_of_party, ":center_faction", ":center_no"),
         (eq, ":center_faction", "fac_player_supporters_faction"),
	 (val_sub,":num_centers","$fief_no"),
	 (val_sub,":num_centers",0),
	 (try_begin),
	 (eq,":num_centers",0),
	 (assign,"$fief_to_give",":center_no"),
	 (try_end),
	 (val_add,":num_centers","$fief_no"),
	 (val_add,":num_centers",0),
         (val_add,":num_centers",1),
       (try_end),
       (ge,"$fief_to_give",0),
       (jump_to_menu,"mnu_manage_fiefs_2"),
        ]
       ),
      ("fief_2",[
       (assign,":num_centers",0),
       (assign,":cur_fief",-1),
       (try_for_range, ":center_no", walled_centers_begin, walled_centers_end),
         (store_faction_of_party, ":center_faction", ":center_no"),
         (eq, ":center_faction", "fac_player_supporters_faction"),
	 (val_sub,":num_centers","$fief_no"),
	 (val_sub,":num_centers",1),
	 (try_begin),
	 (eq,":num_centers",0),
	 (assign,":cur_fief",":center_no"),
	 (try_end),
	 (val_add,":num_centers","$fief_no"),
	 (val_add,":num_centers",1),
         (val_add,":num_centers",1),
       (try_end),
       (ge,":cur_fief",0),
       (party_get_slot, ":lord", ":cur_fief", slot_mainplanet_lord),
       (str_store_party_name,s2,":cur_fief"),
       (str_store_troop_name,s3,":lord"),
       (str_store_string,s1,"@{s2}, belongs to {s3}"),
      ],"{s1}",
       [
       (assign,":num_centers",0),
       (assign,"$fief_to_give",-1),
       (try_for_range, ":center_no", walled_centers_begin, walled_centers_end),
         (store_faction_of_party, ":center_faction", ":center_no"),
         (eq, ":center_faction", "fac_player_supporters_faction"),
	 (val_sub,":num_centers","$fief_no"),
	 (val_sub,":num_centers",1),
	 (try_begin),
	 (eq,":num_centers",0),
	 (assign,"$fief_to_give",":center_no"),
	 (try_end),
	 (val_add,":num_centers","$fief_no"),
	 (val_add,":num_centers",1),
         (val_add,":num_centers",1),
       (try_end),
       (ge,"$fief_to_give",0),
       (jump_to_menu,"mnu_manage_fiefs_2"),
        ]
       ),
      ("fief_3",[
       (assign,":num_centers",0),
       (assign,":cur_fief",-1),
       (try_for_range, ":center_no", walled_centers_begin, walled_centers_end),
         (store_faction_of_party, ":center_faction", ":center_no"),
         (eq, ":center_faction", "fac_player_supporters_faction"),
	 (val_sub,":num_centers","$fief_no"),
	 (val_sub,":num_centers",2),
	 (try_begin),
	 (eq,":num_centers",0),
	 (assign,":cur_fief",":center_no"),
	 (try_end),
	 (val_add,":num_centers","$fief_no"),
	 (val_add,":num_centers",2),
         (val_add,":num_centers",1),
       (try_end),
       (ge,":cur_fief",0),
       (party_get_slot, ":lord", ":cur_fief", slot_mainplanet_lord),
       (str_store_party_name,s2,":cur_fief"),
       (str_store_troop_name,s3,":lord"),
       (str_store_string,s1,"@{s2}, belongs to {s3}"),
      ],"{s1}",
       [
       (assign,":num_centers",0),
       (assign,"$fief_to_give",-1),
       (try_for_range, ":center_no", walled_centers_begin, walled_centers_end),
         (store_faction_of_party, ":center_faction", ":center_no"),
         (eq, ":center_faction", "fac_player_supporters_faction"),
	 (val_sub,":num_centers","$fief_no"),
	 (val_sub,":num_centers",2),
	 (try_begin),
	 (eq,":num_centers",0),
	 (assign,"$fief_to_give",":center_no"),
	 (try_end),
	 (val_add,":num_centers","$fief_no"),
	 (val_add,":num_centers",2),
         (val_add,":num_centers",1),
       (try_end),
       (ge,"$fief_to_give",0),
       (jump_to_menu,"mnu_manage_fiefs_2"),
        ]
       ),
      ("next_3dot",[],"Next...",
       [
       (val_add,"$fief_no",1),
       (jump_to_menu,"mnu_manage_fiefs"),
        ]
       ),
      ("back_3dot",[],"Back...",
       [
       (val_sub,"$fief_no",1),
       (jump_to_menu,"mnu_manage_fiefs"),
        ]
       ),
      ("back_to_camp",[],"Back to camp menu.",
       [(jump_to_menu, "mnu_camp"),
        ]
       ),
      ]
  ),
  ("manage_fiefs_2",menu_text_color(0xFF000d2c),
   "Give to commander ({reg1} to {reg2}):",	#SW modified
   "none",
   [
   (assign,reg1,"$cur_lord_no"),
   (assign,reg2,reg1),
   (val_add,reg2,2),
     ],
    [
      ("player",[
       (str_store_troop_name,s3,"trp_player"),
      ],"{s3}",
       [
       (call_script, "script_give_center_to_lord", "$fief_to_give", "trp_player", 0),
       (jump_to_menu, "mnu_camp"),
        ]
       ),
      ("lord_1",[
       (assign,":num_lords",0),
       (assign,":cur_lord_number",-1),
       (try_for_range,":lord",reserved_knight_begin,reserved_knight_end),	#SW modified
         (troop_slot_eq, ":lord", slot_troop_occupation, slto_faction_hero),
	 (val_sub,":num_lords","$cur_lord_no"),
	 (val_sub,":num_lords",0),
	 (try_begin),
	  (eq,":num_lords",0),
	  (assign,":cur_lord_number",":lord"),
	 (try_end),
	 (val_add,":num_lords","$cur_lord_no"),
	 (val_add,":num_lords",0),
         (val_add,":num_lords",1),
       (try_end),
       (ge,":cur_lord_number",0),
       (str_store_troop_name,s3,":cur_lord_number"),
      ],"{s3}",
       [
       (assign,":num_lords",0),
       (assign,":cur_lord_number",-1),
       (try_for_range,":lord",reserved_knight_begin,reserved_knight_end),	#SW modified
         (troop_slot_eq, ":lord", slot_troop_occupation, slto_faction_hero),
	 (val_sub,":num_lords","$cur_lord_no"),
	 (val_sub,":num_lords",0),
	 (try_begin),
	  (eq,":num_lords",0),
	  (assign,":cur_lord_number",":lord"),
	 (try_end),
	 (val_add,":num_lords","$cur_lord_no"),
	 (val_add,":num_lords",0),
         (val_add,":num_lords",1),
       (try_end),
       (call_script, "script_give_center_to_lord", "$fief_to_give", ":cur_lord_number", 0),
       (jump_to_menu, "mnu_camp"),
        ]
       ),
      ("lord_2",[
       (assign,":num_lords",0),
       (assign,":cur_lord_number",-1),
       (try_for_range,":lord",reserved_knight_begin,reserved_knight_end),	#SW modified
         (troop_slot_eq, ":lord", slot_troop_occupation, slto_faction_hero),
	 (val_sub,":num_lords","$cur_lord_no"),
	 (val_sub,":num_lords",1),
	 (try_begin),
	  (eq,":num_lords",0),
	  (assign,":cur_lord_number",":lord"),
	 (try_end),
	 (val_add,":num_lords","$cur_lord_no"),
	 (val_add,":num_lords",1),
         (val_add,":num_lords",1),
       (try_end),
       (ge,":cur_lord_number",0),
       (str_store_troop_name,s3,":cur_lord_number"),
      ],"{s3}",
       [
       (assign,":num_lords",0),
       (assign,":cur_lord_number",-1),
       (try_for_range,":lord",reserved_knight_begin,reserved_knight_end),	#SW modified
         (troop_slot_eq, ":lord", slot_troop_occupation, slto_faction_hero),
	 (val_sub,":num_lords","$cur_lord_no"),
	 (val_sub,":num_lords",1),
	 (try_begin),
	  (eq,":num_lords",0),
	  (assign,":cur_lord_number",":lord"),
	 (try_end),
	 (val_add,":num_lords","$cur_lord_no"),
	 (val_add,":num_lords",1),
         (val_add,":num_lords",1),
       (try_end),
       (call_script, "script_give_center_to_lord", "$fief_to_give", ":cur_lord_number", 0),
       (jump_to_menu, "mnu_camp"),
        ]
       ),
      ("lord_3",[
       (assign,":num_lords",0),
       (assign,":cur_lord_number",-1),
       (try_for_range,":lord",reserved_knight_begin,reserved_knight_end),	#SW modified
         (troop_slot_eq, ":lord", slot_troop_occupation, slto_faction_hero),
	 (val_sub,":num_lords","$cur_lord_no"),
	 (val_sub,":num_lords",2),
	 (try_begin),
	  (eq,":num_lords",0),
	  (assign,":cur_lord_number",":lord"),
	 (try_end),
	 (val_add,":num_lords","$cur_lord_no"),
	 (val_add,":num_lords",2),
         (val_add,":num_lords",1),
       (try_end),
       (ge,":cur_lord_number",0),
       (str_store_troop_name,s3,":cur_lord_number"),
      ],"{s3}",
       [
       (assign,":num_lords",0),
       (assign,":cur_lord_number",-1),
       (try_for_range,":lord",reserved_knight_begin,reserved_knight_end),	#SW modified
         (troop_slot_eq, ":lord", slot_troop_occupation, slto_faction_hero),
	 (val_sub,":num_lords","$cur_lord_no"),
	 (val_sub,":num_lords",2),
	 (try_begin),
	  (eq,":num_lords",0),
	  (assign,":cur_lord_number",":lord"),
	 (try_end),
	 (val_add,":num_lords","$cur_lord_no"),
	 (val_add,":num_lords",2),
         (val_add,":num_lords",1),
       (try_end),
       (call_script, "script_give_center_to_lord", "$fief_to_give", ":cur_lord_number", 0),
       (jump_to_menu, "mnu_camp"),
        ]
       ),
      ("next_3dot",[],"Next...",
       [
       (val_add,"$cur_lord_no",1),
       (jump_to_menu,"mnu_manage_fiefs_2"),
        ]
       ),
      ("back_3dot",[],"Back...",
       [
       (val_sub,"$cur_lord_no",1),
       (jump_to_menu,"mnu_manage_fiefs_2"),
        ]
       ),
      ("back_to_camp",[],"Back to camp menu.",
       [(jump_to_menu, "mnu_camp"),
        ]
       ),
    ]),
#Own faction end------------------------------    

##############################################################################
#SWC configuration menu
  ("camp_configuration",menu_text_color(0xFF000d2c),
   "Star Wars: Conquest Configuration Menu",
   "none",
	 [
     ],
    [
		#SW - toggle menu option concept by ConstantA - http://forums.taleworlds.net/index.php/topic,63142.msg1647442.html#msg1647442
		("config_shield_bash",
		[
		(str_clear, s1),
		(try_begin),
			(le, "$shield_bash_toggle", 0),
			(str_store_string, s1, "@Currently enabled"),
		(else_try),
			(str_store_string, s1, "@Currently disabled"),
		(try_end),
		],
		"Change Shield Bash integration ( {s1} )",                         
		[
		(try_begin),
			(le, "$shield_bash_toggle", 0),
			(assign, "$shield_bash_toggle", 1),
			(display_message, "@Shield Bash integration has been disabled."),
		(else_try),
			(assign, "$shield_bash_toggle", 0),
			(display_message, "@Shield Bash integration has been enabled."),
		(try_end),
		(str_clear, s1),
		(jump_to_menu, "mnu_camp_configuration"),
		]),  

		("config_random_scene_battles",
		[
		(assign, reg1, "$random_scene_battles"),
		],
		"Change random scene attacks ( Currently {reg1}% )",
		[
		(try_begin),
			(ge, "$random_scene_battles", 100),
			(assign, "$random_scene_battles", 0),
		(else_try),
			(val_add, "$random_scene_battles", 10),
		(try_end),
		(display_message, "@Frequency of random scene battles was modified."),
		(str_clear, s1),
		(jump_to_menu, "mnu_camp_configuration"),
		]),		

		("config_random_scene_assassination",
		[
		(assign, reg1, "$random_scene_assassination"),
		],
		"Change random assassination attempts ( Currently {reg1}% )",
		[
		(try_begin),
			(ge, "$random_scene_assassination", 100),
			(assign, "$random_scene_assassination", 0),
		(else_try),
			(val_add, "$random_scene_assassination", 10),
		(try_end),
		(display_message, "@Frequency of random assassination attempts was modified."),
		(str_clear, s1),
		(jump_to_menu, "mnu_camp_configuration"),
		]),		

		# ("config_arena_weapons",
		# [
		# (str_clear, s1),
		# (try_begin),
			# (le, "$arena_weapons", 0),
			# (str_store_string, s1, "@Currently Lightsabers"),
		# (else_try),
			# (str_store_string, s1, "@Currently Vibroweapons"),
		# (try_end),
		# ],
		# "Change Arena Weapons ( {s1} )",
		# [
		# (try_begin),
			# (le, "$arena_weapons", 0),
			# (assign, "$arena_weapons", 1),
			# #(assign, "$arena_name", "Enter the Arena"),
			# (display_message, "@Arena Weapons were switched to Vibroweapons."),
		# (else_try),
			# (assign, "$arena_weapons", 0),
			# #(assign, "$arena_name", "Enter the Force-Sensitive Arena"),
			# (display_message, "@Arena Weapons were switched to Lightsabers."),
		# (try_end),
		# (str_clear, s1),
		# (jump_to_menu, "mnu_camp_configuration"),
		# ]), 

		("config_faction_colors",
		[
		(str_clear, s1),
		(try_begin),
			(le, "$faction_colors", 0),
			(str_store_string, s1, "@Currently Empire is Blue & Rebel is Red"),
		(else_try),
			(eq, "$faction_colors", 1),
			(str_store_string, s1, "@Currently Empire is Red & Rebel is Green"),
		(else_try),
			(eq, "$faction_colors", 2),
			(str_store_string, s1, "@Currently Empire is Blue & Rebel is Green"),
		(else_try),
			(eq, "$faction_colors", 3),
			(str_store_string, s1, "@Currently Empire is White & Rebel is Red"),
		(else_try),
			(eq, "$faction_colors", 4),
			(str_store_string, s1, "@Currently Empire is White & Rebel is Green"),
		(else_try),	#default
			(str_store_string, s1, "@Currently Empire is Blue & Rebel is Red"),	
		(try_end),
		],
		"Change faction colors ( {s1} )",                         
		[
		(try_begin),
			(le, "$faction_colors", 0),
			(assign, "$faction_colors", 1),
			(faction_set_color, "fac_galacticempire", 0xCC2211),	#RED
			(faction_set_color, "fac_rebelalliance", 0x33DD33),	#GREEN					
			(display_message, "@Empire is now Red & Rebel is Green."),
		(else_try),
			(eq, "$faction_colors", 1),
			(assign, "$faction_colors", 2),
			(faction_set_color, "fac_galacticempire", 0x33DDDD),	#BLUE
			(faction_set_color, "fac_rebelalliance", 0x33DD33),	#GREEN	
			(display_message, "@Empire is now Blue & Rebel is Green."),
		(else_try),
			(eq, "$faction_colors", 2),
			(assign, "$faction_colors", 3),
			(faction_set_color, "fac_galacticempire", 0xDCDCDC),	#WHITE
			(faction_set_color, "fac_rebelalliance", 0xCE0B0B),	#RED			
			(display_message, "@Empire is now White & Rebel is Red."),
		(else_try),
			(eq, "$faction_colors", 3),
			(assign, "$faction_colors", 4),
			(faction_set_color, "fac_galacticempire", 0xDCDCDC),	#WHITE
			(faction_set_color, "fac_rebelalliance", 0x33DD33),	#GREEN	
			(display_message, "@Empire is now White & Rebel is Green."),
		(else_try),			#default
			#(eq, "$faction_colors", 4),
			(assign, "$faction_colors", 0),
			(faction_set_color, "fac_galacticempire", 0x33DDDD),	#BLUE
			(faction_set_color, "fac_rebelalliance", 0xCE0B0B),	#RED			
			(display_message, "@Empire is now Blue & Rebel is Red."),			
		(try_end),
		(str_clear, s1),
		(jump_to_menu, "mnu_camp_configuration"),
		]),  

      ("setup_keys",[],"Configure keys.",
       [(jump_to_menu, "mnu_setup_keys"),
        ]
       ),
		
      ("back_to_camp",[],"Back to camp menu.",
       [(jump_to_menu, "mnu_camp"),
        ]
       ),
		
	]),
	
#####################################################################################

    (
	#code from Expanded Gameplay III
    "setup_keys",menu_text_color(0xFF000d2c),
    "Choose ability and then press a key to assign/change its key binding. To unassign a key, choose an ability and press ESC",
    "none",
    [ 
    #^^{s11}
    #(str_clear,s11),
    (call_script,"script_get_all_binds"),
     
	#(tutorial_message, "@[J]: RAGE (req 14 Int) ^^[O] : SPRINT (req 14 Agi) ^^[T] : WHISTLE FOR HORSE  (req 14 Cha) ^^[Y] : FIRST AID (req 14 Int) ^^[U] : BATTLECRY ^^[B] : WARCRY ^^[G] : TAUNT ^^Press M to close help."),     
     
     ],
    [
      # ("help",[],"Help [{s14}]",
       # [
       # (assign,"$active_key",0),
       # (start_presentation, "prsnt_key_assignment"),
       # ]),    

      ("shield_bash",[],"Shield Bash [ block + attack ]",
       [
       #(assign,"$active_key",1),
       #(start_presentation, "prsnt_key_assignment"),
	   (display_message, "@This key cannot be modified."),
       ]),	   
	   
      ("crouch",[],"Crouch [{s15}]",
       [
       (assign,"$active_key",1),
       (start_presentation, "prsnt_key_assignment"),
       ]),

      ("toggle_weapon",[],"Toggle Weapon Capabilities [{s16}]",
       [
       (assign,"$active_key",2),
       (start_presentation, "prsnt_key_assignment"),
       ]),
	   
      ("helmet_view",[],"Helmet View [{s17}]",
       [
       (assign,"$active_key",3),
       (start_presentation, "prsnt_key_assignment"),
       ]),

      ("jetpack",[],"Jetpack / Force Jump [{s18}]",
       [
       (assign,"$active_key",4),
       (start_presentation, "prsnt_key_assignment"),
       ]),

      # ("warcry",[],"Warcry [{s19}]",
       # [
       # (assign,"$active_key",5),
       # (start_presentation, "prsnt_key_assignment"),
       # ]),
	   
      ("bacta_injector",[],"Bacta Injector [{s20}]",
       [
       (assign,"$active_key",6),
       (start_presentation, "prsnt_key_assignment"),
       ]),
	   
     # ("binoculars",[],"Macrobinoculars [{s21}]",
     #  [
      # (assign,"$active_key",7),
      # (start_presentation, "prsnt_key_assignment"),
     #  ]),
	   
      ("deathcam_forward",[],"After Death Camera - Next [{s22}]",
       [
       (assign,"$active_key",8),
       (start_presentation, "prsnt_key_assignment"),
       ]),
	   
      ("deathcam_backward",[],"After Death Camera - Previous [{s23}]",
       [
       (assign,"$active_key",9),
       (start_presentation, "prsnt_key_assignment"),
       ]),	   
	   
      ("back_to_config_menu",[],"Back to configuration menu.",
       [(jump_to_menu, "mnu_camp_configuration"),]),
     ]     
  ),		
  
##############################################################################  
  ("camp_cheat",menu_text_color(0xFF000d2c),
   #"Modding/Cheat Menu (for development use):^^This menu is intended for development use while we are working on improving this mod. If you enable this option then additonal CHEAT menu's will also appear in other game menu's. Please do not report any bugs with this functionality since it is for testing only.",
   "Modding/Cheat Menu (for development use):^^This menu is intended for development use while we are working on improving this mod. Please do not report any bugs with this functionality since it is for testing only.",
   "none",
	 [
     ],
    [
	      ("devs_island",
		[
		#(eq,"$cheat_mode",1)
		],
		"Go to the SWC Dev Island.",
		[
			(set_jump_mission,"mt_town_center"),
			(jump_to_scene, "scn_swc_dev_island"),
			(change_screen_mission),
        ]
       ),	
	
		#SW - added enable/disable camp cheat menu by ConstantA - http://forums.taleworlds.net/index.php/topic,63142.msg1647442.html#msg1647442
		("cheat_toggle",
		[
		(str_clear, s1),
		(try_begin),
			(eq, "$cheat_mode", 0),
			(str_store_string, s1, "@Enable the M&B Developers CHEAT menu's & DEBUG messages."),
		(else_try),
			(str_store_string, s1, "@Disable the M&B Developers CHEAT menu's & DEBUG messages."),
		(try_end),
		],
		"{s1}",                         
		[
		(try_begin),
			(eq, "$cheat_mode", 0),
			(assign, "$cheat_mode", 1),
			(display_message, "@CHEAT and DEBUG messages are now enabled."),
			(display_message, "@WARNING:  this mode was created by the M&B developers."),
			(display_message, "@WARNING:  Functionality is unknown and has not been tested by the SWC team."),
		(else_try),
			(assign, "$cheat_mode", 0),
			(display_message, "@CHEAT and DEBUG messages are now disabled."),
		(try_end),
		(str_clear, s1),
		(jump_to_menu, "mnu_camp_cheat"),
		]),
	
      ("cheat_walk_around",
		[
		#(eq,"$cheat_mode",1)
		],
		"Walk around a random scene.",
		[
			(set_jump_mission,"mt_ai_training"),
			(call_script, "script_setup_random_scene"),
			(change_screen_mission),
        ]
       ),	

      ("cheat_relocate_party",
	  [
	  #(eq,"$cheat_mode",1)
	  ],
	  "Relocate player to a random planet.",
       [
		(store_random_in_range, ":random_town", mainplanets_begin, mainplanets_end),
		(str_clear, s1),
		(str_store_party_name, s1, ":random_town"),
		(display_message, "@Player was moved to {s1}."),
		(str_clear, s1),
		(party_relocate_near_party, "p_main_party", ":random_town", 3),
        ]
       ),

      # ("cheat_give_planet",
	  # [(eq,"$cheat_mode",1)],
	  # "Give player a random planet.",
       # [
		# (store_random_in_range, ":random_town", mainplanets_begin, mainplanets_end),
		# (str_clear, s1),
		# (str_store_party_name, s1, ":random_town"),
		# (display_message, "@Player is now the ruler of {s1}."),
		# (str_clear, s1),
		# (call_script, "script_give_center_to_lord", ":random_town",  "trp_player", 0),
        # ]
       # ),
	   
      ("cheat_increase_renown",
	  [
	  #(eq,"$cheat_mode",1)
	  ],
	  "Increase player renown.",
       [
		(str_store_string, s1, "@Player renown is increased by 500."),
        (call_script, "script_change_troop_renown", "trp_player" ,500),
        ]
       ),

      ("cheat_change_ship_speed",
	  [
	  #(eq,"$cheat_mode",1)
	  ],
	  "Change player ship speed.",
       [
	   
	   #safety incase this variable isn't set yet
		(try_begin),
			(le, "$cheat_speed_multiplier", 0),
			(assign, "$cheat_speed_multiplier", 1),
		(try_end),

		#increase ship speed
		(try_begin),
			(eq, "$cheat_speed_multiplier", 1),
			(assign, "$cheat_speed_multiplier", 2),
			(display_message, "@Player ship speed is now 2x faster."),
		(else_try),
			(eq, "$cheat_speed_multiplier", 2),
			(assign, "$cheat_speed_multiplier", 3),
			(display_message, "@Player ship speed is now 3x faster."),
		(else_try),
			(eq, "$cheat_speed_multiplier", 3),
			(assign, "$cheat_speed_multiplier", 4),
			(display_message, "@Player ship speed is now 4x faster."),
		(else_try),
			(eq, "$cheat_speed_multiplier", 4),
			(assign, "$cheat_speed_multiplier", 5),
			(display_message, "@Player ship speed is now 5x faster."),
		(else_try),
			(assign, "$cheat_speed_multiplier", 1),
			(display_message, "@Player ship speed is reset to the default."),
		(try_end),

        ]
       ),	   
	   
      ("cheat_add_xp",
	  [
	  #(eq,"$cheat_mode",1)
	  ],
	  "Add experience to player.",
       [
		(add_xp_to_troop, 15000, "trp_player"),
		(display_message, "@Experience added to player."),
        ]
       ),
	   
############## MF for testing start ####################
#SW - camp_mod concept by MartinF - http://forums.taleworlds.net/index.php/topic,57919.0.html
### MF - Add any units you want to test with below, look in troop.py for the troop_id      
      ("camp_mod_4",
      [
	  #(eq,"$cheat_mode",1)
	  ],
      "Add mercenary units to player party.",
      [
        (party_add_members, "p_main_party", "trp_mandalorian_crusader", 5),
		(party_add_members, "p_main_party", "trp_ig88", 5),
		(party_add_members, "p_main_party", "trp_defiler", 5),
		(party_add_members, "p_main_party", "trp_bodyguard", 5),
		(party_add_members, "p_main_party", "trp_rancor", 5),		
		(party_add_members, "p_main_party", "trp_power_droid", 5),
		(party_add_members, "p_main_party", "trp_fxseries_droid", 5),
		
        (display_message, "@Party members added."),
       ]
      ),

      ("camp_mod_1",
      [
	  #(eq,"$cheat_mode",1)
	  ],
	  "Increase relations with all Factions.",
       [
		(call_script, "script_set_player_relation_with_faction", "fac_galacticempire", 40),
		(call_script, "script_set_player_relation_with_faction", "fac_rebelalliance", 40),
		(call_script, "script_set_player_relation_with_faction", "fac_huttcartel", 40),
		(display_message, "@Increased relations with all factions."),
        ]
       ),
	   
      ("camp_mod_1b",
      [
	  #(eq,"$cheat_mode",1)
	  ],
	  "Decrease relations with all Factions.",
       [
		(call_script, "script_set_player_relation_with_faction", "fac_galacticempire", -40),
		(call_script, "script_set_player_relation_with_faction", "fac_rebelalliance", -40),
		(call_script, "script_set_player_relation_with_faction", "fac_huttcartel", -40),
		(display_message, "@Decreased relations with all factions."),
        ]
       ),	   
### MF - change attributes and skills below, or add weapon proficiencies with (troop_raise_proficiency, "trp_player", wpt_). See header.troops.py for options   
      ("camp_mod_2",
      [
	  #(eq,"$cheat_mode",1)
	  ],
      "Raise player's attributes, skills, and proficiencies.",
      [
		#attributes
         (troop_raise_attribute, "trp_player",ca_intelligence,20),
         (troop_raise_attribute, "trp_player",ca_strength,20),
		 (troop_raise_attribute, "trp_player",ca_agility,20),
		 (troop_raise_attribute, "trp_player",ca_charisma,20),
		 
		 #skills
		(troop_raise_skill, "trp_player",skl_riding,10),
		(troop_raise_skill, "trp_player",skl_shield,5),		#there is a bug in M&B 1.x where the shield skill helps out the other team so don't raise it too high
		(troop_raise_skill, "trp_player",skl_spotting,10),
		(troop_raise_skill, "trp_player",skl_pathfinding,10),
		(troop_raise_skill, "trp_player",skl_trainer,10),
		(troop_raise_skill, "trp_player",skl_leadership,10),
		(troop_raise_skill, "trp_player",skl_trade,10),
		(troop_raise_skill, "trp_player",skl_prisoner_management,10),
		(troop_raise_skill, "trp_player", skl_athletics, 10),
		(troop_raise_skill, "trp_player", skl_power_strike, 10),
		(troop_raise_skill, "trp_player", skl_power_draw, 10),
		(troop_raise_skill, "trp_player", skl_power_throw, 10),
		(troop_raise_skill, "trp_player", skl_weapon_master, 10),
		(troop_raise_skill, "trp_player", skl_horse_archery, 10),
		(troop_raise_skill, "trp_player", skl_ironflesh, 10),
		(troop_raise_skill, "trp_player", skl_inventory_management, 10),
	
		#proficiencies
		(troop_raise_proficiency_linear, "trp_player", wpt_one_handed_weapon, 350),
		(troop_raise_proficiency_linear, "trp_player", wpt_two_handed_weapon, 350),
		(troop_raise_proficiency_linear, "trp_player", wpt_polearm, 350),
		(troop_raise_proficiency_linear, "trp_player", wpt_archery, 350),
		(troop_raise_proficiency_linear, "trp_player", wpt_crossbow, 350),
		(troop_raise_proficiency_linear, "trp_player", wpt_throwing, 350),
		(troop_raise_proficiency_linear, "trp_player", wpt_firearm, 350),	 
		 
		(display_message, "@Attributes, skills and proficiencies raised."),
		]
      ),      

### MF - Change items below to anything you want to test out, look in items.py for item_id
     ("camp_mod_3",
     [
	 #(eq,"$cheat_mode",1)
	 ],
      "Add credits and equipment to player.",
		[
		#gold
		(troop_add_gold, "trp_player", 100000),
   
		#equipment
		(troop_add_item, "trp_player","itm_grey_gloves",0),
		#(troop_add_item, "trp_player","itm_mandalorian_beskar_helmet",0),
		#(troop_add_item, "trp_player","itm_mandalorian_beskar_armor",0),
		#(troop_add_item, "trp_player","itm_mandalorian_beskar_boots",0),
		#(troop_add_item, "trp_player","itm_mandalorian_heavy_blaster",0),
		(troop_add_item, "trp_player","itm_boba_fett_helmet",0),
		(troop_add_item, "trp_player","itm_boba_fett_armor",0),
		(troop_add_item, "trp_player","itm_boba_fett_boots",0),
		(troop_add_item, "trp_player","itm_boba_fett_blaster",0),		
		(troop_add_item, "trp_player","itm_laser_bolts_yellow_rifle",0),
		(troop_add_item, "trp_player","itm_lightsaber_yellow",0),
		(troop_add_item, "trp_player","itm_energy_shield_yellow_medium",0),
		(troop_add_item, "trp_player","itm_speeder_fc20",0),
		(troop_add_item, "trp_player","itm_jetpack",0),
		(troop_add_item, "trp_player","itm_force_choke",0),
		(troop_add_item, "trp_player","itm_dlt19_scope",0),
		
		#testing stormtrooper equipment
		(troop_add_item, "trp_player","itm_e11",0),
		#(troop_add_item, "trp_player","itm_imperial_stormtrooper_gloves",0),
		#(troop_add_item, "trp_player","itm_imperial_stormtrooper_boots",0),
		#(troop_add_item, "trp_player","itm_imperial_stormtrooper_helmet",0),
		#(troop_add_item, "trp_player","itm_imperial_stormtrooper_armor",0),
		
		# #testing new melee weapons
		# (troop_add_item, "trp_player","itm_gamorrean_axe_1h",0),
		# (troop_add_item, "trp_player","itm_gamorrean_axe_2h",0),
		# (troop_add_item, "trp_player","itm_vibro_axe_medium_1h",0),
		# (troop_add_item, "trp_player","itm_vibro_axe_medium_2h",0),
		# (troop_add_item, "trp_player","itm_vibro_axe_long_1h",0),
		# (troop_add_item, "trp_player","itm_vibro_axe_long_2h",0),
		
		#testing new female armor
		# (troop_add_item, "trp_player","itm_female_leather_a",0),
		# (troop_add_item, "trp_player","itm_female_leather_b",0),
		# (troop_add_item, "trp_player","itm_female_leather_c",0),
		# (troop_add_item, "trp_player","itm_black_boots",0),
		# (troop_add_item, "trp_player","itm_leather_boots",0),
		(troop_add_item, "trp_player","itm_lightsaber_red_multikill",0),
		#(troop_add_item, "trp_player","itm_tfu_stormie",0),
		
		
		
		#Transparent Items
		(troop_add_item, "trp_player","itm_transparent_body",0),
		(troop_add_item, "trp_player","itm_transparent_head",0),
		(troop_add_item, "trp_player","itm_transparent_hands",0),
		(troop_add_item, "trp_player","itm_transparent_feet",0),
		
		# #testing surrealarms items
		# (troop_add_item, "trp_player","itm_female_dress_a",0),
		# (troop_add_item, "trp_player","itm_female_dress_b",0),
		# (troop_add_item, "trp_player","itm_female_dancer_outfit_a",0),
		# (troop_add_item, "trp_player","itm_female_dancer_outfit_a_cloak",0),
		# (troop_add_item, "trp_player","itm_female_dancer_boots",0),
		
		#testing pistol animations
		# (troop_add_item, "trp_player","itm_ig88_dlt20a",0),
		# (troop_add_item, "trp_player","itm_DH17",0),
		# (troop_add_item, "trp_player","itm_se14r",0),
		# (troop_add_item, "trp_player","itm_DL44a",0),
		# (troop_add_item, "trp_player","itm_DL44b",0),
		# (troop_add_item, "trp_player","itm_Q2",0),
		# (troop_add_item, "trp_player","itm_elg3a",0),
		# (troop_add_item, "trp_player","itm_scout_trooper_pistol",0),
		# (troop_add_item, "trp_player","itm_ddc_defender",0),
		# (troop_add_item, "trp_player","itm_geonosian_sonic_pistol",0),
		# (troop_add_item, "trp_player","itm_dl18",0),
		# (troop_add_item, "trp_player","itm_westar",0),
		# (troop_add_item, "trp_player","itm_ion_pistol",0),
		# (troop_add_item, "trp_player","itm_trandoshan_supressor",0),
		
		(troop_equip_items, "trp_player"),
		
		#items
        (troop_add_item, "trp_player","itm_protein_pack",0),
		# (troop_add_item, "trp_player","itm_protein_pack",0),
        (troop_add_item, "trp_player","itm_carbohydrate_pack",0),
		# (troop_add_item, "trp_player","itm_carbohydrate_pack",0),
		(troop_add_item, "trp_player","itm_bacta_injector",0),
		(troop_add_item, "trp_player","itm_bacta_capsule",0),
		# (troop_add_item, "trp_player","itm_bacta_capsule",0),
		# (troop_add_item, "trp_player","itm_bacta_capsule",0),
		# (troop_add_item, "trp_player","itm_bacta_capsule",0),
		# (troop_add_item, "trp_player","itm_bacta_capsule",0),
		(troop_add_item, "trp_player","itm_ammo_belt_pistol",0),
		(troop_add_item, "trp_player","itm_ammo_belt_rifle",0),
		(troop_add_item, "trp_player","itm_speeder_rebel",0),
		
	    (display_message, "@Credits & equipment added to player."),
        ]
       ),
      
### MF - Spawn any party you want near your party. Look in party_templates.py for pt_id
      ("camp_mod_5",
      [
	  #(eq,"$cheat_mode",1)
	  ],
      "Spawn a party nearby.",
      [
         (spawn_around_party, "p_main_party", "pt_jawas"),
         (display_message, "@Party spawned nearby."),
      ]
      ),
 
############## MF for testing end ####################	

##@> Swyter > Custom Item adder
    #  ("swy_item_adder",
    #  [
    #(eq,"$cheat_mode",1)
    #],
    #  "Swyter's Item adder",
    #  [
    # (start_presentation, "prsnt_typer"),
    #     (troop_add_item, "trp_player",s10,0),
    #  ]
    #  ),
 
############## MF for testing end ####################	

      ("cheat_build_upgrades",
	  [
	  #(eq,"$cheat_mode",1)
	  ],
	  "Build all minor planet upgrades.",
       [
		(try_for_range, ":cur_place", minorplanet_begin, minorplanet_end),
			(party_set_slot, ":cur_place", slot_center_has_clone_chambers, 1),
			(party_set_slot, ":cur_place", slot_center_has_temple, 1),
			(party_set_slot, ":cur_place", slot_center_has_droid_foundry, 1),
			(party_set_slot, ":cur_place", slot_center_has_rancor_pit, 1),
    (try_end),
		(display_message, "@Clone Chambers, Temples, Droid Foundries, and Rancor Pits were added to all planets."),
        ]
       ),

      # ("cheat_heal_player",
	  # [(eq,"$cheat_mode",1)],
	  # "Heal player.",
       # [
		# (agent_set_hit_points,"$g_player_troop",100,0),
		# (display_message, "@Player was healed."),
        # ]
       # ),

      ("cheat_next_page",
	  [
	  #(eq,"$cheat_mode",1)
	  ],
	  "Next page.",
       [(jump_to_menu, "mnu_camp_cheat_2"),
        ]
       ),
	   
      ("back_to_camp",[],"Back to camp menu.",
       [(jump_to_menu, "mnu_camp"),
        ]
       ),
	]
  ),
  
  ("camp_cheat_2",menu_text_color(0xFF000d2c),
   #"Modding/Cheat Menu (for development use):^^This menu is intended for development use while we are working on improving this mod. If you enable this then additonal CHEAT menu's will also appear in other game menu's.",
   "Modding/Cheat Menu (for development use):^^This menu is intended for development use while we are working on improving this mod. Please do not report any bugs with this functionality since it is for testing only.",
   "none",
	 [
     ],
    [
      ("cheat_infest_planet",
	  [
	  #(eq,"$cheat_mode",1)
	  ],
	  "Infest all villages with bandits.",
       [
		(try_for_range, ":cur_place", minorplanet_begin, minorplanet_end),
			(party_set_slot, ":cur_place", slot_minorplanet_infested_by_bandits, "trp_bandit"),
        (try_end),
		(display_message, "@All planets are now infested by bandits."),
        ]
       ),

      ("cheat_increase_planet_relationship",
	  [
	  #(eq,"$cheat_mode",1)
	  ],
	  "Increase relationship with all villages.",
       [
		(try_for_range, ":cur_place", minorplanet_begin, minorplanet_end),
			(party_set_slot, ":cur_place", slot_center_player_relation, 100),
        (try_end),
		(display_message, "@All village relationships were increased to 100."),
        ]
       ),

      ("cheat_decrease_planet_relationship",
	  [
	  #(eq,"$cheat_mode",1)
	  ],
	  "Decrease relationship with all villages.",
       [
		(try_for_range, ":cur_place", minorplanet_begin, minorplanet_end),
			(party_set_slot, ":cur_place", slot_center_player_relation, -100),
        (try_end),
		(display_message, "@All village relationships were decreased to -100."),
        ]
       ),	   
	   
      ("cheat_relocate_fs_trainer",
	  [
	  #(eq,"$cheat_mode",1),
	  ],
	  "Relocate a Force-Sensitive Trainer to the closest planet.",
       [
		#SW - script_setup_random_scene is based on the closest town, determine its name
		(assign, ":closest_dist",100000),
		(assign, ":closest_town", -1),
		(try_for_range, ":cur_town", mainplanets_begin, mainplanets_end),
			(store_distance_to_party_from_party, ":dist", ":cur_town","p_main_party"),
			(lt, ":dist", ":closest_dist"),
				(assign, ":closest_dist", ":dist"),
				(assign, ":closest_town", ":cur_town"),
		(try_end),
		(str_store_party_name, s1, ":closest_town"),
	    #relocate merchant
		(store_random_in_range, ":troop_no", tavern_fs_trainer_begin, tavern_fs_trainer_end),
		(party_set_slot, ":closest_town", slot_center_tavern_bookseller, ":troop_no"),
		(display_message, "@A Force-Sensitive Trainer was moved to {s1}."),
        ]
       ),

      ("cheat_relocate_clone_merchant",
	  [
	  #(eq,"$cheat_mode",1),
	  ],
	  "Relocate a Clone Wars Era merchant to the closest planet.",
       [
		#SW - script_setup_random_scene is based on the closest town, determine its name
		(assign, ":closest_dist",100000),
		(assign, ":closest_town", -1),
		(try_for_range, ":cur_town", mainplanets_begin, mainplanets_end),
			(store_distance_to_party_from_party, ":dist", ":cur_town","p_main_party"),
			(lt, ":dist", ":closest_dist"),
				(assign, ":closest_dist", ":dist"),
				(assign, ":closest_town", ":cur_town"),
		(try_end),
		(str_store_party_name, s1, ":closest_town"),
	    #relocate merchant
		(store_random_in_range, ":troop_no", tavern_ce_merchant_begin, tavern_ce_merchant_end),
		(party_set_slot, ":closest_town", slot_center_tavern_bookseller, ":troop_no"),
		(display_message, "@A Clone Wars Era merchant was moved to {s1}."),
        ]
       ),

      ("cheat_relocate_droid_merchant",
	  [
	  #(eq,"$cheat_mode",1),
	  ],
	  "Relocate a Droid Parts merchant to the closest planet.",
       [
		#SW - script_setup_random_scene is based on the closest town, determine its name
		(assign, ":closest_dist",100000),
		(assign, ":closest_town", -1),
		(try_for_range, ":cur_town", mainplanets_begin, mainplanets_end),
			(store_distance_to_party_from_party, ":dist", ":cur_town","p_main_party"),
			(lt, ":dist", ":closest_dist"),
				(assign, ":closest_dist", ":dist"),
				(assign, ":closest_town", ":cur_town"),
		(try_end),
		(str_store_party_name, s1, ":closest_town"),
	    #relocate merchant
		(store_random_in_range, ":troop_no", tavern_dp_merchant_begin, tavern_dp_merchant_end),
		(party_set_slot, ":closest_town", slot_center_tavern_bookseller, ":troop_no"),
		(display_message, "@A Droid Parts merchant was moved to {s1}."),
        ]
       ),	   

      ("cheat_relocate_plastic_merchant",
	  [
	  #(eq,"$cheat_mode",1),
	  ],
	  "Relocate a Plastic Surgeon to the closest planet.",
       [
		#SW - script_setup_random_scene is based on the closest town, determine its name
		(assign, ":closest_dist",100000),
		(assign, ":closest_town", -1),
		(try_for_range, ":cur_town", mainplanets_begin, mainplanets_end),
			(store_distance_to_party_from_party, ":dist", ":cur_town","p_main_party"),
			(lt, ":dist", ":closest_dist"),
				(assign, ":closest_dist", ":dist"),
				(assign, ":closest_town", ":cur_town"),
		(try_end),
		(str_store_party_name, s1, ":closest_town"),
	    #relocate merchant
		(store_random_in_range, ":troop_no", tavern_ps_merchant_begin, tavern_ps_merchant_end),
		(party_set_slot, ":closest_town", slot_center_tavern_bookseller, ":troop_no"),
		(display_message, "@A Plastic Surgeon was moved to {s1}."),
        ]
       ),

      ("cheat_relocate_npc",
	  [
	  #(eq,"$cheat_mode",1),
	  ],
	  "Relocate a random NPC to the closest planet.",
       [
		#SW - script_setup_random_scene is based on the closest town, determine its name
		(assign, ":closest_dist",100000),
		(assign, ":closest_town", -1),
		(try_for_range, ":cur_town", mainplanets_begin, mainplanets_end),
			(store_distance_to_party_from_party, ":dist", ":cur_town","p_main_party"),
			(lt, ":dist", ":closest_dist"),
				(assign, ":closest_dist", ":dist"),
				(assign, ":closest_town", ":cur_town"),
		(try_end),
		(str_store_party_name, s1, ":closest_town"),
	    #remove all npc's from taverns
		(try_for_range, ":troop_no", companions_begin, companions_end),
			(troop_set_slot, ":troop_no", slot_troop_cur_center, -1),
		(try_end),
		#relocate a random npc
		(store_random_in_range, ":troop_no", companions_begin, companions_end),
		(str_store_troop_name, s2, ":troop_no"),
		(try_begin),
			(troop_slot_eq, ":troop_no", slot_troop_occupation, 0),
			(troop_set_slot, ":troop_no", slot_troop_cur_center, ":closest_town"),
			(display_message, "@{s2} was moved to {s1}."),
		(else_try),
			(display_message, "@{s2} is already in your party, please try again."),
		(try_end),
        ]
       ),
	   
      ("prev_page_dot",[],"Previous page.",
       [(jump_to_menu, "mnu_camp_cheat"),
        ]
       ),
	   
      ("back_to_camp",[],"Back to camp menu.",
       [(jump_to_menu, "mnu_camp"),
        ]
       ),
	   
	]
  ),

##############################################################################
  ("camp_action",menu_text_color(0xFF000d2c),
   "Choose an action:",
   "none",
   [
     ],
    [
      ("camp_recruit_prisoners",
       [(troops_can_join, 1),
        (store_current_hours, ":cur_time"),
        (val_sub, ":cur_time", 24),
        (gt, ":cur_time", "$g_prisoner_recruit_last_time"),
        (try_begin),
          (gt, "$g_prisoner_recruit_last_time", 0),
          (assign, "$g_prisoner_recruit_troop_id", 0),
          (assign, "$g_prisoner_recruit_size", 0),
          (assign, "$g_prisoner_recruit_last_time", 0),
        (try_end),
        ], "Recruit some of your prisoners to your party.",
       [(jump_to_menu, "mnu_camp_recruit_prisoners"),
        ],
       ),
	   #SW - modified book reading menu
      ("action_read_book",[],"Select a holocron to view.",
       [(jump_to_menu, "mnu_camp_action_read_book"),
        ]
       ),
	   #SW - modified so you can change your ship (nevermind, MF improved code with a shipyard)
      # ("action_change_ship",[],"Buy a spaceship.",
       # [(jump_to_menu, "mnu_camp_action_change_ship"),
        # ]
       # ),
	   #SW - modified so you can change your race
      ("action_change_race",[],"Change your race.",
       [(jump_to_menu, "mnu_camp_action_change_race"),
        ]
       ),	   
	  #SW - modified it so you can modify your banner
      #("action_modify_banner",[(eq, "$cheat_mode", 1)],"Cheat: Modify your banner.",
	  ("action_modify_banner",[],"Modify your banner.",
       [
		   #SW - trying to fix the bug when s0 is displayed at the bottom of the banner section (nevermind, fixed it in export_import_npcs menu)
		   #(str_clear, s0),
           (start_presentation, "prsnt_banner_selection"),
           #(start_presentation, "prsnt_custom_banner"),
        ]
       ),
################################################################
#SW - from Jed_Q
      ("Tidy_up_your_inventory",[],"Sort your inventory.",
       [
       (troop_sort_inventory, "trp_player"), 
		(display_message, "@Inventory sorted.", 0xFFFFFF),
        ]
       ),
################################################################	   
      ("action_retire",[],"Retire from adventuring.",
       [(jump_to_menu, "mnu_retirement_verify"),
        ]
       ),
#### export/import NPCs begin #### by rubik - http://forums.taleworlds.net/index.php/topic,61239.0.html
      ("action_export_import",[],"Export/Import NPCs.",
        [
          (assign, "$g_player_troop", "trp_player"),
          (jump_to_menu, "mnu_export_import_npcs"),
        ]
      ),
#### export/import NPCs end ####	   

########################################################
## Easy regulars upgrading kit begin
########################################################
    ("camp_upgrade_troops",
      [
        (call_script, "script_has_enough_slot"),
        (eq, reg0, 1),
      ],
    "Upgrade your troops.", [(jump_to_menu, "mnu_ready_upgrade")]),
    
    ("camp_upgrade_troops_no",
      [
        (call_script, "script_has_enough_slot"),
        (eq, reg0, 0),
        (disable_menu_option),
      ],
    "No slot for upgrading.", []),
########################################################
## Easy regulars upgrading kit end
########################################################

      ("action_swc_readme",[],"Star Wars: Conquest - FAQ & Notes.",
        [
          (jump_to_menu, "mnu_swc_readme"),
        ]
      ),
      ("back_to_camp",[],"Back to camp menu.",
       [(jump_to_menu, "mnu_camp"),
        ]
       ),
      ]
  ),
 
  #"Export/Import NPCs^^Instructions:^^1) click on their name^2) press the 'C' key^3) click Statistics^4) Choose to Export/Import^5) click 'Done' when you are finished",
  #################################################################################################
  #SW - added ability to export or import NPC's
    #### export/import NPCs begin ####	code by rubik - http://forums.taleworlds.net/index.php/topic,61239.0.html
  ("export_import_npcs", mnf_enable_hot_keys,
   "Export/Import NPCs^^Instructions:^^1) click on their name^2) press the 'C' key^3) click Statistics^4) Choose to Export/Import^5) click 'Done' when you are finished^^Current selection:  {reg0?{s0}:none}",
   "none",
    [
      (assign, reg0, "$g_player_troop"),
      (str_store_troop_name, s0, "$g_player_troop"),
    ],
    [
      ("go_back",[],"Go back",
        [
          (assign, "$g_player_troop", "trp_player"),
          (set_player_troop, "$g_player_troop"),
		  #SW - modified to clear the s0 string
		  (str_clear, s0),
          (jump_to_menu, "mnu_camp_action"),
        ]
      ),
     
      ("export_import_npc1", [(str_store_troop_name, s0, "trp_npc1")], "{s0}",
        [
          (assign, "$g_player_troop", "trp_npc1"),
          (set_player_troop, "$g_player_troop"),
        ]
      ),
      ("export_import_npc2", [(str_store_troop_name, s0, "trp_npc2")], "{s0}",
        [
          (assign, "$g_player_troop", "trp_npc2"),
          (set_player_troop, "$g_player_troop"),
        ]
      ),
      ("export_import_npc3", [(str_store_troop_name, s0, "trp_npc3")], "{s0}",
        [
          (assign, "$g_player_troop", "trp_npc3"),
          (set_player_troop, "$g_player_troop"),
        ]
      ),
      ("export_import_npc4", [(str_store_troop_name, s0, "trp_npc4")], "{s0}",
        [
          (assign, "$g_player_troop", "trp_npc4"),
          (set_player_troop, "$g_player_troop"),
        ]
      ),
      ("export_import_npc5", [(str_store_troop_name, s0, "trp_npc5")], "{s0}",
        [
          (assign, "$g_player_troop", "trp_npc5"),
          (set_player_troop, "$g_player_troop"),
        ]
      ),
      ("export_import_npc6", [(str_store_troop_name, s0, "trp_npc6")], "{s0}",
        [
          (assign, "$g_player_troop", "trp_npc6"),
          (set_player_troop, "$g_player_troop"),
        ]
      ),
      ("export_import_npc7", [(str_store_troop_name, s0, "trp_npc7")], "{s0}",
        [
          (assign, "$g_player_troop", "trp_npc7"),
          (set_player_troop, "$g_player_troop"),
        ]
      ),
      ("export_import_npc8", [(str_store_troop_name, s0, "trp_npc8")], "{s0}",
        [
          (assign, "$g_player_troop", "trp_npc8"),
          (set_player_troop, "$g_player_troop"),
        ]
      ),
     
      ("next_page",[],"Next page", [(jump_to_menu, "mnu_export_import_npcs_2")]),
    ]
  ),
 
  ("export_import_npcs_2", mnf_enable_hot_keys,
    "Export/Import NPCs^^Instructions:^^1) click on their name^2) press the 'C' key^3) click Statistics^4) Choose to Export/Import^5) click 'Done' when you are finished^^Current selection:  {reg0?{s0}:none}",
    "none",
     [
       (assign, reg0, "$g_player_troop"),
       (str_store_troop_name, s0, "$g_player_troop"),
     ],
    [
      ("prev_page",[],"Previous page", [(jump_to_menu, "mnu_export_import_npcs")]),
     
      ("export_import_npc9", [(str_store_troop_name, s0, "trp_npc9")], "{s0}",
        [
          (assign, "$g_player_troop", "trp_npc9"),
          (set_player_troop, "$g_player_troop"),
        ]
      ),
      ("export_import_npc10", [(str_store_troop_name, s0, "trp_npc10")], "{s0}",
        [
          (assign, "$g_player_troop", "trp_npc10"),
          (set_player_troop, "$g_player_troop"),
        ]
      ),
      ("export_import_npc11", [(str_store_troop_name, s0, "trp_npc11")], "{s0}",
        [
          (assign, "$g_player_troop", "trp_npc11"),
          (set_player_troop, "$g_player_troop"),
        ]
      ),
      ("export_import_npc12", [(str_store_troop_name, s0, "trp_npc12")], "{s0}",
        [
          (assign, "$g_player_troop", "trp_npc12"),
          (set_player_troop, "$g_player_troop"),
        ]
      ),
      ("export_import_npc13", [(str_store_troop_name, s0, "trp_npc13")], "{s0}",
        [
          (assign, "$g_player_troop", "trp_npc13"),
          (set_player_troop, "$g_player_troop"),
        ]
      ),
      ("export_import_npc14", [(str_store_troop_name, s0, "trp_npc14")], "{s0}",
        [
          (assign, "$g_player_troop", "trp_npc14"),
          (set_player_troop, "$g_player_troop"),
        ]
      ),
      ("export_import_npc15", [(str_store_troop_name, s0, "trp_npc15")], "{s0}",
        [
          (assign, "$g_player_troop", "trp_npc15"),
          (set_player_troop, "$g_player_troop"),
        ]
      ),
      ("export_import_npc16", [(str_store_troop_name, s0, "trp_npc16")], "{s0}",
        [
          (assign, "$g_player_troop", "trp_npc16"),
          (set_player_troop, "$g_player_troop"),
        ]
      ),
	  #SW - new Droid NPC's
      ("export_import_npc17", [(str_store_troop_name, s0, "trp_npc17")], "{s0}",
        [
          (assign, "$g_player_troop", "trp_npc17"),
          (set_player_troop, "$g_player_troop"),
        ]
      ),
	  #SW - new Droid NPC's
      ("export_import_npc18", [(str_store_troop_name, s0, "trp_npc18")], "{s0}",
        [
          (assign, "$g_player_troop", "trp_npc18"),
          (set_player_troop, "$g_player_troop"),
        ]
      ),	  
    ]
  ),
    #### export/import NPCs end ####  
#################################################################################################	
  
  ("camp_recruit_prisoners",menu_text_color(0xFF000d2c),
   "You offer your prisoners freedom if they agree to join you as soldiers. {s18}",
   "none",
   [(assign, ":num_regular_prisoner_slots", 0),
    (party_get_num_prisoner_stacks, ":num_stacks", "p_main_party"),
    (try_for_range, ":cur_stack", 0, ":num_stacks"),
      (party_prisoner_stack_get_troop_id, ":cur_troop_id", "p_main_party", ":cur_stack"),
      (neg|troop_is_hero, ":cur_troop_id"),
      (val_add, ":num_regular_prisoner_slots", 1),
    (try_end),
    (try_begin),
      (eq, ":num_regular_prisoner_slots", 0),
      (jump_to_menu, "mnu_camp_no_prisoners"),
    (else_try),
      (eq, "$g_prisoner_recruit_troop_id", 0),
      (store_current_hours, "$g_prisoner_recruit_last_time"),
      (store_random_in_range, ":rand", 0, 100),
      (store_skill_level, ":persuasion_level", "skl_persuasion", "trp_player"),
      (store_sub, ":reject_chance", 15, ":persuasion_level"),
      (val_mul, ":reject_chance", 4),
      (try_begin),
        (lt, ":rand", ":reject_chance"),
        (assign, "$g_prisoner_recruit_troop_id", -7),
      (else_try),
        (assign, ":num_regular_prisoner_slots", 0),
        (party_get_num_prisoner_stacks, ":num_stacks", "p_main_party"),
        (try_for_range, ":cur_stack", 0, ":num_stacks"),
          (party_prisoner_stack_get_troop_id, ":cur_troop_id", "p_main_party", ":cur_stack"),
          (neg|troop_is_hero, ":cur_troop_id"),
          (val_add, ":num_regular_prisoner_slots", 1),
        (try_end),
        (store_random_in_range, ":random_prisoner_slot", 0, ":num_regular_prisoner_slots"),
        (try_for_range, ":cur_stack", 0, ":num_stacks"),
          (party_prisoner_stack_get_troop_id, ":cur_troop_id", "p_main_party", ":cur_stack"),
          (neg|troop_is_hero, ":cur_troop_id"),
          (val_sub, ":random_prisoner_slot", 1),
          (lt, ":random_prisoner_slot", 0),
          (assign, ":num_stacks", 0),
          (assign, "$g_prisoner_recruit_troop_id", ":cur_troop_id"),
          (party_prisoner_stack_get_size, "$g_prisoner_recruit_size", "p_main_party", ":cur_stack"),
        (try_end),
      (try_end),

      (try_begin),
        (gt, "$g_prisoner_recruit_troop_id", 0),
        (party_get_free_companions_capacity, ":capacity", "p_main_party"),
        (val_min, "$g_prisoner_recruit_size", ":capacity"),
        (assign, reg1, "$g_prisoner_recruit_size"),
        (gt, "$g_prisoner_recruit_size", 0),
        (try_begin),
          (gt, "$g_prisoner_recruit_size", 1),
          (assign, reg2, 1),
        (else_try),
          (assign, reg2, 0),
        (try_end),
        (str_store_troop_name_by_count, s1, "$g_prisoner_recruit_troop_id", "$g_prisoner_recruit_size"),
        (str_store_string, s18, "@{reg1} {s1} {reg2?accept:accepts} the offer."),
      (else_try),
        (str_store_string, s18, "@No one accepts the offer."),
      (try_end),
    (try_end),
    ],
    [
      ("camp_recruit_prisoners_accept",[(gt, "$g_prisoner_recruit_troop_id", 0)],"Take them.",
       [(remove_troops_from_prisoners, "$g_prisoner_recruit_troop_id", "$g_prisoner_recruit_size"),
        (party_add_members, "p_main_party", "$g_prisoner_recruit_troop_id", "$g_prisoner_recruit_size"),
        (store_mul, ":morale_change", -3, "$g_prisoner_recruit_size"),
        (call_script, "script_change_player_party_morale", ":morale_change"),
        (jump_to_menu, "mnu_camp"),
        ]
       ),
      ("camp_recruit_prisoners_reject",[(gt, "$g_prisoner_recruit_troop_id", 0)],"Reject them.",
       [(jump_to_menu, "mnu_camp"),
        (assign, "$g_prisoner_recruit_troop_id", 0),
        (assign, "$g_prisoner_recruit_size", 0),
        ]
       ),
      ("go_back_dot",[(le, "$g_prisoner_recruit_troop_id", 0)],"Go back.",
       [(jump_to_menu, "mnu_camp"),
        ]
       ),
      ]
  ),
  
  ("camp_no_prisoners",menu_text_color(0xFF000d2c),
   "You have no prisoners to recruit from.",
   "none",
   [],
    [
      ("continue_3dot",[],"Continue...",
       [(jump_to_menu, "mnu_camp"),
        ]
       ),
      ]
  ),

  ("camp_action_read_book",menu_text_color(0xFF000d2c),
  #SW - modified read book menu
   "Choose a holocron to view:",
   "none",
   [],
    [
      ("action_read_book_1",[(player_has_item, "itm_book_tactics"),
                             (item_slot_eq, "itm_book_tactics", slot_item_book_read, 0),
                             (str_store_item_name, s1, "itm_book_tactics"),
                             ],"{s1}.",
       [(assign, "$temp", "itm_book_tactics"),
        (jump_to_menu, "mnu_camp_action_read_book_start"),
        ]
       ),
      ("action_read_book_2",[(player_has_item, "itm_book_persuasion"),
                             (item_slot_eq, "itm_book_persuasion", slot_item_book_read, 0),
                             (str_store_item_name, s1, "itm_book_persuasion"),
                             ],"{s1}.",
       [(assign, "$temp", "itm_book_persuasion"),
        (jump_to_menu, "mnu_camp_action_read_book_start"),
        ]
       ),
      ("action_read_book_3",[(player_has_item, "itm_book_leadership"),
                             (item_slot_eq, "itm_book_leadership", slot_item_book_read, 0),
                             (str_store_item_name, s1, "itm_book_leadership"),
                             ],"{s1}.",
       [(assign, "$temp", "itm_book_leadership"),
        (jump_to_menu, "mnu_camp_action_read_book_start"),
        ]
       ),
      ("action_read_book_4",[(player_has_item, "itm_book_intelligence"),
                             (item_slot_eq, "itm_book_intelligence", slot_item_book_read, 0),
                             (str_store_item_name, s1, "itm_book_intelligence"),
                             ],"{s1}.",
       [(assign, "$temp", "itm_book_intelligence"),
        (jump_to_menu, "mnu_camp_action_read_book_start"),
        ]
       ),
      ("action_read_book_5",[(player_has_item, "itm_book_trade"),
                             (item_slot_eq, "itm_book_trade", slot_item_book_read, 0),
                             (str_store_item_name, s1, "itm_book_trade"),
                             ],"{s1}.",
       [(assign, "$temp", "itm_book_trade"),
        (jump_to_menu, "mnu_camp_action_read_book_start"),
        ]
       ),
      ("action_read_book_6",[(player_has_item, "itm_book_weapon_mastery"),
                             (item_slot_eq, "itm_book_weapon_mastery", slot_item_book_read, 0),
                             (str_store_item_name, s1, "itm_book_weapon_mastery"),
                             ],"{s1}.",
       [(assign, "$temp", "itm_book_weapon_mastery"),
        (jump_to_menu, "mnu_camp_action_read_book_start"),
        ]
       ),
      ("action_read_book_7",[(player_has_item, "itm_book_engineering"),
                             (item_slot_eq, "itm_book_engineering", slot_item_book_read, 0),
                             (str_store_item_name, s1, "itm_book_engineering"),
                             ],"{s1}.",
       [(assign, "$temp", "itm_book_engineering"),
        (jump_to_menu, "mnu_camp_action_read_book_start"),
        ]
       ),
      ("back_to_camp",[],"Back to camp menu.",
       [(jump_to_menu, "mnu_camp"),
        ]
       ),
      ]
  ),

  # ("camp_action_change_ship",menu_text_color(0xFF000d2c),
  # #SW - modified so you can choose your own spaceship
   # "Choose the spaceship you want to buy:",
   # "none",
   # [],
    # [
      # #("action_spaceship_1",[],"Galactic Empire",
	  # ("action_spaceship_1",[],"Imperial Star Destroyer (5000 credits)",
       # [
		  # (assign, reg51, 5000),	# the price of the ship
          # (store_troop_gold,reg1,"trp_player"),
          # (try_begin),
            # (lt,reg1,reg51),
            # (display_message, "@You don't have enough money.", 0x88ffff),
          # (else_try),
            # (display_message, "@You purchase the spaceship."),		  
			# (troop_remove_gold, "trp_player", reg51),
            # (play_sound, "snd_money_paid"),
			# (assign, "$pout_party", 0),
			# (party_set_icon, "$pout_party", "icon_imperial_star_destroyer"),			
		    # (jump_to_menu, "mnu_camp"),			
          # (try_end),	   
        # ]
       # ),
      # #("action_spaceship_2",[],"Rebel Alliance",
	  # ("action_spaceship_2",[],"Rebel Transport (4000 credits)",
       # [
		  # (assign, reg51, 4000),	# the price of the ship
          # (store_troop_gold,reg1,"trp_player"),
          # (try_begin),
            # (lt,reg1,reg51),
            # (display_message, "@You don't have enough money.", 0x88ffff),
          # (else_try),
            # (display_message, "@You purchase the spaceship."),		  		  
			# (troop_remove_gold, "trp_player", reg51),
            # (play_sound, "snd_money_paid"),
			# (assign, "$pout_party", 0),
			# (party_set_icon, "$pout_party", "icon_rebel_transport"),			
		    # (jump_to_menu, "mnu_camp"),			
          # (try_end),	   
        # ]
       # ),
      # #("action_spaceship_3",[],"Hutt Cartel",
	  # ("action_spaceship_3",[],"Hutt Cruiser (4000 credits)",
       # [
		  # (assign, reg51, 4000),	# the price of the ship
          # (store_troop_gold,reg1,"trp_player"),
          # (try_begin),
            # (lt,reg1,reg51),
            # (display_message, "@You don't have enough money.", 0x88ffff),
          # (else_try),
            # (display_message, "@You purchase the spaceship."),		  		  
			# (troop_remove_gold, "trp_player", reg51),
            # (play_sound, "snd_money_paid"),
			# (assign, "$pout_party", 0),
			# (party_set_icon, "$pout_party", "icon_hutt_cruiser"),			
		    # (jump_to_menu, "mnu_camp"),			
		  # (try_end),	   
        # ]
       # ),
	  # ("action_spaceship_31",[],"Y-Wing (2000 credits)",
       # [
		  # (assign, reg51, 2000),	# the price of the ship
          # (store_troop_gold,reg1,"trp_player"),
          # (try_begin),
            # (lt,reg1,reg51),
            # (display_message, "@You don't have enough money.", 0x88ffff),
          # (else_try),
            # (display_message, "@You purchase the spaceship."),		  		  
			# (troop_remove_gold, "trp_player", reg51),
            # (play_sound, "snd_money_paid"),
			# (assign, "$pout_party", 0),
			# (party_set_icon, "$pout_party", "icon_y_wing"),			
		    # (jump_to_menu, "mnu_camp"),			
		  # (try_end),	   
        # ]
       # ),
	  # ("action_spaceship_32",[],"Imperial Shuttle (2000 credits)",
       # [
		  # (assign, reg51, 2000),	# the price of the ship
          # (store_troop_gold,reg1,"trp_player"),
          # (try_begin),
            # (lt,reg1,reg51),
            # (display_message, "@You don't have enough money.", 0x88ffff),
          # (else_try),
            # (display_message, "@You purchase the spaceship."),		  		  
			# (troop_remove_gold, "trp_player", reg51),
            # (play_sound, "snd_money_paid"),
			# (assign, "$pout_party", 0),
			# (party_set_icon, "$pout_party", "icon_imperial_shuttle"),			
		    # (jump_to_menu, "mnu_camp"),			
		  # (try_end),	   
        # ]
       # ),	   
	  # ("action_spaceship_4",[],"Merchant Freighter (1500 credits)",
       # [
		  # (assign, reg51, 1500),	# the price of the ship
          # (store_troop_gold,reg1,"trp_player"),
          # (try_begin),
            # (lt,reg1,reg51),
            # (display_message, "@You don't have enough money.", 0x88ffff),
          # (else_try),
            # (display_message, "@You purchase the spaceship."),		  		  
			# (troop_remove_gold, "trp_player", reg51),
            # (play_sound, "snd_money_paid"),
			# (assign, "$pout_party", 0),
			# (party_set_icon, "$pout_party", "icon_freighter"),
		    # (jump_to_menu, "mnu_camp"),			
		  # (try_end),	   
        # ]
       # ),	   
	  # ("action_spaceship_5",[],"Z-95 Headhunter (1000 credits)",
       # [
		  # (assign, reg51, 1000),	# the price of the ship
          # (store_troop_gold,reg1,"trp_player"),
          # (try_begin),
            # (lt,reg1,reg51),
            # (display_message, "@You don't have enough money.", 0x88ffff),
          # (else_try),
            # (display_message, "@You purchase the spaceship."),		  		  
			# (troop_remove_gold, "trp_player", reg51),
            # (play_sound, "snd_money_paid"),
			# (assign, "$pout_party", 0),
			# (party_set_icon, "$pout_party", "icon_z95"),
		    # (jump_to_menu, "mnu_camp"),						
          # (try_end),	   
        # ]
       # ),
	  # ("action_spaceship_6",[],"Mercenary Ship (1000 credits)",
       # [
		  # (assign, reg51, 1000),	# the price of the ship
          # (store_troop_gold,reg1,"trp_player"),
          # (try_begin),
            # (lt,reg1,reg51),
            # (display_message, "@You don't have enough money.", 0x88ffff),
          # (else_try),
            # (display_message, "@You purchase the spaceship."),		  		  
			# (troop_remove_gold, "trp_player", reg51),
            # (play_sound, "snd_money_paid"),
			# (assign, "$pout_party", 0),
			# (party_set_icon, "$pout_party", "icon_bountyhunter"),
		    # (jump_to_menu, "mnu_camp"),						
          # (try_end),	   
        # ]
       # ),	   
	  # ("action_spaceship_7",[],"Civilian Shuttle (500 credits)",
       # [
		  # (assign, reg51, 500),	# the price of the ship
          # (store_troop_gold,reg1,"trp_player"),
          # (try_begin),
            # (lt,reg1,reg51),
            # (display_message, "@You don't have enough money.", 0x88ffff),
          # (else_try),
            # (display_message, "@You purchase the spaceship."),		  		  
			# (troop_remove_gold, "trp_player", reg51),
            # (play_sound, "snd_money_paid"),
			# (assign, "$pout_party", 0),
			# (party_set_icon, "$pout_party", "icon_shuttle"),
		    # (jump_to_menu, "mnu_camp"),						
          # (try_end),	   
        # ]
       # ),	   
      # ("camp_menu",[],"Back to camp menu.",
       # [(jump_to_menu, "mnu_camp"),
        # ]
       # ),
      # ]
  # ),  

  ("camp_action_change_race",menu_text_color(0xFF000d2c),
  #SW - modified so you can change your race
   #"You were born on the planet Zolan, home to a humanoid species known as Clawdites, but often referred to as Changelings. As one of the few shape-shifting species in the galaxy you can change your form and appearance.^^Note: You should review your character in the face generator after making this change.",
   "Please choose your race:^^Note: You should review your character in the face generator after making this change.",
   "none",
   [],
    [
	
      ("race_male",[],"Human Male",
       [
           (troop_set_type,"trp_player",tf_male),
           (assign,"$character_gender",tf_male),
		   (jump_to_menu, "mnu_camp"),
        ]
       ),
      ("race_female",[],"Human Female",
       [
           (troop_set_type,"trp_player",tf_female),
           (assign,"$character_gender",tf_female),
		   (jump_to_menu, "mnu_camp"),
        ]
       ),
      ("race_twilek",[],"Twilek Male",
       [
           (troop_set_type,"trp_player",tf_twilek),
           (assign,"$character_gender",tf_male),
		   (jump_to_menu, "mnu_camp"),
        ]
       ),
      ("race_twilek_female",[],"Twilek Female",
       [
           (troop_set_type,"trp_player",tf_twilek_female),
           (assign,"$character_gender",tf_female),
		   (jump_to_menu, "mnu_camp"),
        ]
       ),	   
      ("race_rodian",[],"Rodian",
       [
           (troop_set_type,"trp_player",tf_rodian),
           (assign,"$character_gender",tf_male),
		   (jump_to_menu, "mnu_camp"),
        ]
       ),
      ("race_moncal",[],"Mon Calamari",
       [
           (troop_set_type,"trp_player",tf_moncal),
           (assign,"$character_gender",tf_male),
		   (jump_to_menu, "mnu_camp"),
        ]
       ),
      ("race_trandoshan",[],"Trandoshan",
       [
           (troop_set_type,"trp_player",tf_trandoshan),
           (assign,"$character_gender",tf_male),
		   (jump_to_menu, "mnu_camp"),
        ]
       ),
      ("race_wookiee",[],"Wookiee",
       [
           (troop_set_type,"trp_player",tf_wookiee),
           (assign,"$character_gender",tf_male),
		   (jump_to_menu, "mnu_camp"),
        ]
       ),
      ("race_sullustan",[],"Sullustan",
       [
           (troop_set_type,"trp_player",tf_sullustan),
           (assign,"$character_gender",tf_male),
		   (jump_to_menu, "mnu_camp"),
        ]
       ),
      ("race_gamorrean",[],"Gamorrean",
       [
           (troop_set_type,"trp_player",tf_gamorrean),
           (assign,"$character_gender",tf_male),
		   (jump_to_menu, "mnu_camp"),
        ]
       ),
      ("race_bothan",[],"Bothan",
       [
           (troop_set_type,"trp_player",tf_bothan),
           (assign,"$character_gender",tf_male),
		   (jump_to_menu, "mnu_camp"),
        ]
       ),
      ("race_droid",[],"Droid",
       [
           (troop_set_type,"trp_player",tf_droid),
           (assign,"$character_gender",tf_male),
           (jump_to_menu,"mnu_camp"),
        ]
       ),	   
      ("race_geonosian",[],"Geonosian",
       [
           (troop_set_type,"trp_player",tf_geonosian),
           (assign,"$character_gender",tf_male),
		   (jump_to_menu, "mnu_camp"),
        ]
       ),
      ("race_tusken",[],"Tusken",
       [
           (troop_set_type,"trp_player",tf_tusken),
           (assign,"$character_gender",tf_male),
		   (jump_to_menu, "mnu_camp"),
        ]
       ),
      ("race_jawa",[],"Jawa",
       [
           (troop_set_type,"trp_player",tf_jawa),
           (assign,"$character_gender",tf_male),
		   (jump_to_menu, "mnu_camp"),
        ]
       ),	   
      # ("race_rancor",[],"Rancor (testing)",
       # [
           # (troop_set_type,"trp_player",tf_rancor),
           # (assign,"$character_gender",tf_male),
		   # (jump_to_menu, "mnu_camp"),
        # ]
       # ),	   	   
      # ("race_clone",[],"Clone (testing 17th race)",
       # [
           # #(troop_set_type,"trp_player",tf_clone),
		   # (troop_set_type,"trp_player",16),
           # (assign,"$character_gender",tf_male),
		   # (jump_to_menu, "mnu_camp"),
        # ]
       # ),	   	   
     ("back_to_camp",[],"Back to camp menu.",
       [(jump_to_menu, "mnu_camp"),
       ]
     ),
    ]
  ),
  
  ("camp_action_read_book_start",menu_text_color(0xFF000d2c),
   "{s1}",
   "none",
   [(assign, ":new_book", "$temp"),
    (str_store_item_name, s2, ":new_book"),
    (try_begin),
      (store_attribute_level, ":int", "trp_player", ca_intelligence),
      (item_get_slot, ":int_req", ":new_book", slot_item_intelligence_requirement),
      (le, ":int_req", ":int"),
	  #SW - modified book reading menu text
      (str_store_string, s1, "@You start viewing {s2}. After a few minutes,\
 you feel you could learn a lot from this holocron. You decide to keep it close by and view it whenever you have the time."),
      (assign, "$g_player_reading_book", ":new_book"),
    (else_try),
      (str_store_string, s1, "@You view a few minutes of {s2}, but you find the concepts confusing and difficult to follow.\
 Try as you might, it soon gives you a headache, and you're forced to give up the attempt."),
    (try_end),],
    [
      ("continue_3dot",[],"Continue...",
       [(jump_to_menu, "mnu_camp"),
        ]
       ),
      ]
  ),


  ("retirement_verify",menu_text_color(0xFF000d2c),
   "You are at day {reg0}. Your current luck is {reg1}. Are you sure you want to retire?",
   "none",
   [
     (store_current_day, reg0),
     (assign, reg1, "$g_player_luck"),
     ],
    [
      ("yes_dot",[],"Yes.",
       [
         (start_presentation, "prsnt_retirement"),
        ]
       ),
      ("no_dot",[],"No.",
       [
         (jump_to_menu, "mnu_camp"),
        ]
       ),
      ]
  ),

  ("end_game",menu_text_color(0xFF000d2c),
   "The decision is made, and you resolve to give up your adventurer's\
 life and settle down. You sell off your weapons and armour, gather up\
 all your credits, and depart into the sunset....",
   "none",
   [],
    [
      ("end_game_bye",[],"May the Force be with you.",
       [
         (change_screen_quit),
        ]
       ),
      ]
  ),

  #SW MF modified to add option to take money out of bank account.
  (
    "pay_day",menu_text_color(0xFF000d2c)|mnf_scale_picture|mnf_disable_all_keys,
    "{s1}.",
    "none",
    [
        (set_background_mesh, "mesh_pic_payment"),
        
        (call_script, "script_calculate_player_faction_wage"),
        (assign, ":total_wages", reg0),
        (assign, reg6, ":total_wages"),

        (assign, reg2, "$g_player_debt_to_party_members"),
        (store_add, reg3, reg6, reg2),
        (store_troop_gold, ":player_wealth", "trp_player"),
        (assign, reg4, ":player_wealth"),
		(store_sub, reg5, reg4, reg3),
        (val_add, ":total_wages", "$g_player_debt_to_party_members"),
		
		(faction_get_slot,":player_bank","fac_trade_federation",slot_faction_bank_deposit),
		(assign, reg7, ":player_bank"),
		(store_add, ":player_total_wealth", ":player_wealth", ":player_bank"),
		(assign, reg8, ":player_total_wealth"),
		
		(str_store_string, s1, "@This week's wages: {reg6} credits.^Earlier debts: {reg2}^Total due: {reg3}^^Current cash: {reg4} credits.^Bank account: {reg7} credits.^Total wealth: {reg8} credits"),
        # (try_begin),
          # (ge, ":player_wealth", ":total_wages"),
          # (assign, "$g_player_debt_to_party_members", 0),
          # (troop_remove_gold, "trp_player",":total_wages"),

          # (str_store_string, s1, "@You paid {reg3} of your {reg4} credits to your men. You have {reg5} credits left."),
        # (else_try),
          # (troop_remove_gold, "trp_player",":player_wealth"),
          # (store_sub, ":unpaid", ":total_wages", ":player_wealth"),
          # (assign, reg5, ":unpaid"),
          # (str_store_string, s1, "@Your debt to your men amounted to {reg3} credits, however you only had {reg4}. Unpaid sum of {reg5} credits is added as debt. Your party loses morale."),
          # (assign, "$g_player_debt_to_party_members", ":unpaid"),
          # (call_script, "script_objectionable_action", tmt_egalitarian, "str_men_unpaid"),
        # (try_end),


        # (str_store_string, s1, "@This week's wages: {reg6} credits^Earlier debts: {reg2} denars^Total payment: {reg3} credits^Current wealth: {reg4} credits^^{s1}"),
    ],
    [
	  ("pay_cash",[
	    (try_begin),
          (ge,reg4, reg3),
          (str_store_string, s2, "@Pay everything in cash"),
        (else_try),
          (str_store_string, s2, "@Pay only as much as you can in cash. Your party will lose morale."),
        (try_end),
	  ],"{s2}",
       [
        (try_begin),
          (ge,reg4, reg3),

          (assign, "$g_player_debt_to_party_members", 0),
          (troop_remove_gold, "trp_player",reg3),
		  (change_screen_return),


        (else_try),
          (troop_remove_gold, "trp_player",reg4),
          (store_sub, ":unpaid", reg3,reg4),
          (assign, reg5, ":unpaid"),
 #         (str_store_string, s2, "@Pay only as much as you can in cash. Your party will lose morale."),
          (assign, "$g_player_debt_to_party_members", ":unpaid"),
          (call_script, "script_objectionable_action", tmt_egalitarian, "str_men_unpaid"),
          (call_script, "script_change_player_party_morale", -50),
		  
		  (change_screen_return),
        (try_end),
        ]
       ),
      ("pay_account",[
		(gt, reg7, 0),
	  	(try_begin),
          (ge,reg4, reg3),
          (str_store_string, s3, "@Pay everything from your bank account"),
        (else_try),
          (str_store_string, s3, "@Pay only as much as you can from your account. Your party will lose morale."),
        (try_end),
	  ],"{s3}",
       [
        (try_begin),
          (ge, reg7, reg3),
          (assign, "$g_player_debt_to_party_members", 0),
		  (val_sub, reg7, reg3),
		  (faction_set_slot,"fac_trade_federation",slot_faction_bank_deposit,reg7),
		  (display_message, "@{reg3} credits have been removed from your bank account and paid to your troops"),
		  (change_screen_return),
        (else_try),
		  (faction_set_slot,"fac_trade_federation",slot_faction_bank_deposit, 0),
          (store_sub, ":unpaid", reg3, reg7),

          (assign, "$g_player_debt_to_party_members", ":unpaid"),
		  (display_message, "@{reg7} credits have been removed from your bank account and paid to your troops"),
          (call_script, "script_objectionable_action", tmt_egalitarian, "str_men_unpaid"),
		  (call_script, "script_change_player_party_morale", -50),
		  (change_screen_return),
        (try_end),
        ]
       ),
	   
	  ("pay_both_1", [(ge, reg8, reg3), (lt,reg4, reg3), (gt, reg7, 0)],"Pay cash first and the rest from bank account",


	   [
          (assign, "$g_player_debt_to_party_members", 0),
          (troop_remove_gold, "trp_player",reg4),
		  (val_sub, reg3,reg4),
		  (val_sub, reg7, reg3),
		  (assign, reg9, reg7),
		  (faction_set_slot,"fac_trade_federation",slot_faction_bank_deposit,reg7),
		  (display_message, "@{reg3} credits have been removed from your bank account and paid to your troops"),


		  (change_screen_return),
		]
		),
		
	 ("pay_both_2", [(ge, reg8, reg3), (lt, reg7, reg3), (gt, reg7, 0)],"Pay from bank account first and the rest in cash",
	   [
	   (ge, reg7, reg3),
          (assign, "$g_player_debt_to_party_members", 0),
		  (faction_set_slot,"fac_trade_federation",slot_faction_bank_deposit, 0),
		  (display_message, "@{reg7} credits have been removed from your bank account and paid to your troops"),
		  (val_sub, reg3, reg7),
          (troop_remove_gold, "trp_player",reg3),
		  (change_screen_return),
		]
		),
	  ("no_pay", [], "Don't pay anything. Your troops will lose morale",[
		(assign, "$g_player_debt_to_party_members", reg3),
		(call_script, "script_objectionable_action", tmt_egalitarian, "str_men_unpaid"),
		(call_script, "script_change_player_party_morale", -60),
		(change_screen_return),
	  ]),
  
]),  
  ("cattle_herd",menu_text_color(0xFF000d2c)|mnf_scale_picture,
   "You encounter a nerf herd.",
   "none",
   [#SW - commented out snd_cow_moo
	#(play_sound, "snd_cow_moo"),
    (set_background_mesh, "mesh_pic_cattle"),
   ],
    [
      ("cattle_drive_away",[],"Drive the nerf herd onward.",
       [
        (party_set_slot, "$g_encountered_party", slot_cattle_driven_by_player, 1),
		 #SW - modified cattle_drive_away so they will follow you
        #(party_set_ai_behavior, "$g_encountered_party", ai_bhvr_driven_by_party),
		(party_set_ai_behavior, "$g_encountered_party", ai_bhvr_escort_party),		
        (party_set_ai_object,"$g_encountered_party", "p_main_party"),
        (change_screen_return),
        ]
       ),
      ("cattle_stop",[],"Bring the herd to a stop.",
       [
        (party_set_slot, "$g_encountered_party", slot_cattle_driven_by_player, 0),
        (party_set_ai_behavior, "$g_encountered_party", ai_bhvr_hold),
        (change_screen_return),
        ]
       ),
      ("cattle_kill",[(assign, ":continue", 1),
                      (try_begin),
                        (check_quest_active, "qst_move_cattle_herd"),
                        (quest_slot_eq, "qst_move_cattle_herd", slot_quest_target_party, "$g_encountered_party"),
                        (assign, ":continue", 0),
                      (try_end),
                      (eq, ":continue", 1)],"Slaughter some of the animals.",
       [(jump_to_menu, "mnu_cattle_herd_kill"),
        ]
       ),
      ("leave_dot",[],"Leave.",
       [(change_screen_return),
        ]
       ),
      ]
  ),

  ("cattle_herd_kill",menu_text_color(0xFF000d2c),
   "How many animals do you want to slaughter?",
   "none",
   [(party_get_num_companions, reg5, "$g_encountered_party")],
    [
      ("one",[(ge, reg5, 1),],"One.",
       [(call_script, "script_kill_cattle_from_herd", "$g_encountered_party", 1),
        (jump_to_menu, "mnu_cattle_herd_kill_end"),
        (change_screen_loot, "trp_temp_troop"),
        (play_sound, "snd_cow_slaughter"),
        ]
       ),
      ("two",[(ge, reg5, 2),],"Two.",
       [(call_script, "script_kill_cattle_from_herd", "$g_encountered_party", 2),
        (jump_to_menu, "mnu_cattle_herd_kill_end"),
        (change_screen_loot, "trp_temp_troop"),
        (play_sound, "snd_cow_slaughter"),
        ]
       ),
      ("three",[(ge, reg5, 3),],"Three.",
       [(call_script, "script_kill_cattle_from_herd", "$g_encountered_party", 3),
        (jump_to_menu, "mnu_cattle_herd_kill_end"),
        (change_screen_loot, "trp_temp_troop"),
        (play_sound, "snd_cow_slaughter"),
        ]
       ),
      ("four",[(ge, reg5, 4),],"Four.",
       [(call_script, "script_kill_cattle_from_herd", "$g_encountered_party", 4),
        (jump_to_menu, "mnu_cattle_herd_kill_end"),
        (change_screen_loot, "trp_temp_troop"),
        (play_sound, "snd_cow_slaughter"),
        ]
       ),
      ("five",[(ge, reg5, 5),],"Five.",
       [(call_script, "script_kill_cattle_from_herd", "$g_encountered_party", 5),
        (jump_to_menu, "mnu_cattle_herd_kill_end"),
        (change_screen_loot, "trp_temp_troop"),
        (play_sound, "snd_cow_slaughter"),
        ]
       ),
      ("go_back_dot",[],"Go back.",
       [(jump_to_menu, "mnu_cattle_herd"),
        ]
       ),
      ]
  ),

  ("cattle_herd_kill_end",menu_text_color(0xFF000d2c),
   "You shouldn't be reading this.",
   "none",
   [(change_screen_return)],
    [
      ]
  ),


  ("arena_duel_fight",menu_text_color(0xFF000d2c),
   "You and your opponent prepare to fight for honour.",
   "none",
   [],
   [
     ("continue_3dot",[],"Continue...",
      [
        (jump_to_menu, "mnu_simple_encounter"),
        (change_screen_mission),
        ]),
      ]
  ),

############################### Duel Mod by MartinF Start  ##############################


("duel_menu",menu_text_color(0xFF000d2c),
   "{s1}{s2}",
   "none",
   [
 (str_clear, s2),  (str_clear, s3), (str_clear, s5), (str_clear, s6), (str_clear, s7),
   (troop_get_slot, ":duel_wins", "$g_talk_troop", slot_troop_duel_won),
   (assign, reg(6), ":duel_wins"),
   (troop_get_slot, ":duel_losses", "$g_talk_troop", slot_troop_duel_lost),
   (assign, reg(7), ":duel_losses"),
   (store_add, ":duel_total", ":duel_wins", ":duel_losses"),
   (assign, reg(5), ":duel_total"),
   (str_store_troop_name, s3, "$g_talk_troop"),
   (try_begin),
      (eq, "$g_duel_result", -1),
      (str_store_string, s1, "@You lost your duel against ^^{s3}"),
   (else_try),
      (eq, "$g_duel_result", 1),
      (str_store_string, s1, "@You won your duel against ^^{s3}"),
   (else_try),
      (str_store_string, s1, "@You prepare to duel ^^{s3}"),
   (try_end),
    (try_begin),
      (troop_is_hero, "$g_talk_troop"),
      (str_store_string, s2, "@^^^^You have fought {s3} {reg5} times. ^^You've won {reg6} times. ^^You've lost {reg7} times"),
   (else_try),
      (str_store_string, s2, "@^^^^Dueling with your own troops will not count towards your dueling statistics."),
   (try_end),

    ],
   
   [
      ("start_fight",[(eq, "$g_duel_result", 0)],"Start the duel.",
       [(try_begin),     
          (is_between, "$g_encountered_party", mainplanets_begin, mainplanets_end),     
            (party_get_slot, ":arena_scene", "$g_encountered_party", slot_mainplanet_arena),   
        (else_try),     
            (assign, ":closest_dist", 100000),     
            (assign, ":closest_town", -1),     
            (try_for_range, ":cur_town", mainplanets_begin, mainplanets_end),       
                (store_distance_to_party_from_party, ":dist", ":cur_town", "p_main_party"),       
                (lt, ":dist", ":closest_dist"),       
                (assign, ":closest_dist", ":dist"),       
                (assign, ":closest_town", ":cur_town"),     
            (try_end),     
            (party_get_slot, ":arena_scene", ":closest_town", slot_mainplanet_arena),
        (try_end),   
        (modify_visitors_at_site, ":arena_scene"),   
        (reset_visitors),
    (set_visitor, "$g_duel_vis_point_opp", "$g_talk_troop"),
    (set_visitor, "$g_duel_vis_point_plyr", "trp_player"),

         (set_jump_mission, "mt_arena_duel_thing_std"),
         (jump_to_scene, ":arena_scene"),
         (change_screen_mission),
        ]
       ),
      ("duel_again",[(neq, "$g_duel_result", 0)],"Duel again.",
       [
           (assign, "$g_duel_result", 0),
           (jump_to_menu, "mnu_duel_menu"),
       ]
       ),
      ("leave_dot",[],"Leave.",
       [(change_screen_map),
        ]
       ),
   ]
   
 ),

############################### Duel Mod End  ##############################
  
  (
    "simple_encounter",menu_text_color(0xFF000d2c)|mnf_enable_hot_keys|mnf_scale_picture,
    "{s2} You have {reg10} troops fit for battle against their {reg11}.",
    "none",
    [
        (assign, "$g_enemy_party", "$g_encountered_party"),
        (assign, "$g_ally_party", -1),
        (call_script, "script_encounter_calculate_fit"),
        (try_begin),
          (eq, "$new_encounter", 1),
          (assign, "$new_encounter", 0),
          (assign, "$g_encounter_is_in_village", 0),
          (assign, "$g_encounter_type", 0),
          (try_begin),
            (party_slot_eq, "$g_enemy_party", slot_party_ai_state, spai_raiding_around_center),
            (party_get_slot, ":minorplanet_no", "$g_enemy_party", slot_party_ai_object),
            (store_distance_to_party_from_party, ":dist", ":minorplanet_no", "$g_enemy_party"),
            (try_begin),
              (lt, ":dist", raid_distance),
              (assign, "$g_encounter_is_in_village", ":minorplanet_no"),
              (assign, "$g_encounter_type", enctype_fighting_against_minorplanet_raid),
            (try_end),
          (try_end),
          (try_begin),
            (gt, "$g_player_raiding_village", 0),
            (assign, "$g_encounter_is_in_village", "$g_player_raiding_village"),
            (assign, "$g_encounter_type", enctype_catched_during_minorplanet_raid),
            (party_quick_attach_to_current_battle, "$g_encounter_is_in_village", 1), #attach as enemy
            (str_store_string, s1, "@Villagers"),
            (display_message, "str_s1_joined_battle_enemy"),
          (else_try),
            (eq, "$g_encounter_type", enctype_fighting_against_minorplanet_raid),
            (party_quick_attach_to_current_battle, "$g_encounter_is_in_village", 0), #attach as friend
            (str_store_string, s1, "@Villagers"),
            (display_message, "str_s1_joined_battle_friend"),
            # Let village party join battle at your side
          (try_end),
          (call_script, "script_let_nearby_parties_join_current_battle", 0, 0),
          (call_script, "script_encounter_init_variables"),
          (assign, "$encountered_party_hostile", 0),
          (assign, "$encountered_party_friendly", 0),
          (try_begin),
            (gt, "$g_encountered_party_relation", 0),
            (assign, "$encountered_party_friendly", 1),
          (try_end),
          (try_begin),
            (lt, "$g_encountered_party_relation", 0),
            (assign, "$encountered_party_hostile", 1),
            (try_begin),
              (encountered_party_is_attacker),
              (assign, "$cant_leave_encounter", 1),
            (try_end),
          (try_end),
          (assign, "$talk_context", tc_party_encounter),
          (call_script, "script_setup_party_meeting", "$g_encountered_party"),
        (else_try), #second or more turn
#          (try_begin),
#            (call_script, "script_encounter_calculate_morale_change"),
#          (try_end),
          (try_begin),
            # We can leave battle only after some troops have been killed. 
            (eq, "$cant_leave_encounter", 1),
            (call_script, "script_party_count_members_with_full_health", "p_main_party_backup"),
            (assign, ":org_total_party_counts", reg0),
            (call_script, "script_party_count_members_with_full_health", "p_encountered_party_backup"),
            (val_add, ":org_total_party_counts", reg0),

            (call_script, "script_party_count_members_with_full_health", "p_main_party"),
            (assign, ":cur_total_party_counts", reg0),
            (call_script, "script_party_count_members_with_full_health", "p_collective_enemy"),
            (val_add, ":cur_total_party_counts", reg0),

            (store_sub, ":leave_encounter_limit", ":org_total_party_counts", 10),
            (lt, ":cur_total_party_counts", ":leave_encounter_limit"),
            (assign, "$cant_leave_encounter", 0),
          (try_end),
          (eq, "$g_leave_encounter",1),
          (change_screen_return),
        (try_end),

        #setup s2
        (try_begin),
          (party_is_active,"$g_encountered_party"),
          (str_store_party_name, s1,"$g_encountered_party"),
          (try_begin),
            (eq, "$g_encounter_type", 0),
            (str_store_string, s2,"@You have encountered {s1}."),
          (else_try),
            (eq, "$g_encounter_type", enctype_fighting_against_minorplanet_raid),
            (str_store_party_name, s3, "$g_encounter_is_in_village"),
            (str_store_string, s2,"@You have engaged {s1} while they were raiding {s3}."),
          (else_try),
            (eq, "$g_encounter_type", enctype_catched_during_minorplanet_raid),
            (str_store_party_name, s3, "$g_encounter_is_in_village"),
            (str_store_string, s2,"@You were caught by {s1} while your forces were raiding {s3}."),
          (try_end),
        (try_end),
        (try_begin),
          (call_script, "script_party_count_members_with_full_health", "p_collective_enemy"),
          (assign, ":num_enemy_regulars_remaining", reg(0)),
          (assign, ":enemy_finished",0),
          (try_begin),
            (eq, "$g_battle_result", 1),
            (eq, ":num_enemy_regulars_remaining", 0), #battle won
            (assign, ":enemy_finished",1),
          (else_try),
            (eq, "$g_engaged_enemy", 1),
            (le, "$g_enemy_fit_for_battle",0),
            (ge, "$g_friend_fit_for_battle",1),
            (assign, ":enemy_finished",1),
          (try_end),
          (this_or_next|eq, ":enemy_finished",1),
          (eq,"$g_enemy_surrenders",1),
          (assign, "$g_next_menu", -1),
          (jump_to_menu, "mnu_total_victory"),
        (else_try),
#          (eq, "$encountered_party_hostile", 1),
          (call_script, "script_party_count_members_with_full_health","p_main_party"),
          (assign, reg(3), reg(0)),
          (assign, ":friends_finished",0),
          (try_begin),
            (eq, "$g_battle_result", -1),
            (eq, reg(3), 0), #battle lost
            (assign,  ":friends_finished",1),
          (else_try),
            (eq, "$g_engaged_enemy", 1),
            (ge, "$g_enemy_fit_for_battle",1),
            (le, "$g_friend_fit_for_battle",0),
            (assign,  ":friends_finished",1),
          (try_end),
          (this_or_next|eq,  ":friends_finished",1),
          (eq,"$g_player_surrenders",1),
          (assign, "$g_next_menu", "mnu_captivity_start_wilderness"),
          (jump_to_menu, "mnu_total_defeat"),
        (try_end),

       
        (try_begin),
          (eq, "$g_encountered_party_template", "pt_jawas"),
          (set_background_mesh, "mesh_pic_bandits"),
        (else_try),
          (eq, "$g_encountered_party_template", "pt_black_sun_pirates"),
          (set_background_mesh, "mesh_pic_black_sun_pirates"),
        (else_try),
          (eq, "$g_encountered_party_template", "pt_night_fang_pirates"),
          (set_background_mesh, "mesh_pic_night_fang_pirates"),
        (else_try),
          (eq, "$g_encountered_party_template", "pt_tusken_raiders"),
          (set_background_mesh, "mesh_pic_tusken_raiders"),
        (else_try),
          (eq, "$g_encountered_party_template", "pt_blazing_claw_pirates"),
          (set_background_mesh, "mesh_pic_blazing_claw_pirates"),
        (else_try),
          (eq, "$g_encountered_party_template", "pt_deserters"),
          (set_background_mesh, "mesh_pic_deserters"),
        (try_end),
    ],
    [
############################################################################################################
##### Custom Commander(CC)
############################################################################################################
    
      ("commander_change",[(str_store_troop_name,s7,"$g_player_troop")],
        "Change the commander. (Current:{s7})",
        [
          (assign, "$g_next_menu", "mnu_simple_encounter"),
          (assign, "$change_commander_menu_offset", 0),
          (jump_to_menu, "mnu_change_commander"),
        ]),

############################################################################################################
##### Custom Commander(CC)
############################################################################################################
      ("encounter_attack",[
          (eq, "$encountered_party_friendly", 0),
          
          #--> Mining vessels suck at open battlefield, only battle in space!
          (party_get_template_id,":i_pt","$g_encountered_party"),
          (neq,":i_pt","pt_miningvessel"),
############################################################################################################
##### Custom Commander(CC)
############################################################################################################
          #(neg|troop_is_wounded, "trp_player"),
          (neg|troop_is_wounded, "$g_player_troop"),
############################################################################################################
##### Custom Commander(CC)
############################################################################################################

		#SW - script_setup_random_scene is based on the closest planet, determine its name
		(assign, ":closest_dist",100000),
		(assign, ":closest_town", -1),
		(try_for_range, ":cur_town", mainplanets_begin, mainplanets_end),
			(store_distance_to_party_from_party, ":dist", ":cur_town","p_main_party"),
			(lt, ":dist", ":closest_dist"),
				(assign, ":closest_dist", ":dist"),
				(assign, ":closest_town", ":cur_town"),
		(try_end),
		(str_store_party_name, s1, ":closest_town"),

          ],
							#------------------------- start of 'fight on the planet surface' code
							#"Land and fight on the planet surface.",[
							"Land and fight on {s1}.",[
                                (assign, "$g_battle_result", 0),
                                (assign, "$g_engaged_enemy", 1),
                                (call_script, "script_calculate_renown_value"),
                                (call_script, "script_calculate_battle_advantage"),
                                (set_battle_advantage, reg0),
                                (set_party_battle_mode),
                                (try_begin),
                                  (eq, "$g_encounter_type", enctype_fighting_against_minorplanet_raid),
                                  (assign, "$g_minorplanet_raid_evil", 0),
                                  (set_jump_mission,"mt_minorplanet_raid"),
                                  (party_get_slot, ":scene_to_use", "$g_encounter_is_in_village", slot_spacestation_exterior),
                                  (jump_to_scene, ":scene_to_use"),
                                (else_try),
                                  (eq, "$g_encounter_type", enctype_catched_during_minorplanet_raid),
                                  (assign, "$g_minorplanet_raid_evil", 0),
                                  (set_jump_mission,"mt_minorplanet_raid"),
                                  (party_get_slot, ":scene_to_use", "$g_encounter_is_in_village", slot_spacestation_exterior),
                                  (jump_to_scene, ":scene_to_use"),
                                (else_try),
                                  (set_jump_mission,"mt_lead_charge"),
                                  (call_script, "script_setup_random_scene"),
                                (try_end),
                                (assign, "$g_next_menu", "mnu_simple_encounter"),
                                (jump_to_menu, "mnu_battle_debrief"),
                                (change_screen_mission),
                                ]),
							#------------------------- end of 'fight on the planet surface' code
      ("encounter_attack_board_ship",[
          (eq, "$encountered_party_friendly", 0),
############################################################################################################
##### Custom Commander(CC)
############################################################################################################
          #(neg|troop_is_wounded, "trp_player"),
          (neg|troop_is_wounded, "$g_player_troop"),
############################################################################################################
##### Custom Commander(CC)
############################################################################################################
          ],
							#------------------------- start of 'board the ship' code
							#"Board the ship.",[
							"Fight on the ship.",[
                                (assign, "$g_battle_result", 0),
                                (assign, "$g_engaged_enemy", 1),
                                (call_script, "script_calculate_renown_value"),
                                (call_script, "script_calculate_battle_advantage"),
                                (set_battle_advantage, reg0),
                                (set_party_battle_mode),
                                (try_begin),
                                  (eq, "$g_encounter_type", enctype_fighting_against_minorplanet_raid),
                                  (set_jump_mission,"mt_minorplanet_raid"),
                                  (party_get_slot, ":scene_to_use", "$g_encounter_is_in_village", slot_spacestation_exterior),
                                  (jump_to_scene, ":scene_to_use"),
                                (else_try),
                                  (eq, "$g_encounter_type", enctype_catched_during_minorplanet_raid),
                                  (set_jump_mission,"mt_minorplanet_raid"),
                                  (party_get_slot, ":scene_to_use", "$g_encounter_is_in_village", slot_spacestation_exterior),
                                  (jump_to_scene, ":scene_to_use"),
                                (else_try),
								  (set_jump_mission,"mt_lead_charge_no_horse"),
								  #(assign, ":scene_to_use", "scn_random_scene_ship"),
								  
								  (faction_get_slot,":hangar_faction","fac_player_supporters_faction", slot_faction_culture),
								  
								  (try_begin),
									(eq,":hangar_faction","fac_culture_1"),
									(assign,":scene_to_use","scn_ship_hangar_imp"),
								  (else_try),
									(eq,":hangar_faction","fac_culture_2"),
									(assign,":scene_to_use","scn_ship_hangar_reb"),
								  (else_try),	
									(eq,":hangar_faction","fac_culture_3"),
									(assign,":scene_to_use","scn_ship_hangar_hut"),
								  (else_try), 
									(assign,":scene_to_use","scn_ship_hangar"),
								  (try_end),
								  
								   # (store_random_in_range, ":rand", 0, 100),
									# (try_begin),
						          	  # (lt, ":rand", 35),
									  # (assign, ":scene_to_use", "scn_ship_hangar_open_3a"),
									# (else_try),
									  # (lt, ":rand", 70),
									  # (assign, ":scene_to_use", "scn_ship_hangar_open_3b"),
									# (else_try),
									  # (lt, ":rand", 85),
									  ##(assign, ":scene_to_use", "scn_ship_hangar_closed_2"),
									  # (assign, ":scene_to_use", "scn_ship_hangar_closed_1a"),
									# (else_try),
									  ##(assign, ":scene_to_use", "scn_ship_hangar_open_2"),
									  # (assign, ":scene_to_use", "scn_ship_hangar_closed_1b"),
									# (try_end),
                                  (jump_to_scene, ":scene_to_use"),
                                (try_end),
							
                                (assign, "$g_next_menu", "mnu_simple_encounter"),
                                (jump_to_menu, "mnu_battle_debrief"),
                                (change_screen_mission),
                                ]),
							#------------------------- end of 'board the ship' code							
      ("encounter_order_attack",[
          (eq, "$encountered_party_friendly", 0),
          (call_script, "script_party_count_members_with_full_health", "p_main_party"),(ge, reg(0), 4),
          ],
           "Order your troops to attack without you.",[(jump_to_menu,"mnu_order_attack_begin"),
                                                            #(simulate_battle,3)
                                                            ]),
      ("leave_dot",[
          (eq,"$cant_leave_encounter", 0),
          ],"Leave.",[

###NPC companion changes begin
              (try_begin),
                  (eq, "$encountered_party_friendly", 0),
                  (encountered_party_is_attacker),
                  (call_script, "script_objectionable_action", tmt_aristocratic, "str_flee_battle"),
              (try_end),
###NPC companion changes end
#Troop commentary changes begin
              (try_begin),
                  (eq, "$encountered_party_friendly", 0),
                  (encountered_party_is_attacker),
                  (party_get_num_companion_stacks, ":num_stacks", "p_encountered_party_backup"),
                  (try_for_range, ":stack_no", 0, ":num_stacks"),
                    (party_stack_get_troop_id,   ":stack_troop","p_encountered_party_backup",":stack_no"),
                    (is_between, ":stack_troop", faction_heroes_begin, faction_heroes_end),
                    (store_troop_faction, ":victorious_faction", ":stack_troop"),
                    (call_script, "script_add_log_entry", logent_player_retreated_from_lord, "trp_player",  -1, ":stack_troop", ":victorious_faction"),
                  (try_end),
              (try_end),
#Troop commentary changes end
          	(leave_encounter),(change_screen_return)]),
      ("encounter_retreat",[
         (eq,"$cant_leave_encounter", 1),
         (call_script, "script_get_max_skill_of_player_party", "skl_tactics"),
         (assign, ":max_skill", reg0),
         (val_add, ":max_skill", 4),

         (call_script, "script_party_count_members_with_full_health", "p_collective_enemy", 0),
         (assign, ":enemy_party_strength", reg0),
         (val_div, ":enemy_party_strength", 2),

         (val_div, ":enemy_party_strength", ":max_skill"),
         (val_max, ":enemy_party_strength", 1),

         (call_script, "script_party_count_fit_regulars", "p_main_party"),
         (assign, ":player_count", reg0),
         (ge, ":player_count", ":enemy_party_strength"),
         ],"Pull back, leaving some soldiers behind to cover your retreat.",[(jump_to_menu, "mnu_encounter_retreat_confirm"),]),
      ("surrender",[
         (eq,"$cant_leave_encounter", 1),
          ],"Surrender.",[(assign,"$g_player_surrenders",1)]),
    ]
  ),

############################################################################################################
##### Custom Commander(CC)
############################################################################################################

  (
    "change_commander",menu_text_color(0xFF000d2c),
    "Please reselect a companion as the commander for the comming battle.^^Current:{s7}.",
    "none",
  [
    (str_store_troop_name,s7,"$g_player_troop"),
    (assign, reg10, 0),
    (assign, reg11, -1),
    (assign, reg12, -1),
    (assign, reg13, -1),
    (assign, reg14, -1),
    (party_get_num_companion_stacks, ":num_stacks","p_main_party"),
    (try_for_range, ":i_stack", 0, ":num_stacks"),
      (party_stack_get_troop_id,":stack_troop","p_main_party",":i_stack"),
      (this_or_next|eq, ":stack_troop", "trp_player"),
      (is_between, ":stack_troop", companions_begin, companions_end),
      (neg|troop_is_wounded, ":stack_troop"),
      (val_add, reg10, 1),
      (try_begin),
        (store_add, reg3, "$change_commander_menu_offset", 1),
        (eq, reg10, reg3),
        (assign, reg11, ":stack_troop"),
        (str_store_troop_name, s11, ":stack_troop"),
      (else_try),
        (store_add, reg3, "$change_commander_menu_offset", 2),
        (eq, reg10, reg3),
        (assign, reg12, ":stack_troop"),
        (str_store_troop_name, s12, ":stack_troop"),
      (else_try),
        (store_add, reg3, "$change_commander_menu_offset", 3),
        (eq, reg10, reg3),
        (assign, reg13, ":stack_troop"),
        (str_store_troop_name, s13, ":stack_troop"),
      (else_try),
        (store_add, reg3, "$change_commander_menu_offset", 4),
        (eq, reg10, reg3),
        (assign, reg14, ":stack_troop"),
        (str_store_troop_name, s14, ":stack_troop"),
      (try_end),
    (try_end),
  ],
    
    [
      ("go_back",[],"Go back",[(jump_to_menu, "$g_next_menu")]),
      
      ("prev_page", 
        [
        (try_begin),
          (eq, "$change_commander_menu_offset", 0),
          (disable_menu_option),
        (try_end),
          ], 
          "Previous page",
        [
          (val_sub, "$change_commander_menu_offset", 4),
          (jump_to_menu, "mnu_change_commander"),
        ]
      ),
       
      ("commander1", [(ge, reg11, 0), (store_troop_health, reg1, reg11, 0)], "{s11}(Health:{reg1}%) ", 
      [(assign, "$g_player_troop", reg11),(set_player_troop, "$g_player_troop")]),
      
      ("commander2", [(gt, reg12, 0), (store_troop_health, reg1, reg12, 0)], "{s12}(Health:{reg1}%) ", 
      [(assign, "$g_player_troop", reg12),(set_player_troop, "$g_player_troop")]),
      
      ("commander3", [(gt, reg13, 0), (store_troop_health, reg1, reg13, 0)], "{s13}(Health:{reg1}%) ", 
      [(assign, "$g_player_troop", reg13),(set_player_troop, "$g_player_troop")]),
      
      ("commander4", [(gt, reg14, 0), (store_troop_health, reg1, reg14, 0)], "{s14}(Health:{reg1}%) ", 
      [(assign, "$g_player_troop", reg14),(set_player_troop, "$g_player_troop")]),
      
      ("next_page",
        [
          (try_begin),
            (le, reg10, 4), 
            (disable_menu_option),
          (else_try),
            (store_sub, reg2, reg10, 4),
            (ge, "$change_commander_menu_offset",reg2),
            (disable_menu_option),
          (try_end),
        ],
          "Next page",
        [
          (val_add, "$change_commander_menu_offset", 4),
          (jump_to_menu, "mnu_change_commander"),
        ]
       ),
       
    ]
  ),

############################################################################################################
##### Custom Commander(CC)
############################################################################################################
  
  (
    "encounter_retreat_confirm",menu_text_color(0xFF000d2c),
    "As the party member with the highest tactics skill,\
 ({reg2}), {reg3?you devise:{s3} devises} a plan that will allow you and your troops to escape with your lives,\
 but you'll have to leave {reg4} soldiers behind to stop the enemy from following you.",
    "none",
    [(call_script, "script_get_max_skill_of_player_party", "skl_tactics"),
     (assign, ":max_skill", reg0),
     (assign, ":max_skill_owner", reg1),
     (assign, reg2, ":max_skill"),
     (val_add, ":max_skill", 4),

     (call_script, "script_party_count_members_with_full_health", "p_collective_enemy", 0),
     (assign, ":enemy_party_strength", reg0),
     (val_div, ":enemy_party_strength", 2),

     (store_div, reg4, ":enemy_party_strength", ":max_skill"),
     (val_max, reg4, 1),
     
     (try_begin),
       (eq, ":max_skill_owner", "trp_player"),
       (assign, reg3, 1),
     (else_try),
       (assign, reg3, 0),
       (str_store_troop_name, s3, ":max_skill_owner"),
     (try_end),
     ],
    [
      ("leave_behind",[],"Go on. The sacrifice of these troops will save the rest.",[
          (assign, ":num_casualties", reg4),
          (try_for_range, ":unused", 0, ":num_casualties"),
            (call_script, "script_cf_party_remove_random_regular_troop", "p_main_party"),
            (assign, ":lost_troop", reg0),
            (store_random_in_range, ":random_no", 0, 100),
            (ge, ":random_no", 30),
            (party_add_prisoners, "$g_encountered_party", ":lost_troop", 1),
           (try_end),
           (call_script, "script_change_player_party_morale", -20),
           (jump_to_menu, "mnu_encounter_retreat"),
          ]),
      ("dont_leave_behind",[],"No. We leave no one behind.",[(jump_to_menu, "mnu_simple_encounter"),]),
    ]
  ),
  (
    "encounter_retreat",menu_text_color(0xFF000d2c),
    "You tell {reg4} of your troops to hold the enemy while you retreat with the rest of your party.",
    "none",
    [
     ],
    [
      ("continue_3dot",[],"Continue...",[
###Troop commentary changes begin
          (call_script, "script_objectionable_action", tmt_aristocratic, "str_flee_battle"),
          (party_get_num_companion_stacks, ":num_stacks", "p_encountered_party_backup"),
          (try_for_range, ":stack_no", 0, ":num_stacks"),
              (party_stack_get_troop_id,   ":stack_troop","p_encountered_party_backup",":stack_no"),
              (is_between, ":stack_troop", faction_heroes_begin, faction_heroes_end),
              (store_troop_faction, ":victorious_faction", ":stack_troop"),
              (call_script, "script_add_log_entry", logent_player_retreated_from_lord_cowardly, "trp_player",  -1, ":stack_troop", ":victorious_faction"),
          (try_end),
###Troop commentary changes end          

          (leave_encounter),(change_screen_return)]),
    ]
  ),
  (
    "order_attack_begin",menu_text_color(0xFF000d2c),
    "Your troops prepare to attack the enemy.",
    "none",
    [],
    [
      ("order_attack_begin",[],"Order the attack to begin.", [
                                    (assign, "$g_engaged_enemy", 1),
                                    (jump_to_menu,"mnu_order_attack_2"),
                                    ]),
      ("call_back",[],"Call them back.",[(jump_to_menu,"mnu_simple_encounter")]),
    ]
  ),
  (
    "order_attack_2",menu_text_color(0xFF000d2c)|mnf_disable_all_keys,
    "{s4}^^Your casualties: {s8}^^Enemy casualties: {s9}",
    "none",
    [
                                    (call_script, "script_party_calculate_strength", "p_main_party", 1), #skip player
                                    (assign, ":player_party_strength", reg0),
                                    (val_div, ":player_party_strength", 5),
                                    (call_script, "script_party_calculate_strength", "p_collective_enemy", 0),
                                    (assign, ":enemy_party_strength", reg0),
                                    (val_div, ":enemy_party_strength", 5),
                                    
#                                    (call_script,"script_inflict_casualties_to_party", "p_main_party", ":enemy_party_strength"),
                                    (inflict_casualties_to_party_group, "p_main_party", ":enemy_party_strength", "p_temp_casualties"),
                                    (call_script, "script_print_casualties_to_s0", "p_temp_casualties", 0),
                                    (str_store_string_reg, s8, s0),
                                    
####                                    (call_script,"script_inflict_casualties_to_party", "$g_encountered_party", ":player_party_strength"),
                                    (inflict_casualties_to_party_group, "$g_encountered_party", ":player_party_strength", "p_temp_casualties"),
                                    (call_script, "script_print_casualties_to_s0", "p_temp_casualties", 0),
                                    (str_store_string_reg, s9, s0),

                                    (party_collect_attachments_to_party, "$g_encountered_party", "p_collective_enemy"),


 #                                   (assign, "$cant_leave_encounter", 0),

                                    (assign, "$no_soldiers_left", 0),
                                    (try_begin),
                                      (call_script, "script_party_count_members_with_full_health","p_main_party"),
                                      (le, reg(0), 0),
                                      (assign, "$no_soldiers_left", 1),
                                      (str_store_string, s4, "str_order_attack_failure"),
                                    (else_try),
                                      (call_script, "script_party_count_members_with_full_health","p_collective_enemy"),
                                      (le, reg(0), 0),
                                      (assign, ":continue", 0),
                                      (party_get_num_companion_stacks, ":party_num_stacks", "p_collective_enemy"),
                                      (try_begin),
                                        (eq, ":party_num_stacks", 0),
                                        (assign, ":continue", 1),
                                      (else_try),
                                        (party_stack_get_troop_id, ":party_leader", "p_collective_enemy", 0),
                                        (try_begin),
                                          (neg|troop_is_hero, ":party_leader"),
                                          (assign, ":continue", 1),
                                        (else_try),
                                          (troop_is_wounded, ":party_leader"),
                                          (assign, ":continue", 1),
                                        (try_end),
                                      (try_end),
                                      (eq, ":continue", 1),
                                      (assign, "$g_battle_result", 1),
                                      (assign, "$no_soldiers_left", 1),
                                      (str_store_string, s4, "str_order_attack_success"),
                                    (else_try),
                                      (str_store_string, s4, "str_order_attack_continue"),
                                    (try_end),
    ],
    [
      ("order_attack_continue",[(eq, "$no_soldiers_left", 0)],"Order your soldiers to continue the attack.",[
          (jump_to_menu,"mnu_order_attack_2"),
          ]),
      ("order_retreat",[(eq, "$no_soldiers_left", 0)],"Call your soldiers back.",[
          (jump_to_menu,"mnu_simple_encounter"),
          ]),
      ("continue_3dot",[(eq, "$no_soldiers_left", 1)],"Continue...",[
          (jump_to_menu,"mnu_simple_encounter"),
          ]),
    ]
  ),

  (
    "battle_debrief",menu_text_color(0xFF000d2c)|mnf_scale_picture|mnf_disable_all_keys,
    "{s11}^^Your Casualties:{s8}{s10}^^Enemy Casualties:{s9}",
    "none",
    [
     (try_begin),
       (eq, "$g_battle_result", 1),
       (call_script, "script_change_troop_renown", "trp_player", "$battle_renown_value"),
     (try_end),
############################################################################################################
##### Custom Commander(CC)
############################################################################################################
     (try_begin),
       (neq, "$g_player_troop", "trp_player"),
       (store_troop_health, "$g_player_end_hp", "trp_player"),
       (party_get_skill_level, ":first_aid_level", "p_main_party", skl_first_aid),
       (val_mul, ":first_aid_level", 5),
       (le, "$g_player_end_hp", "$g_player_begin_hp"),
       (store_sub, ":result_hp", "$g_player_begin_hp", "$g_player_end_hp"),
       (val_mul, ":result_hp", ":first_aid_level"),
       (val_div, ":result_hp", 100),
       (val_add, ":result_hp", "$g_player_end_hp"),
       (troop_set_health, "trp_player", ":result_hp"),
     (try_end),
############################################################################################################
##### Custom Commander(CC)
############################################################################################################
     (call_script, "script_encounter_calculate_fit"),

     (call_script, "script_party_count_fit_regulars", "p_main_party"),
     (assign, "$playerparty_postbattle_regulars", reg0),

     (try_begin),
       (eq, "$g_battle_result", 1),
       (eq, "$g_enemy_fit_for_battle", 0),
       (str_store_string, s11, "@You were victorious!"),
#       (play_track, "track_bogus"), #clear current track.
#       (call_script, "script_music_set_situation_with_culture", mtf_sit_victorious),
       (try_begin),
         (gt, "$g_friend_fit_for_battle", 1),
         (set_background_mesh, "mesh_pic_victory"),
       (try_end),
     (else_try),
       (eq, "$g_battle_result", -1),
       (ge, "$g_enemy_fit_for_battle",1),
       (this_or_next|le, "$g_friend_fit_for_battle",0),
       (             le, "$playerparty_postbattle_regulars", 0),
       (str_store_string, s11, "@Battle was lost. Your forces were utterly crushed."),
       (set_background_mesh, "mesh_pic_defeat"),
     (else_try),
       (eq, "$g_battle_result", -1),
       (str_store_string, s11, "@Your companions carry you away from the fighting."),
############################################################################################################
##### Custom Commander(CC)
############################################################################################################
       #(troop_get_type, ":is_female", "trp_player"),
       (troop_get_type, ":is_female", "$g_player_troop"),
############################################################################################################
##### Custom Commander(CC)
############################################################################################################
       (try_begin),
         (eq, ":is_female", 1),
         (set_background_mesh, "mesh_pic_wounded_fem"),
       (else_try),
         (set_background_mesh, "mesh_pic_wounded"),
       (try_end),
     (else_try),
       (eq, "$g_battle_result", 1),
       (str_store_string, s11, "@You have defeated the enemy."),
       (try_begin),
         (gt, "$g_friend_fit_for_battle", 1),
         (set_background_mesh, "mesh_pic_victory"),
       (try_end),
     (else_try),
       (eq, "$g_battle_result", 0),
       (str_store_string, s11, "@You have retreated from the fight."),
     (try_end),
#NPC companion changes begin
##check for excessive casualties, more forgiving if battle result is good
     (try_begin),
        (gt, "$playerparty_prebattle_regulars", 9),
        (store_add, ":divisor", 3, "$g_battle_result"), 
        (store_div, ":half_of_prebattle_regulars", "$playerparty_prebattle_regulars", ":divisor"),
        (lt, "$playerparty_postbattle_regulars", ":half_of_prebattle_regulars"),
        (call_script, "script_objectionable_action", tmt_egalitarian, "str_excessive_casualties"),
     (try_end),
#NPC companion changes end



     (call_script, "script_print_casualties_to_s0", "p_player_casualties", 0),
     (str_store_string_reg, s8, s0),
     (call_script, "script_print_casualties_to_s0", "p_enemy_casualties", 0),
     (str_store_string_reg, s9, s0),
     (str_clear, s10),
     (try_begin),
       (eq, "$any_allies_at_the_last_battle", 1),
       (call_script, "script_print_casualties_to_s0", "p_ally_casualties", 0),
       (str_store_string, s10, "@^^Ally Casualties:{s0}"),
     (try_end),
     ],
    [
      ("continue_3dot",[],"Continue...",[(jump_to_menu, "$g_next_menu"),]),
    ]
  ),


  
  (
    "total_victory",menu_text_color(0xFF000d2c),
    "You shouldn't be reading this... {s9}",
    "none",
    [
        # We exploit the menu condition system below.
        # The conditions should make sure that always another screen or menu is called.
        (assign, ":done", 0),
        (try_begin),
          # Talk to ally leader
          (eq, "$thanked_by_ally_leader", 0),
          (assign, "$thanked_by_ally_leader", 1),


          (gt, "$g_ally_party", 0),

#          (store_add, ":total_str_without_player", "$g_starting_strength_ally_party", "$g_starting_strength_enemy_party"),
          
          (store_add, ":total_str_without_player", "$g_starting_strength_friends", "$g_starting_strength_enemy_party"),
          (val_sub, ":total_str_without_player", "$g_starting_strength_main_party"),

          (store_sub, ":ally_strength_without_player", "$g_starting_strength_friends", "$g_starting_strength_main_party"),
        
          (store_mul, ":ally_advantage", ":ally_strength_without_player", 100),
          (val_add, ":total_str_without_player", 1),
          (val_div, ":ally_advantage", ":total_str_without_player"),
          #Ally advantage=50  means battle was evenly matched

          (store_sub, ":enemy_advantage", 100, ":ally_advantage"),
        
          (store_mul, ":faction_reln_boost", ":enemy_advantage", "$g_starting_strength_enemy_party"),
          (val_div, ":faction_reln_boost", 3000),
          (val_min, ":faction_reln_boost", 4),

          (store_mul, "$g_relation_boost", ":enemy_advantage", ":enemy_advantage"),
          (val_div, "$g_relation_boost", 700),
          (val_clamp, "$g_relation_boost", 0, 20),
        
          (party_get_num_companion_stacks, ":num_ally_stacks", "$g_ally_party"),
          (gt, ":num_ally_stacks", 0),
          (store_faction_of_party, ":ally_faction","$g_ally_party"),
          (call_script, "script_change_player_relation_with_faction", ":ally_faction", ":faction_reln_boost"),
          (party_stack_get_troop_id, ":ally_leader", "$g_ally_party"),
          (party_stack_get_troop_dna, ":ally_leader_dna", "$g_ally_party"),
          (try_begin),
            (troop_is_hero, ":ally_leader"),
            (troop_get_slot, ":hero_relation", ":ally_leader", slot_troop_player_relation),
            (assign, ":rel_boost", "$g_relation_boost"),
            (try_begin),
              (lt, ":hero_relation", -5),
              (val_div, ":rel_boost", 3),
            (try_end),
            (call_script,"script_change_player_relation_with_troop", ":ally_leader", ":rel_boost"),
          (try_end),
          (assign, "$talk_context", tc_ally_thanks),
          (call_script, "script_setup_troop_meeting",":ally_leader", ":ally_leader_dna"),
        (else_try),
          # Talk to enemy leaders
          (assign, ":done", 0),
          (party_get_num_companion_stacks, ":num_stacks", "p_encountered_party_backup"),
        
          (try_for_range, ":stack_no", "$last_defeated_hero", ":num_stacks"),
            (eq, ":done", 0),
            (party_stack_get_troop_id,   ":stack_troop","p_encountered_party_backup",":stack_no"),
            (party_stack_get_troop_dna,   ":stack_troop_dna","p_encountered_party_backup",":stack_no"),
            
            (troop_is_hero, ":stack_troop"),
            (store_add, "$last_defeated_hero", ":stack_no", 1),
        
            (call_script, "script_remove_troop_from_prison", ":stack_troop"),
            
            (troop_set_slot, ":stack_troop", slot_troop_leaded_party, -1),
            (store_troop_faction, ":defeated_faction", ":stack_troop"),
#steve post 0912 changes begin - removed, this is duplicated elsewhere in game menus
#            (call_script, "script_add_log_entry", logent_lord_defeated_by_player, "trp_player",  -1, ":stack_troop", ":defeated_faction"),
            (try_begin),
              (call_script, "script_cf_check_hero_can_escape_from_player", ":stack_troop"),
              (str_store_troop_name, s1, ":stack_troop"),
              (str_store_faction_name, s3, ":defeated_faction"),
              (str_store_string, s17, "@{s1} of {s3} managed to escape."),
              (display_log_message, "@{s17}"),
              (jump_to_menu, "mnu_enemy_slipped_away"),
              (assign, ":done", 1),
            (else_try),
              (assign, "$talk_context", tc_hero_defeated),
              (call_script, "script_setup_troop_meeting",":stack_troop", ":stack_troop_dna"),
              (assign, ":done", 1),
            (try_end),
          (try_end),
          (eq, ":done", 1),
        (else_try),
          # Talk to freed heroes
          (assign, ":done", 0),
          (party_get_num_prisoner_stacks, ":num_prisoner_stacks","p_encountered_party_backup"),
          (try_for_range, ":stack_no", "$last_freed_hero", ":num_prisoner_stacks"),
            (eq, ":done", 0),
            (party_prisoner_stack_get_troop_id,   ":stack_troop","p_encountered_party_backup",":stack_no"),
            (troop_is_hero, ":stack_troop"),
            (party_prisoner_stack_get_troop_dna,   ":stack_troop_dna","p_encountered_party_backup",":stack_no"),
            (store_add, "$last_freed_hero", ":stack_no", 1),
            (assign, "$talk_context", tc_hero_freed),
            (call_script, "script_setup_troop_meeting",":stack_troop", ":stack_troop_dna"),
            (assign, ":done", 1),
          (try_end),
          (eq, ":done", 1),
        (else_try),
          (eq, "$capture_screen_shown", 0),
          (assign, "$capture_screen_shown", 1),
          (party_clear, "p_temp_party"),
          (assign, "$g_move_heroes", 0),
          (call_script, "script_party_prisoners_add_party_companions", "p_temp_party", "p_collective_enemy"),
          (call_script, "script_party_add_party_prisoners", "p_temp_party", "p_collective_enemy"),

          (try_begin),
            (call_script, "script_party_calculate_strength", "p_collective_friends_backup",0),
            (assign,":total_initial_strength", reg(0)),
            (gt, ":total_initial_strength", 0),
#            (gt, "$g_ally_party", 0),
            (call_script, "script_party_calculate_strength", "p_main_party_backup",0),
            (assign,":player_party_initial_strength", reg(0)),
            # move ally_party_initial_strength/(player_party_initial_strength + ally_party_initial_strength) prisoners to ally party.
            # First we collect the share of prisoners of the ally party and distribute those among the allies.
            (store_sub, ":ally_party_initial_strength", ":total_initial_strength", ":player_party_initial_strength"),

#            (call_script, "script_party_calculate_strength", "p_ally_party_backup"),
#            (assign,":ally_party_initial_strength", reg(0)),
#            (store_add, ":total_initial_strength", ":player_party_initial_strength", ":ally_party_initial_strength"),
            (store_mul, ":ally_share", ":ally_party_initial_strength", 1000),
            (val_div, ":ally_share", ":total_initial_strength"),
            (assign, "$pin_number", ":ally_share"), #we send this as a parameter to the script.
            (party_clear, "p_temp_party_2"),
            (call_script, "script_move_members_with_ratio", "p_temp_party", "p_temp_party_2"),
        
            #TODO: This doesn't handle prisoners if our allies joined battle after us.
            (try_begin),
              (gt, "$g_ally_party", 0),
              (distribute_party_among_party_group, "p_temp_party_2", "$g_ally_party"),
            (try_end),
             #next if there's anything left, we'll open up the party exchange screen and offer them to the player.
          (try_end),
############################################################################################################
##### Custom Commander(CC)
############################################################################################################
          (assign, "$g_player_troop", "trp_player"),
          (set_player_troop, "$g_player_troop"),
############################################################################################################
##### Custom Commander(CC)
############################################################################################################		  
          (party_get_num_companions, ":num_rescued_prisoners", "p_temp_party"),
          (party_get_num_prisoners,  ":num_captured_enemies", "p_temp_party"),
          (store_add, ":total_capture_size", ":num_rescued_prisoners", ":num_captured_enemies"),
          (gt, ":total_capture_size", 0),
          (change_screen_exchange_with_party, "p_temp_party"),
        (else_try),
          (eq, "$loot_screen_shown", 0),
          (assign, "$loot_screen_shown", 1),
          (try_begin),
            (gt, "$g_ally_party", 0),
            (call_script, "script_party_add_party", "$g_ally_party", "p_temp_party"), #Add remaining prisoners to ally TODO: FIX it.
          (else_try),
            (party_get_num_attached_parties, ":num_quick_attachments", "p_main_party"),
            (gt, ":num_quick_attachments", 0),
            (party_get_attached_party_with_rank, ":helper_party", "p_main_party", 0),
            (call_script, "script_party_add_party", ":helper_party", "p_temp_party"), #Add remaining prisoners to our reinforcements
          (try_end),
          (troop_clear_inventory, "trp_temp_troop"),
          (call_script, "script_party_calculate_loot", "p_encountered_party_backup"),
          (gt, reg0, 0),
          (troop_sort_inventory, "trp_temp_troop"),
		  # Autoloot:
          #(change_screen_loot, "trp_temp_troop"),
		  (assign, "$return_menu", "mnu_total_victory"),
		  (jump_to_menu, "mnu_manage_loot_pool"),
		  #end Autoloot
        (else_try),
          #finished all
          (try_begin),
            (le, "$g_ally_party", 0),
            (end_current_battle),
          (try_end),
          (call_script, "script_party_give_xp_and_gold", "p_encountered_party_backup"),
          (try_begin),
            (eq, "$g_enemy_party", 0),
            (display_message,"str_error_string"),
          (try_end),
          (call_script, "script_event_player_defeated_enemy_party", "$g_enemy_party"),
          (call_script, "script_clear_party_group", "$g_enemy_party"),
          (try_begin),
            (eq, "$g_next_menu", -1),

#NPC companion changes begin
           (call_script, "script_post_battle_personality_clash_check"),
#NPC companion changes end

#Post 0907 changes begin
        (party_stack_get_troop_id,   ":enemy_leader","p_encountered_party_backup",0),
        (try_begin),
            (is_between, ":enemy_leader", faction_heroes_begin, faction_heroes_end),
            (neg|is_between, "$g_encountered_party", centers_begin, centers_end),
            (store_troop_faction, ":enemy_leader_faction", ":enemy_leader"),

            (try_begin),
                (eq, "$g_ally_party", 0),
                (call_script, "script_add_log_entry", logent_lord_defeated_by_player, "trp_player",  -1, ":enemy_leader", ":enemy_leader_faction"),
                (try_begin),
                  (eq, "$cheat_mode", 1),
                  (display_message, "@Victory comment. Player was alone"),
                (try_end),
            (else_try),
                (ge, "$g_strength_contribution_of_player", 40), 
                (call_script, "script_add_log_entry", logent_lord_defeated_by_player, "trp_player",  -1, ":enemy_leader", ":enemy_leader_faction"),
                (try_begin),
                  (eq, "$cheat_mode", 1),
                  (display_message, "@Ordinary victory comment. The player provided at least 40 percent forces."),
                (try_end),
            (else_try),
                (gt, "$g_starting_strength_enemy_party", 1000),
                (call_script, "script_get_closest_center", "p_main_party"),
                (assign, ":battle_of_where", reg0),
                (call_script, "script_add_log_entry", logent_player_participated_in_major_battle, "trp_player",  ":battle_of_where", -1, ":enemy_leader_faction"),
                (try_begin),
                  (eq, "$cheat_mode", 1),
                  (display_message, "@Player participation comment. The enemy had at least 1k starting strength."),
                (try_end),
            (else_try),
                (eq, "$cheat_mode", 1),
                (display_message, "@No victory comment. The battle was small, and the player provided less than 40 percent of allied strength"),
            (try_end),
        (try_end),
#Post 0907 changes end
            (val_add, "$g_total_victories", 1),
            (leave_encounter),
            (change_screen_return),
          (else_try),
            (jump_to_menu, "$g_next_menu"),
          (try_end),
        (try_end),
      ],
    [
      ("continue_3dot",[],"Continue...",[]),
        ]
  ),

  (
    "enemy_slipped_away",menu_text_color(0xFF000d2c),
    "{s17}",
    "none",
    [],
    [
      ("continue_3dot",[],"Continue...",[(jump_to_menu,"mnu_total_victory")]),
    ]
  ),

  (
    "total_defeat",menu_text_color(0xFF000d2c),
    "You shouldn't be reading this...",
    "none",
    [
        (play_track, "track_captured", 1),
           # Free prisoners
          (party_get_num_prisoner_stacks, ":num_prisoner_stacks","p_main_party"),
          (try_for_range, ":stack_no", 0, ":num_prisoner_stacks"),
            (party_prisoner_stack_get_troop_id, ":stack_troop","p_main_party",":stack_no"),
            (troop_is_hero, ":stack_troop"),
            (call_script, "script_remove_troop_from_prison", ":stack_troop"),
          (try_end),

          (call_script, "script_loot_player_items", "$g_enemy_party"),

          (assign, "$g_move_heroes", 0),
          (party_clear, "p_temp_party"),
          (call_script, "script_party_add_party_prisoners", "p_temp_party", "p_main_party"),
          (call_script, "script_party_prisoners_add_party_companions", "p_temp_party", "p_main_party"),
          (distribute_party_among_party_group, "p_temp_party", "$g_enemy_party"),
        
          (call_script, "script_party_remove_all_companions", "p_main_party"),
          (assign, "$g_move_heroes", 1),
          (call_script, "script_party_remove_all_prisoners", "p_main_party"),

          (val_add, "$g_total_defeats", 1),

          (try_begin),
            (store_random_in_range, ":random_no", 0, 100),
            (ge, ":random_no", "$g_player_luck"),
            (jump_to_menu, "mnu_permanent_damage"),
          (else_try),
            (try_begin),
              (eq, "$g_next_menu", -1),
              (leave_encounter),
              (change_screen_return),
            (else_try),
              (jump_to_menu, "$g_next_menu"),
            (try_end),
          (try_end),
          (try_begin),
            (gt, "$g_ally_party", 0),
            (call_script, "script_party_wound_all_members", "$g_ally_party"),
          (try_end),

#Troop commentary changes begin
          (party_get_num_companion_stacks, ":num_stacks", "p_encountered_party_backup"),
          (try_for_range, ":stack_no", 0, ":num_stacks"),
            (party_stack_get_troop_id,   ":stack_troop","p_encountered_party_backup",":stack_no"),
            (is_between, ":stack_troop", faction_heroes_begin, faction_heroes_end),
            (store_troop_faction, ":victorious_faction", ":stack_troop"),
            (call_script, "script_add_log_entry", logent_player_defeated_by_lord, "trp_player",  -1, ":stack_troop", ":victorious_faction"),
          (try_end),
#Troop commentary changes end

      ],
    []
  ),

  (
    "permanent_damage",menu_text_color(0xFF000d2c)|mnf_disable_all_keys,
    "{s0}",
    "none",
    [
      (assign, ":end_cond", 1),
      (try_for_range, ":unused", 0, ":end_cond"),
        (store_random_in_range, ":random_attribute", 0, 4),
        (store_attribute_level, ":attr_level", "trp_player", ":random_attribute"),
        (try_begin),
          (gt, ":attr_level", 3),
          (neq, ":random_attribute", ca_charisma),
          (try_begin),
            (eq, ":random_attribute", ca_strength),
            (str_store_string, s0, "@Some of your tendons have been damaged in the battle. You lose 1 strength."),
          (else_try),
            (eq, ":random_attribute", ca_agility),
            (str_store_string, s0, "@You took a nasty wound which will cause you to limp slightly even after it heals. Your lose 1 agility."),
##          (else_try),
##            (eq, ":random_attribute", ca_charisma),
##            (str_store_string, s0, "@After the battle you are aghast to find that one of the terrible blows you suffered has left a deep, disfiguring scar on your face, horrifying those around you. Your charisma is reduced by 1."),
          (else_try),
##            (eq, ":random_attribute", ca_intelligence),
            (str_store_string, s0, "@You have trouble thinking straight after the battle, perhaps from a particularly hard hit to your head, and frequent headaches now plague your existence. Your intelligence is reduced by 1."),
          (try_end),
        (else_try),
          (lt, ":end_cond", 200),
          (val_add, ":end_cond", 1),
        (try_end),
      (try_end),
      (try_begin),
        (eq, ":end_cond", 200),
        (try_begin),
          (eq, "$g_next_menu", -1),
          (leave_encounter),
          (change_screen_return),
        (else_try),
          (jump_to_menu, "$g_next_menu"),
        (try_end),
      (else_try),
        (troop_raise_attribute, "trp_player", ":random_attribute", -1),
      (try_end),
      ],
    [
      ("s0",
       [
         (store_random_in_range, ":random_no", 0, 4),
         (try_begin),
           (eq, ":random_no", 0),
           (str_store_string, s0, "@Perhaps I'm getting unlucky..."),
         (else_try),
           (eq, ":random_no", 1),
           (str_store_string, s0, "@Retirement is starting to sound better and better."),
         (else_try),
           (eq, ":random_no", 2),
           (str_store_string, s0, "@No matter! I will persevere!"),
         (else_try),
           (eq, ":random_no", 3),
           (troop_get_type, ":is_female", "trp_player"),
           (try_begin),
             (eq, ":is_female", 1),
             (str_store_string, s0, "@What did I do to deserve this?"),
           (else_try),
             (str_store_string, s0, "@I suppose it'll make for a good story, at least..."),
           (try_end),
         (try_end),
         ],
       "{s0}",
       [
         (try_begin),
           (eq, "$g_next_menu", -1),
           (leave_encounter),
           (change_screen_return),
         (else_try),
           (jump_to_menu, "$g_next_menu"),
         (try_end),
         ]),
      ]
  ),
  
  (
    "pre_join",menu_text_color(0xFF000d2c),
    "You come across a battle between {s2} and {s1}. You decide to...",
    "none",
    [
        (str_store_party_name, 1,"$g_encountered_party"),
        (str_store_party_name, 2,"$g_encountered_party_2"),
      ],
    [
      ("pre_join_help_attackers",[
          (store_faction_of_party, ":attacker_faction", "$g_encountered_party_2"),
          (store_relation, ":attacker_relation", ":attacker_faction", "fac_player_supporters_faction"),
          (store_faction_of_party, ":defender_faction", "$g_encountered_party"),
          (store_relation, ":defender_relation", ":defender_faction", "fac_player_supporters_faction"),
          (ge, ":attacker_relation", 0),
          (lt, ":defender_relation", 0),
          ],
          "Move in to help the {s2}.",[
              (select_enemy,0),
              (assign,"$g_enemy_party","$g_encountered_party"),
              (assign,"$g_ally_party","$g_encountered_party_2"),
              (jump_to_menu,"mnu_join_battle")]),
      ("pre_join_help_defenders",[
          (store_faction_of_party, ":attacker_faction", "$g_encountered_party_2"),
          (store_relation, ":attacker_relation", ":attacker_faction", "fac_player_supporters_faction"),
          (store_faction_of_party, ":defender_faction", "$g_encountered_party"),
          (store_relation, ":defender_relation", ":defender_faction", "fac_player_supporters_faction"),
          (ge, ":defender_relation", 0),
          (lt, ":attacker_relation", 0),
          ],
          "Rush to the aid of the {s1}.",[
              (select_enemy,1),
              (assign,"$g_enemy_party","$g_encountered_party_2"),
              (assign,"$g_ally_party","$g_encountered_party"),
              (jump_to_menu,"mnu_join_battle")]),
      ("pre_join_leave",[],"Don't get involved.",[(leave_encounter),(change_screen_return)]),
    ]
  ),
  (
    "join_battle",menu_text_color(0xFF000d2c),
    "You are helping the {s2} against the {s1}. You have {reg10} troops fit for battle against the enemy's {reg11}.",
    "none",
    [
        (str_store_party_name, 1,"$g_enemy_party"),
        (str_store_party_name, 2,"$g_ally_party"),

        (call_script, "script_encounter_calculate_fit"),

        (try_begin),
          (eq, "$new_encounter", 1),
          (assign, "$new_encounter", 0),
          (call_script, "script_encounter_init_variables"),
##          (assign, "$capture_screen_shown", 0),
##          (assign, "$loot_screen_shown", 0),
##          (assign, "$g_battle_result", 0),
##          (assign, "$cant_leave_encounter", 0),
##          (assign, "$last_defeated_hero", 0),
##          (assign, "$last_freed_hero", 0),
##          (call_script, "script_party_copy", "p_main_party_backup", "p_main_party"),
##          (call_script, "script_party_copy", "p_encountered_party_backup", "p_collective_enemy"),
##          (call_script, "script_party_copy", "p_ally_party_backup", "p_collective_ally"),
        (else_try), #second or more turn
          (eq, "$g_leave_encounter",1),
          (change_screen_return),
        (try_end),

        (try_begin),
          (call_script, "script_party_count_members_with_full_health","p_collective_enemy"),
          (assign, ":num_enemy_regulars_remaining", reg(0)),
          (assign, ":enemy_finished",0),
          (try_begin),
            (eq, "$g_battle_result", 1),
            (eq, ":num_enemy_regulars_remaining", 0), #battle won
            (assign, ":enemy_finished",1),
          (else_try),
            (eq, "$g_engaged_enemy", 1),
            (le, "$g_enemy_fit_for_battle",0),
            (ge, "$g_friend_fit_for_battle",1),
            (assign, ":enemy_finished",1),
          (try_end),
          (this_or_next|eq, ":enemy_finished",1),
          (eq,"$g_enemy_surrenders",1),
          (assign, "$g_next_menu", -1),
          (jump_to_menu, "mnu_total_victory"),
        (else_try),
#          (eq, "$encountered_party_hostile", 1),
          (call_script, "script_party_count_members_with_full_health","p_collective_friends"),
          (assign, ":ally_num_soldiers", reg(0)),
          (assign, ":battle_lost", 0),
          (try_begin),
            (eq, "$g_battle_result", -1),
            (eq, ":ally_num_soldiers", 0), #battle lost
            (assign, ":battle_lost",1),
          (try_end),
          (this_or_next|eq, ":battle_lost",1),
          (eq,"$g_player_surrenders",1),
        # TODO: Split prisoners to all collected parties.
        # NO Need? Let default battle logic do it for us. 
#          (assign, "$g_move_heroes", 0),
#          (call_script, "script_party_add_party_prisoners", "$g_enemy_party", "p_collective_ally"),
#          (call_script, "script_party_prisoners_add_party_companions", "$g_enemy_party", "p_collective_ally"),
        #TODO: Clear all attached allies.
#          (call_script, "script_party_remove_all_companions", "$g_ally_party"),
#          (call_script, "script_party_remove_all_prisoners", "$g_ally_party"),
          (leave_encounter),
          (change_screen_return),
        (try_end),
      ],
    [

############################################################################################################
##### Custom Commander(CC)
############################################################################################################
    
      ("commander_change",[(str_store_troop_name,s7,"$g_player_troop")],
        "Change the commander. (Current:{s7})",
        [
          (assign, "$g_next_menu", "mnu_join_battle"),
          (assign, "$change_commander_menu_offset", 0),
          (jump_to_menu, "mnu_change_commander"),
        ]),

############################################################################################################
##### Custom Commander(CC)
############################################################################################################
	
      ("join_attack",[
############################################################################################################
##### Custom Commander(CC)
############################################################################################################
          #(neg|troop_is_wounded, "trp_player"),
          (neg|troop_is_wounded, "$g_player_troop"),
############################################################################################################
##### Custom Commander(CC)
############################################################################################################
          ],
                            "Charge the enemy.",[
                                (party_set_next_battle_simulation_time, "$g_encountered_party", -1),
                                (assign, "$g_battle_result", 0),
                                (call_script, "script_calculate_renown_value"),
                                (call_script, "script_calculate_battle_advantage"),
                                (set_battle_advantage, reg0),
                                (set_party_battle_mode),
								#SW - trying to modify so ship battles (ie. terrain = steppe) have no mounts (nevermind, I added a 'board ship' menu option)
								#(set_jump_mission,"mt_lead_charge"),
								# new code ---------------------------------------------
								#(party_get_current_terrain, ":terrain_type", "p_main_party"),
								#(try_begin),
								#  (eq, ":terrain_type", rt_steppe),
								#	(set_jump_mission,"mt_lead_charge_no_horse"),
								#  (else_try),
								#	(set_jump_mission,"mt_lead_charge"),
								#  (try_end),      
								# ------------------------------------------------------
								(set_jump_mission,"mt_lead_charge"),
                                (call_script, "script_setup_random_scene"),
                                (assign, "$g_next_menu", "mnu_join_battle"),
                                (jump_to_menu, "mnu_battle_debrief"),
                                (change_screen_mission),
                                ]),

      ("join_order_attack",[
#          (gt, "$encountered_party_hostile", 0),
          (call_script, "script_party_count_members_with_full_health", "p_main_party"),(ge, reg(0), 3),
          ],
           "Order your troops to attack with your allies while you stay back.",[(party_set_next_battle_simulation_time, "$g_encountered_party", -1),
                                                                         (jump_to_menu,"mnu_join_order_attack"),
                                                            ]),
      
#      ("join_attack",[],"Lead a charge against the enemies",[(set_jump_mission,"mt_charge_with_allies"),
#                                (call_script, "script_setup_random_scene"),
#                                                             (change_screen_mission,0)]),
      ("leave_dot",[],"Leave.",[
        (try_begin),
           (neg|troop_is_wounded, "trp_player"),
           (call_script, "script_objectionable_action", tmt_aristocratic, "str_flee_battle"),
           (party_stack_get_troop_id, ":enemy_leader","$g_enemy_party",0),
           (call_script, "script_add_log_entry", logent_player_retreated_from_lord, "trp_player",  -1, ":enemy_leader", -1),
           (display_message, "@Player retreats from battle"),
        (try_end),

          (leave_encounter),(change_screen_return)]),
    ]
  ),


  (
    "join_order_attack",menu_text_color(0xFF000d2c)|mnf_disable_all_keys,
    "{s4}^^Your casualties: {s8}^^Allies' casualties: {s9}^^Enemy casualties: {s10}",
    "none",
    [
                                    (call_script, "script_party_calculate_strength", "p_main_party", 1), #skip player
                                    (assign, ":player_party_strength", reg0),
                                    (val_div, ":player_party_strength", 5),
                                    (call_script, "script_party_calculate_strength", "p_collective_friends", 0),
                                    (assign, ":friend_party_strength", reg0),
                                    (val_div, ":friend_party_strength", 5),
                                    
                                    (call_script, "script_party_calculate_strength", "p_collective_enemy", 0),
                                    (assign, ":enemy_party_strength", reg0),
                                    (val_div, ":enemy_party_strength", 5),

                                    (assign, ":enemy_party_strength_for_p", ":enemy_party_strength"),
                                    (val_mul, ":enemy_party_strength_for_p", ":player_party_strength"),
                                    (val_div, ":enemy_party_strength_for_p", ":friend_party_strength"),

                                    (val_sub, ":enemy_party_strength", ":enemy_party_strength_for_p"),
                                    (inflict_casualties_to_party_group, "p_main_party", ":enemy_party_strength_for_p", "p_temp_casualties"),
                                    (call_script, "script_print_casualties_to_s0", "p_temp_casualties", 0),
                                    (str_store_string_reg, s8, s0),
                                    
                                    (inflict_casualties_to_party_group, "$g_enemy_party", ":friend_party_strength", "p_temp_casualties"),
                                    (call_script, "script_print_casualties_to_s0", "p_temp_casualties", 0),
                                    (str_store_string_reg, s10, s0),
                                    
                                    (call_script, "script_collect_friendly_parties"),
#                                    (party_collect_attachments_to_party, "$g_ally_party", "p_collective_ally"),

                                    (inflict_casualties_to_party_group, "$g_ally_party", ":enemy_party_strength", "p_temp_casualties"),
                                    (call_script, "script_print_casualties_to_s0", "p_temp_casualties", 0),
                                    (str_store_string_reg, s9, s0),
                                    (party_collect_attachments_to_party, "$g_enemy_party", "p_collective_enemy"),

#                                    (assign, "$cant_leave_encounter", 0),
                                    (assign, "$no_soldiers_left", 0),
                                    (try_begin),
                                      (call_script, "script_party_count_members_with_full_health","p_main_party"),
                                      (le, reg(0), 0),
                                      (assign, "$no_soldiers_left", 1),
                                      (str_store_string, s4, "str_join_order_attack_failure"),
                                    (else_try),
                                      (call_script, "script_party_count_members_with_full_health","p_collective_enemy"),
                                      (le, reg(0), 0),
                                      (assign, "$g_battle_result", 1),
                                      (assign, "$no_soldiers_left", 1),
                                      (str_store_string, s4, "str_join_order_attack_success"),
                                    (else_try),
                                      (str_store_string, s4, "str_join_order_attack_continue"),
                                    (try_end),
    ],
    [
      ("continue_3dot",[],"Continue...",[
          (jump_to_menu,"mnu_join_battle"),
          ]),
    ]
  ),
  
# Towns
  # (
    # "zendar",menu_text_color(0xFF000d2c)|mnf_auto_enter,
    # "You enter the town of Zendar.",
    # "none",
    # [(reset_price_rates,0),(set_price_rate_for_item,"itm_tools",70),(set_price_rate_for_item,"itm_salt",140)],
    # [
      # ("zendar_enter",[],"_",[(set_jump_mission,"mt_town_default"),(jump_to_scene,"scn_zendar_center"),(change_screen_mission)],"Door to the town center."),
      # ("zendar_tavern",[],"_",[(set_jump_mission,"mt_town_default"),
                                                   # (jump_to_scene,"scn_the_happy_boar"),
                                                   # (change_screen_mission)],"Door to the cantina."),
      # ("zendar_merchant",[],"_",[(set_jump_mission,"mt_town_default"),
                                                   # (jump_to_scene,"scn_zendar_merchant"),
                                                   # (change_screen_mission)],"Door to the merchant."),
      # ("zendar_arena",[],"_",[(set_jump_mission,"mt_town_default"),
                                                   # (jump_to_scene,"scn_zendar_arena"),
                                                   # (change_screen_mission)],"Door to the arena."),
#      ("zendar_leave",[],"Leave town.",[[leave_encounter],[change_screen_return]]),
      # ("town_1_leave",[],"_",[(leave_encounter),(change_screen_return)]),
    # ]
  # ),
  # (
    # "salt_mine",menu_text_color(0xFF000d2c)|mnf_auto_enter,
    # "You enter the salt mine.",
    # "none",
    # [(reset_price_rates,0),(set_price_rate_for_item,"itm_salt",55)],
    # [
      # ("enter",[],"Enter.",[(set_jump_mission,"mt_town_center"),(jump_to_scene,"scn_salt_mine"),(change_screen_mission)]),
      # ("leave",[],"Leave.",[(leave_encounter),(change_screen_return)]),
    # ]
  # ),
  # (
    # "four_ways_inn",menu_text_color(0xFF000d2c)|mnf_auto_enter,
    # "You arrive at the Four Ways Inn.",
    # "none",
    # [],
    # [

#      ("enter",[],"Enter.",[[set_jump_mission,"mt_town_default"],[jump_to_scene,"scn_conversation_scene"],[change_screen_mission]]),
      # ("enter",[],"Enter.",[(set_jump_mission,"mt_camera_test"),(jump_to_scene,"scn_four_ways_inn"),(change_screen_mission)]),
      # ("leave",[],"Leave.",[(leave_encounter),(change_screen_return)]),
    # ]
  # ),
  # (
    # "test_scene",menu_text_color(0xFF000d2c)|mnf_auto_enter,
    # "You enter the test scene.",
    # "none",
    # [],
    # [

      # ("enter",[],"Enter.",[[set_jump_mission,"mt_ai_training"],[jump_to_scene,"scn_test_scene"],[change_screen_mission]]),
      # ("leave",[],"Leave.",[(leave_encounter),(change_screen_return)]),
    # ]
  # ),
  # (
    # "battlefields",menu_text_color(0xFF000d2c),
    # "Select a field...",
    # "none",
    # [],
    # [

      # ("enter_f1",[],"Field 1",[[set_jump_mission,"mt_ai_training"],[jump_to_scene,"scn_field_1"],[change_screen_mission]]),
      # ("enter_f2",[],"Field 2",[[set_jump_mission,"mt_ai_training"],[jump_to_scene,"scn_field_2"],[change_screen_mission]]),
      # ("enter_f3",[],"Field 3",[[set_jump_mission,"mt_ai_training"],[jump_to_scene,"scn_field_3"],[change_screen_mission]]),
      # ("enter_f4",[],"Field 4",[[set_jump_mission,"mt_ai_training"],[jump_to_scene,"scn_field_4"],[change_screen_mission]]),
      # ("enter_f5",[],"Field 5",[[set_jump_mission,"mt_ai_training"],[jump_to_scene,"scn_field_5"],[change_screen_mission]]),
      # ("leave",[],"Leave.",[(leave_encounter),(change_screen_return)]),
    # ]
  # ),
  # (
    # "dhorak_keep",menu_text_color(0xFF000d2c),
#    "Dhorak Keep, the stronghold of the bandits stands overlooking the barren wilderness.",
    # "You enter the Dhorak Keep",
    # "none",
    # [],
    # [
      # ("enter",[],"Enter.",[(set_jump_mission,"mt_town_center"),(jump_to_scene,"scn_dhorak_keep"),(change_screen_mission)]),
      # ("leave",[],"Leave.",[(leave_encounter),(change_screen_return)]),
    # ]
  # ),
  
##  (
##    "center_under_attack_while_resting",menu_text_color(0xFF000d2c),
##    "{s1} has been besieged by {s2}, and the enemy seems to be preparing for an assault!\
## What will you do?",
##    "none",
##    [
##        (party_get_battle_opponent, ":besieger_party", "$auto_enter_town"),
##        (str_store_party_name, s1, "$auto_enter_town"),
##        (str_store_party_name, s2, ":besieger_party"),
##    ],
##    [
##      ("defend_against_siege", [],"Help the defenders of {s1}!",
##       [
##           (assign, "$g_last_player_do_nothing_against_siege_next_check", 0),
##           (rest_for_hours, 0, 0, 0),
##           (change_screen_return),
##           (start_encounter, "$auto_enter_town"),
##           ]),
##      ("do_not_defend_against_siege",[],"Find a secure place and wait there.",
##       [
##           (change_screen_return),
##           ]),
##    ]
##  ),

  (
    "join_siege_outside",menu_text_color(0xFF000d2c)|mnf_scale_picture,
    "{s1} has come under siege by {s2}.",
    "none",
    [
        (str_store_party_name, s1, "$g_encountered_party"),
        (str_store_party_name, s2, "$g_encountered_party_2"),
############################################################################################################
##### Custom Commander(CC)
############################################################################################################
       #(troop_get_type, ":is_female", "trp_player"),
       (troop_get_type, ":is_female", "$g_player_troop"),
############################################################################################################
##### Custom Commander(CC)
############################################################################################################
        (try_begin),
          (eq, ":is_female", 1),
          (set_background_mesh, "mesh_pic_siege_sighted_fem"),
        (else_try),
          (set_background_mesh, "mesh_pic_siege_sighted"),
        (try_end),
    ],
    [
      ("approach_besiegers",[(store_faction_of_party, ":faction_no", "$g_encountered_party_2"),
                             (store_relation, ":relation", ":faction_no", "fac_player_supporters_faction"),
                             (ge, ":relation", 0),
                             (store_faction_of_party, ":faction_no", "$g_encountered_party"),
                             (store_relation, ":relation", ":faction_no", "fac_player_supporters_faction"),
                             (lt, ":relation", 0),
                             ],"Approach the siege camp.",[
          (jump_to_menu, "mnu_besiegers_camp_with_allies"),
                                ]),
      ("pass_through_siege",[(store_faction_of_party, ":faction_no", "$g_encountered_party"),
                             (store_relation, ":relation", ":faction_no", "fac_player_supporters_faction"),
                             (ge, ":relation", 0),
                             ],"Pass through the siege lines and enter {s1}.",
       [
            (jump_to_menu,"mnu_cut_siege_without_fight"),
          ]),
      ("leave_dot",[],"Leave.",[(leave_encounter),
                            (change_screen_return)]),
    ]
  ),
  (
    "cut_siege_without_fight",menu_text_color(0xFF000d2c),
    "The besieging fleet lets you pass without challenge, despite a suspicious tone from the communications operator.",
    "none",
    [],
    [
      ("continue_3dot",[],"Continue...",[(try_begin),
                                   (this_or_next|eq, "$g_encountered_party_faction", "fac_player_supporters_faction"),
                                   (eq, "$g_encountered_party_faction", "$players_faction"),
                                   (jump_to_menu, "mnu_town"),
                                 (else_try),
                                   (jump_to_menu, "mnu_spacestation_outside"),
                                 (try_end)]),
      ]
  ),
  (
    "besiegers_camp_with_allies",menu_text_color(0xFF000d2c),
    "{s1} remains under blockade. The blockading ships bear the signature of {s2},\
 and your fleet is welcomed.",
    "none",
    [
        (str_store_party_name, s1, "$g_encountered_party"),
        (str_store_party_name, s2, "$g_encountered_party_2"),
        (assign, "$g_enemy_party", "$g_encountered_party"),
        (assign, "$g_ally_party", "$g_encountered_party_2"),
        (select_enemy, 0),
        (call_script, "script_encounter_calculate_fit"),
        (try_begin),
          (eq, "$new_encounter", 1),
          (assign, "$new_encounter", 0),
          (call_script, "script_encounter_init_variables"),
        (try_end),

        (try_begin),
          (eq, "$g_leave_encounter",1),
          (change_screen_return),
        (else_try),
          (assign, ":enemy_finished", 0),
          (try_begin),
            (eq, "$g_battle_result", 1),
            (assign, ":enemy_finished", 1),
          (else_try),
            (le, "$g_enemy_fit_for_battle", 0),
            (ge, "$g_friend_fit_for_battle", 1),
            (assign, ":enemy_finished", 1),
          (try_end),
          (this_or_next|eq, ":enemy_finished", 1),
          (eq, "$g_enemy_surrenders", 1),
##          (assign, "$g_next_menu", -1),#"mnu_spacestation_taken_by_friends"),
##          (jump_to_menu, "mnu_total_victory"),
          (call_script, "script_party_wound_all_members", "$g_enemy_party"),
          (leave_encounter),
          (change_screen_return),
        (else_try),
          (call_script, "script_party_count_members_with_full_health", "p_collective_friends"),
          (assign, ":ally_num_soldiers", reg0),
          (eq, "$g_battle_result", -1),
          (eq, ":ally_num_soldiers", 0), #battle lost
          (leave_encounter),
          (change_screen_return),
        (try_end),
        ],
    [
      ("talk_to_siege_commander",[]," Request a meeting with the commander.",[
                                (modify_visitors_at_site,"scn_conversation_scene"),(reset_visitors),
                                (set_visitor,0,"trp_player"),
                                (party_stack_get_troop_id, ":siege_leader_id","$g_encountered_party_2",0),
                                (party_stack_get_troop_dna,":siege_leader_dna","$g_encountered_party_2",0),
                                (set_visitor,17,":siege_leader_id",":siege_leader_dna"),
                                (set_jump_mission,"mt_conversation_encounter"),
                                (jump_to_scene,"scn_conversation_scene"),
                                (assign, "$talk_context", tc_siege_commander),
                                (change_screen_map_conversation, ":siege_leader_id")]),
############################################################################################################
##### Custom Commander(CC)
############################################################################################################

      ("commander_change",[(str_store_troop_name,s7,"$g_player_troop")],
        "Change the commander. (Current:{s7})",
        [
          (assign, "$g_next_menu", "mnu_besiegers_camp_with_allies"),
          (assign, "$change_commander_menu_offset", 0),
          (jump_to_menu, "mnu_change_commander"),
        ]),

############################################################################################################
##### Custom Commander(CC)
############################################################################################################
      ("join_siege_with_allies",
      [
############################################################################################################
##### Custom Commander(CC)
############################################################################################################
          #(neg|troop_is_wounded, "trp_player"),
          (neg|troop_is_wounded, "$g_player_troop"),
############################################################################################################
##### Custom Commander(CC)
############################################################################################################
      ], "Join the next assault.",
       [
           (party_set_next_battle_simulation_time, "$g_encountered_party", -1),
           (try_begin),
             (check_quest_active, "qst_join_siege_with_army"),
             (quest_slot_eq, "qst_join_siege_with_army", slot_quest_target_center, "$g_encountered_party"),
             (add_xp_as_reward, 250),
             (call_script, "script_end_quest", "qst_join_siege_with_army"),
             #Reactivating follow army quest
             (faction_get_slot, ":faction_marshall", "$players_faction", slot_faction_marshall),
             (str_store_troop_name_link, s9, ":faction_marshall"),
             (setup_quest_text, "qst_follow_army"),
             (str_store_string, s2, "@{s9} wants you to follow his army until further notice."),
             (call_script, "script_start_quest", "qst_follow_army", ":faction_marshall"),
             (assign, "$g_player_follow_army_warnings", 0),
           (try_end),
           (try_begin),
             (party_slot_eq, "$g_encountered_party", slot_party_type, spt_mainplanet),
             (party_get_slot, ":battle_scene", "$g_encountered_party", slot_mainplanet_walls),
           (else_try),
             (party_get_slot, ":battle_scene", "$g_encountered_party", slot_spacestation_exterior),
           (try_end),
           (call_script, "script_calculate_battle_advantage"),
           (val_mul, reg0, 2),
           (val_div, reg0, 3), #scale down the advantage a bit in sieges.
           (set_battle_advantage, reg0),
           (set_party_battle_mode),
           (try_begin),
             (party_slot_eq, "$g_encountered_party", slot_center_siege_with_belfry, 1),
             (set_jump_mission,"mt_spacestation_attack_walls_belfry"),
           (else_try),
             (set_jump_mission,"mt_spacestation_attack_walls_ladder"),
           (try_end),
           (jump_to_scene,":battle_scene"),
           (assign, "$g_siege_final_menu", "mnu_besiegers_camp_with_allies"),
           (assign, "$g_siege_battle_state", 1),
           (assign, "$g_next_menu", "mnu_spacestation_besiege_inner_battle"),
##           (assign, "$g_next_menu", "mnu_besiegers_camp_with_allies"),
           (jump_to_menu, "mnu_battle_debrief"),
           (change_screen_mission),
          ]),
      ("join_siege_stay_back", [(call_script, "script_party_count_members_with_full_health", "p_main_party"),
                                (ge, reg0, 3),
                                ],
       "Order your soldiers to join the next assault without you.",
       [
         (party_set_next_battle_simulation_time, "$g_encountered_party", -1),
         (try_begin),
           (check_quest_active, "qst_join_siege_with_army"),
           (quest_slot_eq, "qst_join_siege_with_army", slot_quest_target_center, "$g_encountered_party"),
           (add_xp_as_reward, 100),
           (call_script, "script_end_quest", "qst_join_siege_with_army"),
           #Reactivating follow army quest
           (faction_get_slot, ":faction_marshall", "$players_faction", slot_faction_marshall),
           (str_store_troop_name_link, s9, ":faction_marshall"),
           (setup_quest_text, "qst_follow_army"),
           (str_store_string, s2, "@{s9} wants you to follow his army until further notice."),
           (call_script, "script_start_quest", "qst_follow_army", ":faction_marshall"),
           (assign, "$g_player_follow_army_warnings", 0),
         (try_end),
         (jump_to_menu,"mnu_spacestation_attack_walls_with_allies_simulate")]),
      ("leave_dot",[],"Leave.",[(leave_encounter),(change_screen_return)]),
    ]
  ),

  (
    "spacestation_outside",menu_text_color(0xFF000d2c),
    "You are outside {s2}.{s11} {s3} {s4}",
    "none",
    [
        (assign, "$g_enemy_party", "$g_encountered_party"),
        (assign, "$g_ally_party", -1),
        (str_store_party_name, s2,"$g_encountered_party"),
        (call_script, "script_encounter_calculate_fit"),
        (assign,"$all_doors_locked",1),
        (assign, "$current_town","$g_encountered_party"),
		
		#SW - display a new menu background
		(call_script, "script_display_fullscreen_background", "$current_town"),	
		
        (try_begin),
          (eq, "$new_encounter", 1),
          (assign, "$new_encounter", 0),
          (call_script, "script_let_nearby_parties_join_current_battle", 1, 0),
          (call_script, "script_encounter_init_variables"),
          (assign, "$entry_to_town_forbidden",0),
          (assign, "$sneaked_into_town",0),
          (assign, "$town_entered", 0),
#          (assign, "$waiting_for_arena_fight_result", 0),
          (assign, "$encountered_party_hostile", 0),
          (assign, "$encountered_party_friendly", 0),
          (try_begin),
            (gt, "$g_player_besiege_town", 0),
            (neq,"$g_player_besiege_town","$g_encountered_party"),
            (party_slot_eq, "$g_player_besiege_town", slot_center_is_besieged_by, "p_main_party"),
            (call_script, "script_lift_siege", "$g_player_besiege_town", 0),
            (assign,"$g_player_besiege_town",-1),
          (try_end),
          (try_begin),
            (lt, "$g_encountered_party_relation", 0),
            (assign, "$encountered_party_hostile", 1),
            (assign,"$entry_to_town_forbidden",1),
          (try_end),

          (assign,"$cant_sneak_into_town",0),
          (try_begin),
            (eq,"$current_town","$last_sneak_attempt_town"),
            (store_current_hours,reg(2)),
            (val_sub,reg(2),"$last_sneak_attempt_time"),
            (lt,reg(2),12),
            (assign,"$cant_sneak_into_town",1),
          (try_end),
        (else_try), #second or more turn
          (eq, "$g_leave_encounter",1),
          (change_screen_return),
        (try_end),

        (str_clear,s4),
        (try_begin), 
          (eq,"$entry_to_town_forbidden",1),
          (try_begin),
            (eq,"$cant_sneak_into_town",1),
            (str_store_string,s4,"str_sneaking_to_town_impossible"),
          (else_try),
            (str_store_string,s4,"str_entrance_to_town_forbidden"),
          (try_end),
        (try_end),

        (party_get_slot, ":center_lord", "$current_town", slot_mainplanet_lord),
        (store_faction_of_party, ":center_faction", "$current_town"),
        (str_store_faction_name,s9,":center_faction"),
        (try_begin),
          (ge, ":center_lord", 0),
          (str_store_troop_name,s8,":center_lord"),
          (str_store_string,s7,"@{s8} of {s9}"),
        (try_end),

        (try_begin), # same mnu_town
          (party_slot_eq,"$current_town",slot_party_type, spt_castle),
          (try_begin),
            (eq, ":center_lord", "trp_player"),
            (str_store_string,s11,"@ Your own banner flies over the entrance."),
          (else_try),
            (ge, ":center_lord", 0),
            (str_store_string,s11,"@ You see the banner of {s7} over the entrance."),
          (else_try),
            (str_store_string,s11,"@ This castle seems to belong to no one."),
          (try_end),
        (else_try),
          (try_begin),
            (eq, ":center_lord", "trp_player"),
            (str_store_string,s11,"@ Your own banner flies over the entrance."),
          (else_try),
            (ge, ":center_lord", 0),
            (str_store_string,s11,"@ You see the banner of {s7} over the entrance."),
          (else_try),
            (str_store_string,s11,"@ The citizens here have declared their independence."),
          (try_end),
        (try_end),

        (party_get_num_companions, reg(7),"p_collective_enemy"),
        (assign,"$spacestation_undefended",0),
        (str_clear, s3),
        (try_begin),
          (eq,reg(7),0),
          (assign,"$spacestation_undefended",1),
#          (party_set_faction,"$g_encountered_party","fac_neutral"),
#          (party_set_slot, "$g_encountered_party", slot_mainplanet_lord, stl_unassigned),
          (str_store_string, s3, "str_spacestation_is_abondened"),
        (else_try),
          (eq,"$g_encountered_party_faction","fac_player_supporters_faction"),
          (str_store_string, s3, "str_place_is_occupied_by_player"),
        (else_try),
          (lt, "$g_encountered_party_relation", 0),
          (str_store_string, s3, "str_place_is_occupied_by_enemy"),
        (else_try),
#          (str_store_string, s3, "str_place_is_occupied_by_friendly"),
        (try_end),

        (try_begin),
          (eq, "$g_leave_town_outside",1),
          (assign, "$g_leave_town_outside",0),
          (assign, "$g_permitted_to_center", 0),
          (change_screen_return),
        (else_try),
          (check_quest_active, "qst_escort_lady"),
          (quest_slot_eq, "qst_escort_lady", slot_quest_target_center, "$g_encountered_party"),
          (quest_get_slot, ":quest_object_troop", "qst_escort_lady", slot_quest_object_troop),
          (modify_visitors_at_site,"scn_conversation_scene"),
          (reset_visitors),
          (set_visitor,0, "trp_player"),
          (set_visitor,17, ":quest_object_troop"),
          (set_jump_mission, "mt_conversation_encounter"),
          (jump_to_scene, "scn_conversation_scene"),
          (assign, "$talk_context", tc_entering_center_quest_talk),
          (change_screen_map_conversation, ":quest_object_troop"),
        (else_try),
          (check_quest_active, "qst_kidnapped_girl"),
          (quest_slot_eq, "qst_kidnapped_girl", slot_quest_giver_center, "$g_encountered_party"),
          (quest_slot_eq, "qst_kidnapped_girl", slot_quest_current_state, 3),
          (modify_visitors_at_site,"scn_conversation_scene"),
          (reset_visitors),
          (set_visitor,0, "trp_player"),
          (set_visitor,17, "trp_kidnapped_girl"),
          (set_jump_mission, "mt_conversation_encounter"),
          (jump_to_scene, "scn_conversation_scene"),
          (assign, "$talk_context", tc_entering_center_quest_talk),
          (change_screen_map_conversation, "trp_kidnapped_girl"),
##        (else_try),
##          (gt, "$lord_requested_to_talk_to", 0),
##          (store_current_hours, ":cur_hours"),
##          (neq, ":cur_hours", "$quest_given_time"),
##          (modify_visitors_at_site,"scn_conversation_scene"),
##          (reset_visitors),
##          (assign, ":cur_lord", "$lord_requested_to_talk_to"),
##          (assign, "$lord_requested_to_talk_to", 0),
##          (set_visitor,0,"trp_player"),
##          (set_visitor,17,":cur_lord"),
##          (set_jump_mission,"mt_conversation_encounter"),
##          (jump_to_scene,"scn_conversation_scene"),
##          (assign, "$talk_context", tc_spacestation_gate_lord),
##          (change_screen_map_conversation, ":cur_lord"),
        (else_try),
          (eq, "$g_town_visit_after_rest", 1),
          (assign, "$g_town_visit_after_rest", 0),
          (jump_to_menu,"mnu_town"),
        (else_try),
          (party_slot_eq,"$g_encountered_party", slot_mainplanet_lord, "trp_player"),
          (party_slot_eq,"$g_encountered_party", slot_party_type,spt_castle),
          (jump_to_menu, "mnu_enter_your_own_castle"),
        (else_try),
          (party_slot_eq,"$g_encountered_party", slot_party_type,spt_castle),
          (ge, "$g_encountered_party_relation", 0),
          (this_or_next|eq,"$spacestation_undefended",1),
          (eq, "$g_permitted_to_center",1),
          (jump_to_menu, "mnu_town"),
        (else_try),
          (party_slot_eq,"$g_encountered_party", slot_party_type,spt_mainplanet),
          (ge, "$g_encountered_party_relation", 0),
          (jump_to_menu, "mnu_town"),
        (else_try),
          (eq, "$g_player_besiege_town", "$g_encountered_party"),
          (jump_to_menu, "mnu_spacestation_besiege"),
        (try_end),
        ],
    [
#        ("talk_to_spacestation_commander",[
#            (party_get_num_companions, ":no_companions", "$g_encountered_party"),
#            (ge, ":no_companions", 1),
#            (eq,"$ruler_meeting_denied",0), #this variable is removed
#            ],
#         "Request a meeting with the lord of the castle.",[
#             (modify_visitors_at_site,"scn_conversation_scene"),(reset_visitors),
#             (set_visitor,0,"trp_player"),
#             (party_stack_get_troop_id, reg(6),"$g_encountered_party",0),
#             (party_stack_get_troop_dna,reg(7),"$g_encountered_party",0),
#             (set_visitor,17,reg(6),reg(7)),
#             (set_jump_mission,"mt_conversation_encounter"),
#             (jump_to_scene,"scn_conversation_scene"),
#             (assign, "$talk_context", tc_spacestation_commander),
#             (change_screen_map_conversation, reg(6))
#             ]),
      ("approach_gates",[(this_or_next|eq,"$entry_to_town_forbidden",1),
                          (party_slot_eq,"$g_encountered_party", slot_party_type,spt_castle)],
       "Approach the planet and contact the guards.",[
                                                  (jump_to_menu, "mnu_spacestation_guard"),
##                                                   (modify_visitors_at_site,"scn_conversation_scene"),(reset_visitors),
##                                                   (set_visitor,0,"trp_player"),
##                                                   (store_faction_of_party, ":cur_faction", "$g_encountered_party"),
##                                                   (faction_get_slot, ":cur_guard", ":cur_faction", slot_faction_guard_troop),
##                                                   (set_visitor,17,":cur_guard"),
##                                                   (set_jump_mission,"mt_conversation_encounter"),
##                                                   (jump_to_scene,"scn_conversation_scene"),
##                                                   (assign, "$talk_context", tc_spacestation_gate),
##                                                   (change_screen_map_conversation, ":cur_guard")
                                                   ]),
      
      ("town_sneak",[(party_slot_eq,"$g_encountered_party", slot_party_type,spt_mainplanet),
                     (eq,"$entry_to_town_forbidden",1),
                     (eq,"$cant_sneak_into_town",0)],
       "Disguise yourself and try to sneak onto the planet's capital.",
       [
         (faction_get_slot, ":player_alarm", "$g_encountered_party_faction", slot_faction_player_alarm),
         (party_get_num_companions, ":num_men", "p_main_party"),
         (party_get_num_prisoners, ":num_prisoners", "p_main_party"),
         (val_add, ":num_men", ":num_prisoners"),
         (val_mul, ":num_men", 2),
         (val_div, ":num_men", 3),
         (store_add, ":get_caught_chance", ":player_alarm", ":num_men"),
         (store_random_in_range, ":random_chance", 0, 100),
         (try_begin),
           (this_or_next|ge, ":random_chance", ":get_caught_chance"),
           (eq, "$g_last_defeated_bandits_town", "$g_encountered_party"),
           (assign, "$g_last_defeated_bandits_town", 0),
           (assign, "$sneaked_into_town",1),
           (assign, "$town_entered", 1),
           (jump_to_menu,"mnu_sneak_into_town_suceeded"),
         (else_try),
           (jump_to_menu,"mnu_sneak_into_town_caught"),
         (try_end)
         ]),
      ("start_siege",
       [
           (this_or_next|party_slot_eq, "$g_encountered_party", slot_center_is_besieged_by, -1),
           (             party_slot_eq, "$g_encountered_party", slot_center_is_besieged_by, "p_main_party"),
           (store_relation, ":reln", "$g_encountered_party_faction", "fac_player_supporters_faction"),
           (lt, ":reln", 0),
           (lt, "$g_encountered_party_2", 1),
           (call_script, "script_party_count_fit_for_battle","p_main_party"),
           (gt, reg(0), 5),
           (try_begin),
             (party_slot_eq, "$g_encountered_party", slot_party_type, spt_mainplanet),
             (assign, reg6, 1),
           (else_try),
             (assign, reg6, 0),
           (try_end),
           ],
       "Besiege the {reg6?planet:station}.",
       [
         (assign,"$g_player_besiege_town","$g_encountered_party"),
         (store_relation, ":relation", "fac_player_supporters_faction", "$g_encountered_party_faction"),
         (val_min, ":relation", -40),
         (call_script, "script_set_player_relation_with_faction", "$g_encountered_party_faction", ":relation"),
         (call_script, "script_update_all_notes"),
         (jump_to_menu, "mnu_spacestation_besiege"),
         ]),

      ("cheat_start_siege",
       [
         (eq, "$cheat_mode", 1),
         (this_or_next|party_slot_eq, "$g_encountered_party", slot_center_is_besieged_by, -1),
         (             party_slot_eq, "$g_encountered_party", slot_center_is_besieged_by, "p_main_party"),
         (store_relation, ":reln", "$g_encountered_party_faction", "fac_player_supporters_faction"),
         (ge, ":reln", 0),
         (lt, "$g_encountered_party_2", 1),
         (call_script, "script_party_count_fit_for_battle","p_main_party"),
         (gt, reg(0), 1),
         (try_begin),
           (party_slot_eq, "$g_encountered_party", slot_party_type, spt_mainplanet),
           (assign, reg6, 1),
         (else_try),
           (assign, reg6, 0),
         (try_end),
           ],
       "CHEAT: Besiege the {reg6?planet:station}...",
       [
           (assign,"$g_player_besiege_town","$g_encountered_party"),
           (jump_to_menu, "mnu_spacestation_besiege"),
           ]),

      ("leave_dot",[],"Leave.",[(change_screen_return,0)]),
      ("spacestation_cheat_interior",[(eq, "$cheat_mode", 1)], "CHEAT! Interior.",[(set_jump_mission,"mt_ai_training"),
                                                       (party_get_slot, ":spacestation_scene", "$current_town", slot_mainplanet_castle),
                                                       (jump_to_scene,":spacestation_scene"),
                                                       (change_screen_mission)]),
      ("spacestation_cheat_exterior",[(eq, "$cheat_mode", 1)], "CHEAT! Exterior.",[
#                                                       (set_jump_mission,"mt_town_default"),
                                                       (set_jump_mission,"mt_ai_training"),
                                                       (party_get_slot, ":spacestation_scene", "$current_town", slot_spacestation_exterior),
                                                       (jump_to_scene,":spacestation_scene"),
                                                       (change_screen_mission)]),
      ("spacestation_cheat_town_walls",[(eq, "$cheat_mode", 1),(party_slot_eq,"$current_town",slot_party_type, spt_mainplanet),], "CHEAT! Town Walls.",
       [
         (party_get_slot, ":scene", "$current_town", slot_mainplanet_walls),
         (set_jump_mission,"mt_ai_training"),
         (jump_to_scene,":scene"),
         (change_screen_mission)]),

    ]
  ),
   (
    "spacestation_guard",menu_text_color(0xFF000d2c),
    "You approach the landing bay. The guards on the observation posts watch you closely.",
    "none",
    [
	
		#SW - display a new menu background
		(call_script, "script_display_fullscreen_background", "$current_town"),	

    ],
    [
      ("request_shelter",[(party_slot_eq, "$g_encountered_party",slot_party_type, spt_castle),
                          (ge, "$g_encountered_party_relation", 0)],
       #SW - modified dialog
	   "Request entry to the site.",
       [(party_get_slot, ":spacestation_lord", "$g_encountered_party", slot_mainplanet_lord),
        (try_begin),
          (lt, ":spacestation_lord", 0),
          (jump_to_menu, "mnu_spacestation_entry_granted"),
        (else_try),
          (call_script, "script_troop_get_player_relation", ":spacestation_lord"),
          (assign, ":spacestation_lord_relation", reg0),
          #(troop_get_slot, ":spacestation_lord_relation", ":spacestation_lord", slot_troop_player_relation),
          (try_begin),
            (gt, ":spacestation_lord_relation", -15),
            (jump_to_menu, "mnu_spacestation_entry_granted"),
          (else_try),
            (jump_to_menu, "mnu_spacestation_entry_denied"),
          (try_end),
        (try_end),
       ]),
      ("request_meeting_commander",[],
       "Request a meeting with someone.",
       [
          (jump_to_menu, "mnu_spacestation_meeting"),
       ]),
      ("leave_dot",[],
       "Leave.",
       [(change_screen_return,0)]),
    ]
  ),
  (
    "spacestation_entry_granted",menu_text_color(0xFF000d2c),
    "After a brief wait, the guards lower the shields for you and allow your party to land.",
    "none",
    [
	
		#SW - display a new menu background
		(call_script, "script_display_fullscreen_background", "$current_town"),	
	
    ],
    [
      ("continue_3dot",[],
       "Continue...",
       [(jump_to_menu,"mnu_town")]),
    ]
  ),
  (
    "spacestation_entry_denied",menu_text_color(0xFF000d2c),
    "The lord of this planet has forbidden you from landing on the surface,\
 and the guard sergeant informs you that his troops will fire if you attempt to come any closer.",
    "none",
    [
		#SW - display a new menu background
		(call_script, "script_display_fullscreen_background", "$current_town"),	
    ],
    [
      ("continue_3dot",[],
       "Continue...",
       [(jump_to_menu,"mnu_spacestation_guard")]),
    ]
  ),
  (
    "spacestation_meeting",menu_text_color(0xFF000d2c),
    "With whom do you want to meet?",
    "none",
    [
		#SW - display a new menu background
		(call_script, "script_display_fullscreen_background", "$current_town"),	
	
        (assign, "$num_spacestation_meeting_troops", 0),
        (try_for_range, ":troop_no", faction_heroes_begin, faction_heroes_end),
          (troop_slot_eq, ":troop_no", slot_troop_occupation, slto_faction_hero),
          (call_script, "script_get_troop_attached_party", ":troop_no"),
          (eq, "$g_encountered_party", reg0),
          (troop_set_slot, "trp_temp_array_a", "$num_spacestation_meeting_troops", ":troop_no"),
          (val_add, "$num_spacestation_meeting_troops", 1),
        (try_end),
    ],
    [
      ("guard_meet_s5",[(gt, "$num_spacestation_meeting_troops", 0),(troop_get_slot, ":troop_no", "trp_temp_array_a", 0),(str_store_troop_name, s5, ":troop_no")],
       "{s5}.",[(troop_get_slot, "$spacestation_meeting_selected_troop", "trp_temp_array_a", 0),(jump_to_menu,"mnu_spacestation_meeting_selected")]),
      ("guard_meet_s5",[(gt, "$num_spacestation_meeting_troops", 1),(troop_get_slot, ":troop_no", "trp_temp_array_a", 1),(str_store_troop_name, s5, ":troop_no")],
       "{s5}.",[(troop_get_slot, "$spacestation_meeting_selected_troop", "trp_temp_array_a", 1),(jump_to_menu,"mnu_spacestation_meeting_selected")]),
      ("guard_meet_s5",[(gt, "$num_spacestation_meeting_troops", 2),(troop_get_slot, ":troop_no", "trp_temp_array_a", 2),(str_store_troop_name, s5, ":troop_no")],
       "{s5}.",[(troop_get_slot, "$spacestation_meeting_selected_troop", "trp_temp_array_a", 2),(jump_to_menu,"mnu_spacestation_meeting_selected")]),
      ("guard_meet_s5",[(gt, "$num_spacestation_meeting_troops", 3),(troop_get_slot, ":troop_no", "trp_temp_array_a", 3),(str_store_troop_name, s5, ":troop_no")],
       "{s5}.",[(troop_get_slot, "$spacestation_meeting_selected_troop", "trp_temp_array_a", 3),(jump_to_menu,"mnu_spacestation_meeting_selected")]),
      
      ("forget_it",[],
       "Forget it.",
       [(jump_to_menu,"mnu_spacestation_guard")]),
    ]
  ),
  (
    "spacestation_meeting_selected",menu_text_color(0xFF000d2c),
    #"Your request for a meeting is relayed inside, and finally {s6} appears in the courtyard to speak with you.",
	"Your request is relayed as the comm officer communicates with his superior. Finally, their ghostly hologram appears.",
    "none",
    [
		#SW - display a new menu background
		(call_script, "script_display_fullscreen_background", "$current_town"),	
	
		(str_store_troop_name, s6, "$spacestation_meeting_selected_troop")
	],
    [
      ("continue_3dot",[],
       "Continue...",
       [(jump_to_menu, "mnu_spacestation_outside"),
        (modify_visitors_at_site,"scn_conversation_scene"),(reset_visitors),
        (set_visitor,0,"trp_player"),
        (set_visitor,17,"$spacestation_meeting_selected_troop"),
        (set_jump_mission,"mt_conversation_encounter"),
        (jump_to_scene,"scn_conversation_scene"),
        (assign, "$talk_context", tc_spacestation_gate),
        (change_screen_map_conversation, "$spacestation_meeting_selected_troop"),
        ]),
    ]
  ),


   (
    "spacestation_besiege",menu_text_color(0xFF000d2c)|mnf_enable_hot_keys|mnf_scale_picture,
    "You are laying siege to {s1}. {s2} {s3}",
    "none",
    [

		#SW - display a new menu background
		(call_script, "script_display_fullscreen_background", "$current_town"),	
	
############################################################################################################
##### Custom Commander(CC)
############################################################################################################
       #(troop_get_type, ":is_female", "trp_player"),
       (troop_get_type, ":is_female", "$g_player_troop"),
############################################################################################################
##### Custom Commander(CC)
############################################################################################################
        (try_begin),
          (eq, ":is_female", 1),
          (set_background_mesh, "mesh_pic_siege_sighted_fem"),
        (else_try),
          (set_background_mesh, "mesh_pic_siege_sighted"),
        (try_end),
        (assign, "$g_siege_force_wait", 0),
        (try_begin),
          (party_slot_eq, "$g_encountered_party", slot_center_is_besieged_by, -1),
          (party_set_slot, "$g_encountered_party", slot_center_is_besieged_by, "p_main_party"),
          (store_current_hours, ":cur_hours"),
          (party_set_slot, "$g_encountered_party", slot_center_siege_begin_hours, ":cur_hours"),
          (assign, "$g_siege_method", 0),
          (assign, "$g_siege_sallied_out_once", 0),
        (try_end),

        (party_get_slot, ":town_food_store", "$g_encountered_party", slot_party_food_store),
        (call_script, "script_center_get_food_consumption", "$g_encountered_party"),
        (assign, ":food_consumption", reg0),
        (assign, reg7, ":food_consumption"),
        (assign, reg8, ":town_food_store"),
        (store_div, reg3, ":town_food_store", ":food_consumption"),

        (try_begin),
          (party_slot_eq, "$g_encountered_party", slot_party_type, spt_mainplanet),
          (assign, reg6, 1),
        (else_try),
          (assign, reg6, 0),
        (try_end),
        
        (try_begin),
          (gt, reg3, 0),
          (str_store_string, s2, "@The {reg6?planet's:station's} food stores should last for {reg3} more days."),
        (else_try),
          (str_store_string, s2, "@The {reg6?planet's:station's} food stores have run out and the defenders are starving."),
        (try_end),

        (str_store_string, s3, "str_empty_string"),
        (try_begin),
          (ge, "$g_siege_method", 1),
          (store_current_hours, ":cur_hours"),
          (try_begin),
            (lt, ":cur_hours",  "$g_siege_method_finish_hours"),
            (store_sub, reg9, "$g_siege_method_finish_hours", ":cur_hours"),
            (try_begin),
              (eq, "$g_siege_method", 1),
              (str_store_string, s3, "@You're preparing to attack, the work should finish in {reg9} hours."),
            (else_try),
              (eq, "$g_siege_method", 2),
              (str_store_string, s3, "@Your forces are building a siege tower. They estimate another {reg9} hours to complete the build."),
            (try_end),
          (else_try),
            (try_begin),
              (eq, "$g_siege_method", 1),
              #(str_store_string, s3, "@You are ready to attack the walls at any time."),
			  (str_store_string, s3, "@The shields have been destroyed and you are ready to begin the attack at any time."),
            (else_try),
              (eq, "$g_siege_method", 2),
              (str_store_string, s3, "@The siege tower is built and ready to make an assault."),
            (try_end),
          (try_end),
        (try_end),
        
        #Check if enemy leaves the castle to us...
        (try_begin),
          (eq, "$g_spacestation_left_to_player",1), #we come here after dialog. Empty the castle and send parties away.
          (assign, "$g_spacestation_left_to_player",0),
          (store_faction_of_party, ":spacestation_faction", "$g_encountered_party"),
          (party_set_faction,"$g_encountered_party","fac_neutral"), #temporarily erase faction so that it is not the closest town
          (party_get_num_attached_parties, ":num_attached_parties_to_castle","$g_encountered_party"),
          (try_for_range_backwards, ":iap", 0, ":num_attached_parties_to_castle"),
            (party_get_attached_party_with_rank, ":attached_party", "$g_encountered_party", ":iap"),
            (party_detach, ":attached_party"),
            (party_get_slot, ":attached_party_type", ":attached_party", slot_party_type),
            (eq, ":attached_party_type", spt_faction_hero_party),
            (store_faction_of_party, ":attached_party_faction", ":attached_party"),
            (call_script, "script_get_closest_walled_center_of_faction", ":attached_party", ":attached_party_faction"),
            (try_begin),
              (gt, reg0, 0),
              (call_script, "script_party_set_ai_state", ":attached_party", spai_holding_center, reg0),
            (else_try),
              (call_script, "script_party_set_ai_state", ":attached_party", spai_patrolling_around_center, "$g_encountered_party"),
            (try_end),
          (try_end),
          (call_script, "script_party_remove_all_companions", "$g_encountered_party"),
          (change_screen_return),
          (party_collect_attachments_to_party, "$g_encountered_party", "p_collective_enemy"), #recalculate so that
          (call_script, "script_party_copy", "p_encountered_party_backup", "p_collective_enemy"), #leaving troops will not be considered as captured
          (party_set_faction,"$g_encountered_party",":spacestation_faction"), 
        (try_end),

        #Check for victory or defeat....
        (assign, "$g_enemy_party", "$g_encountered_party"),
        (assign, "$g_ally_party", -1),
        (str_store_party_name, 1,"$g_encountered_party"),
        (call_script, "script_encounter_calculate_fit"),
        
        (assign, reg11, "$g_enemy_fit_for_battle"),
        (assign, reg10, "$g_friend_fit_for_battle"),


        (try_begin),
          (eq, "$g_leave_encounter",1),
          (change_screen_return),
        (else_try),
          (call_script, "script_party_count_fit_regulars","p_collective_enemy"),
          (assign, ":enemy_finished", 0),
          (try_begin),
            (eq, "$g_battle_result", 1),
            (assign, ":enemy_finished", 1),
          (else_try),
            (le, "$g_enemy_fit_for_battle", 0),
            (ge, "$g_friend_fit_for_battle", 1),
            (assign, ":enemy_finished", 1),
          (try_end),
          (this_or_next|eq, ":enemy_finished", 1),
          (eq, "$g_enemy_surrenders", 1),
          (assign, "$g_next_menu", "mnu_spacestation_taken"),
          (jump_to_menu, "mnu_total_victory"),
        (else_try),
          (call_script, "script_party_count_members_with_full_health", "p_main_party"),
          (assign, ":main_party_fit_regulars", reg(0)),
          (eq, "$g_battle_result", -1),
          (eq, ":main_party_fit_regulars", 0), #all lost
          (assign, "$g_next_menu", "mnu_captivity_start_spacestation_defeat"),
          (jump_to_menu, "mnu_total_defeat"),
        (try_end),
    ],
    [
      ("siege_request_meeting",[(eq, "$cant_talk_to_enemy", 0)],"Call for a meeting with the commander.", [
          (assign, "$cant_talk_to_enemy", 1),
          (assign, "$g_enemy_surrenders",0),
          (assign, "$g_spacestation_left_to_player",0),
          (assign, "$talk_context", tc_spacestation_commander),
          (party_get_num_attached_parties, ":num_attached_parties_to_castle","$g_encountered_party"),
          (try_begin),
            (gt, ":num_attached_parties_to_castle", 0),
            (party_get_attached_party_with_rank, ":leader_attached_party", "$g_encountered_party", 0),
            (call_script, "script_setup_party_meeting", ":leader_attached_party"),
          (else_try),
            (call_script, "script_setup_party_meeting", "$g_encountered_party"),
          (try_end),
           ]),
        
      ("wait_24_hours",[],"Wait until tomorrow.", [
          (assign,"$auto_besiege_town","$g_encountered_party"),
          (assign, "$g_siege_force_wait", 1),
          (store_time_of_day,":cur_time_of_day"),
          (val_add, ":cur_time_of_day", 1),
          (assign, ":time_to_wait", 31),
          (val_sub,":time_to_wait",":cur_time_of_day"),
          (val_mod,":time_to_wait",24),
          (val_add, ":time_to_wait", 1),
          (rest_for_hours_interactive, ":time_to_wait", 5, 1), #rest while attackable
          (assign, "$cant_talk_to_enemy", 0),
          (change_screen_return),
          ]),

############################################################################################################
##### Custom Commander(CC)
############################################################################################################
    
      ("commander_change",
        [
          (ge, "$g_siege_method", 1),
          (store_current_hours, ":cur_hours"),
          (ge, ":cur_hours", "$g_siege_method_finish_hours"),
          (str_store_troop_name,s7,"$g_player_troop"),
        ],
        "Change the commander. (Current:{s7})",
        [
          (assign, "$g_next_menu", "mnu_spacestation_besiege"),
          (assign, "$change_commander_menu_offset", 0),
          (jump_to_menu, "mnu_change_commander"),
        ]),

############################################################################################################
##### Custom Commander(CC)
############################################################################################################
		  
      ("spacestation_lead_attack",
       [
############################################################################################################
##### Custom Commander(CC)
############################################################################################################
          #(neg|troop_is_wounded, "trp_player"),
          (neg|troop_is_wounded, "$g_player_troop"),
############################################################################################################
##### Custom Commander(CC)
############################################################################################################
         (ge, "$g_siege_method", 1),
         (gt, "$g_friend_fit_for_battle", 3),
         (store_current_hours, ":cur_hours"),
         (ge, ":cur_hours", "$g_siege_method_finish_hours"),
         ],
       "Lead your soldiers in an assault.", [
           (try_begin),
             (party_slot_eq, "$g_encountered_party", slot_party_type, spt_mainplanet),
             (party_get_slot, ":battle_scene", "$g_encountered_party", slot_mainplanet_walls),
           (else_try),
             (party_get_slot, ":battle_scene", "$g_encountered_party", slot_spacestation_exterior),
           (try_end),
           (call_script, "script_calculate_battle_advantage"),
           (assign, ":battle_advantage", reg0),
           (val_mul, ":battle_advantage", 2),
           (val_div, ":battle_advantage", 3), #scale down the advantage a bit in sieges.
           (set_battle_advantage, ":battle_advantage"),
           (set_party_battle_mode),
           (assign, "$g_siege_battle_state", 1),
           (assign, ":siege_sally", 0),
           (try_begin),
             (le, ":battle_advantage", -4), #we are outnumbered, defenders sally out
             (eq, "$g_siege_sallied_out_once", 0),
             (set_jump_mission,"mt_spacestation_attack_walls_defenders_sally"),
             (assign, "$g_siege_battle_state", 0),
             (assign, ":siege_sally", 1),
           (else_try),
             (party_slot_eq, "$current_town", slot_center_siege_with_belfry, 1),
             (set_jump_mission,"mt_spacestation_attack_walls_belfry"),
           (else_try),
             (set_jump_mission,"mt_spacestation_attack_walls_ladder"),
           (try_end),
           (assign, "$cant_talk_to_enemy", 0),           
           (assign, "$g_siege_final_menu", "mnu_spacestation_besiege"),
           (assign, "$g_next_menu", "mnu_spacestation_besiege_inner_battle"),
           (assign, "$g_siege_method", 0), #reset siege timer
           (jump_to_scene,":battle_scene"),
           (try_begin),
             (eq, ":siege_sally", 1),
             (jump_to_menu, "mnu_siege_attack_meets_sally"),
           (else_try),
#           (jump_to_menu,"mnu_spacestation_outside"),
##           (assign, "$g_next_menu", "mnu_spacestation_besiege"),
             (jump_to_menu, "mnu_battle_debrief"),
             (change_screen_mission),
           (try_end),
       ]),
      ("attack_stay_back",
       [
         (ge, "$g_siege_method", 1),
         (gt, "$g_friend_fit_for_battle", 3),
         (store_current_hours, ":cur_hours"),
         (ge, ":cur_hours",  "$g_siege_method_finish_hours"),
         ],
       "Order your soldiers to attack while you stay back...", [(assign, "$cant_talk_to_enemy", 0),(jump_to_menu,"mnu_spacestation_attack_walls_simulate")]),

      ("build_ladders",[(party_slot_eq, "$current_town", slot_center_siege_with_belfry, 0),(eq, "$g_siege_method", 0)],
       #SW - modified menu name
	   #"Prepare ladders to attack the walls.", [(jump_to_menu,"mnu_construct_ladders")]),
	   "Assault the Shields.", [(jump_to_menu,"mnu_construct_ladders")]),

      ("build_siege_tower",[(party_slot_eq, "$current_town", slot_center_siege_with_belfry, 1),(eq, "$g_siege_method", 0)],
       "Build a siege tower.", [(jump_to_menu,"mnu_construct_siege_tower")]),

      ("cheat_spacestation_lead_attack",[(eq, "$cheat_mode", 1),
                                   (eq, "$g_siege_method", 0)],
       "CHEAT: Instant build equipments.",
       [
         (assign, "$g_siege_method", 1),
         (assign, "$g_siege_method_finish_hours", 0),
         (jump_to_menu, "mnu_spacestation_besiege"),
       ]),

      
      ("lift_siege",[],"Abandon the siege.",
       [
         (call_script, "script_lift_siege", "$g_player_besiege_town", 0),
         (assign,"$g_player_besiege_town", -1),
         (change_screen_return)]),
    ]
  ),
  
  (
    "siege_attack_meets_sally",menu_text_color(0xFF000d2c),
    "The defenders sally out to meet your assault.",
    "none",
    [
    ],
    [
      ("continue_3dot",[],
       "Continue...",
       [
             (jump_to_menu, "mnu_battle_debrief"),
             (change_screen_mission),
       ]),
    ]
  ),

   (
    "spacestation_besiege_inner_battle",menu_text_color(0xFF000d2c)|mnf_scale_picture,
    "{s1}",
    "none",
    [
############################################################################################################
##### Custom Commander(CC)
############################################################################################################
       #(troop_get_type, ":is_female", "trp_player"),
       (troop_get_type, ":is_female", "$g_player_troop"),
############################################################################################################
##### Custom Commander(CC)
############################################################################################################
        (try_begin),
          (eq, ":is_female", 1),
          (set_background_mesh, "mesh_pic_siege_sighted_fem"),
        (else_try),
          (set_background_mesh, "mesh_pic_siege_sighted"),
        (try_end),
        (assign, ":result", "$g_battle_result"),#will be reset at script_encounter_calculate_fit
        (call_script, "script_encounter_calculate_fit"),
        
# TODO: To use for the future:
            (str_store_string, s1, "@As a last defensive effort, you retreat to the main hall of the keep.\
 You and your remaining soldiers will put up a desperate fight here. If you are defeated, there's no other place to fall back to."),
            (str_store_string, s1, "@You've been driven away from the walls.\
 Now the attackers are pouring into the streets. IF you can defeat them, you can perhaps turn the tide and save the day."),
        (try_begin),
          (this_or_next|neq, ":result", 1),
          (this_or_next|le, "$g_friend_fit_for_battle", 0),
          (le, "$g_enemy_fit_for_battle", 0),
          (jump_to_menu, "$g_siege_final_menu"),
        (else_try),
          (call_script, "script_encounter_calculate_fit"),
          (party_slot_eq, "$g_encountered_party", slot_party_type, spt_mainplanet),
          (try_begin),
            (eq, "$g_siege_battle_state", 0),
            (eq, ":result", 1),
            (assign, "$g_battle_result", 0),
            (jump_to_menu, "$g_siege_final_menu"),
          (else_try),
            (eq, "$g_siege_battle_state", 1),
            (eq, ":result", 1),
            (str_store_string, s1, "@You've breached the planet shields,\
 but the stubborn defenders continue to resist you on the ground!\
 You'll have to deal with them before you can attack the main hall at the heart of the planet."),
          (else_try),
            (eq, "$g_siege_battle_state", 2),
            (eq, ":result", 1),
            (str_store_string, s1, "@The planet is yours,\
 but the remaining defenders have retreated to the main hall.\
 It must fall before you can complete your victory."),
          (else_try),
            (jump_to_menu, "$g_siege_final_menu"),
          (try_end),
        (else_try),
          (try_begin),
            (eq, "$g_siege_battle_state", 0),
            (eq, ":result", 1),
            (assign, "$g_battle_result", 0),
            (jump_to_menu, "$g_siege_final_menu"),
          (else_try),
            (eq, "$g_siege_battle_state", 1),
            (eq, ":result", 1),
            (str_store_string, s1, "@The remaining defenders have retreated to the main hall as a last defense. You must go in and crush any remaining resistance."),
          (else_try),
            (jump_to_menu, "$g_siege_final_menu"),
          (try_end),
        (try_end),
    ],
    [
      ("continue_3dot",[],
       "Continue...",
       [
           (try_begin),
             (party_slot_eq, "$g_encountered_party", slot_party_type, spt_mainplanet),
             (try_begin),
               (eq, "$g_siege_battle_state", 1),
               (party_get_slot, ":battle_scene", "$g_encountered_party", slot_mainplanet_center),
               (set_jump_mission, "mt_besiege_inner_battle_town_center"),
             (else_try),
               (party_get_slot, ":battle_scene", "$g_encountered_party", slot_mainplanet_castle),
               (set_jump_mission, "mt_besiege_inner_battle_castle"),
             (try_end),
           (else_try),
             (party_get_slot, ":battle_scene", "$g_encountered_party", slot_mainplanet_castle),
             (set_jump_mission, "mt_besiege_inner_battle_castle"),
           (try_end),
##           (call_script, "script_calculate_battle_advantage"),
##           (set_battle_advantage, reg0),
           (set_party_battle_mode),
           (jump_to_scene, ":battle_scene"),
           (val_add, "$g_siege_battle_state", 1),
           (assign, "$g_next_menu", "mnu_spacestation_besiege_inner_battle"),
           (jump_to_menu, "mnu_battle_debrief"),
           (change_screen_mission),
       ]),
    ]
  ),

  
  (
    "construct_ladders",menu_text_color(0xFF000d2c),
	#SW - modified game menu
    #"As the party member with the highest Engineer skill ({reg2}), {reg3?you estimate:{s3} estimates} that it will take\
 #{reg4} hours to build enough scaling ladders for the assault.",
    "As the party member with the highest Engineer skill ({reg2}), {reg3?you estimate:{s3} estimates} that it will take\
 {reg4} hours to destroy the shields so the assault can begin.", 
    "none",
    [(call_script, "script_get_max_skill_of_player_party", "skl_engineer"),
     (assign, ":max_skill", reg0),
     (assign, ":max_skill_owner", reg1),
     (assign, reg2, ":max_skill"),

     (store_sub, reg4, 14, ":max_skill"),
     (val_mul, reg4, 2),
     (val_div, reg4, 3),
     
     (try_begin),
       (eq, ":max_skill_owner", "trp_player"),
       (assign, reg3, 1),
     (else_try),
       (assign, reg3, 0),
       (str_store_troop_name, s3, ":max_skill_owner"),
     (try_end),
    ],
    [
      ("build_ladders_cont",[],
       #"Do it.", [
	   "Begin the Assault.", [
           (assign, "$g_siege_method", 1),
           (store_current_hours, ":cur_hours"),
           (call_script, "script_get_max_skill_of_player_party", "skl_engineer"),
           (store_sub, ":hours_takes", 14, reg0),
           (val_mul, ":hours_takes", 2),
           (val_div, ":hours_takes", 3),
           (store_add, "$g_siege_method_finish_hours",":cur_hours", ":hours_takes"),
           (assign,"$auto_besiege_town","$current_town"),
           (rest_for_hours_interactive, 96, 5, 1), #rest while attackable. A trigger will divert control when attack is ready.
           (change_screen_return),
           ]),
      ("go_back_dot",[],
       "Go back.", [(jump_to_menu,"mnu_spacestation_besiege")]),
        ],
  ),

  
  (
    "construct_siege_tower",menu_text_color(0xFF000d2c),
    "As the party member with the highest Engineer skill ({reg2}), {reg3?you estimate:{s3} estimates} that building a siege tower will take\
 {reg4} hours.",
    "none",
    [(call_script, "script_get_max_skill_of_player_party", "skl_engineer"),
     (assign, ":max_skill", reg0),
     (assign, ":max_skill_owner", reg1),
     (assign, reg2, ":max_skill"),

     (store_sub, reg4, 15, ":max_skill"),
     (val_mul, reg4, 6),
     
     (try_begin),
       (eq, ":max_skill_owner", "trp_player"),
       (assign, reg3, 1),
     (else_try),
       (assign, reg3, 0),
       (str_store_troop_name, s3, ":max_skill_owner"),
     (try_end),
    ],
    [
      ("build_siege_tower_cont",[],
       "Start building.", [
           (assign, "$g_siege_method", 2),
           (store_current_hours, ":cur_hours"),
           (call_script, "script_get_max_skill_of_player_party", "skl_engineer"),
           (store_sub, ":hours_takes", 15, reg0),
           (val_mul, ":hours_takes", 6),
           (store_add, "$g_siege_method_finish_hours",":cur_hours", ":hours_takes"),
           (assign,"$auto_besiege_town","$current_town"),
           (rest_for_hours_interactive, 240, 5, 1), #rest while attackable. A trigger will divert control when attack is ready.
           (change_screen_return),
           ]),
      ("go_back_dot",[],
       "Go back.", [(jump_to_menu,"mnu_spacestation_besiege")]),
        ],
  ),

   (
    "spacestation_attack_walls_simulate",menu_text_color(0xFF000d2c)|mnf_scale_picture|mnf_disable_all_keys,
    "{s4}^^Your casualties:{s8}^^Enemy casualties were: {s9}",
    "none",
    [
############################################################################################################
##### Custom Commander(CC)
############################################################################################################
       #(troop_get_type, ":is_female", "trp_player"),
       (troop_get_type, ":is_female", "$g_player_troop"),
############################################################################################################
##### Custom Commander(CC)
############################################################################################################
        (try_begin),
          (eq, ":is_female", 1),
          (set_background_mesh, "mesh_pic_siege_sighted_fem"),
        (else_try),
          (set_background_mesh, "mesh_pic_siege_sighted"),
        (try_end),
        
        (call_script, "script_party_calculate_strength", "p_main_party", 1), #skip player
        (assign, ":player_party_strength", reg0),
        (val_div, ":player_party_strength", 10),

        (call_script, "script_party_calculate_strength", "$g_encountered_party", 0),
        (assign, ":enemy_party_strength", reg0),
        (val_div, ":enemy_party_strength", 4),

        (inflict_casualties_to_party_group, "p_main_party", ":enemy_party_strength", "p_temp_casualties"),
        (call_script, "script_print_casualties_to_s0", "p_temp_casualties", 0),
        (str_store_string_reg, s8, s0),

        (inflict_casualties_to_party_group, "$g_encountered_party", ":player_party_strength", "p_temp_casualties"),
        (call_script, "script_print_casualties_to_s0", "p_temp_casualties", 0),
        (str_store_string_reg, s9, s0),

        (assign, "$no_soldiers_left", 0),
        (try_begin),
          (call_script, "script_party_count_members_with_full_health","p_main_party"),
          (le, reg(0), 0),
          (assign, "$no_soldiers_left", 1),
          (str_store_string, s4, "str_attack_walls_failure"),
        (else_try),
          (call_script, "script_party_count_members_with_full_health","$g_encountered_party"),
          (le, reg(0), 0),
          (assign, "$no_soldiers_left", 1),
          (assign, "$g_battle_result", 1),
          (str_store_string, s4, "str_attack_walls_success"),
        (else_try),
          (str_store_string, s4, "str_attack_walls_continue"),
        (try_end),
     ],
    [
##      ("lead_next_wave",[(eq, "$no_soldiers_left", 0)],"Lead the next wave of attack personally.", [
##           (party_get_slot, ":battle_scene", "$g_encountered_party", slot_spacestation_exterior),
##           (set_party_battle_mode),
##           (set_jump_mission,"mt_spacestation_attack_walls"),
##           (jump_to_scene,":battle_scene"),
##           (jump_to_menu,"mnu_spacestation_outside"),
##           (change_screen_mission),
##       ]),
##      ("continue_attacking",[(eq, "$no_soldiers_left", 0)],"Order your soldiers to keep attacking...", [
##                                    (jump_to_menu,"mnu_spacestation_attack_walls_3"),
##                                    ]),
##      ("call_soldiers_back",[(eq, "$no_soldiers_left", 0)],"Call your soldiers back.",[(jump_to_menu,"mnu_spacestation_outside")]),
      ("continue_3dot",[],"Continue...",[(jump_to_menu,"mnu_spacestation_besiege")]),
    ]
  ),
  
   (
    "spacestation_attack_walls_with_allies_simulate",menu_text_color(0xFF000d2c)|mnf_scale_picture|mnf_disable_all_keys,
    "{s4}^^Your casualties: {s8}^^Allies' casualties: {s9}^^Enemy casualties: {s10}",
    "none",
    [
############################################################################################################
##### Custom Commander(CC)
############################################################################################################
       #(troop_get_type, ":is_female", "trp_player"),
       (troop_get_type, ":is_female", "$g_player_troop"),
############################################################################################################
##### Custom Commander(CC)
############################################################################################################
        (try_begin),
          (eq, ":is_female", 1),
          (set_background_mesh, "mesh_pic_siege_sighted_fem"),
        (else_try),
          (set_background_mesh, "mesh_pic_siege_sighted"),
        (try_end),

        (call_script, "script_party_calculate_strength", "p_main_party", 1), #skip player
        (assign, ":player_party_strength", reg0),
        (val_div, ":player_party_strength", 10),
        (call_script, "script_party_calculate_strength", "p_collective_friends", 0),
        (assign, ":friend_party_strength", reg0),
        (val_div, ":friend_party_strength", 10),

        (val_max, ":friend_party_strength", 1),

        (call_script, "script_party_calculate_strength", "p_collective_enemy", 0),
        (assign, ":enemy_party_strength", reg0),
        (val_div, ":enemy_party_strength", 4),

##        (assign, reg0, ":player_party_strength"),
##        (assign, reg1, ":friend_party_strength"),
##        (assign, reg2, ":enemy_party_strength"),
##        (assign, reg3, "$g_enemy_party"),
##        (assign, reg4, "$g_ally_party"),
##        (display_message, "@player_str={reg0} friend_str={reg1} enemy_str={reg2}"),
##        (display_message, "@enemy_party={reg3} ally_party={reg4}"),

        (assign, ":enemy_party_strength_for_p", ":enemy_party_strength"),
        (val_mul, ":enemy_party_strength_for_p", ":player_party_strength"),
        (val_div, ":enemy_party_strength_for_p", ":friend_party_strength"),
        (val_sub, ":enemy_party_strength", ":enemy_party_strength_for_p"),

        (inflict_casualties_to_party_group, "p_main_party", ":enemy_party_strength_for_p", "p_temp_casualties"),
        (call_script, "script_print_casualties_to_s0", "p_temp_casualties", 0),
        (str_store_string_reg, s8, s0),
                                    
        (inflict_casualties_to_party_group, "$g_enemy_party", ":friend_party_strength", "p_temp_casualties"),
        (call_script, "script_print_casualties_to_s0", "p_temp_casualties", 0),
        (str_store_string_reg, s10, s0),

        (call_script, "script_collect_friendly_parties"),

        (inflict_casualties_to_party_group, "$g_ally_party", ":enemy_party_strength", "p_temp_casualties"),
        (call_script, "script_print_casualties_to_s0", "p_temp_casualties", 0),
        (str_store_string_reg, s9, s0),

        (party_collect_attachments_to_party, "$g_enemy_party", "p_collective_enemy"),

        (assign, "$no_soldiers_left", 0),
        (try_begin),
          (call_script, "script_party_count_members_with_full_health", "p_main_party"),
          (le, reg0, 0),
          (assign, "$no_soldiers_left", 1),
          (str_store_string, s4, "str_attack_walls_failure"),
        (else_try),
          (call_script, "script_party_count_members_with_full_health", "p_collective_enemy"),
          (le, reg0, 0),
          (assign, "$no_soldiers_left", 1),
          (assign, "$g_battle_result", 1),
          (str_store_string, s4, "str_attack_walls_success"),
        (else_try),
          (str_store_string, s4, "str_attack_walls_continue"),
        (try_end),
     ],
    [
      ("continue_3dot",[],"Continue...",[(jump_to_menu,"mnu_besiegers_camp_with_allies")]),
    ]
  ),

  (
    "spacestation_taken_by_friends",menu_text_color(0xFF000d2c),
    "Nothing to see here.",
    "none",
    [
        (party_clear, "$g_encountered_party"),
        (party_stack_get_troop_id, ":leader", "$g_encountered_party_2", 0),
        (party_set_slot, "$g_encountered_party", slot_center_last_taken_by_troop, ":leader"),
        (store_troop_faction, ":faction_no", ":leader"),
        #Reduce prosperity of the center by 5
        (call_script, "script_change_center_prosperity", "$g_encountered_party", -5),
        (call_script, "script_give_center_to_faction", "$g_encountered_party", ":faction_no"),
        (call_script, "script_add_log_entry", logent_player_participated_in_siege, "trp_player",  "$g_encountered_party", 0, "$g_encountered_party_faction"),
##        (call_script, "script_change_troop_renown", "trp_player", 1),
        (change_screen_return),
    ],
    [
    ],
  ),


  (
    "spacestation_taken",menu_text_color(0xFF000d2c)|mnf_disable_all_keys,
    "{s3} has fallen to your troops, and you now have full control of the {reg2?planet:station}.\
{reg1? It would seem that there is nothing stopping you from taking it for yourself...:}",# Only visible when castle is taken without being a vassal of a faction.
    "none",
    [
        (party_clear, "$g_encountered_party"),
        (call_script, "script_lift_siege", "$g_encountered_party", 0),
        (assign, "$g_player_besiege_town", -1),
        (call_script, "script_add_log_entry", logent_spacestation_captured_by_player, "trp_player",  "$g_encountered_party", 0, "$g_encountered_party_faction"),
        (party_set_slot, "$g_encountered_party", slot_center_last_taken_by_troop, "trp_player"),
        #Reduce prosperity of the center by 5
        (call_script, "script_change_center_prosperity", "$g_encountered_party", -5),
        (call_script, "script_change_troop_renown", "trp_player", 5),
        (call_script, "script_add_log_entry", logent_spacestation_captured_by_player, "trp_player", "$g_encountered_party", -1, "$g_encountered_party_faction"),
        (try_begin),
          (is_between, "$players_faction", factions_begin, factions_end),
          (neq, "$players_faction", "fac_player_supporters_faction"),
          (call_script, "script_give_center_to_faction", "$g_encountered_party", "$players_faction"),
          (call_script, "script_order_best_besieger_party_to_guard_center", "$g_encountered_party", "$players_faction"),
          (jump_to_menu, "mnu_spacestation_taken_2"),
        (else_try),
          (call_script, "script_give_center_to_faction", "$g_encountered_party", "fac_player_supporters_faction"),
          (call_script, "script_order_best_besieger_party_to_guard_center", "$g_encountered_party", "fac_player_supporters_faction"),
          (str_store_party_name, s3, "$g_encountered_party"),
          (assign, reg1, 0),
          (try_begin),
            (faction_slot_eq, "fac_player_supporters_faction", slot_faction_leader, "trp_player"),
            (assign, reg1, 1),
          (try_end),
        (try_end),
        (assign, reg2, 0),
        (try_begin),
          (is_between, "$g_encountered_party", mainplanets_begin, mainplanets_end),
          (assign, reg2, 1),
        (try_end),
    ],
    [
      ("continue_3dot",[],"Continue...",
       [
          (assign, "$auto_enter_town", "$g_encountered_party"),
          (change_screen_return),
        ]),
    ],
  ),
  (
    "spacestation_taken_2",menu_text_color(0xFF000d2c)|mnf_disable_all_keys,
    "{s3} has fallen to your troops, and you now have full control of the station.\
 It is time to send word to {s9} about your victory. {s5}",
    "none",
    [
        (str_store_party_name, s3, "$g_encountered_party"),
        (str_clear, s5),
        (faction_get_slot, ":faction_leader", "$players_faction", slot_faction_leader),
        (str_store_troop_name, s9, ":faction_leader"),
        (try_begin),
          (eq, "$player_has_homage", 0),
          (assign, reg8, 0),
          (try_begin),
            (party_slot_eq, "$g_encountered_party", spt_mainplanet),
            (assign, reg8, 1),
          (try_end),
          (str_store_string, s5, "@However, since you are not a sworn follower of {s9}, there is no chance he would recognize you as the {lord/lady} of this {reg8?planet:station}."),
        (try_end),
    ],
    [
      ("spacestation_taken_claim",[(eq, "$player_has_homage", 1)],"Request that {s3} be awarded to you.",
       [
        (party_set_slot, "$g_encountered_party", slot_center_last_taken_by_troop, "trp_player"),
        (assign, "$g_spacestation_requested_by_player", "$current_town"),
        (assign, "$auto_enter_town", "$g_encountered_party"),
        (change_screen_return),
        ]),
      ("spacestation_taken_no_claim",[],"Ask no rewards.",
       [
        (party_set_slot, "$g_encountered_party", slot_center_last_taken_by_troop, -1),
        (assign, "$auto_enter_town", "$g_encountered_party"),
        (change_screen_return),
#        (jump_to_menu, "mnu_town"),
        ]),
    ],
  ),

  (
    "requested_spacestation_granted_to_player",menu_text_color(0xFF000d2c)|mnf_scale_picture,
    "You receive a message from your liege, {s3}.^^\
 {reg4?She:He} has decided to grant {s2}{reg3? and the nearby planet of {s4}:} to you, with all due incomes and titles,\
 to hold in {reg4?her:his} name for as long as you maintain your oath of homage.",
    "none",
    [(set_background_mesh, "mesh_pic_messenger"),
     (faction_get_slot, ":faction_leader", "$players_faction", slot_faction_leader),
     (str_store_troop_name, s3, ":faction_leader"),
     (str_store_party_name, s2, "$g_center_to_give_to_player"),
     (try_begin),
       (party_slot_eq, "$g_center_to_give_to_player", slot_party_type, spt_castle),
       (assign, reg3, 1),
       (try_for_range, ":cur_village", minorplanet_begin, minorplanet_end),
         (party_slot_eq, ":cur_village", slot_minorplanet_bound_center, "$g_center_to_give_to_player"),
         (str_store_party_name, s4, ":cur_village"),
       (try_end),
     (else_try),
       (assign, reg3, 0),
     (try_end),
     #(troop_get_type, reg4, ":faction_leader"),
     (call_script, "script_gender_fix", ":faction_leader"),(assign,reg4,reg33)
    ],
    [
      ("continue_dot",[],"Continue.",
       [(call_script, "script_give_center_to_lord", "$g_center_to_give_to_player", "trp_player", 0),
        (jump_to_menu, "mnu_give_center_to_player_2"),
        ]),
     ],
  ),
  
  (
    "requested_spacestation_granted_to_another",menu_text_color(0xFF000d2c)|mnf_scale_picture,
    "You receive a message from your leader, {s3}.^^\
 'I was most pleased to hear of your valiant efforts in the capture of {s2}. Your victory has gladdened all our hearts.\
 You also requested me to give you ownership of the planet, but that is a favour which I fear I cannot grant,\
 as you already hold significant estates in my faction.\
 Instead I have sent you {reg6} credits to cover the expenses of your campaign, but {s2} I give to {s5}.'\
 ",
    "none",
    [(set_background_mesh, "mesh_pic_messenger"),
     (faction_get_slot, ":faction_leader", "$players_faction", slot_faction_leader),
     (str_store_troop_name, s3, ":faction_leader"),
     (str_store_party_name, s2, "$g_center_to_give_to_player"),
     (party_get_slot, ":new_owner", "$g_center_to_give_to_player", slot_mainplanet_lord),
     (str_store_troop_name, s5, ":new_owner"),
     (assign, reg6, 900),
    ],
    [
      ("accept_decision",[],"Accept the decision.",
       [
       (call_script, "script_troop_add_gold", "trp_player", reg6),
       (change_screen_return),
        ]),
      ("leave_faction",[],"You have been wronged! Renounce you oath to your liege! ",
       [
         (jump_to_menu, "mnu_leave_faction"),
         (call_script, "script_troop_add_gold", "trp_player", reg6),
        ]),
     ],
  ),

  (
    "leave_faction",menu_text_color(0xFF000d2c),
    "Renouncing your oath is a grave act. Your lord may condemn you and confiscate your lands and holdings.\
 However, if you return them of your own free will, he may let the betrayal go without a fight.",
    "none",
    [
    ],
    [
      ("leave_faction_give_back", [], "Renounce your oath and give up your holdings.",
       [
#Troop commentary changes begin
#        (call_script, "script_add_log_entry", logent_renounced_allegiance,   "trp_player",  -1, "$g_talk_troop", "$g_talk_troop_faction"),
#Troop commentary changes end
        (call_script, "script_player_leave_faction", 1),
        (change_screen_return),
        ]),
      ("leave_faction_hold", [
          (str_store_party_name, s2, "$g_center_to_give_to_player"),
          ], "Renounce your oath and hold on to your lands, including {s2}.",
       [
        (faction_get_slot, ":old_leader", "$players_faction", slot_faction_leader),
        (call_script, "script_add_log_entry", logent_renounced_allegiance,   "trp_player",  -1, ":old_leader", "$players_faction"),

        #Initializing renounce war variables
        (assign, "$players_oath_renounced_against_faction", "$players_faction"),
        (assign, "$players_oath_renounced_given_center", 0),
        (store_current_hours, "$players_oath_renounced_begin_time"),
        
        (call_script, "script_give_center_to_lord", "$g_center_to_give_to_player", "trp_player", 0),
        (call_script, "script_player_leave_faction", 0),
        (try_for_range, ":cur_center", walled_centers_begin, walled_centers_end),
          (store_faction_of_party, ":cur_center_faction", ":cur_center"),
          (party_set_slot, ":cur_center", slot_center_faction_when_oath_renounced, ":cur_center_faction"),
        (try_end),
        (party_set_slot, "$g_center_to_give_to_player", slot_center_faction_when_oath_renounced, "$players_oath_renounced_against_faction"),
        (change_screen_return),
        ]),
      ("leave_faction_cancel", [], "Remain loyal and accept the decision.",
       [
        (change_screen_return),
        ]),
    ],
  ),

  (
    "give_center_to_player",menu_text_color(0xFF000d2c)|mnf_scale_picture,
	  #SW - modified fiefs to territories
    "Your lord offers to extend your territories!\
 {s1} sends word that he is willing to grant {s2} to you in payment for your loyal service,\
 adding it to your holdings. What is your answer?",
    "none",
    [(set_background_mesh, "mesh_pic_messenger"),
     (store_faction_of_party, ":center_faction", "$g_center_to_give_to_player"),
     (faction_get_slot, ":faction_leader", ":center_faction", slot_faction_leader),
     (str_store_troop_name, s1, ":faction_leader"),
     (str_store_party_name, s2, "$g_center_to_give_to_player"),
    ],
    [
      ("accept_offer",[],"Accept the offer.",
       [(call_script, "script_give_center_to_lord", "$g_center_to_give_to_player", "trp_player", 0),
        (jump_to_menu, "mnu_give_center_to_player_2"),
        ]),
      ("give_center_to_player_reject",[],"Reject. You have no interest in holding {s2}.",
       [(party_set_slot, "$g_center_to_give_to_player", slot_mainplanet_lord, stl_rejected_by_player),
        (change_screen_return),
        ]),
    ],
  ),
  
  (
    "give_center_to_player_2",menu_text_color(0xFF000d2c),
    "With a brief ceremony, you are officially confirmed as the new lord of {s2}{reg3? and its bound planet {s4}:}.\
 {reg3?They:It} will make a fine part of your fiefdom.\
 You can now claim the rents and revenues from your personal estates there, draft soldiers from the populace,\
 and manage the lands as you see fit.\
 However, you are also expected to defend your fief and your people from harm,\
 as well as maintaining the rule of law and order.",
    "none",
    [
      (str_store_party_name, s2, "$g_center_to_give_to_player"),
      (assign, reg3, 0),
      (try_begin),
        (party_slot_eq, "$g_center_to_give_to_player", slot_party_type, spt_castle),
        (try_for_range, ":cur_village", minorplanet_begin, minorplanet_end),
          (party_slot_eq, ":cur_village", slot_minorplanet_bound_center, "$g_center_to_give_to_player"),
          (str_store_party_name, s4, ":cur_village"),
          (assign, reg3, 1),
        (try_end),
      (try_end),
    ],
    [
      ("continue_3dot",[],"Continue...",
       [(change_screen_return),
        ]),
    ],
  ),


  (
    "oath_fulfilled",menu_text_color(0xFF000d2c),
    "You had a contract with {s1} to serve him for a certain duration.\
 Your contract has now expired. What will you do?",
    "none",
    [
      (faction_get_slot, ":faction_leader", "$players_faction", slot_faction_leader),
      (str_store_troop_name, s1, ":faction_leader"),
     ],
    [
      ("renew_oath",[(faction_get_slot, ":faction_leader", "$players_faction", slot_faction_leader),
                     (str_store_troop_name, s1, ":faction_leader")], "Renew your contract with {s1} for another month.",
       [
         (store_current_day, ":cur_day"),
         (store_add, "$mercenary_service_next_renew_day", ":cur_day", 30),
         (change_screen_return),
         ]),
      ("dont_renew_oath",[],"Become free of your bond.",
       [
         (call_script, "script_player_leave_faction", 1),
         (change_screen_return),
         ]),
    ]
  ),
  

##  (
##    "spacestation_garrison_stationed",menu_text_color(0xFF000d2c),
###    "The rest of the castle garrison recognizes that their situation is hopeless and surrenders. {s1} is at your mercy now. What do you want to do with this castle?",
##    "_",
##    "none",
##    [
##        (jump_to_menu, "mnu_town"),
##    ],
##    [],
##  ),

##  (
##    "spacestation_choose_captain",menu_text_color(0xFF000d2c),
##    "You will need to assign one of your companions as the castellan. Who will it be?",
##    "none",
##    [
##        (try_for_range, ":slot_no", 0, 20),
##          (troop_set_slot, "trp_temp_troop", ":slot_no", 0),
##        (try_end),
##        (assign, ":num_captains", 0),
##        (party_clear, "p_temp_party"),
##        (party_get_num_companion_stacks, ":num_stacks", "p_main_party"),
##        (try_for_range, ":i_s", 1,":num_stacks"),
##          (party_stack_get_troop_id, ":companion","p_main_party", ":i_s"),
##          (troop_slot_eq, ":companion", slot_troop_occupation, slto_player_companion),
##          (troop_set_slot, "trp_temp_troop", ":num_captains", ":companion"),
##        (try_end),
##    ],
##    [
##      ("castellan_candidate",  [(troop_get_slot, ":captain", "trp_temp_troop", 0),(gt,":captain",0),(str_store_troop_name, s5,":captain")],
##         "{s5}",    [(troop_get_slot, "$selected_castellan", "trp_temp_troop", 0),(jump_to_menu,"mnu_spacestation_captain_chosen")]),
##      ("castellan_candidate",  [(troop_get_slot, ":captain", "trp_temp_troop", 1),(gt,":captain",0),(str_store_troop_name, s5,":captain")],
##         "{s5}",    [(troop_get_slot, "$selected_castellan", "trp_temp_troop", 1),(jump_to_menu,"mnu_spacestation_captain_chosen")]),
##      ("castellan_candidate",  [(troop_get_slot, ":captain", "trp_temp_troop", 2),(gt,":captain",0),(str_store_troop_name, s5,":captain")],
##         "{s5}",    [(troop_get_slot, "$selected_castellan", "trp_temp_troop", 2),(jump_to_menu,"mnu_spacestation_captain_chosen")]),
##      ("castellan_candidate",  [(troop_get_slot, ":captain", "trp_temp_troop", 3),(gt,":captain",0),(str_store_troop_name, s5,":captain")],
##         "{s5}",    [(troop_get_slot, "$selected_castellan", "trp_temp_troop", 3),(jump_to_menu,"mnu_spacestation_captain_chosen")]),
##      ("castellan_candidate",  [(troop_get_slot, ":captain", "trp_temp_troop", 4),(gt,":captain",0),(str_store_troop_name, s5,":captain")],
##         "{s5}",    [(troop_get_slot, "$selected_castellan", "trp_temp_troop", 4),(jump_to_menu,"mnu_spacestation_captain_chosen")]),
##      ("castellan_candidate",  [(troop_get_slot, ":captain", "trp_temp_troop", 5),(gt,":captain",0),(str_store_troop_name, s5,":captain")],
##         "{s5}",    [(troop_get_slot, "$selected_castellan", "trp_temp_troop", 5),(jump_to_menu,"mnu_spacestation_captain_chosen")]),
##      ("castellan_candidate",  [(troop_get_slot, ":captain", "trp_temp_troop", 6),(gt,":captain",0),(str_store_troop_name, s5,":captain")],
##         "{s5}",    [(troop_get_slot, "$selected_castellan", "trp_temp_troop", 6),(jump_to_menu,"mnu_spacestation_captain_chosen")]),
##      ("castellan_candidate",  [(troop_get_slot, ":captain", "trp_temp_troop", 7),(gt,":captain",0),(str_store_troop_name, s5,":captain")],
##         "{s5}",    [(troop_get_slot, "$selected_castellan", "trp_temp_troop", 7),(jump_to_menu,"mnu_spacestation_captain_chosen")]),
##      ("castellan_candidate",  [(troop_get_slot, ":captain", "trp_temp_troop", 8),(gt,":captain",0),(str_store_troop_name, s5,":captain")],
##         "{s5}",    [(troop_get_slot, "$selected_castellan", "trp_temp_troop", 8),(jump_to_menu,"mnu_spacestation_captain_chosen")]),
##      ("castellan_candidate",  [(troop_get_slot, ":captain", "trp_temp_troop", 9),(gt,":captain",0),(str_store_troop_name, s5,":captain")],
##         "{s5}",    [(troop_get_slot, "$selected_castellan", "trp_temp_troop", 9),(jump_to_menu,"mnu_spacestation_captain_chosen")]),
##      ("castellan_candidate",  [(troop_get_slot, ":captain", "trp_temp_troop", 10),(gt,":captain",0),(str_store_troop_name, s5,":captain")],
##         "{s5}",    [(troop_get_slot, "$selected_castellan", "trp_temp_troop", 10),(jump_to_menu,"mnu_spacestation_captain_chosen")]),
##      ("castellan_candidate",  [(troop_get_slot, ":captain", "trp_temp_troop", 11),(gt,":captain",0),(str_store_troop_name, s5,":captain")],
##         "{s5}",    [(troop_get_slot, "$selected_castellan", "trp_temp_troop", 11),(jump_to_menu,"mnu_spacestation_captain_chosen")]),
##      ("castellan_candidate",  [(troop_get_slot, ":captain", "trp_temp_troop", 12),(gt,":captain",0),(str_store_troop_name, s5,":captain")],
##         "{s5}",    [(troop_get_slot, "$selected_castellan", "trp_temp_troop", 12),(jump_to_menu,"mnu_spacestation_captain_chosen")]),
##      ("castellan_candidate",  [(troop_get_slot, ":captain", "trp_temp_troop", 13),(gt,":captain",0),(str_store_troop_name, s5,":captain")],
##         "{s5}",    [(troop_get_slot, "$selected_castellan", "trp_temp_troop", 13),(jump_to_menu,"mnu_spacestation_captain_chosen")]),
##      ("castellan_candidate",  [(troop_get_slot, ":captain", "trp_temp_troop", 14),(gt,":captain",0),(str_store_troop_name, s5,":captain")],
##         "{s5}",    [(troop_get_slot, "$selected_castellan", "trp_temp_troop", 14),(jump_to_menu,"mnu_spacestation_captain_chosen")]),
##      ("castellan_candidate",  [(troop_get_slot, ":captain", "trp_temp_troop", 15),(gt,":captain",0),(str_store_troop_name, s5,":captain")],
##         "{s5}",    [(troop_get_slot, "$selected_castellan", "trp_temp_troop", 15),(jump_to_menu,"mnu_spacestation_captain_chosen")]),
##      
##      ("cancel",[],
##         "Cancel...",
##         [(jump_to_menu, "mnu_town")]),
##    ],
##  ),
##  (
##    "spacestation_captain_chosen",menu_text_color(0xFF000d2c),
##    "h this castle?",
##    "none",
##    [
##        (party_add_leader, "$g_encountered_party",  "$selected_castellan"),
##        (party_remove_members, "p_main_party", "$selected_castellan",1),
##        (party_set_slot, "$g_encountered_party", slot_mainplanet_lord, "trp_player"),
##        (party_set_faction, "$g_encountered_party", "fac_player_supporters_faction"),
##        (try_for_range, ":slot_no", 0, 20), #clear temp troop slots just in case
##          (troop_set_slot, "trp_temp_troop", ":slot_no", 0),
##        (try_end),
##        (jump_to_menu, "mnu_town"),
##        (change_screen_exchange_members,0),
##    ],
##    [],
##  ),

##  (
##    "under_siege_attacked_continue",menu_text_color(0xFF000d2c),
##    "Nothing to see here.",
##    "none",
##    [
##        (assign, "$g_enemy_party", "$g_encountered_party_2"),
##        (assign, "$g_ally_party", "$g_encountered_party"),
##        (party_set_next_battle_simulation_time, "$g_encountered_party", 0),
##        (call_script, "script_encounter_calculate_fit"),
##        (try_begin),
##          (call_script, "script_party_count_fit_regulars", "p_collective_enemy"),
##          (assign, ":num_enemy_regulars_remaining", reg(0)),
##          (assign, ":enemy_finished",0),
##          (try_begin),
##            (eq, "$g_battle_result", 1),
##            (eq, ":num_enemy_regulars_remaining", 0), #battle won
##            (assign, ":enemy_finished",1),
##          (else_try),
##            (eq, "$g_engaged_enemy", 1),
##            (le, "$g_enemy_fit_for_battle",0),
##            (ge, "$g_friend_fit_for_battle",1),
##            (assign, ":enemy_finished",1),
##          (try_end),
##          (this_or_next|eq, ":enemy_finished",1),
##          (eq,"$g_enemy_surrenders",1),
####          (assign, "$g_center_under_siege_battle", 0),
##          (assign, "$g_next_menu", -1),
##          (jump_to_menu, "mnu_total_victory"),
##        (else_try),
##          (assign, ":battle_lost", 0),
##          (try_begin),
##            (eq, "$g_battle_result", -1),
##            (assign, ":battle_lost",1),
##          (try_end),
##          (this_or_next|eq, ":battle_lost",1),
##          (eq,"$g_player_surrenders",1),
####          (assign, "$g_center_under_siege_battle", 0),
##          (assign, "$g_next_menu", "mnu_captivity_start_under_siege_defeat"),
##          (jump_to_menu, "mnu_total_defeat"),
##        (else_try),
##    # Ordinary victory.
##          (try_begin),
##          #check whether enemy retreats
##            (eq, "$g_battle_result", 1),
##            (store_mul, ":min_enemy_str", "$g_enemy_fit_for_battle", 2),
##            (lt, ":min_enemy_str", "$g_friend_fit_for_battle"),
##            (party_set_slot, "$g_enemy_party", slot_party_retreat_flag, 1),
##
##            (try_for_range, ":troop_no", faction_heroes_begin, faction_heroes_end),
##              (troop_slot_eq, ":troop_no", slot_troop_occupation, slto_faction_hero),
##              (troop_slot_eq, ":troop_no", slot_troop_is_prisoner, 0),
##              (troop_get_slot, ":party_no", ":troop_no", slot_troop_leaded_party),
##              (gt, ":party_no", 0),
##              (party_slot_eq, ":party_no", slot_party_ai_state, spai_besieging_center),
##              (party_slot_eq, ":party_no", slot_party_ai_object, "$g_encountered_party"),
##              (party_slot_eq, ":party_no", slot_party_ai_substate, 1),
##              (call_script, "script_party_set_ai_state", ":party_no", spai_undefined, -1),
##              (call_script, "script_party_set_ai_state", ":party_no", spai_besieging_center, ":center_no"),
##            (try_end),
##            (display_message, "@TODO: Enemy retreated. The assault has ended, siege continues."),
##            (change_screen_return),
##          (try_end),
####          (assign, "$g_center_under_siege_battle", 0),
##        (try_end),
##        ],
##    [
##    ]
##  ),


  (
    "siege_started_defender",menu_text_color(0xFF000d2c),
    "{s1} is launching an assault against {s2}. You have {reg10} troops fit for battle against the enemy's {reg11}. You decide to...",
    "none",
    [
        (select_enemy,1),
        (assign, "$g_enemy_party", "$g_encountered_party_2"),
        (assign, "$g_ally_party", "$g_encountered_party"),
        (str_store_party_name, 1,"$g_enemy_party"),
        (str_store_party_name, 2,"$g_ally_party"),
        (call_script, "script_encounter_calculate_fit"),
        (try_begin),
          (eq, "$g_siege_first_encounter", 1),
          (call_script, "script_let_nearby_parties_join_current_battle", 0, 1),
          (call_script, "script_encounter_init_variables"),
        (try_end),

        (try_begin),
          (eq, "$g_siege_first_encounter", 0),
          (try_begin),
            (call_script, "script_party_count_members_with_full_health", "p_collective_enemy"),
            (assign, ":num_enemy_regulars_remaining", reg0),
            (call_script, "script_party_count_members_with_full_health", "p_collective_friends"),
            (assign, ":num_ally_regulars_remaining", reg0),
            (assign, ":enemy_finished", 0),
            (try_begin),
              (eq, "$g_battle_result", 1),
              (eq, ":num_enemy_regulars_remaining", 0), #battle won
              (assign, ":enemy_finished",1),
            (else_try),
              (eq, "$g_engaged_enemy", 1),
              (le, "$g_enemy_fit_for_battle",0),
              (ge, "$g_friend_fit_for_battle",1),
              (assign, ":enemy_finished",1),
            (try_end),
            (this_or_next|eq, ":enemy_finished",1),
            (eq,"$g_enemy_surrenders",1),
            (assign, "$g_next_menu", -1),
            (jump_to_menu, "mnu_total_victory"),
          (else_try),
            (assign, ":battle_lost", 0),
            (try_begin),
              (this_or_next|eq, "$g_battle_result", -1),
              (troop_is_wounded,  "trp_player"),
              (eq, ":num_ally_regulars_remaining", 0),
              (assign, ":battle_lost",1),
            (try_end),
            (this_or_next|eq, ":battle_lost",1),
            (eq,"$g_player_surrenders",1),
            (assign, "$g_next_menu", "mnu_captivity_start_under_siege_defeat"),
            (jump_to_menu, "mnu_total_defeat"),
          (else_try),
            # Ordinary victory/defeat.
            (assign, ":attackers_retreat", 0),
            (try_begin),
            #check whether enemy retreats
              (eq, "$g_battle_result", 1),
  ##            (store_mul, ":min_enemy_str", "$g_enemy_fit_for_battle", 2),
  ##            (lt, ":min_enemy_str", "$g_friend_fit_for_battle"),
              (assign, ":attackers_retreat", 1),
            (else_try),
              (eq, "$g_battle_result", 0),
              (store_div, ":min_enemy_str", "$g_enemy_fit_for_battle", 3),
              (lt, ":min_enemy_str", "$g_friend_fit_for_battle"),
              (assign, ":attackers_retreat", 1),
            (else_try),
              (store_random_in_range, ":random_no", 0, 100),
              (lt, ":random_no", 10),
              (neq, "$new_encounter", 1),
              (assign, ":attackers_retreat", 1),
            (try_end),
            (try_begin),
              (eq, ":attackers_retreat", 1),
              (party_get_slot, ":siege_hardness", "$g_encountered_party", slot_center_siege_hardness),
              (val_add, ":siege_hardness", 100),
              (party_set_slot, "$g_encountered_party", slot_center_siege_hardness, ":siege_hardness"),
              (party_set_slot, "$g_enemy_party", slot_party_retreat_flag, 1),

              (try_for_range, ":troop_no", faction_heroes_begin, faction_heroes_end),
                (troop_slot_eq, ":troop_no", slot_troop_occupation, slto_faction_hero),
                #(troop_slot_eq, ":troop_no", slot_troop_is_prisoner, 0),
                (neg|troop_slot_ge, ":troop_no", slot_troop_prisoner_of_party, 0),
                (troop_get_slot, ":party_no", ":troop_no", slot_troop_leaded_party),
                (gt, ":party_no", 0),
                (party_slot_eq, ":party_no", slot_party_ai_state, spai_besieging_center),
                (party_slot_eq, ":party_no", slot_party_ai_object, "$g_encountered_party"),
                (party_slot_eq, ":party_no", slot_party_ai_substate, 1),
                (call_script, "script_party_set_ai_state", ":party_no", spai_undefined, -1),
                (call_script, "script_party_set_ai_state", ":party_no", spai_besieging_center, "$g_encountered_party"),
              (try_end),
              (display_message, "@The enemy has been forced to retreat. The assault is over, but the siege continues."),
              (assign, "$g_battle_simulation_cancel_for_party", "$g_encountered_party"),
              (leave_encounter),
              (change_screen_return),
              (assign, "$g_battle_simulation_auto_enter_town_after_battle", "$g_encountered_party"),
            (try_end),
          (try_end),
        (try_end),
        (assign, "$g_siege_first_encounter", 0),
        (assign, "$new_encounter", 0),
        ],
    [

############################################################################################################
##### Custom Commander(CC)
############################################################################################################
    
      ("commander_change",[(str_store_troop_name,s7,"$g_player_troop")],
        "Change the commander. (Current:{s7})",
        [
          (assign, "$g_next_menu", "mnu_siege_started_defender"),
          (assign, "$change_commander_menu_offset", 0),
          (jump_to_menu, "mnu_change_commander"),
        ]),

############################################################################################################
##### Custom Commander(CC)
############################################################################################################
	
      ("siege_defender_join_battle",
       [
############################################################################################################
##### Custom Commander(CC)
############################################################################################################
          #(neg|troop_is_wounded, "trp_player"),
          (neg|troop_is_wounded, "$g_player_troop"),
############################################################################################################
##### Custom Commander(CC)
############################################################################################################
         ],
          "Join the battle.",[
              (party_set_next_battle_simulation_time, "$g_encountered_party", -1),
              (assign, "$g_battle_result", 0),
              (try_begin),
                (party_slot_eq, "$g_encountered_party", slot_party_type, spt_mainplanet),
                (party_get_slot, ":battle_scene", "$g_encountered_party", slot_mainplanet_walls),
              (else_try),
                (party_get_slot, ":battle_scene", "$g_encountered_party", slot_spacestation_exterior),
              (try_end),
              (call_script, "script_calculate_battle_advantage"),
              (val_mul, reg0, 2),
              (val_div, reg0, 3), #scale down the advantage a bit.
              (set_battle_advantage, reg0),
              (set_party_battle_mode),
              (try_begin),
                (party_slot_eq, "$current_town", slot_center_siege_with_belfry, 1),
                (set_jump_mission,"mt_spacestation_attack_walls_belfry"),
              (else_try),
                (set_jump_mission,"mt_spacestation_attack_walls_ladder"),
              (try_end),
              (jump_to_scene,":battle_scene"),
              (assign, "$g_next_menu", "mnu_siege_started_defender"),
              (jump_to_menu, "mnu_battle_debrief"),
              (change_screen_mission)]),
      ("siege_defender_troops_join_battle",[(call_script, "script_party_count_members_with_full_health", "p_main_party"),
                                            (this_or_next|troop_is_wounded,  "trp_player"),
                                            (ge, reg0, 3)],
          "Order your men to join the battle without you.",[
              (party_set_next_battle_simulation_time, "$g_encountered_party", -1),
              (select_enemy,1),
              (assign,"$g_enemy_party","$g_encountered_party_2"),
              (assign,"$g_ally_party","$g_encountered_party"),
              (assign,"$g_siege_join", 1),
              (jump_to_menu,"mnu_siege_join_defense")]),
##      ("siege_defender_do_not_join_battle",[(call_script, "script_party_count_fit_regulars","p_collective_ally"),
##                                            (gt, reg0, 0)],
##       "Don't get involved.", [(leave_encounter),
##                               (change_screen_return),
##           ]),

##      ("siege_defender_surrender",[(call_script, "script_party_count_fit_regulars","p_collective_ally"),
##                                   (this_or_next|eq, reg0, 0),
##                                   (party_slot_eq, "$g_encountered_party", slot_mainplanet_lord, "trp_player"),
##                                   ],
##       "Surrender.",[(assign, "$g_player_surrenders", 1),
##                     (jump_to_menu,"mnu_under_siege_attacked_continue")]),
    ]
  ),

  (
    "siege_join_defense",menu_text_color(0xFF000d2c)|mnf_disable_all_keys,
    "{s4}^^Your casualties: {s8}^^Allies' casualties: {s9}^^Enemy casualties: {s10}",
    "none",
    [
        (try_begin),
          (eq, "$g_siege_join", 1),
          (call_script, "script_party_calculate_strength", "p_main_party", 1), #skip player
          (assign, ":player_party_strength", reg0),
          (val_div, ":player_party_strength", 5),
        (else_try),
          (assign, ":player_party_strength", 0),
        (try_end),
        
        (call_script, "script_party_calculate_strength", "p_collective_ally", 0),
        (assign, ":ally_party_strength", reg0),
        (val_div, ":ally_party_strength", 5),
        (call_script, "script_party_calculate_strength", "p_collective_enemy", 0),
        (assign, ":enemy_party_strength", reg0),
        (val_div, ":enemy_party_strength", 10),

        (store_add, ":friend_party_strength", ":player_party_strength", ":ally_party_strength"),
        (assign, ":enemy_party_strength_for_p", ":enemy_party_strength"),
        (val_mul, ":enemy_party_strength_for_p", ":player_party_strength"),
        (val_div, ":enemy_party_strength_for_p", ":friend_party_strength"),

        (val_sub, ":enemy_party_strength", ":enemy_party_strength_for_p"),
        (inflict_casualties_to_party_group, "p_main_party", ":enemy_party_strength_for_p", "p_temp_casualties"),
        (call_script, "script_print_casualties_to_s0", "p_temp_casualties", 0),
        (str_store_string_reg, s8, s0),

        (inflict_casualties_to_party_group, "$g_ally_party", ":enemy_party_strength", "p_temp_casualties"),
        (call_script, "script_print_casualties_to_s0", "p_temp_casualties", 0),
        (str_store_string_reg, s9, s0),
        (party_collect_attachments_to_party, "$g_ally_party", "p_collective_ally"),

        (inflict_casualties_to_party_group, "$g_enemy_party", ":friend_party_strength", "p_temp_casualties"),
        (call_script, "script_print_casualties_to_s0", "p_temp_casualties", 0),
        (str_store_string_reg, s10, s0),
        (party_collect_attachments_to_party, "$g_enemy_party", "p_collective_enemy"),

        (try_begin),
          (call_script, "script_party_count_members_with_full_health","p_main_party"),
          (le, reg(0), 0),
          (str_store_string, s4, "str_siege_defender_order_attack_failure"),
        (else_try),
          (call_script, "script_party_count_members_with_full_health","p_collective_enemy"),
          (le, reg(0), 0),
          (assign, "$g_battle_result", 1),
          (str_store_string, s4, "str_siege_defender_order_attack_success"),
        (else_try),
          (str_store_string, s4, "str_siege_defender_order_attack_continue"),
        (try_end),
    ],
    [
      ("continue_3dot",[],"Continue...",[
          (jump_to_menu,"mnu_siege_started_defender"),
          ]),
    ]
  ),

  (
    "enter_your_own_castle",menu_text_color(0xFF000d2c),
    "As you approach, you are spotted by the planet guards, who welcome you and lower the shields for their {lord/lady}.",
    "none",
    [
      (str_store_party_name, s2, "$current_town"),
    ],
    [
      ("continue_3dot",[],"Continue...",
       [ (jump_to_menu,"mnu_town"),
        ]),
    ],
  ),


  (
    "village",menu_text_color(0xFF000d2c)|mnf_enable_hot_keys,
    "{s10}{s11}{s6}{s7}",
    "none",
    [
        (assign, "$current_town", "$g_encountered_party"),
        (call_script, "script_update_center_recon_notes", "$current_town"),

        (assign, "$g_defending_against_siege", 0), #required for bandit check
        (assign, "$g_battle_result", 0),
        (assign, "$qst_collect_taxes_currently_collecting", 0),
        (assign, "$qst_train_peasants_against_bandits_currently_training", 0),

        (try_begin),
          (gt, "$auto_enter_menu_in_center", 0),
          (jump_to_menu, "$auto_enter_menu_in_center"),
          (assign, "$auto_enter_menu_in_center", 0),
        (try_end),

        (try_begin),
          (neq, "$g_player_raiding_village",  "$current_town"),
          (assign, "$g_player_raiding_village", 0),
        (else_try),
          (jump_to_menu, "mnu_minorplanet_loot_continue"),
        (try_end),

        (try_begin),#Fix for collecting taxes
          (eq, "$g_town_visit_after_rest", 1),
          (assign, "$g_town_visit_after_rest", 0),
        (try_end),

        (str_store_party_name,s2, "$current_town"),
        (party_get_slot, ":center_lord", "$current_town", slot_mainplanet_lord),
        (store_faction_of_party, ":center_faction", "$current_town"),
        (str_store_faction_name,s9,":center_faction"),
        (try_begin),
          (ge, ":center_lord", 0),
          (str_store_troop_name,s8,":center_lord"),
          (str_store_string,s7,"@{s8} of {s9}"),
        (try_end),

        (str_clear, s10),
        (try_begin),
          (neg|party_slot_eq, "$current_town", slot_minorplanet_state, svs_looted),
          (str_store_string, s60, s2),
          (party_get_slot, ":prosperity", "$current_town", slot_mainplanet_prosperity),
          (val_add, ":prosperity", 5),
          (store_div, ":str_offset", ":prosperity", 10),
          (store_add, ":str_id", "str_minorplanet_prosperity_0",  ":str_offset"),
          (str_store_string, s10, ":str_id"),
        (try_end),

        (str_clear, s11),
        (try_begin),
          (party_slot_eq, "$current_town", slot_minorplanet_state, svs_looted),
        (else_try),
          (eq, ":center_lord", "trp_player"),
          (str_store_string,s11,"@ This planet and the surrounding moons belong to you."),
        (else_try),
          (ge, ":center_lord", 0),
          (str_store_string,s11,"@ You remember that this planet and the surrounding moons belong to {s7}."),
        (else_try),
          (str_store_string,s11,"@ These lands belong to no one."),
        (try_end),

        (str_clear, s7),
        (try_begin),
          (neg|party_slot_eq, "$current_town", slot_minorplanet_state, svs_looted),
          (party_get_slot, ":center_relation", "$current_town", slot_center_player_relation),
          (call_script, "script_describe_center_relation_to_s3", ":center_relation"),
          (assign, reg9, ":center_relation"),
          (str_store_string, s7, "@ {s3} ({reg9})."),
        (try_end),
        (str_clear, s6),
        (try_begin),
          (party_slot_ge, "$current_town", slot_minorplanet_infested_by_bandits, 1),
          (party_get_slot, ":bandit_troop", "$current_town", slot_minorplanet_infested_by_bandits),
          (store_character_level, ":player_level", "trp_player"),
          (store_add, "$qst_eliminate_bandits_infesting_minorplanet_num_bandits", ":player_level", 10),
          (val_mul, "$qst_eliminate_bandits_infesting_minorplanet_num_bandits", 12),
          (val_div, "$qst_eliminate_bandits_infesting_minorplanet_num_bandits", 10),
          (store_random_in_range, "$qst_eliminate_bandits_infesting_minorplanet_num_villagers", 25, 30),
          (assign, reg8, "$qst_eliminate_bandits_infesting_minorplanet_num_bandits"),
          (str_store_troop_name_by_count, s35, ":bandit_troop", "$qst_eliminate_bandits_infesting_minorplanet_num_bandits"),
          (str_store_string, s6, "@ The planet is infested by {reg8} {s35}."),
          (try_begin),
            (eq, ":bandit_troop", "trp_blazing_claw_pirate"),
            (set_background_mesh, "mesh_pic_blazing_claw_pirates"),
          (else_try),
            (eq, ":bandit_troop", "trp_steppe_bandit"),
            (set_background_mesh, "mesh_pic_night_fang_pirates"),
          (else_try),
            (eq, ":bandit_troop", "trp_black_sun_pirate_3"),
            (set_background_mesh, "mesh_pic_black_sun_pirates"),
          (else_try),
            (eq, ":bandit_troop", "trp_tusken_1"),
            (set_background_mesh, "mesh_pic_tusken_raiders"),
          (else_try),
            (set_background_mesh, "mesh_pic_bandits"),
          (try_end),
        (else_try),
          (party_slot_eq, "$current_town", slot_minorplanet_state, svs_looted),
          (str_store_string, s6, "@ The planet has been looted. A handful of souls scatter as you pass through the burnt out houses."),
          (try_begin),
            (neq, "$g_player_raid_complete", 1),
			#SW - commented out track_empty_village
            #(play_track, "track_empty_village", 1),
          (try_end),
          (set_background_mesh, "mesh_pic_looted_village"),
        (else_try),
          (party_slot_eq, "$current_town", slot_minorplanet_state, svs_being_raided),
          (str_store_string, s6, "@ The planet is being raided."),
        (else_try),
          # (party_get_current_terrain, ":cur_terrain", "$current_town"),
          # (try_begin),
            # (this_or_next|eq, ":cur_terrain", rt_steppe),
            # (             eq, ":cur_terrain", rt_steppe_forest),
            # (set_background_mesh, "mesh_pic_minorplanet_s"),
          # (else_try),
            # (this_or_next|eq, ":cur_terrain", rt_snow),
            # (             eq, ":cur_terrain", rt_snow_forest),
            # (set_background_mesh, "mesh_pic_minorplanet_w"),
          # (else_try),
            # (set_background_mesh, "mesh_pic_minorplanet_p"),
          # (try_end),
			#SW - display a new menu background
			(call_script, "script_display_fullscreen_background", "$current_town"),			  
        (try_end),

        (try_begin),
          (eq, "$g_player_raid_complete", 1),
          (assign, "$g_player_raid_complete", 0),
          (jump_to_menu, "mnu_minorplanet_loot_complete"),
        (else_try),
          (party_get_slot, ":raider_party", "$current_town", slot_minorplanet_raided_by),
          (gt, ":raider_party", 0),
        # Process here...
        (try_end),

         # #Adding tax to player if player is the owner of the villager
        # (try_begin),
          # (party_slot_eq, "$current_town", slot_mainplanet_lord, "trp_player"),
          # (party_get_slot, ":accumulated_rents", "$current_town", slot_center_accumulated_rents),
          # (gt, ":accumulated_rents", 0),
          # (jump_to_menu, "mnu_center_tax"),
        # (try_end),

        (try_begin),
          (eq,"$g_leave_town",1),
          (assign,"$g_leave_town",0),
          (change_screen_return),
        (try_end),

        (try_begin), 
          (store_time_of_day, ":cur_hour"),
          (ge, ":cur_hour", 5),
          (lt, ":cur_hour", 21),
          (assign, "$town_nighttime", 0),
        (else_try),
          (assign, "$town_nighttime", 1),
        (try_end),
    ],
    [
      ("minorplanet_manage",[(neg|party_slot_eq, "$current_town", slot_minorplanet_state, svs_looted),
                         (neg|party_slot_eq, "$current_town", slot_minorplanet_state, svs_being_raided),
                         (neg|party_slot_ge, "$current_town", slot_minorplanet_infested_by_bandits, 1),
                         (party_slot_eq, "$current_town", slot_mainplanet_lord, "trp_player")]
       #SW - modified menu
	   #,"Manage this village.",
	   ,"Manage this planet.",
       [
           (assign, "$g_next_menu", "mnu_village"),
           (jump_to_menu, "mnu_center_manage"),
        ]),

#SW - Talk to village elder START      
      ("minorplanet_elder_talk",[(neg|party_slot_eq, "$current_town", slot_minorplanet_state, svs_looted),
                         (neg|party_slot_eq, "$current_town", slot_minorplanet_state, svs_being_raided),
                         (neg|party_slot_ge, "$current_town", slot_minorplanet_infested_by_bandits, 1),]
       ,"Speak with the Planet Administrator.",
       [
         (try_begin),
           (call_script, "script_cf_enter_center_location_bandit_check"),
         (else_try),
           (party_get_slot, ":minorplanet_scene", "$current_town", slot_spacestation_exterior),
           (modify_visitors_at_site,":minorplanet_scene"),
           (reset_visitors),
           (party_get_slot, ":minorplanet_elder_troop", "$current_town",slot_mainplanet_elder),
           (set_visitor, 11, ":minorplanet_elder_troop"),

           (call_script, "script_init_town_walkers"),

           (try_begin),
             (check_quest_active, "qst_hunt_down_fugitive"),
             (neg|is_currently_night),
             (quest_slot_eq, "qst_hunt_down_fugitive", slot_quest_target_center, "$current_town"),
             (neg|check_quest_succeeded, "qst_hunt_down_fugitive"),
             (neg|check_quest_failed, "qst_hunt_down_fugitive"),
             (set_visitor, 45, "trp_fugitive"),
           (try_end),

           (set_jump_mission,"mt_minorplanet_center"),
           (jump_to_scene,":minorplanet_scene"),

           (change_screen_map_conversation, ":minorplanet_elder_troop"),
         (try_end),
        ],"Door to the planet center."),
#SW - Talk to village elder END
		
# inserted by obi 2009-04-28 --> recruit clones, droids, force sensitives
		("recruit_clones",[(call_script, "script_cf_minorplanet_recruit_clones_cond"),]
       ,"Recruit Clones.",
       [
         (try_begin),
           (call_script, "script_cf_enter_center_location_bandit_check"),
         (else_try),
           (jump_to_menu, "mnu_recruit_clones"),
         (try_end),
        ]),
		("recruit_force_sensitive",[(call_script, "script_cf_minorplanet_recruit_force_sensitives_cond"),]
       ,"Recruit Force-Sensitives.",
       [
         (try_begin),
           (call_script, "script_cf_enter_center_location_bandit_check"),
         (else_try),
           (jump_to_menu, "mnu_recruit_force_sensitives"),
         (try_end),
        ]),
		("recruit_droid",[(call_script, "script_cf_minorplanet_recruit_droids_cond"),]
       ,"Build Battle Droids.",
       [
         (try_begin),
           (call_script, "script_cf_enter_center_location_bandit_check"),
         (else_try),
           #(jump_to_menu, "mnu_recruit_droids"),
		   (jump_to_menu, "mnu_recruit_droids_pre"),
         (try_end),
        ]),
		("recruit_rancor",[(call_script, "script_cf_minorplanet_recruit_rancors_cond"),]
       ,"Recruit Baby Rancors.",
       [
         (try_begin),
           (call_script, "script_cf_enter_center_location_bandit_check"),
         (else_try),
           (jump_to_menu, "mnu_recruit_rancors"),
         (try_end),
        ]),		
# end of insert
      ("recruit_volunteers",[(call_script, "script_cf_minorplanet_recruit_volunteers_cond"),]
       ,"Recruit Volunteers.",
       [
         (try_begin),
           (call_script, "script_cf_enter_center_location_bandit_check"),
         (else_try),
           (jump_to_menu, "mnu_recruit_volunteers"),
         (try_end),
        ]),
      ("land_surface",[(neg|party_slot_eq, "$current_town", slot_minorplanet_state, svs_looted),
                         (neg|party_slot_eq, "$current_town", slot_minorplanet_state, svs_being_raided),
                         (neg|party_slot_ge, "$current_town", slot_minorplanet_infested_by_bandits, 1),]
       #,"Go to the center.",
	   ,"Land on the planet surface.",
       [
	   
		 (assign, "$g_init_fight", 0),
		 (assign, "$tavern_brawl", 0),
	   
         (try_begin),
           (call_script, "script_cf_enter_center_location_bandit_check"),
         (else_try),
           (party_get_slot, ":minorplanet_scene", "$current_town", slot_spacestation_exterior),	#:minorplanet_scene
           (modify_visitors_at_site,":minorplanet_scene"),
           (reset_visitors),
           (party_get_slot, ":minorplanet_elder_troop", "$current_town",slot_mainplanet_elder),
           (set_visitor, 11, ":minorplanet_elder_troop"),

           (call_script, "script_init_town_walkers"),

           (try_begin),
             (check_quest_active, "qst_hunt_down_fugitive"),
             (neg|is_currently_night),
             (quest_slot_eq, "qst_hunt_down_fugitive", slot_quest_target_center, "$current_town"),
             (neg|check_quest_succeeded, "qst_hunt_down_fugitive"),
             (neg|check_quest_failed, "qst_hunt_down_fugitive"),
             (set_visitor, 45, "trp_fugitive"),
           (try_end),
		   
			#SW - Bounty Hunting Start - http://forums.taleworlds.com/index.php/topic,59300.0.html
           (try_begin),
          (check_quest_active, "qst_bounty_1"),
             (neg|is_currently_night),
             (quest_slot_eq, "qst_bounty_1", slot_quest_target_center, "$current_town"),
             (neg|check_quest_succeeded, "qst_bounty_1"),
             (neg|check_quest_failed, "qst_bounty_1"),
             (store_random_in_range, "$bounty_target_1", bounty_1_targets_begin, bounty_1_targets_end),
			 #(assign, "$bounty_target_1", "trp_bounty_target_1"),
             (set_visitor, 45, "$bounty_target_1"),
           (try_end),
           (try_begin),
          (check_quest_active, "qst_bounty_2"),
             (neg|is_currently_night),
             (quest_slot_eq, "qst_bounty_2", slot_quest_target_center, "$current_town"),
             (neg|check_quest_succeeded, "qst_bounty_2"),
             (neg|check_quest_failed, "qst_bounty_2"),
             (store_random_in_range, "$bounty_target_2", bounty_2_targets_begin, bounty_2_targets_end),
			 #(assign, "$bounty_target_2", "trp_bounty_target_2"),
             (set_visitor, 45, "$bounty_target_2"),
           (try_end),
           (try_begin),
          (check_quest_active, "qst_bounty_3"),
             (neg|is_currently_night),
             (quest_slot_eq, "qst_bounty_3", slot_quest_target_center, "$current_town"),
             (neg|check_quest_succeeded, "qst_bounty_3"),
             (neg|check_quest_failed, "qst_bounty_3"),
             (store_random_in_range, "$bounty_target_3", bounty_3_targets_begin, bounty_3_targets_end),
			 #(assign, "$bounty_target_3", "trp_bounty_target_3"),
             (set_visitor, 45, "$bounty_target_3"),
           (try_end),
           (try_begin),
          (check_quest_active, "qst_bounty_4"),
             (neg|is_currently_night),
             (quest_slot_eq, "qst_bounty_4", slot_quest_target_center, "$current_town"),
             (neg|check_quest_succeeded, "qst_bounty_4"),
             (neg|check_quest_failed, "qst_bounty_4"),
             (store_random_in_range, "$bounty_target_4", bounty_4_targets_begin, bounty_4_targets_end),
			 #(assign, "$bounty_target_4", "trp_bounty_target_4"),
             (set_visitor, 45, "$bounty_target_4"),
           (try_end),
           (try_begin),
          (check_quest_active, "qst_bounty_5"),
             (neg|is_currently_night),
             (quest_slot_eq, "qst_bounty_5", slot_quest_target_center, "$current_town"),
             (neg|check_quest_succeeded, "qst_bounty_5"),
             (neg|check_quest_failed, "qst_bounty_5"),
             (store_random_in_range, "$bounty_target_5", bounty_5_targets_begin, bounty_5_targets_end),
			 #(assign, "$bounty_target_5", "trp_bounty_target_5"),
             (set_visitor, 45, "$bounty_target_5"),
           (try_end),
           (try_begin),
          (check_quest_active, "qst_bounty_6"),
             (neg|is_currently_night),
             (quest_slot_eq, "qst_bounty_6", slot_quest_target_center, "$current_town"),
             (neg|check_quest_succeeded, "qst_bounty_6"),
             (neg|check_quest_failed, "qst_bounty_6"),
             (store_random_in_range, "$bounty_target_6", bounty_6_targets_begin, bounty_6_targets_end),
			 #(assign, "$bounty_target_6", "trp_bounty_target_6"),
             (set_visitor, 45, "$bounty_target_6"),
           (try_end),
			#SW - Bounty Hunting End
		   
		   
		   # # #SW - attempting to add town specific music (this concept doesn't seem to work at all?  I had to add that persist until finished flag...)
			# (try_begin),
				# (this_or_next|eq, "$current_town", "p_endor"),		#Endor
				# (eq, "$current_town", "p_dantooine"),		#Dantooine
				# (play_track, "track_town_endor", 2),	# 0 = default, 1 = fade out current track, 2 = stop current track
			# (else_try),
				# (eq, "$current_town", "p_kashyyyk"),		#Kashyyyk
				# (play_track, "track_town_wookiee", 2),	# 0 = default, 1 = fade out current track, 2 = stop current track
			# (else_try),
				# (this_or_next|eq, "$current_town", "p_gamorr"),		#Gamorr
				# (this_or_next|eq, "$current_town", "p_tatooine"),		#Tatooine
				# (this_or_next|eq, "$current_town", "p_ryloth"),		#Ryloth
				# (eq, "$current_town", "p_nalhutta"),		#Nal_Hutta
				# #(play_track, "track_town_desert", 2),	# 0 = default, 1 = fade out current track, 2 = stop current track
				# (play_track, "track_town_test", 2),		# 0 = default, 1 = fade out current track, 2 = stop current track
			# (try_end),
		   
           (set_jump_mission,"mt_minorplanet_center"),
           (jump_to_scene,":minorplanet_scene"),
           (change_screen_mission),
         (try_end),
        ],"Door to the center."),
		
      ("minorplanet_buy_food",[(party_slot_eq, "$current_town", slot_minorplanet_state, 0),
                           (neg|party_slot_ge, "$current_town", slot_minorplanet_infested_by_bandits, 1),
                           ],"Buy supplies from the inhabitants.",
       [
         (try_begin),
           (call_script, "script_cf_enter_center_location_bandit_check"),
         (else_try),
           (party_get_slot, ":merchant_troop", "$current_town", slot_mainplanet_elder),
           (change_screen_trade, ":merchant_troop"),
         (try_end),
         ]),

############################################################################################################
##### Custom Commander(CC)
############################################################################################################
    
      ("commander_change",
      [
        (party_slot_ge, "$current_town", slot_minorplanet_infested_by_bandits, 1),
        (str_store_troop_name,s7,"$g_player_troop"),
      ],
      "Change the commander. (Current:{s7})",
      [
        (assign, "$g_next_menu", "mnu_village"),
        (assign, "$change_commander_menu_offset", 0),
        (jump_to_menu, "mnu_change_commander"),
      ]),

############################################################################################################
##### Custom Commander(CC)
############################################################################################################		 
		 
      ("minorplanet_attack_bandits",[(party_slot_ge, "$current_town", slot_minorplanet_infested_by_bandits, 1),],
       "Attack the bandits.",
       [(party_get_slot, ":bandit_troop", "$current_town", slot_minorplanet_infested_by_bandits),
        (party_get_slot, ":scene_to_use", "$current_town", slot_spacestation_exterior),
        (modify_visitors_at_site,":scene_to_use"),
        (reset_visitors),
        (set_visitors, 0, ":bandit_troop", "$qst_eliminate_bandits_infesting_minorplanet_num_bandits"),
        (set_visitors, 2, "trp_farmer", "$qst_eliminate_bandits_infesting_minorplanet_num_villagers"),
        (set_party_battle_mode),
        (set_battle_advantage, 0),
        (assign, "$g_battle_result", 0),
        (set_jump_mission,"mt_minorplanet_attack_bandits"),
        (jump_to_scene, ":scene_to_use"),
        (assign, "$g_next_menu", "mnu_minorplanet_infest_bandits_result"),
        (jump_to_menu, "mnu_battle_debrief"),
        (assign, "$g_mt_mode", vba_normal),
        (change_screen_mission),
        ]),

      ("wait_here",
       [(party_slot_eq, "$current_town", slot_center_has_manor, 1),
        (party_slot_eq, "$current_town", slot_mainplanet_lord, "trp_player"),
        ],
         "Wait here for some time.",
         [
           (assign,"$auto_enter_town","$current_town"),
           (assign, "$g_last_rest_center", "$current_town"),
           (rest_for_hours_interactive, 24 * 7, 5, 1), #rest while attackable
           (change_screen_return),
          ]),
      
      
      ("collect_taxes_qst",[(party_slot_eq, "$current_town", slot_minorplanet_state, 0),
                            (check_quest_active, "qst_collect_taxes"),
                            (quest_get_slot, ":quest_giver_troop", "qst_collect_taxes", slot_quest_giver_troop),
                            (quest_slot_eq, "qst_collect_taxes", slot_quest_target_center, "$current_town"),
                            (neg|quest_slot_eq, "qst_collect_taxes", slot_quest_current_state, 4),
                            (str_store_troop_name, s1, ":quest_giver_troop"),
                            (quest_get_slot, reg5, "qst_collect_taxes", slot_quest_current_state),
                            ], "{reg5?Continue collecting taxes:Collect taxes} due to {s1}.",
       [(jump_to_menu, "mnu_collect_taxes"),]),

      ("train_peasants_against_bandits_qst",
       [
         (party_slot_eq, "$current_town", slot_minorplanet_state, 0),
         (check_quest_active, "qst_train_peasants_against_bandits"),
         (neg|check_quest_concluded, "qst_train_peasants_against_bandits"),
         (quest_slot_eq, "qst_train_peasants_against_bandits", slot_quest_target_center, "$current_town"),
         ], "Train the colonists.",
       [(jump_to_menu, "mnu_train_peasants_against_bandits"),]),

      ("minorplanet_hostile_action",[(party_slot_eq, "$current_town", slot_minorplanet_state, 0),
                                 (neg|party_slot_ge, "$current_town", slot_minorplanet_infested_by_bandits, 1),], "Take a hostile action.",
       [(jump_to_menu,"mnu_minorplanet_hostile_action"),
           ]),
      
      ("show_reports",[(eq, "$cheat_mode", 1),], "CHEAT! Show reports.",
       [(jump_to_menu,"mnu_center_reports"),
           ]),
      ("leave_3dot",[],"Leave...",[(change_screen_return,0)]),
      
    ],
  ),


  (
    "minorplanet_hostile_action",menu_text_color(0xFF000d2c),
    "What action do you have in mind?",
    "none",
    [],
    [
      ("minorplanet_take_food",[
          (party_slot_eq, "$current_town", slot_minorplanet_state, 0),
          (neg|party_slot_ge, "$current_town", slot_minorplanet_infested_by_bandits, 1),
          (party_get_slot, ":merchant_troop", "$current_town", slot_mainplanet_elder),
          (assign, ":town_stores_not_empty", 0),
          (try_for_range, ":slot_no", num_equipment_kinds, max_inventory_items + num_equipment_kinds),
            (troop_get_inventory_slot, ":slot_item", ":merchant_troop", ":slot_no"),
            (ge, ":slot_item", 0),
            (assign, ":town_stores_not_empty", 1),
          (try_end),
          (eq, ":town_stores_not_empty", 1),
          ],"Force the colonists to give you supplies.",
       [
           (jump_to_menu, "mnu_minorplanet_take_food_confirm")
        ]),
      ("minorplanet_steal_cattle",
       [
          (party_slot_eq, "$current_town", slot_minorplanet_state, 0),
          (party_slot_eq, "$current_town", slot_minorplanet_player_can_not_steal_cattle, 0),
          (neg|party_slot_ge, "$current_town", slot_minorplanet_infested_by_bandits, 1),
          (party_get_slot, ":num_cattle", "$current_town", slot_minorplanet_number_of_cattle),
          (neg|party_slot_eq, "$current_town", slot_mainplanet_lord, "trp_player"),
          (gt, ":num_cattle", 0),
		  #SW - modified menu
          ],"Steal nerfs.",
       [
           (jump_to_menu, "mnu_minorplanet_steal_cattle_confirm")
        ]),
      ("minorplanet_loot",[(party_slot_eq, "$current_town", slot_minorplanet_state, 0),
                       (neg|party_slot_ge, "$current_town", slot_minorplanet_infested_by_bandits, 1),
                       (store_faction_of_party, ":center_faction", "$current_town"),
                       (store_relation, ":reln", "fac_player_supporters_faction", ":center_faction"),
                       (lt, ":reln", 0),
                       ],
       "Loot and burn this minor planet.",
       [
#           (party_clear, "$current_town"),
#           (party_add_template, "$current_town", "pt_villagers_in_raid"),
           (jump_to_menu, "mnu_minorplanet_start_attack"),
           ]),
      ("forget_it",[],
      "Forget it.",[(jump_to_menu,"mnu_village")]),
    ],
  ),



# inserted by obi 2009-04-28 --> recruit clones, droids, force sensitives
	(
    "recruit_clones",menu_text_color(0xFF000d2c),
    "{s18}",
    "none",
    [
		(party_get_slot, ":volunteer_amount", "$current_town", slot_center_volunteer_troop_amount),
		(party_get_free_companions_capacity, ":free_capacity", "p_main_party"),
		(try_begin),
			(le, ":volunteer_amount", 0),
			(assign, ":volunteer_amount", 0),
		(try_end),
		(str_store_troop_name_by_count, s3, "trp_clone_trooper_1", ":volunteer_amount"), # add troop id
		(assign, reg7, ":volunteer_amount"),
		(assign, reg8, ":free_capacity"),
		(val_min, ":volunteer_amount", ":free_capacity"),
		(store_troop_gold, ":gold", "trp_player"),
		(store_div, ":gold_capacity", ":gold", 100),#100 denars per man, change to whatever you want
		(assign, reg9, ":gold_capacity"),
		(val_min, ":volunteer_amount", ":gold_capacity"),
		(assign, reg5, ":volunteer_amount"),
		#SW - moved higher up in the code since I am just displaying how many are available in the dialog
		#(str_store_troop_name_by_count, s3, "trp_clone_trooper_1", ":volunteer_amount"), # add troop id
		(try_begin),
			(le, reg5, 0),
			(str_store_string, s18, "@There are currently {reg7} {s3} available.^^You have {reg8} available spots free in your party.^^You have enough credits to hire {reg9} of them.^^^^^Currently you cannot hire any troops."),
		(else_try),
			(str_store_string, s18, "@There are currently {reg7} {s3} available.^^You have {reg8} available spots free in your party.^^You have enough credits to hire {reg9} of them."),
			(store_mul, reg6, ":volunteer_amount", 100),#100 per man, change to whatever you want
		(try_end),
		(set_background_mesh, "mesh_pic_recruits"),
    ],
    [
      ("continue_3dot",		[(le, reg5, 0)],
						"Continue...",	[
						(party_set_slot, "$current_town", slot_center_volunteer_troop_amount, -1),
						(jump_to_menu,"mnu_village")
						]),
      ("recruit_them",	[(gt, reg5, 0)],
						"Recruit {reg5} of them ({reg6} credits).",[
						(call_script, "script_minorplanet_recruit_volunteers_clones"),
						(jump_to_menu,"mnu_village"),
                        ]),
      ("forget_it",		[(gt, reg5, 0)],
						"Forget it.",[
						(jump_to_menu,"mnu_village")
						]),
    ],
  ),
	(
    "recruit_force_sensitives",menu_text_color(0xFF000d2c),
    "{s18}",
    "none",
    [
		(party_get_slot, ":volunteer_amount", "$current_town", slot_center_volunteer_troop_amount),
		(party_get_free_companions_capacity, ":free_capacity", "p_main_party"),
		(try_begin),
			(le, ":volunteer_amount", 0),
			(assign, ":volunteer_amount", 0),
		(try_end),
		#SW - added names for faction specific recruits
		(store_faction_of_party, ":cur_center_faction", "$current_town"),
		(try_begin),
		(eq, ":cur_center_faction", "fac_galacticempire"),	#Galactic Empire
			(str_store_troop_name_by_count, s3, "trp_sith_hopeful", ":volunteer_amount"),
		(else_try),
		(eq, ":cur_center_faction", "fac_rebelalliance"),	#Rebel Alliance
			(str_store_troop_name_by_count, s3, "trp_jedi_hopeful", ":volunteer_amount"),			
		(else_try),	#Hutt Cartel, player faction, etc.
			(str_store_troop_name_by_count, s3, "trp_force_sensitive_recruit", ":volunteer_amount"),		
		(try_end),
		(assign, reg7, ":volunteer_amount"),
		(assign, reg8, ":free_capacity"),
		(val_min, ":volunteer_amount", ":free_capacity"),
		(store_troop_gold, ":gold", "trp_player"),
		(store_div, ":gold_capacity", ":gold", 150),#100 denars per man, change to whatever you want
		(assign, reg9, ":gold_capacity"),
		(val_min, ":volunteer_amount", ":gold_capacity"),
		(assign, reg5, ":volunteer_amount"),			
		
		(try_begin),
			(le, reg5, 0),
			(str_store_string, s18, "@There are currently {reg7} {s3} available.^^You have {reg8} available spots free in your party.^^You have enough credits to hire {reg9} of them.^^^^^Currently you cannot hire any troops."),
		(else_try),
			(str_store_string, s18, "@There are currently {reg7} {s3} available.^^You have {reg8} available spots free in your party.^^You have enough credits to hire {reg9} of them."),
			(store_mul, reg6, ":volunteer_amount", 150),#100 per man, change to whatever you want
		(try_end),
		(set_background_mesh, "mesh_pic_recruits"),
    ],
    [
      ("continue_3dot",		[(le, reg5, 0)],
						"Continue...",	[
						(party_set_slot, "$current_town", slot_center_volunteer_troop_amount, -1),
						(jump_to_menu,"mnu_village")
						]),
      ("recruit_them",	[(gt, reg5, 0)],
						"Recruit {reg5} of them ({reg6} credits).",[
						(call_script, "script_minorplanet_recruit_volunteers_force_sensitives"),
						(jump_to_menu,"mnu_village"),
                        ]),
      ("forget_it",		[(gt, reg5, 0)],
						"Forget it.",[
						(jump_to_menu,"mnu_village")
						]),
    ],
  ),

	(
    "recruit_droids_pre",menu_text_color(0xFF000d2c),
    #"What type of Battle Droids do you want to build?",
	"{s18}",
    "none",
    [
		(party_get_slot, ":volunteer_amount", "$current_town", slot_center_volunteer_troop_amount),
		(try_begin),
			(le, ":volunteer_amount", 0),
			(assign, ":volunteer_amount", 0),
		(try_end),
		(assign, reg5, ":volunteer_amount"),
		(try_begin),
			(le, reg5, 0),
			(str_store_string, s18, "@The Droid Foundry can not currently build any troops, please come back later."),
		(else_try),
			(str_store_string, s18, "@The Droid Foundry can build {reg5} droids.^What type of droids do you want to build?"),
		(try_end),
	],
    [

      ("build_oomseries", [(gt, reg5, 0)],
						"OOM-Series Battle Droids.",[
						(assign, "$g_droid_foundry_type", "trp_oom_series_security"),
						(jump_to_menu,"mnu_recruit_droids"),
                        ]),
		("build_b1series", [(gt, reg5, 0)],
						"B1-Series Battle Droids.",	[
						(assign, "$g_droid_foundry_type", "trp_b1series"),
						(jump_to_menu,"mnu_recruit_droids")
						]),
		("build_b2series", [(gt, reg5, 0)],
						"B2-Series Battle Droids.",[
						(assign, "$g_droid_foundry_type", "trp_b2series"),
						(jump_to_menu,"mnu_recruit_droids"),
                        ]),
      # ("build_egseries", [(gt, reg5, 0)],
						# "EG-Series Power Droids.",[
						# (assign, "$g_droid_foundry_type", "trp_power_droid"),
						# (jump_to_menu,"mnu_recruit_droids"),
                        # ]),
      # ("build_fxseries", [(gt, reg5, 0)],
						# "FX-Series Medical Droids.",[
						# (assign, "$g_droid_foundry_type", "trp_fxseries_droid"),
						# (jump_to_menu,"mnu_recruit_droids"),
                        # ]),
      ("go_back_dot",			[],
						"Go back.",[
						(jump_to_menu,"mnu_village")
						]),
    ],
  ),  
	(
    "recruit_droids",menu_text_color(0xFF000d2c),
    "{s18}",
    "none",
    [
		(party_get_slot, ":volunteer_amount", "$current_town", slot_center_volunteer_troop_amount),
		(party_get_free_companions_capacity, ":free_capacity", "p_main_party"),
		(try_begin),
			(le, ":volunteer_amount", 0),
			(assign, ":volunteer_amount", 0),
		(try_end),
		(str_store_troop_name_by_count, s3, "$g_droid_foundry_type", ":volunteer_amount"), # add troop to droid
		(assign, reg7, ":volunteer_amount"),
		(assign, reg8, ":free_capacity"),
		(val_min, ":volunteer_amount", ":free_capacity"),
		(store_troop_gold, ":gold", "trp_player"),
		(store_div, ":gold_capacity", ":gold", 25),#100 denars per man, change to whatever you want
		(assign, reg9, ":gold_capacity"),
		(val_min, ":volunteer_amount", ":gold_capacity"),
		(assign, reg5, ":volunteer_amount"),
		#SW - moved higher up in the code since I am just displaying how many are available in the dialog
		#(str_store_troop_name_by_count, s3, "trp_b1series", ":volunteer_amount"), # add troop to droid
		(try_begin),
			(le, reg5, 0),
			(str_store_string, s18, "@There are currently {reg7} {s3} available.^^You have {reg8} available spots free in your party.^^You have enough credits to hire {reg9} of them.^^^^^Currently you cannot hire any troops."),
		(else_try),
			(str_store_string, s18, "@There are currently {reg7} {s3} available.^^You have {reg8} available spots free in your party.^^You have enough credits to hire {reg9} of them."),
			(store_mul, reg6, ":volunteer_amount", 25),#100 per man, change to whatever you want
		(try_end),
		(set_background_mesh, "mesh_pic_recruits"),
    ],
    [
      ("continue_3dot",		[(le, reg5, 0)],
						"Continue...",	[
						(party_set_slot, "$current_town", slot_center_volunteer_troop_amount, -1),
						(jump_to_menu,"mnu_village")
						]),
      ("recruit_them",	[(gt, reg5, 0)],
						"Recruit {reg5} of them ({reg6} credits).",[
						(call_script, "script_minorplanet_recruit_volunteers_droids"),
						(jump_to_menu,"mnu_village"),
                        ]),
      ("forget_it",		[(gt, reg5, 0)],
						"Forget it.",[
						(jump_to_menu,"mnu_village")
						]),
    ],
  ),
	(
    "recruit_rancors",menu_text_color(0xFF000d2c),
    "{s18}",
    "none",
    [
		(party_get_slot, ":volunteer_amount", "$current_town", slot_center_volunteer_troop_amount),
		(party_get_free_companions_capacity, ":free_capacity", "p_main_party"),
		(try_begin),
			(le, ":volunteer_amount", 0),
			(assign, ":volunteer_amount", 0),
		(try_end),
		(str_store_troop_name_by_count, s3, "trp_rancor", ":volunteer_amount"), # add troop to rancor
		(assign, reg7, ":volunteer_amount"),
		(assign, reg8, ":free_capacity"),
		(val_min, ":volunteer_amount", ":free_capacity"),
		(store_troop_gold, ":gold", "trp_player"),
		(store_div, ":gold_capacity", ":gold", 100),#100 denars per man, change to whatever you want
		(assign, reg9, ":gold_capacity"),
		(val_min, ":volunteer_amount", ":gold_capacity"),
		(assign, reg5, ":volunteer_amount"),
		#SW - moved higher up in the code since I am just displaying how many are available in the dialog
		#(str_store_troop_name_by_count, s3, "trp_rancor", ":volunteer_amount"), # add troop to rancor
	
		(try_begin),
			(le, reg5, 0),
			(str_store_string, s18, "@There are currently {reg7} {s3} available.^^You have {reg8} available spots free in your party.^^You have enough credits to hire {reg9} of them.^^^^^Currently you cannot hire any troops."),
		(else_try),
			(str_store_string, s18, "@There are currently {reg7} {s3} available.^^You have {reg8} available spots free in your party.^^You have enough credits to hire {reg9} of them."),
			(store_mul, reg6, ":volunteer_amount", 100),#100 per man, change to whatever you want
		(try_end),
		(set_background_mesh, "mesh_pic_rancors"),
    ],
    [
      ("continue_3dot",		[(le, reg5, 0)],
						"Continue...",	[
						(party_set_slot, "$current_town", slot_center_volunteer_troop_amount, -1),
						(jump_to_menu,"mnu_village")
						]),
      ("recruit_them",	[(gt, reg5, 0)],
						"Recruit {reg5} of them ({reg6} credits).",[
						(call_script, "script_minorplanet_recruit_volunteers_rancors"),
						(jump_to_menu,"mnu_village"),
                        ]),
      ("forget_it",		[(gt, reg5, 0)],
						"Forget it.",[
						(jump_to_menu,"mnu_village")
						]),
    ],
  ),  
# end of insert
	(
	#SW - modified recruit_volunteers game menu
    "recruit_volunteers",menu_text_color(0xFF000d2c),
    "{s18}",
    "none",
    [
		#SW - modified to have the recruit based on the tier_1_troop of the faction of the town
		#(party_get_slot, ":volunteer_troop", "$current_town", slot_center_volunteer_troop_type),
		(store_faction_of_party, ":town_faction", "$current_town"),
		(faction_get_slot, ":volunteer_troop", ":town_faction", slot_faction_tier_1_troop),
		(try_begin),
			(le, ":volunteer_troop", 0),
			(assign, ":volunteer_troop", "trp_civilian"),
		(try_end),		
		(party_get_slot, ":volunteer_amount", "$current_town", slot_center_volunteer_troop_amount),
		(party_get_free_companions_capacity, ":free_capacity", "p_main_party"),
		(try_begin),
			(le, ":volunteer_amount", 0),
			(assign, ":volunteer_amount", 0),
		(try_end),
		(str_store_troop_name_by_count, s3, ":volunteer_troop", ":volunteer_amount"),		
		(assign, reg7, ":volunteer_amount"),
		(assign, reg8, ":free_capacity"),
		(val_min, ":volunteer_amount", ":free_capacity"),
		(store_troop_gold, ":gold", "trp_player"),
		(store_div, ":gold_capacity", ":gold", 25),#10 denars per man, change to whatever you want
		(assign, reg9, ":gold_capacity"),
		(val_min, ":volunteer_amount", ":gold_capacity"),
		(assign, reg5, ":volunteer_amount"),
		#SW - moved higher up in the code since I am just displaying how many are available in the dialog
		#(str_store_troop_name_by_count, s3, ":volunteer_troop", ":volunteer_amount"),
		
		#SW - only allow recruits from the player's faction
		# (try_begin),
			# (eq, ":town_faction", "$players_faction"),
			 (try_begin),
				(le, reg5, 0),
				(str_store_string, s18, "@There are currently {reg7} {s3} available.^^You have {reg8} available spots free in your party.^^You have enough credits to hire {reg9} of them.^^^^^Currently you cannot hire any troops."),
			(else_try),
				(str_store_string, s18, "@There are currently {reg7} {s3} available.^^You have {reg8} available spots free in your party.^^You have enough credits to hire {reg9} of them."),
				(store_mul, reg6, ":volunteer_amount", 25),#10 per man, change to whatever you want
			(try_end),
		# (else_try),
			# (assign, reg5, 0),
			# (str_store_string, s18, "@There are currently {reg7} {s3} available.^^You have {reg8} available spots free in your party.^^You have enough credits to hire {reg9} troops.^^^^^You are not part of this planet's faction so you cannot hire any troops."),
		# (try_end),
		
		(set_background_mesh, "mesh_pic_recruits"),
    ],
    [
      ("continue_3dot",		[(le, reg5, 0)],
						"Continue...",	[
						(party_set_slot, "$current_town", slot_center_volunteer_troop_amount, -1),
						(jump_to_menu,"mnu_village")
						]),
      ("recruit_them",	[(gt, reg5, 0)],
						"Recruit {reg5} of them ({reg6} credits).",[
						(call_script, "script_minorplanet_recruit_volunteers_recruit"),
						(jump_to_menu,"mnu_village"),
                        ]),
      ("forget_it",		[(gt, reg5, 0)],
						"Forget it.",[
						(jump_to_menu,"mnu_village")
						]),
    ],
  ),
  (
    "minorplanet_hunt_down_fugitive_defeated",menu_text_color(0xFF000d2c),
    "A heavy blow from the fugitive sends you to the ground, and your vision spins and goes dark.\
 Time passes. When you open your eyes again you find yourself battered and bloody,\
 but luckily none of the wounds appear to be lethal.",
    "none",
    [],
    [
      ("continue_3dot",[],"Continue...",[(jump_to_menu, "mnu_village"),]),
    ],
  ),

  (
    "minorplanet_infest_bandits_result",menu_text_color(0xFF000d2c)|mnf_scale_picture,
    "{s9}",
    "none",
    [(try_begin),
       (eq, "$g_battle_result", 1),
       (jump_to_menu, "mnu_minorplanet_infestation_removed"),
     (else_try),
       (str_store_string, s9, "@Try as you might, you could not defeat the bandits.\
 Infuriated, they raze part of the planet to the ground to punish the colonists,\
 and then leave the burning wasteland behind to find more space to plunder."),
       (set_background_mesh, "mesh_pic_looted_village"),
     (try_end),
    ],
    [
      ("continue_3dot",[],"Continue...",
       [(party_set_slot, "$g_encountered_party", slot_minorplanet_infested_by_bandits, 0),
        (call_script, "script_minorplanet_set_state",  "$current_town", svs_looted),
        (party_set_slot, "$current_town", slot_minorplanet_raid_progress, 0),
        (party_set_slot, "$current_town", slot_minorplanet_recover_progress, 0),
        (try_begin),
          (check_quest_active, "qst_eliminate_bandits_infesting_village"),
          (quest_slot_eq, "qst_eliminate_bandits_infesting_village", slot_quest_target_center, "$g_encountered_party"),
          (call_script, "script_change_player_relation_with_center", "$g_encountered_party", -5),
          (call_script, "script_fail_quest", "qst_eliminate_bandits_infesting_village"),
        (else_try),
          (check_quest_active, "qst_deal_with_bandits_at_lords_village"),
          (quest_slot_eq, "qst_deal_with_bandits_at_lords_village", slot_quest_target_center, "$g_encountered_party"),
          (call_script, "script_change_player_relation_with_center", "$g_encountered_party", -4),
          (call_script, "script_fail_quest", "qst_deal_with_bandits_at_lords_village"),
        (else_try),
          (call_script, "script_change_player_relation_with_center", "$g_encountered_party", -3),
        (try_end),
        (jump_to_menu, "mnu_village"),]),
    ],
  ),


  (
    "minorplanet_infestation_removed",menu_text_color(0xFF000d2c)|mnf_disable_all_keys,
    "In a battle worthy of song, you and your men drive the bandits away from the planet, making it safe once more.\
 The colonistss have little left in the way of wealth after their ordeal,\
 but they offer you all they can find.",
    "none",
    [(party_get_slot, ":bandit_troop", "$g_encountered_party", slot_minorplanet_infested_by_bandits),
     (party_set_slot, "$g_encountered_party", slot_minorplanet_infested_by_bandits, 0),
     (party_clear, "p_temp_party"),
     (party_add_members, "p_temp_party", ":bandit_troop", "$qst_eliminate_bandits_infesting_minorplanet_num_bandits"),
     (assign, "$g_strength_contribution_of_player", 50),
     (call_script, "script_party_give_xp_and_gold", "p_temp_party"),
     (try_begin),
       (check_quest_active, "qst_eliminate_bandits_infesting_village"),
       (quest_slot_eq, "qst_eliminate_bandits_infesting_village", slot_quest_target_center, "$g_encountered_party"),
       (call_script, "script_end_quest", "qst_eliminate_bandits_infesting_village"),
       #Add quest reward
       (call_script, "script_change_player_relation_with_center", "$g_encountered_party", 5),
     (else_try),
       (check_quest_active, "qst_deal_with_bandits_at_lords_village"),
       (quest_slot_eq, "qst_deal_with_bandits_at_lords_village", slot_quest_target_center, "$g_encountered_party"),
       (call_script, "script_succeed_quest", "qst_deal_with_bandits_at_lords_village"),
       (call_script, "script_change_player_relation_with_center", "$g_encountered_party", 3),
     (else_try),
     #Add normal reward
       (call_script, "script_change_player_relation_with_center", "$g_encountered_party", 4),
     (try_end),
   
     (party_get_slot, ":merchant_troop", "$current_town", slot_mainplanet_elder),
     (try_for_range, ":slot_no", num_equipment_kinds ,max_inventory_items + num_equipment_kinds),
        (store_random_in_range, ":rand", 0, 100),
        (lt, ":rand", 70),
        (troop_set_inventory_slot, ":merchant_troop", ":slot_no", -1),
     (try_end),
    ],
    [
      ("minorplanet_bandits_defeated_accept",[],"Take it as your just due.",[(jump_to_menu, "mnu_village"),
                                                                         (party_get_slot, ":merchant_troop", "$current_town", slot_mainplanet_elder),
                                                                         (troop_sort_inventory, ":merchant_troop"),
                                                                         (change_screen_loot, ":merchant_troop"),
                                                                       ]),
      ("minorplanet_bandits_defeated_cont",[],  "Refuse, stating that they need these items more than you do.",[(call_script, "script_change_player_relation_with_center", "$g_encountered_party", 3),
                                                                                                            (jump_to_menu, "mnu_village")]),
    ],
  ),

  (
    "center_manage",menu_text_color(0xFF000d2c),
    "{s19}^{reg6?^^You are\
 currently building {s7}. The building will be completed after {reg8} day{reg9?s:}.:}",
    "none",
    [(assign, ":num_improvements", 0),
     (str_clear, s18),
     (try_begin),
       (party_slot_eq, "$g_encountered_party", slot_party_type, spt_minorplanet),
       (assign, ":begin", minorplanet_improvements_begin),
       (assign, ":end", minorplanet_improvements_end),
       #(str_store_string, s17, "@village"),
	   (str_store_string, s17, "@planet"),
     (else_try),
       (assign, ":begin", walled_center_improvements_begin),
       (assign, ":end", walled_center_improvements_end),
       (party_slot_eq, "$g_encountered_party", slot_party_type, spt_mainplanet),
       #(str_store_string, s17, "@town"),
	   (str_store_string, s17, "@planet"),
     (else_try),
       #(str_store_string, s17, "@castle"),
	   (str_store_string, s17, "@planet"),
     (try_end),
     
     (try_for_range, ":improvement_no", ":begin", ":end"),
       (party_slot_ge, "$g_encountered_party", ":improvement_no", 1),
       (val_add,  ":num_improvements", 1),
       (call_script, "script_get_improvement_details", ":improvement_no"),
       (try_begin),
         (eq,  ":num_improvements", 1),
         (str_store_string, s18, "@{s0}"),
       (else_try),
         (str_store_string, s18, "@{s18}^{s0}"),
       (try_end),
     (try_end),
     
     (try_begin),
       (eq,  ":num_improvements", 0),
       (str_store_string, s19, "@The {s17} has no improvements."),
     (else_try),
       (str_store_string, s19, "@The {s17} has the following improvements:^^{s18}"),
     (try_end),
     
     (assign, reg6, 0),
     (try_begin),
       (party_get_slot, ":cur_improvement", "$g_encountered_party", slot_center_current_improvement),
       (gt, ":cur_improvement", 0),
       (call_script, "script_get_improvement_details", ":cur_improvement"),
       (str_store_string, s7, s0),
       (assign, reg6, 1),
       (store_current_hours, ":cur_hours"),
       (party_get_slot, ":finish_time", "$g_encountered_party", slot_center_improvement_end_hour),
       (val_sub, ":finish_time", ":cur_hours"),
       (store_div, reg8, ":finish_time", 24),
       (val_max, reg8, 1),
       (store_sub, reg9, reg8, 1),
     (try_end),
    ],
    [
# inserted by obi 2009-04-28 --> recruit clones, droids, force sensitives
			("center_build_temple",[(eq, reg6, 0),
                             (party_slot_eq, "$g_encountered_party", slot_party_type, spt_minorplanet),
                             (party_slot_eq, "$g_encountered_party", slot_center_has_temple, 0),
                                  ],
       "Build a Force-Sensitive Temple.",[(assign, "$g_improvement_type", slot_center_has_temple),
                         (jump_to_menu, "mnu_center_improve"),]),
      ("center_build_clone_chambers",[(eq, reg6, 0),
                             (party_slot_eq, "$g_encountered_party", slot_party_type, spt_minorplanet),
                             (party_slot_eq, "$g_encountered_party", slot_center_has_clone_chambers, 0),
                                  ],
       "Build Clone Chambers.",[(assign, "$g_improvement_type", slot_center_has_clone_chambers),
                         (jump_to_menu, "mnu_center_improve"),]),
      ("center_build_droid_foundry",[(eq, reg6, 0),
                             (party_slot_eq, "$g_encountered_party", slot_party_type, spt_minorplanet),
                             (party_slot_eq, "$g_encountered_party", slot_center_has_droid_foundry, 0),
                                  ],
       "Build a Droid Foundry.",[(assign, "$g_improvement_type", slot_center_has_droid_foundry),
                         (jump_to_menu, "mnu_center_improve"),]),
      ("center_build_rancor_pit",[(eq, reg6, 0),
                             (party_slot_eq, "$g_encountered_party", slot_party_type, spt_minorplanet),
                             (party_slot_eq, "$g_encountered_party", slot_center_has_rancor_pit, 0),
                                  ],
       "Build a Rancor Pit.",[(assign, "$g_improvement_type", slot_center_has_rancor_pit),
                         (jump_to_menu, "mnu_center_improve"),]),						 
# end of insert		
      ("center_build_manor",[(eq, reg6, 0),
                             (party_slot_eq, "$g_encountered_party", slot_party_type, spt_minorplanet),
                             (party_slot_eq, "$g_encountered_party", slot_center_has_manor, 0),
                                  ],
       "Build a Palace.",[(assign, "$g_improvement_type", slot_center_has_manor),
                         (jump_to_menu, "mnu_center_improve"),]),
      ("center_build_fish_pond",[(eq, reg6, 0),
                                 (party_slot_eq, "$g_encountered_party", slot_party_type, spt_minorplanet),
                                 (party_slot_eq, "$g_encountered_party", slot_center_has_fish_pond, 0),
                                  ],
       "Build a Industrial Factory.",[(assign, "$g_improvement_type", slot_center_has_fish_pond),
                             (jump_to_menu, "mnu_center_improve"),]),
      ("center_build_watch_tower",[(eq, reg6, 0),
                                   (party_slot_eq, "$g_encountered_party", slot_party_type, spt_minorplanet),
                                   (party_slot_eq, "$g_encountered_party", slot_center_has_watch_tower, 0),
                                  ],
       "Build a Radar Station.",[(assign, "$g_improvement_type", slot_center_has_watch_tower),
                               (jump_to_menu, "mnu_center_improve"),]),
      ("center_build_school",[(eq, reg6, 0),
                              (party_slot_eq, "$g_encountered_party", slot_party_type, spt_minorplanet),
                              (party_slot_eq, "$g_encountered_party", slot_center_has_school, 0),
                                  ],
       "Build a Educational Facility.",[(assign, "$g_improvement_type", slot_center_has_school),
                          (jump_to_menu, "mnu_center_improve"),]),
      ("center_build_messenger_post",[(eq, reg6, 0),
                                      (party_slot_eq, "$g_encountered_party", slot_center_has_messenger_post, 0),
                                       ],
       "Build a Communications Center.",[(assign, "$g_improvement_type", slot_center_has_messenger_post),
                                  (jump_to_menu, "mnu_center_improve"),]),
      ("center_build_prisoner_tower",[(eq, reg6, 0),
                                      (this_or_next|party_slot_eq, "$g_encountered_party", slot_party_type, spt_mainplanet),
                                      (party_slot_eq, "$g_encountered_party", slot_party_type, spt_castle),
                                      (party_slot_eq, "$g_encountered_party", slot_center_has_prisoner_tower, 0),
                                       ],
       "Build a Prison Tower.",[(assign, "$g_improvement_type", slot_center_has_prisoner_tower),
                                  (jump_to_menu, "mnu_center_improve"),]),
                           
      ("go_back_dot",[],"Go back.",[(jump_to_menu, "$g_next_menu")]),
    ],
  ),

  (
    "center_improve",menu_text_color(0xFF000d2c),
    "{s19} As the party member with the highest engineer skill ({reg2}), {reg3?you reckon:{s3} reckons} that building the {s4} will cost you\
 {reg5} credits and will take {reg6} days.",
    "none",
    [(call_script, "script_get_improvement_details", "$g_improvement_type"),
     (assign, ":improvement_cost", reg0),
     (str_store_string, s4, s0),
     (str_store_string, s19, s1),
     (call_script, "script_get_max_skill_of_player_party", "skl_engineer"),
     (assign, ":max_skill", reg0),
     (assign, ":max_skill_owner", reg1),
     (assign, reg2, ":max_skill"),

     (store_sub, ":multiplier", 20, ":max_skill"),
     (val_mul, ":improvement_cost", ":multiplier"),
     (val_div, ":improvement_cost", 20),
     
     (store_div, ":improvement_time", ":improvement_cost", 100),
     (val_add, ":improvement_time", 3),

     (assign, reg5, ":improvement_cost"),
	 #SW - try to reduce improvement_time by half
	 (val_div, ":improvement_time", 2),	 	 
     (assign, reg6, ":improvement_time"),

     (try_begin),
       (eq, ":max_skill_owner", "trp_player"),
       (assign, reg3, 1),
     (else_try),
       (assign, reg3, 0),
       (str_store_troop_name, s3, ":max_skill_owner"),
     (try_end),
    ],
    [
      ("go_on",[(store_troop_gold, ":cur_gold", "trp_player"),
                       (ge, ":cur_gold", reg5)],
       "Go on.", [(troop_remove_gold, "trp_player", reg5),
                  (party_set_slot, "$g_encountered_party", slot_center_current_improvement, "$g_improvement_type"),
                  (store_current_hours, ":cur_hours"),
                  (store_mul, ":hours_takes", reg6, 24),
                  (val_add, ":hours_takes", ":cur_hours"),
                  (party_set_slot, "$g_encountered_party", slot_center_improvement_end_hour, ":hours_takes"),
                  (jump_to_menu,"mnu_center_manage"),
                  ]),
      ("forget_it",[(store_troop_gold, ":cur_gold", "trp_player"),
                    (ge, ":cur_gold", reg5)],
       "Forget it.", [(jump_to_menu,"mnu_center_manage")]),
      ("improve_not_enough_gold",[(store_troop_gold, ":cur_gold", "trp_player"),
                                  (lt, ":cur_gold", reg5)],
       "I don't have enough money for that.", [(jump_to_menu, "mnu_center_manage"),]),
    ],
  ),

  (
    "town_bandits_failed",menu_text_color(0xFF000d2c)|mnf_disable_all_keys,
    "{s4} {s5}",
    "none",
    [
#      (call_script, "script_loot_player_items", 0),
      (store_troop_gold, ":total_gold", "trp_player"),
      (store_div, ":gold_loss", ":total_gold", 30),
      (store_random_in_range, ":random_loss", 40, 100),
      (val_add, ":gold_loss", ":random_loss"),
      (val_min, ":gold_loss", ":total_gold"),
      (troop_remove_gold, "trp_player",":gold_loss"),
      (party_set_slot, "$current_town", slot_center_has_bandits, 0),
      (party_get_num_companions, ":num_companions", "p_main_party"),
      (str_store_string, s4, "@The assasins beat you down and leave you for dead. ."),
      (str_store_string, s4, "@You have fallen. The bandits quickly search your body for every coin they can find,\
 then vanish into the night. They have left you alive, if only barely."),
      (try_begin),
        (gt, ":num_companions", 2),
        (str_store_string, s5, "@Luckily some of your companions come to search for you when you do not return, and find you lying by the side of the road. They hurry you to safety and dress your wounds."),
      (else_try),
        (str_store_string, s5, "@Luckily some passing people find you lying by the side of the road, and recognise you as something other than a simple beggar. They carry you to the nearest inn and dress your wounds."),
      (try_end),
    ],
    [
      ("continue_3dot",[],"Continue...",[(change_screen_return)]),
    ],
  ),

  (
    "town_bandits_succeeded",menu_text_color(0xFF000d2c)|mnf_disable_all_keys,
    "The bandits fall before you as wheat to a scythe! Soon you stand alone in the streets\
 while most of your attackers lie unconscious, dead or dying.\
 Searching the bodies, you find a datacard which must have belonged to a previous victim of these brutes.\
 Or perhaps, it was given to them by someone who wanted to arrange a suitable ending to your life.",
    "none",
    [
      (party_set_slot, "$current_town", slot_center_has_bandits, 0),
      (assign, "$g_last_defeated_bandits_town", "$g_encountered_party"),
      (try_begin),
        (check_quest_active, "qst_deal_with_night_bandits"),
        (neg|check_quest_succeeded, "qst_deal_with_night_bandits"),
        (quest_slot_eq, "qst_deal_with_night_bandits", slot_quest_target_center, "$g_encountered_party"),
        (call_script, "script_succeed_quest", "qst_deal_with_night_bandits"),
      (try_end),
      (store_mul, ":xp_reward", "$num_center_bandits", 117),
      (add_xp_to_troop, ":xp_reward", "trp_player"),
      (store_mul, ":gold_reward", "$num_center_bandits", 50),
      (call_script, "script_troop_add_gold","trp_player",":gold_reward"),
    ],
    [
      ("continue_3dot",[],"Continue...",[(change_screen_return)]),
    ],
  ),

  
   (
    "minorplanet_steal_cattle_confirm",menu_text_color(0xFF000d2c),
    "As the party member with the highest looting skill ({reg2}), {reg3?you reckon:{s1} reckons} that you can steal as many as {reg4} nerfs from the colonists' herds.",
    "none",
    [
      (call_script, "script_get_max_skill_of_player_party", "skl_looting"),
      (assign, reg2, reg0),
      (assign, ":max_skill_owner", reg1),
      (try_begin),
        (eq, ":max_skill_owner", "trp_player"),
        (assign, reg3, 1),
      (else_try),
        (assign, reg3, 0),
        (str_store_troop_name, s1, ":max_skill_owner"),
      (try_end),
      (call_script, "script_calculate_amount_of_cattle_can_be_stolen", "$current_town"),
      (assign, reg4, reg0),
      ],
    [
      ("go_on",[],"Go on.",
       [
         (rest_for_hours_interactive, 3, 5, 1), #rest while attackable
         (assign, "$auto_menu", "mnu_minorplanet_steal_cattle"),
         (change_screen_return),
         ]),
      ("forget_it",[],"Forget it.",[(change_screen_return)]),
    ],
  ),

  (
    "minorplanet_steal_cattle",menu_text_color(0xFF000d2c)|mnf_disable_all_keys,
    "{s1}",
    "none",
    [
      (call_script, "script_calculate_amount_of_cattle_can_be_stolen", "$current_town"),
      (assign, ":max_value", reg0),
      (val_add, ":max_value", 1),
      (store_random_in_range, ":random_value", 0, ":max_value"),
      (party_set_slot, "$current_town", slot_minorplanet_player_can_not_steal_cattle, 1),
      (party_get_slot, ":lord", "$current_town", slot_mainplanet_lord),
      (try_begin),
        (le, ":random_value", 0),
        (call_script, "script_change_player_relation_with_center", "$current_town", -3),
        (str_store_string, s1, "@You fail to steal any nerfs."),
      (else_try),
        (assign, reg17, ":random_value"),
        (store_sub, reg12, ":random_value", 1),
        (try_begin),
          (gt, ":lord", 0),
          (call_script, "script_change_player_relation_with_troop", ":lord", -3),
        (try_end),
        (call_script, "script_change_player_relation_with_center", "$current_town", -5),
        (str_store_string, s1, "@You drive away {reg17} nerfs from the village's herd."),
        (call_script, "script_create_cattle_herd", "$current_town", ":random_value"),
        (party_get_slot, ":num_cattle", "$current_town", slot_minorplanet_number_of_cattle),
        (val_sub, ":num_cattle", ":random_value"),
        (party_set_slot, "$current_town", slot_minorplanet_number_of_cattle, ":num_cattle"),
      (try_end),
    ],
    [
      ("continue_3dot",[],"Continue...",
       [
         (change_screen_return),
         ]),
    ],
  ),
  

   (
    "minorplanet_take_food_confirm",menu_text_color(0xFF000d2c),
    "It will be difficult to force and threaten the colonists into giving their precious supplies. You think you will need at least one hour.",
    #TODO: mention looting skill?
    "none",
    [],
    [
      ("go_ahead",[],"Go ahead.",
       [
         (rest_for_hours_interactive, 1, 5, 0), #rest while not attackable
         (assign, "$auto_enter_town", "$current_town"),
         (assign, "$g_town_visit_after_rest", 1),
         (assign, "$auto_enter_menu_in_center", "mnu_minorplanet_take_food"),
         (change_screen_return),
         ]),
      ("forget_it",[],"Forget it.",[(jump_to_menu, "mnu_minorplanet_hostile_action")]),
    ],
  ),

  (
    "minorplanet_take_food",menu_text_color(0xFF000d2c),
    "The colonists grudgingly bring out what they have for you.",
    "none",
    [
       (call_script, "script_party_count_members_with_full_health","p_main_party"),
       (assign, ":player_party_size", reg(0)),
       (call_script, "script_party_count_members_with_full_health","$current_town"),
       (assign, ":villagers_party_size", reg(0)),
       (try_begin),
         (lt, ":player_party_size", 6),
         (ge, ":villagers_party_size", 40),
         (neg|party_slot_eq, "$current_town", slot_mainplanet_lord, "trp_player"),
         (jump_to_menu, "mnu_minorplanet_start_attack"),
       (try_end),
    ],
    [
      ("take_supplies",[],"Take the supplies.",
       [
         (try_begin),
           (party_slot_ge, "$current_town", slot_center_player_relation, -55),
           (try_begin),
             (party_slot_eq, "$current_town", slot_mainplanet_lord, "trp_player"),
             (call_script, "script_change_player_relation_with_center", "$current_town", -1),
           (else_try),
             (call_script, "script_change_player_relation_with_center", "$current_town", -3),
           (try_end),
         (try_end),
         (party_get_slot, ":minorplanet_lord", "$current_town", slot_mainplanet_lord),
         (try_begin),
           (gt,  ":minorplanet_lord", 1),
          (call_script, "script_change_player_relation_with_troop", ":minorplanet_lord", -1),
          (try_end),
         (party_get_slot, ":merchant_troop", "$current_town", slot_mainplanet_elder),
         (party_get_skill_level, ":player_party_looting", "p_main_party", "skl_looting"),
         (val_mul, ":player_party_looting", 3),
         (store_sub, ":random_chance", 70, ":player_party_looting"), #Increases the chance of looting by 3% per skill level
         (try_for_range, ":slot_no", num_equipment_kinds ,max_inventory_items + num_equipment_kinds),
           (store_random_in_range, ":rand", 0, 100), 
           (lt, ":rand", ":random_chance"),
           (troop_set_inventory_slot, ":merchant_troop", ":slot_no", -1),
         (try_end),

###NPC companion changes begin
         (call_script, "script_objectionable_action", tmt_humanitarian, "str_steal_from_villagers"),
#NPC companion changes end
#Troop commentary changes begin
#          (store_faction_of_party,":minorplanet_faction",  "$current_town"),
          (call_script, "script_add_log_entry", logent_minorplanet_extorted, "trp_player",  "$current_town", -1, -1),
#Troop commentary changes end          

         (jump_to_menu, "mnu_village"),
         (troop_sort_inventory, ":merchant_troop"),
         (change_screen_loot, ":merchant_troop"),       
         ]),
      ("let_them_keep_it",[],"Let them keep it.",[(jump_to_menu, "mnu_village")]),
    ],
  ),


  (
    "minorplanet_start_attack",menu_text_color(0xFF000d2c)|mnf_disable_all_keys,
    "Some of the angry colonists grab their tools and prepare to resist you.\
 It looks like you'll have a fight on your hands if you continue.",
    "none",
    [
       (call_script, "script_party_count_members_with_full_health","p_main_party"),
       (assign, ":player_party_size", reg(0)),
       (call_script, "script_party_count_members_with_full_health","$current_town"),
       (assign, ":villagers_party_size", reg(0)),
       
       (try_begin),
         (gt, ":player_party_size", 25),
         (jump_to_menu, "mnu_minorplanet_loot_no_resist"),
       (else_try),
         (this_or_next|eq, ":villagers_party_size", 0),
         (eq, "$g_battle_result", 1),
         (try_begin),
           (eq, "$g_battle_result", 1),
           (store_random_in_range, ":enmity", -30, -15),
           (call_script, "script_change_player_relation_with_center", "$current_town", ":enmity"),
           (party_get_slot, ":town_lord", "$current_town", slot_mainplanet_lord),
           (gt, ":town_lord", 0),
           (call_script, "script_change_player_relation_with_troop", ":town_lord", -3),
         (try_end),
         (jump_to_menu, "mnu_minorplanet_loot_no_resist"),
       (else_try),
         (eq, "$g_battle_result", -1),
         (jump_to_menu, "mnu_minorplanet_loot_defeat"),
       (try_end),
    ],
    [
      ("minorplanet_raid_attack",[],"Charge them.",[
          (store_random_in_range, ":enmity", -10, -5),
          (call_script, "script_change_player_relation_with_center", "$current_town", ":enmity"),
          (try_begin),
            (party_get_slot, ":town_lord", "$current_town", slot_mainplanet_lord),
            (gt, ":town_lord", 0),
            (call_script, "script_change_player_relation_with_troop", ":town_lord", -3),
          (try_end),
          (call_script, "script_calculate_battle_advantage"),
          (set_battle_advantage, reg0),
          (set_party_battle_mode),
          (assign, "$g_battle_result", 0),
          (assign, "$g_minorplanet_raid_evil", 1),
          (set_jump_mission,"mt_minorplanet_raid"),
          (party_get_slot, ":scene_to_use", "$current_town", slot_spacestation_exterior),
          (jump_to_scene, ":scene_to_use"),
          (assign, "$g_next_menu", "mnu_minorplanet_start_attack"),

###NPC companion changes begin
           (call_script, "script_objectionable_action", tmt_humanitarian, "str_loot_village"),
#NPC companion changes end

          (jump_to_menu, "mnu_battle_debrief"),
          (change_screen_mission),
          ]),
      ("minorplanet_raid_leave",[],"Leave this planet alone.",[(change_screen_return)]),
    ],
  ),
  
  (
    "minorplanet_loot_no_resist",menu_text_color(0xFF000d2c),
    "The colonists here are few and frightened, and they quickly scatter and run before you, dropping cheap blaster pistols as they go.\
 The planet is at your mercy.",
    "none",
    [],
    [
      ("minorplanet_plunder",[], "Plunder the planet, then raze it.",
       [
          (call_script, "script_minorplanet_set_state", "$current_town", svs_being_raided),
          (party_set_slot, "$current_town", slot_minorplanet_raided_by, "p_main_party"),
          (assign,"$g_player_raiding_village","$current_town"),
          (rest_for_hours, 3, 5, 1), #rest while attackable (3 hours will be extended by the trigger)
          (change_screen_return),
           ]),
      ("minorplanet_raid_leave",[],"Leave this planet alone.",[(change_screen_return)]),
    ],
  ),
  (
    "minorplanet_loot_complete",menu_text_color(0xFF000d2c)|mnf_disable_all_keys,
    "On your orders your troops sack the planet, pillaging everything of any value,\
 Before destroying any trace of life in your way some valuables are found, you get your share of {reg1} credits.",
    "none",
    [
        (party_get_slot, ":minorplanet_lord", "$current_town", slot_mainplanet_lord),
        (try_begin),
          (gt,  ":minorplanet_lord", 0),
          (call_script, "script_change_player_relation_with_troop", ":minorplanet_lord", -5),
        (try_end),
        (store_random_in_range, ":enmity", -40, -20),
        (call_script, "script_change_player_relation_with_center", "$current_town", ":enmity"),

        (store_faction_of_party, ":minorplanet_faction", "$current_town"),
        (store_relation, ":relation", ":minorplanet_faction", "fac_player_supporters_faction"),
        (try_begin),
          (lt, ":relation", 0),
          (call_script, "script_change_player_relation_with_faction", ":minorplanet_faction", -3),
        (try_end),
        (store_random_in_range, ":morale_increase", 10, 20),
        (call_script, "script_change_player_party_morale", ":morale_increase"),
        (store_random_in_range, reg1, 100, 500),
        (call_script, "script_troop_add_gold", "trp_player", reg1),
#NPC companion changes begin
        (call_script, "script_objectionable_action", tmt_humanitarian, "str_loot_village"),
#NPC companion changes end
      ],
    [
      ("continue_3dot",[], "Continue...",
       [
          (jump_to_menu, "mnu_close"),
          (call_script, "script_calculate_amount_of_cattle_can_be_stolen", "$current_town"),
          (assign, ":max_cattle", reg0),
          (val_mul, ":max_cattle", 3),
          (val_div, ":max_cattle", 2),
          (party_get_slot, ":num_cattle", "$current_town", slot_minorplanet_number_of_cattle),
          (val_min, ":max_cattle", ":num_cattle"),
          (val_add, ":max_cattle", 1),
          (store_random_in_range, ":random_value", 0, ":max_cattle"),
          (try_begin),
            (gt, ":random_value", 0),
            (call_script, "script_create_cattle_herd", "$current_town", ":random_value"),
            (val_sub, ":num_cattle", ":random_value"),
            (party_set_slot, "$current_town", slot_minorplanet_number_of_cattle, ":num_cattle"),
          (try_end),
          (troop_clear_inventory, "trp_temp_troop"),
          (reset_item_probabilities,100),
          (troop_add_merchandise,"trp_temp_troop",itp_type_goods,45),
          (troop_sort_inventory, "trp_temp_troop"),
          (change_screen_loot, "trp_temp_troop"),
        ]),
    ],
  ),
  (
    "minorplanet_loot_defeat",menu_text_color(0xFF000d2c),
    "Fighting with courage and determination, the planet inhabitants manage to hold together and drive off your forces.",
    "none",
    [],
    [
      ("continue_3dot",[],"Continue...",[(change_screen_return)]),
    ],
  ),
  
  (
    "minorplanet_loot_continue",menu_text_color(0xFF000d2c),
    "Do you wish to continue looting this planet?",
    "none",
    [],
    [
      ("yes_dot",[],"Yes.",[ (rest_for_hours, 3, 5, 1), #rest while attackable (3 hours will be extended by the trigger)
                              (change_screen_return),
                              ]),
      ("no_dot",[],"No.",[(call_script, "script_minorplanet_set_state", "$current_town", 0),
                            (party_set_slot, "$current_town", slot_minorplanet_raided_by, -1),
                            (assign, "$g_player_raiding_village", 0),
                            (change_screen_return)]),
    ],
  ),
  
  (
    "close",menu_text_color(0xFF000d2c),
    "Nothing.",
    "none",
    [
        (change_screen_return),
      ],
    [],
  ),
  
  (
    "center_tax",menu_text_color(0xFF000d2c)|mnf_disable_all_keys,
    #"You receive the accumulated rents and taxes of this fief, amounting to {reg1} credits.",
	"You receive the accumulated rents and taxes of all your planets, amounting to {reg1} credits.",
    "none",
    [
        # (str_clear, s3),
        # (try_begin),
          # (party_slot_eq, "$current_town", slot_mainplanet_lord, "trp_player"),
          # (party_get_slot, ":accumulated_rents", "$current_town", slot_center_accumulated_rents),
          # (party_get_slot, ":accumulated_tariffs", "$current_town", slot_center_accumulated_tariffs),
          # (store_add, ":total_tax", ":accumulated_rents", ":accumulated_tariffs"),
          # (assign, reg1, ":total_tax"),
          # (call_script, "script_troop_add_gold", "trp_player", ":total_tax"),
          # (party_set_slot, "$current_town", slot_center_accumulated_rents, 0),
          # (party_set_slot, "$current_town", slot_center_accumulated_tariffs, 0),
        # (try_end),

		#SW - added TheMageLord One Stop Tax Collection Mod
        (str_clear, s3),
        (assign, ":total_tax", 0),
        (try_for_range, ":center_no", centers_begin, centers_end),
          (party_slot_eq, ":center_no", slot_mainplanet_lord, "trp_player"),
          (party_get_slot, ":accumulated_rents", ":center_no", slot_center_accumulated_rents),
          (party_get_slot, ":accumulated_tariffs", ":center_no", slot_center_accumulated_tariffs),
          (val_add, ":total_tax", ":accumulated_rents"),
          (val_add, ":total_tax", ":accumulated_tariffs"),
          (party_set_slot, ":center_no", slot_center_accumulated_rents, 0),
          (party_set_slot, ":center_no", slot_center_accumulated_tariffs, 0),
        (try_end),
        (assign, reg1, ":total_tax"),
        (call_script, "script_troop_add_gold", "trp_player", ":total_tax"),		
      ],
    [
      ("continue_3dot",[], "Continue...",
       [
           (try_begin),
             (party_slot_eq, "$current_town", slot_party_type, spt_minorplanet),
             (jump_to_menu, "mnu_village"),
           (else_try),
             (jump_to_menu, "mnu_town"),
           (try_end),
        ]),
    ],
  ),

  (
    "town",menu_text_color(0xFF000d2c)|mnf_enable_hot_keys,
    "{s10}{s11}{s12}{s13}",
    "none",
    [
		#SW - display a new menu background
		(call_script, "script_display_fullscreen_background", "$current_town"),	
		
        (try_begin),
          (eq, "$sneaked_into_town", 1),
          (call_script, "script_music_set_situation_with_culture", mtf_sit_town_infiltrate),
        (else_try),
          (call_script, "script_music_set_situation_with_culture", mtf_sit_travel),
        (try_end),
        (store_encountered_party,"$current_town"),
        (call_script, "script_update_center_recon_notes", "$current_town"),
        (assign, "$g_defending_against_siege", 0),
        (str_clear, s3),
        (party_get_battle_opponent, ":besieger_party", "$current_town"),
        (store_faction_of_party, ":encountered_faction", "$g_encountered_party"),
        (store_relation, ":faction_relation", ":encountered_faction", "fac_player_supporters_faction"),
        (try_begin),
          (gt, ":besieger_party", 0),
          (ge, ":faction_relation", 0),
          (store_faction_of_party, ":besieger_party_faction", ":besieger_party"),
          (store_relation, ":besieger_party_relation", ":besieger_party_faction", "fac_player_supporters_faction"),
          (lt, ":besieger_party_relation", 0),
          (assign, "$g_defending_against_siege", 1),
          (assign, "$g_siege_first_encounter", 1),
          (jump_to_menu, "mnu_siege_started_defender"),
        (try_end),

        #Quest menus
        
        (assign, "$qst_collect_taxes_currently_collecting", 0),
        
        (try_begin),
          (gt, "$quest_auto_menu", 0),
          (jump_to_menu, "$quest_auto_menu"),
          (assign, "$quest_auto_menu", 0),
        (try_end),

        (try_begin),
##          (eq, "$g_center_under_siege_battle", 1),
##          (jump_to_menu,"mnu_siege_started_defender"),
##        (else_try),
          (eq, "$g_town_assess_trade_goods_after_rest", 1),
          (assign, "$g_town_assess_trade_goods_after_rest", 0),
          (jump_to_menu,"mnu_town_trade_assessment"),
        (try_end),

        (assign, "$talk_context", 0),
        (assign,"$all_doors_locked",0),

        (try_begin),
          (eq, "$g_town_visit_after_rest", 1),
          (assign, "$g_town_visit_after_rest", 0),
          (assign, "$town_entered", 1),
        (try_end),

        (try_begin),
          (eq,"$g_leave_town",1),
          (assign,"$g_leave_town",0),
          (assign,"$g_permitted_to_center",0),
          (leave_encounter),
          (change_screen_return),
        (try_end),

        # #Adding tax to player if player is the owner of the town or castle
        # (try_begin),
          # (party_slot_eq, "$current_town", slot_mainplanet_lord, "trp_player"),
          # (party_get_slot, ":accumulated_rents", "$current_town", slot_center_accumulated_rents),
          # (gt, ":accumulated_rents", 0),
          # (jump_to_menu, "mnu_center_tax"),
        # (try_end),
        

        (str_store_party_name,s2, "$current_town"),
        (party_get_slot, ":center_lord", "$current_town", slot_mainplanet_lord),
        (store_faction_of_party, ":center_faction", "$current_town"),
        (str_store_faction_name,s9,":center_faction"),
        (try_begin),
          (ge, ":center_lord", 0),
          (str_store_troop_name,s8,":center_lord"),
          (str_store_string,s7,"@{s8} of {s9}"),
        (try_end),
        
        (try_begin),
          (party_slot_eq,"$current_town",slot_party_type, spt_mainplanet),
          (str_store_string, s60, s2),
          (party_get_slot, ":prosperity", "$current_town", slot_mainplanet_prosperity),
          (val_add, ":prosperity", 5),
          (store_div, ":str_offset", ":prosperity", 10),
          (store_add, ":str_id", "str_town_prosperity_0",  ":str_offset"),
          (str_store_string, s10, ":str_id"),
        (else_try),
          (str_store_string,s10,"@You are at {s2}."),
        (try_end),
        
        (try_begin),
          (party_slot_eq,"$current_town",slot_party_type, spt_castle),
          (try_begin),
            (eq, ":center_lord", "trp_player"),
            (str_store_string,s11,"@ Your own banner flies over the entrance."),
          (else_try),
            (ge, ":center_lord", 0),
            (str_store_string,s11,"@ You see the banner of {s7} over the entrance."),
          (else_try),
            (str_store_string,s11,"@ This planet seems to belong to no one."),
          (try_end),
        (else_try),
          (try_begin),
            (eq, ":center_lord", "trp_player"),
            (str_store_string,s11,"@ Your own banner flies over the entrance."),
          (else_try),
            (ge, ":center_lord", 0),
            (str_store_string,s11,"@ You see the banner of {s7} over the entrance."),
          (else_try),
            (str_store_string,s11,"@ The citizens here have declared their independence."),
          (try_end),
        (try_end),

        (str_clear, s12),
        (try_begin),
          (party_slot_eq,"$current_town",slot_party_type, spt_mainplanet),
          (party_get_slot, ":center_relation", "$current_town", slot_center_player_relation),
          (call_script, "script_describe_center_relation_to_s3", ":center_relation"),
          (assign, reg9, ":center_relation"),
          (str_store_string, s12, "@ {s3} ({reg9})."),
        (try_end),

        (str_clear, s13),
        (try_begin), 
          (gt,"$entry_to_town_forbidden",0),
          (str_store_string, s13, "@ You have successfully sneaked in."),
        (try_end),

        #forbidden to enter?
        (try_begin), 
          (store_time_of_day,reg(12)),
          (ge,reg(12),5),
          (lt,reg(12),21),
          (assign,"$town_nighttime",0),
        (else_try),
          (assign,"$town_nighttime",1),
          (party_slot_eq,"$current_town",slot_party_type, spt_mainplanet),
          (str_store_string, s13, "str_town_nighttime"),
        (try_end),

        (try_begin),
          (party_slot_ge, "$current_town", slot_mainplanet_has_tournament, 1),
          (neg|is_currently_night),
          (party_set_slot, "$current_town", slot_mainplanet_has_tournament, 1),
          (str_store_string, s13, "@{s13} A tournament will be held here soon."),
        (try_end),

        (assign,"$spacestation_undefended",0),
        (party_get_num_companions, ":spacestation_garrison_size", "p_collective_enemy"),
        (try_begin),
          (eq,":spacestation_garrison_size",0),
          (assign,"$spacestation_undefended",1),
        (try_end),
        ],
    [
      ("main_hall",[(party_slot_eq,"$current_town",slot_party_type, spt_castle)],"Go to the main hall.",
       [
           (try_begin),
             (eq,"$all_doors_locked",1),
             (display_message,"str_door_locked",0xFFFFAAAA),
           (else_try),
             (assign, "$town_entered", 1),
             (call_script, "script_enter_court", "$current_town"),
           (try_end),
        ], "Door to the main hall."),
      
      ("join_tournament", [(neg|is_currently_night),(party_slot_ge, "$current_town", slot_mainplanet_has_tournament, 1),]
       ,"Join the tournament.",
       [
           (call_script, "script_fill_tournament_participants_troop", "$current_town", 1),
           (assign, "$g_tournament_cur_tier", 0),
           (assign, "$g_tournament_player_team_won", -1),
           (assign, "$g_tournament_bet_placed", 0),
           (assign, "$g_tournament_bet_win_amount", 0),
           (assign, "$g_tournament_last_bet_tier", -1),
           (assign, "$g_tournament_next_num_teams", 0),
           (assign, "$g_tournament_next_team_size", 0),
           (jump_to_menu, "mnu_town_tournament"),
        ]),
      
      ("main_hall",[
          (party_slot_eq,"$current_town",slot_party_type, spt_mainplanet),
          (eq,"$entry_to_town_forbidden",0),
#          (party_get_slot, ":spacestation_scene", "$current_town", slot_mainplanet_castle),
#          (scene_slot_ge, ":spacestation_scene", slot_scene_visited, 1), #check if scene has been visited before to allow entry from menu. Otherwise scene will only be accessible from the town center.
          ],"Go to the main hall.",
       [
           (try_begin),
             (this_or_next|eq, "$all_doors_locked", 1),
             (eq, "$sneaked_into_town", 1),
             (display_message,"str_door_locked",0xFFFFAAAA),
           (else_try),
#             (party_get_slot, ":spacestation_scene", "$current_town", slot_mainplanet_castle),
#             (scene_slot_eq, ":spacestation_scene", slot_scene_visited, 0),
#             (display_message,"str_door_locked",0xFFFFAAAA),
#           (else_try),
             (assign, "$town_entered", 1),
             (call_script, "script_enter_court", "$current_town"),
           (try_end),
        ], "Door to the main hall."),
      
      ("land_surface",[
          (party_slot_eq,"$current_town",slot_party_type, spt_mainplanet),
          (this_or_next|eq,"$entry_to_town_forbidden",0),
          (eq, "$sneaked_into_town",1)]
       #,"Take a walk around the streets.",
	   ,"Land on the planet surface.",
       [
		   (assign, "$talk_context", 0),
		   
		   (assign, "$g_init_fight", 0),
		   (assign, "$tavern_brawl", 0),
		   
		   #autoloot flag to allow player to talk to companions
		   (assign, "$g_camp_talk",1),		#must switch back to 0 in the leave game menu		   
		   
           (try_begin),
             (call_script, "script_cf_enter_center_location_bandit_check"),
           (else_try),
             (party_get_slot, ":town_scene", "$current_town", slot_mainplanet_center),
             (modify_visitors_at_site, ":town_scene"),
             (reset_visitors),
             (assign, "$g_mt_mode", tcm_default),
             (store_faction_of_party, ":town_faction","$current_town"),
             (try_begin),
				#SW - commented out below line for fac_player_supporters_faction
               #(neq, ":town_faction", "fac_player_supporters_faction"),
			   #SW - modified how the faction is determined
               #(faction_get_slot, ":troop_prison_guard", "$g_encountered_party_faction", slot_faction_prison_guard_troop),
			   (faction_get_slot, ":troop_prison_guard", ":town_faction", slot_faction_prison_guard_troop),
			   
			   (try_begin),	#SW - added code incase there is no faction slot (ie. player faction)
			     (le,":troop_prison_guard", 0),
				 (assign,":troop_prison_guard","trp_bodyguard"),
			   (try_end),
			   #SW - modified how the faction is determined
               #(faction_get_slot, ":troop_spacestation_guard", "$g_encountered_party_faction", slot_faction_spacestation_guard_troop),
			   (faction_get_slot, ":troop_spacestation_guard", ":town_faction", slot_faction_spacestation_guard_troop),
			   (try_begin),	#SW - added code incase there is no faction slot (ie. player faction)
			     (le,":troop_spacestation_guard", 0),
				 (assign,":troop_spacestation_guard","trp_bodyguard"),
			   (try_end),			   
               (set_visitor, 23, ":troop_spacestation_guard"),
               (set_visitor, 24, ":troop_prison_guard"),
             (try_end),
             (faction_get_slot, ":tier_2_troop", ":town_faction", slot_faction_tier_2_troop),
             (faction_get_slot, ":tier_3_troop", ":town_faction", slot_faction_tier_3_troop),

             (try_begin),
               (gt,":tier_2_troop", 0),
               (assign,reg(0),":tier_3_troop"),
               (assign,reg(1),":tier_3_troop"),
               (assign,reg(2),":tier_2_troop"),
               (assign,reg(3),":tier_2_troop"),
             (else_try),
               (assign,reg(0),"trp_security_guard"),
               (assign,reg(1),"trp_security_guard"),
               (assign,reg(2),"trp_security_guard"),
               (assign,reg(3),"trp_security_guard"),
             (try_end),
             (shuffle_range,0,4),
             (set_visitor,25,reg(0)),
             (set_visitor,26,reg(1)),
             (set_visitor,27,reg(2)),
             (set_visitor,28,reg(3)),

             (party_get_slot, ":spawned_troop", "$current_town", slot_mainplanet_armorer),
             (set_visitor, 9, ":spawned_troop"),
             (party_get_slot, ":spawned_troop", "$current_town", slot_mainplanet_weaponsmith),
             (set_visitor, 10, ":spawned_troop"),
             (party_get_slot, ":spawned_troop", "$current_town", slot_mainplanet_elder),
             (set_visitor, 11, ":spawned_troop"),
             (party_get_slot, ":spawned_troop", "$current_town", slot_mainplanet_horse_merchant),
             (set_visitor, 12, ":spawned_troop"),
			 
             (call_script, "script_init_town_walkers"),
             (set_jump_mission,"mt_town_center"),
             (assign, ":override_state", af_override_horse),
             (try_begin),
               (eq, "$sneaked_into_town", 1), #setup disguise
               (assign, ":override_state", af_override_all),
			 (else_try),
				 #SW - testing allowing a companion to land with the player if they are not sneaking into town
				 (assign, ":companion_1", -1),
				 (assign,":break",0),
				 (party_get_num_companion_stacks,":num_stacks","p_main_party"),
				 (try_for_range,":stack",1,":num_stacks"),	#don't start at stack 1 since that is the player
					(eq,":break",0),
					(party_stack_get_troop_id,":troop_id","p_main_party",":stack"),
					(store_troop_health, ":troop_health", ":troop_id", 0),	#used 0 to get 0-100% range
					(ge, ":troop_health", 10),	#if they have more than 10% health you can continue
					(assign, ":companion_1", ":troop_id"),
					(assign, ":break", 1),	#so we stop the loop
				 (try_end),
				 #(assign, reg4, ":companion_1"), #debug only
				 #(display_message, "@companion_1 = {reg4}"),	#debug only
				 
				 #SW - if we want companion not to have a horse if the player doesn't have a horse?
				 # (troop_get_inventory_slot, ":player_horse_item", "$g_player_troop", ek_horse),
				 # (try_begin),
					# (le, ":player_horse_item", 0),	#no horse, don't allow NPC to have a horse
					# (assign, ":companion_override_state", af_override_horse),
					# (mission_tpl_entry_set_override_flags, "mt_town_center", 49, ":companion_override_state"),
				 # (try_end),	
				 
				 #SW - check what entry point to use for the companion
				 (try_begin),
					(eq, "$town_entered", 0),		# player will use entry point 1 (ie. 49 for companions)
					(assign, ":companion_1_ep", 49),
				 (else_try),	#player is already in town, use entry point 0 (ie. 48 for companion)
					(assign, ":companion_1_ep", 48),
				 (try_end),
				 #SW - spawn the companion if they exist
				 (try_begin),
					(gt, ":companion_1", 0),
					(set_visitor, ":companion_1_ep", ":companion_1"),
					#(assign, reg5, ":companion_1_ep"), #debug only
					#(display_message, "@companion_1 = {reg4}, spawned at {reg5}"),	#debug only
				 (try_end),
             (try_end),
             (mission_tpl_entry_set_override_flags, "mt_town_center", 0, ":override_state"),
             (mission_tpl_entry_set_override_flags, "mt_town_center", 2, ":override_state"),
             (mission_tpl_entry_set_override_flags, "mt_town_center", 3, ":override_state"),
             (mission_tpl_entry_set_override_flags, "mt_town_center", 4, ":override_state"),
             (mission_tpl_entry_set_override_flags, "mt_town_center", 5, ":override_state"),
             (mission_tpl_entry_set_override_flags, "mt_town_center", 6, ":override_state"),
             (mission_tpl_entry_set_override_flags, "mt_town_center", 7, ":override_state"),
             (try_begin),
               (eq, "$town_entered", 0),
               (assign, "$town_entered", 1),
               (eq, "$town_nighttime", 0),
               (set_jump_entry, 1),
             (try_end),
             (jump_to_scene, ":town_scene"),
             (change_screen_mission),
           (try_end),
        ],"Door to the center."),

      ("town_tavern",[
          (party_slot_eq,"$current_town",slot_party_type, spt_mainplanet),
          (this_or_next|eq,"$entry_to_town_forbidden",0),
          (eq, "$sneaked_into_town",1),
#          (party_get_slot, ":scene", "$current_town", slot_mainplanet_cantina),
#          (scene_slot_eq, ":scene", slot_scene_visited, 1), #check if scene has been visited before to allow entry from menu. Otherwise scene will only be accessible from the town center.
          ]
		  #SW - change tavern to cantina
       ,"Visit the cantina.",
       [
           (try_begin),
             (eq,"$all_doors_locked",1),
             (display_message,"str_door_locked",0xFFFFAAAA),
           (else_try),
             (call_script, "script_cf_enter_center_location_bandit_check"),
           (else_try),
             (mission_tpl_entry_set_override_flags, "mt_town_default", 0, af_override_horse),
             (try_begin),
               (eq, "$sneaked_into_town",1),
               (mission_tpl_entry_set_override_flags, "mt_town_default", 0, af_override_all),
             (try_end),
             (assign, "$town_entered", 1),
			 
			  #autoloot flag to allow player to talk to companions
			  (assign, "$g_camp_talk",0),		#set this to zero so we don't mess up companion recruitment dialog
			 
			 #SW - switched jump_mission
			 #(set_jump_mission, "mt_town_center"),
			 (set_jump_mission, "mt_cantina_default"),
			 
			 ###### CANTINA WALKER TESTING START ########################################################
			 #(call_script, "script_init_town_walkers"),
			 ###### CANTINA WALKER TESTING END     ########################################################

             (party_get_slot, ":cur_scene", "$current_town", slot_mainplanet_cantina),
             (jump_to_scene, ":cur_scene"),
             (scene_set_slot, ":cur_scene", slot_scene_visited, 1),

             (assign, "$talk_context", tc_tavern_talk),
			 (assign, "$g_init_fight", 0),	#used for cantina_brawl

             (modify_visitors_at_site, ":cur_scene"),
             (reset_visitors),
             (assign, ":cur_entry", 17),
             (party_get_slot, ":mercenary_troop", "$current_town", slot_center_mercenary_troop_type),
             (party_get_slot, ":mercenary_amount", "$current_town", slot_center_mercenary_troop_amount),
             (try_begin),
               (gt, ":mercenary_amount", 0),
               (set_visitor, ":cur_entry", ":mercenary_troop"),
               (val_add, ":cur_entry", 1),
             (try_end),
             
             (try_for_range, ":companion_candidate", companions_begin, companions_end),
               (troop_slot_eq, ":companion_candidate", slot_troop_occupation, 0),
               (troop_slot_eq, ":companion_candidate", slot_troop_cur_center, "$current_town"),
               (set_visitor, ":cur_entry", ":companion_candidate"),
               (val_add, ":cur_entry", 1),
             (try_end),
             (try_begin),
               (party_get_slot, ":ransom_broker", "$current_town", slot_center_ransom_broker),
               (gt, ":ransom_broker", 0),
               (set_visitor, ":cur_entry", ":ransom_broker"),
               (val_add, ":cur_entry", 1),
             (try_end),
             (try_begin),
               (party_get_slot, ":tavern_traveler", "$current_town", slot_center_tavern_traveler),
               (gt, ":tavern_traveler", 0),
               (set_visitor, ":cur_entry", ":tavern_traveler"),
               (val_add, ":cur_entry", 1),
             (try_end),
##             (try_begin),
##               (party_get_slot, ":tavern_minstrel", "$current_town", slot_center_tavern_minstrel),
##               (gt, ":tavern_minstrel", 0),
##               (set_visitor, 21, ":tavern_minstrel"),
##               (val_add, ":cur_entry", 1),
##             (try_end),
             (try_begin),
               (party_get_slot, ":tavern_bookseller", "$current_town", slot_center_tavern_bookseller),
               (gt, ":tavern_bookseller", 0),
               (set_visitor, ":cur_entry", ":tavern_bookseller"),
               (val_add, ":cur_entry", 1),
             (try_end),
             (try_begin),
               (neg|check_quest_active, "qst_eliminate_bandits_infesting_village"),
               (neg|check_quest_active, "qst_deal_with_bandits_at_lords_village"),
               (assign, ":end_cond", minorplanet_end),
               (try_for_range, ":cur_village", minorplanet_begin, ":end_cond"),
                 (party_slot_eq, ":cur_village", slot_minorplanet_bound_center, "$current_town"),
                 (party_slot_ge, ":cur_village", slot_minorplanet_infested_by_bandits, 1),
                 (neg|party_slot_eq, ":cur_village", slot_mainplanet_lord, "trp_player"),
                 (set_visitor, ":cur_entry", "trp_farmer_from_bandit_village"),
                 (val_add, ":cur_entry", 1),
                 (assign, ":end_cond", 0),
               (try_end),
             (try_end),
			 
			 ###### CANTINA WALKER TESTING START ########################################################
			 #(assign, "$talk_context", tc_town_talk),    #DON'T USE THIS OR THE MERC DIALOG BREAKS, BUT IF YOUTURN IT OFF THEN THE CITIZENS BREAKS.....
			 
			 (store_random_in_range, ":walker_troop_id", cantina_walkers_begin, cantina_walkers_end),
			 (set_visitor,32,":walker_troop_id"),			 
			 (store_random_in_range, ":walker_troop_id", cantina_walkers_begin, cantina_walkers_end),
			 (set_visitor,33,":walker_troop_id"),			 
			 (store_random_in_range, ":walker_troop_id", cantina_walkers_begin, cantina_walkers_end),
			 (set_visitor,34,":walker_troop_id"),			 
			 (store_random_in_range, ":walker_troop_id", cantina_walkers_begin, cantina_walkers_end),
			 (set_visitor,35,":walker_troop_id"),			 
			 (store_random_in_range, ":walker_troop_id", cantina_walkers_begin, cantina_walkers_end),
			 (set_visitor,36,":walker_troop_id"),			 
			 (store_random_in_range, ":walker_troop_id", cantina_walkers_begin, cantina_walkers_end),
			 (set_visitor,37,":walker_troop_id"),			 
			 (store_random_in_range, ":walker_troop_id", cantina_walkers_begin, cantina_walkers_end),
			 (set_visitor,38,":walker_troop_id"),			 
			 (store_random_in_range, ":walker_troop_id", cantina_walkers_begin, cantina_walkers_end),
			 (set_visitor,39,":walker_troop_id"),			 
			 ###### CANTINA WALKER TESTING END     ########################################################
			 # CANTINA DRINKERS
			 (store_random_in_range, ":walker_troop_id", cantina_drinkers_begin, cantina_drinkers_end),
			 (set_visitor,40,":walker_troop_id"),			 
			 (store_random_in_range, ":walker_troop_id", cantina_drinkers_begin, cantina_drinkers_end),
			 (set_visitor,41,":walker_troop_id"),			 
			 (store_random_in_range, ":walker_troop_id", cantina_drinkers_begin, cantina_drinkers_end),
			 (set_visitor,42,":walker_troop_id"),			 
			 (store_random_in_range, ":walker_troop_id", cantina_drinkers_begin, cantina_drinkers_end),
			 (set_visitor,43,":walker_troop_id"),			 
			 (store_random_in_range, ":walker_troop_id", cantina_drinkers_begin, cantina_drinkers_end),
			 (set_visitor,44,":walker_troop_id"),			 
			 (store_random_in_range, ":walker_troop_id", cantina_drinkers_begin, cantina_drinkers_end),
			 (set_visitor,45,":walker_troop_id"),			 
			 #####################################################################################
			 
			 ##### CANTINA MUSIC TESTING START #######################################
			 #(play_sound, "snd_cantina_ambience"),
			 #(play_sound, "snd_laser_fire"),
			 #(play_sound, "snd_cantina_ambience", sf_looping),
			 #(play_cue_track, "track_cantina_1"),		# ended up using play_sound instead
			 ##### CANTINA MUSIC TESTING END    #######################################
			 
             (change_screen_mission),
           (try_end),
		   #SW - updated tavern to cantina
        ],"Door to the cantina."),
      
#      ("town_smithy",[
#          (eq,"$entry_to_town_forbidden",0),
#          (eq,"$town_nighttime",0),
#          ],
#       "Visit the smithy.",
#       [
#           (set_jump_mission,"mt_town_default"),
#           (jump_to_scene,"$pout_scn_smithy"),
#           (change_screen_mission,0),
#        ]),
      
      ("town_merchant",
       [(party_slot_eq,"$current_town",slot_party_type, spt_mainplanet),
           (eq, 1, 0),
           (eq,"$town_nighttime",0),
           (this_or_next|eq,"$entry_to_town_forbidden",0),
           (eq, "$sneaked_into_town",1),
#           (party_get_slot, ":scene", "$current_town", slot_mainplanet_store),
#           (scene_slot_eq, ":scene", slot_scene_visited, 1), #check if scene has been visited before to allow entry from menu. Otherwise scene will only be accessible from the town center.
           ],
       "Speak with the merchant.",
       [
		   #SW - attempt to fix bug where if you enter the shop from the cantina it uses the mercenary dialog           
		   (assign, "$talk_context", 0),
		   
           (try_begin),
             (this_or_next|eq,"$all_doors_locked",1),
             (eq,"$town_nighttime",1),
             (display_message,"str_door_locked",0xFFFFAAAA),
           (else_try),
             (mission_tpl_entry_set_override_flags, "mt_town_default", 0, af_override_horse),
             (try_begin),
               (eq, "$sneaked_into_town",1),
               (mission_tpl_entry_set_override_flags, "mt_town_default", 0, af_override_all),
             (try_end),
             (assign, "$town_entered", 1),
             (set_jump_mission, "mt_town_default"),
             (party_get_slot, ":cur_scene", "$current_town", slot_mainplanet_store),
             (jump_to_scene, ":cur_scene"),
             (scene_set_slot, ":cur_scene", slot_scene_visited, 1),
             (change_screen_mission),
           (try_end),
        ],"Door to the shop."),
      ("town_arena",
       [
		(party_slot_eq,"$current_town",slot_party_type, spt_mainplanet),
        (eq, "$sneaked_into_town", 0),
#           (party_get_slot, ":scene", "$current_town", slot_mainplanet_arena),
#           (scene_slot_eq,  ":scene", slot_scene_visited, 1), #check if scene has been visited before to allow entry from menu. Otherwise scene will only be accessible from the town center.
           ],
	   #SW - modified name of the arena
	   #"Enter the force-sensitive arena.",
	   "Enter the arena.",
       [
           (try_begin),
             (this_or_next|eq,"$all_doors_locked",1),
             (eq,"$town_nighttime",1),
             (display_message,"str_door_locked",0xFFFFAAAA),
           (else_try),
             (assign, "$g_mt_mode", abm_visit),
             (assign, "$town_entered", 1),
			 
			 #SW - added script_set_items_for_arena so we can toggle what weapons are used (didn't work here either...)
			#(call_script, "script_set_items_for_arena", 0),
             (set_jump_mission, "mt_arena_melee_fight"),
             (party_get_slot, ":arena_scene", "$current_town", slot_mainplanet_arena),
             (modify_visitors_at_site, ":arena_scene"),
             (reset_visitors),
             (set_visitor, 43, "trp_veteran_fighter"),
			 #SW - modified set_visitor
			 (set_visitor, 44, "trp_champion_fighter"),			 
             (set_jump_entry, 50),
             (jump_to_scene, ":arena_scene"),
             (scene_set_slot, ":arena_scene", slot_scene_visited, 1),
             (change_screen_mission),
           (try_end),
        ],"Door to the arena."),
      ("town_dungeon",
       [(eq, 1, 0)],
       "Never: Enter the prison.",
       [
           (try_begin),
             (eq,"$all_doors_locked",1),
             (display_message,"str_door_locked",0xFFFFAAAA),
           (else_try),
             (this_or_next|party_slot_eq, "$current_town", slot_mainplanet_lord, "trp_player"),
             (eq, "$g_encountered_party_faction", "$players_faction"),
             (assign, "$town_entered", 1),
             (call_script, "script_enter_dungeon", "$current_town", "mt_visit_town_castle"),
           (else_try),
             (display_message,"str_door_locked",0xFFFFAAAA),
           (try_end),
        #SW - modified
		#],"Door to the dungeon."),
		],"Door to the prison."),
      
      ("spacestation_inspect", [
         (party_slot_eq,"$current_town",slot_party_type, spt_castle),
#           (this_or_next|ge, "$g_encountered_party_relation", 0),
#           (eq,"$spacestation_undefended",1),
          ],
		#SW - modified menu
       #"Take a walk around the courtyard.",
	   "Take a walk around the site.",
       [
           (assign, "$talk_context", tc_town_talk),
           
           (party_get_slot, ":cur_spacestation_exterior", "$current_town", slot_spacestation_exterior),
           (modify_visitors_at_site,":cur_spacestation_exterior"),(reset_visitors),

           (try_begin),
             (neq, "$g_encountered_party_faction", "fac_player_supporters_faction"),
             (faction_get_slot, ":troop_prison_guard", "$g_encountered_party_faction", slot_faction_prison_guard_troop),
             (set_visitor, 24, ":troop_prison_guard"),
           (try_end),
           
		   #SW - commented out old code that uses current party members for castle guards since that messed up the dialogs
           # (assign, ":guard_no", 40),
           # (party_get_num_companion_stacks, ":num_stacks", "$g_encountered_party"),
           # (try_for_range, ":troop_iterator", 0, ":num_stacks"),
             # (lt, ":guard_no", 47),
             # (party_stack_get_troop_id, ":cur_troop_id", "$g_encountered_party", ":troop_iterator"),
             # (neg|troop_is_hero, ":cur_troop_id"),
             # (party_stack_get_size, ":stack_size","$g_encountered_party",":troop_iterator"),
             # (party_stack_get_num_wounded, ":num_wounded","$g_encountered_party",":troop_iterator"),
             # (val_sub, ":stack_size", ":num_wounded"),
             # (gt, ":stack_size", 0),
             # (party_stack_get_troop_dna,":troop_dna","$g_encountered_party",":troop_iterator"),
             # (set_visitor, ":guard_no", ":cur_troop_id", ":troop_dna"),
             # (val_add, ":guard_no", 1),
           # (try_end),

		   #SW - new code for castle guards
		   (faction_get_slot, ":guard", "$g_encountered_party_faction", slot_faction_tier_2_troop),
		   (set_visitor, 40, ":guard"),
		   (faction_get_slot, ":guard", "$g_encountered_party_faction", slot_faction_tier_3_troop),
		   (set_visitor, 41, ":guard"),
		   (faction_get_slot, ":guard", "$g_encountered_party_faction", slot_faction_tier_4_troop),
		   (set_visitor, 42, ":guard"),
		   (faction_get_slot, ":guard", "$g_encountered_party_faction", slot_faction_tier_2_troop),
		   (set_visitor, 43, ":guard"),
		   (faction_get_slot, ":guard", "$g_encountered_party_faction", slot_faction_tier_3_troop),
		   (set_visitor, 44, ":guard"),
		   (faction_get_slot, ":guard", "$g_encountered_party_faction", slot_faction_tier_4_troop),
		   (set_visitor, 45, ":guard"),
		   (faction_get_slot, ":guard", "$g_encountered_party_faction", slot_faction_tier_3_troop),
		   (set_visitor, 46, ":guard"),
		   
           (try_begin),
             (eq, "$town_entered", 0),
             (assign, "$town_entered", 1),
           (try_end),
           (set_jump_entry,1),
           
           (set_jump_mission,"mt_spacestation_visit"),
           (jump_to_scene,":cur_spacestation_exterior"),
           (change_screen_mission),
        #], "To the castle courtyard."),
		], "To the site."),
      ("trade_with_merchants",
       [
           (party_slot_eq,"$current_town",slot_party_type, spt_mainplanet)
        ],
         "Go to the marketplace.",
         [
           (try_begin),
             (call_script, "script_cf_enter_center_location_bandit_check"),
           (else_try),
             (jump_to_menu,"mnu_town_trade"),
           (try_end),
          ]),

      ("walled_center_manage",[(neg|party_slot_eq, "$current_town", slot_minorplanet_state, svs_under_siege),
                      (party_slot_eq, "$current_town", slot_mainplanet_lord, "trp_player"),
                      (assign, reg0, 1),
                      (try_begin),
                        (party_slot_eq, "$current_town", slot_party_type, spt_castle),
                        (assign, reg0, 0),
                      (try_end),]
       #SW - modified menu
	   #,"Manage this {reg0?planet:station}.",
	   ,"Manage this {reg0?planet:planet}.",
       [
           (assign, "$g_next_menu", "mnu_town"),
           (jump_to_menu, "mnu_center_manage"),
        ]),

     ("spacestation_station_troops",
      [
          (party_slot_eq,"$current_town",slot_mainplanet_lord, "trp_player"),
       ],
         "Station a garrison here...",
         [
           (change_screen_exchange_members,1),
          ]),


      ("spacestation_wait",
       [
#           (party_slot_eq,"$current_town",slot_party_type, spt_castle),
           (this_or_next|ge, "$g_encountered_party_relation", 0),
           (eq,"$spacestation_undefended",1),
           (assign, ":can_rest", 1),
           (str_clear, s1),
           (try_begin),
             (neg|party_slot_eq, "$current_town", slot_mainplanet_lord, "trp_player"),
             (party_get_num_companions, ":num_men", "p_main_party"),
             (store_div, reg1, ":num_men", 4),
             (val_add, reg1, 1),
			 #SW - increased cost to rest in towns
			 (try_begin),
				(this_or_next|eq,"$current_town","p_corellia"),
				(this_or_next|eq,"$current_town","p_naboo"),
				(eq,"$current_town","p_coruscant"),
				(val_mul, reg1, 3),
			 (else_try),
				(val_mul, reg1, 2),
			 (try_end),
			 #-----------------------------------------------
             (str_store_string, s1, "@ ({reg1} credits per night)"),
             (store_troop_gold, ":gold", "trp_player"),
             (lt, ":gold", reg1),
             (assign, ":can_rest", 0),
           (try_end),
           (eq, ":can_rest", 1),
##           (eq, "$g_defending_against_siege", 0),
        ],
         #SW - modified menu
		 #"Wait here for some time{s1}.",
		 "Dock your ship in the hangar bay{s1}.",
         [
           (assign,"$auto_enter_town","$current_town"),
           (assign, "$g_town_visit_after_rest", 1),
           (assign, "$g_last_rest_center", "$current_town"),
           (assign, "$g_last_rest_payment_until", -1),

           (rest_for_hours_interactive, 24 * 7, 5, 0), #rest while not attackable
           (change_screen_return),
          ]),

##      ("rest_until_morning",
##       [
##           (this_or_next|ge, "$g_encountered_party_relation", 0),
##           (eq,"$spacestation_undefended",1),
##           (store_time_of_day,reg(1)),(neg|is_between,reg(1), 5, 18),
##           (eq, "$g_defending_against_siege", 0),
##        ],
##         "Rest until morning.",
##         [
##           (store_time_of_day,reg(1)),
##           (assign, reg(2), 30),
##           (val_sub,reg(2),reg(1)),
##           (val_mod,reg(2),24),
##           (assign,"$auto_enter_town","$current_town"),
##           (assign, "$g_town_visit_after_rest", 1),
##           (rest_for_hours_interactive, reg(2)),
##           (change_screen_return),
##          ]),
##      
##      ("rest_until_evening",
##       [
##           (this_or_next|ge, "$g_encountered_party_relation", 0),
##           (eq,"$spacestation_undefended",1),
##           (store_time_of_day,reg(1)), (is_between,reg(1), 5, 18),
##           (eq, "$g_defending_against_siege", 0),
##        ],
##         "Rest until evening.",
##         [
##           (store_time_of_day,reg(1)),
##           (assign, reg(2), 20),
##           (val_sub,reg(2),reg(1)),
##           (assign,"$auto_enter_town","$current_town"),
##           (assign, "$g_town_visit_after_rest", 1),
##           (rest_for_hours_interactive, reg(2)),
##           (change_screen_return),
##          ]),
      ("town_alley",
       [(party_slot_eq,"$current_town",slot_party_type, spt_mainplanet),
        (eq, "$cheat_mode", 1),
           ],
       "CHEAT: Go to the alley.",
       [
           (party_get_slot, reg(11), "$current_town", slot_mainplanet_alley),
           (set_jump_mission,"mt_ai_training"),
           (jump_to_scene,reg(11)),
           (change_screen_mission),
        ]),
      
      ("collect_taxes_qst",[(check_quest_active, "qst_collect_taxes"),
                            (quest_slot_eq, "qst_collect_taxes", slot_quest_target_center, "$current_town"),
                            (neg|quest_slot_eq, "qst_collect_taxes", slot_quest_current_state, 4),
                            (quest_get_slot, ":quest_giver_troop", "qst_collect_taxes", slot_quest_giver_troop),
                            (str_store_troop_name, s1, ":quest_giver_troop"),
                            (quest_get_slot, reg5, "qst_collect_taxes", slot_quest_current_state),
                            ], "{reg5?Continue collecting taxes:Collect taxes} due to {s1}.",
       [(jump_to_menu, "mnu_collect_taxes"),]),
      
      ("leave_3dot",[],"Leave...",[
		    #autoloot flag - turn it off so dialogs don't break
		    (assign, "$g_camp_talk",0),
            (assign, "$g_permitted_to_center",0),
            (change_screen_return,0),
          ],"Leave Area."),
#      ("siege_leave",[(eq, "$g_defending_against_siege", 1)],"Try to break out...",[(jump_to_menu,"mnu_siege_break_out")]),#TODO: Go to Menu here.

      ("spacestation_cheat_interior",[(eq, "$cheat_mode", 1)], "CHEAT! Interior.",[
                                                       (set_jump_mission,"mt_ai_training"),
                                                       (party_get_slot, ":spacestation_scene", "$current_town", slot_mainplanet_castle),
                                                       (jump_to_scene,":spacestation_scene"),
                                                       (change_screen_mission)]),
      ("spacestation_cheat_exterior",[(eq, "$cheat_mode", 1)], "CHEAT! Exterior.",[
                                                       (try_begin),
                                                         (party_slot_eq,"$current_town",slot_party_type, spt_castle),
                                                         (party_get_slot, ":scene", "$current_town", slot_spacestation_exterior),
                                                       (else_try),
                                                         (party_get_slot, ":scene", "$current_town", slot_mainplanet_center),
                                                       (try_end),
                                                       (set_jump_mission,"mt_ai_training"),
                                                       (jump_to_scene,":scene"),
                                                       (change_screen_mission)]),
      ("spacestation_cheat_dungeon",[(eq, "$cheat_mode", 1)], "CHEAT! Prison.",[
                                                       (set_jump_mission,"mt_ai_training"),
                                                       (party_get_slot, ":spacestation_scene", "$current_town", slot_mainplanet_prison),
                                                       (jump_to_scene,":spacestation_scene"),
                                                       (change_screen_mission)]),
      ("spacestation_cheat_town_walls",[(eq, "$cheat_mode", 1),(party_slot_eq,"$current_town",slot_party_type, spt_mainplanet),], "CHEAT! Town Walls.",[
                                                       (party_get_slot, ":scene", "$current_town", slot_mainplanet_walls),
                                                       (set_jump_mission,"mt_ai_training"),
                                                       (jump_to_scene,":scene"),
                                                       (change_screen_mission)]),

      ("cheat_start_siege",
       [
         (eq, "$cheat_mode", 1),
         (party_slot_eq, "$g_encountered_party", slot_center_is_besieged_by, -1),
         (lt, "$g_encountered_party_2", 1),
         (call_script, "script_party_count_fit_for_battle","p_main_party"),
         (gt, reg(0), 1),
         (try_begin),
           (party_slot_eq, "$g_encountered_party", slot_party_type, spt_mainplanet),
           (assign, reg6, 1),
         (else_try),
           (assign, reg6, 0),
         (try_end),
           ],
       "CHEAT: Besiege the {reg6?planet:station}...",
       [
           (assign,"$g_player_besiege_town","$g_encountered_party"),
           (jump_to_menu, "mnu_spacestation_besiege"),
           ]),


      ("show_reports",[(eq, "$cheat_mode", 1),], "CHEAT! Show reports.",
       [(jump_to_menu,"mnu_center_reports"),
           ]),

      ("sail_from_port",[(party_slot_eq,"$current_town",slot_party_type, spt_mainplanet),
                         (eq, "$cheat_mode", 1),
#                         (party_slot_eq,"$current_town",slot_mainplanet_near_shore, 1),
                         ], "CHEAT! Sail from port.",
       [(assign, "$g_player_icon_state", pis_ship),
        (party_set_flags, "p_main_party", pf_is_ship, 1),
        (party_get_position, pos1, "p_main_party"),
        (map_get_water_position_around_position, pos2, pos1, 6),
        (party_set_position, "p_main_party", pos2),
        (assign, "$g_main_ship_party", -1),
        (change_screen_return),
        ]),

      ]
  ),

  (
    "town_tournament_lost",menu_text_color(0xFF000d2c),
    "You have been eliminated from the tournament.",
    "none",
    [
        ],
    [
      ("continue_3dot", [], "Continue...",
       [(jump_to_menu, "mnu_town_tournament_won_by_another"),
        ]),
    ]
  ),

  (
    "town_tournament_won",menu_text_color(0xFF000d2c)|mnf_disable_all_keys,
    "You have won the tournament of {s3}! You are filled with pride as the crowd cheers your name.\
 In addition to honour, fame and glory, you earn a prize of {reg9} credits. {s8}",
    "none",
    [
        (str_store_party_name, s3, "$current_town"),
        (call_script, "script_change_troop_renown", "trp_player", 20),
        (call_script, "script_change_player_relation_with_center", "$current_town", 1),   
        (assign, reg9, 200),
        (add_xp_to_troop, 250, "trp_player"),
        (troop_add_gold, "trp_player", reg9),
        (str_clear, s8),
        (store_add, ":total_win", "$g_tournament_bet_placed", "$g_tournament_bet_win_amount"),
        (try_begin),
          (gt, "$g_tournament_bet_win_amount", 0),
          (assign, reg8, ":total_win"),
          (str_store_string, s8, "@Moreover, you earn {reg8} credits from the clever bets you placed on yourself..."),
        (try_end),
        (troop_add_gold, "trp_player", ":total_win"),
        (assign, ":player_odds_sub", 0),
        (store_div, ":player_odds_sub", "$g_tournament_bet_win_amount", 5),
        (party_get_slot, ":player_odds", "$current_town", slot_mainplanet_player_odds),
        (val_sub, ":player_odds", ":player_odds_sub"),
        (val_max, ":player_odds", 250),
        (party_set_slot, "$current_town", slot_mainplanet_player_odds, ":player_odds"),
        (call_script, "script_play_victorious_sound"),
        ],
    [
      ("continue_3dot", [], "Continue...",
       [(jump_to_menu, "mnu_town"),
        ]),
    ]
  ),
  
  (
    "town_tournament_won_by_another",menu_text_color(0xFF000d2c)|mnf_disable_all_keys,
    "As the only {reg3?fighter:man} to remain undefeated this day, {s1} wins the lists and the glory of this tournament.",
    "none",
    [   (call_script, "script_get_num_tournament_participants"),
        (store_sub, ":needed_to_remove_randomly", reg0, 1),
        (call_script, "script_remove_tournament_participants_randomly", ":needed_to_remove_randomly"),
        (call_script, "script_sort_tournament_participant_troops"),
        (troop_get_slot, ":winner_troop", "trp_tournament_participants", 0),
        (str_store_troop_name, s1, ":winner_troop"),
        (try_begin),
          (troop_is_hero, ":winner_troop"),
          (call_script, "script_change_troop_renown", ":winner_troop", 20),
        (try_end),
        #(troop_get_type, reg3, ":winner_troop"),
        (call_script, "script_gender_fix", ":winner_troop"),(assign,reg3,reg33)
        ],
    [
      ("continue_3dot", [], "Continue...",
       [(jump_to_menu, "mnu_town"),
        ]),
    ]
  ),

  (
    "town_tournament",menu_text_color(0xFF000d2c)|mnf_disable_all_keys,
    "{s1}You are at tier {reg0} of the tournament, with {reg1} participants remaining. In the next round, there will be {reg2} teams with {reg3} {reg4?fighters:fighter} each.",
    "none",
    [
        (party_set_slot, "$current_town", slot_mainplanet_has_tournament, 0), #No way to return back if this menu is left
        (call_script, "script_sort_tournament_participant_troops"),#Moving trp_player to the top of the list
        (call_script, "script_get_num_tournament_participants"),
        (assign, ":num_participants", reg0),
        (try_begin),
          (neg|troop_slot_eq, "trp_tournament_participants", 0, 0),#Player is defeated

          (assign, ":player_odds_add", 0),
          (store_div, ":player_odds_add", "$g_tournament_bet_placed", 5),
          (party_get_slot, ":player_odds", "$current_town", slot_mainplanet_player_odds),
          (val_add, ":player_odds", ":player_odds_add"),
          (val_min, ":player_odds", 4000),
          (party_set_slot, "$current_town", slot_mainplanet_player_odds, ":player_odds"),

          (jump_to_menu, "mnu_town_tournament_lost"),
        (else_try),
          (eq, ":num_participants", 1),#Tournament won
          (jump_to_menu, "mnu_town_tournament_won"),
        (else_try),
          (try_begin),
            (le, "$g_tournament_next_num_teams", 0),
            (call_script, "script_get_random_tournament_team_amount_and_size"),
            (assign, "$g_tournament_next_num_teams", reg0),
            (assign, "$g_tournament_next_team_size", reg1),
          (try_end),
          (assign, reg2, "$g_tournament_next_num_teams"),
          (assign, reg3, "$g_tournament_next_team_size"),
          (store_sub, reg4, reg3, 1),
          (str_clear, s1),
          (try_begin),
            (eq, "$g_tournament_player_team_won", 1),
            (str_store_string, s1, "@Victory is yours! You have won this melee, but now you must prepare yourself for the next round. "),
          (else_try),
            (eq, "$g_tournament_player_team_won", 0),
            (str_store_string, s1, "@You have been bested in this melee, but the master of ceremonies declares a recognition of your skill and bravery, allowing you to take part in the next round. "),
          (try_end),
          (assign, reg1, ":num_participants"),
          (store_add, reg0, "$g_tournament_cur_tier", 1),
        (try_end),
        ],
    [
      ("tournament_view_participants", [], "View participants.",
       [(jump_to_menu, "mnu_tournament_participants"),
        ]),
      ("tournament_bet", [(neq, "$g_tournament_cur_tier", "$g_tournament_last_bet_tier")], "Place a bet on yourself.",
       [(jump_to_menu, "mnu_tournament_bet"),
        ]),
      ("tournament_join_next_fight", [], "Fight in the next round.",
       [
           (party_get_slot, ":arena_scene", "$current_town", slot_mainplanet_arena),
           (modify_visitors_at_site, ":arena_scene"),
           (reset_visitors),
           #Assuming that there are enough participants for the teams
           (val_add, "$g_tournament_cur_tier", 1),

           (store_mul, "$g_tournament_num_participants_for_fight", "$g_tournament_next_num_teams", "$g_tournament_next_team_size"),
           (troop_set_slot, "trp_tournament_participants", 0, -1),#Removing trp_player from the list
           (troop_set_slot, "trp_temp_array_a", 0, "trp_player"),
           (try_for_range, ":slot_no", 1, "$g_tournament_num_participants_for_fight"),
             (call_script, "script_get_random_tournament_participant"),
             (troop_set_slot, "trp_temp_array_a", ":slot_no", reg0),
           (try_end),
           (call_script, "script_shuffle_troop_slots", "trp_temp_array_a", 0, "$g_tournament_num_participants_for_fight"),


           (try_for_range, ":slot_no", 0, 4),#shuffle teams
             (troop_set_slot, "trp_temp_array_b", ":slot_no", ":slot_no"),
           (try_end),
           (call_script, "script_shuffle_troop_slots", "trp_temp_array_b", 0, 4),

           (assign, ":cur_slot", 0),
           (try_for_range, ":cur_team_offset", 0, "$g_tournament_next_num_teams"),
             (troop_get_slot, ":cur_team", "trp_temp_array_b", ":cur_team_offset"),
           
             (try_for_range, ":slot_no", 0, 8),#shuffle entry_points
               (troop_set_slot, "trp_temp_array_c", ":slot_no", ":slot_no"),
             (try_end),
             (call_script, "script_shuffle_troop_slots", "trp_temp_array_c", 0, 8),
           
             (try_for_range, ":cur_index", 0, "$g_tournament_next_team_size"),
               (store_mul, ":cur_entry_point", ":cur_team", 8),
               (troop_get_slot, ":entry_offset", "trp_temp_array_c", ":cur_index"),
               (val_add, ":cur_entry_point", ":entry_offset"),
               (troop_get_slot, ":troop_no", "trp_temp_array_a", ":cur_slot"),
               (set_visitor, ":cur_entry_point", ":troop_no"),
               (val_add, ":cur_slot", 1),
             (try_end),
           (try_end),

           (assign, "$g_tournament_next_num_teams", 0),
           (assign, "$g_tournament_next_team_size", 0),
           
           (assign, "$g_mt_mode", abm_tournament),

           (party_get_slot, ":town_original_faction", "$current_town", slot_center_original_faction),
           (assign, ":town_index_within_faction", 0),
           (assign, ":end_cond", mainplanets_end),
           (try_for_range, ":cur_town", mainplanets_begin, ":end_cond"),
             (try_begin),
               (eq, ":cur_town", "$current_town"),
               (assign, ":end_cond", 0), #break
             (else_try),
               (party_slot_eq, ":cur_town", slot_center_original_faction, ":town_original_faction"),
               (val_add, ":town_index_within_faction", 1),
             (try_end),
           (try_end),
           (try_begin),
             (eq, ":town_original_faction", "fac_galacticempire"),
             #Swadia
             (store_mod, ":mod", ":town_index_within_faction", 4),
             (try_begin),
               (eq, ":mod", 0),
               #SW - modified arena_armor, removed helmet, removed horse chance
			   #(call_script, "script_set_items_for_tournament", 40, 80, 50, 20, 0, 0, 0, 0, "itm_arena_armor_red", "itm_tourney_helm_red"),
			   (call_script, "script_set_items_for_tournament", 0, 80, 50, 20, 0, 0, 0, 0, "itm_arena_tunic_red", 0),
             (else_try),
               (eq, ":mod", 1),
			   #SW - modified arena_armor, removed helmet, switched horse chance to 0
               (call_script, "script_set_items_for_tournament", 0, 100, 0, 0, 0, 0, 0, 0, "itm_arena_tunic_red", 0),
             (else_try),
               (eq, ":mod", 2),
			   #SW - modified arena_armor, removed helmet, switched horse chance to 0
               (call_script, "script_set_items_for_tournament", 0, 0, 100, 0, 0, 0, 0, 0, "itm_arena_tunic_red", 0),
             (else_try),
               (eq, ":mod", 3),
			   #SW - modified arena_armor, removed helmet, switched horse chance to 0
               (call_script, "script_set_items_for_tournament", 0, 80, 50, 20, 40, 0, 0, 0, "itm_arena_tunic_red", 0),
             (try_end),
           (else_try),
             (eq, ":town_original_faction", "fac_rebelalliance"),
             #Vaegirs
             (store_mod, ":mod", ":town_index_within_faction", 4),
             (try_begin),
               (eq, ":mod", 0),
			   #SW - modified arena_armor, removed helmet, switched horse chance to 0
               (call_script, "script_set_items_for_tournament", 0, 80, 50, 20, 0, 0, 0, 0, "itm_arena_tunic_red", 0),
             (else_try),
               (eq, ":mod", 1),
			   #SW - modified arena_armor, removed helmet, switched horse chance to 0
               (call_script, "script_set_items_for_tournament", 0, 50, 0, 0, 0, 20, 30, 0, "itm_arena_tunic_red", 0),
             (else_try),
               (eq, ":mod", 2),
			   #SW - modified arena_armor, removed helmet, switched horse chance to 0
               (call_script, "script_set_items_for_tournament", 0, 0, 50, 0, 0, 20, 30, 0, "itm_arena_tunic_red", 0),
             (else_try),
               (eq, ":mod", 3),
			   #SW - modified arena_armor, removed helmet, switched horse chance to 0
               (call_script, "script_set_items_for_tournament", 0, 80, 50, 20, 30, 0, 60, 0, "itm_arena_tunic_red", 0),
             (try_end),
           (else_try),
             (eq, ":town_original_faction", "fac_huttcartel"),
             #Khergit
             (store_mod, ":mod", ":town_index_within_faction", 2),
             (try_begin),
               (eq, ":mod", 0),
			   #SW - modified arena_armor, removed helmet, switched horse chance to 0
               (call_script, "script_set_items_for_tournament", 0, 0, 0, 0, 0, 40, 60, 0, "itm_arena_tunic_red", 0),
             (else_try),
               (eq, ":mod", 1),
			   #SW - modified arena_armor, removed helmet, switched horse chance to 0
               (call_script, "script_set_items_for_tournament", 0, 50, 25, 0, 0, 30, 50, 0, "itm_arena_tunic_red", 0),
             (try_end),
		   #SW - commented out faction 4 & 5
           # (else_try),
             # (eq, ":town_original_faction", "fac_faction_4"),
             # #Nords
             # (store_mod, ":mod", ":town_index_within_faction", 3),
             # (try_begin),
               # (eq, ":mod", 0),
               # (call_script, "script_set_items_for_tournament", 0, 0, 50, 80, 0, 0, 0, 0, "itm_arena_armor_red", -1),
             # (else_try),
               # (eq, ":mod", 1),
               # (call_script, "script_set_items_for_tournament", 0, 0, 50, 80, 50, 0, 0, 0, "itm_arena_armor_red", -1),
             # (else_try),
               # (eq, ":mod", 2),
               # (call_script, "script_set_items_for_tournament", 40, 0, 0, 100, 0, 0, 0, 0, "itm_arena_armor_red", -1),
             # (try_end),
           # (else_try),
             # #Rhodoks
             # (call_script, "script_set_items_for_tournament", 25, 100, 60, 0, 30, 0, 30, 50, "itm_arena_tunic_red", "itm_arena_helmet_red"),
           (try_end),
           (set_jump_mission, "mt_arena_melee_fight"),
           (jump_to_scene, ":arena_scene"),
           (change_screen_mission),
        ]),
      ("leave_tournament",[],"Withdraw from the tournament.",
       [
           (jump_to_menu, "mnu_tournament_withdraw_verify"),
        ]),
    ]
  ),

  (
    "tournament_withdraw_verify",menu_text_color(0xFF000d2c),
    "Are you sure you want to withdraw from the tournament?",
    "none",
    [],
    [
      ("tournament_withdraw_yes", [], "Yes. This is a pointless affectation.",
       [(jump_to_menu, "mnu_town_tournament_won_by_another"),
        ]),
      ("tournament_withdraw_no", [], "No, not as long as there is a chance of victory!",
       [(jump_to_menu, "mnu_town_tournament"),
        ]),
    ]
  ),

  (
    "tournament_bet",menu_text_color(0xFF000d2c),
    "The odds against you are {reg5} to {reg6}.{reg1? You have already bet {reg1} credits on yourself, and if you win, you will earn {reg2} credits.:} How much do you want to bet?",
    "none",
    [
      (assign, reg1, "$g_tournament_bet_placed"),
      (store_add, reg2, "$g_tournament_bet_win_amount", "$g_tournament_bet_placed"),
      (call_script, "script_get_win_amount_for_tournament_bet"),
      (assign, ":player_odds", reg0),
      (assign, ":min_dif", 100000),
      (assign, ":min_dif_divisor", 1),
      (assign, ":min_dif_multiplier", 1),
      (try_for_range, ":cur_multiplier", 1, 50),
        (try_for_range, ":cur_divisor", 1, 50),
          (store_mul, ":result", 100, ":cur_multiplier"),
          (val_div, ":result", ":cur_divisor"),
          (store_sub, ":difference", ":player_odds", ":result"),
          (val_abs, ":difference"),
          (lt, ":difference", ":min_dif"),
          (assign, ":min_dif", ":difference"),
          (assign, ":min_dif_divisor", ":cur_divisor"),
          (assign, ":min_dif_multiplier", ":cur_multiplier"),
        (try_end),
      (try_end),
      (assign, reg5, ":min_dif_multiplier"),
      (assign, reg6, ":min_dif_divisor"),
      ],
    [
	#SW - switched tournament bet amount back to native values
      ("bet_100_denars", [(store_troop_gold, ":gold", "trp_player"),
                          (ge, ":gold", 100)
                          ],
       "100 credits.",
       [
         (assign, "$temp", 100),
         (jump_to_menu, "mnu_tournament_bet_confirm"),
        ]),
      ("bet_50_denars", [(store_troop_gold, ":gold", "trp_player"),
                         (ge, ":gold", 50)
                         ],
       "50 credits.",
       [
         (assign, "$temp", 50),
         (jump_to_menu, "mnu_tournament_bet_confirm"),
        ]),
      ("bet_20_denars", [(store_troop_gold, ":gold", "trp_player"),
                         (ge, ":gold", 20)
                         ],
       "20 credits.",
       [
         (assign, "$temp", 20),
         (jump_to_menu, "mnu_tournament_bet_confirm"),
        ]),
      ("bet_10_denars", [(store_troop_gold, ":gold", "trp_player"),
                         (ge, ":gold", 10)
                         ],
       "10 credits.",
       [
         (assign, "$temp", 10),
         (jump_to_menu, "mnu_tournament_bet_confirm"),
        ]),
      ("bet_5_denars", [(store_troop_gold, ":gold", "trp_player"),
                        (ge, ":gold", 5)
                        ],
       "5 credits.",
       [
         (assign, "$temp", 5),
         (jump_to_menu, "mnu_tournament_bet_confirm"),
        ]),
      ("go_back_dot", [], "Go back.",
       [
         (jump_to_menu, "mnu_town_tournament"),
        ]),
    ]
  ),

  (
    "tournament_bet_confirm",menu_text_color(0xFF000d2c),
    "If you bet {reg1} credits, you will earn {reg2} credits if you win the tournament. Is that all right?",
    "none",
    [
      (call_script, "script_get_win_amount_for_tournament_bet"),
      (assign, ":win_amount", reg0),
      (val_mul, ":win_amount", "$temp"),
      (val_div, ":win_amount", 100),
      (assign, reg1, "$temp"),
      (assign, reg2, ":win_amount"),
      ],
    [
      ("go_ahead", [],
       "Go ahead.",
       [
         (call_script, "script_tournament_place_bet", "$temp"),
         (jump_to_menu, "mnu_town_tournament"),
         ]),
      ("forget_it", [],
       "Forget it.",
       [
         (jump_to_menu, "mnu_tournament_bet"),
         ]),
    ]
  ),
  
  (
    "tournament_participants",menu_text_color(0xFF000d2c),
    "You ask one of the criers for the names of the tournament participants. They are:^{s11}",
    "none",
    [
        (str_clear, s11),
        (call_script, "script_sort_tournament_participant_troops"),
        (call_script, "script_get_num_tournament_participants"),
        (assign, ":num_participants", reg0),
        (try_for_range, ":cur_slot", 0, ":num_participants"),
          (troop_get_slot, ":troop_no", "trp_tournament_participants", ":cur_slot"),
          (str_store_troop_name, s12, ":troop_no"),
          (str_store_string, s11, "@{s11}^{s12}"),
        (try_end),
        ],
    [
      ("go_back_dot", [], "Go back.",
       [(jump_to_menu, "mnu_town_tournament"),
        ]),
    ]
  ),


  (
    "collect_taxes",menu_text_color(0xFF000d2c)|mnf_disable_all_keys,
    "As the party member with the highest trade skill ({reg2}), {reg3?you expect:{s1} expects} that collecting taxes from here will take {reg4} days...",
    "none",
    [(call_script, "script_get_max_skill_of_player_party", "skl_trade"),
     (assign, ":max_skill", reg0),
     (assign, reg2, reg0),
     (assign, ":max_skill_owner", reg1),
     (try_begin),
       (eq, ":max_skill_owner", "trp_player"),
       (assign, reg3, 1),
     (else_try),
       (assign, reg3, 0),
       (str_store_troop_name, s1, ":max_skill_owner"),
     (try_end),
     (assign, ":tax_quest_expected_revenue", 3000),
     (try_begin),
       (party_slot_eq, "$current_town", slot_party_type, spt_mainplanet),
       (assign, ":tax_quest_expected_revenue", 6000),
     (try_end),

     (try_begin),
       (quest_slot_eq, "qst_collect_taxes", slot_quest_current_state, 0),
       (store_add, ":max_skill_plus_thirty", ":max_skill", 30),
       (try_begin),
         (party_slot_eq, "$current_town", slot_party_type, spt_mainplanet),
         (store_div, "$qst_collect_taxes_total_hours", 24* 7 * 30, ":max_skill_plus_thirty"),
       (else_try),
         #Village
         (store_div, "$qst_collect_taxes_total_hours", 24 * 3 * 30, ":max_skill_plus_thirty"),
       (try_end),

       (call_script, "script_party_count_fit_for_battle", "p_main_party"),
       (val_add, reg0, 20),
       (val_mul, "$qst_collect_taxes_total_hours", 20),
       (val_div, "$qst_collect_taxes_total_hours", reg0),

     
       (quest_set_slot, "qst_collect_taxes", slot_quest_target_amount, "$qst_collect_taxes_total_hours"),
       (store_div, ":menu_begin_time", "$qst_collect_taxes_total_hours", 20),#between %5-%25
       (store_div, ":menu_end_time", "$qst_collect_taxes_total_hours", 4),
       (assign, ":unrest_begin_time", ":menu_end_time"),#between %25-%75
       (store_mul, ":unrest_end_time", "$qst_collect_taxes_total_hours", 3),
       (val_div, ":unrest_end_time", 4),

       (val_mul, ":tax_quest_expected_revenue", 2),
       (store_div, "$qst_collect_taxes_hourly_income", ":tax_quest_expected_revenue", "$qst_collect_taxes_total_hours"),
     
       (store_random_in_range, "$qst_collect_taxes_menu_counter", ":menu_begin_time", ":menu_end_time"),
       (store_random_in_range, "$qst_collect_taxes_unrest_counter", ":unrest_begin_time", ":unrest_end_time"),
       (assign, "$qst_collect_taxes_halve_taxes", 0),
     (try_end),
     (quest_get_slot, ":target_hours", "qst_collect_taxes", slot_quest_target_amount),
     (store_div, ":target_days", ":target_hours", 24),
     (val_mul, ":target_days", 24),
     (try_begin),
       (lt, ":target_days", ":target_hours"),
       (val_add, ":target_days", 24),
     (try_end),
     (val_div, ":target_days", 24),
     (assign, reg4, ":target_days"),
     ],
    [
      ("start_collecting", [], "Start collecting.",
       [(assign, "$qst_collect_taxes_currently_collecting", 1),
        (try_begin),
          (quest_slot_eq, "qst_collect_taxes", slot_quest_current_state, 0),
          (quest_set_slot, "qst_collect_taxes", slot_quest_current_state, 1),
        (try_end),
        (rest_for_hours_interactive, 1000, 5, 0), #rest while not attackable
        (assign,"$auto_enter_town","$current_town"),
        (assign, "$g_town_visit_after_rest", 1),
        (change_screen_return),
        ]),
      ("do_it_later", [], "Put it off until later.",
       [(try_begin),
          (party_slot_eq, "$current_town", slot_party_type, spt_mainplanet),
          (jump_to_menu, "mnu_town"),
        (else_try),
          (jump_to_menu, "mnu_village"),
        (try_end),
        ]),
    ]
  ),

  (
    "collect_taxes_complete",menu_text_color(0xFF000d2c)|mnf_disable_all_keys,
    "You've collected {reg3} credits in taxes from {s3}. {s19} will be expecting you to take the money to him.",
    "none",
    [(str_store_party_name, s3, "$current_town"),
     (quest_get_slot, ":quest_giver", "qst_collect_taxes", slot_quest_giver_troop),
     (str_store_troop_name, s19, ":quest_giver"),
     (quest_get_slot, reg3, "qst_collect_taxes", slot_quest_gold_reward),
     (try_begin),
       (eq, "$qst_collect_taxes_halve_taxes", 0),
       (call_script, "script_change_player_relation_with_center", "$current_town", -2),   
     (try_end),
     (call_script, "script_succeed_quest", "qst_collect_taxes"),
     ],
    [
      ("continue_3dot", [], "Continue...",
       [(change_screen_return),
        ]),
    ]
  ),

  (
    "collect_taxes_rebels_killed",menu_text_color(0xFF000d2c),
    "Your quick action and strong arm have successfully put down the revolt.\
 Surely, anyone with a mind to rebel against you will think better of it after this.",
    "none",
    [
    ],
    [
      ("continue_3dot", [], "Continue...",
       [(change_screen_map),
        ]),
    ]
  ),

  (
    "collect_taxes_failed",menu_text_color(0xFF000d2c)|mnf_disable_all_keys,
    "You could collect only {reg3} credits as tax from {s3} before the revolt broke out.\
 {s1} won't be happy, but some silver will placate him better than nothing at all...",
    "none",
    [(str_store_party_name, s3, "$current_town"),
     (quest_get_slot, ":quest_giver", "qst_collect_taxes", slot_quest_giver_troop),
     (str_store_troop_name, s1, ":quest_giver"),
     (quest_get_slot, reg3, "qst_collect_taxes", slot_quest_gold_reward),
     (call_script, "script_fail_quest", "qst_collect_taxes"),
     (quest_set_slot, "qst_collect_taxes", slot_quest_current_state, 4),
     (rest_for_hours, 0, 0, 0), #stop resting
     ],
    [
      ("continue_3dot", [], "Continue...",
       [(change_screen_map),
        ]),
    ]
  ),

  (
    "collect_taxes_revolt_warning",menu_text_color(0xFF000d2c),
    "The people of {s3} are outraged at your demands and decry it as nothing more than extortion.\
 They're getting very restless, and they may react badly if you keep pressing them.",
    "none",
    [(str_store_party_name, s3, "$current_town"),
     ],
    [
      ("continue_collecting_taxes", [], "Ignore them and continue.",
       [(change_screen_return),]),
      ("halve_taxes", [(quest_get_slot, ":quest_giver_troop", "qst_collect_taxes", slot_quest_giver_troop),
                       (str_store_troop_name, s1, ":quest_giver_troop"),],
       "Agree to reduce your collection by half. ({s1} may be upset)",
       [(assign, "$qst_collect_taxes_halve_taxes", 1),
        (change_screen_return),
        ]),
    ]
  ),

  (
    "collect_taxes_revolt",menu_text_color(0xFF000d2c),
    "You are interrupted while collecting the taxes at {s3}. A large band of angry {reg9?colonists:citizens} is marching nearer,\
 shouting about the exorbitant taxes and waving knives and blaster pistols. It looks like they aim to fight you!",
    "none",
    [(str_store_party_name, s3, "$current_town"),
     (assign, reg9, 0),
     (try_begin),
       (party_slot_eq, "$current_town", slot_party_type, spt_minorplanet),
       (assign, reg9, 1),
     (try_end),
     ],
    [
      ("continue_3dot", [], "Continue...",
       [(set_jump_mission,"mt_back_alley_revolt"),
        (quest_get_slot, ":target_center", "qst_collect_taxes", slot_quest_target_center),
        (try_begin),
          (party_slot_eq, ":target_center", slot_party_type, spt_mainplanet),
          (party_get_slot, ":town_alley", ":target_center", slot_mainplanet_alley),
        (else_try),
          (party_get_slot, ":town_alley", ":target_center", slot_spacestation_exterior),
        (try_end),
        (modify_visitors_at_site,":town_alley"),
        (reset_visitors),
        (assign, ":num_rebels", 6),
        (store_character_level, ":level", "trp_player"),
        (val_div, ":level", 5),
        (val_add, ":num_rebels", ":level"),
        (set_visitors, 1, "trp_tax_rebel", ":num_rebels"),
        (jump_to_scene,":town_alley"),
        (change_screen_mission),
        ]),
    ]
  ),

# They must learn field discipline and the steadiness to follow orders in combat before they can be thought to use arms.",
  (
    "train_peasants_against_bandits",menu_text_color(0xFF000d2c),
    "As the party member with the highest training skill ({reg2}), {reg3?you expect:{s1} expects} that getting some colonists ready for practice will take {reg4} hours.",
    "none",
    [(call_script, "script_get_max_skill_of_player_party", "skl_trainer"),
     (assign, ":max_skill", reg0),
     (assign, reg2, reg0),
     (assign, ":max_skill_owner", reg1),
     (try_begin),
       (eq, ":max_skill_owner", "trp_player"),
       (assign, reg3, 1),
     (else_try),
       (assign, reg3, 0),
       (str_store_troop_name, s1, ":max_skill_owner"),
     (try_end),
     (store_sub, ":needed_hours", 20, ":max_skill"),
     (val_mul, ":needed_hours", 3),
     (val_div, ":needed_hours", 5),
     (store_sub, reg4, ":needed_hours", "$qst_train_peasants_against_bandits_num_hours_trained"),
     ],
    [
      ("make_preparation", [], "Train them.",
       [
         (assign, "$qst_train_peasants_against_bandits_currently_training", 1),
         (rest_for_hours_interactive, 1000, 5, 0), #rest while not attackable
         (assign, "$auto_enter_town", "$current_town"),
         (assign, "$g_town_visit_after_rest", 1),
         (change_screen_return),
         ]),
      ("do_it_later", [], "Put it off until later.",
       [
         (jump_to_menu, "mnu_village"),
        ]),
    ]
  ), 

  (
    "train_peasants_against_bandits_ready",menu_text_color(0xFF000d2c),
    "You put the colonists through the basics of soldiering, discipline and obedience.\
 You think {reg0} of them {reg1?have:has} fully grasped the training and {reg1?are:is} ready for some practice.",
    "none",
    [
      (store_character_level, ":level", "trp_player"),
      (val_div, ":level", 10),
      (val_add, ":level", 1),
      (quest_get_slot, ":quest_target_amount", "qst_train_peasants_against_bandits", slot_quest_target_amount),
      (quest_get_slot, ":quest_current_state", "qst_train_peasants_against_bandits", slot_quest_current_state),
      (val_sub, ":quest_target_amount", ":quest_current_state"),
      (assign, ":max_random", ":level"),
      (val_min, ":max_random", ":quest_target_amount"),
      (val_add, ":max_random", 1),
      (store_random_in_range, ":random_number", 1, ":max_random"),
      (assign, "$g_train_peasants_against_bandits_num_peasants", ":random_number"),
      (assign, reg0, ":random_number"),
      (store_sub, reg1, ":random_number", 1),
      (str_store_troop_name_by_count, s0, "trp_trainee_peasant", ":random_number"),
     ],
    [
      ("peasant_start_practice", [], "Start the practice fight.",
       [
         (set_jump_mission,"mt_minorplanet_training"),
         (quest_get_slot, ":target_center", "qst_train_peasants_against_bandits", slot_quest_target_center),
         (party_get_slot, ":minorplanet_scene", ":target_center", slot_spacestation_exterior),
         (modify_visitors_at_site, ":minorplanet_scene"),
         (reset_visitors),
         (set_visitor, 0, "trp_player"),
         (set_visitors, 1, "trp_trainee_peasant", "$g_train_peasants_against_bandits_num_peasants"),
         (set_jump_entry, 11),
         (jump_to_scene, ":minorplanet_scene"),
         (jump_to_menu, "mnu_train_peasants_against_bandits_training_result"),
         (music_set_situation, 0),
         (change_screen_mission),
         ]),
      ]
    ),

  (
    "train_peasants_against_bandits_training_result",menu_text_color(0xFF000d2c)|mnf_disable_all_keys,
    "{s0}",
    "none",
    [
      (assign, reg5, "$g_train_peasants_against_bandits_num_peasants"),
      (str_store_troop_name_by_count, s0, "trp_trainee_peasant", "$g_train_peasants_against_bandits_num_peasants"),
      (try_begin),
        (eq, "$g_train_peasants_against_bandits_training_succeeded", 0),
        (str_store_string, s0, "@You were beaten. The colonists are heartened by their success, but the lesson you wanted to teach them probably didn't get through..."),
      (else_try),
        (str_store_string, s0, "@After beating your last opponent, you explain to the colonists how to better defend themselves against such an attack. Hopefully they'll take the experience on board and will be prepared next time."),
        (quest_get_slot, ":quest_current_state", "qst_train_peasants_against_bandits", slot_quest_current_state),
        (val_add, ":quest_current_state", "$g_train_peasants_against_bandits_num_peasants"),
        (quest_set_slot, "qst_train_peasants_against_bandits", slot_quest_current_state, ":quest_current_state"),
      (try_end),
     ],
    [
      ("continue_3dot", [], "Continue...",
       [
         (try_begin),
           (quest_get_slot, ":quest_current_state", "qst_train_peasants_against_bandits", slot_quest_current_state),
           (quest_slot_eq, "qst_train_peasants_against_bandits", slot_quest_target_amount, ":quest_current_state"),
           (jump_to_menu, "mnu_train_peasants_against_bandits_attack"),
         (else_try),
           (change_screen_map),
         (try_end),
         ]),
      ]
    ),

  (
    "train_peasants_against_bandits_attack",menu_text_color(0xFF000d2c),
    "As you get ready to continue the training, a sentry from the planet runs up to you, shouting alarms.\
 The bandits have been spotted on the short range scanners, on an intercept course for {s3}.\
 The administrator begs that you organize your newly-trained militia and face them.",
    "none",
    [
	(str_store_party_name, s3, "$current_town"),
     ],
    [
      ("peasants_against_bandits_attack_resist", [], "Prepare for a fight!",
       [
        (store_random_in_range, ":random_no", 0, 3),
        (try_begin),
          (eq, ":random_no", 0),
          (assign, ":bandit_troop", "trp_bandit"),
        (else_try),
          (eq, ":random_no", 1),
          (assign, ":bandit_troop", "trp_black_sun_pirate_3"),
        (else_try),
          (assign, ":bandit_troop", "trp_blazing_claw_pirate"),
        (try_end),
        (party_get_slot, ":scene_to_use", "$g_encountered_party", slot_spacestation_exterior),
        (modify_visitors_at_site, ":scene_to_use"),
        (reset_visitors),
        (store_character_level, ":level", "trp_player"),
        (val_div, ":level", 2),
        (store_add, ":min_bandits", ":level", 16),
        (store_add, ":max_bandits", ":min_bandits", 6),
        (store_random_in_range, ":random_no", ":min_bandits", ":max_bandits"),
        (set_visitors, 0, ":bandit_troop", ":random_no"),
        (assign, ":num_villagers", ":max_bandits"),
        (set_visitors, 2, "trp_trainee_peasant", ":num_villagers"),
        (set_party_battle_mode),
        (set_battle_advantage, 0),
        (assign, "$g_battle_result", 0),
        (set_jump_mission,"mt_minorplanet_attack_bandits"),
        (jump_to_scene, ":scene_to_use"),
        (assign, "$g_next_menu", "mnu_train_peasants_against_bandits_attack_result"),
        (jump_to_menu, "mnu_battle_debrief"),
        (assign, "$g_mt_mode", vba_after_training),
        (change_screen_mission),
        ]),
      ]
    ),

  (
    "train_peasants_against_bandits_attack_result",menu_text_color(0xFF000d2c)|mnf_scale_picture|mnf_disable_all_keys,
    "{s9}",
    "none",
    [
      (try_begin),
        (eq, "$g_battle_result", 1),
        (str_store_string, s9, "@The bandits are broken!\
 Those few who remain alive and conscious run off with their tails between their legs,\
 terrified of the colonists and their new champion."),
	(call_script, "script_succeed_quest", "qst_train_peasants_against_bandits"),
        (jump_to_menu, "mnu_train_peasants_against_bandits_success"),
      (else_try),
        (call_script, "script_fail_quest", "qst_train_peasants_against_bandits"),
        (str_store_string, s9, "@Try as you might, you could not defeat the bandits.\
 Infuriated, they raze part of the planet to the ground to punish the colonists,\
 and then leave the burning wasteland behind to find greener pastures to plunder."),
        (set_background_mesh, "mesh_pic_looted_village"),
      (try_end),
     ],
    [
      ("continue_3dot", [], "Continue...",
       [(try_begin),
          (call_script, "script_minorplanet_set_state",  "$current_town", svs_looted),
          (party_set_slot, "$current_town", slot_minorplanet_raid_progress, 0),
          (party_set_slot, "$current_town", slot_minorplanet_recover_progress, 0),
          (call_script, "script_change_player_relation_with_center", "$g_encountered_party", -3),
          (call_script, "script_end_quest", "qst_train_peasants_against_bandits"),
        (try_end),
        (change_screen_map),
	 ]),
      ]
    ),

   (
    "train_peasants_against_bandits_success",menu_text_color(0xFF000d2c)|mnf_disable_all_keys,
    "The bandits are broken!\
 Those few who remain run off with their tails between their legs,\
 terrified of the colonists and their new champion.\
 The villagers have little left in the way of wealth after their ordeal,\
 but they offer you all they can find to show their gratitude.",
    "none",
    [(party_clear, "p_temp_party"),
     (call_script, "script_end_quest", "qst_train_peasants_against_bandits"),
     (call_script, "script_change_player_relation_with_center", "$g_encountered_party", 4),

     (party_get_slot, ":merchant_troop", "$current_town", slot_mainplanet_elder),
     (try_for_range, ":slot_no", num_equipment_kinds ,max_inventory_items + num_equipment_kinds),
        (store_random_in_range, ":rand", 0, 100),
        (lt, ":rand", 50),
        (troop_set_inventory_slot, ":merchant_troop", ":slot_no", -1),
     (try_end),
     (call_script, "script_add_log_entry", logent_helped_peasants, "trp_player",  "$current_town", -1, -1),
    ],
    [
      ("minorplanet_bandits_defeated_accept",[],"Take it as your just due.",[(jump_to_menu, "mnu_auto_return_to_map"),
                                                                         (party_get_slot, ":merchant_troop", "$current_town", slot_mainplanet_elder),
                                                                         (troop_sort_inventory, ":merchant_troop"),
                                                                         (change_screen_loot, ":merchant_troop"),
                                                                       ]),
      ("minorplanet_bandits_defeated_cont",[],  "Refuse, stating that they need these items more than you do.",[(call_script, "script_change_player_relation_with_center", "$g_encountered_party", 3),
                                                                                                             (call_script, "script_change_player_honor", 1),
                                                                                                                (change_screen_map)]),
    ],
  ),


  (
    "disembark",menu_text_color(0xFF000d2c),
    "Do you wish to disembark?",
    "none",
    [],
    [
      ("yes_dot", [], "Yes.",
       [(assign, "$g_player_icon_state", pis_normal),
        (party_set_flags, "p_main_party", pf_is_ship, 0),
        (party_get_position, pos1, "p_main_party"),
        (party_set_position, "p_main_party", pos0),
        (try_begin),
          (le, "$g_main_ship_party", 0),
          (set_spawn_radius, 0),
          (spawn_around_party, "p_main_party", "pt_none"),
          (assign, "$g_main_ship_party", reg0),
          (party_set_flags, "$g_main_ship_party", pf_is_static|pf_always_visible|pf_hide_defenders|pf_is_ship, 1),
          (str_store_troop_name, s1, "trp_player"),
          #SW - commented out so icon doesn't change, nevermind
		  (party_set_name, "$g_main_ship_party", "@{s1}'s Ship"),
          #(party_set_icon, "$g_main_ship_party", "icon_ship"),
		  (party_set_icon, "$g_main_ship_party", "icon_player"),
          (party_set_slot, "$g_main_ship_party", slot_party_type, spt_ship),
        (try_end),
        (enable_party, "$g_main_ship_party"),
        (party_set_position, "$g_main_ship_party", pos0),
        #SW - do not switch icon, nevermind
		#(party_set_icon, "$g_main_ship_party", "icon_ship_on_land"),
		(party_set_icon, "$g_main_ship_party", "icon_player"),
        (assign, "$g_main_ship_party", -1),
        (change_screen_return),
        ]),
      ("no_dot", [], "No.",
       [(change_screen_return),
        ]),
    ]
  ),

  (
    "ship_reembark",menu_text_color(0xFF000d2c),
    "Do you wish to embark?",
    "none",
    [],
    [
      ("yes_dot", [], "Yes.",
       [(assign, "$g_player_icon_state", pis_ship),
        (party_set_flags, "p_main_party", pf_is_ship, 1),
        (party_get_position, pos1, "p_main_party"),
        (map_get_water_position_around_position, pos2, pos1, 6),
        (party_set_position, "p_main_party", pos2),
        (assign, "$g_main_ship_party", "$g_encountered_party"),
        (disable_party, "$g_encountered_party"),
        (change_screen_return),
        ]),
      ("no_dot", [], "No.",
       [(change_screen_return),
        ]),
    ]
  ),

  (
    "center_reports",menu_text_color(0xFF000d2c),
    "Town Name: {s1}^Rent Income: {reg1} credits^Tariff Income: {reg2} credits^Food Stock: for {reg3} days",
    "none",
    [(party_get_slot, ":town_food_store", "$g_encountered_party", slot_party_food_store),
     (call_script, "script_center_get_food_consumption", "$g_encountered_party"),
     (assign, ":food_consumption", reg0),
     (store_div, reg3, ":town_food_store", ":food_consumption"),
     (str_store_party_name, s1, "$g_encountered_party"),
     (party_get_slot, reg1, "$g_encountered_party", slot_center_accumulated_rents),
     (party_get_slot, reg2, "$g_encountered_party", slot_center_accumulated_tariffs),
     ],
    [
      ("to_price_and_productions", [], "Show prices and productions.",
       [(jump_to_menu, "mnu_price_and_production"),
        ]),
      
      ("go_back_dot",[],"Go back.",
       [(try_begin),
          (party_slot_eq, "$g_encountered_party", slot_party_type, spt_minorplanet),
          (jump_to_menu, "mnu_village"),
        (else_try),
          (jump_to_menu, "mnu_town"),
        (try_end),
        ]),
    ]
  ),
    
  (
    "price_and_production",menu_text_color(0xFF000d2c),
    "Productions are:^{s1}^^Price factors are:^{s2}",
    "none",
    [(str_store_string, s1, "@ "),
     (str_store_string, s2, "@ "),
     (try_for_range, ":cur_good", trade_goods_begin, trade_goods_end),
       (store_sub, ":cur_good_slot", ":cur_good", trade_goods_begin),
       (val_add, ":cur_good_slot", slot_mainplanet_trade_good_productions_begin),
       (store_sub, ":cur_good_price_slot", ":cur_good", trade_goods_begin),
       (val_add, ":cur_good_price_slot", slot_mainplanet_trade_good_prices_begin),
       (party_get_slot, ":production", "$g_encountered_party", ":cur_good_slot"),
       (party_get_slot, ":price", "$g_encountered_party", ":cur_good_price_slot"),
       (str_store_item_name, s3, ":cur_good"),
       (assign, reg1, ":production"),
       (str_store_string, s1, "@^{s3} = {reg1}{s1}"),
       (assign, reg1, ":price"),
       (str_store_string, s2, "@^{s3} = {reg1}{s2}"),
     (try_end),
     ],
    [
      ("go_back_dot",[],"Go back.",
       [(try_begin),
          (party_slot_eq, "$g_encountered_party", slot_party_type, spt_minorplanet),
          (jump_to_menu, "mnu_village"),
        (else_try),
          (jump_to_menu, "mnu_town"),
        (try_end),
        ]),
    ]
  ),
  
  (
    "town_trade",menu_text_color(0xFF000d2c),
    "You head towards the marketplace.",
    "none",
    [],
    [
      ("assess_prices",[],
       "Assess the local prices.",
       [
           (jump_to_menu,"mnu_town_trade_assessment_begin"),
        ]),
      ("trade_with_arms_merchant",[(party_slot_ge, "$current_town", slot_mainplanet_weaponsmith, 1)],
       "Trade with the weapons merchant.",
       [
           (party_get_slot, ":merchant_troop", "$current_town", slot_mainplanet_weaponsmith),
           (change_screen_trade, ":merchant_troop"),
        ]),
      ("trade_with_armor_merchant",[(party_slot_ge, "$current_town", slot_mainplanet_armorer, 1)],
       "Trade with the armor merchant.",
       [
           (party_get_slot, ":merchant_troop", "$current_town", slot_mainplanet_armorer),
           (change_screen_trade, ":merchant_troop"),
        ]),
      ("trade_with_horse_merchant",[(party_slot_ge, "$current_town", slot_mainplanet_horse_merchant, 1)],
		#SW - modified horse merchant menu 
       "Trade with the transportation merchant.",
       [
           (party_get_slot, ":merchant_troop", "$current_town", slot_mainplanet_horse_merchant),
           (change_screen_trade, ":merchant_troop"),
        ]),
      ("trade_with_goods_merchant",[(party_slot_ge, "$current_town", slot_mainplanet_merchant, 1)],
       "Trade with the goods merchant.",
       [
           (party_get_slot, ":merchant_troop", "$current_town", slot_mainplanet_merchant),
           (change_screen_trade, ":merchant_troop"),
        ]),
#SW - integrated companions_overview		
######### JEDEDIAH Q START ######################################################
 	("Companions_overview",[],"Companions overview.",
        [
	(assign, "$jq_in_market_menu", 1), # player is in market menu

	# Exit if no companions #
	(assign, ":heroes_in_party", 0),
	(try_for_range, reg3, companions_begin, companions_end),
   	(main_party_has_troop, reg3),
	(val_add, ":heroes_in_party", 1),
	 (try_end),
	#(display_message, "@ {reg3"),
	    (try_begin),
	 	(eq, ":heroes_in_party", 0),
		(display_message,"@No companions in party!",0xFFFF0000),
	(else_try),
	(start_presentation, "prsnt_jq_companions_quickview"),
     	(try_end),
       	]),
######### JEDEDIAH Q END #############################################
      ("head_back",[],"Head back.",
       [
           (jump_to_menu,"mnu_town"),
        ]),
    ]
  ),

  (
    "town_trade_assessment_begin",menu_text_color(0xFF000d2c),
    "You overhear several discussions about the price of trade goods across the local area.\
 You listen closely, trying to work out the best deals around.",
    "none",
    [],
    [
      ("continue_3dot",[],"Continue...",
       [
           (assign,"$auto_enter_town","$current_town"),
           (assign, "$g_town_assess_trade_goods_after_rest", 1),
           (call_script, "script_get_max_skill_of_player_party", "skl_trade"),
           (val_div, reg0, 2),
           (store_sub, ":num_hours", 6, reg0),
           (assign, "$g_last_rest_center", "$current_town"),
           (assign, "$g_last_rest_payment_until", -1),
           (rest_for_hours, ":num_hours", 5, 0), #rest while not attackable
           (change_screen_return),
        ]),
    ]
  ),

  (
    "town_trade_assessment",menu_text_color(0xFF000d2c)|mnf_disable_all_keys,
    "As the party member with the highest trade skill ({reg2}), {reg3?you try to figure out:{s1} tries to figure out} the best goods to trade in. {s2}",
    "none",
    [(call_script, "script_get_max_skill_of_player_party", "skl_trade"),
     (assign, ":max_skill", reg0),
     (assign, ":max_skill_owner", reg1),

     (assign, ":num_best_results", 0),
     (assign, ":best_result_1_item", -1),
     (assign, ":best_result_1_town", -1),
     (assign, ":best_result_1_profit", 0),
     (assign, ":best_result_2_item", -1),
     (assign, ":best_result_2_town", -1),
     (assign, ":best_result_2_profit", 0),
     (assign, ":best_result_3_item", -1),
     (assign, ":best_result_3_town", -1),
     (assign, ":best_result_3_profit", 0),

     (store_sub, ":num_towns", mainplanets_end, mainplanets_begin),
     (store_sub, ":num_goods", trade_goods_end, trade_goods_begin),
     (store_mul, ":max_iteration", ":num_towns", ":num_goods"),
     (val_mul, ":max_iteration", ":max_skill"),
     (val_div, ":max_iteration", 20),

     (assign, ":org_encountered_party", "$g_encountered_party"),

     (try_for_range, ":unused", 0, ":max_iteration"),
       (store_random_in_range, ":random_trade_good", trade_goods_begin, trade_goods_end),
       (store_random_in_range, ":random_town", mainplanets_begin, mainplanets_end),
       (assign, ":already_best", 0),
       (try_begin),
         (eq, ":random_trade_good", ":best_result_1_item"),
         (eq, ":random_town", ":best_result_1_town"),
         (val_add, ":already_best", 1),
       (else_try),
         (eq, ":random_trade_good", ":best_result_2_item"),
         (eq, ":random_town", ":best_result_2_town"),
         (val_add, ":already_best", 1),
       (else_try),
         (eq, ":random_trade_good", ":best_result_3_item"),
         (eq, ":random_town", ":best_result_3_town"),
         (val_add, ":already_best", 1),
       (try_end),
       (eq, ":already_best", 0),
       (store_item_value, ":random_trade_good_price", ":random_trade_good"),
       (assign, "$g_encountered_party", ":org_encountered_party"),
       (call_script, "script_game_get_item_buy_price_factor", ":random_trade_good"),
       (store_mul, ":random_trade_good_buy_price", ":random_trade_good_price", reg0),
       (val_div, ":random_trade_good_buy_price", 100),
       (val_max, ":random_trade_good_buy_price", 1),
       (assign, "$g_encountered_party", ":random_town"),
       (call_script, "script_game_get_item_sell_price_factor", ":random_trade_good"),
       (store_mul, ":random_trade_good_sell_price", ":random_trade_good_price", reg0),
       (val_div, ":random_trade_good_sell_price", 100),
       (val_max, ":random_trade_good_sell_price", 1),
       (store_sub, ":difference", ":random_trade_good_sell_price", ":random_trade_good_buy_price"),
       (try_begin),
         (gt, ":difference", ":best_result_1_profit"),
         (val_add, ":num_best_results", 1),
         (val_min, ":num_best_results", 3),
         (assign, ":best_result_3_item", ":best_result_2_item"),
         (assign, ":best_result_3_town", ":best_result_2_town"),
         (assign, ":best_result_3_profit", ":best_result_2_profit"),
         (assign, ":best_result_2_item", ":best_result_1_item"),
         (assign, ":best_result_2_town", ":best_result_1_town"),
         (assign, ":best_result_2_profit", ":best_result_1_profit"),
         (assign, ":best_result_1_item", ":random_trade_good"),
         (assign, ":best_result_1_town", ":random_town"),
         (assign, ":best_result_1_profit", ":difference"),
       (else_try),
         (gt, ":difference", ":best_result_2_profit"),
         (val_add, ":num_best_results", 1),
         (val_min, ":num_best_results", 3),
         (assign, ":best_result_3_item", ":best_result_2_item"),
         (assign, ":best_result_3_town", ":best_result_2_town"),
         (assign, ":best_result_3_profit", ":best_result_2_profit"),
         (assign, ":best_result_2_item", ":random_trade_good"),
         (assign, ":best_result_2_town", ":random_town"),
         (assign, ":best_result_2_profit", ":difference"),
       (else_try),
         (gt, ":difference", ":best_result_3_profit"),
         (val_add, ":num_best_results", 1),
         (val_min, ":num_best_results", 3),
         (assign, ":best_result_3_item", ":random_trade_good"),
         (assign, ":best_result_3_town", ":random_town"),
         (assign, ":best_result_3_profit", ":difference"),
       (try_end),
     (try_end),

     (assign, "$g_encountered_party", ":org_encountered_party"),

     (str_clear, s3),
     
     (assign, reg2, ":max_skill"),
     (try_begin),
       (eq, ":max_skill_owner", "trp_player"),
       (assign, reg3, 1),
     (else_try),
       (assign, reg3, 0),
       (str_store_troop_name, s1, ":max_skill_owner"),
     (try_end),
     (try_begin),
       (le, ":num_best_results", 0),
       (str_store_string, s2, "@However, {reg3?You are:{s1} is} unable to find any trade goods that would bring a profit."),
     (else_try),
       (try_begin),
         (ge, ":best_result_3_item", 0),
         (assign, reg6, ":best_result_3_profit"),
         (str_store_item_name, s4, ":best_result_3_item"),
         (str_store_party_name, s5, ":best_result_3_town"),
         (str_store_string, s3, "@^Buying {s4} here and selling it at {s5} would bring a profit of {reg6} credits per item.{s3}"),
       (try_end),
       (try_begin),
         (ge, ":best_result_2_item", 0),
         (assign, reg6, ":best_result_2_profit"),
         (str_store_item_name, s4, ":best_result_2_item"),
         (str_store_party_name, s5, ":best_result_2_town"),
         (str_store_string, s3, "@^Buying {s4} here and selling it at {s5} would bring a profit of {reg6} credits per item.{s3}"),
       (try_end),
       (try_begin),
         (ge, ":best_result_1_item", 0),
         (assign, reg6, ":best_result_1_profit"),
         (str_store_item_name, s4, ":best_result_1_item"),
         (str_store_party_name, s5, ":best_result_1_town"),
         (str_store_string, s3, "@^Buying {s4} here and selling it at {s5} would bring a profit of {reg6} credits per item.{s3}"),
       (try_end),
       (str_store_string, s2, "@{reg3?You find:{s1} finds} out the following:^{s3}"),
     (try_end),
     ],
    [
      ("continue_3dot",[],"Continue...",
       [
           (jump_to_menu,"mnu_town_trade"),
        ]),
    ]
  ),

  (
    "sneak_into_town_suceeded",menu_text_color(0xFF000d2c),
    "Disguised in the garments of a citizen, you fool the guards and make your way onto the planet.",
    "none",
    [
		#SW - display a new menu background
		(call_script, "script_display_fullscreen_background", "$current_town"),			  
	],
    [
      ("continue_3dot",[],"Continue...",
       [
           (assign, "$sneaked_into_town",1),
           (jump_to_menu,"mnu_town"),
        ]),
    ]
  ),
  (
    "sneak_into_town_caught",menu_text_color(0xFF000d2c),
    "As you try to sneak in, one of the guards recognizes you and raises the alarm!\
 You must flee back to your ship before all the guards come down on you!",
    "none",
    [
       (assign,"$auto_menu","mnu_captivity_start_spacestation_surrender"),
    ],
    [
      ("sneak_caught_fight",[],"Try to fight your way out!",
       [
           (assign,"$all_doors_locked",1),
           (party_get_slot, ":sneak_scene", "$current_town",slot_mainplanet_center), # slot_mainplanet_gate),
           (modify_visitors_at_site,":sneak_scene"),(reset_visitors),
           (set_visitor,0,"trp_player"),
           (store_faction_of_party, ":town_faction","$current_town"),
           (faction_get_slot, ":tier_2_troop", ":town_faction", slot_faction_tier_2_troop),
           (faction_get_slot, ":tier_3_troop", ":town_faction", slot_faction_tier_3_troop),
           (try_begin),
             (gt, ":tier_2_troop", 0),
             (gt, ":tier_3_troop", 0),
             (assign,reg(0),":tier_3_troop"),
             (assign,reg(1),":tier_3_troop"),
             (assign,reg(2),":tier_2_troop"),
             (assign,reg(3),":tier_2_troop"),
           (else_try),
             (assign,reg(0),"trp_security_guard"),
             (assign,reg(1),"trp_security_guard"),
             (assign,reg(2),"trp_security_guard"),
             (assign,reg(3),"trp_security_guard"),
           (try_end),
           (assign,reg(4),-1),
           (shuffle_range,0,5),
           (set_visitor,1,reg(0)),
           (set_visitor,2,reg(1)),
           (set_visitor,3,reg(2)),
           (set_visitor,4,reg(3)),
           (set_jump_mission,"mt_sneak_caught_fight"),
 #          (jump_to_menu,"mnu_captivity_start_spacestation_defeat"),
           (set_passage_menu,"mnu_town"),
           (jump_to_scene,":sneak_scene"),
           (change_screen_mission),
        ]),
      ("surrender",[],"Surrender.",
       [
           (jump_to_menu,"mnu_captivity_start_spacestation_surrender"),
        ]),
    ]
  ),
  (
    "sneak_into_town_caught_dispersed_guards",menu_text_color(0xFF000d2c),
    "You drive off the guards and cover your trail before running off, easily losing your pursuers in the maze of streets.",
    "none",
    [],
    [
      ("continue_3dot",[],"Continue...",
       [
           (assign, "$sneaked_into_town",1),
           (assign, "$town_entered", 1),
           (jump_to_menu,"mnu_town"),
        ]),
    ]
  ),
  (
    "sneak_into_town_caught_ran_away",menu_text_color(0xFF000d2c),
    "You make your way back to your ship and quickly retreat to the safety of the stars.",
    "none",
    [],
    [
      ("continue_3dot",[],"Continue...",
       [
           (assign,"$auto_menu",-1),
           (store_encountered_party,"$last_sneak_attempt_town"),
           (store_current_hours,"$last_sneak_attempt_time"),
           (change_screen_return),
        ]),
    ]
  ),


  (
    "enemy_offer_ransom_for_prisoner",menu_text_color(0xFF000d2c),
    "{s2} offers you a sum of {reg12} credits if you are willing to sell him {s1}.",
    "none",
    [(call_script, "script_calculate_ransom_amount_for_troop", "$g_ransom_offer_troop"),
     (assign, reg12, reg0),
     (str_store_troop_name, s1, "$g_ransom_offer_troop"),
     (store_troop_faction, ":faction_no", "$g_ransom_offer_troop"),
     (str_store_faction_name, s2, ":faction_no"),
     ],
    [
      ("accept_offer",[],"Accept the offer.",
       [(troop_add_gold, "trp_player", reg12),
        (party_remove_prisoners, "$g_ransom_offer_party", "$g_ransom_offer_troop", 1),
        #(troop_set_slot, "$g_ransom_offer_troop", slot_troop_is_prisoner, 0),
        (call_script, "script_remove_troop_from_prison", "$g_ransom_offer_troop"),
        (change_screen_return),
        ]),
      ("ransom_reject",[],"Reject the offer.",
       [
        (call_script, "script_change_player_relation_with_troop", "$g_ransom_offer_troop", -4),
        (call_script, "script_change_player_honor", -1),
        (assign, "$g_ransom_offer_rejected", 1),
        (change_screen_return),
        ]),
    ]
  ),


  (
    "training_ground",menu_text_color(0xFF000d2c),
    "You approach a training field where you can practice your martial skills. What kind of training do you want to do?",
    "none",
    [
      (store_add, "$g_training_ground_melee_training_scene", "scn_training_ground_ranged_melee_1", "$g_encountered_party"),
      (val_sub, "$g_training_ground_melee_training_scene", training_grounds_begin),
      (try_begin),
        (ge, "$g_training_ground_training_count", 3),
        (assign, "$g_training_ground_training_count", 0),
        (rest_for_hours, 1, 5, 1), #rest while attackable
        (assign, "$auto_enter_town", "$g_encountered_party"),
        (change_screen_return),
      (try_end),
      ],
    [
	  #SW - modified training menu's
      ("camp_trainer",
       [], "Speak with the trainer.",
       [
         (set_jump_mission, "mt_training_ground_trainer_talk"),
         (modify_visitors_at_site, "$g_training_ground_melee_training_scene"),
         (reset_visitors),
         (set_jump_entry, 5),
         (jump_to_scene, "$g_training_ground_melee_training_scene"),
         (change_screen_mission),
         (music_set_situation, 0),
         ]),
      ("camp_train_melee",
       [
         (neg|troop_is_wounded, "trp_player"),
         (call_script, "script_party_count_fit_for_battle", "p_main_party"),
         (gt, reg0, 1),
         ], "Sparring practice.",
       [
         (assign, "$g_mt_mode", ctm_melee),
         (jump_to_menu, "mnu_training_ground_selection_details_melee_1"),
         (music_set_situation, 0),
         ]),
      ("camp_train_archery",[], "Ranged weapon practice.",
       [
         (jump_to_menu, "mnu_training_ground_selection_details_ranged_1"),
         (music_set_situation, 0),
         ]),
      ("camp_train_mounted",[], "Speeder bike practice.",
       [
         (assign, "$g_mt_mode", ctm_mounted),
         (jump_to_menu, "mnu_training_ground_selection_details_mounted"),
         (music_set_situation, 0),
         ]),
#SW BSG integration
      ("space_entry",[],"Space combat practice.",
       [         
		   #(set_jump_mission,"mt_visit_town_castle"),
		   (set_jump_mission,"mt_space_battle_entry"),
		   #(set_jump_mission,"mt_space_prop"),
#           (jump_to_scene,"scn_space_battle"),
		   (jump_to_scene,"scn_space_battle_entry"),
           (change_screen_mission),
		   #(change_screen_mission)],"Door to the tavern."),
	       ]),

      ("leave_dot",[],"Leave.",
       [(change_screen_return),
        ]),		   
		   
      #("space_battle",[]," ",  #make it a blank space so its not easy to select in the list
	  ("space_battle",[(eq, "$cheat_mode", 1)],"Cheat: Space Battle",  #make it only available in cheat mode so forces player to use the passage in space_battle_entry
       [         
           (set_jump_mission,"mt_space_battle"),
           (jump_to_scene,"scn_space_battle"),
           (change_screen_mission)
		 ],"Fly the spaceship."
       ),

      ("go_to_track",[(eq, "$cheat_mode", 1)],"Cheat: Go to track.",
       [
         (set_jump_mission, "mt_ai_training"),
         (store_add, ":scene_no", "scn_training_ground_horse_track_1", "$g_encountered_party"),
         (val_sub, ":scene_no", training_grounds_begin),
         (jump_to_scene, ":scene_no"),
         (change_screen_mission),
        ]
       ),
      ("go_to_range",[(eq, "$cheat_mode", 1)],"Cheat: Go to range.",
       [
         (set_jump_mission, "mt_ai_training"),
         (jump_to_scene, "$g_training_ground_melee_training_scene"),
         (change_screen_mission),
        ]
       ),
#      ("leave",[],"Leave.",
#       [(change_screen_return),
#        ]),
    ]
  ),

  ("training_ground_selection_details_melee_1",menu_text_color(0xFF000d2c),
   "How many opponents will you go against?",
   "none",
   [
     (call_script, "script_write_fit_party_members_to_stack_selection", "p_main_party", 1),
     (troop_get_slot, "$temp", "trp_stack_selection_amounts", 1), #number of men fit
     (assign, "$temp_2", 1),
     ],
    [
      ("one",[(ge, "$temp", 1)], "One.",
       [
         (assign, "$temp", 1),
         (jump_to_menu, "mnu_training_ground_selection_details_melee_2"),
         ]),
      ("two",[(ge, "$temp", 2)], "Two.",
       [
         (assign, "$temp", 2),
         (jump_to_menu, "mnu_training_ground_selection_details_melee_2"),
         ]),
      ("three",[(ge, "$temp", 3)], "Three.",
       [
         (assign, "$temp", 3),
         (jump_to_menu, "mnu_training_ground_selection_details_melee_2"),
         ]),
      ("four",[(ge, "$temp", 4)], "Four.",
       [
         (assign, "$temp", 4),
         (jump_to_menu, "mnu_training_ground_selection_details_melee_2"),
         ]),
      ("cancel_dot",[],"Cancel.",
       [
         (jump_to_menu, "mnu_training_ground"),
        ]),
      ]
  ),

  ("training_ground_selection_details_melee_2",menu_text_color(0xFF000d2c),
   "Choose your opponent #{reg1}:",
   "none",
   [
     (assign, reg1, "$temp_2"),
     (troop_get_slot, "$temp_3", "trp_stack_selection_amounts", 0), #number of slots
     ],
    [
      ("s0", [(call_script, "script_cf_training_ground_sub_routine_1_for_melee_details", 1),], "{s0}",
       [(call_script, "script_training_ground_sub_routine_2_for_melee_details", 1),]),
      ("s0", [(call_script, "script_cf_training_ground_sub_routine_1_for_melee_details", 2),], "{s0}",
       [(call_script, "script_training_ground_sub_routine_2_for_melee_details", 2),]),
      ("s0", [(call_script, "script_cf_training_ground_sub_routine_1_for_melee_details", 3),], "{s0}",
       [(call_script, "script_training_ground_sub_routine_2_for_melee_details", 3),]),
      ("s0", [(call_script, "script_cf_training_ground_sub_routine_1_for_melee_details", 4),], "{s0}",
       [(call_script, "script_training_ground_sub_routine_2_for_melee_details", 4),]),
      ("s0", [(call_script, "script_cf_training_ground_sub_routine_1_for_melee_details", 5),], "{s0}",
       [(call_script, "script_training_ground_sub_routine_2_for_melee_details", 5),]),
      ("s0", [(call_script, "script_cf_training_ground_sub_routine_1_for_melee_details", 6),], "{s0}",
       [(call_script, "script_training_ground_sub_routine_2_for_melee_details", 6),]),
      ("s0", [(call_script, "script_cf_training_ground_sub_routine_1_for_melee_details", 7),], "{s0}",
       [(call_script, "script_training_ground_sub_routine_2_for_melee_details", 7),]),
      ("s0", [(call_script, "script_cf_training_ground_sub_routine_1_for_melee_details", 8),], "{s0}",
       [(call_script, "script_training_ground_sub_routine_2_for_melee_details", 8),]),
      ("s0", [(call_script, "script_cf_training_ground_sub_routine_1_for_melee_details", 9),], "{s0}",
       [(call_script, "script_training_ground_sub_routine_2_for_melee_details", 9),]),
      ("s0", [(call_script, "script_cf_training_ground_sub_routine_1_for_melee_details", 10),], "{s0}",
       [(call_script, "script_training_ground_sub_routine_2_for_melee_details", 10),]),
      ("s0", [(call_script, "script_cf_training_ground_sub_routine_1_for_melee_details", 11),], "{s0}",
       [(call_script, "script_training_ground_sub_routine_2_for_melee_details", 11),]),
      ("s0", [(call_script, "script_cf_training_ground_sub_routine_1_for_melee_details", 12),], "{s0}",
       [(call_script, "script_training_ground_sub_routine_2_for_melee_details", 12),]),
      ("s0", [(call_script, "script_cf_training_ground_sub_routine_1_for_melee_details", 13),], "{s0}",
       [(call_script, "script_training_ground_sub_routine_2_for_melee_details", 13),]),
      ("s0", [(call_script, "script_cf_training_ground_sub_routine_1_for_melee_details", 14),], "{s0}",
       [(call_script, "script_training_ground_sub_routine_2_for_melee_details", 14),]),
      ("s0", [(call_script, "script_cf_training_ground_sub_routine_1_for_melee_details", 15),], "{s0}",
       [(call_script, "script_training_ground_sub_routine_2_for_melee_details", 15),]),
      ("s0", [(call_script, "script_cf_training_ground_sub_routine_1_for_melee_details", 16),], "{s0}",
       [(call_script, "script_training_ground_sub_routine_2_for_melee_details", 16),]),
      ("s0", [(call_script, "script_cf_training_ground_sub_routine_1_for_melee_details", 17),], "{s0}",
       [(call_script, "script_training_ground_sub_routine_2_for_melee_details", 17),]),
      ("s0", [(call_script, "script_cf_training_ground_sub_routine_1_for_melee_details", 18),], "{s0}",
       [(call_script, "script_training_ground_sub_routine_2_for_melee_details", 18),]),
      ("s0", [(call_script, "script_cf_training_ground_sub_routine_1_for_melee_details", 19),], "{s0}",
       [(call_script, "script_training_ground_sub_routine_2_for_melee_details", 19),]),
      ("s0", [(call_script, "script_cf_training_ground_sub_routine_1_for_melee_details", 20),], "{s0}",
       [(call_script, "script_training_ground_sub_routine_2_for_melee_details", 20),]),
      ("training_ground_selection_details_melee_random", [], "Choose randomly.",
       [(call_script, "script_training_ground_sub_routine_2_for_melee_details", -1),]),
      ("go_back_dot",[],"Go back.",
       [(jump_to_menu, "mnu_training_ground"),
        ]
       ),
      ]
  ),


  #SW - modified mounted training weapons
  ("training_ground_selection_details_mounted",menu_text_color(0xFF000d2c),
   "What kind of weapon do you want to train with?",
   "none",
   [],
    [
      ("camp_train_mounted_details_1",[], "Lightsaber",
       [
         (call_script, "script_start_training_at_training_ground", itp_type_two_handed_wpn, 0),
         ]),
      ("camp_train_rweapon_a",[], "Force Throw Lightsaber",
       [
         (call_script, "script_start_training_at_training_ground", itp_type_thrown, 0),
         ]),
      ("camp_train_rweapon_b",[], "DL-44 Blaster",
       [
         (call_script, "script_start_training_at_training_ground", itp_type_pistol, 0),
         ]),
      ("camp_train_rweapon_c",[], "DLT-19 Rifle",
       [
         (call_script, "script_start_training_at_training_ground", itp_type_musket, 0),
         ]),		 
      ("go_back_dot",[],"Go back.",
       [(jump_to_menu, "mnu_training_ground"),
        ]
       ),
      ]
  ),


  ("training_ground_selection_details_ranged_1",menu_text_color(0xFF000d2c),
   "What kind of ranged weapon do you want to train with?",
   "none",
   [],
    [
      ("camp_train_rweapon_a",[], "Force Throw Lightsaber",
       [
         (assign, "$g_mt_mode", ctm_ranged),
		 (assign, "$temp", itp_type_thrown),
         (jump_to_menu, "mnu_training_ground_selection_details_ranged_2"),
         ]),
      ("camp_train_rweapon_b",[], "DL-44 Blaster",
       [
         (assign, "$g_mt_mode", ctm_ranged),
		 (assign, "$temp", itp_type_pistol),
         (jump_to_menu, "mnu_training_ground_selection_details_ranged_2"),
         ]),
      ("camp_train_rweapon_c",[], "DLT-19 Rifle",
       [
         (assign, "$g_mt_mode", ctm_ranged),
		 (assign, "$temp", itp_type_musket),
         (jump_to_menu, "mnu_training_ground_selection_details_ranged_2"),
         ]),
		 
      ("go_back_dot",[],"Go back.",
       [(jump_to_menu, "mnu_training_ground"),
        ]
       ),
      ]
  ),


  ("training_ground_selection_details_ranged_2",menu_text_color(0xFF000d2c),
   "What range do you want to practice at?",
   "none",
   [],
    [
      ("camp_train_ranged_details_1",[], "10 yards.",
       [
         (call_script, "script_start_training_at_training_ground", "$temp", 10),
         ]),
      ("camp_train_ranged_details_2",[], "20 yards.",
       [
         (call_script, "script_start_training_at_training_ground", "$temp", 20),
         ]),
      ("camp_train_ranged_details_3",[], "30 yards.",
       [
         (call_script, "script_start_training_at_training_ground", "$temp", 30),
         ]),
      ("camp_train_ranged_details_4",[], "40 yards.",
       [
         (call_script, "script_start_training_at_training_ground", "$temp", 40),
         ]),
      ("camp_train_ranged_details_5",[(eq, "$g_mt_mode", ctm_ranged),], "50 yards.",
       [
         (call_script, "script_start_training_at_training_ground", "$temp", 50),
         ]),
      ("camp_train_ranged_details_6",[(eq, "$g_mt_mode", ctm_ranged),], "60 yards.",
       [
         (call_script, "script_start_training_at_training_ground", "$temp", 60),
         ]),
      ("camp_train_ranged_details_7",[(eq, "$g_mt_mode", ctm_ranged),], "70 yards.",
       [
         (call_script, "script_start_training_at_training_ground", "$temp", 70),
         ]),
      ("go_back_dot",[],"Go back.",
       [(jump_to_menu, "mnu_training_ground"),
        ]
       ),
      ]
  ),


  ("training_ground_description",menu_text_color(0xFF000d2c),
   "{s0}",
   "none",
   [],
    [
      ("continue_3dot", [], "Continue...",
       [
         (set_jump_mission, "mt_training_ground_training"),
         (jump_to_scene, "$g_training_ground_training_scene"),
         (change_screen_mission),
        ]
       ),
      ]
  ),

  ("training_ground_training_result",menu_text_color(0xFF000d2c)|mnf_disable_all_keys,
   "{s7}{s2}",
   "none",
   [
     (store_skill_level, ":trainer_skill", "skl_trainer", "trp_player"),
     (store_add, ":trainer_skill_multiplier", 5, ":trainer_skill"),
     (call_script, "script_write_fit_party_members_to_stack_selection", "p_main_party", 1),
     (str_clear, s2),
     (troop_get_slot, ":num_fit", "trp_stack_selection_amounts", 1),
     (troop_get_slot, ":num_slots", "trp_stack_selection_amounts", 0),
     (try_begin),
       (gt, "$g_training_ground_training_success_ratio", 0),
       (store_mul, ":xp_ratio_to_add", "$g_training_ground_training_success_ratio", "$g_training_ground_training_success_ratio"),
       (try_begin),
         (eq, "$g_training_ground_training_success_ratio", 100),
         (val_mul, ":xp_ratio_to_add", 2), #2x when perfect
       (try_end),
       (try_begin),
         (eq, "$g_mt_mode", ctm_melee),
         (val_div, ":xp_ratio_to_add", 2),
       (try_end),
       (val_div, ":xp_ratio_to_add", 10), # value over 1000
       (try_begin),
         (gt, ":num_fit", 8),
         (val_mul, ":xp_ratio_to_add", 3),
         (assign, ":divisor", ":num_fit"),
         (convert_to_fixed_point, ":divisor"),
         (store_sqrt, ":divisor", ":divisor"),
         (convert_to_fixed_point, ":xp_ratio_to_add"),
         (val_div, ":xp_ratio_to_add", ":divisor"),
       (try_end),
##       (assign, reg0, ":xp_ratio_to_add"),
##       (display_message, "@xp earn ratio: {reg0}/1000"),
       (store_mul, ":xp_ratio_to_add_with_trainer_skill", ":xp_ratio_to_add", ":trainer_skill_multiplier"),
       (val_div, ":xp_ratio_to_add_with_trainer_skill", 10),
       (party_get_num_companion_stacks, ":num_stacks", "p_main_party"),
       (store_add, ":end_cond", ":num_slots", 2),
       (try_for_range, ":i_slot", 2, ":end_cond"),
         (troop_get_slot, ":amount", "trp_stack_selection_amounts", ":i_slot"),
         (troop_get_slot, ":troop_id", "trp_stack_selection_ids", ":i_slot"),
         (assign, ":end_cond_2", ":num_stacks"),
         (try_for_range, ":stack_no", 0, ":end_cond_2"),
           (party_stack_get_troop_id, ":stack_troop", "p_main_party", ":stack_no"),
           (eq, ":stack_troop", ":troop_id"),
           (assign, ":end_cond_2", 0), #break
           (call_script, "script_cf_training_ground_sub_routine_for_training_result", ":troop_id", ":stack_no", ":amount", ":xp_ratio_to_add_with_trainer_skill"),
           (str_store_troop_name_by_count, s1, ":troop_id", ":amount"),
           (assign, reg1, ":amount"),
           (str_store_string, s2, "@{s2}^{reg1} {s1} earned {reg0} experience."),
         (try_end),
       (try_end),
       (try_begin),
         (eq, "$g_mt_mode", ctm_melee),
         (store_mul, ":special_xp_ratio_to_add", ":xp_ratio_to_add", 3),
         (val_div, ":special_xp_ratio_to_add", 2),
         (try_for_range, ":enemy_index", 0, "$g_training_ground_training_num_enemies"),
           (troop_get_slot, ":troop_id", "trp_temp_array_a", ":enemy_index"),
           (assign, ":end_cond_2", ":num_stacks"),
           (try_for_range, ":stack_no", 0, ":end_cond_2"),
             (party_stack_get_troop_id, ":stack_troop", "p_main_party", ":stack_no"),
             (eq, ":stack_troop", ":troop_id"),
             (assign, ":end_cond_2", 0), #break
             (call_script, "script_cf_training_ground_sub_routine_for_training_result", ":troop_id", ":stack_no", 1, ":special_xp_ratio_to_add"),
             (str_store_troop_name, s1, ":troop_id"),
             (str_store_string, s2, "@{s2}^{s1} earned an additional {reg0} experience."),
           (try_end),
         (try_end),
       (try_end),
       (try_begin),
         (call_script, "script_cf_training_ground_sub_routine_for_training_result", "trp_player", -1, 1, ":xp_ratio_to_add"),
         (str_store_string, s2, "@^You earned {reg0} experience.{s2}"),
       (try_end),
     (try_end),
     (try_begin),
       (eq, "$g_training_ground_training_success_ratio", 0),
       (str_store_string, s7, "@The training didn't go well at all."),
     (else_try),
       (lt, "$g_training_ground_training_success_ratio", 25),
       (str_store_string, s7, "@The training didn't go well at all."),
     (else_try),
       (lt, "$g_training_ground_training_success_ratio", 50),
       (str_store_string, s7, "@The training didn't go very well."),
     (else_try),
       (lt, "$g_training_ground_training_success_ratio", 75),
       (str_store_string, s7, "@The training went quite well."),
     (else_try),
       (lt, "$g_training_ground_training_success_ratio", 99),
       (str_store_string, s7, "@The training went very well."),
     (else_try),
       (str_store_string, s7, "@The training went perfectly."),
     (try_end),
     
     ],
    [
      ("continue_3dot",[],"Continue...",
       [(jump_to_menu, "mnu_training_ground"),
        ]
       ),
      ]
   ),
  
  ("marshall_selection_candidate_ask",menu_text_color(0xFF000d2c),
   "{s15} will soon select a new marshall for {s23}. Some of the lords have suggested your name as a likely candidate.",
   "none",
   [
     (try_begin),
       (eq, "$g_presentation_marshall_selection_ended", 1),
       (change_screen_return),
     (try_end),
     (faction_get_slot, ":king", "$players_faction", slot_faction_leader),
     (str_store_troop_name, s15, ":king"),
     (str_store_faction_name, s23, "$players_faction"),
     ],
    [
      ("marshall_candidate_accept", [], "Let {s15} learn that you are willing to serve as marshall.",
       [
         (start_presentation, "prsnt_marshall_selection"),
        ]
       ),
      ("marshall_candidate_reject", [], "Tell everyone that you are too busy these days.",
       [
         (try_begin),
           (eq, "$g_presentation_marshall_selection_max_renown_2_troop", "trp_player"),
           (assign, "$g_presentation_marshall_selection_max_renown_2", "$g_presentation_marshall_selection_max_renown_3"),
           (assign, "$g_presentation_marshall_selection_max_renown_2_troop", "$g_presentation_marshall_selection_max_renown_3_troop"),
         (else_try),
           (assign, "$g_presentation_marshall_selection_max_renown_1", "$g_presentation_marshall_selection_max_renown_2"),
           (assign, "$g_presentation_marshall_selection_max_renown_1_troop", "$g_presentation_marshall_selection_max_renown_2_troop"),
           (assign, "$g_presentation_marshall_selection_max_renown_2", "$g_presentation_marshall_selection_max_renown_3"),
           (assign, "$g_presentation_marshall_selection_max_renown_2_troop", "$g_presentation_marshall_selection_max_renown_3_troop"),
         (try_end),
         (start_presentation, "prsnt_marshall_selection"),
        ]
       ),
      ]
  ),



  
##    [
##      ("renew_oath",[],"Renew your oath to {s1} for another month.",[
##          (store_current_day, ":cur_day"),
##          (store_add, "$g_oath_end_day", ":cur_day", 30),
##          (change_screen_return)]),
##      ("dont_renew_oath",[],"Become free of your bond.",[
##          (assign, "$players_faction",0),
##          (assign, "$g_player_permitted_castles", 0),
##          (change_screen_return)]),
##    ]
##  ),


#####################################################################
## Captivity....
#####################################################################
#####################################################################
#####################################################################
#####################################################################
  (
    "captivity_avoid_wilderness",menu_text_color(0xFF000d2c),
    "Suddenly all the world goes black around you.\
 Many hours later you regain your conciousness and find yourself at the spot you fell.\
 Your enemies must have taken you up for dead and left you there.\
 However, it seems that none of your wound were lethal,\
 and altough you feel awful, you find out that can still walk.\
 You get up and try to look for any other survivors from your party.",
    "none",
    [
      ],
    []
  ),

  (
    "captivity_start_wilderness",menu_text_color(0xFF000d2c),
    "Stub",
    "none",
    [
          (assign, "$g_player_is_captive", 1),
          (try_begin),
            (eq,"$g_player_surrenders",1),
            (jump_to_menu, "mnu_captivity_start_wilderness_surrender"), 
          (else_try),
            (jump_to_menu, "mnu_captivity_start_wilderness_defeat"), 
          (try_end),
      ],
    []
  ),
  
  (
    "captivity_start_wilderness_surrender",menu_text_color(0xFF000d2c),
    "Stub",
    "none",
    [
       (assign, "$g_player_is_captive", 1),
       (assign,"$auto_menu",-1), #We need this since we may come here by something other than auto_menu
       (assign, "$capturer_party", "$g_encountered_party"),
       (jump_to_menu, "mnu_captivity_wilderness_taken_prisoner"),
      ],
    []
  ),
  (
    "captivity_start_wilderness_defeat",menu_text_color(0xFF000d2c),
    "Your enemies take you prisoner.",
    "none",
    [
       (assign, "$g_player_is_captive", 1),
       (assign,"$auto_menu",-1),
       (assign, "$capturer_party", "$g_encountered_party"),
       (jump_to_menu, "mnu_captivity_wilderness_taken_prisoner"),
    ],
    []
  ),
  (
    "captivity_start_spacestation_surrender",menu_text_color(0xFF000d2c),
    "Stub",
    "none",
    [
       (assign, "$g_player_is_captive", 1),
       (assign,"$auto_menu",-1),
       (assign, "$capturer_party", "$g_encountered_party"),
       (jump_to_menu, "mnu_captivity_spacestation_taken_prisoner"),
      ],
    []
  ),
  (
    "captivity_start_spacestation_defeat",menu_text_color(0xFF000d2c),
    "Stub",
    "none",
    [
       (assign, "$g_player_is_captive", 1),
       (assign,"$auto_menu",-1),
       (assign, "$capturer_party", "$g_encountered_party"),
       (jump_to_menu, "mnu_captivity_spacestation_taken_prisoner"),
      ],
    []
  ),
  (
    "captivity_start_under_siege_defeat",menu_text_color(0xFF000d2c),
    "Your enemies take you prisoner.",
    "none",
    [
       (assign, "$g_player_is_captive", 1),
       (assign,"$auto_menu",-1),
       (assign, "$capturer_party", "$g_encountered_party"),
       (jump_to_menu, "mnu_captivity_spacestation_taken_prisoner"),
    ],
    []
  ),
  
  (
    "captivity_wilderness_taken_prisoner",menu_text_color(0xFF000d2c)|mnf_scale_picture,
    "Your enemies take you prisoner.",
    "none",
    [
        (set_background_mesh, "mesh_pic_prisoner_wilderness"),
     ],
    [
      ("continue_3dot",[],"Continue...",
       [
         (try_for_range, ":npc", companions_begin, companions_end),
           (main_party_has_troop, ":npc"),
           (store_random_in_range, ":rand", 0, 100),
           (lt, ":rand", 30),
           (remove_member_from_party, ":npc", "p_main_party"),
           (troop_set_slot, ":npc", slot_troop_occupation, 0),
           (troop_set_slot, ":npc", slot_troop_playerparty_history, pp_history_scattered),
           (assign, "$last_lost_companion", ":npc"),
           (store_faction_of_party, ":victorious_faction", "$g_encountered_party"),
           (troop_set_slot, ":npc", slot_troop_playerparty_history_string, ":victorious_faction"),
           (troop_set_health, ":npc", 100),
           (store_random_in_range, ":rand_town", mainplanets_begin, mainplanets_end),
           (troop_set_slot, ":npc", slot_troop_cur_center, ":rand_town"),
           (assign, ":nearest_town_dist", 1000),
           (try_for_range, ":town_no", mainplanets_begin, mainplanets_end),
             (store_faction_of_party, ":town_fac", ":town_no"),
             (store_relation, ":reln", ":town_fac", "fac_player_faction"),
             (ge, ":reln", 0),
             (store_distance_to_party_from_party, ":dist", ":town_no", "p_main_party"),
             (lt, ":dist", ":nearest_town_dist"),
             (assign, ":nearest_town_dist", ":dist"),
             (troop_set_slot, ":npc", slot_troop_cur_center, ":town_no"),
           (try_end),
         (try_end),

         (set_camera_follow_party, "$capturer_party"),
         (assign, "$g_player_is_captive", 1),
         (store_random_in_range, ":random_hours", 18, 30),
         (call_script, "script_event_player_captured_as_prisoner"),
         (call_script, "script_stay_captive_for_hours", ":random_hours"),
         (assign,"$auto_menu","mnu_captivity_wilderness_check"),
         (change_screen_return),
         ]),
      ]
  ),
  (
    "captivity_wilderness_check",menu_text_color(0xFF000d2c),
    "stub",
    "none",
    [(jump_to_menu,"mnu_captivity_end_wilderness_escape")],
    []
  ),
  (
    "captivity_end_wilderness_escape",menu_text_color(0xFF000d2c)|mnf_scale_picture,
    "After painful days of being dragged about as a prisoner, you find a chance and escape from your captors!",
    "none",
    [
        (play_cue_track, "track_escape"),
        (troop_get_type, ":is_female", "trp_player"),
        (try_begin),
          (eq, ":is_female", 1),
          (set_background_mesh, "mesh_pic_escape_1_fem"),
        (else_try),
          (set_background_mesh, "mesh_pic_escape_1"),
        (try_end),
    ],
    [
      ("continue_3dot",[],"Continue...",
       [
           (assign, "$g_player_is_captive", 0),
           (try_begin),
             (party_is_active, "$capturer_party"),
             (party_relocate_near_party, "p_main_party", "$capturer_party", 2),
           (try_end),
           (call_script, "script_set_parties_around_player_ignore_player", 2, 6),
           (assign, "$g_player_icon_state", pis_normal),
           (set_camera_follow_party, "p_main_party"),
           (rest_for_hours, 0, 0, 0), #stop resting
           (change_screen_return),
        ]),
    ]
  ),
  (
    "captivity_spacestation_taken_prisoner",menu_text_color(0xFF000d2c),
    "You are quickly surrounded by guards who take away your weapons. With curses and insults, they throw you into the brig where you must while away the miserable days of your captivity.",
    "none",
    [
        (troop_get_type, ":is_female", "trp_player"),
        (try_begin),
          (eq, ":is_female", 1),
          (set_background_mesh, "mesh_pic_prisoner_fem"),
        (else_try),
          (set_background_mesh, "mesh_pic_prisoner_man"),
        (try_end),
    ],
    [
      ("continue_3dot",[],"Continue...",
       [
           (assign, "$g_player_is_captive", 1),
           (store_random_in_range, ":random_hours", 16, 22),
           (call_script, "script_event_player_captured_as_prisoner"),
           (call_script, "script_stay_captive_for_hours", ":random_hours"),
           (assign,"$auto_menu", "mnu_captivity_spacestation_check"),
           (change_screen_return)
        ]),
    ]
  ),
  (
    "captivity_rescue_lord_taken_prisoner",menu_text_color(0xFF000d2c),
    "You remain in disguise for as long as possible before revealing yourself.\
 The guards are outraged and beat you savagely before throwing you back into the cell for God knows how long...",
    "none",
    [
        (troop_get_type, ":is_female", "trp_player"),
        (try_begin),
          (eq, ":is_female", 1),
          (set_background_mesh, "mesh_pic_prisoner_fem"),
        (else_try),
          (set_background_mesh, "mesh_pic_prisoner_man"),
        (try_end),
   ],
    [
      ("continue_3dot",[],"Continue...",
       [
           (assign, "$g_player_is_captive", 1),
           (store_random_in_range, ":random_hours", 16, 22),
           (call_script, "script_event_player_captured_as_prisoner"),
           (call_script, "script_stay_captive_for_hours", ":random_hours"),
           (assign,"$auto_menu", "mnu_captivity_spacestation_check"),
           (change_screen_return),
        ]),
    ]
  ),
  (
    "captivity_spacestation_check",menu_text_color(0xFF000d2c),
    "stub",
    "none",
    [
        (store_random_in_range, reg(7), 0, 10),
        (try_begin),
          (lt, reg(7), 4),
          (store_random_in_range, "$player_ransom_amount", 3, 6),
          (val_mul, "$player_ransom_amount", 100),
          (store_troop_gold, reg(3), "trp_player"),
          (gt, reg(3), "$player_ransom_amount"),
          (jump_to_menu,"mnu_captivity_end_propose_ransom"),
        (else_try),
          (lt, reg(7), 7),
          (jump_to_menu,"mnu_captivity_end_exchanged_with_prisoner"),
        (else_try),
          (jump_to_menu,"mnu_captivity_spacestation_remain"),
        (try_end),
    ],
    []
  ),
  (
    "captivity_end_exchanged_with_prisoner",menu_text_color(0xFF000d2c),
    "After days of imprisonment, you are finally set free when your captors exchange you with another prisoner.",
    "none",
    [
      (play_cue_track, "track_escape"),
      ],
    [
      ("continue_3dot",[],"Continue...",
       [
           (assign, "$g_player_is_captive", 0),
           (try_begin),
             (party_is_active, "$capturer_party"),
             (party_relocate_near_party, "p_main_party", "$capturer_party", 2),
           (try_end),
           (call_script, "script_set_parties_around_player_ignore_player", 2, 12),
           (assign, "$g_player_icon_state", pis_normal),
           (set_camera_follow_party, "p_main_party"),
           (rest_for_hours, 0, 0, 0), #stop resting
           (change_screen_return),
        ]),
    ]
  ),
  (
    "captivity_end_propose_ransom",menu_text_color(0xFF000d2c),
    "You spend long hours in the sunless dank of the brig, more than you can count.\
 Suddenly one of your captors enters your cell with an offer;\
 he proposes to free you in return for {reg5} credits of your hidden wealth. You decide to...",
    "none",
    [
        (store_character_level, ":player_level", "trp_player"),
        (store_mul, "$player_ransom_amount", ":player_level", 50),
        (val_add, "$player_ransom_amount", 100),
        (assign, reg5, "$player_ransom_amount"),
    ],
    [
      ("accept_offer",[(store_troop_gold,":player_gold", "trp_player"),
                                      (ge, ":player_gold","$player_ransom_amount")],"Accept the offer.",
       [
           (play_cue_track, "track_escape"),
           (assign, "$g_player_is_captive", 0),
           (troop_remove_gold, "trp_player", "$player_ransom_amount"), 
           (try_begin),
             (party_is_active, "$capturer_party"),
             (party_relocate_near_party, "p_main_party", "$capturer_party", 1),
           (try_end),
           (call_script, "script_set_parties_around_player_ignore_player", 2, 6),
           (assign, "$g_player_icon_state", pis_normal),
           (set_camera_follow_party, "p_main_party"),
           (rest_for_hours, 0, 0, 0), #stop resting
           (change_screen_return),
        ]),
      ("captivity_end_ransom_deny",[],"Refuse him, wait for something better.",
       [
           (assign, "$g_player_is_captive", 1),
           (store_random_in_range, reg(8), 16, 22),
           (call_script, "script_stay_captive_for_hours", reg8),
           (assign,"$auto_menu", "mnu_captivity_spacestation_check"),
           (change_screen_return),
        ]),
    ]
  ),
  (
    "captivity_spacestation_remain",menu_text_color(0xFF000d2c)|mnf_scale_picture|mnf_disable_all_keys,
    "More days pass in the darkness of your cell. You get through them as best you can,\
 enduring the kicks and curses of the guards, watching your underfed body waste away more and more...",
    "none",
    [
        (troop_get_type, ":is_female", "trp_player"),
        (try_begin),
          (eq, ":is_female", 1),
          (set_background_mesh, "mesh_pic_prisoner_fem"),
        (else_try),
          (set_background_mesh, "mesh_pic_prisoner_man"),
        (try_end),
        (store_random_in_range, ":random_hours", 16, 22),
        (call_script, "script_stay_captive_for_hours", ":random_hours"),
        (assign,"$auto_menu", "mnu_captivity_spacestation_check"),
        
    ],
    [
      ("continue_3dot",[],"Continue...",
       [
           (assign, "$g_player_is_captive", 1),
           (change_screen_return),
        ]),
    ]
  ),

  (
    "faction_army_quest_report_to_army",menu_text_color(0xFF000d2c)|mnf_scale_picture,
    "{s8} sends word that he wishes you to join his new military campaign.\
 You need to bring at least {reg13} troops to the army,\
 and are instructed to raise more men with all due haste if you do not have enough.",
    "none",
    [
        (set_background_mesh, "mesh_pic_messenger"),
        (quest_get_slot, ":quest_target_troop", "qst_report_to_army", slot_quest_target_troop),
        (quest_get_slot, ":quest_target_amount", "qst_report_to_army", slot_quest_target_amount),
        (call_script, "script_get_information_about_troops_position", ":quest_target_troop", 0),
        (str_clear, s9),
        (try_begin),
          (eq, reg0, 1), #troop is found and text is correct
          (str_store_string, s9, s1),
        (try_end),
        (str_store_troop_name, s8, ":quest_target_troop"),
        (assign, reg13, ":quest_target_amount"),
      ],
    [
      ("continue_3dot",[],"Continue...",
       [
           (quest_get_slot, ":quest_target_troop", "qst_report_to_army", slot_quest_target_troop),
           (quest_get_slot, ":quest_target_amount", "qst_report_to_army", slot_quest_target_amount),
           (str_store_troop_name_link, s13, ":quest_target_troop"),
           (assign, reg13, ":quest_target_amount"),
           (setup_quest_text, "qst_report_to_army"),
           (str_store_string, s2, "@{s13} asked you to report to him with at least {reg13} troops."),
           (call_script, "script_start_quest", "qst_report_to_army", ":quest_target_troop"),
           (call_script, "script_report_quest_troop_positions", "qst_report_to_army", ":quest_target_troop", 3),
           (change_screen_return),
        ]),
     ]
  ),

  (
    "faction_army_quest_messenger",menu_text_color(0xFF000d2c)|mnf_scale_picture,
    "{s8} sends word that he wishes to speak with you about a task he needs performed.\
 He requests you to come and see him as soon as possible.",
    "none",
    [
        (set_background_mesh, "mesh_pic_messenger"),
        (faction_get_slot, ":faction_marshall", "$players_faction", slot_faction_marshall),
        (str_store_troop_name, s8, ":faction_marshall"),
      ],
    [
      ("continue_3dot",[],"Continue...",
       [(change_screen_return),
        ]),
     ]
  ),

  (
    "faction_army_quest_join_siege_order",menu_text_color(0xFF000d2c)|mnf_scale_picture,
    "{s8} sends word that you are to join the siege of {s9} in preparation for a full assault.\
 Your troops are to take {s9} at all costs.",
    "none",
    [
        (set_background_mesh, "mesh_pic_messenger"),
        (faction_get_slot, ":faction_marshall", "$players_faction", slot_faction_marshall),
        (quest_get_slot, ":quest_target_center", "qst_join_siege_with_army", slot_quest_target_center),
        (str_store_troop_name, s8, ":faction_marshall"),
        (str_store_party_name, s9, ":quest_target_center"),
      ],
    [
      ("continue_3dot",[],"Continue...",
       [
           (call_script, "script_end_quest", "qst_follow_army"),
           (quest_get_slot, ":quest_target_center", "qst_join_siege_with_army", slot_quest_target_center),
           (faction_get_slot, ":faction_marshall", "$players_faction", slot_faction_marshall),
           (str_store_troop_name_link, s13, ":faction_marshall"),
           (str_store_party_name_link, s14, ":quest_target_center"),
           (setup_quest_text, "qst_join_siege_with_army"),
           (str_store_string, s2, "@{s13} ordered you to join the assault against {s14}."),
           (call_script, "script_start_quest", "qst_join_siege_with_army", ":faction_marshall"),
           (change_screen_return),
        ]),
     ]
  ),

  (
    "faction_army_follow_failed",menu_text_color(0xFF000d2c)|mnf_scale_picture,
    "You have disobeyed orders and failed to follow {s8}. In anger he has disbanded you from the army,\
 and sends a stern warning that your actions will not be forgotten.",
    "none",
    [
        (set_background_mesh, "mesh_pic_messenger"),
        (faction_get_slot, ":faction_marshall", "$players_faction", slot_faction_marshall),
        (str_store_troop_name, s8, ":faction_marshall"),
        (call_script, "script_abort_quest", "qst_follow_army", 1),
        (call_script, "script_change_player_relation_with_troop", ":faction_marshall", -3),
      ],
    [
      ("continue_3dot",[],"Continue...",
       [(change_screen_return),
        ]),
     ]
  ),


  (
    "invite_player_to_faction_without_center",menu_text_color(0xFF000d2c)|mnf_scale_picture,
    "You receive an offer of promotion!^^\
 {s8} of {s9} has sent you a message with great news.\
 You would be granted the honour of becoming a commander {lord/lady} of {s9},\
 and in return {s8} asks you to swear an oath of homage to him and fight in the war,\
 although he offers you no colonies or titles.\
 He will surely be offended if you do not take the offer...",
    "none",
    [
        (set_background_mesh, "mesh_pic_messenger"),
        (faction_get_slot, "$g_invite_faction_lord", "$g_invite_faction", slot_faction_leader),
        (str_store_troop_name, s8, "$g_invite_faction_lord"),
        (str_store_faction_name, s9, "$g_invite_faction"),
      ],
    [
      ("faction_accept",[],"Accept!",
       [(str_store_troop_name,s1,"$g_invite_faction_lord"),
        (setup_quest_text,"qst_join_faction"),

        (str_store_troop_name_link, s3, "$g_invite_faction_lord"),
        (str_store_faction_name_link, s4, "$g_invite_faction"),
        (quest_set_slot, "qst_join_faction", slot_quest_giver_troop, "$g_invite_faction_lord"),
        (quest_set_slot, "qst_join_faction", slot_quest_expiration_days, 30),
        (str_store_string, s2, "@Find and speak with {s3} of {s4} to give him your oath of homage."),
        (call_script, "script_start_quest", "qst_join_faction", "$g_invite_faction_lord"),
        (call_script, "script_report_quest_troop_positions", "qst_join_faction", "$g_invite_faction_lord", 3),
        (jump_to_menu, "mnu_invite_player_to_faction_accepted"),
        ]),
      ("faction_reject",[],"Decline the invitation.",
       [(call_script, "script_change_player_relation_with_troop", "$g_invite_faction_lord", -3),
        (call_script, "script_change_player_relation_with_faction", "$g_invite_faction", -10),
        (assign, "$g_invite_faction", 0),
        (assign, "$g_invite_faction_lord", 0),
        (assign, "$g_invite_offered_center", 0),
        (change_screen_return),
        ]),
     ]
  ),
  

  (
    "invite_player_to_faction",menu_text_color(0xFF000d2c)|mnf_scale_picture,
    "You receive an offer of promotion!^^\
 {s8} of {s9} has sent you a message with great news.\
 You would be granted the honour of becoming a commander {lord/lady} of {s9},\
 and in return {s8} asks you to swear an oath of homage to him and fight in the war,\
 offering you the planet of {s2} for your loyal service.\
 He will surely be offended if you do not take the offer...",
    "none",
    [
        (set_background_mesh, "mesh_pic_messenger"),
        (faction_get_slot, "$g_invite_faction_lord", "$g_invite_faction", slot_faction_leader),
        (str_store_troop_name, s8, "$g_invite_faction_lord"),
        (str_store_faction_name, s9, "$g_invite_faction"),
        (str_store_party_name, s2, "$g_invite_offered_center"),
      ],
    [
      ("faction_accept",[],"Accept!",
       [(str_store_troop_name,s1,"$g_invite_faction_lord"),
        (setup_quest_text,"qst_join_faction"),

        (str_store_troop_name_link, s3, "$g_invite_faction_lord"),
        (str_store_faction_name_link, s4, "$g_invite_faction"),
        (quest_set_slot, "qst_join_faction", slot_quest_giver_troop, "$g_invite_faction_lord"),
        (quest_set_slot, "qst_join_faction", slot_quest_expiration_days, 30),
        (str_store_string, s2, "@Find and speak with {s3} of {s4} to give him your oath of homage."),
        (call_script, "script_start_quest", "qst_join_faction", "$g_invite_faction_lord"),
        (call_script, "script_report_quest_troop_positions", "qst_join_faction", "$g_invite_faction_lord", 3),
        (jump_to_menu, "mnu_invite_player_to_faction_accepted"),
        ]),
      ("faction_reject",[],"Decline the invitation.",
       [(call_script, "script_change_player_relation_with_troop", "$g_invite_faction_lord", -3),
        (assign, "$g_invite_faction", 0),
        (assign, "$g_invite_faction_lord", 0),
        (assign, "$g_invite_offered_center", 0),
        (change_screen_return),
        ]),
     ]
  ),
  
  (
    "invite_player_to_faction_accepted",menu_text_color(0xFF000d2c),
    "In order to become a commander, you must swear an oath of homage to {s3}.\
 You shall have to find him and give him your oath in person. {s5}",
    "none",
    [
        (call_script, "script_get_information_about_troops_position", "$g_invite_faction_lord", 0),
        (str_store_troop_name, s3, "$g_invite_faction_lord"),
        (str_store_string, s5, "@{s1}"),
      ],
    [
      ("continue_3dot",[],"Continue...",
       [(change_screen_return),
        ]),
     ]
  ),

  (
    "question_peace_offer",menu_text_color(0xFF000d2c),
    "You Receive a Peace Offer^^{s1} offers you a peace agreement. What is your answer?",
    "none",
    [
      (str_store_faction_name, s1, "$g_notification_menu_var1"),
      (set_fixed_point_multiplier, 100),
      (position_set_x, pos0, 65),
      (position_set_y, pos0, 30),
      (position_set_z, pos0, 170),
      (set_game_menu_tableau_mesh, "tableau_faction_note_mesh_banner", "$g_notification_menu_var1", pos0),
      ],
    [
      ("peace_offer_accept",[],"Accept",
       [
         (call_script, "script_diplomacy_start_peace_between_factions", "fac_player_supporters_faction", "$g_notification_menu_var1", 1),
         (change_screen_return),
        ]),
      ("peace_offer_reject",[],"Reject",
       [
         (call_script, "script_change_player_relation_with_faction", "$g_notification_menu_var1", -5),
         (change_screen_return),
        ]),
     ]
  ),

  (
    "notification_player_faction_active",menu_text_color(0xFF000d2c),
    "You now posess land in your name without being tied to any faction, as a masterless warlord who knows no higher authority.\
 Enjoy this freedom, but know that the lords of the galaxy will not look to you kindly and will make every attempt to dispose of you.\
 You may find life very difficult without the protection of a faction.",
    "none",
    [
      (set_fixed_point_multiplier, 100),
      (position_set_x, pos0, 65),
      (position_set_y, pos0, 30),
      (position_set_z, pos0, 170),
      (set_game_menu_tableau_mesh, "tableau_faction_note_mesh_banner", "fac_player_supporters_faction", pos0),
      ],
    [
      ("continue_3dot",[],"Continue...",
       [(change_screen_return),
        ]),
     ]
  ),  

  (
    "notification_player_faction_deactive",menu_text_color(0xFF000d2c),
    "You no longer hold any land.",
    "none",
    [
      (set_fixed_point_multiplier, 100),
      (position_set_x, pos0, 65),
      (position_set_y, pos0, 30),
      (position_set_z, pos0, 170),
      (set_game_menu_tableau_mesh, "tableau_faction_note_mesh_banner", "fac_player_supporters_faction", pos0),
      ],
    [
      ("continue_3dot",[],"Continue...",
       [(change_screen_return),
        ]),
     ]
  ),

  (
    "notification_center_under_siege",menu_text_color(0xFF000d2c),
    "{s1} has been besieged by {s2} of {s3}!",
    "none",
    [
      (str_store_party_name, s1, "$g_notification_menu_var1"),
      (str_store_troop_name, s2, "$g_notification_menu_var2"),
      (store_troop_faction, ":troop_faction", "$g_notification_menu_var2"),
      (str_store_faction_name, s3, ":troop_faction"),
      (set_fixed_point_multiplier, 100),
      (position_set_x, pos0, 62),
      (position_set_y, pos0, 30),
      (position_set_z, pos0, 170),
      (set_game_menu_tableau_mesh, "tableau_center_note_mesh", "$g_notification_menu_var1", pos0),
      ],
    [
      ("continue_3dot",[],"Continue...",
       [(change_screen_return),
        ]),
     ]
  ),  

  (
    "notification_minorplanet_raided",menu_text_color(0xFF000d2c),
    #"Enemies have Laid Waste to a Fief^^{s1} has been raided by {s2} of {s3}!",
	"Enemies have Laid Waste to a territory.^^{s1} has been raided by {s2} of {s3}!",
    "none",
    [
      (str_store_party_name, s1, "$g_notification_menu_var1"),
      (str_store_troop_name, s2, "$g_notification_menu_var2"),
      (store_troop_faction, ":troop_faction", "$g_notification_menu_var2"),
      (str_store_faction_name, s3, ":troop_faction"),
      (set_fixed_point_multiplier, 100),
      (position_set_x, pos0, 62),
      (position_set_y, pos0, 30),
      (position_set_z, pos0, 170),
      (set_game_menu_tableau_mesh, "tableau_center_note_mesh", "$g_notification_menu_var1", pos0),
      ],
    [
      ("continue_3dot",[],"Continue...",
       [(change_screen_return),
        ]),
     ]
  ),  

  (
    "notification_minorplanet_raid_started",menu_text_color(0xFF000d2c),
    "Your planet is under Attack!^^{s2} of {s3} is laying waste to {s1}.",
    "none",
    [
      (str_store_party_name, s1, "$g_notification_menu_var1"),
      (str_store_troop_name, s2, "$g_notification_menu_var2"),
      (store_troop_faction, ":troop_faction", "$g_notification_menu_var2"),
      (str_store_faction_name, s3, ":troop_faction"),
      (set_fixed_point_multiplier, 100),
      (position_set_x, pos0, 62),
      (position_set_y, pos0, 30),
      (position_set_z, pos0, 170),
      (set_game_menu_tableau_mesh, "tableau_center_note_mesh", "$g_notification_menu_var1", pos0),
      ],
    [
      ("continue_3dot",[],"Continue...",
       [(change_screen_return),
        ]),
     ]
  ),

  (
    "notification_one_faction_left",menu_text_color(0xFF000d2c),
    "The Galaxy Conquered by One Faction^^{s1} has defeated all rivals and stands as the sole faction.",
    "none",
    [
      (str_store_faction_name, s1, "$g_notification_menu_var1"),
      (set_fixed_point_multiplier, 100),
      (position_set_x, pos0, 65),
      (position_set_y, pos0, 30),
      (position_set_z, pos0, 170),
      (try_begin),
        (is_between, "$g_notification_menu_var1", "fac_galacticempire", factions_end), #Excluding player faction
        (set_game_menu_tableau_mesh, "tableau_faction_note_mesh_for_menu", "$g_notification_menu_var1", pos0),
      (else_try),
        (set_game_menu_tableau_mesh, "tableau_faction_note_mesh_banner", "$g_notification_menu_var1", pos0),
      (try_end),
      ],
    [
      ("continue_3dot",[],"Continue...",
       [(change_screen_return),
        ]),
     ]
  ),
  
  (
    "notification_oath_renounced_faction_defeated",menu_text_color(0xFF000d2c),
    "Your Old Faction was Defeated^^You won the battle against {s1}! This ends your struggle which started after you renounced your oath to them.",
    "none",
    [
      (str_store_faction_name, s1, "$g_notification_menu_var1"),
      (set_fixed_point_multiplier, 100),
      (position_set_x, pos0, 65),
      (position_set_y, pos0, 30),
      (position_set_z, pos0, 170),
      (try_begin),
        (is_between, "$g_notification_menu_var1", "fac_galacticempire", factions_end), #Excluding player faction
        (set_game_menu_tableau_mesh, "tableau_faction_note_mesh_for_menu", "$g_notification_menu_var1", pos0),
      (else_try),
        (set_game_menu_tableau_mesh, "tableau_faction_note_mesh_banner", "$g_notification_menu_var1", pos0),
      (try_end),
      ],
    [
      ("continue_3dot",[],"Continue...",
       [(change_screen_return),
        ]),
     ]
  ),

  (
    "notification_center_lost",menu_text_color(0xFF000d2c),
    "An Estate was Lost^^You have lost {s1} to {s2}.",
    "none",
    [
      (str_store_party_name, s1, "$g_notification_menu_var1"),
      (str_store_faction_name, s2, "$g_notification_menu_var2"),
      (set_fixed_point_multiplier, 100),
      (position_set_x, pos0, 62),
      (position_set_y, pos0, 30),
      (position_set_z, pos0, 170),
      (set_game_menu_tableau_mesh, "tableau_center_note_mesh", "$g_notification_menu_var1", pos0),
      ],
    [
      ("continue_3dot",[],"Continue...",
       [(change_screen_return),
        ]),
     ]
  ),


  (
    "notification_troop_left_players_faction",menu_text_color(0xFF000d2c),
    "Betrayal!^^{s1} has left {s2} and joined {s3}.",
    "none",
    [
      (str_store_troop_name, s1, "$g_notification_menu_var1"),
      (str_store_faction_name, s2, "$players_faction"),
      (str_store_faction_name, s3, "$g_notification_menu_var2"),
      (set_fixed_point_multiplier, 100),
      (position_set_x, pos0, 55),
      (position_set_y, pos0, 20),
      (position_set_z, pos0, 100),
      (set_game_menu_tableau_mesh, "tableau_troop_note_mesh", "$g_notification_menu_var1", pos0),
      ],
    [
      ("continue_3dot",[],"Continue...",
       [(change_screen_return),
        ]),
     ]
  ),

  (
    "notification_troop_joined_players_faction",menu_text_color(0xFF000d2c),
    "Good news!^^ {s1} has left {s2} and joined {s3}.",
    "none",
    [
      (str_store_troop_name, s1, "$g_notification_menu_var1"),
      (str_store_faction_name, s2, "$g_notification_menu_var2"),
      (str_store_faction_name, s3, "$players_faction"),
      (set_fixed_point_multiplier, 100),
      (position_set_x, pos0, 55),
      (position_set_y, pos0, 20),
      (position_set_z, pos0, 100),
      (set_game_menu_tableau_mesh, "tableau_troop_note_mesh", "$g_notification_menu_var1", pos0),
      ],
    [
      ("continue_3dot",[],"Continue...",
       [(change_screen_return),
        ]),
     ]
  ),

  (
    "notification_war_declared",menu_text_color(0xFF000d2c),
    "Declaration of War^^{s1} has declared war against {s2}!",
    "none",
    [
      (try_begin),
        (eq, "$g_notification_menu_var1", "fac_player_supporters_faction"),
        (str_store_faction_name, s1, "$g_notification_menu_var2"),
        (str_store_string, s2, "@you"),
      (else_try),
        (eq, "$g_notification_menu_var2", "fac_player_supporters_faction"),
        (str_store_faction_name, s1, "$g_notification_menu_var1"),
        (str_store_string, s2, "@you"),
      (else_try),
        (str_store_faction_name, s1, "$g_notification_menu_var1"),
        (str_store_faction_name, s2, "$g_notification_menu_var2"),
      (try_end),
      (set_fixed_point_multiplier, 100),
      (position_set_x, pos0, 65),
      (position_set_y, pos0, 30),
      (position_set_z, pos0, 170),
      (store_sub, ":galacticempire", "$g_notification_menu_var1", factions_begin),
      (store_sub, ":rebelalliance", "$g_notification_menu_var2", factions_begin),
      (val_mul, ":galacticempire", 128),
      (val_add, ":galacticempire", ":rebelalliance"),
      (set_game_menu_tableau_mesh, "tableau_2_factions_mesh", ":galacticempire", pos0),
      ],
    [
      ("continue_3dot",[],"Continue...",
       [(change_screen_return),
        ]),
     ]
  ),

  (
    "notification_peace_declared",menu_text_color(0xFF000d2c),
    "Peace Agreement^^{s1} and {s2} have made peace!",
    "none",
    [
      (str_store_faction_name, s1, "$g_notification_menu_var1"),
      (str_store_faction_name, s2, "$g_notification_menu_var2"),
      (set_fixed_point_multiplier, 100),
      (position_set_x, pos0, 65),
      (position_set_y, pos0, 30),
      (position_set_z, pos0, 170),
      (store_sub, ":galacticempire", "$g_notification_menu_var1", factions_begin),
      (store_sub, ":rebelalliance", "$g_notification_menu_var2", factions_begin),
      (val_mul, ":galacticempire", 128),
      (val_add, ":galacticempire", ":rebelalliance"),
      (set_game_menu_tableau_mesh, "tableau_2_factions_mesh", ":galacticempire", pos0),
      ],
    [
      ("continue_3dot",[],"Continue...",
       [(change_screen_return),
        ]),
     ]
  ),
  
  (
    "notification_faction_defeated",menu_text_color(0xFF000d2c),
    "Faction Eliminated^^{s1} is no more!",
    "none",
    [
      (str_store_faction_name, s1, "$g_notification_menu_var1"),
      (set_fixed_point_multiplier, 100),
      (position_set_x, pos0, 65),
      (position_set_y, pos0, 30),
      (position_set_z, pos0, 170),
      (try_begin),
        (is_between, "$g_notification_menu_var1", "fac_galacticempire", factions_end), #Excluding player faction
        (set_game_menu_tableau_mesh, "tableau_faction_note_mesh_for_menu", "$g_notification_menu_var1", pos0),
      (else_try),
        (set_game_menu_tableau_mesh, "tableau_faction_note_mesh_banner", "$g_notification_menu_var1", pos0),
      (try_end),
      ],
    [
      ("continue_3dot",[],"Continue...",
       [
         (try_begin),
           (is_between, "$supported_pretender", pretenders_begin, pretenders_end),
           (troop_slot_eq, "$supported_pretender", slot_troop_original_faction, "$g_notification_menu_var1"),
           (try_for_range, ":cur_troop", faction_heroes_begin, faction_heroes_end),
             (store_troop_faction, ":cur_faction", ":cur_troop"),
             (eq, ":cur_faction", "fac_player_supporters_faction"),
             (troop_set_faction, ":cur_troop", "$g_notification_menu_var1"),
           (try_end),
           (try_for_parties, ":cur_party"),
             (store_faction_of_party, ":cur_faction", ":cur_party"),
             (eq, ":cur_faction", "fac_player_supporters_faction"),
             (party_set_faction, ":cur_party", "$g_notification_menu_var1"),
           (try_end),
           (assign, "$players_faction", "$g_notification_menu_var1"),
           (call_script, "script_add_notification_menu", "mnu_notification_rebels_switched_to_faction", "$g_notification_menu_var1", "$supported_pretender"),
           (faction_set_slot, "$g_notification_menu_var1", slot_faction_state, sfs_active),
           (faction_set_slot, "fac_player_supporters_faction", slot_faction_state, sfs_inactive),
           (faction_get_slot, ":old_leader", "$g_notification_menu_var1", slot_faction_leader),
           (troop_set_slot, ":old_leader", slot_troop_change_to_faction, "fac_commoners"),
           (faction_set_slot, "$g_notification_menu_var1", slot_faction_leader, "$supported_pretender"),
           (faction_set_slot, "$g_notification_menu_var1", slot_faction_marshall, "trp_player"),
           (faction_set_slot, "$g_notification_menu_var1", slot_faction_ai_state, sfai_default),
           (faction_set_slot, "$g_notification_menu_var1", slot_faction_ai_object, -1),
           (troop_set_slot, "$supported_pretender", slot_troop_occupation, slto_faction_hero),
           (party_remove_members, "p_main_party", "$supported_pretender", 1),
           (call_script, "script_set_player_relation_with_faction", "$g_notification_menu_var1", 0),
           (try_for_range, ":cur_faction", factions_begin, factions_end),
             (faction_slot_eq, ":cur_faction", slot_faction_state, sfs_active),
             (neq, ":cur_faction", "$g_notification_menu_var1"),
             (store_relation, ":reln", ":cur_faction", "fac_player_supporters_faction"),
             (set_relation, ":cur_faction", "$g_notification_menu_var1", ":reln"),
           (try_end),
           (assign, "$supported_pretender", 0),
           (assign, "$supported_pretender_old_faction", 0),
           (assign, "$g_recalculate_ais", 1),
           (call_script, "script_update_all_notes"),
         (try_end),
         (change_screen_return),
        ]),
     ]
  ),

  
  (
    "notification_rebels_switched_to_faction",menu_text_color(0xFF000d2c),
    "Rebellion Success^^ Your rebellion is victorious! Your faction now has the sole claim to the title of {s11}, with {s12} as the single ruler.",
    "none",
    [
      (str_store_faction_name, s11, "$g_notification_menu_var1"),
      (str_store_troop_name, s12, "$g_notification_menu_var2"),
      (set_fixed_point_multiplier, 100),
      (position_set_x, pos0, 65),
      (position_set_y, pos0, 30),
      (position_set_z, pos0, 170),
      (try_begin),
        (is_between, "$g_notification_menu_var1", "fac_galacticempire", factions_end), #Excluding player faction
        (set_game_menu_tableau_mesh, "tableau_faction_note_mesh_for_menu", "$g_notification_menu_var1", pos0),
      (else_try),
        (set_game_menu_tableau_mesh, "tableau_faction_note_mesh_banner", "$g_notification_menu_var1", pos0),
      (try_end),
      ],
    [
      ("continue_3dot",[],"Continue...",
       [
         (assign, "$talk_context", tc_rebel_thanks),
         (start_map_conversation, "$g_notification_menu_var2"),
         (change_screen_return),
        ]),
     ]
  ),


    (
    "kill_local_merchant_begin",menu_text_color(0xFF000d2c),
    "You spot your victim and follow him, observing as he turns a corner into a dark alley.\
 This will surely be your best opportunity to attack him.",
    "none",
    [
    ],
    [
      ("continue_3dot",[],"Continue...",
       [(set_jump_mission,"mt_back_alley_kill_local_merchant"),
        (party_get_slot, ":town_alley", "$qst_kill_local_merchant_center", slot_mainplanet_alley),
        (modify_visitors_at_site,":town_alley"),
        (reset_visitors),
        (set_visitor, 0, "trp_player"),
        (set_visitor, 1, "trp_local_merchant"),
        (jump_to_menu, "mnu_town"),
        (jump_to_scene,":town_alley"),
        (change_screen_mission),
        ]),
     ]
  ),

  (
    "auto_return_to_map",menu_text_color(0xFF000d2c),
    "stub",
    "none",
    [(change_screen_map)],
    []
  ),

#==========================================================================================================
# START OF CUSTOM BATTLE MOD  
##############################################
# Custom Battle Menus
##############################################

# Menu 1: Location Choice
  (
    "custom_battle_config_1",menu_text_color(0xFF000d2c),
	"Please choose the location for this battle.^{s1}",
	"none",
	[
	(try_begin),
	  (eq,"$g_custom_battle_location",1),
	  (str_store_string,s1,"str_custom_battle_location_1"),
	(else_try),
	  (eq,"$g_custom_battle_location",2),
	  (str_store_string,s1,"str_custom_battle_location_2"),
	(else_try),
	  (eq,"$g_custom_battle_location",3),
	  (str_store_string,s1,"str_custom_battle_location_3"),
	(else_try),
	  (eq,"$g_custom_battle_location",4),
	  (str_store_string,s1,"@Felucia"),
	(else_try),
	  (eq,"$g_custom_battle_location",5),
	  (str_store_string,s1,"@Coruscant"),
	(else_try),
	  (eq,"$g_custom_battle_location",6),
	  (str_store_string,s1,"@Tatooine"),
	(else_try),
	  (eq,"$g_custom_battle_location",7),
	  (str_store_string,s1,"@Mustafar"),
	(else_try),
	  (eq,"$g_custom_battle_location",8),
	  (str_store_string,s1,"@Dantooine"),
	(else_try),
	  (eq,"$g_custom_battle_location",9),
	  (str_store_string,s1,"@Kashyyyk"),
	(else_try),
	  (eq,"$g_custom_battle_location",10),
	  (str_store_string,s1,"@Raxus Prime"),
	(else_try),
	  (str_store_string, s1, "str_no_choice"),
	(try_end)],
	[
	  ("open_plains",[],"Geonosis [V. Large]",
	  [(assign, "$g_custom_battle_location", 1),
	   (jump_to_menu, "mnu_custom_battle_config_1"),]
	   ),
	  #("deep_forest",[],"Deep Forest (Large)",
	  ("deep_forest",[],"Yavin IV Plains [Large]",
	  [(assign, "$g_custom_battle_location", 2),
	   (jump_to_menu, "mnu_custom_battle_config_1"),]
	   ), 
	  ("desert_pass",[],"Dagobah Swamp [Medium]",
	  [(assign, "$g_custom_battle_location", 3),
	   (jump_to_menu, "mnu_custom_battle_config_1"),]
	   ), 
	   ##New Custom Battle Maps...
	  ("felucia",[],"Felucia [Medium]",
	  [(assign, "$g_custom_battle_location", 4),
	   (jump_to_menu, "mnu_custom_battle_config_1"),]
	   ), 
	   ("coruscant",[],"Coruscant [Medium]",
	  [(assign, "$g_custom_battle_location", 5),
	   (jump_to_menu, "mnu_custom_battle_config_1"),]
	   ), 
	   ("tatooine",[],"Tatooine [Medium]",
	  [(assign, "$g_custom_battle_location", 6),
	   (jump_to_menu, "mnu_custom_battle_config_1"),]
	   ), 
	   ("mustafar",[],"Mustafar [Medium]",
	  [(assign, "$g_custom_battle_location", 7),
	   (jump_to_menu, "mnu_custom_battle_config_1"),]
	   ), 
	   ("dantooine",[],"Dantooine [Medium]",
	  [(assign, "$g_custom_battle_location", 8),
	   (jump_to_menu, "mnu_custom_battle_config_1"),]
	   ), 
	   ("kashyyyk",[],"Kashyyyk [Medium]",
	  [(assign, "$g_custom_battle_location", 9),
	   (jump_to_menu, "mnu_custom_battle_config_1"),]
	   ), 
	   ("raxus",[],"Raxus Prime [Medium]",
	  [(assign, "$g_custom_battle_location", 10),
	   (jump_to_menu, "mnu_custom_battle_config_1"),]
	   ), 

	  ("next",
	  [
	    # Only display option when player has made a choice
	    (try_begin),
	      (eq, "$g_custom_battle_location", 0),
	      (disable_menu_option),
	    (try_end)
	  ],
	  "Next",
	  [
	    (jump_to_menu, "mnu_custom_battle_config_2"),
	    (assign, "$g_custom_battle_faction_to_edit",1)
	  ]),

	   #SW - added ability to cancel out of custom battle mod
      ("cancel_custom_battle_mod",[],"Cancel",
       [(jump_to_menu, "mnu_start_game_3"),
        ]
       ),	   
	]
  ),
  
# Menu 2: Teams Choice
  (
    "custom_battle_config_2",menu_text_color(0xFF000d2c),
	"Please choose the type of battle.^You have chosen: {s1}",
	"none",
	[
	(str_store_string, s1, "str_no_choice"),
	(try_begin),
		(eq,"$g_custom_battle_type",1),
		(str_store_string,s1,"str_custom_battle_type_1"),
	(else_try),
		(eq,"$g_custom_battle_type",2),
		(str_store_string,s1,"str_custom_battle_type_2"),
	(else_try),
		(eq,"$g_custom_battle_type",3),
		(str_store_string,s1,"str_custom_battle_type_3"),
	#(else_try),
	# (try_begin),
	# (eq,"$g_custom_battle_type",4),
	# (str_store_string,s1,"str_custom_battle_type_4"),
	# (else_try),
	# (try_begin),
	# (eq,"$g_custom_battle_type",5),
	# (str_store_string,s1,"str_custom_battle_type_5"),
	(else_try),
		(eq,"$g_custom_battle_type",6),
		(str_store_string,s1,"str_custom_battle_type_6"),
	(end_try),
	],
	
	[
	  ("1vs1",[],
	  "One Vs One",
	  [(assign, "$g_custom_battle_type", 1),
	  (assign, "$g_custom_battle_num_factions", 2),
	  (troop_set_slot,"trp_custom_battle_spawn_store",1,1),
	  (troop_set_slot,"trp_custom_battle_spawn_store",2,11),(jump_to_menu, "mnu_custom_battle_config_2"),]
	   ), 
	  ("3way",[
	  (this_or_next|eq,"$g_custom_battle_location",1),
	  (eq,"$g_custom_battle_location",2),
	  ],"Three Way",
	  [(assign, "$g_custom_battle_type", 2),
	  (assign, "$g_custom_battle_num_factions", 3),
	  (troop_set_slot,"trp_custom_battle_spawn_store",1,1),
	  (troop_set_slot,"trp_custom_battle_spawn_store",2,21),
	  (troop_set_slot,"trp_custom_battle_spawn_store",3,41),(jump_to_menu, "mnu_custom_battle_config_2"),]
	   ),
	  ("4way",[
	  (this_or_next|eq,"$g_custom_battle_location",1),
	  (eq,"$g_custom_battle_location",2),
	  ],"Four Way",
	  [(assign, "$g_custom_battle_type", 3),
	  (assign, "$g_custom_battle_num_factions", 4),
	  (troop_set_slot,"trp_custom_battle_spawn_store",1,1),
	  (troop_set_slot,"trp_custom_battle_spawn_store",2,21),
	  (troop_set_slot,"trp_custom_battle_spawn_store",3,31),
	  (troop_set_slot,"trp_custom_battle_spawn_store",4,51),(jump_to_menu, "mnu_custom_battle_config_2"),]
	   ),  
	  # ("5way",[
	  # (this_or_next|eq,"$g_custom_battle_location",1),
	  # (eq,"$g_custom_battle_location",2),
	  # ],"Five Way",
	  # [(assign, "$g_custom_battle_type", 4),
	  # (assign, "$g_custom_battle_num_factions", 5),
	  # (troop_set_slot,"trp_custom_battle_spawn_store",1,1),
	  # (troop_set_slot,"trp_custom_battle_spawn_store",2,21),
	  # (troop_set_slot,"trp_custom_battle_spawn_store",3,31),
	  # (troop_set_slot,"trp_custom_battle_spawn_store",4,41),
	  # (troop_set_slot,"trp_custom_battle_spawn_store",5,51),]
	   # ),  
	  # ("6way",[
	  # (this_or_next|eq,"$g_custom_battle_location",1),
	  # (eq,"$g_custom_battle_location",2),
	  # ],"Six Way",
	  # [(assign, "$g_custom_battle_type", 5),
	  # (assign, "$g_custom_battle_num_factions", 6),
	  # (troop_set_slot,"trp_custom_battle_spawn_store",1,1),
	  # (troop_set_slot,"trp_custom_battle_spawn_store",2,11),
	  # (troop_set_slot,"trp_custom_battle_spawn_store",3,21),
	  # (troop_set_slot,"trp_custom_battle_spawn_store",4,31),
	  # (troop_set_slot,"trp_custom_battle_spawn_store",5,41),
	  # (troop_set_slot,"trp_custom_battle_spawn_store",6,51),]
	   # ),
	  ("2vs2",[
	  (this_or_next|eq,"$g_custom_battle_location",1),
	  (eq,"$g_custom_battle_location",2),
	  ],"Two vs Two",
	  [(assign, "$g_custom_battle_type", 6),
	  (assign, "$g_custom_battle_num_factions", 4),
	  # Assign Team Spawn Positions
	  (troop_set_slot,"trp_custom_battle_spawn_store",1,1),
	  (troop_set_slot,"trp_custom_battle_spawn_store",2,11),
	  (troop_set_slot,"trp_custom_battle_spawn_store",3,21),
	  (troop_set_slot,"trp_custom_battle_spawn_store",4,41), (jump_to_menu, "mnu_custom_battle_config_2"),
	  ]
	  ),
	  ("next",
	  [
	    # Only display option when player has made a choice
	    (try_begin),
	      (lt,"$g_custom_battle_type", 1),
	      (disable_menu_option),
	    (try_end)
	  ],
	  "Next",
	  [(jump_to_menu,"mnu_custom_battle_config_3"),
	  (str_store_string,s1,"str_no_choice")]
	   ),	   
	]
  ),
  
  (
    "custom_battle_config_3",menu_text_color(0xFF000d2c),
	"Please choose the faction for army {reg1}.^Your choice: {s1}",
	"none",
	[(assign,reg1,"$g_custom_battle_faction_to_edit")],
	[
#	  ("vaegir",[],"Faction of Vaegirs",
	  ("empire",[(str_store_faction_name, s20, "fac_galacticempire")], "{s20}",
	  [(troop_set_slot,"trp_custom_battle_fac_store",reg(1),1),
	  (str_store_string,s1,"str_galacticempire"), (jump_to_menu,"mnu_custom_battle_config_3"),
	   ]
	   ),
#	  ("swadia",[],"Faction of Swadia",
	  ("rebel",[(str_store_faction_name, s20, "fac_rebelalliance")], "{s20}",
	  [(troop_set_slot,"trp_custom_battle_fac_store",reg(1),2),
	  (str_store_string,s1,"str_rebelalliance"), (jump_to_menu,"mnu_custom_battle_config_3"),
	   ]
	   ),
#	  ("nords",[],"Faction of Nords",
	  ("hutt",[(str_store_faction_name, s20, "fac_huttcartel")], "{s20}",
	  [(troop_set_slot,"trp_custom_battle_fac_store",reg(1),3),
	  (str_store_string,s1,"str_huttcartel"), (jump_to_menu,"mnu_custom_battle_config_3"),
	   ]
	   ),
#	   ("rhodok",[],"Faction of Rhodok",
	  ("mercenary",[],"Mercenaries",
	  [(troop_set_slot,"trp_custom_battle_fac_store",reg(1),4),
	  (str_store_string,s1,"str_faction_4"), (jump_to_menu,"mnu_custom_battle_config_3"),
	   ]
	   ),
	  #("khergit",[],"Khergit Khanate",
	  ("clonewars",[],"Clone Wars",
	   [(troop_set_slot,"trp_custom_battle_fac_store",reg(1),5),
	   (str_store_string,s1,"str_faction_5"), (jump_to_menu,"mnu_custom_battle_config_3"),
	    ]
	   ),
	  ("next",[
	  # Only display option when player has made a choice
	    (try_begin),
	      (neg|troop_slot_ge,"trp_custom_battle_fac_store",reg(1), 1),
	      (disable_menu_option),
	    (try_end)
	  ],"Next",
	  [
	    (jump_to_menu,"mnu_custom_battle_config_4"),
	    (str_store_string,s1,"str_no_choice")
	  ]
	   ),	   
	]
  ),
  
  (
    "custom_battle_config_main_class",menu_text_color(0xFF000d2c),
	"Please choose the main class of your character. (This determines your choice of subclasses)",
	"none",
	[],
	[
	  ("soldier",[],"Ranged Soldier",
	  [(assign, "$g_custom_battle_class", 1),
	   (jump_to_menu, "mnu_custom_battle_config_class"),
	   ]
	   ),
	  ("force_sensitive",[],"Force-Sensitive Warrior",
	  [(assign, "$g_custom_battle_class",2),
	  (jump_to_menu, "mnu_custom_battle_config_class"),
	  ]
	  ),
#	  ("ranged_infantry",[],"Ranged Infantry",
#	  [(assign, "$g_custom_battle_class",3),
#	  (jump_to_menu, "mnu_custom_battle_config_class"),
#	  ]
#	  ),
#	 ("custom",[],"Custom Class",
#	 [(jump_to_menu, "mnu_custom_battle_custom_class_1"),
#	 ]
#	 ),
	]
  ),
  
# (
	# "custom_battle_custom_class_1",menu_text_color(0xFF000d2c),
	# "Choose your body armour",
	# "none",
	# [],
	# [
	# ("plate_armour",[],"Plate Armour",
	  # [(troop_add_item,"trp_player","itm_plate_armor"),
	  # (jump_to_menu,"mnu_custom_battle_custom_class_2"),
	   # ]
	   # ),
	# ("coat_of_plates",[],"Coat of Plates",
	  # [(troop_add_item,"trp_player","itm_coat_of_plates"),
	  # (jump_to_menu,"mnu_custom_battle_custom_class_2"),
	   # ]
	   # ),
	# ("surcoat_over_mail",[],"Surcoat over Mail",
	  # [(troop_add_item,"trp_player","itm_surcoat_over_mail"),
	  # (jump_to_menu,"mnu_custom_battle_custom_class_2"),
	   # ]
	   # ),
	# ("mail_shirt",[],"Mail Shirt",
	  # [(troop_add_item,"trp_player","itm_mail_shirt"),
	  # (jump_to_menu,"mnu_custom_battle_custom_class_2"),
	   # ]
	   # ),
	# ("leather_jerkin",[],"Leather Jerkin",
	  # [(troop_add_item,"trp_player","itm_leather_jerkin"),
	  # (jump_to_menu,"mnu_custom_battle_custom_class_2"),
	   # ]
	   # ),
	# ]
	# ),

# (
	# "custom_battle_custom_class_2",menu_text_color(0xFF000d2c),
	# "Choose your boots",
	# "none",
	# [],
	# [
	# ("iron_greaves",[],"Iron Greaves",
	  # [(troop_add_item,"trp_player","itm_iron_greaves"),
	  # (jump_to_menu,"mnu_custom_battle_custom_class_3"),
	   # ]
	   # ),
	# ("mail_boots",[],"Mail Boots",
	  # [(troop_add_item,"trp_player","itm_mail_boots"),
	  # (jump_to_menu,"mnu_custom_battle_custom_class_3"),
	   # ]
	   # ),
	# ("splinted_greaves",[],"Splinted Greaves",
	  # [(troop_add_item,"trp_player","itm_splinted_greaves"),
	  # (jump_to_menu,"mnu_custom_battle_custom_class_3"),
	   # ]
	   # ),
	# ("leather_boots",[],"Leather Boots",
	  # [(troop_add_item,"trp_player","itm_leather_boots"),
	  # (jump_to_menu,"mnu_custom_battle_custom_class_3"),
	   # ]
	   # ),
	# ]
	# ),
# (
	# "custom_battle_custom_class_3",menu_text_color(0xFF000d2c),
	# "Choose your gauntlets",
	# "none",
	# [],
	# [
	# ("gauntlets",[],"Gauntlets",
	  # [(troop_add_item,"trp_player","itm_gauntlets"),
	  # (jump_to_menu,"mnu_custom_battle_custom_class_4"),
	   # ]
	   # ),
	# ("mail_mittens",[],"Mail Mittens",
	  # [(troop_add_item,"trp_player","itm_mail_mittens"),
	  # (jump_to_menu,"mnu_custom_battle_custom_class_4"),
	   # ]
	   # ),
	# ("scale_gauntlets",[],"Scale Gauntlets",
	  # [(troop_add_item,"trp_player","itm_scale_gauntlets"),
	  # (jump_to_menu,"mnu_custom_battle_custom_class_4"),
	   # ]
	   # ),
	# ("leather_gloves",[],"Leather Gloves",
	  # [(troop_add_item,"trp_player","itm_leather_gloves"),
	  # (jump_to_menu,"mnu_custom_battle_custom_class_4"),
	   # ]
	   # ),
	# ]
	# ),
# (
	# "custom_battle_custom_class_4",menu_text_color(0xFF000d2c),
	# "Choose weapon one",
	# "none",
	# [],
	# [
	# ("gauntlets",[],"Gauntlets",
	  # [(troop_add_item,"trp_player","itm_gauntlets"),
	  # (jump_to_menu,"mnu_custom_battle_custom_class_4"),
	   # ]
	   # ),
	# ("mail_mittens",[],"Mail Mittens",
	  # [(troop_add_item,"trp_player","itm_mail_mittens"),
	  # (jump_to_menu,"mnu_custom_battle_custom_class_4"),
	   # ]
	   # ),
	# ("scale_gauntlets",[],"Scale Gauntlets",
	  # [(troop_add_item,"trp_player","itm_scale_gauntlets"),
	  # (jump_to_menu,"mnu_custom_battle_custom_class_4"),
	   # ]
	   # ),
	# ("leather_gloves",[],"Leather Gloves",
	  # [(troop_add_item,"trp_player","itm_leather_gloves"),
	  # (jump_to_menu,"mnu_custom_battle_custom_class_4"),
	   # ]
	   # ),
	# ]
	# ),
  (
    "custom_battle_config_class",menu_text_color(0xFF000d2c),
	"Please choose the sub class of your character. (This determines your skills and equipment)",
	"none",
	[],
	[
# Horseman Subclasses
# Soldier
	  ("soldier_veteran",[(eq , "$g_custom_battle_class", 1)],"Veteran Soldier (Easy)",
	  [(assign, "$g_custom_battle_sub_class", 1),
	   (jump_to_menu, "mnu_custom_battle_config_finish"),
	   ]
	   ),
	  ("soldier_regular",[(eq , "$g_custom_battle_class", 1)],"Regular Soldier [Medium]",
	  [(assign, "$g_custom_battle_sub_class", 2),
	   (jump_to_menu, "mnu_custom_battle_config_finish"),
	   ]
	   ),
	  ("soldier_recruit",[(eq , "$g_custom_battle_class", 1)],"Soldier Recruit (Hard)",
	  [(assign, "$g_custom_battle_sub_class", 3),
	   (jump_to_menu, "mnu_custom_battle_config_finish"),
	   ]
	   ),
	  # ("mounted_warrior",[(eq , "$g_custom_battle_class", 1)],"Mounted Warrior [Medium]",
	  # [(assign, "$g_custom_battle_sub_class", 4),
	   # (jump_to_menu, "mnu_custom_battle_config_finish"),
	   # ]
	   # ),
	  # ("scout",[(eq , "$g_custom_battle_class", 1)],"Scout (Hard)",
	  # [(assign, "$g_custom_battle_sub_class", 5),
	   # (jump_to_menu, "mnu_custom_battle_config_finish"),
	   # ]
	   # ),
	  # ("horse_archer",[(eq , "$g_custom_battle_class", 1)],"Horse Archer (Hard)",
	  # [(assign, "$g_custom_battle_sub_class", 6),
	   # (jump_to_menu, "mnu_custom_battle_config_finish"),
	   # ]
	   # ),
# Infantry Subclasses
# Force-sensitive
	  ("fs_master",[(eq,"$g_custom_battle_class",2)],"Force-Sensitive Master (Easy)",
	  [(assign,"$g_custom_battle_sub_class", 7),
	  (jump_to_menu,"mnu_custom_battle_config_finish")
	  ]
	  ),
	  ("fs_warrior",[(eq,"$g_custom_battle_class",2)],"Force-Sensitive Warrior [Medium]",
	  [(assign,"$g_custom_battle_sub_class", 8),
	  (jump_to_menu,"mnu_custom_battle_config_finish")
	  ]
	  ),
	  ("fs_apprentice",[(eq,"$g_custom_battle_class",2)],"Force-Sensitive Apprentice (Hard)",
	  [(assign,"$g_custom_battle_sub_class", 9),
	  (jump_to_menu,"mnu_custom_battle_config_finish")
	  ]
	  ),
	  # ("axeman",[(eq , "$g_custom_battle_class", 2)],"Axeman [Medium]",
	  # [(assign, "$g_custom_battle_sub_class", 10),
	   # (jump_to_menu, "mnu_custom_battle_config_finish"),
	   # ]
	   # ),
	  # ("pikeman",[(eq , "$g_custom_battle_class", 2)],"Pikeman [Medium]",
	  # [(assign, "$g_custom_battle_sub_class", 11),
	   # (jump_to_menu, "mnu_custom_battle_config_finish"),
	   # ]
	   # ),
	  # ("militia",[(eq , "$g_custom_battle_class", 2)],"Militia (Hard)",
	  # [(assign, "$g_custom_battle_sub_class", 12),
	   # (jump_to_menu, "mnu_custom_battle_config_finish"),
	   # ]
	   # ),
	  # ("farmer",[(eq , "$g_custom_battle_class", 2)],"Farmer (V.Hard)",
	  # [(assign, "$g_custom_battle_sub_class", 13),
	   # (jump_to_menu, "mnu_custom_battle_config_finish"),
	   # ]
	   # ),
# # Ranged Infantry Subclasses
	  # ("master_archer",[(eq,"$g_custom_battle_class",3)],"Master Archer (V.Easy)",
	  # [(assign,"$g_custom_battle_sub_class", 14),
	  # (jump_to_menu,"mnu_custom_battle_config_finish")
	  # ]
	  # ),
	  # ("master_crossbowman",[(eq,"$g_custom_battle_class",3)],"Master Crossbowman (V.Easy)",
	  # [(assign,"$g_custom_battle_sub_class", 15),
	  # (jump_to_menu,"mnu_custom_battle_config_finish")
	  # ]
	  # ),
	  # ("veteran_archer",[(eq,"$g_custom_battle_class",3)],"Veteran Archer [Medium]",
	  # [(assign,"$g_custom_battle_sub_class", 16),
	  # (jump_to_menu,"mnu_custom_battle_config_finish")
	  # ]
	  # ),
	  # ("veteran_crossbowman",[(eq , "$g_custom_battle_class", 3)],"Veteran Crossbowman [Medium]",
	  # [(assign, "$g_custom_battle_sub_class", 17),
	   # (jump_to_menu, "mnu_custom_battle_config_finish"),
	   # ]
	   # ),
	  # ("axe_thrower",[(eq , "$g_custom_battle_class", 3)],"Axe Thrower [Medium]",
	  # [(assign, "$g_custom_battle_sub_class", 18),
	   # (jump_to_menu, "mnu_custom_battle_config_finish"),
	   # ]
	   # ),
	  # ("javelineer",[(eq , "$g_custom_battle_class", 3)],"Javelineer [Medium]",
	  # [(assign, "$g_custom_battle_sub_class", 19),
	   # (jump_to_menu, "mnu_custom_battle_config_finish"),
	   # ]
	   # ),
	  # ("archer",[(eq , "$g_custom_battle_class", 3)],"Archer (Hard)",
	  # [(assign, "$g_custom_battle_sub_class", 20),
	   # (jump_to_menu, "mnu_custom_battle_config_finish"),
	   # ]
	   # ), 
	  # ("crossbowman",[(eq , "$g_custom_battle_class", 3)],"Crossbowman (Hard)",
	  # [(assign, "$g_custom_battle_sub_class", 21),
	   # (jump_to_menu, "mnu_custom_battle_config_finish"),
	   # ]
	   # ),
	]
  ),
# Set troops for each party
  (
   "custom_battle_config_4",menu_text_color(0xFF000d2c),
	"Select the troops for army {reg11} (Left CTRL + Left Click removes troops, Left Shift + Left Click adds five troops and Left Shift + Left Control + Left Click removes five troops.)",
	"none",
	[
# Show army number
    (assign, reg11, "$g_custom_battle_faction_to_edit"),
# Set troop to store troop numbers on
	(try_begin),
	  (eq,"$g_custom_battle_faction_to_edit", 1),
	  (assign,"$troop_store","trp_custom_battle_fac_1_troops"),
	(else_try),
	  (eq,"$g_custom_battle_faction_to_edit", 2),
	  (assign,"$troop_store","trp_custom_battle_fac_2_troops"),
	(else_try),
	  (eq,"$g_custom_battle_faction_to_edit", 3),
	  (assign,"$troop_store","trp_custom_battle_fac_3_troops"),
	(else_try),
	  (eq,"$g_custom_battle_faction_to_edit", 4),
	  (assign,"$troop_store","trp_custom_battle_fac_4_troops"),
	(else_try),
	  (eq,"$g_custom_battle_faction_to_edit", 5),
	  (assign,"$troop_store","trp_custom_battle_fac_5_troops"),
	(else_try),
	  (eq,"$g_custom_battle_faction_to_edit", 6),
	  (assign,"$troop_store","trp_custom_battle_fac_6_troops"),
	(end_try),
	],[])
	
]


from module_scripts import scripts
from     ID_scripts import script_custom_battle_set_faction_troops

 #swy-- sync up this crap with the other lookup table in custom_battle_set_faction_troops by using a state machine.
 #   -- believe me, it was worse before. magic.gif

generated_entries = []

for opcode in scripts[script_custom_battle_set_faction_troops][1]:

    if type(opcode) is not tuple:
      continue

    if opcode[0] is eq:
      #swy-- e.g: faction number 5, these (eq,) opcodes always prefix a block
      ___cur_magic_entry_troop_faction = opcode[2]

    if opcode[0] is assign:
      #swy-- e.g: "trp_b2series" as-is
      ___cur_magic_entry_troop_identifier = opcode[2]
      #swy-- e.g: reg(17) => slot 7
      ___cur_magic_entry_troop_faction_slot_index = (opcode[1] & ~opmask_register) - 10

      generated_entries += [
      ("custom_battle_config_troop_entry",
	  [
	    (troop_get_slot, ":cur_faction", "trp_custom_battle_fac_store", reg(11)),
	    (eq,             ":cur_faction", ___cur_magic_entry_troop_faction),

	    (troop_get_slot, reg40, "$troop_store", ___cur_magic_entry_troop_faction_slot_index),

        #swy-- get the translated troop name at runtime, hell yeah!
	    (str_store_troop_name, s20, ___cur_magic_entry_troop_identifier),
	  ],
	  "{s20} ({reg40})",
	  [
	    (assign, ":cur_troop_slot", ___cur_magic_entry_troop_faction_slot_index),
	    (troop_get_slot, ":cur_troop_amount", "$troop_store", ":cur_troop_slot"),
	    
	    #swy-- Click + Ctrl + Shift => Remove five if there's at least five
	    (try_begin),
	      (ge,           ":cur_troop_amount", 5),
	      (key_is_down,  key_left_shift),
	      (key_is_down,  key_left_control),
	      # --
	      (val_sub,      ":cur_troop_amount", 5),

	    #swy-- Click + Shift => Add five
	    (else_try),
	      (key_is_down,  key_left_shift),
	      # --
	      (val_add,      ":cur_troop_amount", 5),

	    #swy-- Click + Ctrl => Remove one if there's at least one
	    (else_try),
	      (ge,           ":cur_troop_amount", 1),
	      (key_is_down,  key_left_control),
	      # --
	      (val_sub,      ":cur_troop_amount", 1),
	      
	    #swy-- Click => Add one
	    (else_try),
	      (val_add,      ":cur_troop_amount", 1),
	    (end_try),

	   (troop_set_slot, "$troop_store", ":cur_troop_slot", ":cur_troop_amount"),
	   (jump_to_menu, "mnu_custom_battle_config_4"),
	  ]) ]

game_menus[-1] = list(game_menus[-1])
game_menus[-1][5] = generated_entries + \
	[
	 ("next", [], "Next",
	  [
	    (try_begin),
	      (eq,"$g_custom_battle_faction_to_edit", "$g_custom_battle_num_factions"),
	      (jump_to_menu, "mnu_custom_battle_config_main_class"),
	    (else_try),
	      (val_add,"$g_custom_battle_faction_to_edit", 1),
	      (jump_to_menu,"mnu_custom_battle_config_3"),
	    (end_try)
	  ]),	  
	]

game_menus += [

  (
    "custom_battle_config_finish",menu_text_color(0xFF000d2c),
    "The battle is ready.",
    "none",
    [
     (assign, "$g_battle_result", 0),
     #local variables never used?
	 #(assign, ":ally_count", 0),
     #(assign, ":enemy_count", 0),

     (troop_clear_inventory, "trp_player"),
     (troop_raise_attribute, "trp_player", ca_strength, -1000),
     (troop_raise_attribute, "trp_player", ca_agility, -1000),
     (troop_raise_attribute, "trp_player", ca_charisma, -1000),
     (troop_raise_attribute, "trp_player", ca_intelligence, -1000),
     (troop_raise_skill, "trp_player", skl_shield, -1000),
     (troop_raise_skill, "trp_player", skl_athletics, -1000),
     (troop_raise_skill, "trp_player", skl_riding, -1000),
     (troop_raise_skill, "trp_player", skl_power_strike, -1000),
     (troop_raise_skill, "trp_player", skl_power_throw, -1000),
     (troop_raise_skill, "trp_player", skl_weapon_master, -1000),
     (troop_raise_skill, "trp_player", skl_horse_archery, -1000),
     (troop_raise_skill, "trp_player", skl_ironflesh, -1000),
     (troop_raise_proficiency_linear, "trp_player", wpt_one_handed_weapon, -10000),
     (troop_raise_proficiency_linear, "trp_player", wpt_two_handed_weapon, -10000),
     (troop_raise_proficiency_linear, "trp_player", wpt_polearm, -10000),
     (troop_raise_proficiency_linear, "trp_player", wpt_archery, -10000),
     (troop_raise_proficiency_linear, "trp_player", wpt_crossbow, -10000),
     (troop_raise_proficiency_linear, "trp_player", wpt_throwing, -10000),
     (troop_raise_proficiency_linear, "trp_player", wpt_firearm, -10000),	 

     (reset_visitors),
#   Set player skills and equipment based on class
	#  Main Class 1: Horseman
	# Subclass 1:  Knight
     (try_begin),
	 
       (eq, "$g_custom_battle_sub_class", 1),

       (troop_raise_attribute, "trp_player", ca_strength, 18),
       (troop_raise_attribute, "trp_player", ca_agility, 18),
       (troop_raise_attribute, "trp_player", ca_charisma, 18),
       (troop_raise_attribute, "trp_player", ca_intelligence, 18),
       (troop_raise_skill, "trp_player", skl_ironflesh, 6),
       (troop_raise_skill, "trp_player", skl_shield, 6),
       (troop_raise_skill, "trp_player", skl_athletics, 6),
	   (troop_raise_skill, "trp_player", skl_riding, 6),
       (troop_raise_skill, "trp_player", skl_power_strike, 6),
       (troop_raise_skill, "trp_player", skl_power_throw, 6),
       (troop_raise_skill, "trp_player", skl_weapon_master, 6),	   
       (troop_raise_proficiency_linear, "trp_player", wpt_one_handed_weapon, 200),
       (troop_raise_proficiency_linear, "trp_player", wpt_two_handed_weapon, 200),
       (troop_raise_proficiency_linear, "trp_player", wpt_polearm, 200),
       (troop_raise_proficiency_linear, "trp_player", wpt_archery, 200),
       (troop_raise_proficiency_linear, "trp_player", wpt_crossbow, 200),
       (troop_raise_proficiency_linear, "trp_player", wpt_throwing, 200),
	   (troop_raise_proficiency_linear, "trp_player", wpt_firearm, 200),
	   (troop_add_item, "trp_player","itm_transparent_helmet",0),
       (troop_add_item, "trp_player","itm_quick_battle_armor",0),
       (troop_add_item, "trp_player","itm_leather_boots",0),
       (troop_add_item, "trp_player","itm_vibro_sword3_gold",0),
       (troop_add_item, "trp_player","itm_energy_shield_yellow_large",0),
       (troop_add_item, "trp_player","itm_a295",0),
       (troop_add_item, "trp_player","itm_laser_bolts_yellow_rifle",0),	   
       (troop_equip_items, "trp_player"),
	# Subclass 2: Lancer
	(else_try),
       (eq, "$g_custom_battle_sub_class", 2),

       (troop_raise_attribute, "trp_player", ca_strength, 15),
       (troop_raise_attribute, "trp_player", ca_agility, 15),
       (troop_raise_attribute, "trp_player", ca_charisma, 15),
       (troop_raise_attribute, "trp_player", ca_intelligence, 15),
       (troop_raise_skill, "trp_player", skl_ironflesh, 4),
       (troop_raise_skill, "trp_player", skl_shield, 4),
       (troop_raise_skill, "trp_player", skl_athletics, 4),
	   (troop_raise_skill, "trp_player", skl_riding, 4),
       (troop_raise_skill, "trp_player", skl_power_strike, 4),
       (troop_raise_skill, "trp_player", skl_power_throw, 4),
       (troop_raise_skill, "trp_player", skl_weapon_master, 4),	   
       (troop_raise_proficiency_linear, "trp_player", wpt_one_handed_weapon, 160),
       (troop_raise_proficiency_linear, "trp_player", wpt_two_handed_weapon, 160),
       (troop_raise_proficiency_linear, "trp_player", wpt_polearm, 160),
       (troop_raise_proficiency_linear, "trp_player", wpt_archery, 160),
       (troop_raise_proficiency_linear, "trp_player", wpt_crossbow, 160),
       (troop_raise_proficiency_linear, "trp_player", wpt_throwing, 160),
	   (troop_raise_proficiency_linear, "trp_player", wpt_firearm, 160),
	   (troop_add_item, "trp_player","itm_transparent_helmet",0),
       (troop_add_item, "trp_player","itm_quick_battle_armor",0),
       (troop_add_item, "trp_player","itm_leather_boots",0),
       (troop_add_item, "trp_player","itm_vibro_axe_medium_1h",0),
       (troop_add_item, "trp_player","itm_energy_shield_yellow_medium",0),
       (troop_add_item, "trp_player","itm_ee3",0),
       (troop_add_item, "trp_player","itm_laser_bolts_yellow_rifle",0),	   
       (troop_equip_items, "trp_player"),
	# Subclass 3: Master Horse Archer
	(else_try),
       (eq, "$g_custom_battle_sub_class", 3),

       (troop_raise_attribute, "trp_player", ca_strength, 12),
       (troop_raise_attribute, "trp_player", ca_agility, 12),
       (troop_raise_attribute, "trp_player", ca_charisma, 12),
       (troop_raise_attribute, "trp_player", ca_intelligence, 12),
       (troop_raise_skill, "trp_player", skl_ironflesh, 2),
       (troop_raise_skill, "trp_player", skl_shield, 2),
       (troop_raise_skill, "trp_player", skl_athletics, 2),
	   (troop_raise_skill, "trp_player", skl_riding, 2),
       (troop_raise_skill, "trp_player", skl_power_strike, 2),
       (troop_raise_skill, "trp_player", skl_power_throw, 2),
       (troop_raise_skill, "trp_player", skl_weapon_master, 2),	   
       (troop_raise_proficiency_linear, "trp_player", wpt_one_handed_weapon, 120),
       (troop_raise_proficiency_linear, "trp_player", wpt_two_handed_weapon, 120),
       (troop_raise_proficiency_linear, "trp_player", wpt_polearm, 120),
       (troop_raise_proficiency_linear, "trp_player", wpt_archery, 120),
       (troop_raise_proficiency_linear, "trp_player", wpt_crossbow, 120),
       (troop_raise_proficiency_linear, "trp_player", wpt_throwing, 120),
	   (troop_raise_proficiency_linear, "trp_player", wpt_firearm, 120), 
	   #(troop_add_item, "trp_player","itm_transparent_helmet",0),
       (troop_add_item, "trp_player","itm_quick_battle_armor",0),
       (troop_add_item, "trp_player","itm_leather_boots",0),
       (troop_add_item, "trp_player","itm_vibro_blade1",0),
       (troop_add_item, "trp_player","itm_energy_shield_yellow_small",0),
       (troop_add_item, "trp_player","itm_dl44a",0),
       (troop_add_item, "trp_player","itm_laser_bolts_yellow_pistol",0),
       (troop_equip_items, "trp_player"), 
	# Subclass 4: Mounted Warrior
		# (else_try),
       # (eq, "$g_custom_battle_sub_class", 4),

       # (troop_raise_attribute, "trp_player", ca_strength, 12),
       # (troop_raise_attribute, "trp_player", ca_agility, 9),
       # (troop_raise_attribute, "trp_player", ca_charisma, 5),
       # (troop_raise_attribute, "trp_player", ca_intelligence, 5),
       # (troop_raise_skill, "trp_player", skl_ironflesh, 2),
       # (troop_raise_skill, "trp_player", skl_riding, 3),
       # (troop_raise_skill, "trp_player", skl_power_strike, 2),
       # (troop_raise_skill, "trp_player", skl_weapon_master, 3),
       # (troop_raise_proficiency_linear, "trp_player", wpt_one_handed_weapon, 100),
       # (troop_raise_proficiency_linear, "trp_player", wpt_two_handed_weapon, 40),
       # (troop_raise_proficiency_linear, "trp_player", wpt_polearm, 20),
       # (troop_raise_proficiency_linear, "trp_player", wpt_archery, 10),
       # (troop_raise_proficiency_linear, "trp_player", wpt_crossbow, 20),
       # (troop_raise_proficiency_linear, "trp_player", wpt_throwing, 20),
       # (troop_add_item, "trp_player","itm_mail_hauberk",0),
       # (troop_add_item, "trp_player","itm_mail_chausses",0),
       # (troop_add_item, "trp_player","itm_one_handed_war_axe_a",0),
	   # (troop_add_item, "trp_player","itm_shield_heater_c",0),
       # (troop_add_item, "trp_player","itm_saddle_horse",0),
       # (troop_equip_items, "trp_player"),
	# # Subclass 5:  Scout
		# (else_try),
       # (eq, "$g_custom_battle_sub_class", 5),
	   
       # (troop_raise_attribute, "trp_player", ca_strength, 9),
       # (troop_raise_attribute, "trp_player", ca_agility, 15),
       # (troop_raise_attribute, "trp_player", ca_charisma, 5),
       # (troop_raise_attribute, "trp_player", ca_intelligence, 5),
       # (troop_raise_skill, "trp_player", skl_ironflesh, 2),
       # (troop_raise_skill, "trp_player", skl_shield, 2),
       # (troop_raise_skill, "trp_player", skl_athletics, 2),
       # (troop_raise_skill, "trp_player", skl_power_strike, 1),
       # (troop_raise_skill, "trp_player", skl_weapon_master, 2),
       # (troop_raise_skill, "trp_player", skl_riding, 7),
       # (troop_raise_proficiency_linear, "trp_player", wpt_one_handed_weapon, 80),
       # (troop_raise_proficiency_linear, "trp_player", wpt_two_handed_weapon, 40),
       # (troop_raise_proficiency_linear, "trp_player", wpt_polearm, 30),
       # (troop_raise_proficiency_linear, "trp_player", wpt_archery, 20),
       # (troop_raise_proficiency_linear, "trp_player", wpt_crossbow, 20),
       # (troop_raise_proficiency_linear, "trp_player", wpt_throwing, 20),
       # (troop_add_item, "trp_player","itm_leather_jerkin",0),
       # (troop_add_item, "trp_player","itm_leather_boots",0),
       # (troop_add_item, "trp_player","itm_sword_medieval_b_small",0),
       # (troop_add_item, "trp_player","itm_courser",imod_spirited),
       # (troop_equip_items, "trp_player"),
	# # Subclass 6: Horse Archer
	# (else_try),
       # (eq, "$g_custom_battle_sub_class", 3),

       # (troop_raise_attribute, "trp_player", ca_strength, 9),
       # (troop_raise_attribute, "trp_player", ca_agility, 15),
       # (troop_raise_attribute, "trp_player", ca_charisma, 5),
       # (troop_raise_attribute, "trp_player", ca_intelligence, 5),
       # (troop_raise_skill, "trp_player", skl_ironflesh, 1),
       # (troop_raise_skill, "trp_player", skl_riding, 4),
       # (troop_raise_skill, "trp_player", skl_power_draw, 3),
       # (troop_raise_skill, "trp_player", skl_weapon_master, 3),
	   # (troop_raise_skill, "trp_player", skl_horse_archery, 4),
       # (troop_raise_proficiency_linear, "trp_player", wpt_one_handed_weapon, 50),
       # (troop_raise_proficiency_linear, "trp_player", wpt_two_handed_weapon, 40),
       # (troop_raise_proficiency_linear, "trp_player", wpt_polearm, 20),
       # (troop_raise_proficiency_linear, "trp_player", wpt_archery, 120),
       # (troop_raise_proficiency_linear, "trp_player", wpt_crossbow, 20),
       # (troop_raise_proficiency_linear, "trp_player", wpt_throwing, 20),
       # (troop_add_item, "trp_player","itm_padded_leather",0),
       # (troop_add_item, "trp_player","itm_splinted_greaves",0),
       # (troop_add_item, "trp_player","itm_nomad_bow",0),
       # (troop_add_item, "trp_player","itm_khergit_arrows",0),
       # (troop_add_item, "trp_player","itm_pickaxe",0),
       # (troop_add_item, "trp_player","itm_steppe_horse",0),
       # (troop_equip_items, "trp_player"), 
# Main  Class 2: Infantry
	# Subclass 7:  Dismounted Knight
	(else_try),
       (eq, "$g_custom_battle_sub_class", 7),

       (troop_raise_attribute, "trp_player", ca_strength, 18),
       (troop_raise_attribute, "trp_player", ca_agility, 18),
       (troop_raise_attribute, "trp_player", ca_charisma, 18),
       (troop_raise_attribute, "trp_player", ca_intelligence, 18),
       (troop_raise_skill, "trp_player", skl_ironflesh, 7),
       (troop_raise_skill, "trp_player", skl_shield, 7),
       (troop_raise_skill, "trp_player", skl_athletics, 7),
	   (troop_raise_skill, "trp_player", skl_riding, 7),
       (troop_raise_skill, "trp_player", skl_power_strike, 7),
       (troop_raise_skill, "trp_player", skl_power_draw, 7),
       (troop_raise_skill, "trp_player", skl_weapon_master, 7),	   
       (troop_raise_proficiency_linear, "trp_player", wpt_one_handed_weapon, 200),
       (troop_raise_proficiency_linear, "trp_player", wpt_two_handed_weapon, 200),
       (troop_raise_proficiency_linear, "trp_player", wpt_polearm, 200),
       (troop_raise_proficiency_linear, "trp_player", wpt_archery, 200),
       (troop_raise_proficiency_linear, "trp_player", wpt_crossbow, 200),
       (troop_raise_proficiency_linear, "trp_player", wpt_throwing, 200),
	   (troop_raise_proficiency_linear, "trp_player", wpt_firearm, 200),
	   (troop_add_item, "trp_player","itm_transparent_helmet",0),
       (troop_add_item, "trp_player","itm_quick_battle_armor",0),
       (troop_add_item, "trp_player","itm_leather_boots",0),
	   (troop_add_item, "trp_player","itm_force_lightning_ammo",0),
	   (troop_add_item, "trp_player","itm_force_power_ds_4",0),
       (troop_add_item, "trp_player","itm_lightsaber_yellow",0),
       (troop_add_item, "trp_player","itm_force_shield",0),
#	   (troop_add_item, "trp_player","itm_force_push",0),
       (troop_equip_items, "trp_player"),
	# Subclass 8: Elite Guard
	(else_try),
       (eq, "$g_custom_battle_sub_class", 8),

       (troop_raise_attribute, "trp_player", ca_strength, 15),
       (troop_raise_attribute, "trp_player", ca_agility, 15),
       (troop_raise_attribute, "trp_player", ca_charisma, 15),
       (troop_raise_attribute, "trp_player", ca_intelligence, 15),
       (troop_raise_skill, "trp_player", skl_ironflesh, 5),
       (troop_raise_skill, "trp_player", skl_shield, 5),
       (troop_raise_skill, "trp_player", skl_athletics, 5),
	   (troop_raise_skill, "trp_player", skl_riding, 5),
       (troop_raise_skill, "trp_player", skl_power_draw, 5),
       (troop_raise_skill, "trp_player", skl_power_throw, 5),
       (troop_raise_skill, "trp_player", skl_weapon_master, 5),	   
       (troop_raise_proficiency_linear, "trp_player", wpt_one_handed_weapon, 160),
       (troop_raise_proficiency_linear, "trp_player", wpt_two_handed_weapon, 160),
       (troop_raise_proficiency_linear, "trp_player", wpt_polearm, 160),
       (troop_raise_proficiency_linear, "trp_player", wpt_archery, 160),
       (troop_raise_proficiency_linear, "trp_player", wpt_crossbow, 160),
       (troop_raise_proficiency_linear, "trp_player", wpt_throwing, 160),
	   (troop_raise_proficiency_linear, "trp_player", wpt_firearm, 160),
	   (troop_add_item, "trp_player","itm_transparent_helmet",0),
       (troop_add_item, "trp_player","itm_quick_battle_armor",0),
       (troop_add_item, "trp_player","itm_leather_boots",0),
	   (troop_add_item, "trp_player","itm_force_lightning_ammo",0),
	   (troop_add_item, "trp_player","itm_force_power_ds_3",0),
       (troop_add_item, "trp_player","itm_lightsaber_yellow",0),
       (troop_add_item, "trp_player","itm_force_block",0),
       (troop_equip_items, "trp_player"),
	# Subclass 9: Barbarian
	(else_try),
       (eq, "$g_custom_battle_sub_class", 9),

       (troop_raise_attribute, "trp_player", ca_strength, 12),
       (troop_raise_attribute, "trp_player", ca_agility, 12),
       (troop_raise_attribute, "trp_player", ca_charisma, 12),
       (troop_raise_attribute, "trp_player", ca_intelligence, 12),
       (troop_raise_skill, "trp_player", skl_ironflesh, 3),
       (troop_raise_skill, "trp_player", skl_shield, 3),
       (troop_raise_skill, "trp_player", skl_athletics, 3),
	   (troop_raise_skill, "trp_player", skl_riding, 3),
       (troop_raise_skill, "trp_player", skl_power_strike, 3),
       (troop_raise_skill, "trp_player", skl_power_draw, 3),
       (troop_raise_skill, "trp_player", skl_weapon_master, 3),	   
       (troop_raise_proficiency_linear, "trp_player", wpt_one_handed_weapon, 120),
       (troop_raise_proficiency_linear, "trp_player", wpt_two_handed_weapon, 120),
       (troop_raise_proficiency_linear, "trp_player", wpt_polearm, 120),
       (troop_raise_proficiency_linear, "trp_player", wpt_archery, 120),
       (troop_raise_proficiency_linear, "trp_player", wpt_crossbow, 120),
       (troop_raise_proficiency_linear, "trp_player", wpt_throwing, 120),
	   (troop_raise_proficiency_linear, "trp_player", wpt_firearm, 120),
	   #(troop_add_item, "trp_player","itm_transparent_helmet",0),
       (troop_add_item, "trp_player","itm_quick_battle_armor",0),
       (troop_add_item, "trp_player","itm_leather_boots",0),
       (troop_add_item, "trp_player","itm_lightsaber_yellow_1h",0),
	   (troop_add_item, "trp_player","itm_force_block",0),
	   (troop_add_item, "trp_player","itm_force_power_ls_2",0),
	   (troop_add_item, "trp_player","itm_force_push_ammo",0),
       (troop_equip_items, "trp_player"),
	# Subclass 10: Axeman
	# (else_try),
       # (eq, "$g_custom_battle_sub_class", 10),

       # (troop_raise_attribute, "trp_player", ca_strength, 15),
       # (troop_raise_attribute, "trp_player", ca_agility, 12),
       # (troop_raise_attribute, "trp_player", ca_charisma, 5),
       # (troop_raise_attribute, "trp_player", ca_intelligence, 5),
       # (troop_raise_skill, "trp_player", skl_ironflesh, 5),
       # (troop_raise_skill, "trp_player", skl_athletics, 6),
       # (troop_raise_skill, "trp_player", skl_power_strike, 4),
       # (troop_raise_skill, "trp_player", skl_weapon_master, 3),
       # (troop_raise_proficiency_linear, "trp_player", wpt_one_handed_weapon, 40),
       # (troop_raise_proficiency_linear, "trp_player", wpt_two_handed_weapon, 120),
       # (troop_raise_proficiency_linear, "trp_player", wpt_polearm, 30),
       # (troop_raise_proficiency_linear, "trp_player", wpt_archery, 30),
       # (troop_raise_proficiency_linear, "trp_player", wpt_crossbow, 20),
       # (troop_raise_proficiency_linear, "trp_player", wpt_throwing, 20),
       # (troop_add_item, "trp_player","itm_mail_shirt",0),
       # (troop_add_item, "trp_player","itm_mail_chausses",0),
       # (troop_add_item, "trp_player","itm_fighting_axe",0),
	   # (troop_add_item, "trp_player","itm_shield_heater_c",0),
	   # (troop_add_item, "trp_player","itm_skullcap",0),
       # (troop_equip_items, "trp_player"),
	# # Subclass 11: Pikeman
	# (else_try),
       # (eq, "$g_custom_battle_sub_class", 11),

       # (troop_raise_attribute, "trp_player", ca_strength, 12),
       # (troop_raise_attribute, "trp_player", ca_agility, 12),
       # (troop_raise_attribute, "trp_player", ca_charisma, 5),
       # (troop_raise_attribute, "trp_player", ca_intelligence, 5),
       # (troop_raise_skill, "trp_player", skl_ironflesh, 2),
       # (troop_raise_skill, "trp_player", skl_athletics, 3),
       # (troop_raise_skill, "trp_player", skl_power_strike, 3),
       # (troop_raise_skill, "trp_player", skl_weapon_master, 3),
       # (troop_raise_proficiency_linear, "trp_player", wpt_one_handed_weapon, 70),
       # (troop_raise_proficiency_linear, "trp_player", wpt_two_handed_weapon, 20),
       # (troop_raise_proficiency_linear, "trp_player", wpt_polearm, 110),
       # (troop_raise_proficiency_linear, "trp_player", wpt_archery, 30),
       # (troop_raise_proficiency_linear, "trp_player", wpt_crossbow, 20),
       # (troop_raise_proficiency_linear, "trp_player", wpt_throwing, 20),
       # (troop_add_item, "trp_player","itm_byrnie",0),
       # (troop_add_item, "trp_player","itm_mail_chausses",0),
       # (troop_add_item, "trp_player","itm_pike",0),
       # (troop_add_item, "trp_player","itm_sword_viking_1",0),
	   # (troop_add_item, "trp_player","itm_nasal_helmet",0),
       # (troop_equip_items, "trp_player"),
	# # Subclass 12: Militia
	# (else_try),
       # (eq, "$g_custom_battle_sub_class", 12),

       # (troop_raise_attribute, "trp_player", ca_strength, 9),
       # (troop_raise_attribute, "trp_player", ca_agility, 9),
       # (troop_raise_attribute, "trp_player", ca_charisma, 5),
       # (troop_raise_attribute, "trp_player", ca_intelligence, 5),
       # (troop_raise_skill, "trp_player", skl_ironflesh, 1),
       # (troop_raise_skill, "trp_player", skl_athletics, 2),
       # (troop_raise_skill, "trp_player", skl_power_strike, 2),
       # (troop_raise_skill, "trp_player", skl_weapon_master, 2),
       # (troop_raise_proficiency_linear, "trp_player", wpt_one_handed_weapon, 70),
       # (troop_raise_proficiency_linear, "trp_player", wpt_two_handed_weapon, 20),
       # (troop_raise_proficiency_linear, "trp_player", wpt_polearm, 20),
       # (troop_raise_proficiency_linear, "trp_player", wpt_archery, 30),
       # (troop_raise_proficiency_linear, "trp_player", wpt_crossbow, 20),
       # (troop_raise_proficiency_linear, "trp_player", wpt_throwing, 20),
       # (troop_add_item, "trp_player","itm_padded_cloth",0),
       # (troop_add_item, "trp_player","itm_nomad_boots",0),
       # (troop_add_item, "trp_player","itm_spiked_club",0),
       # (troop_add_item, "trp_player","itm_leather_covered_round_shield",0),
       # (troop_equip_items, "trp_player"),
	# # Subclass 13: Farmer
	# (else_try),
       # (eq, "$g_custom_battle_sub_class", 13),

       # (troop_raise_attribute, "trp_player", ca_strength, 6),
       # (troop_raise_attribute, "trp_player", ca_agility, 6),
       # (troop_raise_attribute, "trp_player", ca_charisma, 5),
       # (troop_raise_attribute, "trp_player", ca_intelligence, 5),
       # (troop_raise_skill, "trp_player", skl_ironflesh, 1),
       # (troop_raise_skill, "trp_player", skl_athletics, 2),
       # (troop_raise_skill, "trp_player", skl_power_strike, 2),
       # (troop_raise_skill, "trp_player", skl_weapon_master, 2),
       # (troop_raise_proficiency_linear, "trp_player", wpt_one_handed_weapon, 30),
       # (troop_raise_proficiency_linear, "trp_player", wpt_two_handed_weapon, 20),
       # (troop_raise_proficiency_linear, "trp_player", wpt_polearm, 20),
       # (troop_raise_proficiency_linear, "trp_player", wpt_archery, 30),
       # (troop_raise_proficiency_linear, "trp_player", wpt_crossbow, 20),
       # (troop_raise_proficiency_linear, "trp_player", wpt_throwing, 20),
       # (troop_add_item, "trp_player","itm_linen_tunic",0),
       # (troop_add_item, "trp_player","itm_wrapping_boots",0),
       # (troop_add_item, "trp_player","itm_pitch_fork",0),
       # (troop_add_item, "trp_player","itm_knife",0),
       # (troop_equip_items, "trp_player"),
# # Main Class 3: Ranged Infantry
	# # Subclass 14: Master Archer
	# (else_try),
       # (eq, "$g_custom_battle_sub_class", 14),

       # (troop_raise_attribute, "trp_player", ca_strength, 15),
       # (troop_raise_attribute, "trp_player", ca_agility, 18),
       # (troop_raise_attribute, "trp_player", ca_charisma, 5),
       # (troop_raise_attribute, "trp_player", ca_intelligence, 5),
       # (troop_raise_skill, "trp_player", skl_ironflesh, 2),
       # (troop_raise_skill, "trp_player", skl_athletics, 4),
       # (troop_raise_skill, "trp_player", skl_power_draw, 8),
       # (troop_raise_skill, "trp_player", skl_weapon_master, 4),
       # (troop_raise_proficiency_linear, "trp_player", wpt_one_handed_weapon, 30),
       # (troop_raise_proficiency_linear, "trp_player", wpt_two_handed_weapon, 20),
       # (troop_raise_proficiency_linear, "trp_player", wpt_polearm, 20),
       # (troop_raise_proficiency_linear, "trp_player", wpt_archery, 200),
       # (troop_raise_proficiency_linear, "trp_player", wpt_crossbow, 20),
       # (troop_raise_proficiency_linear, "trp_player", wpt_throwing, 20),
       # (troop_add_item, "trp_player","itm_war_bow",0),
       # (troop_add_item, "trp_player","itm_bodkin_arrows",0),
	   # (troop_add_item, "trp_player","itm_bodkin_arrows",0),
       # (troop_add_item, "trp_player","itm_light_mail_and_plate",0),
       # (troop_add_item, "trp_player","itm_iron_greaves",0),
	   # (troop_add_item, "trp_player","itm_sword_viking_2",0),
       # (troop_equip_items, "trp_player"),
	# # Subclass 15: Master Crossbowman
	# (else_try),
       # (eq, "$g_custom_battle_sub_class", 15),

       # (troop_raise_attribute, "trp_player", ca_strength, 15),
       # (troop_raise_attribute, "trp_player", ca_agility, 18),
       # (troop_raise_attribute, "trp_player", ca_charisma, 5),
       # (troop_raise_attribute, "trp_player", ca_intelligence, 5),
       # (troop_raise_skill, "trp_player", skl_ironflesh, 2),
       # (troop_raise_skill, "trp_player", skl_athletics, 4),
       # (troop_raise_skill, "trp_player", skl_power_strike, 1),
       # (troop_raise_skill, "trp_player", skl_weapon_master, 4),
       # (troop_raise_proficiency_linear, "trp_player", wpt_one_handed_weapon, 30),
       # (troop_raise_proficiency_linear, "trp_player", wpt_two_handed_weapon, 20),
       # (troop_raise_proficiency_linear, "trp_player", wpt_polearm, 20),
       # (troop_raise_proficiency_linear, "trp_player", wpt_archery, 10),
       # (troop_raise_proficiency_linear, "trp_player", wpt_crossbow, 200),
       # (troop_raise_proficiency_linear, "trp_player", wpt_throwing, 20),
       # (troop_add_item, "trp_player","itm_sniper_crossbow",0),
       # (troop_add_item, "trp_player","itm_bolts",0),
	   # (troop_add_item, "trp_player","itm_bolts",0),
       # (troop_add_item, "trp_player","itm_mail_and_plate",0),
       # (troop_add_item, "trp_player","itm_iron_greaves",0),
	   # (troop_add_item, "trp_player","itm_sword_viking_2",0),
       # (troop_equip_items, "trp_player"),
	# # Subclass 16: Veteran Archer
	# (else_try),
       # (eq, "$g_custom_battle_sub_class", 16),

       # (troop_raise_attribute, "trp_player", ca_strength, 12),
       # (troop_raise_attribute, "trp_player", ca_agility, 15),
       # (troop_raise_attribute, "trp_player", ca_charisma, 5),
       # (troop_raise_attribute, "trp_player", ca_intelligence, 5),
       # (troop_raise_skill, "trp_player", skl_ironflesh, 2),
       # (troop_raise_skill, "trp_player", skl_athletics, 4),
       # (troop_raise_skill, "trp_player", skl_power_draw, 8),
       # (troop_raise_skill, "trp_player", skl_weapon_master, 4),
       # (troop_raise_proficiency_linear, "trp_player", wpt_one_handed_weapon, 30),
       # (troop_raise_proficiency_linear, "trp_player", wpt_two_handed_weapon, 20),
       # (troop_raise_proficiency_linear, "trp_player", wpt_polearm, 20),
       # (troop_raise_proficiency_linear, "trp_player", wpt_archery, 20),
       # (troop_raise_proficiency_linear, "trp_player", wpt_crossbow, 120),
       # (troop_raise_proficiency_linear, "trp_player", wpt_throwing, 20),
       # (troop_add_item, "trp_player","itm_long_bow",0),
       # (troop_add_item, "trp_player","itm_arrows",0),
	   # (troop_add_item, "trp_player","itm_arrows",0),
       # (troop_add_item, "trp_player","itm_mail_shirt",0),
       # (troop_add_item, "trp_player","itm_mail_chausses",0),
	   # (troop_add_item, "trp_player","itm_dagger",0),
       # (troop_equip_items, "trp_player"),
	# # Subclass 17: Veteran Crossbowman
	# (else_try),
       # (eq, "$g_custom_battle_sub_class", 17),

       # (troop_raise_attribute, "trp_player", ca_strength, 12),
       # (troop_raise_attribute, "trp_player", ca_agility, 15),
       # (troop_raise_attribute, "trp_player", ca_charisma, 5),
       # (troop_raise_attribute, "trp_player", ca_intelligence, 5),
       # (troop_raise_skill, "trp_player", skl_ironflesh, 2),
       # (troop_raise_skill, "trp_player", skl_athletics, 4),
       # (troop_raise_skill, "trp_player", skl_power_draw, 8),
       # (troop_raise_skill, "trp_player", skl_weapon_master, 4),
       # (troop_raise_proficiency_linear, "trp_player", wpt_one_handed_weapon, 30),
       # (troop_raise_proficiency_linear, "trp_player", wpt_two_handed_weapon, 20),
       # (troop_raise_proficiency_linear, "trp_player", wpt_polearm, 20),
       # (troop_raise_proficiency_linear, "trp_player", wpt_archery, 20),
       # (troop_raise_proficiency_linear, "trp_player", wpt_crossbow, 120),
       # (troop_raise_proficiency_linear, "trp_player", wpt_throwing, 20),
       # (troop_add_item, "trp_player","itm_crossbow",0),
       # (troop_add_item, "trp_player","itm_bolts",0),
	   # (troop_add_item, "trp_player","itm_bolts",0),
       # (troop_add_item, "trp_player","itm_mail_shirt",0),
       # (troop_add_item, "trp_player","itm_mail_chausses",0),
	   # (troop_add_item, "trp_player","itm_dagger",0),
       # (troop_equip_items, "trp_player"),
	# # Subclass 18: Axe Thrower
	# (else_try),
       # (eq, "$g_custom_battle_sub_class", 18),

       # (troop_raise_attribute, "trp_player", ca_strength, 12),
       # (troop_raise_attribute, "trp_player", ca_agility, 15),
       # (troop_raise_attribute, "trp_player", ca_charisma, 5),
       # (troop_raise_attribute, "trp_player", ca_intelligence, 5),
       # (troop_raise_skill, "trp_player", skl_ironflesh, 2),
       # (troop_raise_skill, "trp_player", skl_athletics, 4),
       # (troop_raise_skill, "trp_player", skl_power_throw, 3),
       # (troop_raise_skill, "trp_player", skl_weapon_master, 3),
       # (troop_raise_proficiency_linear, "trp_player", wpt_one_handed_weapon, 30),
       # (troop_raise_proficiency_linear, "trp_player", wpt_two_handed_weapon, 20),
       # (troop_raise_proficiency_linear, "trp_player", wpt_polearm, 20),
       # (troop_raise_proficiency_linear, "trp_player", wpt_archery, 20),
       # (troop_raise_proficiency_linear, "trp_player", wpt_crossbow, 20),
       # (troop_raise_proficiency_linear, "trp_player", wpt_throwing, 120),
       # (troop_add_item, "trp_player","itm_throwing_axes",0),
       # (troop_add_item, "trp_player","itm_throwing_axes",0),
       # (troop_add_item, "trp_player","itm_haubergeon",0),
       # (troop_add_item, "trp_player","itm_mail_chausses",0),
	   # (troop_add_item, "trp_player","itm_pickaxe",0),
	   # (troop_add_item, "trp_player","itm_fur_covered_shield",0),
       # (troop_equip_items, "trp_player"),
	# # Subclass 19: Javelineer
	# (else_try),
       # (eq, "$g_custom_battle_sub_class", 19),

       # (troop_raise_attribute, "trp_player", ca_strength, 12),
       # (troop_raise_attribute, "trp_player", ca_agility, 12),
       # (troop_raise_attribute, "trp_player", ca_charisma, 5),
       # (troop_raise_attribute, "trp_player", ca_intelligence, 5),
       # (troop_raise_skill, "trp_player", skl_ironflesh, 2),
       # (troop_raise_skill, "trp_player", skl_athletics, 4),
       # (troop_raise_skill, "trp_player", skl_power_throw, 3),
       # (troop_raise_skill, "trp_player", skl_weapon_master, 3),
       # (troop_raise_proficiency_linear, "trp_player", wpt_one_handed_weapon, 30),
       # (troop_raise_proficiency_linear, "trp_player", wpt_two_handed_weapon, 20),
       # (troop_raise_proficiency_linear, "trp_player", wpt_polearm, 20),
       # (troop_raise_proficiency_linear, "trp_player", wpt_archery, 20),
       # (troop_raise_proficiency_linear, "trp_player", wpt_crossbow, 20),
       # (troop_raise_proficiency_linear, "trp_player", wpt_throwing, 120),
       # (troop_add_item, "trp_player","itm_javelin",0),
       # (troop_add_item, "trp_player","itm_javelin",0),
       # (troop_add_item, "trp_player","itm_studded_leather_coat",0),
       # (troop_add_item, "trp_player","itm_splinted_leather_greaves",0),
	   # (troop_add_item, "trp_player","itm_military_pick",0),
	   # (troop_add_item, "trp_player","itm_hide_covered_round_shield",0),
       # (troop_equip_items, "trp_player"),
	# # Subclass 20: Archer
	# (else_try),
       # (eq, "$g_custom_battle_sub_class", 20),

       # (troop_raise_attribute, "trp_player", ca_strength, 9),
       # (troop_raise_attribute, "trp_player", ca_agility, 9),
       # (troop_raise_attribute, "trp_player", ca_charisma, 5),
       # (troop_raise_attribute, "trp_player", ca_intelligence, 5),
       # (troop_raise_skill, "trp_player", skl_ironflesh, 2),
       # (troop_raise_skill, "trp_player", skl_athletics, 2),
       # (troop_raise_skill, "trp_player", skl_power_draw, 2),
       # (troop_raise_skill, "trp_player", skl_weapon_master, 2),
       # (troop_raise_proficiency_linear, "trp_player", wpt_one_handed_weapon, 30),
       # (troop_raise_proficiency_linear, "trp_player", wpt_two_handed_weapon, 20),
       # (troop_raise_proficiency_linear, "trp_player", wpt_polearm, 20),
       # (troop_raise_proficiency_linear, "trp_player", wpt_archery, 80),
       # (troop_raise_proficiency_linear, "trp_player", wpt_crossbow, 20),
       # (troop_raise_proficiency_linear, "trp_player", wpt_throwing, 20),
       # (troop_add_item, "trp_player","itm_hunting_bow",0),
       # (troop_add_item, "trp_player","itm_arrows",0),
       # (troop_add_item, "trp_player","itm_arrows",0),
       # (troop_add_item, "trp_player","itm_leather_jerkin",0),
       # (troop_add_item, "trp_player","itm_leather_boots",0),
	   # (troop_add_item, "trp_player","itm_hatchet",0),
       # (troop_equip_items, "trp_player"),
	# # Subclass 21: Crossbowman
	# (else_try),
       # (eq, "$g_custom_battle_sub_class", 21),

       # (troop_raise_attribute, "trp_player", ca_strength, 9),
       # (troop_raise_attribute, "trp_player", ca_agility, 9),
       # (troop_raise_attribute, "trp_player", ca_charisma, 5),
       # (troop_raise_attribute, "trp_player", ca_intelligence, 5),
       # (troop_raise_skill, "trp_player", skl_ironflesh, 2),
       # (troop_raise_skill, "trp_player", skl_athletics, 2),
       # (troop_raise_skill, "trp_player", skl_weapon_master, 2),
       # (troop_raise_proficiency_linear, "trp_player", wpt_one_handed_weapon, 30),
       # (troop_raise_proficiency_linear, "trp_player", wpt_two_handed_weapon, 20),
       # (troop_raise_proficiency_linear, "trp_player", wpt_polearm, 20),
       # (troop_raise_proficiency_linear, "trp_player", wpt_archery, 10),
       # (troop_raise_proficiency_linear, "trp_player", wpt_crossbow, 80),
       # (troop_raise_proficiency_linear, "trp_player", wpt_throwing, 20),
       # (troop_add_item, "trp_player","itm_hunting_crossbow",0),
       # (troop_add_item, "trp_player","itm_bolts",0),
       # (troop_add_item, "trp_player","itm_bolts",0),
       # (troop_add_item, "trp_player","itm_padded_leather",0),
       # (troop_add_item, "trp_player","itm_leather_boots",0),
	   # (troop_add_item, "trp_player","itm_hatchet",0),
       # (troop_equip_items, "trp_player"),
	(try_end),

# Setup scene choice
	(try_begin),
	(eq, "$g_custom_battle_location", 1),
	(assign, "$g_custom_battle_scene", "scn_custom_battle_1"),
	(else_try),
	(eq, "$g_custom_battle_location", 2),
	(assign, "$g_custom_battle_scene", "scn_custom_battle_2"),
	(else_try),
	(eq, "$g_custom_battle_location", 3),
	(assign, "$g_custom_battle_scene", "scn_custom_battle_3"),
	(else_try),
	(eq, "$g_custom_battle_location", 4),
	(assign, "$g_custom_battle_scene", "scn_mainplanet_felucia_land_battle"),
	(else_try),
	(eq, "$g_custom_battle_location", 5),
	(assign, "$g_custom_battle_scene", "scn_mainplanet_coruscant_land_battle"),
	(else_try),
	(eq, "$g_custom_battle_location", 6),
	(assign, "$g_custom_battle_scene", "scn_mainplanet_tatooine_land_battle"),
	(else_try),
	(eq, "$g_custom_battle_location", 7),
	(assign, "$g_custom_battle_scene", "scn_mainplanet_mustafar_land_battle"),
	(else_try),
	(eq, "$g_custom_battle_location", 8),
	(assign, "$g_custom_battle_scene", "scn_mainplanet_dantooine_land_battle"),
	(else_try),
	(eq, "$g_custom_battle_location", 9),
	(assign, "$g_custom_battle_scene", "scn_mainplanet_kashyyyk_land_battle"),
	(else_try),
	(eq, "$g_custom_battle_location", 10),
	(assign, "$g_custom_battle_scene", "scn_mainplanet_raxusprime_land_battle"),
	(end_try),


# Set troop positions

# Player Troops (Army)
	(assign,reg(32),1),
	(troop_get_slot,reg(1),"trp_custom_battle_fac_1_troops", 1),
	(troop_get_slot,reg(2),"trp_custom_battle_fac_1_troops", 2),
	(troop_get_slot,reg(3),"trp_custom_battle_fac_1_troops", 3),
	(troop_get_slot,reg(4),"trp_custom_battle_fac_1_troops", 4),
	(troop_get_slot,reg(5),"trp_custom_battle_fac_1_troops", 5),
	(troop_get_slot,reg(6),"trp_custom_battle_fac_1_troops", 6),
	(troop_get_slot,reg(7),"trp_custom_battle_fac_1_troops", 7),
	(troop_get_slot,reg(8),"trp_custom_battle_fac_1_troops", 8),
	(troop_get_slot,reg(9),"trp_custom_battle_fac_1_troops", 9),
	(troop_get_slot,reg(10),"trp_custom_battle_fac_1_troops", 10),
	(call_script,"script_custom_battle_set_faction_troops"),
	(modify_visitors_at_site, "$g_custom_battle_scene"),
	(set_visitor,0,"trp_player"),
	(set_visitors,1,reg(11),reg(1)),
	(set_visitors,2,reg(12),reg(2)),
	(set_visitors,3,reg(13),reg(3)),
	(set_visitors,4,reg(14),reg(4)),
	(set_visitors,5,reg(15),reg(5)),
	(set_visitors,6,reg(16),reg(6)),
	(set_visitors,7,reg(17),reg(7)),
	(set_visitors,8,reg(18),reg(8)),
	(set_visitors,9,reg(19),reg(9)),
	(set_visitors,10,reg(20),reg(10)),
	
# Army 2
	(assign,reg(32),2),
	(troop_get_slot,reg(1),"trp_custom_battle_fac_2_troops", 1),
	(troop_get_slot,reg(2),"trp_custom_battle_fac_2_troops", 2),
	(troop_get_slot,reg(3),"trp_custom_battle_fac_2_troops", 3),
	(troop_get_slot,reg(4),"trp_custom_battle_fac_2_troops", 4),
	(troop_get_slot,reg(5),"trp_custom_battle_fac_2_troops", 5),
	(troop_get_slot,reg(6),"trp_custom_battle_fac_2_troops", 6),
	(troop_get_slot,reg(7),"trp_custom_battle_fac_2_troops", 7),
	(troop_get_slot,reg(8),"trp_custom_battle_fac_2_troops", 8),
	(troop_get_slot,reg(9),"trp_custom_battle_fac_2_troops", 9),
	(troop_get_slot,reg(10),"trp_custom_battle_fac_2_troops", 10),
	(call_script,"script_custom_battle_set_faction_troops"),
	(modify_visitors_at_site, "$g_custom_battle_scene"),
	(troop_get_slot,reg(30),"trp_custom_battle_spawn_store",2),
	(set_visitors,reg(30),reg(11),reg(1)),
	(val_add,reg(30),1),
	(set_visitors,reg(30),reg(12),reg(2)),
	(val_add,reg(30),1),
	(set_visitors,reg(30),reg(13),reg(3)),
	(val_add,reg(30),1),
	(set_visitors,reg(30),reg(14),reg(4)),
	(val_add,reg(30),1),
	(set_visitors,reg(30),reg(15),reg(5)),
	(val_add,reg(30),1),
	(set_visitors,reg(30),reg(16),reg(6)),
	(val_add,reg(30),1),
	(set_visitors,reg(30),reg(17),reg(7)),
	(val_add,reg(30),1),
	(set_visitors,reg(30),reg(18),reg(8)),
	(val_add,reg(30),1),
	(set_visitors,reg(30),reg(19),reg(9)),
	(val_add,reg(30),1),
	(set_visitors,reg(30),reg(20),reg(10)),
	
# Army 3
	(try_begin),
	(ge,"$g_custom_battle_num_factions",3),
	(assign,reg(32),3),
	(troop_get_slot,reg(1),"trp_custom_battle_fac_3_troops", 1),
	(troop_get_slot,reg(2),"trp_custom_battle_fac_3_troops", 2),
	(troop_get_slot,reg(3),"trp_custom_battle_fac_3_troops", 3),
	(troop_get_slot,reg(4),"trp_custom_battle_fac_3_troops", 4),
	(troop_get_slot,reg(5),"trp_custom_battle_fac_3_troops", 5),
	(troop_get_slot,reg(6),"trp_custom_battle_fac_3_troops", 6),
	(troop_get_slot,reg(7),"trp_custom_battle_fac_3_troops", 7),
	(troop_get_slot,reg(8),"trp_custom_battle_fac_3_troops", 8),
	(troop_get_slot,reg(9),"trp_custom_battle_fac_3_troops", 9),
	(troop_get_slot,reg(10),"trp_custom_battle_fac_3_troops", 10),
	(call_script,"script_custom_battle_set_faction_troops"),
	(modify_visitors_at_site, "$g_custom_battle_scene"),
	(troop_get_slot,reg(30),"trp_custom_battle_spawn_store",3),
	(set_visitors,reg(30),reg(11),reg(1)),
	(val_add,reg(30),1),
	(set_visitors,reg(30),reg(12),reg(2)),
	(val_add,reg(30),1),
	(set_visitors,reg(30),reg(13),reg(3)),
	(val_add,reg(30),1),
	(set_visitors,reg(30),reg(14),reg(4)),
	(val_add,reg(30),1),
	(set_visitors,reg(30),reg(15),reg(5)),
	(val_add,reg(30),1),
	(set_visitors,reg(30),reg(16),reg(6)),
	(val_add,reg(30),1),
	(set_visitors,reg(30),reg(17),reg(7)),
	(val_add,reg(30),1),
	(set_visitors,reg(30),reg(18),reg(8)),
	(val_add,reg(30),1),
	(set_visitors,reg(30),reg(19),reg(9)),
	(val_add,reg(30),1),
	(set_visitors,reg(30),reg(20),reg(10)),
	(try_end),
	
# Army 4
	(try_begin),
	(ge,"$g_custom_battle_num_factions",4),
	(assign,reg(32),4),
	(troop_get_slot,reg(1),"trp_custom_battle_fac_4_troops", 1),
	(troop_get_slot,reg(2),"trp_custom_battle_fac_4_troops", 2),
	(troop_get_slot,reg(3),"trp_custom_battle_fac_4_troops", 3),
	(troop_get_slot,reg(4),"trp_custom_battle_fac_4_troops", 4),
	(troop_get_slot,reg(5),"trp_custom_battle_fac_4_troops", 5),
	(troop_get_slot,reg(6),"trp_custom_battle_fac_4_troops", 6),
	(troop_get_slot,reg(7),"trp_custom_battle_fac_4_troops", 7),
	(troop_get_slot,reg(8),"trp_custom_battle_fac_4_troops", 8),
	(troop_get_slot,reg(9),"trp_custom_battle_fac_4_troops", 9),
	(troop_get_slot,reg(10),"trp_custom_battle_fac_4_troops", 10),
	(call_script,"script_custom_battle_set_faction_troops"),
	(modify_visitors_at_site, "$g_custom_battle_scene"),
	(troop_get_slot,reg(30),"trp_custom_battle_spawn_store",4),
	(set_visitors,reg(30),reg(11),reg(1)),
	(val_add,reg(30),1),
	(set_visitors,reg(30),reg(12),reg(2)),
	(val_add,reg(30),1),
	(set_visitors,reg(30),reg(13),reg(3)),
	(val_add,reg(30),1),
	(set_visitors,reg(30),reg(14),reg(4)),
	(val_add,reg(30),1),
	(set_visitors,reg(30),reg(15),reg(5)),
	(val_add,reg(30),1),
	(set_visitors,reg(30),reg(16),reg(6)),
	(val_add,reg(30),1),
	(set_visitors,reg(30),reg(17),reg(7)),
	(val_add,reg(30),1),
	(set_visitors,reg(30),reg(18),reg(8)),
	(val_add,reg(30),1),
	(set_visitors,reg(30),reg(19),reg(9)),
	(val_add,reg(30),1),
	(set_visitors,reg(30),reg(20),reg(10)),
	(try_end),
	
# Army 5
	(try_begin),
	(ge,"$g_custom_battle_num_factions",5),
	(assign,reg(32),5),
	(troop_get_slot,reg(1),"trp_custom_battle_fac_5_troops", 1),
	(troop_get_slot,reg(2),"trp_custom_battle_fac_5_troops", 2),
	(troop_get_slot,reg(3),"trp_custom_battle_fac_5_troops", 3),
	(troop_get_slot,reg(4),"trp_custom_battle_fac_5_troops", 4),
	(troop_get_slot,reg(5),"trp_custom_battle_fac_5_troops", 5),
	(troop_get_slot,reg(6),"trp_custom_battle_fac_5_troops", 6),
	(troop_get_slot,reg(7),"trp_custom_battle_fac_5_troops", 7),
	(troop_get_slot,reg(8),"trp_custom_battle_fac_5_troops", 8),
	(troop_get_slot,reg(9),"trp_custom_battle_fac_5_troops", 9),
	(troop_get_slot,reg(10),"trp_custom_battle_fac_5_troops", 10),
	(call_script,"script_custom_battle_set_faction_troops"),
	(modify_visitors_at_site, "$g_custom_battle_scene"),
	(troop_get_slot,reg(30),"trp_custom_battle_spawn_store",5),
	(set_visitors,reg(30),reg(11),reg(1)),
	(val_add,reg(30),1),
	(set_visitors,reg(30),reg(12),reg(2)),
	(val_add,reg(30),1),
	(set_visitors,reg(30),reg(13),reg(3)),
	(val_add,reg(30),1),
	(set_visitors,reg(30),reg(14),reg(4)),
	(val_add,reg(30),1),
	(set_visitors,reg(30),reg(15),reg(5)),
	(val_add,reg(30),1),
	(set_visitors,reg(30),reg(16),reg(6)),
	(val_add,reg(30),1),
	(set_visitors,reg(30),reg(17),reg(7)),
	(val_add,reg(30),1),
	(set_visitors,reg(30),reg(18),reg(8)),
	(val_add,reg(30),1),
	(set_visitors,reg(30),reg(19),reg(9)),
	(val_add,reg(30),1),
	(set_visitors,reg(30),reg(20),reg(10)),
	(try_end),

# # Army 6
	# (try_begin),
	# (ge,"$g_custom_battle_num_factions",6),
	# (assign,reg(32),6),
	# (troop_get_slot,reg(1),"trp_custom_battle_fac_6_troops", 1),
	# (troop_get_slot,reg(2),"trp_custom_battle_fac_6_troops", 2),
	# (troop_get_slot,reg(3),"trp_custom_battle_fac_6_troops", 3),
	# (troop_get_slot,reg(4),"trp_custom_battle_fac_6_troops", 4),
	# (troop_get_slot,reg(5),"trp_custom_battle_fac_6_troops", 5),
	# (troop_get_slot,reg(6),"trp_custom_battle_fac_6_troops", 6),
	# (troop_get_slot,reg(7),"trp_custom_battle_fac_6_troops", 7),
	# (troop_get_slot,reg(8),"trp_custom_battle_fac_6_troops", 8),
	# (troop_get_slot,reg(9),"trp_custom_battle_fac_6_troops", 9),
	# (troop_get_slot,reg(10),"trp_custom_battle_fac_6_troops", 10),
	# (call_script,"script_custom_battle_set_faction_troops"),
	# (modify_visitors_at_site, "$g_custom_battle_scene"),
	# (troop_get_slot,reg(30),"trp_custom_battle_spawn_store",6),
	# (set_visitors,reg(30),reg(11),reg(1)),
	# (val_add,reg(30),1),
	# (set_visitors,reg(30),reg(12),reg(2)),
	# (val_add,reg(30),1),
	# (set_visitors,reg(30),reg(13),reg(3)),
	# (val_add,reg(30),1),
	# (set_visitors,reg(30),reg(14),reg(4)),
	# (val_add,reg(30),1),
	# (set_visitors,reg(30),reg(15),reg(5)),
	# (val_add,reg(30),1),
	# (set_visitors,reg(30),reg(16),reg(6)),
	# (val_add,reg(30),1),
	# (set_visitors,reg(30),reg(17),reg(7)),
	# (val_add,reg(30),1),
	# (set_visitors,reg(30),reg(18),reg(8)),
	# (val_add,reg(30),1),
	# (set_visitors,reg(30),reg(19),reg(9)),
	# (val_add,reg(30),1),
	# (set_visitors,reg(30),reg(20),reg(10)),
	# (try_end),
	

# Set neutral troops
#	(try_begin),
#	(eq,"$g_custom_battle_location",8),
#	(modify_visitors_at_site, "$g_custom_battle_scene"),
#	(set_visitors, 21, "trp_farmer",12),
#	(set_visitors, 22, "trp_peasant_woman",8),
#	(else_try),
#	(eq,"$g_custom_battle_location",9),
#	(modify_visitors_at_site, "$g_custom_battle_scene"),
#	(set_visitors, 23, "trp_farmer",12),
#	(set_visitors, 24, "trp_peasant_woman",8),
#	(end_try),
     
	 ],
    
    [
      ("custom_battle_go",[],"Start.",
       [
	   (try_begin),
	   (eq,"$g_custom_battle_type",6),
	   (set_jump_mission,"mt_custom_battle_2vs2"),
	   (else_try),
	   (set_jump_mission,"mt_custom_battle_standard"),
	   (end_try),
        (jump_to_menu, "mnu_custom_battle_end"),
        (jump_to_scene,"$g_custom_battle_scene"),
        (change_screen_mission),
        ]
       ),
	  ("optional_settings", [], "Optional Settings",
	  [(jump_to_menu, "mnu_custom_battle_optional"),
	  ]
	  ),
#	  ("testing_menu", [], "Testing Menu",
#	  [(jump_to_menu, "mnu_custom_battle_test"),
#	  ]
#	  ),
    ]
  ),
  
# Testing Menu
(
	"custom_battle_test",menu_text_color(0xFF000d2c),
	"The factions for this battle are:{s1},{s2},{s3},{s4},{s5}.",
	"none",
	[
# Display team factions
	# Team One
	(troop_get_slot,reg(1),"trp_custom_battle_fac_store",1),
	(try_begin),
	(eq,reg(1),1),
	(str_store_string,s1,"str_galacticempire"),
	(else_try),
	(eq,reg(1),2),
	(str_store_string,s1,"str_rebelalliance"),
	(else_try),
	(eq,reg(1),3),
	(str_store_string,s1,"str_huttcartel"),
	(else_try),
	(eq,reg(1),4),
	(str_store_string,s1,"str_faction_4"),
	(else_try),
	(eq,reg(1),5),
	(str_store_string,s1,"str_faction_5"),
	(else_try),
	(str_store_string,s1,"str_no_faction"),
	(end_try),
	# Team Two
	(troop_get_slot,reg(2),"trp_custom_battle_fac_store",2),
	(try_begin),
	(eq,reg(2),1),
	(str_store_string,s2,"str_galacticempire"),
	(else_try),
	(eq,reg(2),2),
	(str_store_string,s2,"str_rebelalliance"),
	(else_try),
	(eq,reg(2),3),
	(str_store_string,s2,"str_huttcartel"),
	(else_try),
	(eq,reg(2),4),
	(str_store_string,s2,"str_faction_4"),
	(else_try),
	(eq,reg(2),5),
	(str_store_string,s2,"str_faction_5"),
	(else_try),
	(str_store_string,s2,"str_no_faction"),
	(end_try),
	# Team One
	(troop_get_slot,reg(3),"trp_custom_battle_fac_store",3),
	(try_begin),
	(eq,reg(3),1),
	(str_store_string,s3,"str_galacticempire"),
	(else_try),
	(eq,reg(3),2),
	(str_store_string,s3,"str_rebelalliance"),
	(else_try),
	(eq,reg(3),3),
	(str_store_string,s3,"str_huttcartel"),
	(else_try),
	(eq,reg(3),4),
	(str_store_string,s3,"str_faction_4"),
	(else_try),
	(eq,reg(3),5),
	(str_store_string,s3,"str_faction_5"),
	(else_try),
	(str_store_string,s3,"str_no_faction"),
	(end_try),
	# Team One
	(troop_get_slot,reg(4),"trp_custom_battle_fac_store",4),
	(try_begin),
	(eq,reg(4),1),
	(str_store_string,s4,"str_galacticempire"),
	(else_try),
	(eq,reg(4),2),
	(str_store_string,s4,"str_rebelalliance"),
	(else_try),
	(eq,reg(4),3),
	(str_store_string,s4,"str_huttcartel"),
	(else_try),
	(eq,reg(4),4),
	(str_store_string,s4,"str_faction_4"),
	(else_try),
	(eq,reg(4),5),
	(str_store_string,s4,"str_faction_5"),
	(else_try),
	(str_store_string,s4,"str_no_faction"),
	(end_try),
	# Team Five
	(troop_get_slot,reg(5),"trp_custom_battle_fac_store",5),
	(try_begin),
	(eq,reg(5),1),
	(str_store_string,s5,"str_galacticempire"),
	(else_try),
	(eq,reg(5),2),
	(str_store_string,s5,"str_rebelalliance"),
	(else_try),
	(eq,reg(5),3),
	(str_store_string,s5,"str_huttcartel"),
	(else_try),
	(eq,reg(5),4),
	(str_store_string,s5,"str_faction_4"),
	(else_try),
	(eq,reg(5),5),
	(str_store_string,s5,"str_faction_5"),
	(else_try),
	(str_store_string,s5,"str_no_faction"),
	(end_try),
	],
	[
	("team_1",[],"Show team one troops",
	[(assign,reg(30),"trp_custom_battle_fac_1_troops"),
	(jump_to_menu,"mnu_custom_battle_test_troops")]
	),
	("team_2",[],"Show team two troops",
	[(assign,reg(30),"trp_custom_battle_fac_2_troops"),
	(jump_to_menu,"mnu_custom_battle_test_troops")]
	),
	("team_3",[],"Show team three troops",
	[(assign,reg(30),"trp_custom_battle_fac_3_troops"),
	(jump_to_menu,"mnu_custom_battle_test_troops")]
	),
	("team_4",[],"Show team four troops",
	[(assign,reg(30),"trp_custom_battle_fac_4_troops"),
	(jump_to_menu,"mnu_custom_battle_test_troops")]
	),
	("team_5",[],"Show team five troops",
	[(assign,reg(30),"trp_custom_battle_fac_5_troops"),
	(jump_to_menu,"mnu_custom_battle_test_troops")]
	),
	("team_6",[],"Show team six troops",
	[(assign,reg(30),"trp_custom_battle_fac_6_troops"),
	(jump_to_menu,"mnu_custom_battle_test_troops")]
	),
	("continue",[],"Continue",
	[(jump_to_menu,"mnu_custom_battle_config_finish")]
	),
	]
	),
	
(
	"custom_battle_test_troops",menu_text_color(0xFF000d2c),
	"The number of troops for this team are:{reg1},{reg2},{reg3},{reg4},{reg5},{reg6},{reg7},{reg8},{reg9},{reg10}",
	"none",
	[
# Display team troops
	(troop_get_slot,reg(1),reg(30),1),
	(troop_get_slot,reg(2),reg(30),2),
	(troop_get_slot,reg(3),reg(30),3),
	(troop_get_slot,reg(4),reg(30),4),
	(troop_get_slot,reg(5),reg(30),5),
	(troop_get_slot,reg(6),reg(30),6),
	(troop_get_slot,reg(7),reg(30),7),
	(troop_get_slot,reg(8),reg(30),8),
	(troop_get_slot,reg(9),reg(30),9),
	(troop_get_slot,reg(10),reg(30),10),	
	],
	[
	("back_to_test_menu",[],"Back to test menu",
	[(jump_to_menu,"mnu_custom_battle_test")]
	),
	]
	),
  (
    "custom_battle_optional",menu_text_color(0xFF000d2c),
	"From here the time of day and the weather can be changed.",
	"none",
	[
	(try_begin),
	  (eq, "$g_rain_settings", 0),
	  (str_store_string, 1, "str_custom_battle_rain_0"),
	  (else_try),
	  (eq, "$g_rain_settings", 1),
	  (str_store_string, 1, "str_custom_battle_rain_1"),
	  (else_try),
	  (eq, "$g_rain_settings", 2),
	  (str_store_string, 1, "str_custom_battle_rain_2"),
	  (else_try),
	  (eq, "$g_rain_settings", 3),
	  (str_store_string, 1, "str_custom_battle_rain_3"),
	  (else_try),
	  (eq, "$g_rain_settings", 4),
	  (str_store_string, 1, "str_custom_battle_rain_4"),
	  (else_try),
	  (eq, "$g_rain_settings", 5),
	  (str_store_string, 1, "str_custom_battle_rain_5"),
	  (else_try),
	  (eq, "$g_rain_settings", 6),
	  (str_store_string, 1, "str_custom_battle_rain_6"),
	  (end_try),
	(try_begin),
	  (eq, "$g_fog_settings", 0),
	  (str_store_string, 2, "str_custom_battle_fog_0"),
	  (else_try),
	  (eq, "$g_fog_settings", 1),
	  (str_store_string, 2, "str_custom_battle_fog_1"),
	  (else_try),
	  (eq, "$g_fog_settings", 2),
	  (str_store_string, 2, "str_custom_battle_fog_2"),
	  (else_try),
	  (eq, "$g_fog_settings", 3),
	  (str_store_string, 2, "str_custom_battle_fog_3"),
	  (end_try),
	],
	[
	  ("rain",[],"Rain/Snow ({s1})",
	  [(try_begin),
	  (eq, "$g_rain_settings", 0),
	  (assign, "$g_rain_settings", 1),
	  (else_try),
	  (eq, "$g_rain_settings", 1),
	  (assign, "$g_rain_settings", 2),
	  (else_try),
	  (eq, "$g_rain_settings", 2),
	  (assign, "$g_rain_settings", 3),
	  (else_try),
	  (eq, "$g_rain_settings", 3),
	  (assign, "$g_rain_settings", 4),
	  (else_try),
	  (eq, "$g_rain_settings", 4),
	  (assign, "$g_rain_settings", 5),
	  (else_try),
	  (eq, "$g_rain_settings", 5),
	  (assign, "$g_rain_settings", 6),
	  (else_try),
	  (eq, "$g_rain_settings", 6),
	  (assign, "$g_rain_settings", 0),
	  (end_try),
	   ]
	   ),
	  ("fog",[],"Fog ({s2})",
	  [(try_begin),
	  (eq, "$g_fog_settings", 0),
	  (assign, "$g_fog_settings", 1),
	  (else_try),
	  (eq, "$g_fog_settings", 1),
	  (assign, "$g_fog_settings", 2),
	  (else_try),
	  (eq, "$g_fog_settings", 2),
	  (assign, "$g_fog_settings", 3),
	  (else_try),
	  (eq, "$g_fog_settings", 3),
	  (assign, "$g_fog_settings", 0),
	  (end_try),
	   ]
	   ),
	  ("next",[],"Next",
	  [(jump_to_menu, "mnu_custom_battle_config_finish")]
	  ),
	]
  ),
  (
    "custom_battle_end",menu_text_color(0xFF000d2c),
    "Battle is over. {s1} Your party killed {reg5} troops, enemy party killed {reg6} troops. You have killed {reg7} troops.",
    "none",
    [(assign, reg5, "$g_custom_battle_team2_death_count"),
     (assign, reg6, "$g_custom_battle_team1_death_count"),
     (get_player_agent_kill_count, ":kill_count"),
     (get_player_agent_kill_count, ":wound_count", 1),
     (store_add, reg7, ":kill_count", ":wound_count"),
     (try_begin),
       (eq, "$g_battle_result", 1),
       (str_store_string, s1, "str_battle_won"),
     (else_try),
       (str_store_string, s1, "str_battle_lost"),
     (try_end),],
    [
      ("exit",[],"Exit to main menu",
       [(change_screen_quit),
        ]
       ),
      ("replay",[],"Replay this battle",
       [(jump_to_menu, "mnu_custom_battle_config_finish"),
        ]
       ),
      ("new_battle",[],"Set up a new battle",
       [(jump_to_menu, "mnu_custom_battle_config_1"),
	   	# Set all friendly troop values to zero.
    (assign, "$g_custom_battle_location", 0),

	# Reset weather settings
	(assign,"$g_rain_settings",0),
	(assign,"$g_fog_settings",0),
	# Reset class setttings
	(assign,"$g_custom_battle_class",0),
	(assign,"$g_custom_battle_sub_class",0),
	# Remove all equipment
	(troop_set_inventory_slot,"trp_player",0,0),
	(troop_set_inventory_slot,"trp_player",1,0),
	(troop_set_inventory_slot,"trp_player",2,0),
	(troop_set_inventory_slot,"trp_player",3,0),
	(troop_set_inventory_slot,"trp_player",4,0),
	(troop_set_inventory_slot,"trp_player",5,0),
	(troop_set_inventory_slot,"trp_player",6,0),
	(troop_set_inventory_slot,"trp_player",7,0),
	(troop_set_inventory_slot,"trp_player",8,0),
        ]
       ),
    ]
  ),

# END OF CUSTOM BATTLE
#==========================================================================================================

########################################################
# Autoloot Game Menus Begin
########################################################
  
	##########################################################
	# Inventory allocation / Loot allocation Game Menu  -  by Fisheye
	# Parameters:
	# $return_menu : return to this menu after managing loot.  0 if this menu is called via random encounter
	("manage_loot_pool",
		0,
		"{s10}",
		"none",
		[
			(assign, "$pool_troop", "trp_temp_troop"),
			(assign, reg20,0),
			(troop_get_inventory_capacity, ":inv_cap", "$pool_troop"),
				(try_for_range, ":i_slot", 0, ":inv_cap"),
					(troop_get_inventory_slot, ":item_id", "$pool_troop", ":i_slot"),
					(ge, ":item_id", 0),
					(val_add, reg20,1),
				(try_end),
				# reg20 now contains number of items in loot pool
				(try_begin),
					(eq, reg20, 0),
					(str_store_string, 10, "str_item_pool_no_items"),
					(str_store_string, 20, "str_item_pool_leave"),
				(else_try),
					(eq, reg20, 1),
					(str_store_string, 10, "str_item_pool_one_item"),
					(str_store_string, 20, "str_item_pool_abandon"),
				(else_try),
					(str_store_string, 10, "str_item_pool_many_items"),
					(str_store_string, 20, "str_item_pool_abandon"),
				(try_end),
			(assign, reg10, 0),
			(assign, reg11, 0),
			(assign, reg12, 0),
			(assign, reg13, 0),
			(assign, reg14, 0),
			(party_get_num_companion_stacks, ":num_stacks","p_main_party"),
				(try_for_range, ":i_stack", 1, ":num_stacks"),
					(party_stack_get_troop_id,":stack_troop","p_main_party",":i_stack"),
					(is_between, ":stack_troop", companions_begin, companions_end),
					(val_add, reg10, 1),
						(try_begin),
							(store_add, reg2, "$inventory_menu_offset", 1),
							(eq, reg10, reg2),
							(assign, reg11, ":stack_troop"),
							(str_store_troop_name, 11, ":stack_troop"),
						(else_try),
							(store_add, reg2, "$inventory_menu_offset", 2),
							(eq, reg10, reg2),
							(assign, reg12, ":stack_troop"),
							(str_store_troop_name, 12, ":stack_troop"),
						(else_try),
							(store_add, reg2, "$inventory_menu_offset", 3),
							(eq, reg10, reg2),
							(assign, reg13, ":stack_troop"),
							(str_store_troop_name, 13, ":stack_troop"),
						(else_try),
							(store_add, reg2, "$inventory_menu_offset", 4),
							(eq, reg10, reg2),
							(assign, reg14, ":stack_troop"),
							(str_store_troop_name, 14, ":stack_troop"),
						(try_end),
				(try_end),
			# reg10 now contains total num of heroes
		],
		[
			("auto_loot",
				[
					(eq, "$inventory_menu_offset",0),
					(store_free_inventory_capacity, ":space", "$pool_troop"),
					(ge, ":space", 10)
				],
				"Let your heroes select gear from the item pool.",
				[
					(jump_to_menu, "mnu_auto_loot")
				]
			),
			("auto_loot_no",
				[
					(eq, "$inventory_menu_offset",0),
					(store_free_inventory_capacity, ":space", "$pool_troop"),
					(lt, ":space", 10),
					(disable_menu_option)
				],
				"Insufficient item pool space for auto-upgrade.",
				[]
			),
			("prev_page_dot",
				[
					(neq, "$inventory_menu_offset",0)
				],
				"Previous page.",
				[
					(val_sub, "$inventory_menu_offset", num_loot_management_menu_heroes),
					(jump_to_menu, "mnu_manage_loot_pool")
				]
			),
			("more_party_members",
				[
						(try_begin),
							(le, reg10, num_loot_management_menu_heroes), #enough entries for everyone
							(disable_menu_option),
						(else_try),
							# allow "next page" of heroes
							(store_sub, reg2, reg10, num_loot_management_menu_heroes),
							#  if already at last page
							(ge, "$inventory_menu_offset",reg2),
							# disable "next page" option
							(disable_menu_option),
						(try_end),
				],
				"More party members...",
				[
					(val_add, "$inventory_menu_offset", num_loot_management_menu_heroes),
					(jump_to_menu, "mnu_manage_loot_pool")
				]
			),
			("loot",
				[],
				"Access the item pool.",
				[
					(change_screen_loot, "$pool_troop")
				]
			),
			("companion1",
				[
					(gt, reg11, 0)
				],
				"Talk to {s11}",
				[
					(call_script, "script_loot_menu_talk", reg11)
				]
			),
			("companion2",
				[
					(gt, reg12, 0)
				],
				"Talk to {s12}",
				[
					(call_script, "script_loot_menu_talk", reg12)
				]
			),
			("companion3",
				[
					(gt, reg13, 0)
				],
				"Talk to {s13}",
				[
					(call_script, "script_loot_menu_talk", reg13)
				]
			),
			("companion4",
				[
					(gt, reg14, 0)
				],
				"Talk to {s14}",
				[
					(call_script, "script_loot_menu_talk", reg14)
				]
			),
			("autoloot_no_items",
				[],
				"{s20}",
				[
				    (assign, "$g_camp_talk",0),
					(jump_to_menu, "$return_menu"),					
				]
			),
		]
	  ),
	
	("auto_loot",
		0,
		"Your heroes will automatically grab items from the item pool based on their pre-selected upgrade options. Heroes listed first in the party order will have first pick. Any equipment no longer needed will be placed back into the item pool. Are you sure you wish to do this?",
		"none",
		[],
		[
			("No",
				[],
				"No, I've changed my mind.",
				[
					(jump_to_menu, "mnu_manage_loot_pool")
				]
			),
			("Yes",
				[],
				"Yes, perform the upgrading.",
				[
					(call_script, "script_auto_loot_all"),
					(jump_to_menu, "mnu_manage_loot_pool")
				]
			),
		]
	),
####################################################################################	

#SW start Trade base menus
("trade_base", 0,
	"You arrive at {s1}. There are a number of ^facilities here. Which one do you want to visit?" ,"none", 
	[
		#get the name of the location
		(str_store_party_name, s1, "$g_encountered_party"),
	],
	[
	
	("trade_1", [],
	"Go to the shipyard.",
		[(jump_to_menu, "mnu_shipyard")]),

	("trade_2", [],
	"Go to the bank.",
		[(jump_to_menu, "mnu_bank")]),
		
	# ("trade_3", [],
	# "Go to the shipyard",
		# [(jump_to_menu, "mnu_shipyard")]),
		
	("trade_3", [],
	"Go to the merchants.",
		[
			#may be necessary for dialogs to work correctly?
			#(assign, "$talk_context", 0),
			(assign, "$talk_context", tc_tavern_talk),
		
			#modify/reset visitors
			(modify_visitors_at_site,"scn_trade_federation"),
			#(modify_visitors_at_site,"scn_mainplanet_mandalore_tavern"),
			(reset_visitors),
			
			#set the player entry point
			(set_visitor, 0, "$g_player_troop"),
			
			#set the merchants entry points
			(store_random_in_range, ":troop_no", tavern_fs_trainer_begin, tavern_fs_trainer_end),
			(set_visitor, 30, ":troop_no"),
			(store_random_in_range, ":troop_no", tavern_ce_merchant_begin, tavern_ce_merchant_end),
			(set_visitor, 31, ":troop_no"),
			(store_random_in_range, ":troop_no", tavern_dp_merchant_begin, tavern_dp_merchant_end),
			(set_visitor, 32, ":troop_no"),			
			(store_random_in_range, ":troop_no", tavern_iw_merchant_begin, tavern_iw_merchant_end),
			(set_visitor, 33, ":troop_no"),
			#(store_random_in_range, ":troop_no", tavern_ps_merchant_begin, tavern_ps_merchant_end),
			(set_visitor, 34, "trp_ramun_the_slave_trader"),
			(store_random_in_range, ":troop_no", tavern_ps_merchant_begin, tavern_ps_merchant_end),
			(set_visitor, 35, ":troop_no"),	
			(store_random_in_range, ":troop_no", tavern_fs_merchant_begin, tavern_fs_merchant_end),
			(set_visitor, 36, ":troop_no"),	
			#set bounty hunter
			#(set_visitor, 37, "trp_bounty_hunter"),
			#slave dancers - entry #38
			(store_random_in_range, ":random", 1, 5),
			(try_begin),
				(eq,":random",1),
				(set_visitor, 38, "trp_mainplanet_walker_twilek_female_slave"),
			(else_try),
				(eq, ":random", 2),
				(set_visitor, 38, "trp_mainplanet_walker_slave_dancer"),
			(else_try),
				(eq, ":random", 3),
				(set_visitor, 38, "trp_mainplanet_walker_hutt_4"),
			(else_try),
				#do nothing
			(try_end),
			#slave dancers - entry #39
			(store_random_in_range, ":random", 1, 5),
			(try_begin),
				(eq,":random",1),
				(set_visitor, 39, "trp_mainplanet_walker_twilek_female_slave"),
			(else_try),
				(eq, ":random", 2),
				(set_visitor, 39, "trp_mainplanet_walker_slave_dancer"),
			(else_try),
				(eq, ":random", 3),
				(set_visitor, 39, "trp_mainplanet_walker_hutt_4"),
			(else_try),
				#do nothing
			(try_end),

			#set the mission template
			(set_jump_mission,"mt_trade_federation"),
			#(set_jump_mission,"mt_cantina_default"),
			
			#jump to the scene
			(jump_to_scene,"scn_trade_federation"),
			#(jump_to_scene,"scn_mainplanet_mandalore_tavern"),			
			
			#start the scene
			(change_screen_mission),			
		]),		
		
	("leave_dot", [],
	"Leave.", [(change_screen_map)]),

	# ("trade_5", [
		# #(eq, 2,1),	#make sure this menu always stays hidden since its only used in the trade merchants scene
		# ],
		# "Go back to the trade menu",
		# [
		# (jump_to_menu, "mnu_trade_base")
		# ],
		# "Leave"),
	]),		

("shipyard", 0,
	"You enter the Shipyard. {s1}{s4}", "none", 
	[
	
		#setup the required slots for all spaceships (eventually move to game start)
		(call_script, "script_setup_spaceship_slots"),
		
		#set the ships that are available at this shipyard
		# (assign, "$g_ship_choice_1", "p_spaceship_z95"),
		# (assign, "$g_ship_choice_2", "p_spaceship_mercenary_raider"),
		# (assign, "$g_ship_choice_3", "p_spaceship_z95"),
		# (assign, "$g_ship_choice_4", "p_spaceship_mercenary_raider"),
		# (assign, "$g_ship_choice_5", "p_spaceship_z95"),
		# (assign, "$g_ship_choice_6", "p_spaceship_mercenary_raider"),
		# (assign, "$g_ship_choice_7", "p_spaceship_z95"),
		#use random ships

		(try_begin),
			(this_or_next|eq, "$g_encountered_party", "p_shipyard_trade_federation"),
			(eq, "$g_encountered_party", "p_shipyard_mandalore"),
			(store_random_in_range, "$g_ship_choice_1", spaceship_hutt_other_begin, spaceship_hutt_other_end),
			(store_random_in_range, "$g_ship_choice_2", spaceship_hutt_other_begin, spaceship_hutt_other_end),
			(store_random_in_range, "$g_ship_choice_3", spaceship_hutt_other_begin, spaceship_hutt_other_end),
			(store_random_in_range, "$g_ship_choice_4", spaceship_hutt_other_begin, spaceship_hutt_other_end),
			(store_random_in_range, "$g_ship_choice_5", spaceship_hutt_other_begin, spaceship_hutt_other_end),
			(store_random_in_range, "$g_ship_choice_6", spaceship_hutt_other_begin, spaceship_hutt_other_end),
			(store_random_in_range, "$g_ship_choice_7", spaceship_hutt_other_begin, spaceship_hutt_other_end),
		(else_try),
			(eq, "$g_encountered_party", "p_shipyard_corellia"),
			#(store_random_in_range, "$g_ship_choice_1", spaceship_rebel_begin, spaceship_rebel_end),
			#(store_random_in_range, "$g_ship_choice_2", spaceship_rebel_begin, spaceship_rebel_end),
			#(store_random_in_range, "$g_ship_choice_3", spaceship_rebel_begin, spaceship_rebel_end),
			(store_random_in_range, "$g_ship_choice_1", spaceship_rebel_corel_begin, spaceship_rebel_corel_end),
			(store_random_in_range, "$g_ship_choice_2", spaceship_rebel_corel_begin, spaceship_rebel_corel_end),
			(store_random_in_range, "$g_ship_choice_3", spaceship_rebel_corel_begin, spaceship_rebel_corel_end),
			(store_random_in_range, "$g_ship_choice_4", spaceship_rebel_begin, spaceship_rebel_end),
			(store_random_in_range, "$g_ship_choice_5", spaceship_other_begin, spaceship_other_end),
			(store_random_in_range, "$g_ship_choice_6", spaceship_other_begin, spaceship_other_end),
			(store_random_in_range, "$g_ship_choice_7", spaceship_other_begin, spaceship_other_end),
		(else_try),
			(eq, "$g_encountered_party", "p_shipyard_moncal"),
			(store_random_in_range, "$g_ship_choice_1", spaceship_rebel_moncal_begin, spaceship_rebel_moncal_end),
			(store_random_in_range, "$g_ship_choice_2", spaceship_rebel_moncal_begin, spaceship_rebel_moncal_end),
			(store_random_in_range, "$g_ship_choice_3", spaceship_rebel_begin, spaceship_rebel_end),
			(store_random_in_range, "$g_ship_choice_4", spaceship_rebel_begin, spaceship_rebel_end),
			(store_random_in_range, "$g_ship_choice_5", spaceship_empire_begin, spaceship_empire_end),
			(store_random_in_range, "$g_ship_choice_6", spaceship_empire_begin, spaceship_empire_end),
			(store_random_in_range, "$g_ship_choice_7", spaceship_empire_begin, spaceship_empire_end),
		(else_try),
			(this_or_next|eq, "$g_encountered_party", "p_shipyard_fondor"),
			(this_or_next|eq, "$g_encountered_party", "p_shipyard_raxus"),
			(eq, "$g_encountered_party", "p_shipyard_kuat"),
			(store_random_in_range, "$g_ship_choice_1", spaceship_empire_begin, spaceship_empire_end),
			(store_random_in_range, "$g_ship_choice_2", spaceship_empire_begin, spaceship_empire_end),
			(store_random_in_range, "$g_ship_choice_3", spaceship_empire_begin, spaceship_empire_end),
			(store_random_in_range, "$g_ship_choice_4", spaceship_empire_begin, spaceship_empire_end),
			(store_random_in_range, "$g_ship_choice_5", spaceship_other_begin, spaceship_other_end),
			(store_random_in_range, "$g_ship_choice_6", spaceship_other_begin, spaceship_other_end),
			(store_random_in_range, "$g_ship_choice_7", spaceship_other_begin, spaceship_other_end),
		(else_try),
			#safety
			(store_random_in_range, "$g_ship_choice_1", spaceship_all_begin, spaceship_all_end),
			(store_random_in_range, "$g_ship_choice_2", spaceship_all_begin, spaceship_all_end),
			(store_random_in_range, "$g_ship_choice_3", spaceship_all_begin, spaceship_all_end),
			(store_random_in_range, "$g_ship_choice_4", spaceship_all_begin, spaceship_all_end),
			(store_random_in_range, "$g_ship_choice_5", spaceship_all_begin, spaceship_all_end),
			(store_random_in_range, "$g_ship_choice_6", spaceship_all_begin, spaceship_all_end),
			(store_random_in_range, "$g_ship_choice_7", spaceship_all_begin, spaceship_all_end),
		(try_end),

		#testing
		#(troop_set_slot, "trp_player", slot_troop_has_spaceship, "p_spaceship_z95"),
	
		(assign, ":troop_no", "trp_player"),
		(troop_get_slot, ":spaceship", ":troop_no", slot_troop_has_spaceship),
		(try_begin),
			(le, ":spaceship", 0),
			(str_store_string, s1, "@^^^You currently don't own a spaceship"),
			(str_clear, s4),
		(else_try),
			(str_clear, s1),(str_clear, s3),(str_clear, s4),
			(party_get_slot, ":name", ":spaceship", slot_spaceship_name),
			(str_store_string, s3, ":name"),
			(str_store_string, s4, "@^^To buy a new ship, you will have to sell your current one first."),
			(str_store_string, s1, "@^^^Your current ship is a {s3}"),
		(try_end),
		],
	[
	#("shipyard_1",[], "Look at the available ships", 
	#		[(assign, "$g_ship_type", 1),(assign, "$g_ship_icon", "icon_z96"),(start_presentation, "prsnt_starship")]),	
	("shipyard_1",[], "Look at the available ships.", 
			[
				# this is the far left currently selected ship and icon for when the presentation loads
				(assign, "$g_ship_type", "$g_ship_choice_1"),
				(party_get_slot, "$g_ship_icon", "$g_ship_type", slot_spaceship_icon),
				(start_presentation, "prsnt_starship")
			]),
	("shipyard_2",[(troop_slot_ge, "trp_player", slot_troop_has_spaceship, 1)], "Upgrade your current ship.",
			[(assign, "$g_presentation_details", 0),(start_presentation, "prsnt_ship_details")]),
	
	("shipyard_3",[(troop_slot_ge, "trp_player", slot_troop_has_spaceship, 1)], "Sell your current ship.",
			[(assign, "$g_presentation_details", 2),(start_presentation, "prsnt_ship_details")]), 
			
	("leave_dot",[], "Leave.", 
			[(jump_to_menu, "mnu_trade_base")]),
]),

  (
    "bank",menu_text_color(0xFF000d2c),
    #"You visit the bank of the {s1}.\
	"You visit the bank.\
 ^^You can deposit money and earn interest, or take a loan.\
 ^^You currently have {reg6} credits deposited with this bank.\
{s3} {s2}\
 ^^The current interest rate is {reg10}% for deposits and {reg9}% for loans.",
    "none",
    [
	 #(str_store_faction_name, s1, "fac_trade_federation"),
     (faction_get_slot,"$g_player_debt","fac_trade_federation",slot_faction_bank_debt),
     (faction_get_slot,"$g_player_deposit","fac_trade_federation",slot_faction_bank_deposit),
	 (faction_get_slot,":debt_expires","fac_trade_federation",slot_faction_debt_expires),
	 (faction_get_slot,":cur_interest_debt","fac_trade_federation",slot_faction_debt_interest),
	 (faction_get_slot,":cur_interest_deposit","fac_trade_federation",slot_faction_deposit_interest),
	 (store_current_hours, ":cur_hours"),
	 (store_sub, ":time_left", ":debt_expires", ":cur_hours"), 
	 (assign, reg6, "$g_player_deposit"),
     (assign, reg7, "$g_player_debt"),
	 (assign, reg9, ":cur_interest_debt"),
	 (assign, reg10, ":cur_interest_deposit"),

	 (try_begin),
		 (gt, "$g_player_debt", 0),
		 (str_store_string, s3, "@^^Your outstanding loan amount is {reg7}."),
		 (try_begin),
			(gt, ":time_left", 0),
			(store_div, reg8,":time_left", 24), #nr of days left
			(str_store_string, s2, "@ The loan is due in {reg8} days."), 

		(else_try),

			(str_store_string, s2, "@ The loan is overdue."),
		 (try_end),
	 (else_try),
		(str_clear, s2),
		(str_clear, s3),
	 (try_end),
	 ],
    [
      ("take_loan",[(faction_slot_eq, "fac_trade_federation", slot_faction_bank_debt, 0)],"Apply for a loan.",
       [(jump_to_menu, "mnu_take_out_loan")
        ]),
      ("give_loan",[(store_troop_gold,":player_wealth", "trp_player"),(gt,":player_wealth",1000),(gt,"$g_player_debt",1000)],"Repay 1000 credits of your debt.",
       [
	   (troop_remove_gold, "trp_player", 1000),
           (val_sub, "$g_player_debt", 1000),
      (faction_set_slot,"fac_trade_federation",slot_faction_bank_debt,"$g_player_debt"),
        ]),
      ("give_loan_all",[(store_troop_gold,":player_wealth", "trp_player"),(gt,":player_wealth","$g_player_debt"),(gt,"$g_player_debt",0)],"Repay all of your debt.",
       [
	   (troop_remove_gold, "trp_player", "$g_player_debt"),
           (val_sub, "$g_player_debt", "$g_player_debt"),
      (faction_set_slot,"fac_trade_federation",slot_faction_bank_debt,"$g_player_debt"),
        ]),
      ("give_deposit",[(store_troop_gold,":player_wealth", "trp_player"),(gt,":player_wealth",1000)],"Deposit 1000 credits with the bank.",
       [
	   (troop_remove_gold, "trp_player", 1000),
           (val_add, "$g_player_deposit", 1000),
      (faction_set_slot,"fac_trade_federation",slot_faction_bank_deposit,"$g_player_deposit"),
        ]),
      ("take_deposit",[(ge,"$g_player_deposit",1000)],"Withdraw 1000 credits from your account.",
       [
	   (troop_add_gold, "trp_player", 1000),
           (val_sub, "$g_player_deposit", 1000),
      (faction_set_slot,"fac_trade_federation",slot_faction_bank_deposit,"$g_player_deposit"),
        ]),
      ("take_deposit_all",[(ge,"$g_player_deposit",1)],"Withdraw all funds from your account.",
       [
	   (troop_add_gold, "trp_player", reg6),
           (val_sub, "$g_player_deposit", reg6),
      (faction_set_slot,"fac_trade_federation",slot_faction_bank_deposit,"$g_player_deposit"),
        ]),
      ("head_back",[],"Head back.",
       [
           (jump_to_menu,"mnu_trade_base"),
        ]),
]),

("take_out_loan", 0, 
"The loan officer at the bank has approved you for a loan.\
^^You can only take out one loan at a time. The interest will be set at the time you take the loan and the amount will be added to your total debt.\
^^All loans run for 30 days. You will need to repay your loan before that time runs out.", "none", [(faction_get_slot,"$g_cur_interest_debt","fac_trade_federation",slot_faction_debt_interest),],
[
	("1000_credits", [
		(store_add, ":interest_multiplier", "$g_cur_interest_debt", 100),
		(store_mul, ":total_debt", ":interest_multiplier", 1000),
		(val_div, ":total_debt", 100),
		(assign, reg11, ":total_debt"),

		
	], "Take a loan of 1000 credits. You'll have to repay {reg11} credits.",
		[
		(troop_add_gold, "trp_player", 1000),
		(store_add, ":interest_multiplier", "$g_cur_interest_debt", 100),
		(store_mul, ":total_debt", ":interest_multiplier", 1000),
		(val_div, ":total_debt", 100),
		(val_add, "$g_player_debt", ":total_debt"),
		(faction_set_slot,"fac_trade_federation",slot_faction_bank_debt,"$g_player_debt"),
		(store_current_hours, ":cur_hours"),
		(val_add, ":cur_hours", 720), #720 hours is 30 days which added to cur_hours gives time of expiry
		(faction_set_slot,"fac_trade_federation",slot_faction_debt_expires,":cur_hours"),
		(jump_to_menu, "mnu_bank"),
		]),
	("2500_credits", [
		(store_add, ":interest_multiplier", "$g_cur_interest_debt", 100),
		(store_mul, ":total_debt", ":interest_multiplier", 2500),
		(val_div, ":total_debt", 100),
		(assign, reg11, ":total_debt"),
	], "Take a loan of 2500 credits. You'll have to repay {reg11} credits.",
		[
		(troop_add_gold, "trp_player", 2500),
		(store_add, ":interest_multiplier", "$g_cur_interest_debt", 100),
		(store_mul, ":total_debt", ":interest_multiplier", 2500),
		(val_div, ":total_debt", 100),
		(val_add, "$g_player_debt", ":total_debt"),
		(faction_set_slot,"fac_trade_federation",slot_faction_bank_debt,"$g_player_debt"),
		(store_current_hours, ":cur_hours"),
		(val_add, ":cur_hours", 720), #720 hours is 30 days which added to cur_hours gives time of expiry
		(faction_set_slot,"fac_trade_federation",slot_faction_debt_expires,":cur_hours"),
		(jump_to_menu, "mnu_bank"),
		]),
	("5000_credits", [
		(store_add, ":interest_multiplier", "$g_cur_interest_debt", 100),
		(store_mul, ":total_debt", ":interest_multiplier", 5000),
		(val_div, ":total_debt", 100),
		(assign, reg11, ":total_debt"),
	], "Take a loan of 5000 credits. You'll have to repay {reg11} credits.",
		[
		(troop_add_gold, "trp_player", 5000),
		(store_add, ":interest_multiplier", "$g_cur_interest_debt", 100),
		(store_mul, ":total_debt", ":interest_multiplier", 5000),
		(val_div, ":total_debt", 100),
		(val_add, "$g_player_debt", ":total_debt"),
		(faction_set_slot,"fac_trade_federation",slot_faction_bank_debt,"$g_player_debt"),
		(store_current_hours, ":cur_hours"),
		(val_add, ":cur_hours", 720), #720 hours is 30 days which added to cur_hours gives time of expiry
		(faction_set_slot,"fac_trade_federation",slot_faction_debt_expires,":cur_hours"),
		(jump_to_menu, "mnu_bank"),
		]),
    ("head_back",[],"Head back.",
       [
           (jump_to_menu,"mnu_bank"),
        ]),
]),

#SW - added swc_readme game menu
  (
    "swc_readme",menu_text_color(0xFF000d2c),
    "Star Wars: Conquest - FAQ & Notes^^This mod is still in development. We hope to eventually add more models, factions, quests, complete scene editing for all scenes, and add other functionality. Please post any bugs or suggestions on our forum.^^Content for this mod and future changes will primarily be focused on the original movies, Episode 4-6 range.  Clone Wars era troops and equipment have been included but are not planned to be further improved or a major feature of this mod.^^Scene editing is still in progress and we have made changes to many of the major planets like Tatooine, Yavin IV, Naboo, Geonosis, Ryloth, Kashyyyk, and Endor.  We are also working on creating several generic scenes to use for battlestations, outposts, and smaller planets. This is still a work in progress so not all scenes have been modified yet.^^The Trade Federation Base has several merchants like a Force-Sensitive Trainer, Clone Wars Era Merchant, Droid Parts Merchant, Plastic Surgeon, and others. Their inventory refreshes every hour and they can also randomly appear in the cantina's.^^Clone Troopers, B1-Series Battledroids, Baby Rancors, and Force-Sensitive troops can be recruited by building village upgrades.^^Space Battles can be found at the Training Academy.  Improving the controls or this functionality is a lower priority but may be reviewed in the future.^^Heavy Weapons (rocket launcher, flame rifle, etc) and some force powers (force kill, force knockdown, etc) are include for fun but are overpowered and will unbalance the game if you choose to use them.^^Currently some spaceships can be purchased and upgraded at the Trade Federation base and we plan to add more later.^^It is possible to get droids from Jawa prisoners but currently these droids do not do anything in battle.^^We could use help with this mod with models, textures, scene editing, and coding. Please post on our forum if you are interested in helping.^^Thanks very much to everybody who has directly or indirectly contributed to this mod, we all appreciate it.",
    "none",[],
    [("done",[],"Done.",[(change_screen_return),]),]
   ),

   
########################################################
## Easy regulars upgrading kit begin
########################################################
  ("ready_upgrade", menu_text_color(0xFF000d2c),
  "{s0}",
    "none", 
    [
      ## use reg10 to record wheather can continue or not
      ## use reg11 to record the progress of upgrading
      (try_begin),
        (party_get_num_companion_stacks, ":num_stacks", "p_main_party"),
        (eq, ":num_stacks", 1),
        (str_store_string, s0, "@ No one can upgrade."),
        (assign, reg10, 0),
      (else_try),
        (call_script, "script_calculate_upgrade_troops"),
        (try_begin),
          (troop_slot_eq, "trp_temp_array_a", 0, -1),
          (str_store_string, s0, "@ No one can upgrade."),
          (assign, reg10, 0),
        (else_try),
          (assign, reg10, 1),
          (assign, ":kinds_of_upgrade_troop", 0),
          (try_for_range, ":slot_id", 0, 32),
            (troop_get_slot, ":upgrade_troop", "trp_temp_array_a", ":slot_id"),
            (troop_get_slot, ":upgrade_size", "trp_temp_array_b", ":slot_id"),
            (gt, ":upgrade_troop", 0),
            (try_begin),
              (eq, ":kinds_of_upgrade_troop", 0),
              (str_store_troop_name_by_count, s1, ":upgrade_troop", ":upgrade_size"),
              (assign, reg1, ":upgrade_size"),
              (str_store_string, s0, "@{reg1} {s1} can upgrade."),
            (else_try),
              (eq, ":kinds_of_upgrade_troop", 1),
              (str_store_troop_name_by_count, s1, ":upgrade_troop", ":upgrade_size"),
              (assign, reg1, ":upgrade_size"),
              (str_store_string, s0, "@{reg1} {s1} and {s0}"),
            (else_try),
              (str_store_troop_name_by_count, s1, ":upgrade_troop", ":upgrade_size"),
              (assign, reg1, ":upgrade_size"),
              (str_store_string, s0, "@{reg1} {s1}, {s0}"),
            (try_end),
            (val_add, ":kinds_of_upgrade_troop", 1),
          (try_end),
        (try_end),
      (try_end),
    ],
    [
      ("go_back_dot", [(eq, reg10, 0)],
        "Go back.",
        [(jump_to_menu, "mnu_camp_action")]
      ),
      
      ("continue_3dot", [(eq, reg10, 1)],
        "Continue...",
        [
          (jump_to_menu, "mnu_camp_action"),
          (assign, reg11, 0),
          (start_presentation, "prsnt_upgrade_troops"),
        ]
      ),
    ]
  ),
########################################################
## Easy regulars upgrading kit end
########################################################
   
]

######### Quick Scene Chooser integration - http://forums.taleworlds.net/index.php/topic,51851.0.html

import header_scenes
from template_tools import *
from module_scenes import scenes

sorted_scenes = sorted(scenes)
for i in xrange(len(sorted_scenes)):
  current_scene = list(sorted_scenes[i])
  current_scene[1] = get_flags_from_bitmap(header_scenes, "sf_", current_scene[1])
  sorted_scenes[i] = tuple(current_scene)

choose_scene_template = Game_Menu_Template(
  id="choose_scenes_",
  text="Choose a scene: (Page {current_page} of {num_pages})",
  optn_id="choose_scene_",
  optn_text="{list_item[0]}{list_item[1]}",
  optn_consq = [
    (jump_to_scene, "scn_{list_item[0]}"),
    (change_screen_mission)
  ]
)

game_menus += choose_scene_template.generate_menus(sorted_scenes) 

###############################################################
