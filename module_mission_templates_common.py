# S T A R   W A R S   C O N Q U E S T   M O D U L E   S Y S T E M
# / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /
# By Taleworlds, HokieBT, MartinF and Swyter - Do not use/copy without permission

from header_common import *
from header_operations import *
from header_mission_templates import *
from header_animations import *
from header_sounds import *
from header_music import *
from module_constants import *
#SW - needed to add unused_horse_animation
from module_animations import *
#SW - needed to add for toggle_weapon_capabilities code
from header_items import *

####################################################################################################################
#   Each mission-template is a tuple that contains the following fields:
#  1) Mission-template id (string): used for referencing mission-templates in other files.
#     The prefix mt_ is automatically added before each mission-template id
#
#  2) Mission-template flags (int): See header_mission-templates.py for a list of available flags
#  3) Mission-type(int): Which mission types this mission template matches.
#     For mission-types to be used with the default party-meeting system,
#     this should be 'charge' or 'charge_with_ally' otherwise must be -1.
#
#  4) Mission description text (string).
#  5) List of spawn records (list): Each spawn record is a tuple that contains the following fields:
#    5.1) entry-no: Troops spawned from this spawn record will use this entry
#    5.2) spawn flags.
#    5.3) alter flags. which equipment will be overriden
#    5.4) ai flags.
#    5.5) Number of troops to spawn.
#    5.6) list of equipment to add to troops spawned from here (maximum 8).
#  6) List of triggers (list).
#     See module_triggers.py for infomation about triggers.
#
#  Please note that mission templates is work in progress and can be changed in the future versions.
#
####################################################################################################################

####################################################################
####################### INITIALIZE AUTOFIRE ########################
####################################################################
common_init_auto_fire = (ti_after_mission_start, 0, ti_once, [], 
    [

############### NEEDED TO PREVENT UNINITIALIZE SLOTS ###############
      (call_script, "script_init_item_accuracy"),
      (call_script, "script_init_item_shoot_speed"),
      (call_script, "script_init_item_speed_rating"),
    ])

common_auto_fire_held = (
   0.1, 0.5, 0, [ # adjust the delay to match the time it takes to play the ready animation
  (game_key_is_down, gk_attack),
   ],[
      (get_player_agent_no, ":shooter_agent"),
  (agent_set_slot, ":shooter_agent", slot_agent_autofire_ready, 1),
    ])

common_auto_fire_clicked = (
   0.1, 0, 0, [
      (get_player_agent_no, ":shooter_agent"),
      (agent_get_animation, ":shooter_stance", ":shooter_agent", 1),
      (this_or_next|eq, ":shooter_stance", "anim_reload_crossbow"),
      (this_or_next|eq, ":shooter_stance", "anim_reload_musket"),
      (this_or_next|eq, ":shooter_stance", "anim_reload_pistol"),
  (neg|game_key_is_down, gk_attack),
   ],[
      (get_player_agent_no, ":shooter_agent"),
  (agent_set_slot, ":shooter_agent", slot_agent_autofire_ready, 0),
    ])

####################################################################
################## CHECK IF BULLET CAN BE FIRED ####################
####################################################################
common_auto_fire = (
   0.1, 0, 0, [],
   [
      (try_for_agents, ":shooter_agent"),
         (agent_is_alive, ":shooter_agent"),
         (try_begin),
############# CHECK IF AGENT WIELDS AN AUTOFIRE WEAPON #############
            (agent_get_wielded_item, ":cur_weapon", ":shooter_agent", 0),
            (is_between, ":cur_weapon", "itm_a280", "itm_dh17"),

########### CHECK IF AGENT IS IN READY WEAPON ANIMATION ############
            (agent_get_animation, ":shooter_stance", ":shooter_agent", 1),
            (this_or_next|eq, ":shooter_stance", "anim_ready_bow"),
            (this_or_next|eq, ":shooter_stance", "anim_ready_crossbow"),
            (this_or_next|eq, ":shooter_stance", "anim_ready_javelin"),
            (this_or_next|eq, ":shooter_stance", "anim_ready_pistol"),
            (eq, ":shooter_stance", "anim_ready_musket"), 


(assign, ":ready_flag", 0),
(try_begin), #Limits the AI to burst firing
   (agent_is_non_player, ":shooter_agent"),
   (agent_get_combat_state, ":cur_state", ":shooter_agent"),
   (eq, ":cur_state", 3),
   (assign, ":ready_flag", 1),
(else_try), #Check if a player has held down the attack button
   (neg|agent_is_non_player, ":shooter_agent"),
   (agent_slot_eq, ":shooter_agent", slot_agent_autofire_ready, 1),
   (assign, ":ready_flag", 1),
(try_end),
(eq, ":ready_flag", 1),

################## FIND WEAPON AND SET AMMO TYPE ##################
            (try_for_range, ":cur_slot", 0, 4),
               (agent_get_item_slot, ":cur_item", ":shooter_agent", ":cur_slot"),
               (try_begin),
                (eq, ":cur_item", ":cur_weapon"),
                (assign, ":weapon_slot", ":cur_slot"),
              (else_try),
                (is_between, ":cur_item", "itm_laser_bolts_green_rifle", "itm_laser_bolts_training_pistol"),
                (assign, ":ammo_item", ":cur_item"),
              (try_end),
            (try_end),

############################ REDUCE AMMO ###########################
            (try_begin),
               (agent_get_ammo_for_slot, ":ammo", ":shooter_agent", ":weapon_slot"),
               (gt, ":ammo", 0),
               (val_sub, ":ammo", 1),
               (agent_set_ammo, ":shooter_agent", ":cur_weapon", ":ammo"),

####################### SET FIRING ANIMATION #######################
                (try_begin),
                  (item_has_capability, ":cur_weapon", itcf_shoot_crossbow),
                  (neq, ":cur_weapon", "itm_z6"),
                  (agent_set_animation, ":shooter_agent", "anim_release_crossbow", 1),  
               (else_try),                 
                  (agent_set_animation, ":shooter_agent", "anim_release_musket", 1),
               (try_end),
               (call_script, "script_fire_auto_weapon", ":shooter_agent", ":cur_weapon", ":ammo_item"),
            (try_end),
         (else_try),
################## REDUCES RECOIL FOR ALL AGENTS ###################
            (agent_get_slot, ":wander", ":shooter_agent", slot_agent_firearm_wander),
            (val_sub, ":wander", 20),
            (val_min, ":wander", 0),
            (agent_set_slot, ":shooter_agent", slot_agent_firearm_wander, ":wander"),
         (try_end),
      (try_end),
   ])


####>>>>>>>
#Motomataru's new AI
common_ranged_avoid_melee =  (.3, 0, 0, [], [(call_script, "script_ranged_avoid_melee")])

#AI triggers v3 by motomataru
AI_triggers = [

  (ti_inventory_key_pressed, 0, 0,
      [
        (game_key_is_down, gk_view_char),
        # (set_trigger_result,1),
      ], [
        (get_player_agent_no, ":player_agent"),
        (assign, ":end", ek_foot), #should add a global as iterator
        (try_for_range, ":item_slot", ek_item_0, ":end"),
          (agent_get_item_slot, ":item_no", ":player_agent", ":item_slot"),
          (gt, ":item_no", -1),
          (item_slot_ge, ":item_no", slot_item_num_components, 1),
          (assign, "$g_current_opened_item_details", ":item_no"),
          (assign, ":end", -1),
          (start_presentation, "prsnt_customize_weapon"),
        (try_end),
        (try_begin), #none found
          (eq, ":end", ek_foot),
          (display_message, "str_cant_use_inventory_tutorial"),
          (assign, "$g_current_opened_item_details", -1),
        (try_end),
      ]),

  (ti_before_mission_start, 0, 0, [], [
    (assign, "$cur_casualties", 0),
    (assign, "$prev_casualties", 0),
    (assign, "$ranged_clock", 1),
  ]),

  (0, .3, ti_once, [], [(call_script, "script_SW_field_tactics", 1)]),  #delay to allow spawning to finish

  (1, .9, 0, [], [
    (try_begin),
      (call_script, "script_cf_count_casualties"),
      (assign, "$cur_casualties", reg0),
    (try_end),

    (try_begin),  #reassess ranged position upon first casualty
      (gt, "$cur_casualties", 0),
      (eq, "$prev_casualties", 0),
      (call_script, "script_SW_field_tactics", 1),
      (assign, "$ranged_clock", 0),
    (else_try),
      (lt, "$ranged_clock", 10),
      (call_script, "script_SW_field_tactics", 0),
    (else_try),  #reassess ranged position every ten seconds after first casualty
      (gt, "$prev_casualties", 0),
      (call_script, "script_SW_field_tactics", 1),
      (assign, "$ranged_clock", 0),
    (try_end),

    (val_add, "$ranged_clock", 1),
  ]),

  common_ranged_avoid_melee,
]
####>>>>>>>

#SW - modified pilgrim disguise
pilgrim_disguise = [itm_transparent_helmet,itm_vest_closed_a,itm_black_boots,itm_vibro_blade1,itm_laser_bolts_yellow_pistol,itm_westar,itm_energy_shield_yellow_small]
#SW - modified af_spacestation_lord
#af_spacestation_lord = af_override_horse | af_override_weapons| af_require_civilian
af_spacestation_lord = af_override_horse | af_override_weapons

#SW MF stuff for stay in battle after knockdown and death-cam- BIG Thanks to silverkatana & DMOD Valkyrie for base code - http://forums.taleworlds.com/index.php/topic,60329.msg1559908.html

sw_victory_defeat_conditions = (
  5, 2, 3,
  [(all_enemies_defeated)],
  [

    (assign, "$battle_won",1),
    (assign, "$g_battle_result", 1),
    (display_message,"str_msg_battle_won"),
    (set_mission_result, 1),
  ])
  
  
#swy-- temporarily disable the buggy deathcam
sw_deathcam_follow_troop         = (0, 0, 0,[],[])
sw_deathcam_valkyrie_move_camera = (0, 0, 0,[],[])
sw_deathcam_cycle_fowards        = (0, 0, 0,[],[])
sw_deathcam_cycle_backwards      = (0, 0, 0,[],[])

'''
sw_deathcam_follow_troop = (0, 0, 0,[
  (eq, "$dmod_move_camera", 2),
    (agent_get_position, 1, "$dmod_current_agent"),
    (get_player_agent_no, ":player_agent"),
    (agent_set_position, ":player_agent", 1)

     ],[])
sw_deathcam_valkyrie_move_camera = (0, .3, 2.1,[
  (eq, "$dmod_move_camera", 1),
        #(agent_get_position, pos2, "$dmod_current_agent"),
        #(position_move_z, pos2, 300),
        #(mission_cam_set_mode, 1),
        #(mission_cam_set_position, pos2),
        
        #(position_move_z, pos2, 300),
        #(mission_cam_animate_to_position, pos2, 400),
     ],[
        (mission_cam_set_mode, 0, 300, 1),
        (assign, "$dmod_move_camera", 2),
     ])
sw_deathcam_cycle_fowards =   (0, 0, 0,[
    #(key_clicked, key_m),
    (key_clicked, "$deathcam_forward_key"),
    (main_hero_fallen),
        (call_script, "script_dmod_cycle_forwards"),
        ], [])

sw_deathcam_cycle_backwards = (0, 0, 0,[
    #(key_clicked, key_n),
    (key_clicked, "$deathcam_backward_key"),
    (main_hero_fallen),
        (call_script, "script_dmod_cycle_backwards"),
        ], [])
'''
############################################################################################################
##### Custom Commander(CC)
############################################################################################################
common_check_player_can_join_battle = (
  0, 0, ti_once,
  [
    (neq,"$g_player_troop","trp_player"),
    (store_troop_health, "$g_player_begin_hp", "trp_player"),
    (neg|troop_is_wounded, "trp_player"),
    (get_player_agent_no, ":player_agent"),
    (ge, ":player_agent", 0),
    (agent_get_team, ":player_team", ":player_agent"),
    (agent_get_position, pos49, ":player_agent"),
    (position_move_x, pos49, -100),
    (set_spawn_position, pos49),
    (spawn_agent,"trp_player"),
    (agent_set_team, reg0, ":player_team"),
  ], [])

##  dismounted: for siege and inner battle to override the player's horse
##  when a NPC was selected as the commander
common_check_player_can_join_battle_dismounted = (
  0, 0, ti_once,
  [
    (neq,"$g_player_troop","trp_player"),
    (store_troop_health, "$g_player_begin_hp", "trp_player"),
    (neg|troop_is_wounded, "trp_player"),
    (get_player_agent_no, ":player_agent"),
    (ge, ":player_agent", 0),
    (agent_get_team, ":player_team", ":player_agent"),
    (agent_get_position, pos49, ":player_agent"),
    (position_move_x, pos49, -100),
    (set_spawn_position, pos49),
    (troop_get_inventory_slot, ":player_horse_item", "trp_player", 8),  ## ek_horse = 8
    (troop_get_inventory_slot_modifier, ":player_horse_item_modifier", "trp_player", 8),
    (troop_set_inventory_slot, "trp_player", 8, -1),
    (spawn_agent,"trp_player"),
    (agent_set_team, reg0, ":player_team"),
    (troop_set_inventory_slot, "trp_player", 8, ":player_horse_item"),
    (troop_set_inventory_slot_modifier, "trp_player", 8, ":player_horse_item_modifier"),
  ], [])

##  display messages about the changes of npc's proficiency
##  when he/she was selected as the commander
common_npc_proficiency_limit =(
  0, 0, ti_once, [(neq, "$g_player_troop", "trp_player")],
  [
    (store_proficiency_level, "$g_cur_one_handed_weapon_limt", "$g_player_troop", wpt_one_handed_weapon),
    (store_proficiency_level, "$g_cur_two_handed_weapon_limt", "$g_player_troop", wpt_two_handed_weapon),
    (store_proficiency_level, "$g_cur_polearm_limt", "$g_player_troop", wpt_polearm),
    (store_proficiency_level, "$g_cur_archery_limt", "$g_player_troop", wpt_archery),
    (store_proficiency_level, "$g_cur_crossbow_limt", "$g_player_troop", wpt_crossbow),
    (store_proficiency_level, "$g_cur_throwing_limt", "$g_player_troop", wpt_throwing),
  #SW - added firearm
  (store_proficiency_level, "$g_cur_firearm_limt", "$g_player_troop", wpt_firearm),
  ])

common_npc_raise_proficiency =(
  1, 0, 0, [(neq, "$g_player_troop", "trp_player")],
  [
    (store_proficiency_level, ":cur_one_handed_weapon", "$g_player_troop", wpt_one_handed_weapon),
    (store_proficiency_level, ":cur_two_handed_weapon", "$g_player_troop", wpt_two_handed_weapon),
    (store_proficiency_level, ":cur_polearm", "$g_player_troop", wpt_polearm),
    (store_proficiency_level, ":cur_archery", "$g_player_troop", wpt_archery),
    (store_proficiency_level, ":cur_crossbow", "$g_player_troop", wpt_crossbow),
    (store_proficiency_level, ":cur_throwing", "$g_player_troop", wpt_throwing),
  #SW - added firearm
    (store_proficiency_level, ":cur_firearm", "$g_player_troop", wpt_firearm),
      (str_store_troop_name, s1, "$g_player_troop"),
      (try_begin),
        (gt, ":cur_one_handed_weapon", "$g_cur_one_handed_weapon_limt"),
        (store_sub, ":amout", ":cur_one_handed_weapon", "$g_cur_one_handed_weapon_limt"),
        (assign, reg2, ":amout"),
        (val_sub, ":amout", 1),
        (assign, reg3, ":amout"),
        (assign, reg1, ":cur_one_handed_weapon"),
        (display_message, "@{reg3?{s1}'s proficiency in one handed weapon has improved by {reg2} to {reg1}.:{s1}'s one handed weapon proficiency have reach to {reg1}.}", 0xEEEE00),
        (assign, "$g_cur_one_handed_weapon_limt", ":cur_one_handed_weapon"),
      (else_try),
        (gt, ":cur_two_handed_weapon", "$g_cur_two_handed_weapon_limt"),
        (store_sub, ":amout", ":cur_two_handed_weapon", "$g_cur_two_handed_weapon_limt"),
        (assign, reg2, ":amout"),
        (val_sub, ":amout", 1),
        (assign, reg3, ":amout"),
        (assign, reg1, ":cur_two_handed_weapon"),
        (display_message, "@{reg3?{s1}'s proficiency in two handed weapon has improved by {reg2} to {reg1}.:{s1}'s two handed weapon proficiency have reach to {reg1}.}", 0xEEEE00),
        (assign, "$g_cur_two_handed_weapon_limt", ":cur_two_handed_weapon"),
      (else_try),
        (gt, ":cur_polearm", "$g_cur_polearm_limt"),
        (store_sub, ":amout", ":cur_polearm", "$g_cur_polearm_limt"),
        (assign, reg2, ":amout"),
        (val_sub, ":amout", 1),
        (assign, reg3, ":amout"),
        (assign, reg1, ":cur_polearm"),
        (display_message, "@{reg3?{s1}'s proficiency in polearm has improved by {reg2} to {reg1}.:{s1}'s polearm proficiency have reach to {reg1}.}", 0xEEEE00),
        (assign, "$g_cur_polearm_limt", ":cur_polearm"),
      (else_try),
        (gt, ":cur_archery", "$g_cur_archery_limt"),
        (store_sub, ":amout", ":cur_archery", "$g_cur_archery_limt"),
        (assign, reg2, ":amout"),
        (val_sub, ":amout", 1),
        (assign, reg3, ":amout"),
        (assign, reg1, ":cur_archery"),
        (display_message, "@{reg3?{s1}'s proficiency in archery has improved by {reg2} to {reg1}.:{s1}'s archery proficiency have reach to {reg1}.}", 0xEEEE00),
        (assign, "$g_cur_archery_limt", ":cur_archery"),
      (else_try),
        (gt, ":cur_crossbow", "$g_cur_crossbow_limt"),
        (store_sub, ":amout", ":cur_crossbow", "$g_cur_crossbow_limt"),
        (assign, reg2, ":amout"),
        (val_sub, ":amout", 1),
        (assign, reg3, ":amout"),
        (assign, reg1, ":cur_crossbow"),
        (display_message, "@{reg3?{s1}'s proficiency in crossbow has improved by {reg2} to {reg1}.:{s1}'s crossbow proficiency have reach to {reg1}.}", 0xEEEE00),
        (assign, "$g_cur_crossbow_limt", ":cur_crossbow"),
      (else_try),
        (gt, ":cur_throwing", "$g_cur_throwing_limt"),
        (store_sub, ":amout", ":cur_throwing", "$g_cur_throwing_limt"),
        (assign, reg2, ":amout"),
        (val_sub, ":amout", 1),
        (assign, reg3, ":amout"),
        (assign, reg1, ":cur_throwing"),
        (display_message, "@{reg3?{s1}'s proficiency in throwing has improved by {reg2} to {reg1}.:{s1}'s throwing proficiency have reach to {reg1}.}", 0xEEEE00),
        (assign, "$g_cur_throwing_limt", ":cur_throwing"),
    #SW - added firearm else_try
      (else_try),
        (gt, ":cur_firearm", "$g_cur_firearm_limt"),
        (store_sub, ":amout", ":cur_firearm", "$g_cur_firearm_limt"),
        (assign, reg2, ":amout"),
        (val_sub, ":amout", 1),
        (assign, reg3, ":amout"),
        (assign, reg1, ":cur_firearm"),
        (display_message, "@{reg3?{s1}'s proficiency in firearms has improved by {reg2} to {reg1}.:{s1}'s firearm proficiency have reach to {reg1}.}", 0xEEEE00),
        (assign, "$g_cur_firearm_limt", ":cur_firearm"),
      (try_end),
  ])
