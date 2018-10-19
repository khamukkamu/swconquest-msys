# S T A R   W A R S   C O N Q U E S T   M O D U L E   S Y S T E M
# / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /
# By Taleworlds, HokieBT, MartinF and Swyter - Do not use/copy without permission

from header_skins import *
from ID_particle_systems import *

####################################################################################################################
#  Each skin record contains the following fields:
#  1) Skin id: used for referencing skins.
#  2) Skin flags. Not used yet. Should be 0.
#  3) Body mesh.
#  4) Calf mesh (left one).
#  5) Hand mesh (left one).
#  6) Head mesh.
#  7) Face keys (list)
#  8) List of hair meshes.
#  9) List of beard meshes.
# 10) List of hair textures.
# 11) List of beard textures.
# 12) List of face textures.
# 13) List of voices.
# 14) Skeleton name
# 15) Scale (doesn't fully work yet)
# 16) Blood particles 1 (do not add this if you wish to use the default particles)
# 17) Blood particles 2 (do not add this if you wish to use the default particles)
# 17) Face key constraints (do not add this if you do not wish to use it)
####################################################################################################################

#SW NOTE - there seems to be a maximum value of 16 skins that can be defined

man_face_keys = [
  (20, 0,  0.7, -0.6, "Chin Size"),
  (260,0, -0.6,  1.4, "Chin Shape"),
  (10, 0, -0.5,  0.9, "Chin Forward"),
  (240,0,  0.9, -0.8, "Jaw Width"),
  (210,0, -0.5,  1.0, "Jaw Position"),
  (250,0,  0.8, -1.0, "Mouth-Nose Distance"),
  (200,0, -0.3,  1.0, "Mouth Width"),
  (50, 0, -1.5,  1.0, "Cheeks"),
  (220,0, -0.1,  0.9, "Neck Width"),

  (60, 0, -0.4,  1.35,"Nose Height"),
  (70, 0, -0.6,  0.7, "Nose Width"),
  (80, 0,  1.0, -0.1, "Nose Size"),
  (270,0, -0.5,  1.0, "Nose Shape"),
  (290,0,  0.0,  1.0, "Nasal Curvature"),
  (90, 0, -0.2,  1.4, "Nose Bridge"),

  (100,0, -0.3,  1.5, "Cheek Bones"),
  (150,0, -0.2,  3.0, "Eye Width"),
  (110,0,  1.5, -0.9, "Eye to Eye Dist"),
  (120,0,  1.9, -1.0, "Eye Shape"),
  (130,0, -0.5,  1.1, "Eye Depth"),
  (140,0,  1.0, -1.2, "Eyelids"),

  (160,0,  1.3, -0.2, "Eyebrow Position"),
  (170,0, -0.1,  1.9, "Eyebrow Height"),
 #SW - modified to use Barf's updated male_head model
 #(220,0, -0.1,  0.9, "Eyebrow Depth"),
  (180,0, -1.1,  1.6, "Eyebrow Shape"),
  (230,0,  1.2, -0.7, "Temple Width"),
 #(310,0, -1.1,  1.6, "Zabrak Horns"),

  (30, 0, -0.6,  0.9, "Face Depth"),
  (40, 0,  0.9, -0.6, "Face Ratio"),
  (190,0,  0.0,  0.95,"Face Width"),

  (280,0,0.0 ,1.0 , "Post-Edit"),
]

# Face width-Jaw width Temple width
woman_face_keys = [
  (230,0, 0.8,-1.0, "Chin Size"),
  (220,0,-1.0, 1.0, "Chin Shape"),
  (10, 0,-1.2, 1.0, "Chin Forward"),
  (20, 0,-0.6, 1.2, "Jaw Width"),
  (40, 0,-0.7, 1.0, "Jaw Position"),
  (270,0, 0.9,-0.9, "Mouth-Nose Distance"),
  (30, 0,-0.5, 1.0, "Mouth Width"),
  (50, 0,-0.5, 1.0, "Cheeks"),

  (60, 0,-0.5, 1.0, "Nose Height"),
  (70, 0,-0.5, 1.1, "Nose Width"),
  (80, 0, 1.5,-0.3, "Nose Size"),
  (240,0,-1.0, 0.8, "Nose Shape"),
  (90, 0, 0.0, 1.1, "Nose Bridge"),

  (100,0,-0.5, 1.5, "Cheek Bones"),
  (150,0,-0.4, 1.0, "Eye Width"),
  (110,0, 1.0, 0.0, "Eye to Eye Dist"),
  (120,0,-0.2, 1.0, "Eye Shape"),
  (130,0,-0.1, 1.6, "Eye Depth"),
  (140,0,-0.2, 1.0, "Eyelids"),

  (160,0,-0.2, 1.2, "Eyebrow Position"),
  (170,0,-0.2, 0.7, "Eyebrow Height"),
  (250,0,-0.4, 0.9, "Eyebrow Depth"),
  (180,0,-1.5, 1.2, "Eyebrow Shape"),
  (260,0, 1.0,-0.7, "Temple Width"),

  (200,0,-0.5, 1.0, "Face Depth"),
  (210,0,-0.5, 0.9, "Face Ratio"),
  (190,0,-0.4, 0.8, "Face Width"),

  (280,0, 0.0, 1.0, "Post-Edit")
]
#undead_face_keys = []

