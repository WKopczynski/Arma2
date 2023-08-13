# Description: Find and Save to txt A2 Object Names
#
# Name: A2_searchFile.py
# Version: 0.1
#
# made by: WKopczynski
# 08.2023
#
# Note: This program was tested on files with A2 editor objects placed without additional settings

readFile = 'File.txt'          # path to file with generated A2 mission code
writeFile = 'ObjListArma2.txt' # path to new or existing file in which A2 Object Names will be saved
prefix = 'createVehicle ["'    # part before searching word
suffix = '", ['                # part after searching word

with open(readFile, 'r') as fp:
    with open(writeFile, 'w') as fp2:
        lines = fp.readlines()
        for row in lines:
            if row.find(prefix) != -1:
                row = row.split(prefix,1)[1]
                if row.find(suffix) != -1:
                    name = row.split(suffix,1)[0]
                    print(name)
                    fp2.write(name + '\n')
                
