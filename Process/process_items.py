import string

from process_common import *
from module_items import *
from process__swyhelper import *

def get_item_code(item):
  prefix = "it_"
  code = prefix + item[0]
  return code

def save_python_header():
  file = open("./IDs/ID_items.py","w")
  for i_item in xrange(len(items)):
    file.write("itm_%s = %d\n"%(convert_to_identifier(items[i_item][0]),i_item))
  file.close()

def write_items(variable_list,variable_uses,tag_uses,quick_strings):
  itemkinds_file_name = export_dir + "item_kinds1.txt"
  ofile = open(itemkinds_file_name,"w")
  ofile.write("itemsfile version 3\n")
  ofile.write("%d\n"%len(items))
  for item in items:
    if (item[3] & itp_merchandise) > 0:
      id_no = find_object(items,convert_to_identifier(item[0]))
      add_tag_use(tag_uses,tag_item,id_no)
    ofile.write(" itm_%s %s %s %d "%(convert_to_identifier(item[0]),replace_spaces(item[1]),replace_spaces(item[1]),len(item[2])))
    item_variations = item[2]
##########################################################################
# Autoloot
##########################################################################
# encode item difficulty in less-significant digit of price (only for items over 50 denars, all items below 50 denars assumed to have 0 difficulty)
    if (item[5] >= 50):
	  item[5] -= item[5] % 10
	  diff = get_difficulty(item[6])
	  if (diff > 5):
		diff-= 5
	  item[5] += diff
# End Autoloot
##########################################################################

    for item_variation in item_variations:
      #swy-- different dummy mesh for warband, for invisible objects, fixes game crashing
      #      when it tries to add a missing "_" missile mesh to a shield that has been hit.
      from module_info import wb_compile_switch as is_a_wb_item

      item_variation = list(item_variation)

      if is_a_wb_item:

        for i, mesh in enumerate(item_variation):
          if type(mesh) is str and mesh == "_" or mesh == "0":
            #print item,item_variation,i,mesh; print "\n\n"
            item_variation[i] = "dummy_mesh"
      # --
      ofile.write(" %s %d "%(item_variation[0],item_variation[1]))

    #swy-- don't make blaster bolts or force effects pickupable, ignore gravity
    if is_a_wb_item and                          \
     ( ((item[3] & 0xff) == itp_type_bolts)   or \
       ((item[3] & 0xff) == itp_type_arrows) or  \
       ((item[3] & 0xff) == itp_type_bullets) or \
       ((item[3] & 0xff) == itp_type_thrown and item[0] not in ["twilek_dagger_throwing",
                                                                "discblade",
                                                                "throwing_axes",
                                                                "thermal_detonator1",
                                                                "thermal_detonator2",
                                                                "thermal_detonator3"]) ):
      #print "%x %x %x %s" % (itp_type_bolts, itp_type_thrown, item[3], item); print "\n\n"
      item[3] |= itp_ignore_gravity | itp_no_pick_up_from_ground

    ofile.write(" %d %d %d %d %s %d %d %d %d %d %d %d %d %d %d %d %d\n"%(item[3], item[4], item[5], item[7],
                                                   swytrailzro(get_weight(item[6])),
                                                   get_abundance(item[6]),
                                                   get_head_armor(item[6]),
                                                   get_body_armor(item[6]),
                                                   get_leg_armor(item[6]),
                                                   get_difficulty(item[6]),
                                                   get_hit_points(item[6]),
                                                   get_speed_rating(item[6]),
                                                   get_missile_speed(item[6]),
                                                   get_weapon_length(item[6]),
                                                   get_max_ammo(item[6]),
                                                   get_thrust_damage(item[6]),
                                                   get_swing_damage(item[6]),
                                                               ))

    if (len(item) > 9):
      ofile.write(" %d\n"%(len(item[9])))
      for item_faction in item[9]:
        ofile.write(" %d"%item_faction)
      ofile.write("\n")
    else:
      ofile.write(" 0\n")
    trigger_list = []
    if (len(item) > 8):
      trigger_list = item[8]
    save_simple_triggers(ofile,trigger_list, variable_list,variable_uses,tag_uses,quick_strings)


  ofile.close()

print "Exporting item data..."

if len(items)>=915:
  print "----\r\n Warning! Mod over the 1.011 item limit. Crashie on battles.\r\n----"

save_python_header()

from module_info import *

from process_common import *
from process_operations import *

variable_uses = []
variables = load_variables(export_dir,variable_uses)
tag_uses = load_tag_uses(export_dir)
quick_strings = load_quick_strings(export_dir)
write_items(variables,variable_uses,tag_uses,quick_strings)
save_variables(export_dir,variables,variable_uses)
save_tag_uses(export_dir,tag_uses)
save_quick_strings(export_dir,quick_strings)
#print "Finished with Items."