############################################################################################################
##### Custom Commander(CC)
############################################################################################################
##### more scripts by rubik
# common_custom_commander_camera = (
  # 0, 0, 0, [],
  # [
    # (get_player_agent_no, ":player_agent"),
    # (agent_get_look_position, pos1, ":player_agent"),
    # (position_move_z, pos1, "$g_camera_z"),
    # (position_move_y, pos1, "$g_camera_y"),
    # (agent_get_horse, ":horse_agent", ":player_agent"),
    # (try_begin),
      # (ge, ":horse_agent", 0),
      # (position_move_z, pos1, 80),
    # (try_end),
    # (mission_cam_set_position, pos1),
    # (try_begin),
      # (key_is_down, key_left_control),
      # (assign, ":move_val", 50),
    # (else_try),
      # (assign, ":move_val", 10),
    # (try_end),
    # (try_begin),
      # (key_clicked, key_up),
      # (mission_cam_set_mode, 1, 50),
      # (val_add, "$g_camera_z", ":move_val"),
    # (else_try),
      # (key_clicked, key_down),
      # (mission_cam_set_mode, 1, 50),
      # (val_sub, "$g_camera_z", ":move_val"),
    # (else_try),
      # (key_clicked, key_left),
      # (mission_cam_set_mode, 1, 50),
      # (val_add, "$g_camera_y", ":move_val"),
    # (else_try),
      # (key_clicked, key_right),
      # (mission_cam_set_mode, 1, 50),
      # (val_sub, "$g_camera_y", ":move_val"),
    # (try_end),
    # (try_begin),
      # (this_or_next|game_key_clicked, gk_view_char),
      # (game_key_clicked, gk_cam_toggle),
      # (mission_cam_set_mode, 0),
    # (try_end),
  # ])
############################################################################################################

#Highlander begin--------------------------------------
common_physics_init = (
ti_before_mission_start,0,0,[],
[(assign,"$timer",0),
#(assign,"$timer_in_seconds",0),
(assign,"$timer_speed",5),
(try_for_range,":projectile",0,256),
  (troop_set_slot,"trp_pjct_active",":projectile",0),
(try_end),

(try_for_range,":scene_prop",0,"spr_scene_props_end"),
 (scene_prop_get_num_instances,":num_instances",":scene_prop"),
 (try_for_range,":instance_no",0,":num_instances"),
  (scene_prop_get_instance,":instance",":scene_prop",":instance_no"),
  (troop_set_slot,"trp_instance_attached_to",":instance",0),
 (try_end),
(try_end),
])
common_timer = (0.05,0,0,
[(val_add,"$timer","$timer_speed"),
#(store_mission_timer_a,":time_in_sec"),
#(try_begin),
#  (neq,":time_in_sec","$timer_in_seconds"),
#  (val_mul,"$timer_speed",100),
#  (store_mul,":timer_delta_sub","$timer_in_seconds",100),
#  (store_sub,":timer_delta","$timer",":timer_delta_sub"),
#  (val_div,"$timer_speed",":timer_delta"),
#  (store_mul,"$timer",":time_in_sec",100),
#  (assign,"$timer_in_seconds",":time_in_sec"),
#(try_end),
],[])
common_physics = (
0.05,1.75,0,
[
(set_fixed_point_multiplier,100),
(assign,":one_explosion_or_more",0),
(try_for_range,":projectile",0,256),
  (troop_slot_eq,"trp_pjct_active",":projectile",1),

  #movement
  (troop_get_slot,":emit_time","trp_pjct_emit_time",":projectile"),
  (troop_get_slot,":x_pos","trp_pjct_x",":projectile"),
  (troop_get_slot,":y_pos","trp_pjct_y",":projectile"),
  (troop_get_slot,":z_pos","trp_pjct_z",":projectile"),
  (troop_get_slot,":x_velocity","trp_pjct_x_velocity",":projectile"),
  (troop_get_slot,":y_velocity","trp_pjct_y_velocity",":projectile"),
  (troop_get_slot,":z_velocity","trp_pjct_z_velocity",":projectile"),
  (store_sub,":dt","$timer",":emit_time"),
  (val_mul,":x_velocity",":dt"),
  (val_mul,":y_velocity",":dt"),
  (val_mul,":z_velocity",":dt"),
  (assign,":gravity",981),
  (val_mul,":gravity",":dt"),
  (val_mul,":gravity",":dt"),
  (val_div,":gravity",10000),
  (val_add,":x_pos",":x_velocity"),
  (val_add,":y_pos",":y_velocity"),
  (val_sub,":z_velocity",":gravity"),
  (val_add,":z_pos",":z_velocity"),
  (init_position,pos1),
  (position_set_x,pos1,":x_pos"),
  (position_set_y,pos1,":y_pos"),
  (position_set_z,pos1,":z_pos"),

  #particle_system
  (troop_get_slot,":particle_system","trp_pjct_particle_system",":projectile"),
  (try_begin),
    (ge,":particle_system",0),
#    (copy_position,pos3,pos1),
#    (party_get_slot,":x_velocity",":projectile",pjct_x_velocity),
#    (party_get_slot,":y_velocity",":projectile",pjct_y_velocity),
#    (party_get_slot,":z_velocity",":projectile",pjct_z_velocity),
#    (store_mul,":gravity",981,":dt"),
#    (val_div,":gravity",5000),
#    (val_sub,":z_velocity",":gravity"),
#    (party_get_slot,":particle_system_magnitude",":projectile",pjct_particle_system_magnitude),
#    (val_div,":x_velocity",":particle_system_magnitude"),
#    (val_div,":y_velocity",":particle_system_magnitude"),
#    (val_div,":z_velocity",":particle_system_magnitude"),
#    (val_mul,":particle_system_magnitude",10),
#    (try_for_range,":unused",0,":particle_system_magnitude"),
  (particle_system_burst,":particle_system",pos1,10),
#  (position_move_x,pos3,":x_velocity"),
#  (position_move_y,pos3,":y_velocity"),
#  (position_move_z,pos3,":z_velocity"),
#    (try_end),
  (try_end),

  (copy_position,pos2,pos1),
  (copy_position,pos3,pos1),
  (troop_get_slot,":x_velocity","trp_pjct_x_velocity",":projectile"),
  (troop_get_slot,":y_velocity","trp_pjct_y_velocity",":projectile"),
  (troop_get_slot,":z_velocity","trp_pjct_z_velocity",":projectile"),

  (store_mul,":velocity",":x_velocity",":x_velocity"),
  (store_mul,":velocity_b",":y_velocity",":y_velocity"),
  (val_add,":velocity",":velocity_b"),
  (store_mul,":velocity_b",":z_velocity",":z_velocity"),
  (val_add,":velocity",":velocity_b"),
  (store_sqrt,":all_in_all_velocity",":velocity"),

  (store_mul,":gravity",981,":dt"),
  (val_div,":gravity",10000),
  (val_sub,":z_velocity",":gravity"),
  (position_move_x,pos3,":x_velocity"),
  (position_move_y,pos3,":y_velocity"),
  (position_move_z,pos3,":z_velocity"),
  (call_script,"script_position_face_position",pos2,pos3),
  (position_copy_rotation,pos3,pos2),

  (troop_get_slot,":instance","trp_pjct_attach_scene_prop",":projectile"),
  (try_begin),
    (ge,":instance",0),
    (prop_instance_animate_to_position,":instance",pos3,10),
  (try_end),

  #hit an agent?
  (troop_get_slot,":damage","trp_pjct_damage",":projectile"),
  (try_begin),
    (gt,":damage",0),
    (troop_get_slot,":agent_deliverer","trp_pjct_source_agent",":projectile"),
    (try_for_agents,":agent"),
      (agent_is_alive,":agent"),
      (agent_get_position,pos3,":agent"),
      (position_move_z,pos3,100),
      (position_transform_position_to_local,pos4,pos2,pos3),
      (position_get_y,":pos_y",pos4),
      (is_between,":pos_y",0,":all_in_all_velocity"),
      (position_get_x,":pos_x",pos4),
      (is_between,":pos_x",-100,100),
      (position_get_z,":pos_z",pos4),
      (is_between,":pos_z",-100,100),
      (call_script,"script_agent_deliver_damage_to_agent",":agent_deliverer",":agent",":damage"),
      (assign,":explosition",1),
    (try_end),
  (try_end),

  (position_get_z,":pos_z",pos1),

  (copy_position,pos2,pos1),
  (position_set_z,pos2,10000),
  (position_set_z_to_ground_level,pos2),
  (position_get_z,":ground",pos2),
  (val_sub,":pos_z",":ground"),
  (assign,":explosition",0),

  (try_begin),
    (troop_slot_eq,"trp_pjct_check_collision",":projectile",0),
    (position_get_z,":pos_z",pos1),
    (try_begin),
      (le, ":pos_z","$ground_level"),
      (assign,":ground","$ground_level"),
      (assign,":pos_z",9),
    (else_try),
      (assign,":pos_z",10),
    (try_end),
  (try_end),

  (try_begin),
  #check explosition countdown
    (troop_get_slot,":explosion_countdown","trp_pjct_explosion_countdown",":projectile"),
    (gt,"$timer",":explosion_countdown"),
    (assign,":explosition",1),
  (else_try),
  #ground hit
    (lt,":pos_z",10),
    (troop_get_slot,":explode_on_ground_hit","trp_pjct_explode_on_ground_hit",":projectile"),
    (try_begin),
      (eq,":explode_on_ground_hit",1),
      (assign,":explosition",1),
    (else_try),
      (troop_get_slot,":bounce_effect","trp_pjct_bounce_effect",":projectile"),
      (troop_get_slot,":x_velocity","trp_pjct_x_velocity",":projectile"),
      (troop_get_slot,":y_velocity","trp_pjct_y_velocity",":projectile"),
      (troop_get_slot,":z_velocity","trp_pjct_z_velocity",":projectile"),
      (store_mul,":gravity_velocity",981,":dt"),
      (val_div,":gravity_velocity",10000),
      (val_sub,":z_velocity",":gravity_velocity"),
      (val_mul,":x_velocity",":bounce_effect"),
      (val_mul,":y_velocity",":bounce_effect"),
      (val_mul,":z_velocity",":bounce_effect"),
      (val_div,":z_velocity",-10),
      (val_div,":x_velocity",10),
      (val_div,":y_velocity",10),
      (troop_set_slot,"trp_pjct_x_velocity",":projectile",":x_velocity"),
      (troop_set_slot,"trp_pjct_y_velocity",":projectile",":y_velocity"),
      (troop_set_slot,"trp_pjct_z_velocity",":projectile",":z_velocity"),
      (troop_set_slot,"trp_pjct_emit_time",":projectile","$timer"),
      (troop_set_slot,"trp_pjct_x",":projectile",":x_pos"),
      (troop_set_slot,"trp_pjct_y",":projectile",":y_pos"),
      (val_add,":ground",10),
      (troop_set_slot,"trp_pjct_z",":projectile",":ground"),
    (try_end),
  (try_end),

  #explosition
  (try_begin),
    (eq,":explosition",1),
    (troop_get_slot,":explosive","trp_pjct_explosive",":projectile"),
    (try_begin),
      (eq,":explosive",1),
      (assign,":one_explosion_or_more",1),
      (troop_get_slot,":explosion_area","trp_pjct_explosion_area",":projectile"),
      (troop_get_slot,":explosion_damage","trp_pjct_explosion_damage",":projectile"),
      (troop_get_slot,":agent_deliverer","trp_pjct_source_agent",":projectile"),
      (particle_system_burst, "psys_explosion_fire_b", pos1, 40),
#      (particle_system_burst, "psys_explosion_fire", pos1, 10),
#      (particle_system_burst, "psys_explosion_smoke", pos1, 60),
      (play_sound,"snd_loud_explosion"),
      (try_for_agents,":agent"),
       (agent_is_alive,":agent"),
       (agent_is_human,":agent"),
       (agent_get_position,pos2,":agent"),
       (position_move_z,pos2,100),
       (get_distance_between_positions,":distance",pos1,pos2),
       (gt,":explosion_area",":distance"),
       (store_sub,":distance_inverse",":explosion_area",":distance"),
       (val_mul,":explosion_damage",":distance_inverse"),
       (val_div,":explosion_damage",":explosion_area"),
       (call_script,"script_agent_deliver_damage_to_agent",":agent_deliverer",":agent",":explosion_damage"),
      (try_end),
      (val_mul,":explosion_damage",2),
      (val_mul,":explosion_area",2),
      (try_for_agents,":agent"),
       (agent_is_alive,":agent"),
       (neg|agent_is_human,":agent"),
       (agent_get_position,pos2,":agent"),
       (position_move_z,pos2,100),
       (get_distance_between_positions,":distance",pos1,pos2),
       (gt,":explosion_area",":distance"),
       (store_sub,":distance_inverse",":explosion_area",":distance"),
       (val_mul,":explosion_damage",":distance_inverse"),
       (val_div,":explosion_damage",":explosion_area"),
       (call_script,"script_agent_deliver_damage_to_agent",":agent_deliverer",":agent",":explosion_damage"),
      (try_end),
      (scene_prop_get_num_instances,":num_instances","spr_explosion"),
      (gt,":num_instances",0),
      (scene_prop_get_instance,":instance", "spr_explosion", 0),
      (position_copy_origin,pos2,pos1),
      (prop_instance_set_position,":instance",pos2),
      (position_move_z,pos2,1000),
      (prop_instance_animate_to_position,":instance",pos2,175),
    (try_end),

#destroy particle
    (troop_set_slot,"trp_pjct_active",":projectile",0),

    (troop_get_slot,":instance","trp_pjct_attach_scene_prop",":projectile"),
    (try_begin),
      (ge,":instance",0),
      (troop_set_slot,"trp_instance_attached_to",":instance",0),
    (try_end),
  (try_end),
(try_end),
(eq,":one_explosion_or_more",1),
],
[
      (scene_prop_get_num_instances,":num_instances","spr_explosion"),
      (gt,":num_instances",0),
      (scene_prop_get_instance,":instance", "spr_explosion", 0),
      (prop_instance_get_position,pos2,":instance"),
      (position_move_z,pos2,-1000),
      (prop_instance_animate_to_position,":instance",pos2,300),
])
#Highlander end--------------------------------------

common_battle_mission_start = (
  ti_before_mission_start, 0, 0, [],
  [
    (team_set_relation, 0, 2, 1),
    (team_set_relation, 1, 3, 1),
    (call_script, "script_change_banners_and_chest"),
    ])

