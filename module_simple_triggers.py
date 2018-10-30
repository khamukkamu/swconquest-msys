# S T A R   W A R S   C O N Q U E S T   M O D U L E   S Y S T E M 
# / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /
# By Taleworlds, HokieBT, MartinF and Swyter - Do not use/copy without permission

from header_common import *
from header_operations import *
from header_parties import *
from header_items import *
from header_skills import *
from header_triggers import *
from header_troops import *
from header_music import *

from module_constants import *

####################################################################################################################
# Simple triggers are the alternative to old style triggers. They do not preserve state, and thus simpler to maintain.
#
#  Each simple trigger contains the following fields:
# 1) Check interval: How frequently this trigger will be checked
# 2) Operation block: This must be a valid operation block. See header_operations.py for reference. 
####################################################################################################################



simple_triggers = [

# This trigger is deprecated. Use "script_game_event_party_encounter" in module_scripts.py instead  
  (ti_on_party_encounter,
   [
    ]),


# This trigger is deprecated. Use "script_game_event_simulate_battle" in module_scripts.py instead 
  (ti_simulate_battle,
   [
    ]),

  (1,
   [
      (gt,"$auto_besiege_town",0),
      (gt,"$g_player_besiege_town", 0),
      (ge, "$g_siege_method", 1),
      (store_current_hours, ":cur_hours"),
      (eq, "$g_siege_force_wait", 0),
      (ge, ":cur_hours", "$g_siege_method_finish_hours"),
      (neg|is_currently_night),
      (rest_for_hours, 0, 0, 0), #stop resting
    ]),

  (0,
   [
      (eq,"$g_player_is_captive",1),
      (gt, "$capturer_party", 0),
      (party_is_active, "$capturer_party"),
      (party_relocate_near_party, "p_main_party", "$capturer_party", 0),
    ]),

#Auto-menu
  (0,
   [
     (try_begin),
       (gt, "$g_last_rest_center", 0),
       (party_get_battle_opponent, ":besieger_party", "$g_last_rest_center"),
       (gt, ":besieger_party", 0),
       (store_faction_of_party, ":encountered_faction", "$g_last_rest_center"),
       (store_relation, ":faction_relation", ":encountered_faction", "fac_player_supporters_faction"),
       (store_faction_of_party, ":besieger_party_faction", ":besieger_party"),
       (store_relation, ":besieger_party_relation", ":besieger_party_faction", "fac_player_supporters_faction"),
       (ge, ":faction_relation", 0),
       (lt, ":besieger_party_relation", 0),
       (start_encounter, "$g_last_rest_center"),
       (rest_for_hours, 0, 0, 0), #stop resting
     (else_try),
       (store_current_hours, ":cur_hours"),
       (assign, ":check", 0),
       (try_begin),
         (neq, "$g_check_autos_at_hour", 0),
         (ge, ":cur_hours", "$g_check_autos_at_hour"),
         (assign, ":check", 1),
         (assign, "$g_check_autos_at_hour", 0),
       (try_end),
       (this_or_next|eq, ":check", 1),
       (map_free),
       (try_begin),
         (ge,"$auto_menu",1),
         (jump_to_menu,"$auto_menu"),
         (assign,"$auto_menu",-1),
       (else_try),
         (ge,"$auto_enter_town",1),
         (start_encounter, "$auto_enter_town"),
       (else_try),
         (ge,"$auto_besiege_town",1),
         (start_encounter, "$auto_besiege_town"),
       (else_try),
         (ge,"$g_camp_mode", 1),
         (assign, "$g_camp_mode", 0),
         (assign, "$g_player_icon_state", pis_normal),
         (display_message, "@Breaking camp..."),
       (try_end),
     (try_end),
     ]),


#Notification menus
  (0,
   [
     (troop_slot_ge, "trp_notification_menu_types", 0, 1),
     (troop_get_slot, ":menu_type", "trp_notification_menu_types", 0),
     (troop_get_slot, "$g_notification_menu_var1", "trp_notification_menu_var1", 0),
     (troop_get_slot, "$g_notification_menu_var2", "trp_notification_menu_var2", 0),
     (jump_to_menu, ":menu_type"),
     (assign, ":end_cond", 2),
     (try_for_range, ":cur_slot", 1, ":end_cond"),
       (try_begin),
         (troop_slot_ge, "trp_notification_menu_types", ":cur_slot", 1),
         (val_add, ":end_cond", 1),
       (try_end),
       (store_sub, ":cur_slot_minus_one", ":cur_slot", 1),
       (troop_get_slot, ":local_temp", "trp_notification_menu_types", ":cur_slot"),
       (troop_set_slot, "trp_notification_menu_types", ":cur_slot_minus_one", ":local_temp"),
       (troop_get_slot, ":local_temp", "trp_notification_menu_var1", ":cur_slot"),
       (troop_set_slot, "trp_notification_menu_var1", ":cur_slot_minus_one", ":local_temp"),
       (troop_get_slot, ":local_temp", "trp_notification_menu_var2", ":cur_slot"),
       (troop_set_slot, "trp_notification_menu_var2", ":cur_slot_minus_one", ":local_temp"),
     (try_end),
    ]),

  #Music,
  (1,
   [
       (map_free),
       (call_script, "script_music_set_situation_with_culture", mtf_sit_travel),
	   (call_script, "script_flush_gatesys_cache"),
   
	   #SW - trying to eliminate fog on the world map with the set_fog_distance command (doesn't seem to work)
	   #(set_fog_distance,100000000),
	   
	   ##SW - scene debug
	   #(party_get_slot, ":minorplanet_id", "p_minorplanet_66", slot_spacestation_exterior),
       #(assign, reg7, ":minorplanet_id"), #diagnostic only
       #(display_message, "@Village 66 = {reg7}"),#diagnostic only
    ]),
	
	#swy - swc 0.9.0.4 - set outpost icon depending of the faction - pretty cool and automated
   (35,
	[
	   #@> swy - set outpost icons depending of the faction - new map icons by Vector Dalon
	  (call_script, "script_swy_map_outpost_icon_routine","icon_outpost_imp","icon_outpost_reb","icon_outpost_hut"),
	  (call_script, "script_swy_map_outpost_icon_routine","icon_XQ_04_Station_3","icon_XQ_04_Station_2","icon_XQ_04_Station_5"),
	   #@> swy - set aura colors depending of the faction
	  (call_script, "script_swy_map_planet_aura_routine",mainplanets_begin,mainplanets_end),
	  (call_script, "script_swy_map_planet_aura_routine",minorplanet_begin,minorplanet_end),
	]),
	
# #SW - new music (doesn't work that well, stops playing after 5 seconds)
  # (0,
   # [
		# (map_free),
		# (try_begin),
			# (neq, "$g_music_mode", music_mode_map),
			# (display_message, "@DEBUG:  stop_all_sounds"),
			# (stop_all_sounds,2),
			# #(play_track, "track_stop", 2),
		# (try_end),
		# (assign, "$g_music_mode", music_mode_map),
		
		# #(store_random_in_range, ":random", 1, 7),
		# #(try_begin),
		# (play_track, "track_town_test", 2),
		# #(play_cue_track, "track_town_test"),
    # ]),



#Player raiding a village
# This trigger will check if player's raid has been completed and will lead control to village menu.
  (1,
   [
      (ge,"$g_player_raiding_village",1),
      (try_begin),
        (neq, "$g_player_is_captive", 0),
        (rest_for_hours, 0, 0, 0), #stop resting - abort
        (assign,"$g_player_raiding_village",0),
      (else_try),
        (map_free), #we have been attacked during raid
        (assign,"$g_player_raiding_village",0),
      (else_try),
        (this_or_next|party_slot_eq, "$g_player_raiding_village", slot_minorplanet_state, svs_looted),
        (party_slot_eq, "$g_player_raiding_village", slot_minorplanet_state, svs_deserted),
        (start_encounter, "$g_player_raiding_village"),
        (rest_for_hours, 0),
        (assign,"$g_player_raiding_village",0),
        (assign,"$g_player_raid_complete",1),
      (else_try),
        (party_slot_eq, "$g_player_raiding_village", slot_minorplanet_state, svs_being_raided),
        (rest_for_hours, 3, 5, 1), #rest while attackable
      (else_try),
        (rest_for_hours, 0, 0, 0), #stop resting - abort
        (assign,"$g_player_raiding_village",0),
        (assign,"$g_player_raid_complete",0),
      (try_end),
    ]),

#---------------------------------------------------------------------------------------
#SW - trying to switch each faction to have their own unique spaceship
# this didn't work correctly and was a bad idea, do it in "script_create_faction_hero_party" instead....
    # (0.1,
     # [
	# (assign,":faction_hero_no",0),
	# (try_for_range, ":faction_hero_no", "trp_knight_1_1", "trp_knight_1_20"),
	     # (party_set_icon, ":faction_hero_no", "icon_player"),
	# (try_end),
	# (try_for_range, ":faction_hero_no", "trp_knight_2_1", "trp_knight_2_20"),
	     # (party_set_icon, ":faction_hero_no", "icon_player"),
	# (try_end),
     # ]),	
	
#---------------------------------------------------------------------------------------
#Reload Player Character Cartridge Ammunition.
#TEST - temp remove reload ammo script
#SW - script to reload ammo (red and green laser bolts, added all others), from Winter and used in the Peasants are Revolting mod
    # (0.1,
     # [
	# (assign,":max_ammo_level",0),
        # (troop_get_inventory_capacity, ":inv_cap", "trp_player"),
        # (try_for_range, ":i_slot", 0, ":inv_cap"),
        # (troop_get_inventory_slot, ":item_id", "trp_player", ":i_slot"),
        # (eq, ":item_id", "itm_laser_bolts_green"),
        # (troop_inventory_slot_get_item_amount,":ammo_level","trp_player",":i_slot"),
        # (troop_inventory_slot_get_item_max_amount,":max_ammo_level","trp_player",":i_slot"),
        # (lt,":ammo_level",":max_ammo_level"),
        # (troop_inventory_slot_set_item_amount,"trp_player",":i_slot",":max_ammo_level"),
        # (try_end),
     # ]),
    # (0.1,
     # [
	# (assign,":max_ammo_level",0),
        # (troop_get_inventory_capacity, ":inv_cap", "trp_player"),
        # (try_for_range, ":i_slot", 0, ":inv_cap"),
        # (troop_get_inventory_slot, ":item_id", "trp_player", ":i_slot"),
        # (eq, ":item_id", "itm_laser_bolts_orange"),
        # (troop_inventory_slot_get_item_amount,":ammo_level","trp_player",":i_slot"),
        # (troop_inventory_slot_get_item_max_amount,":max_ammo_level","trp_player",":i_slot"),
        # (lt,":ammo_level",":max_ammo_level"),
        # (troop_inventory_slot_set_item_amount,"trp_player",":i_slot",":max_ammo_level"),
        # (try_end),
     # ]),	 
    # (0.1,
     # [
	# (assign,":max_ammo_level",0),
        # (troop_get_inventory_capacity, ":inv_cap", "trp_player"),
        # (try_for_range, ":i_slot", 0, ":inv_cap"),
        # (troop_get_inventory_slot, ":item_id", "trp_player", ":i_slot"),
        # (eq, ":item_id", "itm_laser_bolts_red"),
        # (troop_inventory_slot_get_item_amount,":ammo_level","trp_player",":i_slot"),
        # (troop_inventory_slot_get_item_max_amount,":max_ammo_level","trp_player",":i_slot"),
        # (lt,":ammo_level",":max_ammo_level"),
        # (troop_inventory_slot_set_item_amount,"trp_player",":i_slot",":max_ammo_level"),
        # (try_end),
     # ]),
    # (0.1,
     # [
	# (assign,":max_ammo_level",0),
        # (troop_get_inventory_capacity, ":inv_cap", "trp_player"),
        # (try_for_range, ":i_slot", 0, ":inv_cap"),
        # (troop_get_inventory_slot, ":item_id", "trp_player", ":i_slot"),
        # (eq, ":item_id", "itm_stun_beam"),
        # (troop_inventory_slot_get_item_amount,":ammo_level","trp_player",":i_slot"),
        # (troop_inventory_slot_get_item_max_amount,":max_ammo_level","trp_player",":i_slot"),
        # (lt,":ammo_level",":max_ammo_level"),
        # (troop_inventory_slot_set_item_amount,"trp_player",":i_slot",":max_ammo_level"),
        # (try_end),
     # ]),	 
    # (0.1,
     # [
	# (assign,":max_ammo_level",0),
        # (troop_get_inventory_capacity, ":inv_cap", "trp_player"),
        # (try_for_range, ":i_slot", 0, ":inv_cap"),
        # (troop_get_inventory_slot, ":item_id", "trp_player", ":i_slot"),
        # (eq, ":item_id", "itm_laser_bolts_yellow"),
        # (troop_inventory_slot_get_item_amount,":ammo_level","trp_player",":i_slot"),
        # (troop_inventory_slot_get_item_max_amount,":max_ammo_level","trp_player",":i_slot"),
        # (lt,":ammo_level",":max_ammo_level"),
        # (troop_inventory_slot_set_item_amount,"trp_player",":i_slot",":max_ammo_level"),
        # (try_end),
     # ]),	 
    # (0.1,
     # [
	# (assign,":max_ammo_level",0),
        # (troop_get_inventory_capacity, ":inv_cap", "trp_player"),
        # (try_for_range, ":i_slot", 0, ":inv_cap"),
        # (troop_get_inventory_slot, ":item_id", "trp_player", ":i_slot"),
        # (eq, ":item_id", "itm_laser_bolts_blue"),
        # (troop_inventory_slot_get_item_amount,":ammo_level","trp_player",":i_slot"),
        # (troop_inventory_slot_get_item_max_amount,":max_ammo_level","trp_player",":i_slot"),
        # (lt,":ammo_level",":max_ammo_level"),
        # (troop_inventory_slot_set_item_amount,"trp_player",":i_slot",":max_ammo_level"),
        # (try_end),
     # ]),	 
    # (0.1,
     # [
	# (assign,":max_ammo_level",0),
        # (troop_get_inventory_capacity, ":inv_cap", "trp_player"),
        # (try_for_range, ":i_slot", 0, ":inv_cap"),
        # (troop_get_inventory_slot, ":item_id", "trp_player", ":i_slot"),
        # (eq, ":item_id", "itm_ion_beam"),
        # (troop_inventory_slot_get_item_amount,":ammo_level","trp_player",":i_slot"),
        # (troop_inventory_slot_get_item_max_amount,":max_ammo_level","trp_player",":i_slot"),
        # (lt,":ammo_level",":max_ammo_level"),
        # (troop_inventory_slot_set_item_amount,"trp_player",":i_slot",":max_ammo_level"),
        # (try_end),
     # ]),	 	 
#SW - end of reload ammo
#---------------------------------------------------------------------------------------

  #Pay day.
  (24 * 7,
   [
     (call_script, "script_calculate_player_faction_wage"),
     (assign, ":total_wages", reg0),
     (store_add, ":total_debt", ":total_wages", "$g_player_debt_to_party_members"),
     (try_begin),
       (gt, ":total_debt", 0),
       (jump_to_menu,"mnu_pay_day"),
     (try_end),
     (assign, "$g_cur_week_half_daily_wage_payments", 0),#Reseting the weekly half wage payments
    ]),

  #Mercenary Pay day.
  (6,
   [
     (store_current_hours, ":cur_hours"),
     (try_begin),
       (ge, ":cur_hours", "$mercenary_service_next_pay_time"),
       (call_script, "script_party_calculate_strength", "p_main_party", 0),
       (assign, ":offer_value", reg0),
       (val_div, ":offer_value", 2),
       (val_add, ":offer_value", 30),
       (call_script, "script_round_value", ":offer_value"),
       (val_add, "$mercenary_service_accumulated_pay", reg0),
       (store_add, "$mercenary_service_next_pay_time", ":cur_hours", 7 * 24),
     (try_end),
    ]),
  
  # Oath fulfilled?
  (24,
   [
      (le, "$auto_menu", 0),
      (gt, "$players_faction", 0),
      (neq, "$players_faction", "fac_player_supporters_faction"),
      (eq, "$player_has_homage", 0),
      (store_current_day, ":cur_day"),
      (gt, ":cur_day", "$mercenary_service_next_renew_day"),
      (jump_to_menu, "mnu_oath_fulfilled"),
    ]),

  # Reducing luck by 1 in every 180 hours
  (180,
   [
     (val_sub, "$g_player_luck", 1),
     (val_max, "$g_player_luck", 0),
    ]),

  # Banner selection menu
  (24,
   [
    (eq, "$g_player_banner_granted", 1),
    (troop_slot_eq, "trp_player", slot_troop_banner_scene_prop, 0),
    (le,"$auto_menu",0),
#normal_banner_begin
    (start_presentation, "prsnt_banner_selection"),
#custom_banner_begin
#    (start_presentation, "prsnt_custom_banner"),
    ]),

  # Party Morale: Move morale towards target value.
  (24,
   [
      (call_script, "script_get_player_party_morale_values"),
      (assign, ":target_morale", reg0),
      (party_get_morale, ":cur_morale", "p_main_party"),
      (store_sub, ":dif", ":target_morale", ":cur_morale"),
      (store_div, ":dif_to_add", ":dif", 5),
      (store_mul, ":dif_to_add_correction", ":dif_to_add", 5),
      (try_begin),#finding ceiling of the value
        (neq, ":dif_to_add_correction", ":dif"),
        (try_begin),
          (gt, ":dif", 0),
          (val_add, ":dif_to_add", 1),
        (else_try),
          (val_sub, ":dif_to_add", 1),
        (try_end),
      (try_end),
      (val_add, ":cur_morale", ":dif_to_add"),
      (party_set_morale, "p_main_party", ":cur_morale"),
    ]),
  

#Party AI: pruning some of the prisoners in each center (once a week)
  (24*7,
   [
       (try_for_range, ":center_no", centers_begin, centers_end),
         (party_get_num_prisoner_stacks, ":num_prisoner_stacks",":center_no"),
         (try_for_range_backwards, ":stack_no", 0, ":num_prisoner_stacks"),
           (party_prisoner_stack_get_troop_id, ":stack_troop",":center_no",":stack_no"),
           (neg|troop_is_hero, ":stack_troop"),
           (party_prisoner_stack_get_size, ":stack_size",":center_no",":stack_no"),
           (store_random_in_range, ":rand_no", 0, 40),
           (val_mul, ":stack_size", ":rand_no"),
           (val_div, ":stack_size", 100),
           (party_remove_prisoners, ":center_no", ":stack_troop", ":stack_size"),
         (try_end),
       (try_end),
    ]),


#SW - added safety code to run script_fix_town_walkers incase they were messed up
  (24*7,
   [	
		(try_for_range, ":center_no", walled_centers_begin, walled_centers_end),
			(call_script, "script_fix_town_walkers", ":center_no"),
		(try_end),	
	]),
	
  #Adding net incomes to heroes (once a week)
  #Increasing debts to heroes by 1% (once a week)
  #Adding net incomes to centers (once a week)
  (24*7,
   [
       (try_for_range, ":troop_no", faction_heroes_begin, faction_heroes_end),
         (troop_get_slot, ":cur_debt", ":troop_no", slot_troop_player_debt),#Increasing debt
         (val_mul, ":cur_debt", 101),
         (val_div, ":cur_debt", 100),
         (troop_set_slot, ":troop_no", slot_troop_player_debt, ":cur_debt"),
         (call_script, "script_calculate_hero_weekly_net_income_and_add_to_wealth", ":troop_no"),#Adding net income
       (try_end),
       (try_for_range, ":center_no", walled_centers_begin, walled_centers_end),
         #If non-player center, adding income to wealth
         (neg|party_slot_eq, ":center_no", slot_mainplanet_lord, "trp_player"), #center does not belong to player.
         (party_slot_ge, ":center_no", slot_mainplanet_lord, 1), #center belongs to someone.
         (party_get_slot, ":cur_wealth", ":center_no", slot_mainplanet_wealth),
         (party_get_slot, ":prosperity", ":center_no", slot_mainplanet_prosperity),
         (store_mul, ":added_wealth", ":prosperity", 15),
         (val_add, ":added_wealth", 700),
         (try_begin),
           (party_slot_eq, ":center_no", slot_party_type, spt_mainplanet),
           (val_mul, ":added_wealth", 3),
           (val_div, ":added_wealth", 2),
         (try_end),
         (val_add, ":cur_wealth", ":added_wealth"),
         (call_script, "script_calculate_weekly_party_wage", ":center_no"),
         (val_sub, ":cur_wealth", reg0),
         (val_max, ":cur_wealth", 0),
         (party_set_slot, ":center_no", slot_mainplanet_wealth, ":cur_wealth"),
       (try_end),
    ]),

  #Hiring men with hero wealths (once a day)
  #Hiring men with center wealths (once a day)
  (24,
   [
       (try_for_range, ":troop_no", faction_heroes_begin, faction_heroes_end),
         (troop_get_slot, ":party_no", ":troop_no", slot_troop_leaded_party),
         (ge, ":party_no", 1),
         (party_get_attached_to, ":cur_attached_party", ":party_no"),
         (is_between, ":cur_attached_party", centers_begin, centers_end),
         (party_slot_eq, ":cur_attached_party", slot_center_is_besieged_by, -1), #center not under siege
         (call_script, "script_hire_men_to_faction_hero_party", ":troop_no"), #Hiring men with current wealth
       (try_end),
       (try_for_range, ":center_no", walled_centers_begin, walled_centers_end),
         (neg|party_slot_eq, ":center_no", slot_mainplanet_lord, "trp_player"), #center does not belong to player.
         (party_slot_ge, ":center_no", slot_mainplanet_lord, 1), #center belongs to someone.
         (party_get_slot, ":cur_wealth", ":center_no", slot_mainplanet_wealth),
         (party_slot_eq, ":center_no", slot_center_is_besieged_by, -1), #center not under siege
         (assign, ":hiring_budget", ":cur_wealth"),
         (val_div, ":hiring_budget", 5),
         (gt, ":hiring_budget", reinforcement_cost),
         (call_script, "script_cf_reinforce_party", ":center_no"),
         (val_sub, ":cur_wealth", reinforcement_cost),
         (party_set_slot, ":center_no", slot_mainplanet_wealth, ":cur_wealth"),
       (try_end),
    ]),

  #Converging center prosperity to ideal prosperity once in every 15 days
  (24*15,
   [(try_for_range, ":center_no", centers_begin, centers_end),
      (call_script, "script_get_center_ideal_prosperity", ":center_no"),
      (assign, ":ideal_prosperity", reg0),
      (party_get_slot, ":prosperity", ":center_no", slot_mainplanet_prosperity),
      (try_begin),
        (gt, ":prosperity", ":ideal_prosperity"),
        (call_script, "script_change_center_prosperity", ":center_no", -1),
      (else_try),
        (lt, ":prosperity", ":ideal_prosperity"),
        (call_script, "script_change_center_prosperity", ":center_no", 1),
      (try_end),
    (try_end),
    ]),

  #Checking if the troops are resting at a half payment point
  (6,
   [(store_current_day, ":cur_day"),
    (try_begin),
      (neq, ":cur_day", "$g_last_half_payment_check_day"),
      (assign, "$g_last_half_payment_check_day", ":cur_day"),
      (try_begin),
        (eq, "$g_half_payment_checkpoint", 1),
        (val_add, "$g_cur_week_half_daily_wage_payments", 1), #half payment for yesterday
      (try_end),
      (assign, "$g_half_payment_checkpoint", 1),
    (try_end),
    (assign, ":resting_at_manor_or_walled_center", 0),
    (try_begin),
      (neg|map_free),
      (ge, "$g_last_rest_center", 0),
      (this_or_next|party_slot_eq, "$g_last_rest_center", slot_center_has_manor, 1),
      (is_between, "$g_last_rest_center", walled_centers_begin, walled_centers_end),
      (assign, ":resting_at_manor_or_walled_center", 1),
    (try_end),
    (eq, ":resting_at_manor_or_walled_center", 0),
    (assign, "$g_half_payment_checkpoint", 0),
    ]),


  # Give some xp to hero parties
   (48,
   [
       (try_for_range, ":troop_no", faction_heroes_begin, faction_heroes_end),
         (store_random_in_range, ":rand", 0, 100),
         (lt, ":rand", 30),
         (troop_get_slot, ":hero_party", ":troop_no", slot_troop_leaded_party),
         (gt, ":hero_party", centers_end),
         (party_is_active, ":hero_party"),
         (store_skill_level, ":trainer_level", skl_trainer, ":troop_no"),
         (val_add, ":trainer_level", 2),
         (store_mul, ":xp_gain", ":trainer_level", 500),
         (party_upgrade_with_xp, ":hero_party", ":xp_gain"),
       (try_end),
       
       (try_for_range, ":center_no", walled_centers_begin, walled_centers_end),
         (store_random_in_range, ":rand", 0, 100),
         (lt, ":rand", 10),
         (party_get_slot, ":center_lord", ":center_no", slot_mainplanet_lord),
         (neq, ":center_lord", "trp_player"),
         (party_upgrade_with_xp, ":center_no", 3000),
       (try_end),
    ]),

  # Process sieges
   (24,
   [
       (call_script, "script_process_sieges"),
    ]),

  # Process village raids
   (2,
   [
       (call_script, "script_process_minorplanet_raids"),
    ]),


  # Decide vassal ai
   (7,
    [
      (call_script, "script_init_ai_calculation"),
      (call_script, "script_decide_faction_party_ais"),
      ]),

  # Hold regular marshall elections for players_faction
   (24,
    [
      (val_add, "$g_election_date", 1),
      (ge, "$g_election_date", 90),
      (is_between, "$players_faction", factions_begin, factions_end),
      (neq, "$players_faction", "fac_player_supporters_faction"),
      (assign, "$g_presentation_input", -1),
      (assign, "$g_presentation_marshall_selection_1_vote", 0),
      (assign, "$g_presentation_marshall_selection_2_vote", 0),

      (assign, "$g_presentation_marshall_selection_max_renown_1", -10000),
      (assign, "$g_presentation_marshall_selection_max_renown_2", -10000),
      (assign, "$g_presentation_marshall_selection_max_renown_3", -10000),
      (assign, "$g_presentation_marshall_selection_max_renown_1_troop", -10000),
      (assign, "$g_presentation_marshall_selection_max_renown_2_troop", -10000),
      (assign, "$g_presentation_marshall_selection_max_renown_3_troop", -10000),
      (assign, ":num_men", 0),
      (try_for_range, ":loop_var", "trp_faction_heroes_including_player_begin", faction_heroes_end),
        (assign, ":cur_troop", ":loop_var"),
        (assign, ":continue", 0),
        (try_begin),
          (eq, ":loop_var", "trp_faction_heroes_including_player_begin"),
          (assign, ":cur_troop", "trp_player"),
          (try_begin),
            (eq, "$g_player_is_captive", 0),
            (assign, ":continue", 1),
          (try_end),
        (else_try),
          (store_troop_faction, ":cur_troop_faction", ":cur_troop"),
          (eq, "$players_faction", ":cur_troop_faction"),
          #(troop_slot_eq, ":cur_troop", slot_troop_is_prisoner, 0),
          (neg|troop_slot_ge, ":cur_troop", slot_troop_prisoner_of_party, 0),
          (troop_slot_ge, ":cur_troop", slot_troop_leaded_party, 1),
          (troop_slot_eq, ":cur_troop", slot_troop_occupation, slto_faction_hero),
          (neg|faction_slot_eq, ":cur_troop_faction", slot_faction_leader, ":cur_troop"),
          (troop_get_slot, ":cur_party", ":cur_troop", slot_troop_leaded_party),
          (gt, ":cur_party", 0),
          (party_is_active, ":cur_party"),
          (call_script, "script_party_count_fit_for_battle", ":cur_party"),
          (assign, ":party_fit_for_battle", reg0),
          (call_script, "script_party_get_ideal_size", ":cur_party"),
          (assign, ":ideal_size", reg0),
          (store_mul, ":relative_strength", ":party_fit_for_battle", 100),
          (val_div, ":relative_strength", ":ideal_size"),
          (ge, ":relative_strength", 25),
          (assign, ":continue", 1),
        (try_end),
        (eq, ":continue", 1),
        (val_add, ":num_men", 1),
        (troop_get_slot, ":renown", ":cur_troop", slot_troop_renown),
        (try_begin),
          (gt, ":renown", "$g_presentation_marshall_selection_max_renown_1"),
          (assign, "$g_presentation_marshall_selection_max_renown_3", "$g_presentation_marshall_selection_max_renown_2"),
          (assign, "$g_presentation_marshall_selection_max_renown_2", "$g_presentation_marshall_selection_max_renown_1"),
          (assign, "$g_presentation_marshall_selection_max_renown_1", ":renown"),
          (assign, "$g_presentation_marshall_selection_max_renown_3_troop", "$g_presentation_marshall_selection_max_renown_2_troop"),
          (assign, "$g_presentation_marshall_selection_max_renown_2_troop", "$g_presentation_marshall_selection_max_renown_1_troop"),
          (assign, "$g_presentation_marshall_selection_max_renown_1_troop", ":cur_troop"),
        (else_try),
          (gt, ":renown", "$g_presentation_marshall_selection_max_renown_2"),
          (assign, "$g_presentation_marshall_selection_max_renown_3", "$g_presentation_marshall_selection_max_renown_2"),
          (assign, "$g_presentation_marshall_selection_max_renown_2", ":renown"),
          (assign, "$g_presentation_marshall_selection_max_renown_3_troop", "$g_presentation_marshall_selection_max_renown_2_troop"),
          (assign, "$g_presentation_marshall_selection_max_renown_2_troop", ":cur_troop"),
        (else_try),
          (gt, ":renown", "$g_presentation_marshall_selection_max_renown_3"),
          (assign, "$g_presentation_marshall_selection_max_renown_3", ":renown"),
          (assign, "$g_presentation_marshall_selection_max_renown_3_troop", ":cur_troop"),
        (try_end),
      (try_end),
      (ge, "$g_presentation_marshall_selection_max_renown_1_troop", 0),
      (ge, "$g_presentation_marshall_selection_max_renown_2_troop", 0),
      (ge, "$g_presentation_marshall_selection_max_renown_3_troop", 0),
      (gt, ":num_men", 2), #at least 1 voter
      (assign, "$g_election_date", 0),
      (assign, "$g_presentation_marshall_selection_ended", 0),
      (try_begin),
        (neq, "$g_presentation_marshall_selection_max_renown_1_troop", "trp_player"),
        (neq, "$g_presentation_marshall_selection_max_renown_2_troop", "trp_player"),
        (start_presentation, "prsnt_marshall_selection"),
      (else_try),
        (jump_to_menu, "mnu_marshall_selection_candidate_ask"),
      (try_end),
      ]),

  # Changing readiness to join army
   (10,
    [
      (try_for_range, ":troop_no", faction_heroes_begin, faction_heroes_end),
        (assign, ":modifier", 1),
        (troop_get_slot, ":party_no", ":troop_no", slot_troop_leaded_party),
        (try_begin),
          (gt, ":party_no", 0),
          (party_get_slot, ":commander_party", ":party_no", slot_party_commander_party),
          (ge, ":commander_party", 0),
          (store_faction_of_party, ":faction_no", ":party_no"),
          (faction_get_slot, ":faction_marshall", ":faction_no", slot_faction_marshall),
          (ge, ":faction_marshall", 0),
          (troop_get_slot, ":marshall_party", ":faction_marshall", slot_troop_leaded_party),
          (eq, ":commander_party", ":marshall_party"),
          (assign, ":modifier", -1),
        (try_end),
        (troop_get_slot, ":readiness", ":troop_no", slot_troop_readiness_to_join_army),
        (val_add, ":readiness", ":modifier"),
        (val_clamp, ":readiness", 0, 100),
        (troop_set_slot, ":troop_no", slot_troop_readiness_to_join_army, ":readiness"),
        (assign, ":modifier", 1),
        (try_begin),
          (gt, ":party_no", 0),
          (store_troop_faction, ":troop_faction", ":troop_no"),
          (eq, ":troop_faction", "fac_player_supporters_faction"),
          (neg|troop_slot_eq, ":troop_no", slot_troop_player_order_state, spai_undefined),
          (party_get_slot, ":party_ai_state", ":party_no", slot_party_ai_state),
          (party_get_slot, ":party_ai_object", ":party_no", slot_party_ai_object),
          #Check if party is following player orders
          (try_begin),
            (troop_slot_eq, ":troop_no", slot_troop_player_order_state, ":party_ai_state"),
            (troop_slot_eq, ":troop_no", slot_troop_player_order_object, ":party_ai_object"),
            (assign, ":modifier", -1),
          (else_try),
            #Leaving following player orders if the current party order is not the same.
            (troop_set_slot, ":troop_no", slot_troop_player_order_state, spai_undefined),
            (troop_set_slot, ":troop_no", slot_troop_player_order_object, -1),
          (try_end),
        (try_end),
        (troop_get_slot, ":readiness", ":troop_no", slot_troop_readiness_to_follow_orders),
        (val_add, ":readiness", ":modifier"),
        (val_clamp, ":readiness", 0, 100),
        (troop_set_slot, ":troop_no", slot_troop_readiness_to_follow_orders, ":readiness"),
        (try_begin),
          (lt, ":readiness", 10),
          (troop_set_slot, ":troop_no", slot_troop_player_order_state, spai_undefined),
          (troop_set_slot, ":troop_no", slot_troop_player_order_object, -1),
        (try_end),
      (try_end),
      ]),
  
  # Process vassal ai
   (2,
   [
       (call_script, "script_process_faction_parties_ai"),
    ]),

  # Process alarms
   (3,
   [
       (call_script, "script_process_alarms"),
    ]),

  # Process siege ai
   (3,
   [
        (store_current_hours, ":cur_hours"),
        (store_random_in_range, ":center_no", walled_centers_begin, walled_centers_end),
        (party_get_slot, ":besieger_party", ":center_no", slot_center_is_besieged_by),
        (gt, ":besieger_party", 0),
        (party_is_active, ":besieger_party"),
        (store_faction_of_party, ":besieger_faction", ":besieger_party"),
        (party_slot_ge, ":center_no", slot_center_is_besieged_by, 1),
        (party_get_slot, ":siege_begin_hours", ":center_no", slot_center_siege_begin_hours),
        (store_sub, ":siege_begin_hours", ":cur_hours", ":siege_begin_hours"),
        (assign, ":launch_attack", 0),
        (assign, ":call_attack_back", 0),
        (assign, ":attacker_strength", 0),
        (assign, ":marshall_attacking", 0),
        (try_for_range, ":troop_no", faction_heroes_begin, faction_heroes_end),
          (troop_slot_eq, ":troop_no", slot_troop_occupation, slto_faction_hero),
          #(troop_slot_eq, ":troop_no", slot_troop_is_prisoner, 0),
          (neg|troop_slot_ge, ":troop_no", slot_troop_prisoner_of_party, 0),
          (troop_get_slot, ":party_no", ":troop_no", slot_troop_leaded_party),
          (gt, ":party_no", 0),
          (party_is_active, ":party_no"),
          
          (store_troop_faction, ":troop_faction_no", ":troop_no"),
          (eq, ":troop_faction_no", ":besieger_faction"),
          (assign, ":continue", 0),
          (try_begin),
            (party_slot_eq, ":party_no", slot_party_ai_state, spai_besieging_center),
            (party_slot_eq, ":party_no", slot_party_ai_object, ":center_no"),
            (assign, ":continue", 1),
          (else_try),
            (party_slot_eq, ":party_no", slot_party_ai_state, spai_accompanying_army),
            (party_get_slot, ":commander_party", ":party_no", slot_party_ai_object),
            (gt, ":commander_party", 0),
            (party_is_active, ":commander_party"),
            (party_slot_eq, ":commander_party", slot_party_ai_state, spai_besieging_center),
            (party_slot_eq, ":commander_party", slot_party_ai_object, ":center_no"),
            (assign, ":continue", 1),
          (try_end),
          (eq, ":continue", 1),
          (party_get_battle_opponent, ":opponent", ":party_no"),
          (this_or_next|lt, ":opponent", 0),
          (eq, ":opponent", ":center_no"),
          (try_begin),
            (faction_slot_eq, ":besieger_faction", slot_faction_marshall, ":troop_no"),
            (assign, ":marshall_attacking", 1),
          (try_end),
          (call_script, "script_party_calculate_regular_strength", ":party_no"),
          (val_add, ":attacker_strength", reg0),
        (try_end),
        (try_begin),
          (gt, ":attacker_strength", 0),
          (party_collect_attachments_to_party, ":center_no", "p_collective_enemy"),
          (call_script, "script_party_calculate_regular_strength", "p_collective_enemy"),
          (assign, ":defender_strength", reg0),
          (try_begin),
            (eq, "$auto_enter_town", ":center_no"),
            (eq, "$g_player_is_captive", 0),
            (call_script, "script_party_calculate_regular_strength", "p_main_party"),
            (val_add, ":defender_strength", reg0),
            (val_mul, ":attacker_strength", 2), #double the power of attackers if the player is in the campaign
          (try_end),
          (party_get_slot, ":siege_hardness", ":center_no", slot_center_siege_hardness),
          (val_add, ":siege_hardness", 100),
          (val_mul, ":defender_strength", ":siege_hardness"),
          (val_div, ":defender_strength", 100),
          (val_max, ":defender_strength", 1),
          (try_begin),
            (eq, ":marshall_attacking", 1),
            (eq, ":besieger_faction", "$players_faction"),
            (check_quest_active, "qst_follow_army"),
            (val_mul, ":attacker_strength", 2), #double the power of attackers if the player is in the campaign
          (try_end),
          (store_mul, ":strength_ratio", ":attacker_strength", 100),
          (val_div, ":strength_ratio", ":defender_strength"),
          (store_sub, ":random_up_limit", ":strength_ratio", 250), #was 300 (1.126)
          
          (try_begin),
            (gt, ":random_up_limit", -100), #never attack if the strength ratio is less than 150%
            (store_div, ":siege_begin_hours_effect", ":siege_begin_hours", 2), #was 3 (1.126)
            (val_add, ":random_up_limit", ":siege_begin_hours_effect"),
          (try_end),
          (val_div, ":random_up_limit", 5),
          (val_max, ":random_up_limit", 0),
          (store_sub, ":random_down_limit", 175, ":strength_ratio"), #was 200 (1.126)
          (val_max, ":random_down_limit", 0),
          (try_begin),
            (store_random_in_range, ":rand", 0, 100),
            (lt, ":rand", ":random_up_limit"),
            (gt, ":siege_begin_hours", 24),#initial preparation
            (assign, ":launch_attack", 1),
          (else_try),
            (store_random_in_range, ":rand", 0, 100),
            (lt, ":rand", ":random_down_limit"),
            (assign, ":call_attack_back", 1),
          (try_end),
        (else_try),
          (assign, ":call_attack_back", 1),
        (try_end),
        
        #Assault the fortress
        (try_begin),
          (eq, ":launch_attack", 1),
          (call_script, "script_begin_assault_on_center", ":center_no"),
        (else_try),
          (eq, ":call_attack_back", 1),
          (try_for_range, ":troop_no", faction_heroes_begin, faction_heroes_end),
            (troop_slot_eq, ":troop_no", slot_troop_occupation, slto_faction_hero),
            #(troop_slot_eq, ":troop_no", slot_troop_is_prisoner, 0),
            (neg|troop_slot_ge, ":troop_no", slot_troop_prisoner_of_party, 0),
            (troop_get_slot, ":party_no", ":troop_no", slot_troop_leaded_party),
            (gt, ":party_no", 0),
            (party_is_active, ":party_no"),
            
            (party_slot_eq, ":party_no", slot_party_ai_state, spai_besieging_center),
            (party_slot_eq, ":party_no", slot_party_ai_object, ":center_no"),
            (party_slot_eq, ":party_no", slot_party_ai_substate, 1),
            (call_script, "script_party_set_ai_state", ":party_no", spai_undefined, -1),
            (call_script, "script_party_set_ai_state", ":party_no", spai_besieging_center, ":center_no"),
            #resetting siege begin time if at least 1 party retreats
            (party_set_slot, ":center_no", slot_center_siege_begin_hours, ":cur_hours"),
          (try_end),
        (try_end),
        # (try_end),
    ]),

  # Decide faction ai
   (36,
   [
       (assign, "$g_recalculate_ais", 1),
    ]),
    
  # Decide faction ai flag check
   (0,
   [
	 (eq, "$g_recalculate_ais", 1),
	 (assign, "$g_recalculate_ais", 0),
	 (call_script, "script_recalculate_ais"),
    ]),
  
  # Count faction armies
   (24,
   [
       (try_for_range, ":faction_no", factions_begin, factions_end),
         (call_script, "script_faction_recalculate_strength", ":faction_no"),
       (try_end),
    ]),

  # Reset hero quest status
  # Change hero relation
   (36,
   [
     (try_for_range, ":troop_no", heroes_begin, heroes_end),
       (troop_set_slot, ":troop_no", slot_troop_does_not_give_quest, 0),
     (try_end),
     
     (try_for_range, ":troop_no", planet_admins_begin, planet_admins_end),
       (troop_set_slot, ":troop_no", slot_troop_does_not_give_quest, 0),
     (try_end),
    ]),

  # Refresh merchant inventories
   (24,
   [
      (try_for_range, ":minorplanet_no", minorplanet_begin, minorplanet_end),
        (call_script, "script_refresh_minorplanet_merchant_inventory", ":minorplanet_no"),
      (try_end),
    ]),

  #Refreshing village defenders
  #Clearing slot_minorplanet_player_can_not_steal_cattle flags
   (48,
   [
      (try_for_range, ":minorplanet_no", minorplanet_begin, minorplanet_end),
        (call_script, "script_refresh_minorplanet_defenders", ":minorplanet_no"),
        (party_set_slot, ":minorplanet_no", slot_minorplanet_player_can_not_steal_cattle, 0),
      (try_end),
    ]),

  # Refresh number of cattle in villages
  (24,
   [(try_for_range, ":minorplanet_no", minorplanet_begin, minorplanet_end),
      (party_get_slot, ":num_cattle", ":minorplanet_no", slot_minorplanet_number_of_cattle),
      (store_random_in_range, ":random_no", 0, 100),
      (try_begin),
        (lt, ":random_no", 3),#famine
        (assign, ":num_cattle", 0),
        (try_begin),
#          (eq, "$cheat_mode", 1),
#          (str_store_party_name, s1, ":minorplanet_no"),
#          (display_message, "@Cattle in {s1} are exterminated due to famine."),
        (try_end),
      (else_try),
        (lt, ":random_no", 10),#double growth
        (store_random_in_range, ":random_no", 111, 121),
        (val_mul, ":num_cattle", ":random_no"),
        (val_div, ":num_cattle", 100),
        (store_random_in_range, ":random_no", 1, 3),
        (val_add, ":num_cattle", ":random_no"),
      (else_try),
        #SW - modified cattle/nerfs to not have as much negative growth
        #(lt, ":random_no", 50),#negative growth
        #(store_random_in_range, ":random_no", 3, 8),
        (lt, ":random_no", 30),#negative growth
        (store_random_in_range, ":random_no", 2, 4),        
        (val_sub, ":num_cattle", ":random_no"),
      (else_try),#positive growth
        (store_random_in_range, ":random_no", 101, 111),
        (val_mul, ":num_cattle", ":random_no"),
        (val_div, ":num_cattle", 100),
        (store_random_in_range, ":random_no", 1, 3),
        (val_add, ":num_cattle", ":random_no"),
      (try_end),
      (val_clamp, ":num_cattle", 0, 101),
      (party_set_slot, ":minorplanet_no", slot_minorplanet_number_of_cattle, ":num_cattle"),
      #Reassigning the cattle production in the village
      (store_sub, ":production", ":num_cattle", 10),
      (val_div, ":production", 2),
      (call_script, "script_center_change_trade_good_production", ":minorplanet_no", "itm_cattle_meat", ":production", 0),
    (try_end),
    ]),

  # Accumulate taxes
   (24 * 7,
   [
      (try_for_range, ":center_no", centers_begin, centers_end),
        (party_get_slot, ":accumulated_rents", ":center_no", slot_center_accumulated_rents),
        (assign, ":cur_rents", 0),
        (try_begin),
          (party_slot_eq, ":center_no", slot_party_type, spt_minorplanet),
          (try_begin),
            (party_slot_eq, ":center_no", slot_minorplanet_state, svs_normal),
            (assign, ":cur_rents", 500),
          (try_end),
        (else_try),
          (party_slot_eq, ":center_no", slot_party_type, spt_castle),
          (assign, ":cur_rents", 250),
        (else_try),
          (party_slot_eq, ":center_no", slot_party_type, spt_mainplanet),
          (assign, ":cur_rents", 1000),
        (try_end),
        (party_get_slot, ":prosperity", ":center_no", slot_mainplanet_prosperity),
        (store_add, ":multiplier", 10, ":prosperity"),
        (val_mul, ":cur_rents", ":multiplier"),
        (val_div, ":cur_rents", 110),#Prosperity of 100 gives the default values
        (val_add, ":accumulated_rents", ":cur_rents"),
        (party_set_slot, ":center_no", slot_center_accumulated_rents, ":accumulated_rents"),
      (try_end),

      #Adding earnings to town lords' wealths.
      (try_for_range, ":center_no", centers_begin, centers_end),
        (party_get_slot, ":town_lord", ":center_no", slot_mainplanet_lord),
        (neq, ":town_lord", "trp_player"),
        (is_between, ":town_lord", faction_heroes_begin, faction_heroes_end),
        (party_get_slot, ":accumulated_rents", ":center_no", slot_center_accumulated_rents),
        (party_get_slot, ":accumulated_tariffs", ":center_no", slot_center_accumulated_tariffs),
        (troop_get_slot, ":troop_wealth", ":town_lord", slot_troop_wealth),
        (val_add, ":troop_wealth", ":accumulated_rents"),
        (val_add, ":troop_wealth", ":accumulated_tariffs"),
        (troop_set_slot, ":town_lord", slot_troop_wealth, ":troop_wealth"),
        (party_set_slot, ":center_no", slot_center_accumulated_rents, 0),
        (party_set_slot, ":center_no", slot_center_accumulated_tariffs, 0),
        (try_begin),
          (eq, "$cheat_mode", 1),
          (assign, reg1, ":troop_wealth"),
          (add_troop_note_from_sreg, ":town_lord", 1, "@Current wealth: {reg1}", 0),
        (try_end),
      (try_end),
	  #SW MF added global variable so our banking trigger knows taxes are ready
	  (assign, "$g_taxes_calculated", 1),
    ]),

#   (7 * 24,
#   [
##       (call_script, "script_get_number_of_unclaimed_centers_by_player"),
##       (assign, ":unclaimed_centers", reg0),
##       (gt, ":unclaimed_centers", 0),
# You are holding an estate without a lord.        
#       (try_for_range, ":troop_no", heroes_begin, heroes_end),
#         (troop_slot_eq, ":troop_no", slot_troop_occupation, slto_faction_hero),
#         (troop_get_slot, ":relation", ":troop_no", slot_troop_player_relation),
#         (val_sub, ":relation", 1),
#         (val_max, ":relation", -100),
#         (troop_set_slot, ":troop_no", slot_troop_player_relation, ":relation"),
#       (try_end),
# You relation with all factions other than your own has decreased by 1.     
#       (try_for_range, ":faction_no", factions_begin, factions_end),
#         (neq, ":faction_no", "$players_faction"),
#         (store_relation,":faction_relation",":faction_no","fac_player_supporters_faction"),
#         (val_sub, ":faction_relation", 1),
#         (val_max, ":faction_relation", -100),
#		  WARNING: Never use set_relation!
#         (set_relation, ":faction_no", "fac_player_supporters_faction", ":faction_relation"),
#       (try_end),
#    ]),

  
  # Offer player to join faction
   (32,
   [
     (eq, "$players_faction", 0),
     (le, "$g_invite_faction", 0),
     (eq, "$g_player_is_captive", 0),
     (store_random_in_range, ":faction_no", factions_begin, factions_end),
     (assign, ":min_distance", 999999),
     (try_for_range, ":center_no", walled_centers_begin, walled_centers_end),
       (store_faction_of_party, ":center_faction", ":center_no"),
       (eq, ":center_faction", ":faction_no"),
       (store_distance_to_party_from_party, ":cur_distance", "p_main_party", ":center_no"),
       (val_min, ":min_distance", ":cur_distance"),
     (try_end),
     (lt, ":min_distance", 30),
     (store_relation, ":faction_relation", ":faction_no", "fac_player_supporters_faction"),
     (faction_get_slot, ":faction_lord", ":faction_no", slot_faction_leader),
     (call_script, "script_troop_get_player_relation", ":faction_lord"),
     (assign, ":lord_relation", reg0),
     #(troop_get_slot, ":lord_relation", ":faction_lord", slot_troop_player_relation),
     (call_script, "script_get_number_of_hero_centers", "trp_player"),
     (assign, ":num_centers_owned", reg0),
     (try_begin),
       (eq, ":num_centers_owned", 0),
       (troop_get_slot, ":player_renown", "trp_player", slot_troop_renown),
       (ge, ":player_renown", 160),
       (ge, ":faction_relation", 0),
       (ge, ":lord_relation", 0),
       (store_random_in_range, ":rand", 0, 100),
       (lt, ":rand", 50),
       (call_script, "script_get_poorest_minorplanet_of_faction", ":faction_no"),
       (assign, "$g_invite_offered_center", reg0),
       (ge, "$g_invite_offered_center", 0),
       (assign, "$g_invite_faction", ":faction_no"),
       (jump_to_menu, "mnu_invite_player_to_faction"),
     (else_try),
       (gt, ":num_centers_owned", 0),
       (neq, "$players_oath_renounced_against_faction", ":faction_no"),
       (ge, ":faction_relation", -80),
       (ge, ":lord_relation", -30),
       (store_random_in_range, ":rand", 0, 100),
       (lt, ":rand", 20),
       (assign, "$g_invite_faction", ":faction_no"),
       (assign, "$g_invite_offered_center", -1),
       (jump_to_menu, "mnu_invite_player_to_faction_without_center"),
     (try_end),
    ]),

  # Change faction relations
   (24 * 7,
   [(call_script, "script_randomly_start_war_peace", 1),
    ]),

  # During rebellion, removing troops from player faction randomly because of low relation points
   (5,
   [
     (gt, "$supported_pretender", 0),
     (try_for_range, ":cur_troop", faction_heroes_begin, faction_heroes_end),
       (store_troop_faction, ":cur_faction", ":cur_troop"),
       (eq, ":cur_faction", "fac_player_supporters_faction"),
       (neg|troop_slot_ge, ":cur_troop", slot_troop_change_to_faction, 1),
       (call_script, "script_troop_get_player_relation", ":cur_troop"),
       (assign, ":player_relation", reg0),
       #(troop_get_slot, ":player_relation", ":cur_troop", slot_troop_player_relation),
       (lt, ":player_relation", -5),
       (neq, "$supported_pretender", ":cur_troop"),
       (val_mul, ":player_relation", -1),
       (val_sub, ":player_relation", 5),
       (store_random_in_range, ":random_no", 0, 2000),
       (lt, ":random_no", ":player_relation"),
       (call_script, "script_cf_get_random_active_faction_except_player_faction_and_faction", -1),
       (troop_set_slot, ":cur_troop", slot_troop_change_to_faction, reg0),
     (try_end),
    ]),


  # Reset faction lady current centers
##   (28,
##   [
##       (try_for_range, ":troop_no", heroes_begin, heroes_end),
##         (troop_slot_eq, ":troop_no", slot_troop_occupation, slto_faction_lady),
##
##         # Find the active quest ladies
##         (assign, ":not_ok", 0),
##         (try_for_range, ":quest_no", lord_quests_begin, lord_quests_end),
##           (eq, ":not_ok", 0),
##           (check_quest_active, ":quest_no"),
##           (quest_slot_eq, ":quest_no", slot_quest_object_troop, ":troop_no"),
##           (assign, ":not_ok", 1),
##         (try_end),
##         (eq, ":not_ok", 0),
##
##         (troop_get_slot, ":troop_center", ":troop_no", slot_troop_cur_center),
##         (assign, ":is_under_siege", 0),
##         (try_begin),
##           (is_between, ":troop_center", walled_centers_begin, walled_centers_end),
##           (party_get_battle_opponent, ":besieger_party", ":troop_center"),
##           (gt, ":besieger_party", 0),
##           (assign, ":is_under_siege", 1),
##         (try_end),
##
##         (eq, ":is_under_siege", 0),# Omit ladies in centers under siege
##
##         (try_begin),
##           (store_random_in_range, ":random_num",0, 100),
##           (lt, ":random_num", 20),
##           (store_troop_faction, ":cur_faction", ":troop_no"),
##           (call_script, "script_cf_select_random_town_with_faction", ":cur_faction"),#Can fail
##           (troop_set_slot, ":troop_no", slot_troop_cur_center, reg0),
##         (try_end),
##       
##         (store_random_in_range, ":random_num",0, 100),
##         (lt, ":random_num", 50),
##         (troop_get_slot, ":lord_no", ":troop_no", slot_troop_father),
##         (try_begin),
##           (eq, ":lord_no", 0),
##           (troop_get_slot, ":lord_no", ":troop_no", slot_troop_spouse),
##         (try_end),
##         (gt, ":lord_no", 0),
##         (troop_get_slot, ":cur_party", ":lord_no", slot_troop_leaded_party),
##         (gt, ":cur_party", 0),
##         (party_get_attached_to, ":cur_center", ":cur_party"),
##         (gt, ":cur_center", 0),
##
##         (troop_set_slot, ":troop_no", slot_troop_cur_center, ":cur_center"),
##       (try_end),
##    ]),


  # Attach Lord Parties to the town they are in
  (0.1,
   [
       (try_for_range, ":troop_no", heroes_begin, heroes_end),
         (troop_slot_eq, ":troop_no", slot_troop_occupation, slto_faction_hero),
         (troop_get_slot, ":troop_party_no", ":troop_no", slot_troop_leaded_party),
         (ge, ":troop_party_no", 1),
         (party_get_attached_to, ":cur_attached_town", ":troop_party_no"),
         (lt, ":cur_attached_town", 1),
         (party_get_cur_town, ":destination", ":troop_party_no"),
         (is_between, ":destination", centers_begin, centers_end),
         (call_script, "script_get_relation_between_parties", ":destination", ":troop_party_no"),
         (try_begin),
           (ge, reg0, 0),
           (party_attach_to_party, ":troop_party_no", ":destination"),
         (else_try),
           (party_set_ai_behavior, ":troop_party_no", ai_bhvr_hold),
         (try_end),
         (try_begin),
           (this_or_next|party_slot_eq, ":destination", slot_party_type, spt_mainplanet),
           (party_slot_eq, ":destination", slot_party_type, spt_castle),
           (store_faction_of_party, ":troop_faction_no", ":troop_party_no"),
           (store_faction_of_party, ":destination_faction_no", ":destination"),
           (eq, ":troop_faction_no", ":destination_faction_no"),
           (party_get_num_prisoner_stacks, ":num_stacks", ":troop_party_no"),
           (gt, ":num_stacks", 0),
           (assign, "$g_move_heroes", 1),
           (call_script, "script_party_prisoners_add_party_prisoners", ":destination", ":troop_party_no"),#Moving prisoners to the center
           (assign, "$g_move_heroes", 1),
           (call_script, "script_party_remove_all_prisoners", ":troop_party_no"),
         (try_end),
       (try_end),
    ]),

  # Check escape chances of hero prisoners.
  (48,
   [
       (call_script, "script_randomly_make_prisoner_heroes_escape_from_party", "p_main_party", 50),
       (try_for_range, ":center_no", walled_centers_begin, walled_centers_end),
##         (party_slot_eq, ":center_no", slot_mainplanet_lord, "trp_player"),
         (assign, ":chance", 30),
         (try_begin),
           (party_slot_eq, ":center_no", slot_center_has_prisoner_tower, 1),
           (assign, ":chance", 5),
         (try_end),
         (call_script, "script_randomly_make_prisoner_heroes_escape_from_party", ":center_no", ":chance"),
       (try_end),
    ]),

  # Asking the ownership of captured centers to the player
  (3,
   [
    (assign, "$g_center_taken_by_player_faction", -1),
    (try_for_range, ":center_no", centers_begin, centers_end),
      (eq, "$g_center_taken_by_player_faction", -1),
      (store_faction_of_party, ":center_faction", ":center_no"),
      (eq, ":center_faction", "fac_player_supporters_faction"),
      (this_or_next|party_slot_eq, ":center_no", slot_mainplanet_lord, stl_reserved_for_player),
      (this_or_next|party_slot_eq, ":center_no", slot_mainplanet_lord, stl_unassigned),
      (party_slot_eq, ":center_no", slot_mainplanet_lord, stl_rejected_by_player),
      (assign, "$g_center_taken_by_player_faction", ":center_no"),
    (try_end),
    (ge, "$g_center_taken_by_player_faction", 0),
    (faction_get_slot, ":leader", "fac_player_supporters_faction", slot_faction_leader),
    (start_map_conversation, ":leader"),
    ]),


  # Respawn hero party after faction hero is released from captivity.
  (48,
   [
       (try_for_range, ":troop_no", faction_heroes_begin, faction_heroes_end),
         (troop_slot_eq, ":troop_no", slot_troop_occupation, slto_faction_hero),
         #(troop_slot_eq, ":troop_no", slot_troop_is_prisoner, 0),
         (neg|troop_slot_ge, ":troop_no", slot_troop_prisoner_of_party, 0),
         (neg|troop_slot_ge, ":troop_no", slot_troop_leaded_party, 1),

         (store_troop_faction, ":cur_faction", ":troop_no"),
         (try_begin),
           (call_script, "script_cf_select_random_walled_center_with_faction_and_owner_priority_no_siege", ":cur_faction", ":troop_no"),#Can fail
           (assign, ":center_no", reg0),
           (call_script, "script_create_faction_hero_party", ":troop_no", ":center_no"),
           (party_attach_to_party, "$pout_party", ":center_no"),
         (else_try),
           (neg|faction_slot_eq, ":cur_faction", slot_faction_state, sfs_active),
           (try_begin),
             (is_between, ":troop_no", kings_begin, kings_end),
             (troop_set_slot, ":troop_no", slot_troop_change_to_faction, "fac_commoners"),
           (else_try),
             (store_random_in_range, ":random_no", 0, 100),
             (lt, ":random_no", 10),
             (call_script, "script_cf_get_random_active_faction_except_player_faction_and_faction", ":cur_faction"),
             (troop_set_slot, ":troop_no", slot_troop_change_to_faction, reg0),
           (try_end),
         (try_end),
       (try_end),
    ]),

  # Spawn merchant caravan parties
##  (3,
##   [
##       (try_for_range, ":troop_no", merchants_begin, merchants_end),
##         (troop_slot_eq, ":troop_no", slot_troop_occupation, slto_merchant),
##         (troop_slot_eq, ":troop_no", slot_troop_is_prisoner, 0),
##         (neg|troop_slot_ge, ":troop_no", slot_troop_leaded_party, 1),
##
##         (call_script, "script_cf_create_merchant_party", ":troop_no"),
##       (try_end),
##    ]),

  # Spawn village farmer parties
  (24,
   [
       (try_for_range, ":minorplanet_no", minorplanet_begin, minorplanet_end),
         (party_slot_eq, ":minorplanet_no", slot_minorplanet_state, svs_normal),
         (party_get_slot, ":farmer_party", ":minorplanet_no", slot_minorplanet_farmer_party),
         (this_or_next|eq, ":farmer_party", 0),
         (neg|party_is_active, ":farmer_party"),
         (store_random_in_range, ":random_no", 0, 100),
         (lt, ":random_no", 30),
         (call_script, "script_create_minorplanet_farmer_party", ":minorplanet_no"),
         (party_set_slot, ":minorplanet_no", slot_minorplanet_farmer_party, reg0),
#         (str_store_party_name, s1, ":minorplanet_no"),
#         (display_message, "@Village farmers created at {s1}."),
       (try_end),
    ]),

  
   (72,
   [
  # Updating trade good prices according to the productions
       (call_script, "script_update_trade_good_prices"),
 # Updating player odds
       (try_for_range, ":cur_center", centers_begin, centers_end),
         (party_get_slot, ":player_odds", ":cur_center", slot_mainplanet_player_odds),
         (try_begin),
           (gt, ":player_odds", 1000),
           (val_mul, ":player_odds", 95),
           (val_div, ":player_odds", 100),
           (val_max, ":player_odds", 1000),
         (else_try),
           (lt, ":player_odds", 1000),
           (val_mul, ":player_odds", 105),
           (val_div, ":player_odds", 100),
           (val_min, ":player_odds", 1000),
         (try_end),
         (party_set_slot, ":cur_center", slot_mainplanet_player_odds, ":player_odds"),
       (try_end),
    ]),


  #Troop AI: Merchants thinking
  (8,
   [
       (try_for_parties, ":party_no"),
         (party_slot_eq, ":party_no", slot_party_type, spt_faction_caravan),
         (party_is_in_any_town, ":party_no"),

         (store_faction_of_party, ":merchant_faction", ":party_no"),
         (faction_get_slot, ":num_towns", ":merchant_faction", slot_faction_num_towns),
         (try_begin),
           (le, ":num_towns", 0),
           (remove_party, ":party_no"),
         (else_try),
           (store_random_in_range, ":random_no", 0, 100),
           (lt, ":random_no", 35),
       
           (party_get_cur_town, ":cur_center", ":party_no"),

           (assign, ":can_leave", 1),
           (try_begin),
             (is_between, ":cur_center", walled_centers_begin, walled_centers_end),
             (neg|party_slot_eq, ":cur_center", slot_center_is_besieged_by, -1),
             (assign, ":can_leave", 0),
           (try_end),
           (eq, ":can_leave", 1),

           (assign, ":do_trade", 0),
           (try_begin),
             (party_get_slot, ":cur_ai_state", ":party_no", slot_party_ai_state),
             (eq, ":cur_ai_state", spai_trading_with_town),
             (party_get_slot, ":cur_ai_object", ":party_no", slot_party_ai_object),
             (eq, ":cur_center", ":cur_ai_object"),
             (assign, ":do_trade", 1),
           (try_end),

           (assign, ":target_center", -1),
           
           (try_begin), #Make sure escorted caravan continues to its original destination.
             (eq, "$caravan_escort_party_id", ":party_no"),
             (neg|party_is_in_town, ":party_no", "$caravan_escort_destination_town"),
             (assign, ":target_center", "$caravan_escort_destination_town"),
           (else_try),
             (call_script, "script_cf_select_random_town_at_peace_with_faction_in_trade_route", ":cur_center", ":merchant_faction"),
             (assign, ":target_center", reg0),
           (try_end),
           (is_between, ":target_center", mainplanets_begin, mainplanets_end),
           (neg|party_is_in_town, ":party_no", ":target_center"),
       
           (try_begin),
             (eq, ":do_trade", 1),
             (call_script, "script_do_merchant_town_trade", ":party_no", ":cur_center"),
           (try_end),
           (party_set_ai_behavior, ":party_no", ai_bhvr_travel_to_party),
           (party_set_ai_object, ":party_no", ":target_center"),
           (party_set_flags, ":party_no", pf_default_behavior, 0),
           (party_set_slot, ":party_no", slot_party_ai_state, spai_trading_with_town),
           (party_set_slot, ":party_no", slot_party_ai_object, ":target_center"),
         (try_end),
       (try_end),
    ]),

  #Troop AI: Village farmers thinking
  (8,
   [
       (try_for_parties, ":party_no"),
         (party_slot_eq, ":party_no", slot_party_type, spt_minorplanet_farmer),
         (party_is_in_any_town, ":party_no"),
         (party_get_slot, ":home_center", ":party_no", slot_party_home_center),
         (party_get_cur_town, ":cur_center", ":party_no"),

         (assign, ":can_leave", 1),
         (try_begin),
           (is_between, ":cur_center", walled_centers_begin, walled_centers_end),
           (neg|party_slot_eq, ":cur_center", slot_center_is_besieged_by, -1),
           (assign, ":can_leave", 0),
         (try_end),
         (eq, ":can_leave", 1),

         (try_begin),
           (eq, ":cur_center", ":home_center"),
           (try_begin),
             (store_random_in_range, ":random_no", 0, 100),
             (lt, ":random_no", 5),
             (call_script, "script_do_party_center_trade", ":party_no", ":home_center", 50),
             (assign, ":total_change", reg0),
             (party_get_slot, ":prosperity", ":home_center", slot_mainplanet_prosperity),
             (val_add, ":prosperity", 30),
             (val_mul, ":total_change", ":prosperity"),
             (val_div, ":total_change", 2600), #(30 + prosperity) / 130 * 5% of the sales.

             #Adding tax revenue to the center
             (party_get_slot, ":accumulated_tariffs", ":home_center", slot_center_accumulated_tariffs),
             (val_add, ":accumulated_tariffs", ":total_change"),
             (party_set_slot, ":home_center", slot_center_accumulated_tariffs, ":accumulated_tariffs"),
      
             #Moving farmers to the home town
             (party_get_slot, ":market_town", ":home_center", slot_minorplanet_market_town),
             (party_set_slot, ":party_no", slot_party_ai_object, ":market_town"),
             (party_set_slot, ":party_no", slot_party_ai_state, spai_trading_with_town),
             (party_set_ai_behavior, ":party_no", ai_bhvr_travel_to_party),
             (party_set_ai_object, ":party_no", ":market_town"),
##             (try_begin),
##               (eq, "$cheat_mode", 1),
##               (str_store_party_name, s1, ":home_center"),
##               (assign, reg1, ":total_change"),
##               (display_message, "@Village farmers traded with {s1} merchants. Tax={reg1}"),
##             (try_end),
           (try_end),
         (else_try),
           (try_begin),
             (party_get_slot, ":cur_ai_object", ":party_no", slot_party_ai_object),
             (eq, ":cur_center", ":cur_ai_object"),

             (call_script, "script_do_party_center_trade", ":party_no", ":cur_ai_object", 10),
             (assign, ":total_change", reg0),
             (party_get_slot, ":prosperity", ":cur_ai_object", slot_mainplanet_prosperity),
             (val_add, ":prosperity", 30),
             (val_mul, ":total_change", ":prosperity"),
             (val_div, ":total_change", 2600), #(30 + prosperity) / 130 * 5% of the sales.

             #Adding tax revenue to the center
             (party_get_slot, ":accumulated_tariffs", ":cur_ai_object", slot_center_accumulated_tariffs),
             (val_add, ":accumulated_tariffs", ":total_change"),
             (party_set_slot, ":cur_ai_object", slot_center_accumulated_tariffs, ":accumulated_tariffs"),
             #Adding tax revenue to the home center
             (party_get_slot, ":accumulated_tariffs", ":home_center", slot_center_accumulated_tariffs),
             (val_add, ":accumulated_tariffs", ":total_change"),
             (party_set_slot, ":home_center", slot_center_accumulated_tariffs, ":accumulated_tariffs"),

             #Increasing food stocks of the town
             (party_get_slot, ":town_food_store", ":cur_ai_object", slot_party_food_store),
             (call_script, "script_center_get_food_store_limit", ":cur_ai_object"),
             (assign, ":food_store_limit", reg0),
             (val_add, ":town_food_store", 1000),
             (val_min, ":town_food_store", ":food_store_limit"),
             (party_set_slot, ":cur_ai_object", slot_party_food_store, ":town_food_store"),

             #Adding 1 to village prosperity
             (try_begin),
               (store_random_in_range, ":rand", 0, 100),
               (lt, ":rand", 35),
               (call_script, "script_change_center_prosperity", ":home_center", 1),
             (try_end),
           (try_end),

           #Moving farmers to their home village
           (party_set_slot, ":party_no", slot_party_ai_object, ":home_center"),
           (party_set_slot, ":party_no", slot_party_ai_state, spai_trading_with_town),
           (party_set_ai_behavior, ":party_no", ai_bhvr_travel_to_party),
           (party_set_ai_object, ":party_no", ":home_center"),
##           (try_begin),
##             (eq, "$cheat_mode", 1),
##             (str_store_party_name, s1, ":cur_ai_object"),
##             (assign, reg1, ":total_change"),
##             (display_message, "@Village farmers traded with {s1} merchants. Tax={reg1} to both sides"),
##           (try_end),
         (try_end),
       (try_end),
    ]),

 #Increase castle food stores
  (2,
   [
       (try_for_range, ":center_no", castles_begin, castles_end),
         (party_slot_eq, ":center_no", slot_center_is_besieged_by, -1), #castle is not under siege
         (party_get_slot, ":center_food_store", ":center_no", slot_party_food_store),
         (val_add, ":center_food_store", 100),
         (call_script, "script_center_get_food_store_limit", ":center_no"),
         (assign, ":food_store_limit", reg0),
         (val_min, ":center_food_store", ":food_store_limit"),
         (party_set_slot, ":center_no", slot_party_food_store, ":center_food_store"),
       (try_end),
    ]),

 #cache party strengths (to avoid re-calculating)
##  (2,
##   [
##       (try_for_range, ":cur_troop", heroes_begin, heroes_end),
##         (troop_slot_eq, ":cur_troop", slot_troop_occupation, slto_faction_hero),
##         (troop_get_slot, ":cur_party", ":cur_troop", slot_troop_leaded_party),
##         (ge, ":cur_party", 0),
##         (call_script, "script_party_calculate_strength", ":cur_party", 0), #will update slot_party_cached_strength
##       (try_end),
##    ]),
##  
##  (6,
##   [
##       (try_for_range, ":cur_center", walled_centers_begin, walled_centers_end),
##         (call_script, "script_party_calculate_strength", ":cur_center", 0), #will update slot_party_cached_strength
##       (try_end),
##    ]),

##  (1,
##   [
##       (try_for_range, ":cur_center", walled_centers_begin, walled_centers_end),
##         (store_random_in_range, ":rand", 0, 100),
##         (lt, ":rand", 10),
##         (store_faction_of_party, ":center_faction", ":cur_center"),
##         (assign, ":friend_strength", 0),
##         (try_for_range, ":cur_troop", heroes_begin, heroes_end),
##           (troop_slot_eq, ":cur_troop", slot_troop_occupation, slto_faction_hero),
##           (troop_get_slot, ":cur_troop_party", ":cur_troop", slot_troop_leaded_party),
##           (gt, ":cur_troop_party", 0),
##           (store_distance_to_party_from_party, ":distance", ":cur_troop_party", ":cur_center"),
##           (lt, ":distance", 10),
##           (store_troop_faction, ":army_faction", ":cur_troop"),
##           (store_relation, ":rel", ":army_faction", ":center_faction"),
##           (try_begin),
##             (gt, ":rel", 10),
##             (party_get_slot, ":str", ":cur_troop_party", slot_party_cached_strength),
##             (val_add, ":friend_strength", ":str"),
##           (try_end),
##         (try_end),
##         (party_set_slot, ":cur_center", slot_party_nearby_friend_strength, ":friend_strength"),
##       (try_end),
##    ]),

  # Make heroes running away from someone retreat to friendly centers
  (0.5,
   [
       (try_for_range, ":cur_troop", heroes_begin, heroes_end),
         (troop_slot_eq, ":cur_troop", slot_troop_occupation, slto_faction_hero),
         (troop_get_slot, ":cur_party", ":cur_troop", slot_troop_leaded_party),
         (gt, ":cur_party", 0),
         (try_begin),
           (party_is_active, ":cur_party"),
           (try_begin),
             (get_party_ai_current_behavior, ":ai_bhvr", ":cur_party"),
             (eq, ":ai_bhvr", ai_bhvr_avoid_party),
             (store_faction_of_party, ":party_faction", ":cur_party"),
             (party_get_slot, ":commander_party", ":cur_party", slot_party_commander_party),
             (faction_get_slot, ":faction_marshall", ":party_faction", slot_faction_marshall),
             (neq, ":faction_marshall", ":cur_troop"),
             (assign, ":continue", 1),
             (try_begin),
               (ge, ":faction_marshall", 0),
               (troop_get_slot, ":faction_marshall_party", ":faction_marshall", slot_troop_leaded_party),
               (ge, ":faction_marshall_party", 0),
               (eq, ":commander_party", ":faction_marshall_party"),
               (assign, ":continue", 0),
             (try_end),
             (eq, ":continue", 1),
             (assign, ":done", 0),
             (try_for_range, ":cur_center", walled_centers_begin, walled_centers_end),
               (eq, ":done", 0),
               (party_slot_eq, ":cur_center", slot_center_is_besieged_by, -1),
               (store_faction_of_party, ":center_faction", ":cur_center"),
               (store_relation, ":cur_relation", ":center_faction", ":party_faction"),
               (gt, ":cur_relation", 0),
               (store_distance_to_party_from_party, ":cur_distance", ":cur_party", ":cur_center"),
               (lt, ":cur_distance", 20),
               (party_get_position, pos1, ":cur_party"),
               (party_get_position, pos2, ":cur_center"),
               (neg|position_is_behind_position, pos2, pos1),
               (call_script, "script_party_set_ai_state", ":cur_party", spai_retreating_to_center, ":cur_center"),
               (assign, ":done", 1),
             (try_end),
           (try_end),
         (else_try),
           (troop_set_slot, ":cur_troop", slot_troop_leaded_party, -1),
         (try_end),
       (try_end),
    ]),

  # Centers give alarm if the player is around
  (0.5,
   [
     (store_current_hours, ":cur_hours"),
     (store_mod, ":cur_hours_mod", ":cur_hours", 11),
     (store_sub, ":hour_limit", ":cur_hours", 5),
     (party_get_num_companions, ":num_men", "p_main_party"),
     (party_get_num_prisoners, ":num_prisoners", "p_main_party"),
     (val_add, ":num_men", ":num_prisoners"),
     (convert_to_fixed_point, ":num_men"),
     (store_sqrt, ":num_men_effect", ":num_men"),
     (convert_from_fixed_point, ":num_men_effect"),
     (try_begin),
       (eq, ":cur_hours_mod", 0),
       #Reduce alarm by 2 in every 11 hours.
       (try_for_range, ":cur_faction", factions_begin, factions_end),
         (faction_get_slot, ":player_alarm", ":cur_faction", slot_faction_player_alarm),
         (val_sub, ":player_alarm", 1),
         (val_max, ":player_alarm", 0),
         (faction_set_slot, ":cur_faction", slot_faction_player_alarm, ":player_alarm"),
       (try_end),
     (try_end),
     (eq, "$g_player_is_captive", 0),
     (try_for_range, ":cur_center", centers_begin, centers_end),
       (store_faction_of_party, ":cur_faction", ":cur_center"),
       (store_relation, ":reln", ":cur_faction", "fac_player_supporters_faction"),
       (lt, ":reln", 0),
       (store_distance_to_party_from_party, ":dist", "p_main_party", ":cur_center"),
       (lt, ":dist", 5),
       (store_mul, ":dist_sqr", ":dist", ":dist"),
       (store_sub, ":dist_effect", 20, ":dist_sqr"),
       (store_sub, ":reln_effect", 20, ":reln"),
       (store_mul, ":total_effect", ":dist_effect", ":reln_effect"),
       (val_mul, ":total_effect", ":num_men_effect"),
       (store_div, ":spot_chance", ":total_effect", 10),
       (store_random_in_range, ":random_spot", 0, 1000),
       (lt, ":random_spot", ":spot_chance"),
       (faction_get_slot, ":player_alarm", ":cur_faction", slot_faction_player_alarm),
       (val_add, ":player_alarm", 1),
       (val_min, ":player_alarm", 100),
       (faction_set_slot, ":cur_faction", slot_faction_player_alarm, ":player_alarm"),
       (try_begin),
         (neg|party_slot_ge, ":cur_center", slot_center_last_player_alarm_hour, ":hour_limit"),
         (str_store_party_name_link, s1, ":cur_center"),
         (display_message, "@Your party is spotted by {s1}."),
         (party_set_slot, ":cur_center", slot_center_last_player_alarm_hour, ":cur_hours"),
       (try_end),
     (try_end),
    ]),
  
  # Consuming food at every 14 hours
  (14,
   [#(store_sub, ":num_food", food_end, food_begin),
    (eq, "$g_player_is_captive", 0),
    (party_get_num_companion_stacks, ":num_stacks","p_main_party"),
    (assign, ":num_men", 0),
    (try_for_range, ":i_stack", 0, ":num_stacks"),
      (party_stack_get_size, ":stack_size","p_main_party",":i_stack"),
      (val_add, ":num_men", ":stack_size"),
    (try_end),
    (val_div, ":num_men", 3),
    (try_begin),
      (eq, ":num_men", 0),
      (val_add, ":num_men", 1),
    (try_end),
    
    (assign, ":consumption_amount", ":num_men"),
    (assign, ":no_food_displayed", 0),
    (try_for_range, ":unused", 0, ":consumption_amount"),
      (assign, ":available_food", 0),
      (try_for_range, ":cur_food", food_begin, food_end),
        (item_set_slot, ":cur_food", slot_item_is_checked, 0),
        (call_script, "script_cf_player_has_item_without_modifier", ":cur_food", imod_rotten),
        (val_add, ":available_food", 1),
      (try_end),
      (try_begin),
        (gt, ":available_food", 0),
        (store_random_in_range, ":selected_food", 0, ":available_food"),
        (call_script, "script_consume_food", ":selected_food"),
      (else_try),
        (eq, ":no_food_displayed", 0),
        (display_message, "@Party has nothing to eat!", color_terrible_news),
        (call_script, "script_change_player_party_morale", -3),
        (assign, ":no_food_displayed", 1),
#NPC companion changes begin
        (try_begin),
            (call_script, "script_party_count_fit_regulars", "p_main_party"),
            (gt, reg0, 0),
            (call_script, "script_objectionable_action", tmt_egalitarian, "str_men_hungry"),
        (try_end),
#NPC companion changes end
      (try_end),
    (try_end),
    ]),

  # Setting item modifiers for food
  (24,
   [
     (troop_get_inventory_capacity, ":inv_size", "trp_player"),
     (try_for_range, ":i_slot", 0, ":inv_size"),
       (troop_get_inventory_slot, ":item_id", "trp_player", ":i_slot"),
       (eq, ":item_id", "itm_cattle_meat"),
       (troop_get_inventory_slot_modifier, ":modifier", "trp_player", ":i_slot"),
       (try_begin),
         (ge, ":modifier", imod_fresh),
         (lt, ":modifier", imod_rotten),
         (val_add, ":modifier", 1),
         (troop_set_inventory_slot_modifier, "trp_player", ":i_slot", ":modifier"),
       (else_try),
         (lt, ":modifier", imod_fresh),
         (troop_set_inventory_slot_modifier, "trp_player", ":i_slot", imod_fresh),
       (try_end),
     (try_end),
    ]),

  # Assigning lords to centers with no leaders
  (72,
   [(call_script, "script_assign_lords_to_empty_centers"),
    ]),

#SW - commented out code so icon_player map icon is not modified, nevermind, causes some global variable errors, made minor changes so icon wouldn't switch
  #Updating player icon in every frame
  (0,
   [(troop_get_inventory_slot, ":cur_horse", "trp_player", 8), #horse slot
    (assign, ":new_icon", -1),
    (try_begin),
      (eq, "$g_player_icon_state", pis_normal),
      (try_begin),
        (ge, ":cur_horse", 0),
        #(assign, ":new_icon", "icon_player_horseman"),
		(assign, ":new_icon", "icon_player"),
      (else_try),
        (assign, ":new_icon", "icon_player"),
      (try_end),
    (else_try),
      (eq, "$g_player_icon_state", pis_camping),
      #(assign, ":new_icon", "icon_camp"),
	  (assign, ":new_icon", "icon_player"),
    (else_try),
      (eq, "$g_player_icon_state", pis_ship),
      #(assign, ":new_icon", "icon_ship"),
	  (assign, ":new_icon", "icon_player"),
    (try_end),
    (neq, ":new_icon", "$g_player_party_icon"),
    (assign, "$g_player_party_icon", ":new_icon"),
    #(party_set_icon, "p_main_party", ":new_icon"),
    ]),
  
 #Update how good a target player is for bandits
  (2,
   [
       (store_troop_gold, ":total_value", "trp_player"),
       (store_div, ":bandit_attraction", ":total_value", (10000/100)), #10000 gold = excellent_target

       (troop_get_inventory_capacity, ":inv_size", "trp_player"),
       (try_for_range, ":i_slot", 0, ":inv_size"),
         (troop_get_inventory_slot, ":item_id", "trp_player", ":i_slot"),
         (ge, ":item_id", 0),
         (try_begin),
           (is_between, ":item_id", trade_goods_begin, trade_goods_end),
           (store_item_value, ":item_value", ":item_id"),
           (val_add, ":total_value", ":item_value"),
         (try_end),
       (try_end),
       (val_clamp, ":bandit_attraction", 0, 100),
       (party_set_bandit_attraction, "p_main_party", ":bandit_attraction"),
    ]),

  # Checking escape chances of prisoners that joined the party recently.
  (6,
   [(gt, "$g_prisoner_recruit_troop_id", 0),
    (gt, "$g_prisoner_recruit_size", 0),
    (gt, "$g_prisoner_recruit_last_time", 0),
    (is_currently_night),
    (try_begin),
      (store_skill_level, ":leadership", "skl_leadership", "trp_player"),
      (val_mul, ":leadership", 5),
      (store_sub, ":chance", 66, ":leadership"),
      (gt, ":chance", 0),
      (assign, ":num_escaped", 0),
      (try_for_range, ":unused", 0, "$g_prisoner_recruit_size"),
        (store_random_in_range, ":random_no", 0, 100),
        (lt, ":random_no", ":chance"),
        (val_add, ":num_escaped", 1),
      (try_end),
      (party_remove_members, "p_main_party", "$g_prisoner_recruit_troop_id", ":num_escaped"),
      (assign, ":num_escaped", reg0),
      (gt, ":num_escaped", 0),
      (try_begin),
        (gt, ":num_escaped", 1),
        (assign, reg2, 1),
      (else_try),
        (assign, reg2, 0),
      (try_end),
      (assign, reg1, ":num_escaped"),
      (str_store_troop_name_by_count, s1, "$g_prisoner_recruit_troop_id", ":num_escaped"),
      (display_log_message, "@{reg1} {s1} {reg2?have:has} escaped from your party during the night.", color_bad_news),
    (try_end),
    (assign, "$g_prisoner_recruit_troop_id", 0),
    (assign, "$g_prisoner_recruit_size", 0),
    ]),

  # Offering ransom fees for player's prisoner heroes
  (24,
   [(neq, "$g_ransom_offer_rejected", 1),
    (call_script, "script_offer_ransom_amount_to_player_for_prisoners_in_party", "p_main_party"),
    (eq, reg0, 0),#no prisoners offered
    (assign, ":end_cond", walled_centers_end),
    (try_for_range, ":center_no", walled_centers_begin, ":end_cond"),
      (party_slot_eq, ":center_no", slot_mainplanet_lord, "trp_player"),
      (call_script, "script_offer_ransom_amount_to_player_for_prisoners_in_party", ":center_no"),
      (eq, reg0, 1),#a prisoner is offered
      (assign, ":end_cond", 0),#break
    (try_end),
    ]), 

  # Exchanging hero prisoners between factions and clearing old ransom offers
  (72,
   [(assign, "$g_ransom_offer_rejected", 0),
    (try_for_range, ":center_no", walled_centers_begin, walled_centers_end),
      (party_get_slot, ":town_lord", ":center_no", slot_mainplanet_lord),
      (gt, ":town_lord", 0),
      (party_get_num_prisoner_stacks, ":num_stacks", ":center_no"),
      (try_for_range_backwards, ":i_stack", 0, ":num_stacks"),
        (party_prisoner_stack_get_troop_id, ":stack_troop", ":center_no", ":i_stack"),
        (troop_is_hero, ":stack_troop"),
        (troop_slot_eq, ":stack_troop", slot_troop_occupation, slto_faction_hero),
        (store_random_in_range, ":random_no", 0, 100),
        (try_begin),
          (le, ":random_no", 10),
          (call_script, "script_calculate_ransom_amount_for_troop", ":stack_troop"),
          (assign, ":ransom_amount", reg0),
          (troop_get_slot, ":wealth", ":town_lord", slot_troop_wealth),
          (val_add, ":wealth", ":ransom_amount"),
          (troop_set_slot, ":town_lord", slot_troop_wealth, ":wealth"),
          (party_remove_prisoners, ":center_no", ":stack_troop", 1),
          (call_script, "script_remove_troop_from_prison", ":stack_troop"),
          (store_troop_faction, ":faction_no", ":town_lord"),
          (store_troop_faction, ":troop_faction", ":stack_troop"),
          (str_store_troop_name, s1, ":stack_troop"),
          (str_store_faction_name, s2, ":faction_no"),
          (str_store_faction_name, s3, ":troop_faction"),
		  # HC - Select the message color based on the circumstances. reg20 holds the color.
		  (call_script, "script_get_message_color", news_lord_freed, ":stack_troop"),
		  (display_log_message, "@{s1} of {s3} has been released from captivity.", reg20),
          #(display_log_message, "@{s1} of {s3} has been released from captivity."),
        (try_end),
      (try_end),
    (try_end),
    ]),
  
  # Adding mercenary troops to the towns
  #SW - switched mercenaries and others to switch every 36 hours
  #(72,
  (36,
   [(call_script, "script_update_mercenary_units_of_towns"),
#NPC changes begin
# removes   (call_script, "script_update_companion_candidates_in_taverns"),
#NPC changes end
    (call_script, "script_update_ransom_brokers"),
    (call_script, "script_update_tavern_travelers"),
    (call_script, "script_update_tavern_minstels"),
    (call_script, "script_update_booksellers"),
    (call_script, "script_update_villages_infested_by_bandits"),
    (try_for_range, ":minorplanet_no", minorplanet_begin, minorplanet_end),
      (call_script, "script_update_volunteer_troops_in_village", ":minorplanet_no"),
      (call_script, "script_update_npc_volunteer_troops_in_village", ":minorplanet_no"),
    (try_end),
    ]),

  #SW - refresh inventory of force-sensitive trainers and clone era merchants (ie. bookseller)
  (1,
   [
		(call_script, "script_update_fs_merchants"),
		(call_script, "script_update_fs_trainers"),
		(call_script, "script_update_ce_merchants"),	
		(call_script, "script_update_iw_merchants"),
		(call_script, "script_update_dp_merchants"),
		(call_script, "script_update_ps_merchants"),
   ]),	

  # Setting random walker types
  (36,
   [(try_for_range, ":center_no", centers_begin, centers_end),
      (this_or_next|party_slot_eq, ":center_no", slot_party_type, spt_mainplanet),
      (             party_slot_eq, ":center_no", slot_party_type, spt_minorplanet),
      (call_script, "script_center_remove_walker_type_from_walkers", ":center_no", walkert_needs_money),
      (call_script, "script_center_remove_walker_type_from_walkers", ":center_no", walkert_needs_money_helped),
      (store_random_in_range, ":rand", 0, 100),
      (try_begin),
        (lt, ":rand", 70),
        (neg|party_slot_ge, ":center_no", slot_mainplanet_prosperity, 60),
        (call_script, "script_cf_center_get_free_walker", ":center_no"),
        (call_script, "script_center_set_walker_to_type", ":center_no", reg0, walkert_needs_money),
      (try_end),
    (try_end),
    ]),

  # Checking center upgrades
  (12,
   [(try_for_range, ":center_no", centers_begin, centers_end),
      (party_get_slot, ":cur_improvement", ":center_no", slot_center_current_improvement),
      (gt, ":cur_improvement", 0),
      (party_get_slot, ":cur_improvement_end_time", ":center_no", slot_center_improvement_end_hour),
      (store_current_hours, ":cur_hours"),
      (ge, ":cur_hours", ":cur_improvement_end_time"),
      (party_set_slot, ":center_no", ":cur_improvement", 1),
      (party_set_slot, ":center_no", slot_center_current_improvement, 0),
      (call_script, "script_get_improvement_details", ":cur_improvement"),
      (try_begin),
        (party_slot_eq, ":center_no", slot_mainplanet_lord, "trp_player"),
        (str_store_party_name, s4, ":center_no"),
        (display_log_message, "@Building of {s0} in {s4} has been completed.", color_quest_and_faction_news),
      (try_end),
      (try_begin),
        (is_between, ":center_no", minorplanet_begin, minorplanet_end),
        (eq, ":cur_improvement", slot_center_has_fish_pond),
        (call_script, "script_change_center_prosperity", ":center_no", 5),
      (try_end),
    (try_end),
    ]),

  # Adding tournaments to towns
  # Adding bandits to towns and villages
  (24,
   [(assign, ":num_active_tournaments", 0),
    (try_for_range, ":center_no", mainplanets_begin, mainplanets_end),
      (party_get_slot, ":has_tournament", ":center_no", slot_mainplanet_has_tournament),
      (try_begin),
        (eq, ":has_tournament", 1),#tournament ended, simulate
        (call_script, "script_fill_tournament_participants_troop", ":center_no", 0),
        (call_script, "script_sort_tournament_participant_troops"),#may not be needed
        (call_script, "script_get_num_tournament_participants"),
        (store_sub, ":needed_to_remove_randomly", reg0, 1),
        (call_script, "script_remove_tournament_participants_randomly", ":needed_to_remove_randomly"),
        (call_script, "script_sort_tournament_participant_troops"),
        (troop_get_slot, ":winner_troop", "trp_tournament_participants", 0),
        (try_begin),
          (is_between, ":winner_troop", faction_heroes_begin, faction_heroes_end),
          (str_store_troop_name_link, s1, ":winner_troop"),
          (str_store_party_name_link, s2, ":center_no"),
          (display_message, "@{s1} has won the tournament at {s2}.", color_hero_news),
          (call_script, "script_change_troop_renown", ":winner_troop", 20),
        (try_end),
      (try_end),
      (val_sub, ":has_tournament", 1),
      (val_max, ":has_tournament", 0),
      (party_set_slot, ":center_no", slot_mainplanet_has_tournament, ":has_tournament"),
      (try_begin),
        (gt, ":has_tournament", 0),
        (val_add, ":num_active_tournaments", 1),
      (try_end),
    (try_end),
    (try_for_range, ":center_no", centers_begin, centers_end),
      (this_or_next|party_slot_eq, ":center_no", slot_party_type, spt_mainplanet),
      (party_slot_eq, ":center_no", slot_party_type, spt_minorplanet),
      (party_get_slot, ":has_bandits", ":center_no", slot_center_has_bandits),
      (try_begin),
        (le, ":has_bandits", 0),
        (assign, ":continue", 0),
        (try_begin),
          (check_quest_active, "qst_deal_with_night_bandits"),
          (quest_slot_eq, "qst_deal_with_night_bandits", slot_quest_target_center, ":center_no"),
          (neg|check_quest_succeeded, "qst_deal_with_night_bandits"),
          (assign, ":continue", 1),
        (else_try),
          (store_random_in_range, ":random_no", 0, 100),
          (lt, ":random_no", 3),
          (assign, ":continue", 1),
        (try_end),
        (try_begin),
          (eq, ":continue", 1),
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
          (party_set_slot, ":center_no", slot_center_has_bandits, ":bandit_troop"),
          (try_begin),
            (eq, "$cheat_mode", 1),
            (str_store_party_name, s1, ":center_no"),
            (display_message, "@{s1} is infested by bandits (at night)."),
          (try_end),
        (try_end),
      (else_try),
        (try_begin),
          (assign, ":random_chance", 40),
          (try_begin),
            (party_slot_eq, ":center_no", slot_party_type, spt_mainplanet),
            (assign, ":random_chance", 20),
          (try_end),
          (store_random_in_range, ":random_no", 0, 100),
          (lt, ":random_no", ":random_chance"),
          (party_set_slot, ":center_no", slot_center_has_bandits, 0),
          (try_begin),
            (eq, "$cheat_mode", 1),
            (str_store_party_name, s1, ":center_no"),
            (display_message, "@{s1} is no longer infested by bandits (at night)."),
          (try_end),
        (try_end),
      (try_end),
    (try_end),
    (try_begin),
      (lt, ":num_active_tournaments", 3),
      (store_random_in_range, ":random_no", 0, 100),
      #Add new tournaments with a 30% chance if there are less than 3 tournaments going on
      (lt, ":random_no", 30),
      (store_random_in_range, ":random_town", mainplanets_begin, mainplanets_end),
      (store_random_in_range, ":random_days", 12, 15),
      (party_set_slot, ":random_town", slot_mainplanet_has_tournament, ":random_days"),
      (try_begin),
        (eq, "$cheat_mode", 1),
        (str_store_party_name, s1, ":random_town"),
        (display_message, "@{s1} is holding a tournament."),
      (try_end),
    (try_end),
    ]),

  # Asking to give center to player
  (8,
   [
    (assign, ":done", 0),
    (try_for_range, ":center_no", centers_begin, centers_end),
      (eq, ":done", 0),
      (party_slot_eq, ":center_no", slot_mainplanet_lord, stl_reserved_for_player),
      (assign, "$g_center_to_give_to_player", ":center_no"),
      (try_begin),
        (eq, "$g_center_to_give_to_player", "$g_spacestation_requested_by_player"),
        (assign, "$g_spacestation_requested_by_player", 0),
        (jump_to_menu, "mnu_requested_spacestation_granted_to_player"),
      (else_try),
        (jump_to_menu, "mnu_give_center_to_player"),
      (try_end),
      (assign, ":done", 1),
    (else_try),
      (eq, ":center_no", "$g_spacestation_requested_by_player"),
      (party_slot_ge, ":center_no", slot_mainplanet_lord, faction_heroes_begin),
      (assign, "$g_spacestation_requested_by_player", 0),
      (store_faction_of_party, ":faction", ":center_no"),
      (eq, ":faction", "$players_faction"),
      (assign, "$g_center_to_give_to_player", ":center_no"),
      (jump_to_menu, "mnu_requested_spacestation_granted_to_another"),
      (assign, ":done", 1),
    (try_end),
    ]),
  
  # Taking denars from player while resting in not owned centers
  (1,
   [(neg|map_free),
    (is_currently_night),
    (ge, "$g_last_rest_center", 0),
    (neg|party_slot_eq, "$g_last_rest_center", slot_mainplanet_lord, "trp_player"),
    (store_current_hours, ":cur_hours"),
    (ge, ":cur_hours", "$g_last_rest_payment_until"),
    (store_add, "$g_last_rest_payment_until", ":cur_hours", 24),
    (store_troop_gold, ":gold", "trp_player"),
    (party_get_num_companions, ":num_men", "p_main_party"),
    (store_div, ":total_cost", ":num_men", 4),
    (val_add, ":total_cost", 1),
	#SW - increased cost to rest in towns
	(try_begin),
		(this_or_next|eq,"$g_last_rest_center","p_corellia"),
		(this_or_next|eq,"$g_last_rest_center","p_naboo"),
		(eq,"$g_last_rest_center","p_coruscant"),
		(val_mul, ":total_cost", 3),
	(else_try),
		(val_mul, ":total_cost", 2),
	 (try_end),
	#-----------------------------------------------	
    (try_begin),
      (ge, ":gold", ":total_cost"),
      (display_message, "@You pay for accommodation."),
      (troop_remove_gold, "trp_player", ":total_cost"),
    (else_try),
      (gt, ":gold", 0),
      (troop_remove_gold, "trp_player", ":gold"),
    (try_end),
    ]),
  # Spawn some bandits.
  #SW MF Increased this for patrol effects
  (12,
   [
       (call_script, "script_spawn_bandits"),
    ]),

  # Make parties larger as game progresses.
  (24,
   [
       (call_script, "script_update_party_creation_random_limits"),
    ]),
  
  # Check if a faction is defeated every day
  (24,
   [
    (assign, ":num_active_factions", 0),
    (try_for_range, ":cur_faction", factions_begin, factions_end),
      (faction_set_slot, ":cur_faction", slot_faction_number_of_parties, 0),
    (try_end),
    (try_for_parties, ":cur_party"),
      (store_faction_of_party, ":party_faction", ":cur_party"),
      (is_between, ":party_faction", factions_begin, factions_end),
      (this_or_next|is_between, ":cur_party", centers_begin, centers_end),
      (party_slot_eq, ":cur_party", slot_party_type, spt_faction_hero_party),
      (faction_get_slot, ":faction_num_parties", ":party_faction", slot_faction_number_of_parties),
      (val_add, ":faction_num_parties", 1),
      (faction_set_slot, ":party_faction", slot_faction_number_of_parties, ":faction_num_parties"),
    (try_end),
    (try_for_range, ":cur_faction", factions_begin, factions_end),
##      (try_begin),
##        (eq, "$cheat_mode", 1),
##        (str_store_faction_name, s1, ":cur_faction"),
##        (faction_get_slot, reg1, ":cur_faction", slot_faction_number_of_parties),
##        (display_message, "@Number of parties belonging to {s1}: {reg1}"),
##      (try_end),
      (faction_slot_eq, ":cur_faction", slot_faction_state, sfs_active),
      (val_add, ":num_active_factions", 1),
      (faction_slot_eq, ":cur_faction", slot_faction_number_of_parties, 0),
      (assign, ":faction_removed", 0),
      (try_begin),
        (eq, ":cur_faction", "fac_player_supporters_faction"),
        (try_begin),
          (le, "$supported_pretender", 0),
          (faction_set_slot, ":cur_faction", slot_faction_state, sfs_inactive),
          (assign, ":faction_removed", 1),
        (try_end),
      (else_try),
        (neq, "$players_faction", ":cur_faction"),
        (faction_set_slot, ":cur_faction", slot_faction_state, sfs_defeated),
        (try_for_parties, ":cur_party"),
          (store_faction_of_party, ":party_faction", ":cur_party"),
          (eq, ":party_faction", ":cur_faction"),
          (party_get_slot, ":home_center", ":cur_party", slot_party_home_center),
          (store_faction_of_party, ":home_center_faction", ":home_center"),
          (party_set_faction, ":cur_party", ":home_center_faction"),
        (try_end),
        (assign, ":faction_pretender", -1),
        (try_for_range, ":cur_pretender", pretenders_begin, pretenders_end),
          (troop_slot_eq, ":cur_pretender", slot_troop_original_faction, ":cur_faction"),
          (assign, ":faction_pretender", ":cur_pretender"),
        (try_end),
        (try_begin),
          (is_between, ":faction_pretender", pretenders_begin, pretenders_end),
          (neq, ":faction_pretender", "$supported_pretender"),
          (troop_set_slot, ":faction_pretender", slot_troop_cur_center, 0), #remove pretender from the world
        (try_end),
        (assign, ":faction_removed", 1),
        (try_begin),
          (eq, "$players_oath_renounced_against_faction", ":cur_faction"),
          (assign, "$players_oath_renounced_against_faction", 0),
          (assign, "$players_oath_renounced_given_center", 0),
          (assign, "$players_oath_renounced_begin_time", 0),
          (call_script, "script_add_notification_menu", "mnu_notification_oath_renounced_faction_defeated", ":cur_faction", 0),
        (try_end),
        #This menu must be at the end because faction banner will change after this menu if the player's supported pretender's original faction is cur_faction
        (call_script, "script_add_notification_menu", "mnu_notification_faction_defeated", ":cur_faction", 0),
      (try_end),
      (try_begin),
        (eq, ":faction_removed", 1),
        (val_sub, ":num_active_factions", 1),
        (call_script, "script_store_average_center_value_per_faction"),
      (try_end),
      (try_for_range, ":cur_rebelalliance", factions_begin, factions_end),
        (call_script, "script_update_faction_notes", ":cur_rebelalliance"),
      (try_end),
    (try_end),
    (try_begin),
      (eq, ":num_active_factions", 1),
      (try_for_range, ":cur_faction", factions_begin, factions_end),
        (faction_slot_eq, ":cur_faction", slot_faction_state, sfs_active),
        (call_script, "script_add_notification_menu", "mnu_notification_one_faction_left", ":cur_faction", 0),
      (try_end),
    (try_end),
    ]),

  # Reduce renown slightly by 0.5% every week
  (7 * 24,
   [
       (troop_get_slot, ":player_renown", "trp_player", slot_troop_renown),
       (store_div, ":renown_decrease", ":player_renown", 200),
       (val_sub, ":player_renown", ":renown_decrease"),
       (troop_set_slot, "trp_player", slot_troop_renown, ":player_renown"),
    ]),

  # Read books if player is resting.
  (1, [(neg|map_free),
       (gt, "$g_player_reading_book", 0),
       (player_has_item, "$g_player_reading_book"),
       (store_attribute_level, ":int", "trp_player", ca_intelligence),
       (item_get_slot, ":int_req", "$g_player_reading_book", slot_item_intelligence_requirement),
       (le, ":int_req", ":int"),
       (item_get_slot, ":book_reading_progress", "$g_player_reading_book", slot_item_book_reading_progress),
       (item_get_slot, ":book_read", "$g_player_reading_book", slot_item_book_read),
       (eq, ":book_read", 0),
       #SW - try to increase reading speed of books, book_reading_progress
       #(val_add, ":book_reading_progress", 7),
       (val_add, ":book_reading_progress", 11),
       (item_set_slot, "$g_player_reading_book", slot_item_book_reading_progress, ":book_reading_progress"),
       (ge, ":book_reading_progress", 1000),
       (item_set_slot, "$g_player_reading_book", slot_item_book_read, 1),
       (str_store_item_name, s1, "$g_player_reading_book"),
       (str_clear, s2),
       (try_begin),
         (eq, "$g_player_reading_book", "itm_book_tactics"),
         (troop_raise_skill, "trp_player", "skl_tactics", 1),
         (str_store_string, s2, "@ Your tactics skill has increased by 1."),
       (else_try),
         (eq, "$g_player_reading_book", "itm_book_persuasion"),
         (troop_raise_skill, "trp_player", "skl_persuasion", 1),
         (str_store_string, s2, "@ Your persuasion skill has increased by 1."),
       (else_try),
         (eq, "$g_player_reading_book", "itm_book_leadership"),
         (troop_raise_skill, "trp_player", "skl_leadership", 1),
         (str_store_string, s2, "@ Your leadership skill has increased by 1."),
       (else_try),
         (eq, "$g_player_reading_book", "itm_book_intelligence"),
         (troop_raise_attribute, "trp_player", ca_intelligence, 1),
         (str_store_string, s2, "@ Your intelligence has increased by 1."),
       (else_try),
         (eq, "$g_player_reading_book", "itm_book_trade"),
         (troop_raise_skill, "trp_player", "skl_trade", 1),
         (str_store_string, s2, "@ Your trade skill has increased by 1."),
       (else_try),
         (eq, "$g_player_reading_book", "itm_book_weapon_mastery"),
         (troop_raise_skill, "trp_player", "skl_weapon_master", 1),
         (str_store_string, s2, "@ Your weapon master skill has increased by 1."),
       (else_try),
         (eq, "$g_player_reading_book", "itm_book_engineering"),
         (troop_raise_skill, "trp_player", "skl_engineer", 1),
         (str_store_string, s2, "@ Your engineer skill has increased by 1."),
       (try_end),
       #SW - modified text
       #(dialog_box, "@You have finished reading {s1}.{s2}", "@Book Read"),
       (dialog_box, "@You have finished viewing {s1}.{s2}", "@Book Read"),
       (assign, "$g_player_reading_book", 0),
       ]),

# Removing cattle herds if they are way out of range
  (12, [(try_for_parties, ":cur_party"),
          (party_slot_eq, ":cur_party", slot_party_type, spt_cattle_herd),
          (store_distance_to_party_from_party, ":dist",":cur_party", "p_main_party"),
          (try_begin),
            (gt, ":dist", 30),
            (remove_party, ":cur_party"),
            (try_begin),
              #Fail quest if the party is the quest party
              (check_quest_active, "qst_move_cattle_herd"),
              (neg|check_quest_concluded, "qst_move_cattle_herd"),
              (quest_slot_eq, "qst_move_cattle_herd", slot_quest_target_party, ":cur_party"),
              (call_script, "script_fail_quest", "qst_move_cattle_herd"),
            (end_try),
          (else_try),
            (gt, ":dist", 10),
            (party_set_slot, ":cur_party", slot_cattle_driven_by_player, 0),
            (party_set_ai_behavior, ":cur_party", ai_bhvr_hold),
          (try_end),
        (try_end),
    ]),

  
#####!!!!!

# Village upgrade triggers

# School
  (30 * 24,
   [(try_for_range, ":cur_village", minorplanet_begin, minorplanet_end),
      (party_slot_eq, ":cur_village", slot_mainplanet_lord, "trp_player"),
      (party_get_slot, ":cur_relation", ":cur_village", slot_center_player_relation),
	  # HC - Changed relation increase from from 1 to 3
      (val_add, ":cur_relation", 3),
      (val_min, ":cur_relation", 100),
      (party_set_slot, ":cur_village", slot_center_player_relation, ":cur_relation"),
    (try_end),
    ]),

# Quest triggers:

# Remaining days text update
  (24, [(try_for_range, ":cur_quest", all_quests_begin, all_quests_end),
          (try_begin),
            (check_quest_active, ":cur_quest"),
            (try_begin),
              (neg|check_quest_concluded, ":cur_quest"),
              (quest_slot_ge, ":cur_quest", slot_quest_expiration_days, 1),
              (quest_get_slot, ":exp_days", ":cur_quest", slot_quest_expiration_days),
              (val_sub, ":exp_days", 1),
              (try_begin),
                (eq, ":exp_days", 0),
                (call_script, "script_abort_quest", ":cur_quest", 1),
              (else_try),
                (quest_set_slot, ":cur_quest", slot_quest_expiration_days, ":exp_days"),
                (assign, reg0, ":exp_days"),
                (add_quest_note_from_sreg, ":cur_quest", 7, "@You have {reg0} days to finish this quest.", 0),
              (try_end),
            (try_end),
          (else_try),
            (quest_slot_ge, ":cur_quest", slot_quest_dont_give_again_remaining_days, 1),
            (quest_get_slot, ":value", ":cur_quest", slot_quest_dont_give_again_remaining_days),
            (val_sub, ":value", 1),
            (quest_set_slot, ":cur_quest", slot_quest_dont_give_again_remaining_days, ":value"),
          (try_end),
        (try_end),
    ]),

# Report to army quest
  (6,
   [
     (is_between, "$players_faction", factions_begin, factions_end),
     (eq, "$g_player_is_captive", 0),
     (neg|faction_slot_eq, "$players_faction", slot_faction_ai_state, sfai_default),
     (neg|check_quest_active, "qst_report_to_army"),
     (neg|check_quest_active, "qst_follow_army"),
     (neg|quest_slot_ge, "qst_report_to_army", slot_quest_dont_give_again_remaining_days, 1),
     (faction_get_slot, ":faction_marshall", "$players_faction", slot_faction_marshall),
     (gt, ":faction_marshall", 0),
     (troop_get_slot, ":faction_marshall_party", ":faction_marshall", slot_troop_leaded_party),
     (gt, ":faction_marshall_party", 0),
     (assign, ":has_no_quests", 1),
     (try_for_range, ":cur_quest", lord_quests_begin, lord_quests_end),
       (check_quest_active, ":cur_quest"),
       (quest_slot_eq, ":cur_quest", slot_quest_giver_troop, ":faction_marshall"),
       (assign, ":has_no_quests", 0),
     (try_end),
     (eq, ":has_no_quests", 1),
     (try_for_range, ":cur_quest", army_quests_begin, army_quests_end),
       (check_quest_active, ":cur_quest"),
       (assign, ":has_no_quests", 0),
     (try_end),
     (eq, ":has_no_quests", 1),
     (store_character_level, ":level", "trp_player"),
     (ge, ":level", 8),
     (assign, ":cur_target_amount", 2),
     (try_for_range, ":cur_center", centers_begin, centers_end),
       (party_slot_eq, ":cur_center", slot_mainplanet_lord, "trp_player"),
       (try_begin),
         (party_slot_eq, ":cur_center", slot_party_type, spt_mainplanet),
         (val_add, ":cur_target_amount", 3),
       (else_try),
         (party_slot_eq, ":cur_center", slot_party_type, spt_castle),
         (val_add, ":cur_target_amount", 1),
       (else_try),
         (val_add, ":cur_target_amount", 1),
       (try_end),
     (try_end),
     (val_mul, ":cur_target_amount", 4),
     (val_min, ":cur_target_amount", 60),
     (quest_set_slot, "qst_report_to_army", slot_quest_giver_troop, ":faction_marshall"),
     (quest_set_slot, "qst_report_to_army", slot_quest_target_troop, ":faction_marshall"),
     (quest_set_slot, "qst_report_to_army", slot_quest_target_amount, ":cur_target_amount"),
     (quest_set_slot, "qst_report_to_army", slot_quest_expiration_days, 4),
     (quest_set_slot, "qst_report_to_army", slot_quest_dont_give_again_period, 28),
     (jump_to_menu, "mnu_faction_army_quest_report_to_army"),
     ]),


# Army quest initializer
  (3,
   [
     (assign, "$g_random_army_quest", -1),
     (check_quest_active, "qst_follow_army", 1),
     (is_between, "$players_faction", factions_begin, factions_end),
#Rebellion changes begin
#     (neg|is_between, "$players_faction", rebel_factions_begin, rebel_factions_end),
#Rebellion changes end
     (neg|faction_slot_eq, "$players_faction", slot_faction_ai_state, sfai_default),
     (faction_get_slot, ":faction_marshall", "$players_faction", slot_faction_marshall),
     (neq, ":faction_marshall", "trp_player"),
     (gt, ":faction_marshall", 0),
     (troop_get_slot, ":faction_marshall_party", ":faction_marshall", slot_troop_leaded_party),
     (gt, ":faction_marshall_party", 0),
     (store_distance_to_party_from_party, ":dist", ":faction_marshall_party", "p_main_party"),
     (try_begin),
       (lt, ":dist", 15),
       (assign, "$g_player_follow_army_warnings", 0),
       (store_current_hours, ":cur_hours"),
       (faction_get_slot, ":last_offensive_time", "$players_faction", slot_faction_ai_last_offensive_time),
       (store_sub, ":passed_time", ":cur_hours", ":last_offensive_time"),

       (assign, ":result", -1),
       (try_begin),
         (store_random_in_range, ":random_no", 0, 100),
         (lt, ":random_no", 30),
         (troop_slot_eq, ":faction_marshall", slot_troop_does_not_give_quest, 0),
         (try_for_range, ":unused", 0, 20), #Repeat trial twenty times
           (eq, ":result", -1),
           (store_random_in_range, ":quest_no", army_quests_begin, army_quests_end),
           (neg|quest_slot_ge, ":quest_no", slot_quest_dont_give_again_remaining_days, 1),
           (try_begin),
             (eq, ":quest_no", "qst_deliver_cattle_to_army"),
             (try_begin),
               (faction_slot_eq, "$players_faction", slot_faction_ai_state, sfai_attacking_center),
               (gt, ":passed_time", 120),#5 days
               (store_random_in_range, ":quest_target_amount", 5, 10),
               (assign, ":result", ":quest_no"),
               (quest_set_slot, ":result", slot_quest_target_amount, ":quest_target_amount"),
               (quest_set_slot, ":result", slot_quest_expiration_days, 10),
               (quest_set_slot, ":result", slot_quest_dont_give_again_period, 30),
             (try_end),
           (else_try),
             (eq, ":quest_no", "qst_join_siege_with_army"),
             (try_begin),
               (faction_slot_eq, "$players_faction", slot_faction_ai_state, sfai_attacking_center),
               (faction_get_slot, ":ai_object", "$players_faction", slot_faction_ai_object),
               (is_between, ":ai_object", walled_centers_begin, walled_centers_end),
               (party_get_battle_opponent, ":besieged_center", ":faction_marshall_party"),
               (eq, ":besieged_center", ":ai_object"),
               #army is assaulting the center
               (assign, ":result", ":quest_no"),
               (quest_set_slot, ":result", slot_quest_target_center, ":ai_object"),
               (quest_set_slot, ":result", slot_quest_expiration_days, 2),
               (quest_set_slot, ":result", slot_quest_dont_give_again_period, 15),
             (try_end),
           (else_try),
             (eq, ":quest_no", "qst_scout_waypoints"),
             (try_begin),
               (assign, ":end_cond", 100),
               (assign, "$qst_scout_waypoints_wp_1", -1),
               (assign, "$qst_scout_waypoints_wp_2", -1),
               (assign, "$qst_scout_waypoints_wp_3", -1),
               (assign, ":continue", 0),
               (try_for_range, ":unused", 0, ":end_cond"),
                 (try_begin),
                   (lt, "$qst_scout_waypoints_wp_1", 0),
                   (call_script, "script_cf_get_random_enemy_center_within_range", ":faction_marshall_party", 50),
                   (assign, "$qst_scout_waypoints_wp_1", reg0),
                 (try_end),
                 (try_begin),
                   (lt, "$qst_scout_waypoints_wp_2", 0),
                   (call_script, "script_cf_get_random_enemy_center_within_range", ":faction_marshall_party", 50),
                   (neq, "$qst_scout_waypoints_wp_1", reg0),
                   (assign, "$qst_scout_waypoints_wp_2", reg0),
                 (try_end),
                 (try_begin),
                   (lt, "$qst_scout_waypoints_wp_3", 0),
                   (call_script, "script_cf_get_random_enemy_center_within_range", ":faction_marshall_party", 50),
                   (neq, "$qst_scout_waypoints_wp_1", reg0),
                   (neq, "$qst_scout_waypoints_wp_2", reg0),
                   (assign, "$qst_scout_waypoints_wp_3", reg0),
                 (try_end),
                 (neq, "$qst_scout_waypoints_wp_1", "$qst_scout_waypoints_wp_2"),
                 (neq, "$qst_scout_waypoints_wp_1", "$qst_scout_waypoints_wp_2"),
                 (neq, "$qst_scout_waypoints_wp_2", "$qst_scout_waypoints_wp_3"),
                 (ge, "$qst_scout_waypoints_wp_1", 0),
                 (ge, "$qst_scout_waypoints_wp_2", 0),
                 (ge, "$qst_scout_waypoints_wp_3", 0),
                 (assign, ":end_cond", 0),
                 (assign, ":continue", 1),
               (try_end),
               (eq, ":continue", 1),
               (assign, "$qst_scout_waypoints_wp_1_visited", 0),
               (assign, "$qst_scout_waypoints_wp_2_visited", 0),
               (assign, "$qst_scout_waypoints_wp_3_visited", 0),
               (assign, ":result", ":quest_no"),
               (quest_set_slot, ":result", slot_quest_expiration_days, 7),
               (quest_set_slot, ":result", slot_quest_dont_give_again_period, 25),
             (try_end),
           (try_end),
         (try_end),
         (try_begin),
           (neq, ":result", -1),
           (quest_set_slot, ":result", slot_quest_current_state, 0),
           (quest_set_slot, ":result", slot_quest_giver_troop, ":faction_marshall"),
           (try_begin),
             (eq, ":result", "qst_join_siege_with_army"),
             (jump_to_menu, "mnu_faction_army_quest_join_siege_order"),
           (else_try),
             (assign, "$g_random_army_quest", ":result"),
             (quest_set_slot, "$g_random_army_quest", slot_quest_giver_troop, ":faction_marshall"),
             (jump_to_menu, "mnu_faction_army_quest_messenger"),
           (try_end),
         (try_end),
       (try_end),
     (else_try),
       (val_add, "$g_player_follow_army_warnings", 1),
       (try_begin),
         (lt, "$g_player_follow_army_warnings", 12),
         (try_begin),
           (store_mod, ":follow_mod", "$g_player_follow_army_warnings", 4),
           (eq, ":follow_mod", 0),
           (str_store_troop_name_link, s1, ":faction_marshall"),
           (try_begin),
             (lt, "$g_player_follow_army_warnings", 8),
             (display_message, "@You must follow {s1}!", color_quest_and_faction_news),
           (else_try),
             (display_message, "@You must follow {s1}! This is your last warning!", color_terrible_news),
           (try_end),
         (try_end),
       (else_try),
         (jump_to_menu, "mnu_faction_army_follow_failed"),
       (try_end),
     (try_end),
    ]),

# Move cattle herd
  (0.5, [(check_quest_active,"qst_move_cattle_herd"),
         (neg|check_quest_concluded,"qst_move_cattle_herd"),
         (quest_get_slot, ":target_party", "qst_move_cattle_herd", slot_quest_target_party),
         (quest_get_slot, ":target_center", "qst_move_cattle_herd", slot_quest_target_center),
         (store_distance_to_party_from_party, ":dist",":target_party", ":target_center"),
         (lt, ":dist", 3),
         (remove_party, ":target_party"),
         (call_script, "script_succeed_quest", "qst_move_cattle_herd"),
    ]),

  (2, [
       (try_for_range, ":troop_no", faction_heroes_begin, faction_heroes_end),
         (troop_get_slot, ":party_no", ":troop_no", slot_troop_leaded_party),
         (ge, ":party_no", 1),
         (party_slot_eq, ":party_no", slot_party_following_player, 1),
         (store_current_hours, ":cur_time"),
         (neg|party_slot_ge, ":party_no", slot_party_follow_player_until_time, ":cur_time"),
         (party_set_slot, ":party_no", slot_party_commander_party, -1),
         (party_set_slot, ":party_no", slot_party_following_player, 0),
         (assign,  ":dont_follow_period", 200),
         (store_add, ":dont_follow_time", ":cur_time", ":dont_follow_period"),
         (party_set_slot, ":party_no", slot_party_dont_follow_player_until_time,  ":dont_follow_time"),
       (try_end),
    ]),

# Deliver cattle and deliver cattle to army
  (0.5,
   [
     (try_begin),
       (check_quest_active,"qst_deliver_cattle"),
       (neg|check_quest_succeeded, "qst_deliver_cattle"),
       (quest_get_slot, ":target_center", "qst_deliver_cattle", slot_quest_target_center),
       (quest_get_slot, ":target_amount", "qst_deliver_cattle", slot_quest_target_amount),
       (quest_get_slot, ":cur_amount", "qst_deliver_cattle", slot_quest_current_state),
       (store_sub, ":left_amount", ":target_amount", ":cur_amount"),
       (call_script, "script_remove_cattles_if_herd_is_close_to_party", ":target_center", ":left_amount"),
       (val_add, ":cur_amount", reg0),
       (quest_set_slot, "qst_deliver_cattle", slot_quest_current_state, ":cur_amount"),
       (le, ":target_amount", ":cur_amount"),
       (call_script, "script_succeed_quest", "qst_deliver_cattle"),
     (try_end),
     (try_begin),
       (check_quest_active, "qst_deliver_cattle_to_army"),
       (neg|check_quest_succeeded, "qst_deliver_cattle_to_army"),
       (quest_get_slot, ":giver_troop", "qst_deliver_cattle_to_army", slot_quest_giver_troop),
       (troop_get_slot, ":target_party", ":giver_troop", slot_troop_leaded_party),
       (try_begin),
         (gt, ":target_party", 0),
         (quest_get_slot, ":target_amount", "qst_deliver_cattle_to_army", slot_quest_target_amount),
         (quest_get_slot, ":cur_amount", "qst_deliver_cattle_to_army", slot_quest_current_state),
         (store_sub, ":left_amount", ":target_amount", ":cur_amount"),
         (call_script, "script_remove_cattles_if_herd_is_close_to_party", ":target_party", ":left_amount"),
         (val_add, ":cur_amount", reg0),
         (quest_set_slot, "qst_deliver_cattle_to_army", slot_quest_current_state, ":cur_amount"),
         (try_begin),
           (le, ":target_amount", ":cur_amount"),
           (call_script, "script_succeed_quest", "qst_deliver_cattle_to_army"),
         (try_end),
       (else_try),
         (call_script, "script_abort_quest", "qst_deliver_cattle_to_army", 0),
       (try_end),
     (try_end),
     ]),

# Train peasants against bandits
  (1,
   [
     (neg|map_free),
     (check_quest_active, "qst_train_peasants_against_bandits"),
     (neg|check_quest_concluded, "qst_train_peasants_against_bandits"),
     (eq, "$qst_train_peasants_against_bandits_currently_training", 1),
     (val_add, "$qst_train_peasants_against_bandits_num_hours_trained", 1),
     (call_script, "script_get_max_skill_of_player_party", "skl_trainer"),
     (assign, ":trainer_skill", reg0),
     (store_sub, ":needed_hours", 20, ":trainer_skill"),
     (val_mul, ":needed_hours", 3),
     (val_div, ":needed_hours", 5),
     (ge, "$qst_train_peasants_against_bandits_num_hours_trained", ":needed_hours"),
     (assign, "$qst_train_peasants_against_bandits_num_hours_trained", 0),
     (rest_for_hours, 0, 0, 0), #stop resting
     (jump_to_menu, "mnu_train_peasants_against_bandits_ready"),
     ]),

# Scout waypoints
  (1,
   [
     (check_quest_active,"qst_scout_waypoints"),
     (neg|check_quest_succeeded, "qst_scout_waypoints"),
     (try_begin),
       (eq, "$qst_scout_waypoints_wp_1_visited", 0),
       (store_distance_to_party_from_party, ":distance", "$qst_scout_waypoints_wp_1", "p_main_party"),
       (le, ":distance", 3),
       (assign, "$qst_scout_waypoints_wp_1_visited", 1),
       (str_store_party_name_link, s1, "$qst_scout_waypoints_wp_1"),
       (display_message, "@{s1} is scouted.", color_quest_and_faction_news),
     (try_end),
     (try_begin),
       (eq, "$qst_scout_waypoints_wp_2_visited", 0),
       (store_distance_to_party_from_party, ":distance", "$qst_scout_waypoints_wp_2", "p_main_party"),
       (le, ":distance", 3),
       (assign, "$qst_scout_waypoints_wp_2_visited", 1),
       (str_store_party_name_link, s1, "$qst_scout_waypoints_wp_2"),
       (display_message, "@{s1} is scouted.", color_quest_and_faction_news),
     (try_end),
     (try_begin),
       (eq, "$qst_scout_waypoints_wp_3_visited", 0),
       (store_distance_to_party_from_party, ":distance", "$qst_scout_waypoints_wp_3", "p_main_party"),
       (le, ":distance", 3),
       (assign, "$qst_scout_waypoints_wp_3_visited", 1),
       (str_store_party_name_link, s1, "$qst_scout_waypoints_wp_3"),
       (display_message, "@{s1} is scouted.", color_quest_and_faction_news),
     (try_end),
     (eq, "$qst_scout_waypoints_wp_1_visited", 1),
     (eq, "$qst_scout_waypoints_wp_2_visited", 1),
     (eq, "$qst_scout_waypoints_wp_3_visited", 1),
     (call_script, "script_succeed_quest", "qst_scout_waypoints"),
     ]),
  
# Kill local merchant
  
  (3, [(neg|map_free),
       (check_quest_active, "qst_kill_local_merchant"),
       (quest_slot_eq, "qst_kill_local_merchant", slot_quest_current_state, 0),
       (quest_set_slot, "qst_kill_local_merchant", slot_quest_current_state, 1),
       (rest_for_hours, 0, 0, 0), #stop resting
       (assign, "$auto_enter_town", "$qst_kill_local_merchant_center"),
       (assign, "$quest_auto_menu", "mnu_kill_local_merchant_begin"),
       ]),

# Collect taxes
  (1, [(neg|map_free),
       (check_quest_active, "qst_collect_taxes"),
       (eq, "$g_player_is_captive", 0),
       (eq, "$qst_collect_taxes_currently_collecting", 1),
       (quest_get_slot, ":quest_current_state", "qst_collect_taxes", slot_quest_current_state),
       (this_or_next|eq, ":quest_current_state", 1),
       (this_or_next|eq, ":quest_current_state", 2),
       (eq, ":quest_current_state", 3),
       (quest_get_slot, ":left_hours", "qst_collect_taxes", slot_quest_target_amount),
       (val_sub, ":left_hours", 1),
       (quest_set_slot, "qst_collect_taxes", slot_quest_target_amount, ":left_hours"),
       (call_script, "script_get_max_skill_of_player_party", "skl_trade"),
       
       (try_begin),
         (lt, ":left_hours", 0),
         (assign, ":quest_current_state", 4),
         (quest_set_slot, "qst_collect_taxes", slot_quest_current_state, 4),
         (rest_for_hours, 0, 0, 0), #stop resting
         (jump_to_menu, "mnu_collect_taxes_complete"),
       (else_try),
         #Continue collecting taxes
         (assign, ":max_collected_tax", "$qst_collect_taxes_hourly_income"),
         (party_get_slot, ":prosperity", "$g_encountered_party", slot_mainplanet_prosperity),
         (store_add, ":multiplier", 30, ":prosperity"),
         (val_mul, ":max_collected_tax", ":multiplier"),
         (val_div, ":max_collected_tax", 80),#Prosperity of 50 gives the default values
       
         (try_begin),
           (eq, "$qst_collect_taxes_halve_taxes", 1),
           (val_div, ":max_collected_tax", 2),
         (try_end),
         (val_max, ":max_collected_tax", 2),
         (store_random_in_range, ":collected_tax", 1, ":max_collected_tax"),
         (quest_get_slot, ":cur_collected", "qst_collect_taxes", slot_quest_gold_reward),
         (val_add, ":cur_collected", ":collected_tax"),
         (quest_set_slot, "qst_collect_taxes", slot_quest_gold_reward, ":cur_collected"),
         (call_script, "script_troop_add_gold", "trp_player", ":collected_tax"),
       (try_end),
       (try_begin),
         (eq, ":quest_current_state", 1),
         (val_sub, "$qst_collect_taxes_menu_counter", 1),
         (le, "$qst_collect_taxes_menu_counter", 0),
         (quest_set_slot, "qst_collect_taxes", slot_quest_current_state, 2),
         (jump_to_menu, "mnu_collect_taxes_revolt_warning"),
       (else_try), #Chance of revolt against player
         (eq, ":quest_current_state", 2),
         (val_sub, "$qst_collect_taxes_unrest_counter", 1),
         (le, "$qst_collect_taxes_unrest_counter", 0),
         (eq, "$qst_collect_taxes_halve_taxes", 0),
         (quest_set_slot, "qst_collect_taxes", slot_quest_current_state, 3),

         (store_div, ":unrest_chance", 10000, "$qst_collect_taxes_total_hours"),
         (val_add, ":unrest_chance",30),
       
         (store_random_in_range, ":unrest_roll", 0, 1000),
         (try_begin),
           (lt, ":unrest_roll", ":unrest_chance"),
           (jump_to_menu, "mnu_collect_taxes_revolt"),
         (try_end),
       (try_end),
       ]),


#persuade_lords_to_make_peace begin

  (72, [(gt, "$g_force_peace_galacticempire", 0),
        (gt, "$g_force_peace_rebelalliance", 0),
        (try_begin),
          (store_relation, ":relation", "$g_force_peace_galacticempire", "$g_force_peace_rebelalliance"),
          (lt, ":relation", 0),
          (call_script, "script_diplomacy_start_peace_between_factions", "$g_force_peace_galacticempire", "$g_force_peace_rebelalliance", 1),
        (try_end),
        (assign, "$g_force_peace_galacticempire", 0),
        (assign, "$g_force_peace_rebelalliance", 0),
       ]),  



#NPC changes begin

(1, 
   [
#Resolve one issue each hour
        (try_begin),
### Here do NPC that is quitting
         # HC - don't allow companions to quit - http://forums.taleworlds.net/index.php/topic,68851.0.html
         (eq, "$disable_npc_complaints", 0),
            (gt, "$npc_is_quitting", 0),
            (try_begin),
                (main_party_has_troop, "$npc_is_quitting"),
                (neq, "$g_player_is_captive", 1),

                (start_map_conversation, "$npc_is_quitting"),
            (else_try),
                (assign, "$npc_is_quitting", 0),
            (try_end),

        (else_try),
#### Grievance
            (gt, "$npc_with_grievance", 0),
            (eq, "$disable_npc_complaints", 0),
            (try_begin),
                (main_party_has_troop, "$npc_with_grievance"),
                (neq, "$g_player_is_captive", 1),

                (assign, "$npc_map_talk_context", slot_troop_morality_state),
                (start_map_conversation, "$npc_with_grievance"),
            (else_try),
                (assign, "$npc_with_grievance", 0),
            (try_end),
        (else_try),
            (gt, "$npc_with_personality_clash", 0),
            (eq, "$disable_npc_complaints", 0),
            (troop_get_slot, ":object", "$npc_with_personality_clash", slot_troop_personalityclash_object),
            (try_begin),
                (main_party_has_troop, "$npc_with_personality_clash"),
                (main_party_has_troop, ":object"),
                (neq, "$g_player_is_captive", 1),
                (assign, "$npc_map_talk_context", slot_troop_personalityclash_state),
                (start_map_conversation, "$npc_with_personality_clash"),
            (else_try),
                (assign, "$npc_with_personality_clash", 0),
            (try_end),
        (else_try), ###check for regional background
            (eq, "$disable_local_histories", 0),
            (try_for_range, ":npc", companions_begin, companions_end),
                (main_party_has_troop, ":npc"),           
                (troop_slot_eq, ":npc", slot_troop_home_speech_delivered, 0),
#                (eq, "$npc_map_talk_context", 0),
                (troop_get_slot, ":home", ":npc", slot_troop_home),
                (gt, ":home", 0),
                (store_distance_to_party_from_party, ":distance", ":home", "p_main_party"),
                (lt, ":distance", 7),                
                (assign, "$npc_map_talk_context", slot_troop_home),
                (start_map_conversation, ":npc"),
            (try_end),
        (try_end),

]),
#NPC changes end

##(1, 
##   [(store_random_in_range, ":random_troop", faction_heroes_begin, faction_heroes_end),
##    (store_random_in_range, ":random_faction", factions_begin, factions_end),
##    (store_troop_faction, ":troop_faction", ":random_troop"),
##    (neq, ":troop_faction", ":random_faction"),
##    (faction_slot_eq, ":random_faction", slot_faction_state, sfs_active),
##    (troop_set_slot, ":random_troop", slot_troop_change_to_faction, ":random_faction"),
##    (str_store_troop_name, s1, ":random_troop"),
##    (str_store_faction_name, s2, ":troop_faction"),
##    (str_store_faction_name, s3, ":random_faction"),
##    (display_message, "@{s1} is willing to switch from {s2} to {s3}."),
##    ]),

(4, 
   [(try_for_range, ":troop_no", faction_heroes_begin, faction_heroes_end),
      (troop_slot_ge, ":troop_no", slot_troop_change_to_faction, 1),
      (store_troop_faction, ":faction_no", ":troop_no"),
      (troop_get_slot, ":new_faction_no", ":troop_no", slot_troop_change_to_faction),
      (troop_get_slot, ":party_no", ":troop_no", slot_troop_leaded_party),
      (assign, ":continue", 0),
      (try_begin),
        (le, ":party_no", 0),
        #(troop_slot_eq, ":troop_no", slot_troop_is_prisoner, 0),
        (neg|troop_slot_ge, ":troop_no", slot_troop_prisoner_of_party, 0),
        (assign, ":continue", 1),
      (else_try),
        (gt, ":party_no", 0),

        #checking if the party is outside the centers
        (party_get_attached_to, ":cur_center_no", ":party_no"),
        (try_begin),
          (lt, ":cur_center_no", 0),
          (party_get_cur_town, ":cur_center_no", ":party_no"),
        (try_end),
        (this_or_next|neg|is_between, ":cur_center_no", centers_begin, centers_end),
        (party_slot_eq, ":cur_center_no", slot_mainplanet_lord, ":troop_no"),
    
        #checking if the party is away from his original faction parties
        (assign, ":end_cond", faction_heroes_end),
        (try_for_range, ":enemy_troop_no", faction_heroes_begin, ":end_cond"),
          (troop_get_slot, ":enemy_party_no", ":enemy_troop_no", slot_troop_leaded_party),
          (gt, ":enemy_party_no", 0),
          (store_faction_of_party, ":enemy_faction_no", ":enemy_party_no"),
          (eq, ":enemy_faction_no", ":faction_no"),
          (store_distance_to_party_from_party, ":dist", ":party_no", ":enemy_party_no"),
          (lt, ":dist", 4),
          (assign, ":end_cond", 0),
        (try_end),
        (neq, ":end_cond", 0),
        (assign, ":continue", 1),
      (try_end),
      (eq, ":continue", 1),
      (call_script, "script_change_troop_faction", ":troop_no", ":new_faction_no"),
      (troop_set_slot, ":troop_no", slot_troop_change_to_faction, 0),
      (try_begin),
        (is_between, ":new_faction_no", factions_begin, factions_end),
        (str_store_troop_name_link, s1, ":troop_no"),
        (str_store_faction_name_link, s2, ":faction_no"),
        (str_store_faction_name_link, s3, ":new_faction_no"),
        (display_message, "@{s1} has switched from {s2} to {s3}.", color_hero_news),
        (try_begin),
          (eq, ":faction_no", "$players_faction"),
          (call_script, "script_add_notification_menu", "mnu_notification_troop_left_players_faction", ":troop_no", ":new_faction_no"),
        (else_try),
          (eq, ":new_faction_no", "$players_faction"),
          (call_script, "script_add_notification_menu", "mnu_notification_troop_joined_players_faction", ":troop_no", ":faction_no"),
        (try_end),
      (try_end),
    (try_end),
#SW - had to add for new trigger below
    ]),
#    ]),

#  #SW - make sure faction1 (empire) and faction2 (rebel) are always at war (popup appears every time unfortunately, even if they are at war)
#  (24,
#   [
#     (call_script, "script_diplomacy_start_war_between_factions", "fac_galacticempire", "fac_rebelalliance",1),
#    ])

#Run spawn script for parties who have a patrol base.
(8, [	(eq, "$total_init_done", 1),
		#(display_message,"@running spawn trigger"),
		(try_for_range, ":cur_base", walled_centers_begin, walled_centers_end),
			  (party_get_slot, ":base_lvl", ":cur_base", slot_center_has_patrol),
			  # (assign, reg1, ":base_lvl"),
			  # (display_message, "@base lvl is {reg1}"),
			  (is_between, ":base_lvl", 1, 4),
			  # don't spawn patrol for towns that are under siege
			  #(party_get_slot, ":siege_state", ":cur_base", slot_minorplanet_state),	#stage is always zero for player sieges (bug), use slot_center_is_besieged_by as a workaround
			  #(neq, ":siege_state", svs_under_siege),
			  (party_get_slot, ":besieger_party", ":cur_base", slot_center_is_besieged_by),
			  (lt, ":besieger_party", 0), #town is not under siege
			  (call_script, "script_patrol_base_spawn_patrols", ":cur_base"),
		(try_end),
		  ]),

#SW - every 1 hour, destroy all patrols or trade federation convoys that have zero troops
(1, [

#SW - commenting out to try and fix random crashes, but leaving trigger so it will still be 0.9.0.1 saved game compatible

	# (try_for_parties,":cur_party"), #go through all parties to find patrols
		# (party_get_template_id,":cur_party_template",":cur_party"),
		# (this_or_next|eq, ":cur_party_template", "pt_galacticempire_escort"),	#patrol
		# (eq, ":cur_party_template", "pt_independent_traders"),
		# (party_get_num_companions,":num_troops",":cur_party"),
		# (try_begin),
			# (le, ":num_troops", 0),
			# #(party_clear, ":cur_party"),		#probably not necessary and may introduce issues?
			# (remove_party, ":cur_party"),
		# (try_end),
	# (try_end),
	
	]),		  
		  
#SW - every 6 hours, destroy all patrols that are not of the same faction as their home base, are from a base that is under siege
(6, [

#SW - 	this trigger below originally removed parties, which appeared to cause random crashes in 0.9.0 because a part could be removed while engaged in battle
#		I have attempted to fix this by switching the icon/troops of the party if its not correct and not removing patrols if the planet is under siege

			(try_for_range, ":cur_base", walled_centers_begin, walled_centers_end),
				(party_get_slot, ":base_lvl", ":cur_base", slot_center_has_patrol),
				(is_between, ":base_lvl", 1, 4),
				(store_faction_of_party, ":cur_base_faction", ":cur_base"),
				#(party_get_slot, ":siege_state", ":cur_base", slot_minorplanet_state),	#state is always zero for player sieges, use slot_center_is_besieged_by as a workaround
				(party_get_slot, ":besieger_party", ":cur_base", slot_center_is_besieged_by),
				(try_for_parties,":cur_patrol"), #go through all parties to find patrols
					(party_get_template_id,":cur_party_template",":cur_patrol"),
					(eq, ":cur_party_template", "pt_galacticempire_escort"),
					(party_slot_eq, ":cur_patrol", slot_party_home_center, ":cur_base"),
					(store_faction_of_party, ":cur_patrol_faction", ":cur_patrol"),
					#(assign, reg1, ":cur_base"),		#test
					#(assign, reg2, ":cur_base_faction"),	#test					
					#(assign, reg3, ":cur_patrol"),			#test
					#(assign, reg4, ":cur_patrol_faction"),	#test
					#(display_log_message,"@Base = {reg1}, Base Faction = {reg2}, Patrol = {reg3}, Patrol Faction = {reg4}"),	#test
					#(party_get_num_companions,":num_troops",":cur_patrol"),
					(try_begin),
						(neq, ":cur_base_faction",":cur_patrol_faction"),
						#(display_log_message,"@ERROR: Patrol Faction does not match Base Faction!"),	#test
						# They are not the same, destroy the party so it can be re-created by the simple trigger
						#(call_script, "script_clear_party_group", ":cur_patrol"),
						#(party_detach, ":cur_patrol"),		#maybe not necessary, I got an in-game script error? maybe I need to check if they are active or in battle?
						#(party_clear, ":cur_patrol"),	#probably not necessary and may introduce issues?
						
						#SW - commented out this code since it could case crashes in 0.9.0 if a party in battle was removed
						#(remove_party, ":cur_patrol"),
						
						#SW - adding new code to switch the faction, icon, and troops
						#set faction
						(party_set_faction, ":cur_patrol", ":cur_base_faction"),
						#set icon
						(try_begin),
							(eq, ":cur_base_faction", "fac_galacticempire"),	#empire
							(party_set_icon, ":cur_patrol", "icon_tie_fighter"),
						(else_try),
							(eq, ":cur_base_faction", "fac_galacticempire"),	#rebel
							(party_set_icon, ":cur_patrol", "icon_a_wing"),
						(else_try),
							(eq, ":cur_base_faction", "fac_galacticempire"),	#hutt
							(party_set_icon, ":cur_patrol", "icon_hutt_patrol"),
						(else_try),
							#other
							(party_set_icon, ":cur_patrol", "icon_z95"),
						(try_end),
						#remove troops that don't belong to that faction
						(faction_get_slot, ":faction_trp_1", ":cur_base_faction", slot_faction_patrol_unit_1),
						(faction_get_slot, ":faction_trp_2", ":cur_base_faction", slot_faction_patrol_unit_2),
						(faction_get_slot, ":faction_trp_3", ":cur_base_faction", slot_faction_patrol_unit_3),
						(display_message, "@running party_clear"),	#debug
						#clear the troops
						(party_clear, ":cur_patrol"),
						#add party members
						(try_begin),
							(eq, ":base_lvl", 1),
							(party_add_members,":cur_patrol",":faction_trp_1",15),
							(party_add_members,":cur_patrol",":faction_trp_2",5),				
			#				(display_message, "@added units lvl 1"),
						(else_try),
							(eq, ":base_lvl", 2),
							(party_add_members,":cur_patrol",":faction_trp_1",20),
							(party_add_members,":cur_patrol",":faction_trp_2",10),
							(party_add_members,":cur_patrol",":faction_trp_3",5),				
			#				(display_message, "@added units lvl 2"),
						(else_try),
							(eq, ":base_lvl", 3),
							(party_add_members,":cur_patrol",":faction_trp_1",25),
							(party_add_members,":cur_patrol",":faction_trp_2",15),
							(party_add_members,":cur_patrol",":faction_trp_3",10),				
			#				(display_message, "@added units lvl 3"),
						(try_end),
					(try_end),
					#SW - Check if the planet is under siege and destroy parties? probably not necessary
					(try_begin),	#siege
						#(eq, ":siege_state", svs_under_siege),	#state is always zero for player sieges, use slot_center_is_besieged_by as a workaround
						(ge, ":besieger_party", 0), #town is under siege
						
						# (assign, reg1, ":cur_base"),		#test
						# (assign, reg2, ":base_state"),	#test	
						# (assign, reg3, ":besieger_party"),	#test
						# (display_log_message,"@Base = {reg1}, State = {reg2}, Besieger Party = {reg3}"),						
						#(display_message, "@Base {reg1} is under siege, destroy patrol!!!"),
						
						#(call_script, "script_clear_party_group", ":cur_patrol"),
						#(party_detach, ":cur_patrol"),		#maybe not necessary, I got an in-game script error? maybe I need to check if they are active or in battle?
						#(party_clear, ":cur_patrol"),		#probably not necessary and may introduce issues?
						
						#SW - commented out this line since it seemed to cause random crashes in 0.9.0.1...
						#(remove_party, ":cur_patrol"),
						
					#remove parties with zero members as a safety? (switched to a separate trigger every hours)
					# (else_try),
						# (le, ":num_troops", 0),
						# (party_clear, ":cur_patrol"),
						# (remove_party, ":cur_patrol"),						
					(try_end),										
					# #remove troops that don't belong to that faction
					# (faction_get_slot, ":faction_trp_1", ":cur_base_faction", slot_faction_patrol_unit_1),
					# (faction_get_slot, ":faction_trp_2", ":cur_base_faction", slot_faction_patrol_unit_2),
					# (faction_get_slot, ":faction_trp_3", ":cur_base_faction", slot_faction_patrol_unit_3),
					# (try_begin),
						# (party_get_num_companions,":num_troops",":cur_patrol"),
						# (gt, ":num_troops", 0),
						# (party_get_num_companion_stacks, ":num_stacks",":cur_patrol"),
						# (try_for_range_backwards, ":i_stack", 0, ":num_stacks"),
							# (party_stack_get_troop_id, ":temp_id", ":cur_patrol", ":i_stack"),
							# (try_begin),
								# (this_or_next|eq, ":faction_trp_1", ":temp_id"),
								# (this_or_next|eq, ":faction_trp_2", ":temp_id"),
								# (             eq, ":faction_trp_3", ":temp_id"),
							# (else_try),
								# (party_stack_get_size, ":stack_size",":cur_patrol",":i_stack"),
								# (party_remove_members,":cur_patrol",":temp_id",":stack_size"),
						# #		(assign, reg24, ":temp_id"),
						# #		(assign, reg25, ":stack_size"),
						# #		(display_message, "@units removed: {reg25} x unit {reg24}"),
							# (try_end),
						# (try_end),
					# (try_end),
				(try_end),
			(try_end),
			
	]),

(1, [
	  (eq, "$total_init_done", 0),
	  (call_script, "script_init_patrol_faction_settings"),
	  (call_script, "script_init_patrol_bases"),
	  (call_script, "script_init_patrol_faction_settings"),
	  (assign, "$total_init_done", 1),
	  ]),
#trigger for patrol processing

(0.5,	[
	(try_for_parties, ":cur_patrol"),
		(party_get_template_id,":cur_party_template",":cur_patrol"),
		(eq, ":cur_party_template", "pt_galacticempire_escort"),
		(call_script, "script_process_patrol_ai", ":cur_patrol"),
	(try_end),
	]),

(2,	[
	(try_for_parties, ":cur_patrol"),
		(party_get_template_id,":cur_party_template",":cur_patrol"),
		(eq, ":cur_party_template", "pt_galacticempire_escort"),
		(call_script, "script_process_patrol_maintenance", ":cur_patrol"),
	(try_end),
		]),

(1, [

	(try_for_range, ":cur_base", walled_centers_begin, walled_centers_end),
		(party_get_slot, ":base_lvl", ":cur_base", slot_center_has_patrol),
		(gt, ":base_lvl", 0),
		(call_script, "script_process_automated_attack_system", ":cur_base"),
	(try_end),	
	]),
	
##simple trigger for Trade Federation thinking
(2,
	[
	#check if any parties need to be spawned
	#will spawn one party per cycle around Nal Hutta and call the decide destination script
	(try_begin),
		(store_num_parties_of_template, ":num_parties", "pt_independent_traders"),
		(lt, ":num_parties", 5),
		(set_spawn_radius, 5),
		(spawn_around_party,"p_nalhutta","pt_independent_traders"),
		(assign, ":cur_party", reg0),
		(party_set_slot, ":cur_party", slot_party_home_center, "p_nalhutta"), #set the home base to Nal Hutta
		(party_set_faction, ":cur_party", "fac_trade_federation"),
		(call_script, "script_decide_next_trader_destination", ":cur_party"),
#		(display_message, "@spawned a trader, id is {reg0}"), #test
	(try_end),
	
	#reqs and info gathering for processing the traders in the game
	(try_for_parties, ":cur_party"),
#		(assign, reg28, ":cur_party"),
		(party_get_template_id,":cur_party_template",":cur_party"),
		(eq, ":cur_party_template", "pt_independent_traders"),
		(get_party_ai_current_behavior,":cur_behavior",":cur_party"),
		(get_party_ai_object,":cur_object",":cur_party"),
		(party_get_slot, ":cur_home_base", ":cur_party", slot_party_home_center),
		(party_get_slot, ":cur_wealth", ":cur_object", slot_mainplanet_wealth),
#		(assign, reg26, ":cur_object"), #test
#		(assign, reg33, ":cur_behavior"),
#		(display_message, "@this is {reg28}. My behvior is {reg33}, my object is {reg26}"),
		
		#start thinking
		(try_begin),
			(eq,":cur_behavior",ai_bhvr_in_town),
			(eq,":cur_object", ":cur_home_base"),
#			(display_message, "@{reg28} is at home. That's {reg26}"),
			#we're home. Remove all prisoners
			(try_begin), 
				(party_get_num_prisoners,":num_prisoners",":cur_party"),
				(gt, ":num_prisoners", 0),
				(party_get_num_prisoner_stacks, ":num_prisoner_stacks",":cur_party"),
				(try_for_range_backwards, ":i_stack", 0, ":num_prisoner_stacks"),
					(party_prisoner_stack_get_troop_id, ":stack_troop",":cur_party", ":i_stack"),
					(gt, ":stack_troop", 0), #avoid cloning player by accident
					(party_prisoner_stack_get_size, ":stack_size",":cur_party",":i_stack"),
	#				(party_add_prisoners,":cur_home_base",":stack_troop",":stack_size"),	#will implement this later, for now just destroy them							
					(party_remove_prisoners,":cur_party",":stack_troop",":stack_size"),
#					(assign, reg24, ":stack_troop"),
#					(assign, reg29, ":stack_size"),
#					(display_message, "@{reg28} dropped {reg24}x{reg29} off at Nal Hutta"), #test
				(try_end),
			(try_end),
			
			#now get rid of the r2 units - although they're added as prisoners, they might pick up some in fights with bandits
			(try_begin),
				(party_count_members_of_type,":r2_available",":cur_party","trp_r2series"),
				(gt, ":r2_available", 0),
				(party_remove_members,":cur_party","trp_r2series",":r2_available"),
			(try_end),
			
			#we're done with offloading, time to move out
			(call_script, "script_decide_next_trader_destination", ":cur_party"),
		
		(else_try),
			(eq,":cur_behavior",ai_bhvr_in_town),
#			(display_message, "@{reg28} is in a town, the id is {reg26}. "), #test
			(neq,":cur_object", ":cur_home_base"),
			
			#we're at another port of call. Start loading up!
			#prisoners first
			(assign, ":total_bill", 0),
			(try_begin),
				(party_get_num_prisoners,":num_prisoners",":cur_object"),
				(gt, ":num_prisoners", 0),
#				(assign, reg35, ":num_prisoners"),
				(val_mul, ":num_prisoners", 2),
				(store_div, ":get_prisoners", ":num_prisoners", 3), #we're only buying 2/3 of them
#				(assign, reg34, ":get_prisoners"),
#				(display_message, "@ this is {reg28} buying prisoners at {reg26}. There are {reg35} available and we're buying {reg34}"),
				(assign, ":num_transported", 0),
				(party_get_num_prisoner_stacks, ":num_prisoner_stacks",":cur_object"),
				(try_for_range_backwards, ":i_stack", 0, ":num_prisoner_stacks"),
					(lt, ":num_transported", ":get_prisoners"), #keep buying stacks until we've reached the target
					(party_prisoner_stack_get_troop_id, ":stack_troop",":cur_object", ":i_stack"),
					(gt, ":stack_troop", 0), #avoid cloning player by accident
					(neg|troop_is_hero, ":stack_troop"), # don't take away the heroes
					(party_prisoner_stack_get_size, ":stack_size",":cur_object",":i_stack"),
					(store_sub, ":get_max", ":get_prisoners", ":num_transported"), #get max should be nr of prisoners we still need
					(val_clamp, ":stack_size", 0, ":get_max"), #so stack size is never more than nr pris we still need
					(party_add_prisoners,":cur_party",":stack_troop",":stack_size"),								
					(party_remove_prisoners,":cur_object",":stack_troop",":stack_size"),
					(val_add, ":num_transported", ":stack_size"),
					#calculate the price of our current stack and add that to the bill
					(store_character_level, ":troop_level", ":stack_troop"),
					(assign, ":ransom_amount", ":troop_level"),
					#set lvl based ransom modifier so units lvl 10 or below are worth less (lvl 10 will be 25credits, lvl 30 will be 200)
					(try_begin),
						(le, ":troop_level", 10),
						(assign, ":lvl_modifier", 16),
					(else_try),
						(assign, ":lvl_modifier", 8),
					(try_end),
					(val_add, ":ransom_amount", 10), 
					(val_mul, ":ransom_amount", ":ransom_amount"),
					(val_div, ":ransom_amount", ":lvl_modifier"), #this is now the price per prisoner
					(val_mul, ":ransom_amount", ":stack_size"),
					(val_add, ":total_bill" , ":ransom_amount"),
#					(assign, reg24, ":stack_troop"),
#					(assign, reg29, ":stack_size"),
#					(display_message, "@{reg28} bought {reg24}x{reg29} prisoners"), #test
				(try_end),
#					(assign, reg36, ":num_transported"),
#					(display_message, "@ this is {reg28} buying prisoners at {reg26}. We bought {reg36} in total"),
					
			(try_end),
			
			#now look for R2 units
			(try_begin),
				(party_count_members_of_type,":r2_available",":cur_object","trp_r2series"),
				(gt, ":r2_available", 0),
				(party_remove_members,":cur_object","trp_r2series",":r2_available"),
				(party_add_prisoners,":cur_party","trp_r2series",":r2_available"), #r2 units are sold into slavery, I'm sure C3PO would approve
				(val_mul, ":r2_available", 112), #112 is the value based on the prisoner value system, see above block
				(val_add, ":total_bill", ":r2_available"),
				(assign, reg30, ":r2_available"),
#				(display_message, "@{reg28} bought {reg30} r2 units"),
			(try_end),
			
			#if we're under strength, try to recruit some mercenaries. Using same basic code as prisoners block above so see there for what does what
			(try_begin),
				(party_get_num_companions,":num_troops",":cur_party"),
				(lt, ":num_troops", 30),
				(store_sub, ":hire_nr", 30, ":num_troops"), #30 minus what we've already got will be what we need
#				(assign, reg47, ":hire_nr"),
#				(display_message, "@we're under str, looking for {reg47} mercs"),
				(party_get_num_companion_stacks, ":num_stacks",":cur_object"),
				(assign, ":nr_hired", 0),
				(try_for_range, ":i_stack", 0, ":num_stacks"),
					(lt, ":nr_hired", ":hire_nr"),
					(party_stack_get_troop_id, ":temp_id", ":cur_object", ":i_stack"),
					(is_between, ":temp_id", mercenary_troops_begin, mercenary_troops_end),
					(party_stack_get_size, ":stack_size",":cur_object",":i_stack"),
					(store_sub, ":get_max", ":hire_nr", ":nr_hired"),
					(val_clamp, ":stack_size", 0, ":get_max"),
					(party_remove_members,":cur_object",":temp_id",":stack_size"),
					(party_add_members,":cur_party",":temp_id",":stack_size"),
#					(assign, reg29, ":stack_size"),
					(val_add, ":nr_hired", ":stack_size"),
					(val_mul, ":stack_size", 50), #just using generic recompensation of 50 credits per unit
					(val_add, ":total_bill", ":stack_size"),
#					(assign, reg24, ":temp_id"),
#					(display_message, "@{reg28} took {reg24}x{reg29} new mercenaries on board"), #test
				(try_end),
			(try_end),
			
			#settle the bill - right now the money is just created. Will have to work out a system where traders have their own cash.
			#can add test to trigger where they disband if they become too poor and retire if they become too rich, or maybe morph into a higher type of unit
			(try_begin),
				(gt, ":total_bill", 0),
				(val_add, ":cur_wealth", ":total_bill"),
				(party_set_slot, ":cur_home_base", slot_mainplanet_wealth, ":cur_wealth"),
#				(assign, reg31, ":total_bill"),
#				(assign, reg32, ":cur_wealth"),
#				(display_message, "@{reg28} paid a bill of {reg31} making the total wealth {reg32}"),
			(try_end),
			
			#we're done with shopping, let's move out
			(call_script, "script_decide_next_trader_destination", ":cur_party"),
		(else_try),
		
			#find new destination for idle units
			(neq,":cur_behavior",ai_bhvr_in_town),
			(neq,":cur_behavior",ai_bhvr_travel_to_party), #we should be either traveling or loading/unloading.
			(call_script, "script_decide_next_trader_destination", ":cur_party"),
		(try_end),
	(try_end),
	]),
	
(1, [
	(neq, "$g_bank_init", 1),
	(faction_set_slot,"fac_trade_federation",slot_faction_debt_interest,12),
	(faction_set_slot,"fac_trade_federation",slot_faction_deposit_interest, 8),
	(assign, "$g_bank_init", 1),
]),

#Simple trigger for collecting taxes from your holdings and putting them in your bank
(24, [
	(eq, "$g_taxes_calculated", 1),
	#SW - added TheMageLord One Stop Tax Collection Mod - MF modified
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
	(try_begin),
	(gt, ":total_tax", 0),
		(faction_get_slot,":player_funds","fac_trade_federation",slot_faction_bank_deposit),
		(val_add, ":player_funds", ":total_tax"),
		(faction_set_slot,"fac_trade_federation",slot_faction_bank_deposit,":player_funds"),
		(dialog_box, "@A total of {reg1} credits in tariffs and rents from your planets was added to your bank account", "@Weekly Income"),
	(try_end),
	(assign, "$g_taxes_calculated", 0),
]),

#simple trigger for calculating and paying out bank interest. Interest is based on 30 days but calculated every 6 days.
#need to change this to take compound interest into account but for now it's a quick and dirty solution
#this doesn't seem possible.. need to be able to do something other than a square root: (n root of (x+1)) -1 = interest per period. Where n is nr of compound periods and x is interest per 30 days expressed as a decimal fraction of 1 (so 0,08 for 8%)
(24*6, [
		(faction_get_slot, ":interest", "fac_trade_federation", slot_faction_deposit_interest),
		(faction_get_slot, ":player_money", "fac_trade_federation", slot_faction_bank_deposit),
		(val_mul, ":interest", 100),
		(val_div, ":interest", 5),
		(store_mul, ":interest", ":player_money", ":interest"),
		(val_div, ":interest", 10000),
		(val_add, ":player_money", ":interest"),
		(faction_set_slot, "fac_trade_federation", slot_faction_bank_deposit, ":player_money"),
		(assign, reg10, ":interest"),
		(assign, reg11, ":player_money"),
		(gt, ":interest", 0),
		(display_message, "@Your bank added {reg10} credits interest to your account, making your balance {reg11}"),
		]),
		
# #simple trigger checking repay time on player loan and sending message
# (24, [
	# (faction_get_slot, ":loan_amount", "fac_trade_federation", slot_faction_bank_debt),
	# (gt, ":loan", 0),
	# (assign, reg11, ":loan_amunt"),
	# (faction_get_slot, ":loan_expires", "fac_trade_federation", slot_faction_debt_expires),
	# (store_current_hours, ":cur_hours"),
	# (val_sub, ":loan_expires", ":cur_hours"),
	# (store_div, ":loan_days", ":loan_expires", 24),
	# (assign, reg12, ":loan_days"),
	# (try_begin),
		# (is_between, ":loan_expires", 25, 120),
		# (display_message, "@Your bank reminds you that your loan will expire in {reg12} days and you still need to repay {reg11} credits"),
	# (else_try),
		# (is_between, ":loan_expires", 0, 24),
		# (display_message, "@Your bank reminds you that payment for your loan is due today. You will need to repay {reg11} credits"),
	# (else_try),
		# (eq, "$g_bank_loan_warning", 0),
		# (lt, ":loan_expires", 0),
		# (dialog_box, "@Your bank sends you a message that your loan is overdue. If you don't pay soon, they will be forced to take action.", "@Loan overdue"),
		# (call_script, "script_change_player_relation_with_faction", "fac_trade_federation", -5),
		# (assign, "$g_bank_loan_warning", 1),
	# (else_try),
		# (eq, "$g_bank_loan_warning", 1),
		# (lt, ":loan_expires", 0),
		# (dialog_box, "@Your bank sends you a final warning to repay your loan or face the consequences", "@Final warning"),
		# (call_script, "script_change_player_relation_with_faction", "fac_trade_federation", -5),
		# (assign, "$g_bank_loan_warning", 2),
	# (else_try),
		# (eq, "$g_bank_loan_warning", 2),
		# (lt, ":loan_expires", 0),
		# (val_mul, ":loan_amount", 3),
		# (store_div, ":bounty", ":loan_amount", 2), # set 2/3 of the loan as the bounty
		# (val_clamp, ":bounty", 2000, 5000), #with a minumum of 2000 and max of 5000
		# (assign, ":bounty", reg15),
		# (call_script, "script_set_bounty_on_party", "p_main_party", ":bounty"),
		# (call_script, "script_change_player_relation_with_faction", "fac_trade_federation", -5),
		# (dialog_box, "@As a result of your continuing refusal to repay your loan, the Trade Federation has placed a bounty of {reg15} credits on your head. ", "@Bounty placed")
		# (assign, "$g_bank_loan_warning", 3),
	# (try_end),
	# ]),
	
#Mining Vessel spwning (every map day) -- swyter
(24,[
    
    ##--> If we are in bounds skip, if not then create a new one, populating the map once at a time.
    (try_begin),
      #if less than 10 mining vessels
      (store_num_parties_of_template, ":mvess_count", "pt_miningvessel"),
      (lt,":mvess_count",10),
      
      #spawn around debris of asteroids
      (set_spawn_radius, 2),
      (store_random_in_range,":spawn_point", "p_debris_01","p_debris_10"),
      (spawn_around_party,   ":spawn_point", "pt_miningvessel"),
       
      #get the instance number
      (assign, ":instance", reg0),
      (party_get_position, pos1, ":instance"),
      (map_get_random_position_around_position, pos2, pos1, 5),
      
      #add properties
      #(party_set_ai_behavior,":instance", ai_bhvr_patrol_party),
      #(party_set_ai_object,  ":instance", ":spawn_point"),
      
      (party_set_ai_behavior, ":instance", ai_bhvr_patrol_location),
      (party_set_ai_patrol_radius,":instance", 10),
      (party_set_ai_target_position, ":instance", pos2),
      (party_set_ai_object, ":instance", ":spawn_point"),
      
      (party_set_flags, ":instance", pf_default_behavior, 0),
      (party_set_flags, ":instance", slot_party_ai_substate, 0),
      (party_set_flags, ":instance", pf_is_ship|pf_hide_defenders, 1),
      (party_set_bandit_attraction, ":instance", 50), #hmmm tasty miners
      (party_set_extra_text, ":instance", "@Mining asteroids for ore..."),
      
      (party_set_slot, ":instance", slot_center_player_relation, 0), #neutral by default, as they are independent
      
      #--> from here dbg
      #(call_script, "script_get_closest_center", ":instance"),
      #(try_begin),
      #  (gt, reg0, 0),
      #  (str_store_party_name, s1, reg0),
      # (else_try),
      #  (str_store_string, s1, "@unknown place"),
      #(try_end),
      
      #(display_message, "@$--->Mining vessel spawned, near {s1}",color_bad_news),
      #(party_relocate_near_party,":instance","p_main_party",1),
    (try_end),
    ]),
    
#Mining Vessel movement, from time to time -- swyter
(2, [
    (try_for_parties,":i"),
      (party_get_template_id,":i_pt",":i"),
      (eq,":i_pt","pt_miningvessel"),
      
      #--> in case we're dealing with such a badass...
      
      (party_get_position, pos1, ":i"),
      (map_get_random_position_around_position, pos2, pos1, 2),
      (party_set_ai_behavior, ":i", ai_bhvr_travel_to_point),  #pick a random point and go there, ore!
      (party_set_ai_target_position, ":i", pos2),
    (try_end)
    ]),

#spare trigger 1
(24*7,	[


	]),

#+freelancer start
    #  WEEKLY PAY
    
    (24 * 7, [
        (eq, "$freelancer_state", 1),
        
        #kham - removed upgrade condition from this block as it takes too long.
        
        (store_faction_of_troop, ":commander_faction", "$enlisted_lord"),
        (faction_get_slot, ":is_sarge", ":commander_faction", slot_faction_freelancer_captain), #is sarge / captain?
        
        (store_character_level, ":level", "$player_cur_troop"),
        #pays player 10 times the troop level
        (try_begin),
          (eq, ":is_sarge", 1), #sarge
          (store_mul, ":weekly_pay", 15, ":level"),
        (else_try),
          (eq, ":is_sarge", 2), #cap
          (store_mul, ":weekly_pay", 22, ":level"),
        (else_try),
          (store_mul, ":weekly_pay", 10, ":level"),
        (try_end),
        
        (troop_add_gold, "trp_player", ":weekly_pay"),
        (add_xp_to_troop, 70, "trp_player"),
        (play_sound, "snd_money_received", 0),
        (val_add, "$g_next_pay_time", 7), #We add the next payday here.
    ]),
    
    #  UPGRADE CHECK
    (24 * 3,[
        (eq, "$freelancer_state", 1),
        
        (troop_get_slot, ":service_xp_start", "trp_player", slot_troop_freelancer_start_xp),
        (troop_get_xp, ":player_xp_cur", "trp_player"),
        (store_sub, ":service_xp_cur", ":player_xp_cur", ":service_xp_start"),
        
        (store_faction_of_troop, ":commander_faction", "$enlisted_lord"),
        (faction_get_slot, ":is_sarge", ":commander_faction", slot_faction_freelancer_captain), #is sarge / captain?
        
        #Piggy Backing for Sarge / Captain Troop Replenishment
        
        (try_begin),
          (ge, ":is_sarge", 1),
          (party_get_num_companions, ":num_companions", "p_main_party"),
          (try_begin),
            (eq, ":is_sarge", 1),
            (assign, ":amount_required", 9), #Sarge
          (else_try),
            (assign, ":amount_required", 16), #Captain
          (try_end),
          (lt, ":num_companions", ":amount_required"),
          (store_sub, ":required_replenish", ":amount_required", ":num_companions"),
          (quest_get_slot, ":type", "qst_freelancer_enlisted", slot_quest_current_state), #if 1 = infantry / if 2 = ranged
          (try_begin),
            (eq, ":type", 1),
            (faction_get_slot, ":troop_to_add", ":commander_faction", slot_faction_tier_2_troop),
          (else_try),
            (faction_get_slot, ":troop_to_add", ":commander_faction", slot_faction_tier_1_archer),
          (try_end),
          (gt, ":troop_to_add", 0),
          (party_add_members, "p_main_party", ":troop_to_add", ":required_replenish"),
          (display_message, "@You are given new troops under your command", color_good_news),
        (try_end),
        
        #END Troop Replenishment
        
        
        #ranks for pay levels and to upgrade player equipment based on upgrade troop level times 1000
        # (try_begin),
        # (troop_get_upgrade_troop, ":upgrade_troop", "$player_cur_troop", 0),
        # (gt, ":upgrade_troop", 1), #make sure troop is valid and not player troop
        # (store_character_level, ":level", ":upgrade_troop"),
        # (store_pow, ":required_xp", ":level", 2), #square the level and
        # (val_mul, ":required_xp", 100),           #multiply by 100 to get xp
        # (ge, ":service_xp_cur", ":level"),
        # (jump_to_menu, "mnu_upgrade_path"),
        # (try_end),
        
        (try_begin),
          (troop_get_upgrade_troop, ":upgrade_troop", "$player_cur_troop", 0),
          #(gt, ":upgrade_troop", 1), #make sure troop is valid and not player troop
          
          (try_begin),
            (eq, "$freelancer_enhanced_upgrade", 0), #Let's put this as a choice for players.
            (try_begin), #Captain / Sarge Check
              (gt, ":is_sarge", 0),
              (store_character_level, ":player_level", "trp_player"),
              (store_sub, ":cur_xp", ":player_level", 1),
              (get_level_boundary, ":cur_xp", ":cur_xp"),
              (val_add, ":player_level", 5), #add 5 levels to current level to become sarge / captain
              (get_level_boundary, ":required_xp", ":player_level"),
              (val_sub, ":required_xp", ":cur_xp"),
            (else_try),
              (call_script, "script_game_get_upgrade_xp", "$player_cur_troop"),
              (assign, ":required_xp", reg0),
            (try_end),
            
          (else_try),
            
            ##THIS  BLOCK IS ALMOST DEFINITELY BE BETTER than the above two lines which could be commented out in exchange for them. - Implemented by Kham
            
            (try_begin), #Captain / Sarge Check
              (gt, ":is_sarge", 0),
              (store_character_level, ":player_level", "trp_player"),
              (store_sub, ":cur_xp", ":player_level", 1),
              (get_level_boundary, ":cur_xp", ":cur_xp"),
              (val_add, ":player_level", 5), #add 5 levels to current level to become sarge / captain
              (get_level_boundary, ":required_xp", ":player_level"),
              (val_sub, ":required_xp", ":cur_xp"),
            (else_try),
              (store_character_level, ":cur_level", "$player_cur_troop"),
              (val_sub, ":cur_level", 1),
              (get_level_boundary, ":cur_level", ":cur_level"),
              (store_character_level, ":required_xp", ":upgrade_troop"),
              ##Kham Changes Begin
              (try_begin),
                (gt, ":required_xp", 19),
                (assign, ":sub_amount", 1),
              (else_try),
                (assign, ":sub_amount", 3),
              (try_end),
              #Kham Changes END
              (val_sub, ":required_xp", ":sub_amount"),
              (get_level_boundary, ":required_xp", ":required_xp"),
              (val_sub, ":required_xp", ":cur_level"),
            (try_end),
          (try_end), #End Captain / Sarge Check
          ##
          
          (ge, ":service_xp_cur", ":required_xp"),
          
          (try_begin),
            (call_script, "script_cf_freelancer_player_can_upgrade", ":upgrade_troop"),
            (troop_set_slot, "trp_player", slot_troop_freelancer_start_xp, ":player_xp_cur"),
            (jump_to_menu, "mnu_upgrade_path"),
          (else_try),
            (assign, ":reason", reg0), #from cf_freelancer_player_can_upgrade
            (try_begin),
              (eq, ":reason", 0), #not enough strength, for melee weapons
              (display_message, "@You are not strong enough to lift a weapon fit for your promotion!"),
            (else_try),
              (eq, ":reason", 1), #not enough strength, for armor
              (display_message, "@You are not strong enough to hold all that weight required with promotion!."),
            (else_try),
              (eq, ":reason", 2), #not enough power draw/throw/strength for bow/crossbow/throwing
              (display_message, "@Your arms are to weak to advance in the artillary at this moment."),
            (else_try),
              (eq, ":reason", 3), #not enough riding skill for horse
              (display_message, "@You require more horse riding skills to fit your next poisition!"),
            (try_end),
          (try_end),
        (try_end),
        
    ]),
    
    #  HOURLY CHECKS
    
    (1,[
        (eq, "$freelancer_state", 1),
        #so that sight and camera follows near commander's party
        (set_camera_follow_party, "$enlisted_party"),
        (party_relocate_near_party, "p_main_party", "$enlisted_party", 1),
        
        (assign, ":num_food", 0),
        (troop_get_inventory_capacity, ":max_inv_slot", "trp_player"),
        (try_for_range, ":cur_inv_slot", ek_item_0, ":max_inv_slot"),
          (troop_get_inventory_slot, ":cur_item", "trp_player", ":cur_inv_slot"),
          (ge, ":cur_item", 0),
          (is_between, ":cur_item", food_begin, food_end),
          (val_add, ":num_food", 1),
        (try_end),
        (store_faction_of_troop, ":commander_faction", "$enlisted_lord"),
        (faction_get_slot, ":is_sarge", ":commander_faction", slot_faction_freelancer_captain), #is sarge / captain?
        (try_begin),
          (lt, ":num_food", 2),
          (try_begin),
            (eq, ":is_sarge", 1), #sarge
            (troop_add_item, "trp_player", "itm_dried_meat"),
          (else_try),
            (eq, ":is_sarge", 2), #cap
            (troop_add_item, "trp_player", "itm_cattle_meat"),
          (else_try),
            (troop_add_item, "trp_player", "itm_bread"),
          (try_end),
        (try_end),
    ]),
    
    #+freelancer end
    
    #Kham Freelancer Improvement triggers
    
    #Random Missions
    (12,[
        
        (eq, "$freelancer_missions", 1),
        (eq, "$freelancer_state", 1),
        (store_random_in_range, ":rand", 0, 100),
        (ge, ":rand", 50), #50% chance for a mission
        (call_script, "script_get_freelancer_mission"),
        
    ]),
    

    #trigger reserved for future save game compatibility
    #(999,[]),
    #trigger reserved for future save game compatibility
    #(999,[]),
    #trigger reserved for future save game compatibility
    (999,[]),
    
    #trigger reserved for future save game compatibility
    (999,[]),
    #trigger reserved for future save game compatibility
    (999,[]),
    #trigger reserved for future save game compatibility
    (999,[]),
    #trigger reserved for future save game compatibility
    (999,[]),
    #trigger reserved for future save game compatibility
    (999,[]),
    #trigger reserved for future save game compatibility
    (999,[]),
    #trigger reserved for future save game compatibility
    (999,[]),
    #trigger reserved for future save game compatibility
    (999,[]),
    #trigger reserved for future save game compatibility
    (999,[]),
    #trigger reserved for future save game compatibility
    (999,[]),
    #trigger reserved for future save game compatibility
    (999,[]),
    #trigger reserved for future save game compatibility
    (999,[]),
    #trigger reserved for future save game compatibility
    (999,[]),
    #trigger reserved for future save game compatibility
    (999,[]),
    #trigger reserved for future save game compatibility
    (999,[]),
    #trigger reserved for future save game compatibility
    (999,[]),
    #trigger reserved for future save game compatibility
    (999,[]),
    #trigger reserved for future save game compatibility
    (999,[]),
    #trigger reserved for future save game compatibility
    (999,[]),
    #trigger reserved for future save game compatibility
    (999,[]),
    #trigger reserved for future save game compatibility
    (999,[]),
    #trigger reserved for future save game compatibility
    (999,[]),
    #trigger reserved for future save game compatibility
    (999,[]),
    #trigger reserved for future save game compatibility
    (999,[]),
    #trigger reserved for future save game compatibility
    (999,[]),

]

