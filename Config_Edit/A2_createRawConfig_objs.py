# Description: Create raw addon config file with given Object Names
#
# Name: A2_createRawConfig_objs.py
# Version: 0.1
#
# made by: WKopczynski
# 08.2023
#
# Note: This version of tool only helps with creating config file of new addon.
#       Created config MUST be edited to work properly.

readBaseConfig = 'base_config.txt' # Path to base config file
readFile = 'ObjListArma2.txt'      # Path to file with generated A2 mission code
writeFile = 'config.txt'           # Path to new or existing file in which A2 Object Names will be saved
# prefix = 'createVehicle ["'      # Part before searching word
# suffix = '", ['                  # Part after searching word
set1 = 34  # Ending index of 1st part of base config data to copy
set2a = 36 # Start index of 2nd part of base config data to copy
set2b = 38 # Ending index of 2nd part of base config data to copy
set3a = 39 # Start index of 3rd part of base config data to copy
set3b = 39 # Ending index of 3rd part of base config data to copy
set4a = 41 # Start index of 4th part of base config data to copy
set4b = 44 # Ending index of 4th part of base config data to copy

with open(readBaseConfig, 'r') as fbc:   # BASE CONFIG (BC)
    with open(readFile, 'r') as ff:      # OBJ NAMES   (ON)
        with open(writeFile, 'w') as fw: # RAW CONFIG  (RC)
            
            lines_BC = fbc.readlines()
            lines_ON = ff.readlines()
            lenLinesON = len(lines_ON)
            
            # Copy first part of base config
            cl = 0
            while cl < set1:
                fw.write(lines_BC[cl])
                cl += 1
            
            # Create extern classes in CfgVehicles
            for obj in range (0, lenLinesON):
                fw.write('	/*extern*/ class ' + lines_ON[obj])
            
            # Copy second part of base config
            for cl in range (set2a - 1, set2b):
                fw.write(lines_BC[cl])
            
            # Create custom obj class for each object from ON file
            for obj in range (0, lenLinesON):
                fw.write('\n' + '	class <cust_class> : ' + lines_ON[obj].strip('\n') + ' {' + '\n')
                for cl in range (set4a - 1, set4b):
                    fw.write(lines_BC[cl])
            
            fw.write('\n};')