common_battle_tab_press = (
  ti_tab_pressed, 0, 0, [],
  [
    (try_begin),
      (eq, "$battle_won", 1),
      (call_script, "script_count_mission_casualties_from_agents"),
    (call_script, "script_flush_gatesys_cache"),
      (finish_mission,0),
  (else_try),
    (eq, "$pin_player_fallen", 1),
    (call_script, "script_simulate_retreat", 5, 20),
    (str_store_string, s5, "str_retreat"),
    (call_script, "script_count_mission_casualties_from_agents"),
    (set_mission_result, -1),
    (finish_mission,0),
    (else_try),
      (call_script, "script_cf_check_enemies_nearby"),
      (question_box,"str_do_you_want_to_retreat"),
    (else_try),
      (display_message,"str_can_not_retreat"),
    (try_end),
    ])

common_arena_fight_tab_press = (
  ti_tab_pressed, 0, 0, [],
  [
    (question_box,"str_give_up_fight"),
    ])

#SW BSG integration - new popup box
common_space_battle_tab_press = (
  ti_tab_pressed, 0, 0, [],
  [
    (question_box,"str_give_up_training"),
    ])

common_custom_battle_tab_press = (
  ti_tab_pressed, 0, 0, [],
  [
    (try_begin),
      (neq, "$g_battle_result", 0),
      (call_script, "script_custom_battle_end"),
    (call_script, "script_flush_gatesys_cache"),
      (finish_mission),
    (else_try),
      (question_box,"str_give_up_fight"),
    (try_end),
    ])

custom_battle_check_victory_condition = (
  1, 60, ti_once,
  [
    (store_mission_timer_a,reg(1)),
    (ge,reg(1),10),
    (all_enemies_defeated, 2),
#    (neg|main_hero_fallen, 0),
    (set_mission_result,1),
    (display_message,"str_msg_battle_won"),
    (assign, "$battle_won",1),
    (assign, "$g_battle_result", 1),
    ],
  [
    (call_script, "script_custom_battle_end"),
    (finish_mission, 1),
    ])

custom_battle_check_defeat_condition = (
  1, 4, ti_once,
  [
    (main_hero_fallen),
    (assign,"$g_battle_result",-1),
    ],
  [
    (call_script, "script_custom_battle_end"),
    (finish_mission),
    ])

common_battle_victory_display = (
  4, 0, 0, [],
  [
    (eq,"$battle_won",1),
    (display_message,"str_msg_battle_won"),
    ])

common_siege_question_answered = (
  ti_question_answered, 0, 0, [],
   [
     (store_trigger_param_1,":answer"),
     (eq,":answer",0),
     (assign, "$pin_player_fallen", 0),
     (get_player_agent_no, ":player_agent"),
     (agent_get_team, ":agent_team", ":player_agent"),
     (try_begin),
       (neq, "$attacker_team", ":agent_team"),
       (neq, "$attacker_team_2", ":agent_team"),
       (str_store_string, s5, "str_siege_continues"),
       (call_script, "script_simulate_retreat", 8, 15),
     (else_try),
       (str_store_string, s5, "str_retreat"),
       (call_script, "script_simulate_retreat", 5, 20),
     (try_end),
     (call_script, "script_count_mission_casualties_from_agents"),
     (finish_mission,0),
     ])

common_custom_battle_question_answered = (
   ti_question_answered, 0, 0, [],
   [
     (store_trigger_param_1,":answer"),
     (eq,":answer",0),
     (assign, "$g_battle_result", -1),
     (call_script, "script_custom_battle_end"),
     (finish_mission),
     ])

common_custom_siege_init = (
  0, 0, ti_once, [],
  [
    (assign, "$g_battle_result", 0),
    (call_script, "script_music_set_situation_with_culture", mtf_sit_siege),
    ])

common_siege_init = (
  0, 0, ti_once, [],
  [
    (assign,"$battle_won",0),
    (assign,"$defender_reinforcement_stage",0),
    (assign,"$attacker_reinforcement_stage",0),
    (assign,"$g_presentation_battle_active", 0),
    (call_script, "script_music_set_situation_with_culture", mtf_sit_siege),
    ])

common_music_situation_update = (
  30, 0, 0, [],
  [
    (call_script, "script_combat_music_set_situation_with_culture"),
    ])

common_siege_ai_trigger_init = (
  0, 0, ti_once,
  [
    (assign, "$defender_team", 0),
    (assign, "$attacker_team", 1),
    (assign, "$defender_team_2", 2),
    (assign, "$attacker_team_2", 3),
    ], [])

common_siege_ai_trigger_init_2 = (
  0, 0, ti_once,
  [
    (set_show_messages, 0),
    (entry_point_get_position, pos10, 10),
    (team_give_order, "$defender_team", grc_infantry, mordr_hold),
    (team_give_order, "$defender_team", grc_infantry, mordr_stand_closer),
    (team_give_order, "$defender_team", grc_infantry, mordr_stand_closer),
    (team_give_order, "$defender_team", grc_archers, mordr_stand_ground),
    (team_set_order_position, "$defender_team", grc_everyone, pos10),
    (team_give_order, "$defender_team_2", grc_infantry, mordr_hold),
    (team_give_order, "$defender_team_2", grc_infantry, mordr_stand_closer),
    (team_give_order, "$defender_team_2", grc_infantry, mordr_stand_closer),
    (team_give_order, "$defender_team_2", grc_archers, mordr_stand_ground),
    (team_set_order_position, "$defender_team_2", grc_everyone, pos10),
    (set_show_messages, 1),
    ], [])

common_siege_ai_trigger_init_after_2_secs = (
  0, 2, ti_once, [],
  [
    (try_for_agents, ":agent_no"),
      (agent_set_slot, ":agent_no", slot_agent_is_not_reinforcement, 1),
    (try_end),
    ])

common_siege_defender_reinforcement_check = (
  3, 0, 5, [],
  [(lt, "$defender_reinforcement_stage", 7),
   (store_mission_timer_a,":mission_time"),
   (ge,":mission_time",10),
   (store_normalized_team_count,":num_defenders",0),
   (lt,":num_defenders",10),
   (add_reinforcements_to_entry,4, 7),
   (val_add,"$defender_reinforcement_stage",1),
   (try_begin),
     (ge, "$defender_reinforcement_stage", 2),
     (set_show_messages, 0),
     (team_give_order, "$defender_team", grc_infantry, mordr_charge), #AI desperate charge:infantry!!!
     (team_give_order, "$defender_team_2", grc_infantry, mordr_charge), #AI desperate charge:infantry!!!
     (set_show_messages, 1),
     (ge, "$defender_reinforcement_stage", 4),
     (set_show_messages, 0),
     (team_give_order, "$defender_team", grc_everyone, mordr_charge), #AI desperate charge: everyone!!!
     (team_give_order, "$defender_team_2", grc_everyone, mordr_charge), #AI desperate charge: everyone!!!
     (set_show_messages, 1),
   (try_end),
   ])


common_siege_defender_reinforcement_archer_reposition = (
  2, 0, 0,
  [
    (gt, "$defender_reinforcement_stage", 0),
    ],
  [
    (call_script, "script_siege_move_archers_to_archer_positions"),
    ])

common_siege_attacker_reinforcement_check = (
  1, 0, 5,
  [
    (lt,"$attacker_reinforcement_stage",5),
    (store_mission_timer_a,":mission_time"),
    (ge,":mission_time",10),
    (store_normalized_team_count,":num_attackers",1),
    (lt,":num_attackers",6)
    ],
  [
    (add_reinforcements_to_entry, 1, 8),
    (val_add,"$attacker_reinforcement_stage", 1),
    ])

common_siege_attacker_do_not_stall = (
  5, 0, 0, [],
  [ #Make sure attackers do not stall on the ladders...
    (try_for_agents, ":agent_no"),
      (agent_is_human, ":agent_no"),
      (agent_is_alive, ":agent_no"),
      (agent_get_team, ":agent_team", ":agent_no"),
      (this_or_next|eq, ":agent_team", "$attacker_team"),
      (eq, ":agent_team", "$attacker_team_2"),
##      (neg|agent_is_defender, ":agent_no"),
      (agent_ai_set_always_attack_in_melee, ":agent_no", 1),
    (try_end),
    ])

common_battle_check_friendly_kills = (
  2, 0, 0, [],
  [
    (call_script, "script_check_friendly_kills"),
    ])

common_battle_check_victory_condition = (
  1, 60, ti_once,
  [
    (store_mission_timer_a,reg(1)),
    (ge,reg(1),10),
    (all_enemies_defeated, 5),
 #   (neg|main_hero_fallen, 0),
    (set_mission_result,1),
    (display_message,"str_msg_battle_won"),
    (assign,"$battle_won",1),
    (assign, "$g_battle_result", 1),
    (call_script, "script_play_victorious_sound"),
    ],
  [
    (call_script, "script_count_mission_casualties_from_agents"),
    (finish_mission, 1),
    ])

common_battle_victory_display = (
  4, 0, 0, [],
  [
    (eq,"$battle_won",1),
    (display_message,"str_msg_battle_won"),
    ])

common_siege_refill_ammo = (
  120, 0, 0, [],
  [#refill ammo of defenders every two minutes.
    (get_player_agent_no, ":player_agent"),
    (try_for_agents,":cur_agent"),
      (neq, ":cur_agent", ":player_agent"),
      (agent_is_alive, ":cur_agent"),
      (agent_is_human, ":cur_agent"),
##      (agent_is_defender, ":cur_agent"),
      (agent_get_team, ":agent_team", ":cur_agent"),
      (this_or_next|eq, ":agent_team", "$defender_team"),
      (eq, ":agent_team", "$defender_team_2"),
      (agent_refill_ammo, ":cur_agent"),
    (try_end),
    ])

common_siege_check_defeat_condition = (
  1, 4, ti_once,
  [
    (main_hero_fallen)
    ],
  [
    (assign, "$pin_player_fallen", 1),
  (display_message, "@You have been knocked out by the enemy. Watch your men continue the fight without you or press Tab to retreat."),
  (call_script,"script_get_key","$deathcam_forward_key"),
  (str_store_string,s1,s13),
  (call_script,"script_get_key","$deathcam_backward_key"),
  (str_store_string,s2,s13),
  #(display_message, "@If you choose to watch the fight you can use the M and N keys to change your camera view."),
  (display_message, "@If you choose to watch the fight you can use the '{s1}' and '{s2}' keys to change your camera view."),
    # (get_player_agent_no, ":player_agent"),
    # (agent_get_team, ":agent_team", ":player_agent"),
    # (try_begin),
      # (neq, "$attacker_team", ":agent_team"),
      # (neq, "$attacker_team_2", ":agent_team"),
      # (str_store_string, s5, "str_siege_continues"),
      # (call_script, "script_simulate_retreat", 8, 15),
    # (else_try),
      # (str_store_string, s5, "str_retreat"),
      # (call_script, "script_simulate_retreat", 5, 20),
    # (try_end),
    # (assign, "$g_battle_result", -1),
    # (set_mission_result,-1),
    # (call_script, "script_count_mission_casualties_from_agents"),
    # (finish_mission,0),
    ])

from module_info import wb_compile_switch as is_a_wb_mt

common_battle_order_panel = (0, 0, 0, [],
	[
	    (try_begin),
	      #-- {show up the ticker on backspace}
	      (game_key_clicked, gk_view_orders),
	      (neq, "$g_presentation_battle_active", 1),
	      #--

	      (start_presentation, "prsnt_battle"),
	    (try_end),
	]
	 + (is_a_wb_mt==1 and 
	[
	    #swy-- what a shamefur dispray!
	    (try_begin),
	      (game_key_clicked, gk_view_orders),
	      #-- {guard against rogue Esc presses that kill the ticker without notice}
	      (eq, "$g_presentation_battle_active", 1),
	      (is_presentation_active, "prsnt_battle"),
	      #--

	      (assign, "$g_presentation_battle_active", 0),
	      (set_show_messages, 1),

	      (try_for_agents, ":cur_agent"),
	        (agent_set_slot, ":cur_agent", slot_agent_map_overlay_id, 0),
	      (try_end),

	      (presentation_set_duration, 0),
	    #swy-- what a shamefur dispray!
	    (else_try),
	      #-- {guard against rogue Esc presses that kill the ticker without notice}
	      (eq, "$g_presentation_battle_active", 1),
	      (neg|is_presentation_active, "prsnt_battle"),
	      #--

	      (assign, "$g_presentation_battle_active", 0),
	      (set_show_messages, 1),

	      (try_for_agents, ":cur_agent"),
	        (agent_set_slot, ":cur_agent", slot_agent_map_overlay_id, 0),
	      (try_end),

	      (presentation_set_duration, 0),
	    (try_end)
	    
	] or [])
)

common_battle_order_panel_tick = (0.1, 0, 0, [], [ (eq, "$g_presentation_battle_active", 1),(call_script, "script_update_order_panel_statistics_and_map")])

common_battle_inventory = (
  ti_inventory_key_pressed, 0, 0, [],
  [
    (display_message,"str_use_baggage_for_inventory"),
    ])

common_inventory_not_available = (
  ti_inventory_key_pressed, 0, 0,
  [
    (display_message, "str_cant_use_inventory_now"),
    ], [])

common_siege_init_ai_and_belfry = (
  0, 0, ti_once,
  [
    (call_script, "script_cf_siege_init_ai_and_belfry"),
    ], [])

common_siege_move_belfry = (
  0, 0, ti_once,
  [
    (call_script, "script_cf_siege_move_belfry"),
    ], [])

common_siege_rotate_belfry = (
  0, 2, ti_once,
  [
    (call_script, "script_cf_siege_rotate_belfry_platform"),
    ],
  [
    (assign, "$belfry_positioned", 3),
    ])

common_siege_assign_men_to_belfry = (
  0, 0, ti_once,
  [
    (call_script, "script_cf_siege_assign_men_to_belfry"),
    ], [])

#SW - Chronicles of Talera regen rate script by Kardiophylax START
common_regeneration_store_info = (
  0, 0, ti_once, [], [                      # run this only once at the start of battle
   (get_player_agent_no, "$agent_for_player"),             # these aren't required, I use them for other things
   #(agent_get_team, "$agent_for_player_team", "$agent_for_player"),  # these aren't required, I use them for other things

   (try_for_agents, "$talera_agent"),
      #(agent_set_slot, "$talera_agent", slot_agent_regen_rate, 0),  # this is probably redundant, I think all agents have new, fresh ids when created
   (try_end),

   (try_for_agents, "$talera_agent"),
       (agent_get_troop_id, "$agent_troop_type", "$talera_agent"),
       (try_begin),
          (is_between, "$agent_troop_type", kings_begin, kings_end),
          (agent_set_slot, "$talera_agent", slot_agent_regen_rate, 4),
       (else_try),
          (is_between, "$agent_troop_type", faction_heroes_begin, faction_heroes_end),
          (agent_set_slot, "$talera_agent", slot_agent_regen_rate, 3),
       (try_end),
   (try_end),

   # for testing
   (agent_set_slot, "$agent_for_player", slot_agent_regen_rate, 4),
  ]
)

common_regeneration = (
1, 0, 0, [], [
    (try_for_agents, "$talera_agent"),
       (agent_is_alive, "$talera_agent"),
       (agent_get_slot, ":regen_rate", "$talera_agent", slot_agent_regen_rate),
       (ge, ":regen_rate", 1),
       (store_agent_hit_points, ":agent_health", "$talera_agent", 1),
       (val_add, ":agent_health", ":regen_rate"),
       (agent_set_hit_points, "$talera_agent", ":agent_health", 1),
    (try_end),
  ]
)
#SW - Chronicles of Talera regen rate script by Kardiophylax END

