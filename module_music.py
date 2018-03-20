# S T A R   W A R S   C O N Q U E S T   M O D U L E   S Y S T E M
# / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /
# By Taleworlds, HokieBT, MartinF and Swyter - Do not use/copy without permission

from header_music import *

####################################################################################################################
#  Each track record contains the following fields:
#  1) Track id: used for referencing tracks.
#  2) Track file: filename of the track
#  3) Track flags. See header_music.py for a list of available flags
#  4) Continue Track flags: Shows in which situations or cultures the track can continue playing. See header_music.py for a list of available flags
####################################################################################################################

# WARNING: You MUST add mtf_module_track flag to the flags of the tracks located under module directory

tracks = [

#########################################################################################################
#SW - modified music

	# NEW MUSIC TRACKS
	#main title
	("mount_and_blade_title_screen", "swc_intro.ogg", mtf_sit_main_title|mtf_start_immediately|mtf_module_track, 0),

	#SW - some music track names are called by play_track and play_cue_track so these must be the same names as native
	("captured", "swc-capture.ogg", mtf_persist_until_finished|mtf_module_track, 0),
	#("empty_village", "encounter_looted_planet.ogg", mtf_persist_until_finished|mtf_module_track, 0),
	("escape", "swc-escape.ogg", mtf_persist_until_finished|mtf_module_track, 0),  #track_escape

	#ARENA
	("arena_1", "swc-arena-1.ogg", mtf_sit_arena|mtf_module_track, mtf_sit_arena),
	("arena_2", "swc-arena-2.ogg", mtf_sit_arena|mtf_module_track, mtf_sit_arena),

	#FIGHT/BATTLE
	("battle_2", "swc-battle-2.ogg",           mtf_sit_fight|mtf_sit_ambushed|mtf_sit_siege|mtf_module_track, mtf_sit_fight|mtf_sit_ambushed|mtf_sit_siege),
	("battle_3", "swc-battle-3.ogg",           mtf_sit_fight|mtf_sit_ambushed|mtf_sit_siege|mtf_module_track, mtf_sit_fight|mtf_sit_ambushed|mtf_sit_siege),
	#("battle_empire", "SWC-Battle-Empire.ogg", mtf_culture_1|mtf_sit_fight|mtf_sit_ambushed|mtf_sit_siege|mtf_module_track, mtf_sit_fight|mtf_sit_ambushed|mtf_sit_siege|mtf_culture_all),
	("battle_empire", "swc-battle-empire.ogg", mtf_sit_fight|mtf_sit_ambushed|mtf_sit_siege|mtf_module_track, mtf_sit_fight|mtf_sit_ambushed|mtf_sit_siege),

	#TAVERN/CANTINA
	("cantina_1",     "swc-cantina.ogg",   mtf_sit_tavern|mtf_module_track, mtf_sit_tavern),
	("cantina_fight", "swc-bar_fight.ogg", mtf_persist_until_finished|mtf_module_track, 0),		#only used in cantina bar fights

	#DEFEAT/KILLED
	("killed", "swc-defeat.ogg", mtf_persist_until_finished|mtf_sit_killed|mtf_module_track, 0),

	#MAP
	("map_dspace", "swc-deep_space.ogg", mtf_sit_travel|mtf_sit_day|mtf_sit_night|mtf_module_track, mtf_sit_travel|mtf_sit_day|mtf_sit_night),
	("map_1",      "swc-map-1.ogg",      mtf_sit_travel|mtf_sit_day|mtf_sit_night|mtf_module_track, mtf_sit_travel|mtf_sit_day|mtf_sit_night),
	("map_2",      "swc-map-2.ogg",      mtf_sit_travel|mtf_sit_day|mtf_sit_night|mtf_module_track, mtf_sit_travel|mtf_sit_day|mtf_sit_night),
	("map_3",      "swc-map-3.ogg",      mtf_sit_travel|mtf_sit_day|mtf_sit_night|mtf_module_track, mtf_sit_travel|mtf_sit_day|mtf_sit_night),
	("map_4",      "swc-map-4.ogg",      mtf_sit_travel|mtf_sit_day|mtf_sit_night|mtf_module_track, mtf_sit_travel|mtf_sit_day|mtf_sit_night),
	("map_5",      "swc-map-5.ogg",      mtf_sit_travel|mtf_sit_day|mtf_sit_night|mtf_module_track, mtf_sit_travel|mtf_sit_day|mtf_sit_night),
	("map_6",      "swc-map-6.ogg",      mtf_sit_travel|mtf_sit_day|mtf_sit_night|mtf_module_track, mtf_sit_travel|mtf_sit_day|mtf_sit_night),
	("map_7",      "swc-map-7.ogg",      mtf_sit_travel|mtf_sit_day|mtf_sit_night|mtf_module_track, mtf_sit_travel|mtf_sit_day|mtf_sit_night),

	#VICTORY
	("victory", "swc-victory.ogg", mtf_persist_until_finished|mtf_sit_victorious, 0),

	#TOWN/PLANET TRACKS
	("town_bizaar",     "swc-bizaarplanettexture.ogg", mtf_sit_town|mtf_sit_town_infiltrate|mtf_module_track, mtf_sit_town|mtf_sit_town_infiltrate),
	("town_gentle",     "swc-gentle-planet.ogg",       mtf_sit_town|mtf_sit_town_infiltrate|mtf_module_track, mtf_sit_town|mtf_sit_town_infiltrate),
	("town_beautiful",  "swc-beautiful_planet.ogg",    mtf_sit_town|mtf_sit_town_infiltrate|mtf_module_track, mtf_sit_town|mtf_sit_town_infiltrate),
	#TOWN SPECIFIC (doesn't seem to work correctly with the play_track commands so I had to add mtf_persist_until_finished)
	("town_desert",     "swc-dessert-planet.ogg",      mtf_persist_until_finished|mtf_module_track, 0),
	("town_wookiee",    "swc-wookieplanettexture.ogg", mtf_persist_until_finished|mtf_module_track, 0),
	("town_endor",      "swc-endor.ogg",               mtf_persist_until_finished|mtf_module_track, 0),
	("town_bothawui",   "swc-bothawui.ogg",            mtf_persist_until_finished|mtf_module_track, 0),
	("town_felucia",    "swc-felucia.ogg",             mtf_persist_until_finished|mtf_module_track, 0),
	("town_nalhutta",   "swc-nul_hutta.ogg",           mtf_persist_until_finished|mtf_module_track, 0),
	("town_raxusprime", "swc-raxus_prime.ogg",         mtf_persist_until_finished|mtf_module_track, 0),
	#TOWN BATTLES? maybe also use for fights or town_infiltrate ?
	("town_battle",     "swc-planet_battle.ogg",       mtf_persist_until_finished|mtf_module_track, 0),
	#TOWN TESTING
	#("town_test", "test_music.ogg", mtf_persist_until_finished|mtf_module_track, 0),

	#NEW Throne Room Tracks (may also be used for castle entry)
	("throne_empire_1", "swc-empire_throne_1.ogg", mtf_persist_until_finished|mtf_module_track, 0),
	("throne_empire_2", "swc-empire_throne_2.ogg", mtf_persist_until_finished|mtf_module_track, 0),
	("throne_empire_3", "swc-empire_throne_3.ogg", mtf_persist_until_finished|mtf_module_track, 0),
	("throne_hutt_1",   "swc-hutt_throne_1.ogg",   mtf_persist_until_finished|mtf_module_track, 0),
	("throne_hutt_2",   "swc-hutt_throne_2.ogg",   mtf_persist_until_finished|mtf_module_track, 0),
	("throne_hutt_3",   "swc-hutt_throne_3.ogg",   mtf_persist_until_finished|mtf_module_track, 0),
	("throne_rebel_1",  "swc-rebel_throne_1.ogg",  mtf_persist_until_finished|mtf_module_track, 0),
	("throne_rebel_2",  "swc-rebel_throne_2.ogg",  mtf_persist_until_finished|mtf_module_track, 0),
	("throne_rebel_3",  "swc-rebel_throne_3.ogg",  mtf_persist_until_finished|mtf_module_track, 0),
	("throne_rebel_4",  "swc-rebel_throne_4.ogg",  mtf_persist_until_finished|mtf_module_track, 0),

########################################################################################################################

]
