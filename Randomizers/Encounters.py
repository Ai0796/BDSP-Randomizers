#py -m pip install UnityPy
import UnityPy
import random

#PathIDs inside Unity
#DO NOT CHANGE UNLESS GAME IS UPDATED
diamondEncount = 361824127573837173
pearlEncount = -9035030829162387677

pathList = [diamondEncount, pearlEncount]

# make sure the file gamesettings is in this folder
# gamesettings is in Dpr/scriptableassets
src = "gamesettings"

env = UnityPy.load(src)

for obj in env.objects:
    
    if obj.path_id in pathList:
        tree = obj.read_typetree()
        
        ##Two encounter tables are named FieldEncountTable_d (diamond) and FieldEncountTable_p (pearl)
        for area in tree['table']:
            for key in area.keys():
                if type(area[key]) != int:
                    if type(area[key][0]) == dict:
                        for mon in area[key]:
                            if mon['monsNo'] != 0:
                                mon['monsNo'] = random.randint(1,493)
        #Saves the object tree
        obj.save_typetree(tree)
                
# saving an edited file
# apply modifications to the objects
# don't forget to use data.save()
    # ...
    # 
    # 
#This output is uncompressed, make sure to compress using LZ4 in UABEA
with open("randomEncounters", "wb") as f:
    f.write(env.file.save(packer = (64,2)))