#SW - start of special weapon noise by Jinnai - http://forums.taleworlds.net/index.php/topic,56917.msg1475545.html#msg1475545
lightsaber_noise_idle = (
  1, 0, 0, [],
    [
    (try_for_agents, ":agent"),
      (agent_is_alive, ":agent"),
      (agent_is_human, ":agent"),
      (agent_get_wielded_item, ":handone", ":agent", 0),
      (agent_get_wielded_item, ":handtwo", ":agent", 1),
      #(this_or_next|eq, ":handone", "itm_special_weapon"),
      #(this_or_next|eq, ":handone", "itm_lightsaber_green"),
      (this_or_next|is_between, ":handone", lightsaber_noise_begin, lightsaber_noise_end),
      #(eq, ":handtwo", "itm_special_weapon"),
      #(eq, ":handtwo", "itm_lightsaber_green"),
      (is_between, ":handtwo", lightsaber_noise_begin, lightsaber_noise_end),
      #(agent_play_sound,":agent","snd_special_weapon_idle"), #This assumes it's a 1 second long clip, change trigger length if it's different
      (agent_play_sound,":agent","snd_lightsaber_idle"), #This assumes it's a 1 second long clip, change trigger length if it's different
    (try_end),
    ]
)
lightsaber_noise_agent = (
  0.1, 0, 0, [],
    [
    (get_player_agent_no, ":player_agent"),
    (try_for_agents, ":agent"),
      (agent_is_alive, ":agent"),
      (agent_is_human, ":agent"),
      (neq, ":agent", ":player_agent"),    #we have a different trigger for the player_agent
      (agent_get_wielded_item, ":handone", ":agent", 0),
      (agent_get_wielded_item, ":handtwo", ":agent", 1),
      #(this_or_next|eq, ":handone", "itm_special_weapon"),
      #(this_or_next|eq, ":handone", "itm_lightsaber_green"),
      (this_or_next|is_between, ":handone", lightsaber_noise_begin, lightsaber_noise_end),
      #(eq, ":handtwo", "itm_special_weapon"),
      #(eq, ":handtwo", "itm_lightsaber_green"),
      (is_between, ":handtwo", lightsaber_noise_begin, lightsaber_noise_end),
      (agent_get_combat_state, ":state", ":agent"),
      (try_begin),
        (eq,":state",4), #This is the combat state for melee swing
        (agent_slot_eq,":agent",slot_agent_attack_sound, 0),
        (agent_set_slot, ":agent", slot_agent_attack_sound, 1),
        #(agent_play_sound,":agent","snd_special_weapon_attack"),
        (agent_play_sound,":agent","snd_lightsaber_swing"),
      (else_try),
        (neq,":state",4),
        (agent_set_slot, ":agent", slot_agent_attack_sound, 0),
      (try_end),
    (try_end),
    ]
)
# old code (plays sound when you click the attack key)
lightsaber_noise_player = (
  0, 0, 1,   #there's a 1 second refresh timer to give the attack sound time to complete
    [
    (neg|conversation_screen_is_active),
    (game_key_clicked, gk_attack),
    (neg|game_key_is_down, gk_defend),
    ],
    [
      (get_player_agent_no, ":agent"),
      (agent_is_alive, ":agent"),
      (agent_get_wielded_item, ":handone", ":agent", 0),
      (agent_get_wielded_item, ":handtwo", ":agent", 1),
      (this_or_next|is_between, ":handone", lightsaber_noise_begin, lightsaber_noise_end),
      (is_between, ":handtwo", lightsaber_noise_begin, lightsaber_noise_end),
      (agent_play_sound,":agent","snd_lightsaber_swing"),
    ]
)

# # new code (plays sound when you release the attack key, uses play_sound because agent_play_sound didn't work) - however, the code doesn't sound great when you jam on the buttons a lot so I went back to the old method....
# lightsaber_noise_player = (
  # 0, 0, 0,  # check, delay, re-arm interval (re-arm after 1 second so the sound has a change to play, this doesn't work for some reason?)
    # [
      # (this_or_next|game_key_is_down, gk_attack),
      # (eq, "$attack_key", 1),  #attack key was previously down (0 = up, 1 = down,)
      # (neg|conversation_screen_is_active),  #don't play sound when on a conversation screen
      # (neg|eq, "$play_sound_lock", 1),
    # ],
    # [
      # (assign, "$play_sound_lock", 1),
      # (get_player_agent_no, ":player_agent"),
      # (agent_is_alive, ":player_agent"),      # only check if player is alive
      # (try_begin),
      # (game_key_is_down, gk_attack),
      # (assign, "$attack_key", 1),  #attack key is down (0 = up, 1 = down)
      # (else_try),  #attack key was just released
      # (assign, "$attack_key", 0),  #attack key was released (0 = up, 1 = down)
      # #(display_message, "@attack key was released."),
      # (agent_get_wielded_item, ":handone", ":player_agent", 0),
      # (agent_get_wielded_item, ":handtwo", ":player_agent", 1),
      # (this_or_next|is_between, ":handone", lightsaber_noise_begin, lightsaber_noise_end),
      # (is_between, ":handtwo", lightsaber_noise_begin, lightsaber_noise_end),
      # (play_sound,"snd_lightsaber_swing"),
      # #(play_sound,"snd_lightsaber_swing", sf_2d),
      # (try_end),
      # (assign, "$play_sound_lock", 0),
    # ]
# )

# lightsaber_noise_player = (
  # 0, 0, 0,
    # [
      # (this_or_next|game_key_is_down, gk_attack),
      # (eq, "$attack_key", 1),  #attack key was previously down (0 = up, 1 = down, 2 = released)
      # (neq, "$attack_key", 2),  #attack key was just released (0 = up, 1 = down, 2 = released)
    # ],
    # [
      # (try_begin),
      # (game_key_is_down, gk_attack),
      # (assign, "$attack_key", 1),  #attack key is down (0 = up, 1 = down, 2 = released)
      # (else_try),  #attack key was just released
      # (assign, "$attack_key", 2),  #attack key was released (0 = up, 1 = down, 2 = released)
      # (display_message, "@attack key was released."),
      # (try_end),
    # ]
# )
# # new code (plays sound when you release the attack key)
# lightsaber_noise_player_2 = (
  # 0, 0, 1.5,  #there's a 1.5 second refresh timer to give the attack sound time to complete
    # [
      # (eq, "$attack_key", 2),  #attack key was released (0 = up, 1 = down, 2 = released)
    # ],
    # [
      # (display_message, "@now play a custom sound since the attack key was released."),
      # (get_player_agent_no, ":player_agent"),
      # (try_begin),
        # (agent_is_alive, ":player_agent"),
      # (agent_get_wielded_item, ":handone", ":player_agent", 0),
      # (agent_get_wielded_item, ":handtwo", ":player_agent", 1),
      # (this_or_next|is_between, ":handone", lightsaber_noise_begin, lightsaber_noise_end),
      # (is_between, ":handtwo", lightsaber_noise_begin, lightsaber_noise_end),
      # (agent_play_sound,":player_agent","snd_lightsaber_swing"),
      # (try_end),
      # (assign, "$attack_key", 0),  #attack key is up (0 = up, 1 = down, 2 = released)
    # ]
# )

#SW - end of special weapon noise by Jinnai

# #SW - new warcry noise
# warcry_player = (
  # 0, 0, 1,  #there's a 1 second refresh timer to give the sound time to complete
    # [
      # #(key_clicked, key_e),
      # (key_clicked, "$warcry_key"),
      # (neg|conversation_screen_is_active),
    # ],
    # [
      # #(display_message, "@warcry_player started."),    #debug
      # (get_player_agent_no, ":agent"),
      # (agent_is_alive, ":agent"),
      # #(troop_get_type, ":race", "$g_player_troop"),
      # (troop_get_type, ":race", ":agent"),
      # (try_begin),
      # (eq, ":race", 1),  #female
      # (agent_play_sound,":agent","snd_woman_victory"),
      # (agent_set_animation, ":agent", "anim_cheer"),
      # (else_try),
      # (agent_play_sound,":agent","snd_man_victory"),
      # (agent_set_animation, ":agent", "anim_cheer"),
      # (try_end),
      # #(display_message, "@warcry_player finished."),    #debug
    # ]
# )
# #SW - end of new warcry noise

common_switch_sw_scene_props = (
  ti_before_mission_start, 0, 0, [],
  [
    #get the current towns faction
    (store_faction_of_party, ":center_faction", "$current_town"),
    (try_begin),
      (eq, ":center_faction", "fac_galacticempire"),  #empire
      (assign, ":faction_sign_begin", sw_empire_sign_begin),
      (assign, ":faction_sign_end", sw_empire_sign_end),
      (assign, ":faction_poster_begin", sw_empire_poster_begin),
      (assign, ":faction_poster_end", sw_empire_poster_end),
    (else_try),
      (eq, ":center_faction", "fac_rebelalliance"),  #rebel
      (assign, ":faction_sign_begin", sw_rebel_sign_begin),
      (assign, ":faction_sign_end", sw_rebel_sign_end),
      (assign, ":faction_poster_begin", sw_rebel_poster_begin),
      (assign, ":faction_poster_end", sw_rebel_poster_end),
    (else_try),
      #other
      (assign, ":faction_sign_begin", sw_generic_sign_begin),
      (assign, ":faction_sign_end", sw_generic_sign_end),
      (assign, ":faction_poster_begin", sw_generic_poster_begin),
      (assign, ":faction_poster_end", sw_generic_poster_end),
    (try_end),

    #SW - replace signs
    (store_random_in_range, ":sign", sw_all_sign_begin, sw_all_sign_end),
    (replace_scene_props, "spr_sw_sign_random_all_1", ":sign"),
    (store_random_in_range, ":sign", sw_all_sign_begin, sw_all_sign_end),
    (replace_scene_props, "spr_sw_sign_random_all_2", ":sign"),
    (store_random_in_range, ":sign", sw_all_sign_begin, sw_all_sign_end),
    (replace_scene_props, "spr_sw_sign_random_all_3", ":sign"),
    (store_random_in_range, ":sign", sw_all_sign_begin, sw_all_sign_end),
    (replace_scene_props, "spr_sw_sign_random_all_4", ":sign"),
    (store_random_in_range, ":sign", ":faction_sign_begin", ":faction_sign_end"),
    (replace_scene_props, "spr_sw_sign_random_galacticempire", ":sign"),
    (store_random_in_range, ":sign", ":faction_sign_begin", ":faction_sign_end"),
    (replace_scene_props, "spr_sw_sign_random_rebelalliance", ":sign"),
    (store_random_in_range, ":sign", ":faction_sign_begin", ":faction_sign_end"),
    (replace_scene_props, "spr_sw_sign_random_huttcartel", ":sign"),
    (store_random_in_range, ":sign", ":faction_sign_begin", ":faction_sign_end"),
    (replace_scene_props, "spr_sw_sign_random_galacticempire", ":sign"),
    (store_random_in_range, ":sign", sw_generic_sign_begin, sw_generic_sign_end),
    (replace_scene_props, "spr_sw_sign_random_generic_1", ":sign"),
    (store_random_in_range, ":sign", sw_generic_sign_begin, sw_generic_sign_end),
    (replace_scene_props, "spr_sw_sign_random_generic_2", ":sign"),
    (store_random_in_range, ":sign", sw_generic_sign_begin, sw_generic_sign_end),
    (replace_scene_props, "spr_sw_sign_random_generic_3", ":sign"),
    (store_random_in_range, ":sign", sw_generic_sign_begin, sw_generic_sign_end),
    (replace_scene_props, "spr_sw_sign_random_generic_4", ":sign"),
    #SW - replace posters
    (store_random_in_range, ":poster", sw_all_poster_begin, sw_all_poster_end),
    (replace_scene_props, "spr_sw_poster_random_all_1", ":poster"),
    (store_random_in_range, ":poster", sw_all_poster_begin, sw_all_poster_end),
    (replace_scene_props, "spr_sw_poster_random_all_2", ":poster"),
    (store_random_in_range, ":poster", sw_all_poster_begin, sw_all_poster_end),
    (replace_scene_props, "spr_sw_poster_random_all_3", ":poster"),
    (store_random_in_range, ":poster", sw_all_poster_begin, sw_all_poster_end),
    (replace_scene_props, "spr_sw_poster_random_all_4", ":poster"),
    (store_random_in_range, ":poster", ":faction_poster_begin", ":faction_poster_end"),
    (replace_scene_props, "spr_sw_poster_random_towngalacticempire", ":poster"),
    (store_random_in_range, ":poster", ":faction_poster_begin", ":faction_poster_end"),
    (replace_scene_props, "spr_sw_poster_random_townrebelalliance", ":poster"),
    (store_random_in_range, ":poster", ":faction_poster_begin", ":faction_poster_end"),
    (replace_scene_props, "spr_sw_poster_random_townhuttcartel", ":poster"),
    (store_random_in_range, ":poster", ":faction_poster_begin", ":faction_poster_end"),
    (replace_scene_props, "spr_sw_poster_random_townfaction_4", ":poster"),
    (store_random_in_range, ":poster", sw_generic_poster_begin, sw_generic_poster_end),
    (replace_scene_props, "spr_sw_poster_random_generic_1", ":poster"),
    (store_random_in_range, ":poster", sw_generic_poster_begin, sw_generic_poster_end),
    (replace_scene_props, "spr_sw_poster_random_generic_2", ":poster"),
    (store_random_in_range, ":poster", sw_generic_poster_begin, sw_generic_poster_end),
    (replace_scene_props, "spr_sw_poster_random_generic_3", ":poster"),
    (store_random_in_range, ":poster", sw_generic_poster_begin, sw_generic_poster_end),
    (replace_scene_props, "spr_sw_poster_random_generic_4", ":poster"),

    ])

common_agent_droid_refill_trigger = (
  30, 0, 0,  # check every 5 seconds
    [],
    [
      #(display_message, "@running common_agent_droid_refill_trigger"),  #debug
      (get_player_agent_no, ":player_agent"),
      (assign, ":player_agent_refilled_ammo", 0),
      (assign, ":player_agent_refilled_health", 0),
      (assign, ":power_droid_agent", 0),
      (assign, ":med_droid_agent", 0),
      (try_for_agents, ":agent"),
        (agent_is_alive, ":agent"),  #so we don't try dead agents
        (agent_is_human,":agent"),  #agent is a human
        #(agent_get_troop_id, ":agent_troop", ":agent"),
        #(eq, ":agent_troop", "trp_power_droid"),
        #(display_message, "@trp_power_droid found!"),  #debug
        (try_begin),
          #check for power droids to refill ammo
          (this_or_next|agent_has_item_equipped,":agent","itm_power_droid_grey"),
          (this_or_next|agent_has_item_equipped,":agent","itm_power_droid_snow"),
          (agent_has_item_equipped,":agent","itm_power_droid_tan"),
          (agent_get_position,pos1,":agent"),
          (agent_get_team,":agent_team", ":agent"),
          (try_for_agents, ":chosen"),
            (agent_is_alive, ":chosen"),  #so we don't try dead agents
            (agent_is_human,":chosen"),  #agent is a human
            (agent_get_team  ,":chosen_team", ":chosen"),
            (eq, ":agent_team", ":chosen_team"),
            (agent_get_position, pos2, ":chosen"),
            (get_distance_between_positions,":dist",pos1,pos2),
            (lt,":dist",400),  #SW - how close they have to be to refill ammo
            (agent_refill_ammo, ":chosen"),
            (eq, ":chosen",":player_agent"),
            (assign, ":player_agent_refilled_ammo", 1),
            (assign, ":power_droid_agent", ":agent"),  #remember an agent that refilled the players ammo
          (try_end),
        (else_try),
          #check for med droids to refill health
          (agent_has_item_equipped,":agent","itm_fxseries_droid_armor"),
          (agent_get_position,pos1,":agent"),
          (agent_get_team,":agent_team", ":agent"),
          (try_for_agents, ":chosen"),
            (agent_is_alive, ":chosen"),  #so we don't try dead agents
            (agent_is_human,":chosen"),  #agent is a human
            (agent_get_team  ,":chosen_team", ":chosen"),
            (eq, ":agent_team", ":chosen_team"),
            (agent_get_position, pos2, ":chosen"),
            (get_distance_between_positions,":dist",pos1,pos2),
            (lt,":dist",400),  #SW - how close they have to be to refill ammo
            (store_agent_hit_points,":chosen_health",":chosen",0),  #relative number, 0-100%
            (lt, ":chosen_health", 100),
            (val_add, ":chosen_health", 5),  #add 5%
            (try_begin),
              (gt, ":chosen_health", 100),
              (assign, ":chosen_health", 100),    #so we don't try and set hit points > 100%
            (try_end),
            (agent_set_hit_points,":chosen",":chosen_health",0),  #relative number, 0-100%
            (eq, ":chosen",":player_agent"),
            (assign, ":player_agent_refilled_health", 1),
            (assign, ":med_droid_agent", ":agent"),  #remember an agent that refilled the players ammo
          (try_end),
        (try_end),
      (try_end),
      (try_begin),
        (eq, ":player_agent_refilled_ammo", 1),
        (display_message, "@A Power Droid refilled your ammo!"),
        (agent_play_sound, ":power_droid_agent", "snd_gonk_noise"),  #play a sound from the agent that refilled the player's ammo
      (try_end),
      (try_begin),
        (eq, ":player_agent_refilled_health", 1),
        (display_message, "@A Medical Droid refilled some of your health!"),
        (agent_play_sound, ":med_droid_agent", "snd_bacta_heal"),  #play a sound from the agent that refilled the player's health
      (try_end),
    ])

from ID_animations import *

common_speeder_trigger_1 = (
   # SW - script to stop riderless horses (ie. speeders) from moving (script from KON_Air)
   5, 0, 0,  #length of stationary animation
   #0, 0, ti_once,  #only need to run once since I used agent_set_stand_animation, nope, didn't work....
      [],
    [
    (try_for_agents, ":cur_agent"),
     (agent_is_alive, ":cur_agent"),  #so we don't try dead agents
      (neg|agent_is_human,":cur_agent"),  #agent is a horse
       (agent_get_rider,":cur_rider", ":cur_agent"),
      (try_begin),
          (lt, ":cur_rider", 0),  #horse does not have a rider
        (agent_play_sound,":cur_agent","snd_speeder_noise_idle"),
      #(display_message, "@debug: sound played - no rider"),
         (agent_set_animation, ":cur_agent", anim_speeder_stationary),  #so the horse doesn't move, must include module_animations at the top
        #(agent_set_stand_animation, ":cur_agent", anim_speeder_stationary),  #doesn't work to stop them?
      #(else_try),
      #  (agent_play_sound,":cur_agent","snd_speeder_noise_moving"),
      #(agent_play_sound,":cur_rider","snd_speeder_noise_moving"),
      #(display_message, "@debug: sound played - with rider"),
      (try_end),
    (try_end),
      ])