#SW - new face keys
#jawa_face_keys      = []		# used tusken body for jawa
tusken_face_keys     = []
rodian_face_keys     = []
moncal_face_keys     = []
trandoshan_face_keys = []
droid_face_keys      = []
#weequay_face_keys   = man_face_keys
wookiee_face_keys    = []
sullustan_face_keys  = []
#chiss_face_keys     = man_face_keys
#chiss_female_face_keys = woman_face_keys
gamorrean_face_keys  = []
twilek_face_keys     = []
twilek_female_face_keys = woman_face_keys

bothan_face_keys = [
  (10,0,0.0,1.0, "Bothan Face Shape"),
  (30,0,0.0,1.0, "Bothan Mouth Forward"),
  (50,0,0.0,1.0, "Bothan Head Size"),
  ( 0,0,1.0,0.0, "Post-Edit")
]

geonosian_face_keys = [
  (10,0,0.0,1.0, "Exoskeleton Shape"),
  (30,0,0.0,1.0, "Exoskeleton Forward"),
  (50,0,1.0,0.0, "Exoskeleton Size"),
  ( 0,0,1.0,0.0, "Post-Edit")
]

clone_face_keys = []
rancor_face_keys = []

chin_size           =   0
chin_shape          =   1
chin_forward        =   2
jaw_width           =   3
jaw_position        =   4
mouth_nose_distance =   5
mouth_width         =   6
cheeks              =   7
nose_height         =   8
nose_width          =   9
nose_size           =  10
nose_shape          =  11
nose_bridge         =  12
cheek_bones         =  13
eye_width           =  14
eye_to_eye_dist     =  15
eye_shape           =  16
eye_depth           =  17
eyelids             =  18
eyebrow_position    =  19
eyebrow_height      =  20
eyebrow_depth       =  21
eyebrow_shape       =  22
temple_width        =  23
face_depth          =  24
face_ratio          =  25
face_width          =  26

comp_less_than      = -1;
comp_greater_than   =  1;