common_speeder_trigger_2 = (
   # SW - script to stop riderless horses (ie. speeders) from moving (script from KON_Air)
   0.5, 0, 0,  #check more often then common_speeder_trigger_1
      [],
    [
    (get_player_agent_no, ":player_agent"),
    (try_for_agents, ":cur_agent"),
     (agent_is_alive, ":cur_agent"),  #so we don't try dead agents
      (neg|agent_is_human,":cur_agent"),  #agent is a horse
       (agent_get_rider,":cur_rider", ":cur_agent"),
     (agent_get_slot, ":speeder_movement", ":cur_agent", slot_agent_speeder_movement),
      (try_begin),
          (lt, ":cur_rider", 0),  #horse does not have a rider
      (lt, ":speeder_movement", 0),  #slot is not set
      (agent_set_slot, ":cur_agent", slot_agent_speeder_movement, 0),  #horse does not have a rider
      (else_try),
          (ge, ":cur_rider", 0),  #horse has a rider
      (lt, ":speeder_movement", 0),  #slot is not set
      (agent_set_slot, ":cur_agent", slot_agent_speeder_movement, 1),  #horse has a rider
      (else_try),
          (lt, ":cur_rider", 0),  #horse does not have a rider
      (eq, ":speeder_movement", 1),  #speeder was previously mounted
      (agent_set_slot, ":cur_agent", slot_agent_speeder_movement, 0),  #horse does not have a rider
      (eq, ":cur_agent", ":player_agent"),
      (stop_all_sounds,2),  #so we stop the speeder's engine noise loop that started for the player
      #(display_message, "@debug: agent got OFF a speeder"),
      (else_try),
          (ge, ":cur_rider", 0),  #horse has a rider
      (eq, ":speeder_movement", 0),  #speeder was previously not mounted
      (agent_set_slot, ":cur_agent", slot_agent_speeder_movement, 1),  #horse has a rider
      #(display_message, "@debug: agent got ON a speeder"),
       (agent_set_animation, ":cur_agent", anim_speeder_allow_movement),  #cancel the current animation and allow the horse to move
       #(agent_play_sound, ":cur_agent", "snd_speeder_noise_begin"),
       (eq, ":cur_agent", ":player_agent"),
       (play_sound, "snd_speeder_noise_loop", sf_looping),
      (else_try),
      (ge, ":cur_rider", 0),  #horse has a rider
      (eq, ":speeder_movement", 1),  #speeder is mounted
      #(agent_play_sound,":cur_agent","snd_speeder_noise_moving"),    #make moving sound (doesn't work all that well)
      (try_end),
        # (agent_play_sound,":cur_agent","snd_speeder_noise_idle"),
      # (display_message, "@sound played - no rider"),
        # (agent_set_animation, ":cur_agent", "anim_speeder_stationary"),  #so the horse doesn't move, must include module_animations at the top
        # #(agent_set_stand_animation, ":cur_agent", "anim_speeder_stationary"),  #doesn't work to stop them?
      # (else_try),
        # (agent_play_sound,":cur_agent","snd_speeder_noise_moving"),
      # #(agent_play_sound,":cur_rider","snd_speeder_noise_moving"),
      # (display_message, "@sound played - with rider"),
    (try_end),
      ])

common_check_town_fight = (
  3, 0, 0,  [

          #SW - maybe use all_enemies_defeated ?
          #(all_enemies_defeated, 5),

          #(assign, reg1, "$g_init_fight"),          #debug only
          #(display_message, "@g_init_fight = {reg1}"),    #debug only

          #(assign, reg1, "$g_player_current_own_troop_kills"),
          (try_begin),
            (eq, "$g_init_fight", 1),  #no battle, allow player to start a town fight

            # #-------------------------- OLD CODE -------------------------------------
            # #(get_player_agent_kill_count, ":wound_count", 1),  #can use this to get the wound_count instead of kill count?
            # #(assign, reg1, "$player_current_friendly_kills"),
            # (get_player_agent_own_troop_kill_count, ":count"),
            # #(assign, reg2, ":count"),
            # #(display_message, "@g_player = {reg1}, own_troop_kill = {reg2}"),
            # (try_begin),
              # (gt, ":count", "$player_current_friendly_kills"),
              # (dialog_box,"@You have killed a citizen and are now wanted by the local authorities!", "@Alert"),  # display dialog popup ?
              # (call_script, "script_start_town_fight"),
              # (assign, "$g_init_fight", 2),
            # (try_end),

            (get_player_agent_no, ":player_agent"),
            (assign, ":wounded", 0),
            #(assign, ":killed", 0),
            (try_for_agents, ":agent"),
              (agent_is_human,":agent"), # SWY @> It shouldn't be triggered by horse damage
              (agent_get_team  ,":team", ":agent"),(eq, ":team", 2),  #citizens
              (neq, ":agent", ":player_agent"), # SWY @> non-player agents only
              
              #SWY @> Bounty hunters don't trigger a civilian kill
              #<https://bitbucket.org/Swyter/swconquest/issue/87/bounty-hunter-missions-end-in-riots>
              (agent_get_troop_id,":trp_agent", ":agent"),
              (neq, ":trp_agent", "$bounty_target_1"),
              (neq, ":trp_agent", "$bounty_target_2"),
              (neq, ":trp_agent", "$bounty_target_3"),
              (neq, ":trp_agent", "$bounty_target_4"),
              (neq, ":trp_agent", "$bounty_target_5"),
              (neq, ":trp_agent", "$bounty_target_6"),
              
              (store_agent_hit_points,":agent_hp",":agent",1),  #set to 1 to retrive absolute hp
              (agent_get_slot, ":old_agent_hp", ":agent", slot_agent_hit_points),
              (try_begin),
                (lt, ":agent_hp", ":old_agent_hp"),
                (val_add, ":wounded", 1),
              (try_end),
              #check if you have killed anybody?  then all citizens attack
            (try_end),
            (try_begin),
              (eq, "$tavern_brawl", 1),
              (assign, "$g_init_fight", 2),
            (else_try),
              (gt, ":wounded", 0),
              (dialog_box,"@You have attacked a citizen and are now wanted by the local authorities!", "@Alert"),  # display dialog popup ?
              (assign, "$g_started_battle_random_by_enemy_faction", 0), #swy--fixes gaining relation with faction when attacking a citizen!
              (call_script, "script_start_town_fight"),
              (assign, "$g_init_fight", 2),
            (try_end),

          (else_try),
            (eq, "$g_init_fight", 2),  #random scene battle
            (get_player_agent_no, ":player_agent"),
            #set_party_battle_mode is off, so manually set the players hit points so they are injured after battle
            (store_agent_hit_points,":player_agent_health",":player_agent",0),  #relative health (0-100)
            #(troop_set_health, "trp_player", ":player_agent_health"),
            (troop_set_health, "$g_player_troop", ":player_agent_health"),
            #count the teams
            #(agent_get_team, ":player_team", ":player_agent"),
            (assign, ":enemies",0),
            (try_for_agents,":agent"),
              (agent_is_human,":agent"),
              #SW - now try and check if we need to decrease the companions health
              (agent_get_entry_no,":entry_no",":agent"),
              (try_begin),
                (this_or_next|eq,":entry_no",48),    #player's companion
                (eq,":entry_no",49),          #player's companion
                (agent_get_troop_id, ":agent_troop_id", ":agent"),
                (is_between,":agent_troop_id", companions_begin, companions_end),  #verify they are a npc
                (store_agent_hit_points,":agent_health",":agent",0),  #relative health (0-100)
                (troop_set_health, ":agent_troop_id", ":agent_health"),
              (try_end),
              #now check the rest of the agents to see if there are any enemies
              (agent_is_alive,":agent"),
              (neg|agent_is_ally, ":agent"),
              (val_add, ":enemies", 1),
              #debug
              #(assign, reg1, ":player_team_count"),
              #(display_message, "@player_team_count = {reg1}, other_team_count = {reg2}"),
            (try_end),
            (try_begin),
              (eq,":enemies",0),
              (dialog_box,"@All enemies at this location have been defeated!", "@Success"),  # display dialog popup ?
              (add_xp_to_troop,100,"$g_player_troop"),  #since custom commander is integrated
              (call_script, "script_troop_add_gold", "$g_player_troop", 100),
              (assign, "$g_init_fight", 0),  #turn it off
              (store_faction_of_party, ":minorplanet_faction", "$current_town"),
                  #@> SWY - Added some conditionals for changing dynamically the faction relations
                  (try_begin),
                    (eq, "$g_started_battle_random_by_enemy_faction", 1),
                    (call_script, "script_change_player_relation_with_faction", ":minorplanet_faction", 1),
                  (else_try),
                    (call_script, "script_change_player_relation_with_faction", ":minorplanet_faction", -3),
                  (try_end),
            (try_end),
          (try_end),


        ],[])

#SW - START OF SHIELD BASH
#shield bash integration - http://forums.taleworlds.net/index.php/topic,44290.0.html
shield_bash_kit_1 = (
  ti_before_mission_start, 0, 0, [], [
                    (le, "$shield_bash_toggle", 0),
                    (assign,"$bash_readiness",0),
                    ])
shield_bash_kit_2 = (
    0.1, 0, 0, [], [
          (le, "$shield_bash_toggle", 0),
          (val_add,"$bash_readiness",1),
          ])
shield_bash_kit_3 = (
    0, 0, 0, [
      (le, "$shield_bash_toggle", 0),
      (game_key_is_down, gk_defend),
      (game_key_clicked, gk_attack),
      ],
  [(assign,":continue",0),
  (get_player_agent_no,":player"),
  (agent_is_alive,":player"),
    #SW - modified to add shields_begin and shields_end
  #(try_for_range,":shield","itm_wooden_shield","itm_jarid"),
  (try_for_range,":shield",shield_bash_begin,shield_bash_end),
    (agent_has_item_equipped,":player",":shield"),
    (assign,":continue",1),
  (end_try),
  (eq,":continue",1),
  (agent_get_horse,":horse",":player"),
  (neg|gt,":horse",0),
  (ge,"$bash_readiness",10),
  (assign,"$bash_readiness",0),
  (call_script,"script_cf_agent_shield_bash",":player"),
  ])
shield_bash_kit_4 = (
    1.0, 0, 0, [
        (le, "$shield_bash_toggle", 0),
        ],
  [
  (get_player_agent_no,":player"),
  (try_for_agents,":agent"),
    (agent_is_alive,":agent"),
    (agent_is_human,":agent"),
    (neq,":agent",":player"),
    (agent_get_class ,":class", ":agent"),
    (neq,":class",grc_cavalry),
    (assign,":continue",0),
    #SW - modified to add shields_begin and shields_end
    #(try_for_range,":shield","itm_wooden_shield","itm_jarid"),
    (try_for_range,":shield",shield_bash_begin,shield_bash_end),
      (agent_has_item_equipped,":agent",":shield"),
      (assign,":continue",1),
    (end_try),
    (eq,":continue",1),
    (assign,":chances",0),
    (agent_get_team,":team",":agent"),
    (agent_get_position,pos1,":agent"),
    (try_for_agents,":other"),
      (agent_is_alive,":other"),
      (agent_is_human,":other"),
      (agent_get_class ,":class", ":other"),
      (neq,":class",grc_cavalry),
      (agent_get_team,":otherteam",":other"),
      (neq,":team",":otherteam"),
      (agent_get_position,pos2,":other"),
      (get_distance_between_positions,":dist",pos1,pos2),
      (neg|position_is_behind_position,pos2,pos1),
      (lt,":dist",200),
      (val_add,":chances",1),
    (end_try),
    (store_agent_hit_points,":health",":agent",0),
    (val_mul,":health",-1),
    (val_add,":health",100),
    (val_div,":health",10),
    (val_mul,":chances",":health"),
    (store_random_in_range,":rand",1,25),
    (lt,":rand",":chances"),
    (call_script,"script_cf_agent_shield_bash",":agent"),
  (end_try),])
# END OF SHIELD BASH

#--------------------------------------------------------------------------------------------------------------------------
#SW - common_alternative_attack code from Highlander (only disadvantage is that ammo is refilled)
# I also switched the code from trp_player to $g_player_troop since I use custom commander
#common_alternative_attack = (0,0,0,

#SW - actually, this code causes issues with the battle summary at the end since it reports the player was injured, so I am no longer using it
#  - there is also another issue that you see your dead body indoor scenes, but this would not be a problem in warband since there is now a remove_agent

# common_toggle_weapon_capabilities = (0, 0, 0,
# [
  # #(key_clicked, key_t),
  # (key_clicked, "$toggle_weapon_key"),
  # (neg|conversation_screen_is_active),
  # (get_player_agent_no,":player"),
  # (agent_is_alive, ":player"),      # only continue if player is alive
  # (agent_get_team,":team",":player"),
  # (agent_get_wielded_item,":item",":player",0),
  # (gt,":item",-1),
  # #(item_get_slot,":item_b",":item",slot_item_alternative_attack),
  # (item_get_slot,":item_b",":item",slot_item_alternate_weapon),
  # (gt,":item_b",0),
  # (set_show_messages,0),
  # (agent_get_horse,":horse",":player"),
  # (troop_get_inventory_slot,":slot_horse","$g_player_troop",ek_horse),
  # (troop_get_inventory_slot_modifier,":slot_horse_modifier","$g_player_troop",ek_horse),
  # (init_position,pos2),
  # (try_begin),
    # (lt,":horse",0),
  # (troop_set_inventory_slot,"$g_player_troop",ek_horse,"itm_no_item"),
    # (troop_remove_item, "$g_player_troop", "itm_no_item"),
  # (else_try),
    # (agent_get_item_id,":horse_item",":horse"),
  # (troop_set_inventory_slot,"$g_player_troop",ek_horse,":horse_item"),
   # (agent_set_position,":horse",pos2),
  # (try_end),
  # (try_for_range,":slot",0,4),
  # (troop_get_inventory_slot,":slot_item","$g_player_troop",":slot"),
    # (troop_get_inventory_slot_modifier,":slot_modifier","$g_player_troop",":slot"),
    # (eq,":slot_item",":item"),
  # (troop_get_inventory_slot,":slot_item_0","$g_player_troop",0),
    # (troop_get_inventory_slot_modifier,":slot_modifier_0","$g_player_troop",0),
    # (troop_set_inventory_slot,"$g_player_troop",0,":item_b"),
    # (troop_set_inventory_slot_modifier,"$g_player_troop",0,":slot_modifier"),
    # (neq,":slot",0),
  # (troop_set_inventory_slot,"$g_player_troop",":slot",":slot_item_0"),
    # (troop_set_inventory_slot_modifier,"$g_player_troop",":slot",":slot_modifier_0"),
  # (try_end),
  # (store_agent_hit_points,":hit_points",":player",1),
  # (agent_get_position,pos1,":player"),
  # (agent_set_position,":player",pos2),
  # (call_script,"script_dmod_kill_agent",":player"),
  # (set_spawn_position,pos1),
  # (spawn_agent,"$g_player_troop"),
  # (agent_set_hit_points,reg0,":hit_points",1),
  # (agent_set_team,reg0,":team"),
  # (try_begin),
    # (lt,":slot_horse",0),
  # (troop_set_inventory_slot,"$g_player_troop",ek_horse,"itm_no_item"),
  # (troop_remove_item, "$g_player_troop", "itm_no_item"),
  # (else_try),
  # (troop_set_inventory_slot,"$g_player_troop",ek_horse,":slot_horse"),
  # (troop_set_inventory_slot_modifier,"$g_player_troop",ek_horse,":slot_horse_modifier"),
  # (try_end),
  # (set_show_messages,1),
# ],[])
#--------------------------------------------------------------------------------------------------------------------------------------------------
#SW - old toggle_weapon_capabilities code (you must display a dialog and ammo is refilled)
#common_toggle_weapon_capabilities_w_popup = (0, 0, 0, [
common_toggle_weapon_capabilities = (0, 0, 0, [
  #(key_clicked, key_t),
  (key_clicked, "$toggle_weapon_key"),
  (neg|conversation_screen_is_active),
  (get_player_agent_no, ":player_agent"),
  (agent_get_wielded_item,":wielded_item",":player_agent",0),
  (gt,":wielded_item",-1),
  (item_slot_ge, ":wielded_item", slot_item_alternate_weapon, 1),  #see if the item has an alternate weapon slot defined
  ],
  
  [


    (get_player_agent_no, ":player_agent"),
    (agent_is_alive, ":player_agent"),
    #clear the strings
    (str_clear, s1),(str_clear, s2),(str_clear, s10),(str_clear, s11),(str_clear, s12),(str_clear, s13),
    (assign, "$show_switch_weapon_dialog", 0),
    (agent_get_wielded_item,":wielded_item",":player_agent",0),
    (try_begin),
      (gt,":wielded_item",-1),
      (item_slot_ge, ":wielded_item", slot_item_alternate_weapon, 1),  #see if the item has an alternate weapon slot defined
      (item_get_slot, ":alternate_weapon", ":wielded_item", slot_item_alternate_weapon),  #get the alternate weapon
      (try_for_range, ":slot_no", 0, 4),
        (troop_get_inventory_slot, ":item_in_slot", "$g_player_troop",":slot_no"),  #since custom commander is integrated
        (eq, ":item_in_slot", ":wielded_item"),
        (troop_get_inventory_slot_modifier, ":modifier", "$g_player_troop", ":slot_no"),  #get the modifier
        (troop_set_inventory_slot, "$g_player_troop", ":slot_no", ":alternate_weapon"),  #set the alternate weapon
        (troop_set_inventory_slot_modifier, "$g_player_troop", ":slot_no", ":modifier"),  #set the modifier
        #record the names to display in the dialog later
        (str_store_item_name, s1, ":wielded_item"),
        (str_store_item_name, s2, ":alternate_weapon"),
        (item_get_thrust_damage, reg3, ":alternate_weapon"),
        (item_get_speed_rating, reg4, ":alternate_weapon"),
        (item_get_accuracy, reg5, ":alternate_weapon"),
        (item_get_missile_speed, reg7, ":alternate_weapon"),
        (item_get_thrust_damage_type, reg6, ":alternate_weapon"), #0 =cut; 1= Pierce, 2 = Blunt    
        (try_begin),
          (eq, reg6, 2),
          (str_store_string, s11, "@ (Stun)"),
        (else_try),
          (str_store_string, s11, "@ "),
        (try_end),    
        (try_begin),
          (is_between, ":alternate_weapon", "itm_ranged_weapons_begin", "itm_ranged_weapons_end"),
          (str_store_string, s12, "@Damage: {reg3}{s12} -- Accuracy: {reg5}, -- Velocity: {reg7} -- Fire Rate: {reg4}"),
        (else_try),
          (str_store_string, s12, "@Damage: {reg3}{s12}"),
        (try_end),
        (str_store_string, s10, "@Switched to {s2} Mode: {s12}", message_neutral),
      (try_end),
    (try_end),
    (item_get_type, ":item_type", ":wielded_item"),
    (try_begin),
      (eq, ":item_type", itp_type_crossbow),
      (agent_set_animation, ":player_agent",  "anim_unequip_bayonet",1),
    (else_try),
      (eq, ":item_type", itp_type_pistol),
      (agent_set_animation, ":player_agent",  "anim_equip_bayonet",1),
    (else_try),
      (agent_set_animation, ":player_agent", "anim_alt_sword", 1),
    (try_end),
    (agent_unequip_item, ":player_agent", ":wielded_item"),
    (agent_equip_item, ":player_agent", ":alternate_weapon"),
    (agent_set_wielded_item, ":player_agent", ":alternate_weapon"),
    (display_message, "@{s10}", color_good_news),
  ])
#--------------------------------------------------------------------------------------------------------------------------------------------------
# #SW - new player_damage
# common_player_damage = (1, 0, ti_once, [
  # #(neg|conversation_screen_is_active),
  # #(le, "$player_damage", 0),

    # #SW - so it neverruns
    # (eq, 0, 1),

  # ],
  # [
    # (get_player_agent_no, ":player_agent"),
    # #(agent_is_alive, ":player_agent"),
    # # (store_agent_hit_points,":player_hp",":player_agent",0),  # set absolute to 1 to retrieve actual hps, otherwise will return relative hp in range [0..100]
    # # (try_begin),
      # # (eq, ":player_hp", "$player_hp_previous"),
      # # #do nothing
    # # (else_try),
      # # (le, ":player_hp", 90),
    # # (try_begin),
      # # (le, ":player_hp", 75),
      # # #(display_message, "@prsnt_player_damage..."),
      # # (start_presentation, "prsnt_player_damage"),
    # # (try_end),
    # (start_presentation, "prsnt_player_damage"),

    # (assign, "$player_hp_previous", ":player_hp"),
  # ])
#--------------------------------------------------------------------------------------------------------------------------------------------------
# common_crouch_toggle = (0, 0, 0, [
  # (key_clicked, key_f),(neg|conversation_screen_is_active)
  # ],
  # [
    # #(get_player_agent_no, ":player_agent"),
    # #(assign, ":cur_agent", ":player_agent"),

    # (try_begin),
      # (le, "$crouch_toggle", 0),  #incase this variable isn't set yet
      # (assign, "$crouch_toggle", 1),  #turn it on
      # (try_for_agents, ":cur_agent"),
        # (agent_is_alive, ":cur_agent"),
        # (agent_set_speed_limit, ":cur_agent", 1),    #forces them to walk, it affects AI only
        # (agent_set_stand_animation, ":cur_agent", "anim_stand_crouch"),          #only works when weapons aren't equipped
        # (agent_set_walk_forward_animation, ":cur_agent", "anim_walk_forward_crouch"),  #only works when weapons aren't equipped
      # (try_end),
      # (display_message, "@crouch is now ON."),
    # (else_try),
      # (assign, "$crouch_toggle", 0),  #turn it off
      # (try_for_agents, ":cur_agent"),
        # (agent_set_speed_limit, ":cur_agent", 100),    #set it high so they can run again, it affects AI only
        # (agent_set_stand_animation, ":cur_agent", "anim_stand"),        #only works when weapons aren't equipped
        # (agent_set_walk_forward_animation, ":cur_agent", "anim_walk_forward"),  #only works when weapons aren't equipped
      # (try_end),
      # (display_message, "@crouch is now OFF."),
    # (try_end),
  # ])
#--------------------------------------------------------------------------------------------------------------------------------------------------
#Swyter Turret Code
common_turret = (0, 0, 0,
  [
    (neg|conversation_screen_is_active),
    (get_player_agent_no, ":player_agent"),
    (agent_is_alive, ":player_agent"),
    (agent_get_horse, ":horse", ":player_agent"),
    (eq, ":horse", -1),    #can only crouch if you aren't on a horse
  ],
  [
    # (get_player_agent_no, ":player_agent"),

    # (agent_get_position,pos1,":player_agent"),
    ##(prop_instance_get_position,1,"$ship"),
        # (assign,":dist",150),
           # (scene_prop_get_num_instances,reg50,"spr_swy_hoth_turret"),
           # (val_add,reg50,1),
           # (try_for_range,":instance",0,reg50),
              # (scene_prop_get_instance,":thechosenturret", "spr_swy_hoth_turret", ":instance"),
              # (prop_instance_get_position,2,":thechosenturret"),
              # (get_distance_between_positions,":distance",1,2),
              # (lt,":distance",":dist"),
              # (assign,":dist",":distance"),

        ##(key_is_down, "$crouch_key"),
        # (neq|position_is_behind_position,pos1,pos2),
      # (prop_instance_get_position,pos1,":thechosenturret"),
      # (position_rotate_z,pos1,90),
      # (prop_instance_animate_to_position,":thechosenturret",pos1,2),
            # (end_try),


      (get_player_agent_no, ":player_agent"),
      (scene_prop_get_num_instances,":num_instances","spr_swy_hoth_turret_cannon"),
      (gt, ":num_instances", 0),
      (try_for_range, ":cur_i", 0, ":num_instances"),
        (scene_prop_get_instance,":instance", "spr_swy_hoth_turret_cannon", ":cur_i"),
        (prop_instance_get_position,pos1,":instance"),
        (agent_get_position, pos2, ":player_agent"),
        (get_distance_between_positions,":dist",pos1,pos2),
        #get health
        #(store_agent_hit_points,":player_agent_health",":player_agent",0),  #relative number, 0-100
        #(try_begin),
        (try_begin),
          #(eq, ":player_agent_health", 100),  #player is fully healed
          #(le, ":dist", 125),  #very close
          (le, ":dist", 425),  #very close
          (eq, "$mounted_turret", 0),
          (neq|position_is_behind_position,pos2,pos1),
          (game_key_is_down, gk_action),


          (agent_play_sound, ":player_agent", "snd_bacta_heal"),
          #(init_position,pos3),
          #(copy_position,pos2,pos3),
          #(agent_set_position, ":player_agent", pos1),
          (assign, "$mounted_turret", 1),
          (display_message, "@Mounted on Turret:"),
          ##@(display_message, ":instance"),
        (else_try),
          #(le, ":dist", 425),  #very close
          (eq, "$mounted_turret", 1),
          (position_copy_rotation,pos2,pos1),
          (prop_instance_animate_to_position,":instance",pos1,100),

                  (position_move_z,pos1,260),
              (position_rotate_x,pos1,-5),
              (position_move_y,pos1,-1000),

              (mission_cam_animate_to_position, pos1,100,1),



          (game_key_is_down, gk_action),
          (agent_play_sound, ":player_agent", "snd_bacta_heal"),
          #(agent_set_position, ":player_agent", pos3),
          (mission_cam_set_target_agent, ":player_agent",1),
          (assign, "$mounted_turret", 0),
          (display_message, "@Dismounted of Turret:"),
          ##@(display_message, ":instance"),
          #(display_message, "@You are not injured and do not need the Bacta Tank at this time."),
        #(else_try),
          #(lt, ":player_agent_health", 100),  #player is injured
          #(le, ":dist", 125),  #very close
          #(display_message, "@You are being healed by the Bacta Tank..."),
          #(val_add, ":player_agent_health", 10),  #add 10%
          #(try_begin),
            #(gt, ":player_agent_health", 100),
            #(assign, ":player_agent_health", 100),    #so we don't try and set hit points > 100%
          #(try_end),
          #(agent_set_hit_points,":player_agent",":player_agent_health",0),
          #(troop_set_health, "$g_player_troop", ":player_agent_health"),

        (else_try),
          (le, ":dist", 1300),  #in room
          (eq, "$mounted_turret", 0),
          #(display_message, "@Debug: Far of turret:"),
          #(display_message, ":dist"),
          (position_rotate_z,pos1,90),
          (prop_instance_animate_to_position,":instance",pos1,200),
        (try_end),
      (try_end),



  ])

#--------------------------------------------------------------------------------------------------------------------------------------------------
#Swyter Gate System Code - Vertical Single side kind.
common_gate_system = (1, 1, 0,
  [],
    [
        #@~ Original code
    (try_begin),
        (scene_prop_get_num_instances,":num_instances","spr_swy_gate.sys"),
      (gt, ":num_instances", 0),
        (try_for_range, ":cur_i", 0, ":num_instances"),  #-> Try for every door in the scene
          #(assign,":break_try",0),
          (troop_set_slot, "trp_gate_sys_counter", ":cur_i",0),
            (try_for_agents,":gate_sys_agent"), #-> Try for every guy in the scene
              #(eq,":break_try",0),
              (scene_prop_get_instance,":instance", "spr_swy_gate.sys", ":cur_i"),
              (prop_instance_get_position,pos1,":instance"),
              (agent_get_position, pos2, ":gate_sys_agent"),
              (get_distance_between_positions,":dist",pos1,pos2),

                (try_begin), # How many people it's soon to the door?
                  (le, ":dist", 700),
                  (troop_get_slot,reg1,"trp_gate_sys_counter",":cur_i"),
                  (val_add,reg1,1),
                  (troop_set_slot, "trp_gate_sys_counter", ":cur_i",reg1),
                (try_end),
            (try_end),

            (try_begin),
              #(eq,":break_try",0),
              #(le, ":dist", 700),

                  (try_begin), #CLOSE DOOR -> Need to handle various ids
                      #(eq,":break_try",0),
                      #(le, ":dist", 700),
                      (troop_get_slot,reg1,"trp_gate_sys_counter",":cur_i"),
                      (eq,reg1,0),

                      (troop_get_slot,":is_open","trp_gate_sys_array",":cur_i"),
                      (eq,":is_open",1),

                      (agent_play_sound, ":gate_sys_agent", "snd_blast_door_close"),
                      #(display_message, "@@SWY -> Door opened / {reg1}"),

                      #(assign,":break_try",1),
                      (troop_set_slot, "trp_gate_sys_array", ":cur_i",0), #used as save array: door[id]=0/1

                      #@> We move the door...
                      (position_move_z,pos1,-400),
                      (prop_instance_animate_to_position,":instance",pos1,100),
                  (try_end),
                  (try_begin), #OPEN DOOR -> When a guy it's 0.7 meters far from the gate it will open
                      (troop_get_slot,reg1,"trp_gate_sys_counter",":cur_i"),
                      (gt,reg1,0),

                      (troop_get_slot,":is_open","trp_gate_sys_array",":cur_i"),
                      (neq|eq,":is_open",1),

                      #(eq,":break_try",0),
                      #(le, ":dist", 700),
                      #(troop_get_slot,":is_closed","trp_gate_sys_array",":cur_i"),
                      #(eq,":is_closed",1),

                      (agent_play_sound, ":gate_sys_agent", "snd_blast_door_open"),
                      #(display_message, "@@SWY -> Door closed / {reg1}"),

                      #(assign,":break_try",1),
                      (troop_set_slot, "trp_gate_sys_array", ":cur_i",1), #used as save array: door[id]=0/1

                      #@> We move the door...
                      (position_move_z,pos1,400),
                      (prop_instance_animate_to_position,":instance",pos1,100),
                  (try_end),

            (try_end),

        (try_end),
    (try_end), #--> Original code end
    #@~ Death Star Blast Doors [deathstar_parts_1_door]
    (try_begin),
      (scene_prop_get_num_instances,":num_instances","spr_deathstar_parts_1_door"),
      (gt, ":num_instances", 0),
        (try_for_range, ":cur_i", 0, ":num_instances"),  #-> Try for every door in the scene
          (troop_set_slot, "trp_gate_sys_counter2", ":cur_i",0),
            (try_for_agents,":gate_sys_agent"), #-> Try for every guy in the scene
              (scene_prop_get_instance,":instance", "spr_deathstar_parts_1_door", ":cur_i"),
              (prop_instance_get_position,pos1,":instance"),
              (agent_get_position, pos2, ":gate_sys_agent"),
              (get_distance_between_positions,":dist",pos1,pos2),

                (try_begin), # How many people it's close to the door?
                  (le, ":dist", 1000),
                  (troop_get_slot,reg1,"trp_gate_sys_counter2",":cur_i"),
                  (val_add,reg1,1),
                  (troop_set_slot, "trp_gate_sys_counter2", ":cur_i",reg1),
                (try_end),
            (try_end),

            (try_begin),

                  (try_begin), #CLOSE DOOR -> Need to handle various ids

                      (troop_get_slot,reg1,"trp_gate_sys_counter2",":cur_i"),
                      (eq,reg1,0),

                      (troop_get_slot,":is_open","trp_gate_sys_array2",":cur_i"),
                      (eq,":is_open",1),

                      (agent_play_sound, ":gate_sys_agent", "snd_blast_door_close"),
                      (troop_set_slot, "trp_gate_sys_array2", ":cur_i",0), #used as save array: door[id]=0/1

                      #@> We move the door...
                      (position_move_x,pos1,400),
                      (prop_instance_animate_to_position,":instance",pos1,200),
                  (try_end),
                  (try_begin), #OPEN DOOR -> When a guy it's 0.7 meters far from the gate it will open
                      (troop_get_slot,reg1,"trp_gate_sys_counter2",":cur_i"),
                      (gt,reg1,0),

                      (troop_get_slot,":is_open","trp_gate_sys_array2",":cur_i"),
                      (neq|eq,":is_open",1),

                      (agent_play_sound, ":gate_sys_agent", "snd_blast_door_open"),
                      (troop_set_slot, "trp_gate_sys_array2", ":cur_i",1), #used as save array: door[id]=0/1

                      #@> We move the door...
                      (position_move_x,pos1,-400),
                      (prop_instance_animate_to_position,":instance",pos1,200),
                  (try_end),
            (try_end),

        (try_end),
    (try_end), #--> Death Star Blast door end
  ])

#--------------------------------------------------------------------------------------------------------------------------------------------------
common_crouch_button = (0, 0, 0,
  [
    (neg|conversation_screen_is_active),
    (get_player_agent_no, ":player_agent"),
    (agent_get_horse, ":horse", ":player_agent"),
    (eq, ":horse", -1),    #can only crouch if you aren't on a horse
    (this_or_next|key_is_down, "$crouch_key"),
    (eq, "$crouch_key_down", 1),    #crouch key was previously down ( 0 = up, 1 = down )
  ],
  [
    (get_player_agent_no, ":player_agent"),
    (agent_is_alive, ":player_agent"),
    (try_begin),
      (key_is_down, "$crouch_key"),
      (eq, "$crouch_key_down", 0),
      #player just pressed crouch key, play an animation
      (agent_set_animation, ":player_agent", "anim_crouch"),  #play a crouch animation that loops
      (assign, "$crouch_key_down", 1),    #crouch key is down ( 0 = up, 1 = down )
    (else_try),
      (key_is_down, "$crouch_key"),
      (eq, "$crouch_key_down", 1),
      #player is still holding down the crouch key, do nothing unless they are trying to walk forward?
      #(game_key_is_down, gk_move_forward),
      #player is trying to move forward, set the animation
      #(agent_set_animation, ":player_agent", "anim_walk_forward_crouch"),  #play a walk forward crouch animation
    (else_try),
      (neg|key_is_down, "$crouch_key"),
      #player no longer has the crouch key down, play an animation to turn it off
      (agent_set_animation, ":player_agent", "anim_crouch_stop"),  #play a quick animation to turn it off
      (assign, "$crouch_key_down", 0),    #crouch key is up ( 0 = up, 1 = down )
    (try_end),

  ])