skins = [
  (
    "man", 0,
    "new_man_body", "_", "m_handL",
    "male_head_new", man_face_keys,
    #["man_hair_s","man_hair_m","man_hair_n","man_hair_o", "man_hair_y10", "man_hair_y12","man_hair_p","man_hair_r","man_hair_q","man_hair_v","man_hair_t","man_hair_y6","man_hair_y3","man_hair_y7","man_hair_y9","man_hair_y11","man_hair_u","man_hair_y","man_hair_y2","man_hair_y4"], #man_hair_meshes ,"man_hair_y5","man_hair_y8",
	["man_hair_o", "man_hair_y10", "man_hair_y12","man_hair_u","man_hair_y4","man_hair_s","man_hair_n","man_hair_p","man_hair_r","man_hair_q","man_hair_v","man_hair_t","man_hair_y9","man_hair_y","man_hair_y11","man_hair_y2","man_hair_y3","man_hair_y6","man_hair_y7","man_hair_m","man_hair_y5","man_hair_y8","zabrak_horns"], #man_hair_meshes
    #["beard_e","beard_d","beard_k","beard_l","beard_i","beard_j","beard_z","beard_m","beard_n","beard_y","beard_p","beard_o",   "beard_v", "beard_f", "beard_b", "beard_c","beard_t","beard_u","beard_r","beard_s","beard_a","beard_h","beard_g",], #beard meshes ,"beard_q"
	["beard_i","beard_l","beard_j","beard_r","beard_h","beard_g","beard_d","beard_k","beard_m","beard_n","beard_y","beard_p","beard_o",   "beard_v", "beard_f", "beard_b", "beard_c","beard_t","beard_u","beard_s","beard_a","beard_e","beard_z","beard_q"], #beard meshes
    #["hair_blonde", "hair_red", "hair_brunette", "hair_black", "hair_white"], #hair textures
	["hair_blonde"], #hair textures
    #["beard_blonde","beard_red","beard_brunette","beard_black","beard_white"], #beard_materials
	["beard_blonde"], #beard_materials
    [
		("manface_young_2",0xffcbe0e0,["hair_blonde"],[0xffffffff, 0xffb04717, 0xff502a19]),
		("manface_midage",0xffdfefe1,["hair_blonde"],[0xffffffff, 0xffb04717, 0xff632e18, 0xff502a19, 0xff19100c]),
		("manface_young",0xffd0e0e0,["hair_blonde"],[0xff83301a, 0xff502a19, 0xff19100c, 0xff0c0d19]),
		#("manface_old",0xffd0d0d0,["hair_white","hair_brunette","hair_red","hair_blonde"],[0xffffcded, 0xffbbcded, 0xff99eebb]),
		("manface_young_3",0xffdceded,["hair_blonde"],[0xff2f180e, 0xff171313, 0xff007080c]),
		("manface_7",0xffc0c8c8,["hair_blonde"],[0xff171313, 0xff007080c]),
		("manface_midage_2",0xfde4c8d8,["hair_blonde"],[0xff502a19, 0xff19100c, 0xff0c0d19]),
		("manface_rugged",0xffb0aab5,["hair_blonde"],[0xff171313, 0xff007080c]),
		#("manface_young_4",0xffe0e8e8,["hair_blonde"],[0xff2f180e, 0xff171313, 0xff007080c]),
		#("manface_old_2",0xffd5d5c5,["hair_white"],[0xffffcded, 0xffbbcded, 0xff99eebb]),
		#new faces from JED_Q
		("Jed_Q_1",0xffdfefe1,["hair_blonde"],[0xffffffff, 0xffb04717, 0xff632e18, 0xff502a19, 0xff19100c]),
		("Jed_Q_2",0xffdfefe1,["hair_blonde"],[0xffffffff, 0xffb04717, 0xff632e18, 0xff502a19, 0xff19100c]),
		("Jed_Q_3",0xffdfefe1,["hair_blonde"],[0xffffffff, 0xffb04717, 0xff632e18, 0xff502a19, 0xff19100c]),
		("Jed_Q_4",0xffdfefe1,["hair_blonde"],[0xffffffff, 0xffb04717, 0xff632e18, 0xff502a19, 0xff19100c]),
		("Jed_Q_5",0xffdfefe1,["hair_blonde"],[0xffffffff, 0xffb04717, 0xff632e18, 0xff502a19, 0xff19100c]),
		("Jed_Q_6",0xffdfefe1,["hair_blonde"],[0xffffffff, 0xffb04717, 0xff632e18, 0xff502a19, 0xff19100c]),
		("Jed_Q_7",0xffdfefe1,["hair_blonde"],[0xffffffff, 0xffb04717, 0xff632e18, 0xff502a19, 0xff19100c]),
		("Jed_Q_8",0xffdfefe1,["hair_blonde"],[0xffffffff, 0xffb04717, 0xff632e18, 0xff502a19, 0xff19100c]),
		("Jed_Q_9",0xffdfefe1,["hair_blonde"],[0xffffffff, 0xffb04717, 0xff632e18, 0xff502a19, 0xff19100c]),
		("manface_african",0xff807c8a,["hair_blonde"],[0xff120808, 0xff007080c]),
		("sith_darth_maul",0x006b0808,["hair_blonde"],[0xffffffff, 0xffb04717, 0xff632e18, 0xff502a19, 0xff19100c]),	# from I-V-I-O-R-T
		("palpatine",0xffffffff,["hair_blonde"],[0xffffffff, 0xffb04717, 0xff632e18, 0xff502a19, 0xff19100c]),
		("twilek_face_bib",0x00e1d489,["hair_blonde"],[0xffffffff, 0xffb04717, 0xff632e18, 0xff502a19, 0xff19100c]),
		("chiss_face_a",0x00355bff,["hair_blonde"],[0xff120808, 0xff007080c]),
		("weequay_face_a",0xFF807c8a,["hair_blonde"],[0xFF120808, 0xFF007080c]),	# from I-V-I-O-R-T
		("weequay_face_b",0xFF807c8a,["hair_blonde"],[0xFF120808, 0xFF007080c])		# from I-V-I-O-R-T

     ], #man_face_textures,
    [(voice_die,"snd_man_die"),(voice_hit,"snd_man_hit"),(voice_grunt,"snd_man_grunt"),(voice_grunt_long,"snd_man_grunt_long"),(voice_yell,"snd_man_yell"),(voice_victory,"snd_man_victory")], #voice sounds
	#SW - why was voice_warcry removed?  should we add it back in?
	#[(voice_die,"snd_man_die"),(voice_hit,"snd_man_hit"),(voice_grunt,"snd_man_grunt"),(voice_grunt_long,"snd_man_grunt_long"),(voice_yell,"snd_man_yell"),(voice_warcry,"snd_man_victory"),(voice_victory,"snd_man_victory")], #voice sounds
    "skel_human", 1.0,
    0,0, #psys_swy_damage_sparks,psys_swy_damage_smoke,
    #psys_game_blood,psys_game_blood_2,
    #psys_game_blood_green,psys_game_blood_2_green,
    [[1.7, comp_greater_than, (1.0,face_width), (1.0,temple_width)], #constraints: ex: 1.7 > (face_width + temple_width)
     [0.3, comp_less_than, (1.0,face_width), (1.0,temple_width)],
     [1.7, comp_greater_than, (1.0,face_width), (1.0,face_depth)],
     [0.3, comp_less_than, (1.0,eyebrow_height), (1.0,eyebrow_position)],
     [1.7, comp_greater_than, (1.0,eyebrow_height), (1.0,eyebrow_position)],
     [-0.7, comp_less_than, (1.0,nose_size), (-1.0,nose_shape)],
     [0.7, comp_greater_than, (1.0,nose_size), (-1.0,nose_shape)],
     [2.7, comp_greater_than, (1.0,chin_size), (1.0,mouth_nose_distance), (1.0,nose_height), (-1.0,face_width)],
     ]
  ),

  (
    "woman", skf_use_morph_key_10,
    "new_woman_body",  "_", "w_handL",
    "female_head_new", woman_face_keys,
    ["woman_hair_p","woman_hair_n","woman_hair_o","woman_hair_q","woman_hair_r","woman_hair_t","woman_hair_s","woman_hair_buns","zabrak_horns"], #woman_hair_meshes
	#    ["woman_hair_a","woman_hair_b","woman_hair_c","woman_hair_d","woman_hair_e","woman_hair_f","woman_hair_g"], #woman_hair_meshes
    [],
    #["hair_blonde", "hair_red", "hair_brunette", "hair_black", "hair_white"], #hair textures
	["hair_blonde"], #hair textures
    [],
    [
      ("womanface_young",0xffe3e8ef,["hair_blonde"],[0xffffffff, 0xffb04717, 0xff502a19, 0xff19100c]),
      ("womanface_a",0xffe8dfe5,["hair_blonde"],[0xff502a19, 0xff19100c, 0xff0c0d19]),
      ("womanface_b",0xffdfdfdf,["hair_blonde"],[0xffa5481f, 0xff502a19, 0xff19100c, 0xff0c0d19]),
      ("womanface_new_a",0xffe8dfe5,["hair_blonde"],[0xff502a19, 0xff19100c, 0xff0c0d19]),
      ("womanface_new_b",0xffdfdfdf,["hair_blonde"],[0xffa5481f, 0xff502a19, 0xff19100c, 0xff0c0d19]),
      ("Jed_Q_w_1",0xffe3e8ef,["hair_blonde"],[0xffffffff, 0xffb04717, 0xff502a19, 0xff19100c]),	#from Jed_Q
      ("womanface_brown",0xffaf9f7e,["hair_blonde"],[0xff19100c, 0xff0c0d19, 0xff007080c]),
      ("sibylla_womanface_amidala",0xffe3e8ef,["hair_blonde"],[0xffffffff, 0xffb04717, 0xff502a19, 0xff19100c]),	#from Jed_Q
      ("womanface_african",0xff808080,["hair_blonde"],[0xff120808, 0xff007080c]),
      ("sith_darth_maul_female",0x0097392c,["hair_blonde"],[0xffffffff, 0xffb04717, 0xff632e18, 0xff502a19, 0xff19100c]),	# from I-V-I-O-R-T
      ("chiss_female_face_a",0x00355bff,["hair_blonde"],[0xff120808, 0xff007080c]),
      ("womanface_new_young",0xffe3e8ef,["hair_blonde"],[0xffffffff, 0xffb04717, 0xff502a19, 0xff19100c]),
      #("woman_face_nightsister",0x00c2b59a,["hair_blonde"],[0xff120808, 0xff34312a]),
      #("woman_face_silri",0x00c2b59a,["hair_blonde"],[0xff120808, 0xff34312a]),
#     ("womanface_midage",0xffe5eaf0,["hair_black","hair_brunette","hair_red","hair_white"],[0xffffcded, 0xffbbcded, 0xff99eebb]),
     ],#woman_face_textures
# HC - Added in new sounds for snd_woman_die - #SW also added in voice_yell
    [(voice_die,"snd_woman_die"),(voice_hit,"snd_woman_hit"),(voice_grunt,"snd_woman_grunt"),(voice_grunt_long,"snd_woman_grunt_long"),(voice_yell,"snd_woman_yell"),(voice_victory,"snd_woman_victory")], #voice sounds
    "skel_human", 1.0,
    0,0, #psys_swy_damage_sparks,psys_swy_damage_smoke,
    #psys_game_blood,psys_game_blood_2,
  ),

#SW - had to un-comment undead in order to get next skins to work, nevermind, I just modified my skin id's in head_troops.py
  # (
    # "undead", 0,
    # "undead_body", "undead_calf_l", "undead_handL",
    # "undead_head", undead_face_keys,
    # [],
    # [],
     # ["hair_blonde"], #hair textures NOTE - you MUST have a hair texture (even if it is not used) for the game not to crash
    # [],
    # [("undeadface_a",0xffffffff,[]),
     # ("undeadface_b",0xffcaffc0,[]),
     # ], #undead_face_textures
    # [], #voice sounds
    # "skel_human", 1.0,
  # ),

 #SW - new jawa skin
   (
     "jawa", 0,
     "tusken_body", "tusken_calf_l", "tusken_gloveL",
     "tusken_head", tusken_face_keys,
     [],
     [],
     ["hair_blonde"], #hair textures NOTE - you MUST have a hair texture (even if it is not used) for the game not to crash
     [],
     [
		("tusken_face_a",0xffffffff,[])
	 ], #undead_face_textures
     [(voice_die,"snd_jawa_die"),(voice_hit,"snd_jawa_hit"),(voice_grunt,"snd_jawa_grunt"),(voice_grunt_long,"snd_jawa_grunt_long"),(voice_yell,"snd_jawa_yell"),(voice_warcry,"snd_jawa_victory"),(voice_victory,"snd_jawa_victory")], #man voice sounds
     #"skel_human", 1.0,
	 "skel_human", 0.76,		#attempting to make the hitbox a little smaller
	 #"skel_jawa", 1.0,		#new skel_jawa skeleton
	 0,0, #psys_swy_damage_sparks,psys_swy_damage_smoke,
    #psys_game_blood,psys_game_blood_2,
   ),

 #SW - new tusken skin
   (
     "tusken", 0,
     "tusken_body", "tusken_calf_l", "tusken_gloveL",
     "tusken_head", tusken_face_keys,
     [],
     [],
     ["hair_blonde"], #hair textures NOTE - you MUST have a hair texture (even if it is not used) for the game not to crash
     [],
     [
		("tusken_face_a",0xffffffff,[])
	], #face_textures
     [(voice_die,"snd_tusken_die"),(voice_hit,"snd_tusken_hit"),(voice_grunt,"snd_tusken_grunt"),(voice_grunt_long,"snd_tusken_grunt_long"),(voice_yell,"snd_tusken_yell"),(voice_warcry,"snd_tusken_victory"),(voice_victory,"snd_tusken_victory")], #man voice sounds
     "skel_human", 0.9,
    0,0, #psys_swy_damage_sparks,psys_swy_damage_smoke,
    #psys_game_blood,psys_game_blood_2,
   ),

 #SW - new rodian skin
   (
     "rodian", 0,
     "rodian_body", "rodian_calf_l", "rodian_handL",
     "rodian_head", tusken_face_keys,
     [],
     [],
     ["hair_blonde"], #hair textures NOTE - you MUST have a hair texture (even if it is not used) for the game not to crash
     [],
     [
		("rodian_face_a",0xffffffff,[]),
		("rodian_face_b",0xffffffff,[]),
		("rodian_face_c",0xffffffff,[])
	 ], #face_textures
     [(voice_die,"snd_rodian_die"),(voice_hit,"snd_rodian_hit"),(voice_grunt,"snd_rodian_grunt"),(voice_grunt_long,"snd_rodian_grunt_long"),(voice_yell,"snd_rodian_yell"),(voice_warcry,"snd_rodian_victory"),(voice_victory,"snd_rodian_victory")], #man voice sounds
     "skel_human", 0.86,
    0,0, #psys_swy_damage_sparks,psys_swy_damage_smoke,
    #psys_game_blood,psys_game_blood_2,
   ),

 #SW - new moncal skin
   (
     "moncal", 0,
     "new_moncal_body", "_", "moncal_mittenL",
#     "moncal_body", "moncal_calf_l", "moncal_mittenL",
     "moncal_head", moncal_face_keys,
     [],
     [],
     ["hair_blonde"], #hair textures NOTE - you MUST have a hair texture (even if it is not used) for the game not to crash
     [],
     [("moncal_face_a",0xffffffff,[])
	 ], #face_textures
     [(voice_die,"snd_man_die"),(voice_hit,"snd_man_hit"),(voice_grunt,"snd_man_grunt"),(voice_grunt_long,"snd_man_grunt_long"),(voice_yell,"snd_man_yell"),(voice_victory,"snd_man_victory")], #man voice sounds
     "skel_human", 1.1,
    0,0, #psys_swy_damage_sparks,psys_swy_damage_smoke,
    #psys_game_blood,psys_game_blood_2,
   ),

 #SW - new trandoshan skin
   (
     "trandoshan", 0,
	 #"trandoshan_body", "trandoshan_foot_L", "trandoshan_handL",
	 #"trandoshan_body", "trandoshan_foot_L", "trandoshan_clawL",
	 "new_trandoshan_body", "_", "_",
     "_", trandoshan_face_keys,
     [],
     [],
     ["hair_blonde"], #hair textures NOTE - you MUST have a hair texture (even if it is not used) for the game not to crash
     [],
     [
		#("trandoshan_face_a",0xffffffff,[]),	#original, no longer used
		("trandoshan_face_yellow",0xffb0b14e,[]),	#yellow
		("trandoshan_face_green",0xff70b877,[])		#green
	 ], #face_textures
     [(voice_die,"snd_trandoshan_die"),(voice_hit,"snd_trandoshan_hit"),(voice_grunt,"snd_trandoshan_grunt"),(voice_grunt_long,"snd_trandoshan_grunt_long"),(voice_yell,"snd_trandoshan_yell"),(voice_warcry,"snd_trandoshan_victory"),(voice_victory,"snd_trandoshan_victory")], #man voice sounds
     "skel_human", 1.0,
	 #psys_game_blood_green,psys_game_blood_2_green,
    0,0, #psys_swy_damage_sparks,psys_swy_damage_smoke,
    #psys_game_blood,psys_game_blood_2,
   ),

 #SW - new rseries skin
   (
     "droid", 0,
     #"transparent_body", "transparent_calf_l", "transparent_handL",
	 #"transparent_head", droid_face_keys,
    "droid_body", "droid_leg_L", "droid_hand_L",
    "droid_head_half", droid_face_keys,
	#"droid_head", droid_face_keys,
     [],
     [],
     ["hair_blonde"], #hair textures NOTE - you MUST have a hair texture (even if it is not used) for the game not to crash
     [],
     [("droid_head",0xffffffff,[])
	 ], #face_textures
#     [(voice_die,"snd_droid_die"),(voice_hit,"snd_droid_hit"),(voice_grunt,"snd_droid_grunt"),(voice_grunt_long,"snd_droid_grunt_long"),(voice_yell,"snd_droid_yell"),(voice_warcry,"snd_droid_victory"),(voice_victory,"snd_droid_victory")], #r2series voice sounds
     [(voice_die,"snd_battledroid_die"),(voice_hit,"snd_battledroid_hit"),(voice_grunt,"snd_battledroid_grunt"),(voice_grunt_long,"snd_battledroid_grunt_long"),(voice_yell,"snd_battledroid_yell"),(voice_warcry,"snd_battledroid_victory"),(voice_victory,"snd_battledroid_victory")], #r2series voice sounds

     #"skel_human", 1.0,
	 "skel_human", 1.1,		#attempting to make the hitbox a little smaller
	 #"skel_horse", 1.0,	# does doing this seem to cause the game to randomly crash?  seemed to happen a few times after I made this change, so not sure if its related.  AncientWanker confirmed this was an issue
    0,0, #psys_swy_damage_sparks,psys_swy_damage_smoke,
	 #psys_droid_blood,psys_droid_blood_2,
   ),

 #SW - new weequay skin (commented out since there is a limit on the number of skins, used a chiss face texture on the humans instead)
   # (
     # "weequay", 0,
     # "weequay_body", "weequay_calf_l", "weequay_handL",
     # "weequay_head", weequay_face_keys,
     # ["man_hair_t"], #man_hair_meshes
     # [],
     # ["hair_blonde"], #hair textures NOTE - you MUST have a hair texture (even if it is not used) for the game not to crash
     # [],
     # [("weequay_face_a",0xffffffff,[]),("weequay_face_b",0xffffffff,[])
	 # ], #face_textures
     # [(voice_die,"snd_man_die"),(voice_hit,"snd_man_hit"),(voice_grunt,"snd_man_grunt"),(voice_grunt_long,"snd_man_grunt_long"),(voice_yell,"snd_man_yell"),(voice_victory,"snd_man_victory")], #man voice sounds
     # "skel_human", 1.0,
   # ),

 #SW - new wookiee skin
   (
     "wookiee", 0,
     "new_wookiee_body", "_", "_",
     #"wookiee_head_new_half", wookiee_face_keys,
	 "wookiee_head_new_half", wookiee_face_keys,
     [],
     [],
     ["hair_blonde"], #hair textures NOTE - you MUST have a hair texture (even if it is not used) for the game not to crash
     [],
     [
		("wookiee_face_a_new",0xffffffff,[]),
		("wookiee_face_a_new2",0xffffffff,[]),
		#("wookiee_face_a",0xffffffff,[]),
		#("wookiee_face_b",0xffffffff,[])
	 ], #face_textures
     [(voice_die,"snd_wookiee_die"),(voice_hit,"snd_wookiee_hit"),(voice_grunt,"snd_wookiee_grunt"),(voice_grunt_long,"snd_wookiee_grunt_long"),(voice_yell,"snd_wookiee_yell"),(voice_warcry,"snd_wookiee_victory"),(voice_victory,"snd_wookiee_victory")], #man voice sounds
     "skel_human", 1.3,
	 #"skel_wookiee", 1.0,
    0,0, #psys_swy_damage_sparks,psys_swy_damage_smoke,
    #psys_game_blood,psys_game_blood_2,
   ),

#SW - new sullustan skin
   (
     "sullustan", 0,
     "new_sullustan_body", "_", "sullustan_handL",
     "sullustan_head", sullustan_face_keys,
     [],
     [],
     ["hair_blonde"], #hair textures NOTE - you MUST have a hair texture (even if it is not used) for the game not to crash
     [],
     [("sullustan_face_a",0xffffffff,[])
	 ], #face_textures
     [(voice_die,"snd_man_die"),(voice_hit,"snd_man_hit"),(voice_grunt,"snd_man_grunt"),(voice_grunt_long,"snd_man_grunt_long"),(voice_yell,"snd_sullustan_yell"),(voice_warcry,"snd_sullustan_victory"),(voice_victory,"snd_sullustan_victory")], #man voice sounds
     "skel_human", 1.0,
    0,0, #psys_swy_damage_sparks,psys_swy_damage_smoke,
    #psys_game_blood,psys_game_blood_2,
   ),

 #SW - new gamorrean skin
   (
     "gamorrean", 0,
     "gamorrean_body", "_", "gamorrean_handL",
     "gamorrean_head", gamorrean_face_keys,
     [],
     [],
     ["hair_blonde"], #hair textures NOTE - you MUST have a hair texture (even if it is not used) for the game not to crash
     [],
     [("gamorrean_face_a",0xffffffff,[])
	 ], #face_textures
     [(voice_die,"snd_gamorrean_die"),(voice_hit,"snd_gamorrean_hit"),(voice_grunt,"snd_gamorrean_grunt"),(voice_grunt_long,"snd_gamorrean_grunt_long"),(voice_yell,"snd_gamorrean_yell"),(voice_warcry,"snd_gamorrean_victory"),(voice_victory,"snd_gamorrean_victory")], #man voice sounds
     "skel_human", 0.87,
    0,0, #psys_swy_damage_sparks,psys_swy_damage_smoke,
    #psys_game_blood,psys_game_blood_2,
   ),

 #SW - new twilek skin
   (
     "twilek", 0,
     "new_twilek_body", "_", "twilek_handL",
     "twilek_head", twilek_face_keys,
     [],
     [],
     ["hair_blonde"], #hair textures NOTE - you dddMUST have a hair texture (even if it is not used) for the game not to crash
     [],
     #[("twilek_face_a",0xffffffff,[]),("twilek_face_b",0xff000000,[]),("twilek_face_c",0xff0000ff,[]),("twilek_face_d",0xff00ff00,[]),("twilek_face_e",0xffff0000,[])
	 [
		#("twilek_face_tan",0xffffffff,[]),
		("twilek_face_red",0x00ff5757,[]),
		("twilek_face_green",0x0057ff57,[]),
		("twilek_face_blue",0x00355bff,[]),
		("twilek_face_bib",0x00e1d489,[]),
		("sith_darth_maul",0x006b0808,[])	# from I-V-I-O-R-T
		#notes on good body hue:  Yellow = 0x00fff76f, Dark Blue = 0x00008ce5

	 ], #face_textures
     [(voice_die,"snd_man_die"),(voice_hit,"snd_man_hit"),(voice_grunt,"snd_man_grunt"),(voice_grunt_long,"snd_man_grunt_long"),(voice_yell,"snd_man_yell"),(voice_victory,"snd_man_victory")], #man voice sounds
     "skel_human", 1.0,
    0,0, #psys_swy_damage_sparks,psys_swy_damage_smoke,
    #psys_game_blood,psys_game_blood_2,
   ),

 #SW - new twilek female skin
  (
    "twilek_female", skf_use_morph_key_10,
    #"twilek_female_body",  "twilek_female_calf_l", "twilek_female_handL",
	"new_twilekwomen_body", "_", "twilek_female_handL",
    "twilek_female_head_new", twilek_female_face_keys,
    [], #woman_hair_meshes
    [],
    ["hair_blonde"], #hair textures NOTE - you MUST have a hair texture (even if it is not used) for the game not to crash
    [],
	[
		#("twilek_female_face_tan",0xffffffff,[]),
		("twilek_female_face_red",0x00ff5757,[]),
		("twilek_female_face_green",0x0081ba68,[]),
		("twilek_female_face_blue",0x006e79ba,[]),
		("sith_darth_maul_female",0x007b2010,[]),
		#notes on good body hue:  Yellow = 0x00fff76f, Dark Blue = 0x00008ce5, 97392c = good red color
     ],#woman_face_textures
# HC - Added in new sounds for snd_woman_die	#SW - also added in voice_yell
    [(voice_die,"snd_woman_die"),(voice_hit,"snd_woman_hit"),(voice_grunt,"snd_woman_grunt"),(voice_grunt_long,"snd_woman_grunt_long"),(voice_yell,"snd_twilek_female_yell"),(voice_victory,"snd_twilek_female_victory")], #voice sounds
    "skel_human", 1.0,
    0,0, #psys_swy_damage_sparks,psys_swy_damage_smoke,
    #psys_game_blood,psys_game_blood_2,
  ),

 #SW - new bothan skin
   (
     "bothan", 0,
     "new_bothan_body", "_", "bothan_handL",
     "bothan_head", bothan_face_keys,
     ["bothan_hair_a","bothan_hair_b","bothan_hair_c"],	#hair meshes
     [],
     #["hair_blonde"], #hair textures NOTE - you MUST have a hair texture (even if it is not used) for the game not to crash
	 ["bothan_hair"], #hair textures NOTE - you MUST have a hair texture (even if it is not used) for the game not to crash
     [],
     [("bothan_face_a",0xffffffff,[])
	 ], #face_textures
     [(voice_die,"snd_man_die"),(voice_hit,"snd_man_hit"),(voice_grunt,"snd_man_grunt"),(voice_grunt_long,"snd_man_grunt_long"),(voice_yell,"snd_man_yell"),(voice_victory,"snd_man_victory")], #man voice sounds
     "skel_human", 0.9,
    0,0, #psys_swy_damage_sparks,psys_swy_damage_smoke,
    #psys_game_blood,psys_game_blood_2,
   ),

 #SW - new geonosian skin
   (
     "geonosian", 0,
     "new_geonosian_body", "_", "_",
     "geonosian_head", geonosian_face_keys,
     [],
     [],
     ["hair_blonde"], #hair textures NOTE - you MUST have a hair texture (even if it is not used) for the game not to crash
     [],
     [("geonosian_face_a",0xffffffff,[])
	 ], #face_textures
     [(voice_die,"snd_geonosian_die"),(voice_hit,"snd_geonosian_hit"),(voice_grunt,"snd_geonosian_grunt"),(voice_grunt_long,"snd_geonosian_grunt_long"),(voice_yell,"snd_geonosian_yell"),(voice_warcry,"snd_geonosian_victory"),(voice_victory,"snd_geonosian_victory")], #man voice sounds
     "skel_human", 0.88,
	 0,0, #psys_swy_damage_sparks,psys_swy_damage_smoke,
   ),

	#SW - new rancor skin
   (
     "rancor", 0,
     "_", "_", "_",
     "_", rancor_face_keys,
     [],
     [],
     ["hair_blonde"], #hair textures NOTE - you MUST have a hair texture (even if it is not used) for the game not to crash
     [],
     [("default",0xffffffff,[])
	 ], #face_textures
     [(voice_die,"snd_gamorrean_die"),(voice_hit,"snd_gamorrean_hit"),(voice_grunt,"snd_gamorrean_grunt"),(voice_grunt_long,"snd_gamorrean_grunt_long"),(voice_yell,"snd_gamorrean_yell"),(voice_warcry,"snd_gamorrean_victory"),(voice_victory,"snd_gamorrean_victory")], #man voice sounds
     "skel_human", 1.1,
	 #"skel_rancor", 1.0,	#new rancor skeleton
    0,0, #psys_swy_damage_sparks,psys_swy_damage_smoke,
    #psys_game_blood,psys_game_blood_2,
   ),

   # #SW - new clone skin
   # (
    # "clone", 0,
    # "man_body", "man_calf_l", "m_handL",
    # "cloneface", clone_face_keys,
     # [],
     # [],
     # ["hair_blonde"], #hair textures NOTE - you MUST have a hair texture (even if it is not used) for the game not to crash
     # [],
     # [	# decent skin color = ff988d8c
		# ("cloneface",0xff797271,[]),
		# ("cloneface_scar",0xff797271,[])
	 # ], #face_textures
     # [(voice_die,"snd_man_die"),(voice_hit,"snd_man_hit"),(voice_grunt,"snd_man_grunt"),(voice_grunt_long,"snd_man_grunt_long"),(voice_yell,"snd_man_yell"),(voice_victory,"snd_man_victory")], #man voice sounds
     # "skel_human", 1.0,
   # ),

 # #SW - new klatooinian skin
   # (
    # "klatooinian", 0,
    # "man_body", "man_calf_l", "m_handL",
    # "cloneface", clone_face_keys,
     # [],
     # [],
     # ["hair_blonde"], #hair textures NOTE - you MUST have a hair texture (even if it is not used) for the game not to crash
     # [],
     # [	# decent skin color = ff988d8c
		# ("cloneface",0xff797271,[]),
		# ("cloneface_scar",0xff797271,[])
	 # ], #face_textures
     # [(voice_die,"snd_man_die"),(voice_hit,"snd_man_hit"),(voice_grunt,"snd_man_grunt"),(voice_grunt_long,"snd_man_grunt_long"),(voice_yell,"snd_man_yell"),(voice_victory,"snd_man_victory")], #man voice sounds
     # "skel_human", 1.0,
   # ),

 # #SW - new chiss skin (commented out since there is a limit on the number of skins, used a chiss face texture on the humans instead)
   # (
     # "chiss", 0,
     # "chiss_body", "chiss_calf_l", "chiss_handL",
     # "chiss_head", chiss_face_keys,
     # ["man_hair_u","man_hair_o","man_hair_y8","man_hair_y10","man_hair_y12"], #man_hair_meshes
     # [],
     # ["hair_blonde"], #hair textures NOTE - you MUST have a hair texture (even if it is not used) for the game not to crash
     # [],
     # [("chiss_face_a",0xffffffff,[])
	 # ], #face_textures
     # [(voice_die,"snd_man_die"),(voice_hit,"snd_man_hit"),(voice_grunt,"snd_man_grunt"),(voice_grunt_long,"snd_man_grunt_long"),(voice_yell,"snd_man_yell"),(voice_victory,"snd_man_victory")], #man voice sounds
     # "skel_human", 1.0,
   # ),

 # #SW - new chiss female skin (commented out since there is a limit on the number of skins, used a chiss face texture on the humans instead)
  # (
    # "chiss_female", skf_use_morph_key_10,
    # "chiss_female_body",  "chiss_female_calf_l", "chiss_female_handL",
    # "chiss_female_head", chiss_female_face_keys,
    # ["woman_hair_n","woman_hair_o","woman_hair_p","woman_hair_r","woman_hair_t"], #woman_hair_meshes
    # [],
    # ["hair_blonde"], #hair textures NOTE - you MUST have a hair texture (even if it is not used) for the game not to crash
    # [],
	# [("chiss_female_face_a",0xffffffff,[])
     # ],#woman_face_textures
# # HC - Added in new sounds for snd_woman_die
    # [(voice_die,"snd_woman_die"),(voice_hit,"snd_woman_hit"),(voice_grunt,"snd_woman_grunt"),(voice_grunt_long,"snd_woman_grunt_long"),(voice_victory,"snd_woman_victory")], #voice sounds
    # "skel_human", 1.0,
  # ),

]