#--------------------------------------------------------------------------------------------------------------------------------------------------
#SW - new helmet view
common_helmet_view = [
  (0, .01, ti_once, [(eq, "$helmet_view", 1),], [(start_presentation, "prsnt_helmet_view")]),
  (0, 0, 0, [
    #(key_clicked, key_v),
    (key_clicked, "$helmet_view_key"),
    (neg|conversation_screen_is_active),
    ],
    [
      (get_player_agent_no, ":player_agent"),
      (agent_is_alive, ":player_agent"),

      (try_begin),
        (le, "$helmet_view", 0),  #incase this variable isn't set yet
        (assign, "$helmet_view", 1),
        (start_presentation, "prsnt_helmet_view"),
      (else_try),
        (assign, "$helmet_view", 0),
      (try_end),
    ])
 ]
#--------------------------------------------------------------------------------------------------------------------------------------------------
#SW - new zoom view
common_zoom_view = (0, 0, 0, [
    (game_key_is_down, gk_zoom),(neg|conversation_screen_is_active)
  ],
  [
    #(display_message,"@zoom is down"),  #debug
    (get_player_agent_no, ":player_agent"),
    (agent_is_alive, ":player_agent"),
    #(display_message,"@player is alive"),  #debug

    #(try_begin),
    #  (le, "$zoom_view", 0),  #incase this variable isn't set yet
    #  (assign, "$zoom_view", 1),
      (start_presentation, "prsnt_zoom_view"),
      #(display_message,"@presentation started"),  #debug
    #(try_end),
  ])
#--------------------------------------------------------------------------------------------------------------------------------------------------
#SW - fix_droid_walking
common_fix_droid_walking = (ti_on_agent_spawn, 0, 0, [],
  [
    (store_trigger_param_1, ":cur_agent"),
    (try_begin),
      (agent_is_alive,":cur_agent"),
      (agent_is_human,":cur_agent"),
      (this_or_next|agent_has_item_equipped,":cur_agent","itm_r2series_blue"),
      (this_or_next|agent_has_item_equipped,":cur_agent","itm_r2series_green"),
      (this_or_next|agent_has_item_equipped,":cur_agent","itm_r2series_orange"),
      (this_or_next|agent_has_item_equipped,":cur_agent","itm_r2series_purple"),
      (this_or_next|agent_has_item_equipped,":cur_agent","itm_lin_droid_armor"),
      (this_or_next|agent_has_item_equipped,":cur_agent","itm_lin_droid_armor_w_arm"),
      (this_or_next|agent_has_item_equipped,":cur_agent","itm_mse6_armor"),
      (this_or_next|agent_has_item_equipped,":cur_agent","itm_power_droid_grey"),
      (this_or_next|agent_has_item_equipped,":cur_agent","itm_power_droid_snow"),
      (this_or_next|agent_has_item_equipped,":cur_agent","itm_power_droid_tan"),
      (agent_has_item_equipped,":cur_agent","itm_fxseries_droid_armor"),
      #(display_message, "@its a droid, setting agent to use anim_droid_walk_forward..."),
      (agent_set_walk_forward_animation, ":cur_agent", "anim_droid_walk_forward"),  #make these agents use a different walking animation, only works if they don't have a weapon equipped
    (try_end),
  ])
#--------------------------------------------------------------------------------------------------------------------------------------------------
#SW - Super-Mario Stype Super Jump concept - http://forums.taleworlds.net/index.php/topic,65520.msg1703891.html
common_use_jetpack = (0, 0, 0, [
  #(key_clicked, key_j),
  (key_clicked, "$jetpack_key"),
  (neg|conversation_screen_is_active),
  ],
  [
    (get_player_agent_no, ":player_agent"),
    (agent_is_alive, ":player_agent"),
    (try_begin),
      (this_or_next|player_has_item,"itm_jetpack"),
      (player_has_item,"itm_force_jump"),
      (agent_get_horse, ":player_horse", ":player_agent"),
      #(assign, reg7, ":player_horse"), #diagnostic only
            #(display_message, "@Player Horse = {reg7}"),#diagnostic only
      (try_begin),
        (eq, ":player_horse",-1),
        #run the animation
        (agent_set_animation, ":player_agent", "anim_jetpack"),
      (else_try),
        (display_message, "@Can't use while mounted!"),
      (try_end),
    (else_try),
      (display_message, "@You don't have a Jetpack or Force Jump in inventory!"),
    (try_end),

    # #(troop_get_inventory_capacity, ":inv_cap", "trp_player"),
    # (troop_get_inventory_capacity, ":inv_cap", "$g_player_troop"),  #since custom commander is integrated
    # (assign, ":binocular_slot", -1),
    # (try_for_range, ":slot_no", 0, ":inv_cap"),
      # #(troop_get_inventory_slot,":item_id","trp_player",":slot_no"),
      # (troop_get_inventory_slot,":item_id","$g_player_troop",":slot_no"),  #since custom commander is integrated
      # #check for binoculars
      # (try_begin),
        # (eq, ":item_id", "itm_binocular"),
        # (assign, ":binocular_slot", ":slot_no"),
      # (try_end),
    # (try_end),

  ])
#--------------------------------------------------------------------------------------------------------------------------------------------------

kham_iron_sights_triggers = [
 #-- numeric constants

 # cam_mode_default = 0
 # cam_mode_free    = 1
 # cam_mode_fixed   = 2

  #-- camera_init
  (0, 0, ti_once,
  [
    (get_player_agent_no, "$cam_current_agent"),
    (gt,                  "$cam_current_agent", -1)
  ],
  [
    (assign, "$cam_free",   0),
    (assign, "$g_camera_z", 180),
  ]),

#-- camera_set
  (0, 0, 0,
  [ 
    (get_player_agent_no, ":player"),
    (agent_get_wielded_item, ":weapon", ":player", 0),
    (is_between, ":weapon", "itm_a280", "itm_dh17"), #Rifles only
    (key_clicked, "$key_camera_toggle"),
    (lt, "$cam_mode", 2),
  ],
  # toggling only when camera mode = 0, 1, 2 (3 = disable); shoot_mode = 1 temporarily disable toggling
  [
    (try_begin),
      (eq,     "$cam_mode", 0),
      (assign, "$cam_mode", 1),
      (display_message, "@Zoom Camera"),
    (else_try),
      (eq, "$cam_mode", 1),
      (assign, "$cam_mode", 0),
      (display_message, "@Default Camera"),
    (try_end),

    (mission_cam_set_mode, "$cam_mode"),
  ]),

   #-- camera_mode
  (0, 0, 0, [],
  [
    (try_begin),
      (eq, "$cam_mode", 1),
      (set_fixed_point_multiplier, 100),
      (agent_get_look_position, pos7, "$cam_current_agent"),
      (position_get_rotation_around_x, ":angle", pos7),
      (store_sub, ":reverse", 0, ":angle"),
      (position_rotate_x, pos7, ":reverse"),
      (position_move_y, pos7, "$g_camera_y"),
      (position_move_z, pos7, "$g_camera_z"),
      (agent_get_horse, ":horse_agent", "$cam_current_agent"),
      (try_begin),
        (ge, ":horse_agent", 0),
        (position_move_z, pos7, 50),
      (try_end),
      (store_mul, ":reverse", 1, "$g_camera_y"),
      (store_atan2, ":drop", "$g_camera_z", ":reverse"),
      (convert_from_fixed_point, ":drop"),
      (val_sub, ":angle", ":drop"),
      (val_add, ":angle", 5),
      (position_rotate_x, pos7, ":angle"),
      (mission_cam_animate_to_position, pos7, 100, 0),
      (start_presentation, "prsnt_iron_sights"),
    (else_try),
      (lt, "$cam_mode", 2),
      (main_hero_fallen),
      (agent_get_position, 1, "$cam_current_agent"),
      (get_player_agent_no,   ":player_agent"),
      (agent_set_position,    ":player_agent", 1),
    (try_end),
  ]),

]


#SW - zoom in/out code by jik and WilliamBerne - http://forums.taleworlds.net/index.php/topic,68192.0.html - modified further by HokieBT
common_use_binocular_1 = (0, 0, 0, [
  (key_clicked, key_b),
  #(key_clicked, "$binoculars_key"),
  (neg|conversation_screen_is_active),
  ],
  [
    (get_player_agent_no, ":player_agent"),
    (agent_is_alive, ":player_agent"),
    #(troop_get_inventory_capacity, ":inv_cap", "trp_player"),
    (troop_get_inventory_capacity, ":inv_cap", "$g_player_troop"),  #since custom commander is integrated
    (assign, ":binocular_slot", -1),
    (try_for_range, ":slot_no", 0, ":inv_cap"),
      #(troop_get_inventory_slot,":item_id","trp_player",":slot_no"),
      (troop_get_inventory_slot,":item_id","$g_player_troop",":slot_no"),  #since custom commander is integrated
      #check for binoculars
      (try_begin),
        (eq, ":item_id", "itm_binocular"),
        (assign, ":binocular_slot", ":slot_no"),
      (try_end),
    (try_end),

    (try_begin),
      (eq, ":binocular_slot", -1),
      (display_message, "@You don't have any Macrobinoculars in your inventory!"),
    (else_try),

      (try_begin),
        (le, "$binocular_magnification", 0),  #incase this variable isn't set yet
        (assign, "$binocular_magnification", 2000),
        (display_message, "@Macrobinocular Zoom is 2x"),
      (else_try),
        (eq, "$binocular_magnification", 2000),
        (assign, "$binocular_magnification", 4000),
        (display_message, "@Macrobinocular Zoom is 4x"),
      (else_try),
        (eq, "$binocular_magnification", 4000),
        (assign, "$binocular_magnification", 6000),
        (display_message, "@Macrobinocular Zoom is 6x"),
      (else_try),
        (eq, "$binocular_magnification", 6000),
        (assign, "$binocular_magnification", 8000),
        (display_message, "@Macrobinocular Zoom is 8x"),
      (else_try),
        (eq, "$binocular_magnification", 8000),
        (assign, "$binocular_magnification", 0),
        (display_message, "@Macrobinocular Zoom is off"),
      (try_end),
      #change the zoom
      (try_begin),
        (le, "$binocular_magnification", 0),
        (mission_cam_clear_target_agent),
        (mission_cam_set_mode,0),
        (mission_cam_set_target_agent, ":player_agent", 1),
      (else_try),
        (mission_cam_clear_target_agent),
        (assign,":height",0),
        #get where the player is looking
        (agent_get_look_position, pos1, ":player_agent"),
        (position_move_y,pos1,"$binocular_magnification"),
        (position_get_z,":height",pos1),
        (try_begin),
          (lt,":height",50),
          (position_move_z,pos1,200),
        (try_end),
        (mission_cam_set_mode,1),
        (mission_cam_animate_to_position, pos1, 100, 0),    #the speed of the zoom-in
        (start_presentation, "prsnt_binocular_display"),
      (try_end),
    (try_end),
  ])

common_use_binocular_2 = (
  0.1, 0, 0,
   [
    (try_begin),
      (gt, "$binocular_magnification", 0),
      (get_player_agent_no, ":player_agent"),
      (agent_is_alive, ":player_agent"),
      #(agent_set_animation, ":player_agent", "anim_unused_human_anim_1"),  #so the player doesn't move, must include module_animations at the top of the python file
      (agent_set_animation, ":player_agent", "anim_defend_fist"),  #so the player looks more like they are holding binoculars
      (agent_get_horse, ":player_horse", ":player_agent"),
      (try_begin),
        (ge, ":player_horse", 0),
        (agent_is_alive, ":player_horse"),  #so we don't try dead agents
        (agent_set_animation, ":player_horse", "anim_unused_horse_anim_01"),  #so the horse doesn't move, must include module_animations at the top of the python file
      (try_end),
      #(try_for_agents, ":cur_agent"),
      #  (agent_is_alive, ":cur_agent"),  #so we don't try dead agents
      #  (neg|agent_is_human,":cur_agent"),  #agent is a horse
      #  (agent_get_rider,":cur_rider", ":cur_agent"),
      #  (eq, ":cur_rider", ":player_agent"),  #rider of this horse is the player
      #  (agent_set_animation, ":cur_agent", "anim_unused_horse_anim_1"),  #so the horse doesn't move, must include module_animations at the top of the python file
      #(try_end),

      #fix the camera to follow the mouse movement
      #reset the camera (not sure all of these steps are necessary?)
      (mission_cam_clear_target_agent),
      (mission_cam_set_mode,0),
      (mission_cam_set_target_agent, ":player_agent", 1),
      #zoom in the camera (removed the height check so the camera wouldn't jump on the z-axis as the player moved the mouse around)
      (mission_cam_clear_target_agent),
      (agent_get_look_position, pos1, ":player_agent"),
      (position_move_y,pos1,"$binocular_magnification"),
      (mission_cam_set_mode,1),
      (mission_cam_animate_to_position, pos1, 1, 0),    #the speed of the zoom-in (really fast for the mouse movement camera, zero doesn't work)
      #(start_presentation, "prsnt_binocular_display"),  #not necessary

    (try_end),
    ],
   [
    ])
#-----------------------------------------------------------------------------------------------------------------------------------------------------
#SW - new zoom view
common_speeder_attack = (0, 0, 0, [
    (key_clicked, key_e),(neg|conversation_screen_is_active)
  ],
  [
    (get_player_agent_no, ":player_agent"),
    (agent_is_alive, ":player_agent"),
    (agent_get_horse, ":player_horse", ":player_agent"),
    (try_begin),
      (eq, ":player_horse",-1),  # player is on foot
    (else_try),
       (try_for_range,reg5,1,500),
        (particle_system_burst, "psys_food_steam", pos1, 15),
        (position_move_y,pos1,10),
        (copy_position,pos2,pos1),
        (position_set_z_to_ground_level, pos2),
        (get_distance_between_positions,":dist",pos1,pos2),
        (lt,":dist",10),
        (play_sound,"snd_concussion_fire"),
        (try_for_agents,":agent"),
           (agent_get_position,pos2,":agent"),
           (get_distance_between_positions,":dist",pos1,pos2),
           (lt,":dist",300),
           (agent_set_hit_points,":agent",1,0),
           #(agent_set_hit_points,":agent",0,1),
           #(agent_deliver_damage_to_agent,":agent",":agent"),  #SW modified
           (agent_deliver_damage_to_agent,":player_agent",":agent"),
        (end_try),
        (scene_prop_get_instance,":instance", "spr_explosion", 0),
        (position_copy_origin,pos2,pos1),
        (prop_instance_set_position,":instance",pos2),
        (position_move_z,pos2,1000),
        (prop_instance_animate_to_position,":instance",pos2,175),
        (assign,reg5,1000),
        (end_try),
    (try_end),
  ])

#---------------------------------------------------------------------------------------------------------------------------------------------------
sw_common_battle_kill_underwater = (
  # code concept from http://forums.taleworlds.net/index.php/topic,68852.0.html and http://forums.taleworlds.net/index.php/topic,58880.15.html
  5, 0, 1, [],  #one second refresh to allow sound time to complete
  [
    (try_for_agents,":agent"),
      (agent_is_alive,":agent"),
      (agent_get_position,pos1,":agent"),
      (position_get_z, ":pos_z", pos1),
      #(assign, reg1, ":pos_z"), #debug only
      #(display_message, "@agent z-position is {reg1}"),  #debug only
      (try_begin),
        (le, ":pos_z",-150),  #agent is about 6ft underwater
        (store_agent_hit_points,":hp",":agent",1),
        #(val_sub,":hp",7),
        (val_sub,":hp",10),
        (try_begin),
          (le, ":hp", 0),
          (agent_set_hit_points,":agent",0,0),
        (else_try),
          (agent_set_hit_points,":agent",":hp",1),
        (try_end),
        #(play_sound,"snd_man_grunt"),
        (agent_play_sound,":agent","snd_man_grunt"),
        (agent_deliver_damage_to_agent,":agent",":agent"),
      (try_end),
    (try_end),
  ])

#SW - healthpack code by ConstantA - http://forums.taleworlds.net/index.php/topic,66181.msg1719939.html#msg1719939 - modified further by HokieBT
common_use_healthpack = (0, 0, 0, [
  #(key_clicked, key_h),
  (key_clicked, "$bacta_injector_key"),
  (neg|conversation_screen_is_active),
  ],
  [
    (get_player_agent_no, ":player_agent"),
    (agent_is_alive, ":player_agent"),
    (store_agent_hit_points, ":player_hp", ":player_agent"),
    (try_begin),
      (lt, ":player_hp", 100),
      #(troop_get_inventory_capacity, ":inv_cap", "trp_player"),
      (troop_get_inventory_capacity, ":inv_cap", "$g_player_troop"),  #since custom commander is integrated
      (assign, ":healing_item_injector_slot", -1),
      (assign, ":healing_item_capsule_slot", -1),
      (assign, reg1, 0),
      (try_for_range, ":slot_no", 0, ":inv_cap"),
        #(troop_get_inventory_slot,":item_id","trp_player",":slot_no"),
        (troop_get_inventory_slot,":item_id","$g_player_troop",":slot_no"),  #since custom commander is integrated
        (try_begin),
          (eq, ":item_id", "itm_bacta_injector"),
            (assign, ":healing_item_injector_slot", ":slot_no"),
        (else_try),
          (eq, ":item_id", "itm_bacta_capsule"),
            (assign, ":healing_item_capsule_slot", ":slot_no"),
            (val_add, reg1, 1),
        (try_end),
      (try_end),
      (try_begin),
        (eq, ":healing_item_injector_slot", -1),
          (display_message, "@You don't have a Bacta Injector in inventory!"),
      (else_try),
        (le, reg1, 0),
          (display_message, "@You don't have any Bacta Capsules in inventory!"),
      (else_try),
          (store_agent_hit_points, ":player_hp", ":player_agent", 1),
          (val_add, ":player_hp", 20), #hp to add
          (agent_set_hit_points, ":player_agent", ":player_hp", 1),
          #(troop_set_inventory_slot,"trp_player",":healing_item_capsule_slot", -1),
          (troop_set_inventory_slot,"$g_player_troop",":healing_item_capsule_slot", -1),  #since custom commander is integrated
          (val_sub, reg1,1),
          (agent_play_sound,":player_agent","snd_bacta_injector"),
          (display_message, "@You were healed for 20 hp and have {reg1} bacta capsules left."),
      (try_end),
    (else_try),
      (display_message, "@You are not hurt."),
    (try_end),
  ])
#--------------------------------------------------------------------------------------------------------------------------

common_change_fog = (
  0, 0, ti_once,
  [
  #SW - set_fog_distance to a very high number to disable fog in scenes
  (try_begin),
    (eq, "$current_town","p_kamino"),
    (set_fog_distance, 175, 0xEE121118),
  (else_try),
    (eq, "$current_town","p_mustafar"),
    (set_fog_distance, 175, 0xEE272222),
  (else_try),
    (eq, "$current_town","p_corellia"),
    (set_fog_distance, 175, 0xEE654a2f),
  (else_try),
    (eq, "$current_town","p_felucia"),
    (set_fog_distance, 165, 0xAA92b595),
  (else_try),
    (eq, "$current_town","p_raxusprime"),
    (set_fog_distance, 165, 0xAABDAF86),
  (else_try),
    (this_or_next
    |eq, "$current_town","p_tatooine"),
    (eq, "$current_town","p_ryloth"),
    (set_fog_distance, 175, 0xEE655436),
  (else_try),
    (eq, "$current_town","p_spacestation_4"), #Dagobah
    (set_fog_distance, 220, 0xEE222722),
  (else_try),
    (eq, "$current_town","p_spacestation_28"), #Dathomir
    (set_fog_distance, 195, 0x00324D3F),
  (else_try),
    (set_fog_distance, 100000000), #otherwise fog isn't well received here
  (try_end),
    ], [])

tournament_triggers = [
  (ti_before_mission_start, 0, 0, [], [
                    (call_script, "script_change_banners_and_chest"),
                    (assign, "$g_arena_training_num_agents_spawned", 0),
                    #SW - added script_change_rain
                    (call_script, "script_change_rain", "$current_town"),
                     ]),

   #SW - added shield bash integration
   shield_bash_kit_1,
   shield_bash_kit_2,
   shield_bash_kit_3,
   shield_bash_kit_4,

   #SW - added common_battle_kill_underwater
   sw_common_battle_kill_underwater,

   #SW - added regen for certain agents
   #common_regeneration_store_info,
   #common_regeneration,

  #SW - add custom lightsaber noise
  #lightsaber_noise_idle,      #commented out, not necessary and idle noise sometimes interupts saber swing
  lightsaber_noise_player,
  lightsaber_noise_agent,
  common_change_fog,
  #common_use_healthpack,    #not usable in tournaments
  ##common_use_binocular_1,    #not usable in tournaments
  ##common_use_binocular_2,    #not usable in tournaments
  #common_helmet_view,      #not usable in tournaments
  #common_zoom_view,      #not usable in tournaments
  #common_use_jetpack,        #not usable in tournaments
  #common_toggle_weapon_capabilities, #not usable in tournaments
  common_switch_sw_scene_props,
  common_crouch_button,



  (ti_inventory_key_pressed, 0, 0, [(display_message,"str_cant_use_inventory_arena")], []),
  (ti_tab_pressed, 0, 0, [],
   [(try_begin),
      (eq, "$g_mt_mode", abm_visit),
      (set_trigger_result, 1),
    (else_try),
      (question_box,"str_give_up_fight"),
    (try_end),
    ]),
  (ti_question_answered, 0, 0, [],
   [(store_trigger_param_1,":answer"),
    (eq,":answer",0),
    (try_begin),
      (eq, "$g_mt_mode", abm_tournament),
      (call_script, "script_end_tournament_fight", 0),
    (else_try),
      (eq, "$g_mt_mode", abm_training),
      (get_player_agent_no, ":player_agent"),
      (agent_get_kill_count, "$g_arena_training_kills", ":player_agent", 1),#use this for conversation
    (try_end),
    (finish_mission,0),
    ]),

  (1, 0, ti_once, [], [
      (eq, "$g_mt_mode", abm_visit),
      (call_script, "script_music_set_situation_with_culture", mtf_sit_travel),
      (store_current_scene, reg(1)),
      (scene_set_slot, reg(1), slot_scene_visited, 1),
      (mission_enable_talk),
      (get_player_agent_no, ":player_agent"),
      (assign, ":team_set", 0),
      (try_for_agents, ":agent_no"),
        (neq, ":agent_no", ":player_agent"),
        (agent_get_troop_id, ":troop_id", ":agent_no"),
        (is_between, ":troop_id", regular_troops_begin, regular_troops_end),
        (eq, ":team_set", 0),
        (agent_set_team, ":agent_no", 1),
        (assign, ":team_set", 1),
      (try_end),
    ]),
##
##  (0, 0, 0, [],
##   [
##      #refresh hit points for arena visit trainers
##      (eq, "$g_mt_mode", abm_visit),
##      (get_player_agent_no, ":player_agent"),
##      (try_for_agents, ":agent_no"),
##        (neq, ":agent_no", ":player_agent"),
##        (agent_get_troop_id, ":troop_id", ":agent_no"),
##        (is_between, ":troop_id", regular_troops_begin, regular_troops_end),
##        (agent_set_hit_points, ":agent_no", 100),
##      (try_end),
##    ]),

##      (1, 4, ti_once, [(eq, "$g_mt_mode", abm_fight),
##                       (this_or_next|main_hero_fallen),
##                       (num_active_teams_le,1)],
##       [
##           (try_begin),
##             (num_active_teams_le,1),
##             (neg|main_hero_fallen),
##             (assign,"$arena_fight_won",1),
##             #Fight won, decrease odds
##             (assign, ":player_odds_sub", 0),
##             (try_begin),
##               (ge,"$arena_bet_amount",1),
##               (store_div, ":player_odds_sub", "$arena_win_amount", 2),
##             (try_end),
##             (party_get_slot, ":player_odds", "$g_encountered_party", slot_mainplanet_player_odds),
##             (val_add, ":player_odds_sub", 5),
##             (val_sub, ":player_odds", ":player_odds_sub"),
##             (val_max, ":player_odds", 250),
##             (party_set_slot, "$g_encountered_party", slot_mainplanet_player_odds, ":player_odds"),
##           (else_try),
##             #Fight lost, increase odds
##             (assign, ":player_odds_add", 0),
##             (try_begin),
##               (ge,"$arena_bet_amount",1),
##               (store_div, ":player_odds_add", "$arena_win_amount", 2),
##             (try_end),
##             (party_get_slot, ":player_odds", "$g_encountered_party", slot_mainplanet_player_odds),
##             (val_add, ":player_odds_add", 5),
##             (val_add, ":player_odds", ":player_odds_add"),
##             (val_min, ":player_odds", 4000),
##             (party_set_slot, "$g_encountered_party", slot_mainplanet_player_odds, ":player_odds"),
##           (try_end),
##           (store_remaining_team_no,"$arena_winner_team"),
##           (assign, "$g_mt_mode", abm_visit),
##           (party_get_slot, ":arena_mission_template", "$current_town", slot_mainplanet_arena_template),
##           (set_jump_mission, ":arena_mission_template"),
##           (party_get_slot, ":arena_scene", "$current_town", slot_mainplanet_arena),
##           (modify_visitors_at_site, ":arena_scene"),
##           (reset_visitors),
##           (set_visitor, 35, "trp_veteran_fighter"),
##           (set_visitor, 36, "trp_hired_blade"),
##           (set_jump_entry, 50),
##           (jump_to_scene, ":arena_scene"),
##           ]),

  (0, 0, ti_once, [],
   [
     (eq, "$g_mt_mode", abm_tournament),
     (play_sound, "snd_arena_ambiance", sf_looping),
     (call_script, "script_music_set_situation_with_culture", mtf_sit_arena),
     ]),

  (1, 4, ti_once, [(eq, "$g_mt_mode", abm_tournament),
                   (this_or_next|main_hero_fallen),
                   (num_active_teams_le, 1)],
   [
       (try_begin),
         (neg|main_hero_fallen),
         (call_script, "script_end_tournament_fight", 1),
         (call_script, "script_play_victorious_sound"),
         (finish_mission),
       (else_try),
         (call_script, "script_end_tournament_fight", 0),
         (finish_mission),
       (try_end),
       ]),

  (0, 0, ti_once, [], [(eq, "$g_mt_mode", abm_training),(start_presentation, "prsnt_arena_training")]),
  (0, 0, ti_once, [], [(eq, "$g_mt_mode", abm_training),
                       #(assign, "$g_arena_training_max_opponents", 40),
             (assign, "$g_arena_training_max_opponents", 50),    #SW - increased the number of arena opponents
                       (assign, "$g_arena_training_num_agents_spawned", 0),
                       (assign, "$g_arena_training_kills", 0),
                       (assign, "$g_arena_training_won", 0),
                       (call_script, "script_music_set_situation_with_culture", mtf_sit_arena),
                       ]),

  (1, 4, ti_once, [(eq, "$g_mt_mode", abm_training),
                   (store_mission_timer_a, ":cur_time"),
                   (gt, ":cur_time", 3),
                   (assign, ":win_cond", 0),
                   (try_begin),
                     (ge, "$g_arena_training_num_agents_spawned", "$g_arena_training_max_opponents"),#spawn at most X agents
                     (num_active_teams_le, 1),
                     (assign, ":win_cond", 1),
                   (try_end),
                   (this_or_next|eq, ":win_cond", 1),
                   (main_hero_fallen)],
   [
       (get_player_agent_no, ":player_agent"),
       (agent_get_kill_count, "$g_arena_training_kills", ":player_agent", 1),#use this for conversation
       (assign, "$g_arena_training_won", 0),
       (try_begin),
         (neg|main_hero_fallen),
         (assign, "$g_arena_training_won", 1),#use this for conversation
       (try_end),
       (assign, "$g_mt_mode", abm_visit),
       (set_jump_mission, "mt_arena_melee_fight"),
       (party_get_slot, ":arena_scene", "$current_town", slot_mainplanet_arena),
       (modify_visitors_at_site, ":arena_scene"),
       (reset_visitors),
       (set_visitor, 35, "trp_veteran_fighter"),
     #SW - modified set_visitor
     (set_visitor, 36, "trp_champion_fighter"),
       (set_jump_entry, 50),
       (jump_to_scene, ":arena_scene"),
       ]),


  #SW - this appears to be the refresh that spawns the arena fighters
  (0.2, 0, 0,
   [
       (eq, "$g_mt_mode", abm_training),
       (assign, ":num_active_fighters", 0),
       (try_for_agents, ":agent_no"),
         (agent_is_human, ":agent_no"),
         (agent_is_alive, ":agent_no"),
         (agent_get_team, ":team_no", ":agent_no"),
         (is_between, ":team_no", 0 ,7),
         (val_add, ":num_active_fighters", 1),
       (try_end),
       #(lt, ":num_active_fighters", 7),
     (lt, ":num_active_fighters", 9),    #SW - increase the number of fighters in arena at one time
       (neg|main_hero_fallen),
       (store_mission_timer_a, ":cur_time"),
       (this_or_next|ge, ":cur_time", "$g_arena_training_next_spawn_time"),
       (this_or_next|lt, "$g_arena_training_num_agents_spawned", 6),
       (num_active_teams_le, 1),
       (lt, "$g_arena_training_num_agents_spawned", "$g_arena_training_max_opponents"),
      ],
    [
       (assign, ":added_troop", "$g_arena_training_num_agents_spawned"),
       (store_div,  ":added_troop", "$g_arena_training_num_agents_spawned", 6),
       (assign, ":added_troop_sequence", "$g_arena_training_num_agents_spawned"),
       (val_mod, ":added_troop_sequence", 6),
       (val_add, ":added_troop", ":added_troop_sequence"),
       (val_min, ":added_troop", 9),
       (val_add, ":added_troop", "trp_arena_training_fighter_1"),
       (assign, ":end_cond", 10000),
       (get_player_agent_no, ":player_agent"),
       (agent_get_position, pos5, ":player_agent"),
       (try_for_range, ":unused", 0, ":end_cond"),
         (store_random_in_range, ":random_entry_point", 32, 40),
         (neq, ":random_entry_point", "$g_player_entry_point"), # make sure we don't overwrite player
         (entry_point_get_position, pos1, ":random_entry_point"),
         (get_distance_between_positions, ":dist", pos5, pos1),
         (gt, ":dist", 1200), #must be at least 12 meters away from the player
         (assign, ":end_cond", 0),
       (try_end),

    #SW - added script_set_items_for_arena so we can toggle what weapons are used
    (call_script, "script_set_items_for_arena", ":random_entry_point",":added_troop"),

       (add_visitors_to_current_scene, ":random_entry_point", ":added_troop", 1),
       (store_add, ":new_spawned_count", "$g_arena_training_num_agents_spawned", 1),
       (store_mission_timer_a, ":cur_time"),
     #SW - modified how quickly agents spawn
       #(store_add, "$g_arena_training_next_spawn_time", ":cur_time", 14),
       #(store_div, ":time_reduction", ":new_spawned_count", 3),
       #(val_sub, "$g_arena_training_next_spawn_time", ":time_reduction"),
     (try_begin),
      (le, ":new_spawned_count", 10),
      (store_add, "$g_arena_training_next_spawn_time", ":cur_time", 15),
    (else_try),
      (le, ":new_spawned_count", 30),
      (store_add, "$g_arena_training_next_spawn_time", ":cur_time", 10),
    (else_try),
      (store_add, "$g_arena_training_next_spawn_time", ":cur_time", 5),
    (try_end),


       ]),

  (0, 0, 0,
   [
       (eq, "$g_mt_mode", abm_training)
       ],
    [
       (assign, ":max_teams", 6),
       (val_max, ":max_teams", 1),
       (get_player_agent_no, ":player_agent"),
       (try_for_agents, ":agent_no"),
         (agent_is_human, ":agent_no"),
         (agent_is_alive, ":agent_no"),
         (agent_slot_eq, ":agent_no", slot_agent_arena_team_set, 0),
         (agent_get_team, ":team_no", ":agent_no"),
         (is_between, ":team_no", 0 ,7),
         (try_begin),
           (eq, ":agent_no", ":player_agent"),
           (agent_set_team, ":agent_no", 6), #player is always team 6.
         (else_try),
           (store_random_in_range, ":selected_team", 0, ":max_teams"),
          # find strongest team
           (try_for_range, ":t", 0, 6),
             (troop_set_slot, "trp_temp_array_a", ":t", 0),
           (try_end),
           (try_for_agents, ":other_agent_no"),
             (agent_is_human, ":other_agent_no"),
             (agent_is_alive, ":other_agent_no"),
             (neq, ":agent_no", ":player_agent"),
             (agent_slot_eq, ":other_agent_no", slot_agent_arena_team_set, 1),
             (agent_get_team, ":other_agent_team", ":other_agent_no"),
             (troop_get_slot, ":count", "trp_temp_array_a", ":other_agent_team"),
             (val_add, ":count", 1),
             (troop_set_slot, "trp_temp_array_a", ":other_agent_team", ":count"),
           (try_end),
           (assign, ":strongest_team", 0),
           (troop_get_slot, ":strongest_team_count", "trp_temp_array_a", 0),
           (try_for_range, ":t", 1, 6),
             (troop_slot_ge, "trp_temp_array_a", ":t", ":strongest_team_count"),
             (troop_get_slot, ":strongest_team_count", "trp_temp_array_a", ":t"),
             (assign, ":strongest_team", ":t"),
           (try_end),
           (store_random_in_range, ":rand", 5, 100),
           (try_begin),
             (lt, ":rand", "$g_arena_training_num_agents_spawned"),
             (assign, ":selected_team", ":strongest_team"),
           (try_end),
           (agent_set_team, ":agent_no", ":selected_team"),
         (try_end),
         (agent_set_slot, ":agent_no", slot_agent_arena_team_set, 1),
         (try_begin),
           (neq, ":agent_no", ":player_agent"),
           (val_add, "$g_arena_training_num_agents_spawned", 1),
         (try_end),
       (try_end),
       ]),


  ]
