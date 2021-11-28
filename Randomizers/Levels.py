#py -m pip install UnityPy
import UnityPy
import random
from PyQt5.QtWidgets import QTextEdit
import os
from pathlib import Path

#PathIDs inside Unity
#DO NOT CHANGE UNLESS GAME IS UPDATED
diamondEncount = 361824127573837173
pearlEncount = -9035030829162387677
modPath = "romfs/StreamingAssets/AssetAssistant/Dpr/scriptableobjects"

pathList = [diamondEncount, pearlEncount]
# make sure the file gamesettings is in this folder
# gamesettings is in Dpr/scriptableassets

        
def RandomizeLevels(text,flat, min, max):

    # Checks if romfs path already exist
    cwd = os.getcwd()
    if os.path.exists(modPath) == True:
        if os.path.isfile(modPath + '/gamesettings') == True:
            os.chdir(modPath)

    src = "gamesettings"
    env = UnityPy.load(src)  
    text.append("Gamesettings Loaded.")
    text.append("Randomizing Pokemon Levels.")
    for obj in env.objects:
        
        if obj.path_id in pathList:
            tree = obj.read_typetree()
            
            ##Two encounter tables are named FieldEncountTable_d (diamond) and FieldEncountTable_p (pearl)
            for area in tree['table']:
                for key in area.keys():
                    if type(area[key]) != int:
                        if type(area[key][0]) == dict:
                            for mon in area[key]:
                                if mon['minlv'] != 0:
                                    if flat:
                                        mon['minlv'] = random.choice(range(min, max))
                                    else:
                                        if random.choice(0,1) == 1:
                                            mon['minlv'] *= (random.choice(range(min, max))/100 * 100)
                                        else:
                                            mon['minlv'] *= (random.choice(range(min, max))/100 * -100)
            #Saves the object tree
            obj.save_typetree(tree)
            text.append("Randomzing minLevels Done.")
    for obj in env.objects:
        if obj.path_id in pathList:
            tree = obj.read_typetree()
            
            ##Two encounter tables are named FieldEncountTable_d (diamond) and FieldEncountTable_p (pearl)
            for area in tree['table']:
                for key in area.keys():
                    if type(area[key]) != int:
                        if type(area[key][0]) == dict:
                            for mon in area[key]:
                                if mon['maxlv'] != 0:
                                    if flat:
                                        mon['maxlv'] = random.choice(range(min, max))
                                    else:
                                        if random.choice(0,1) == 1:
                                            mon['maxlv'] *= (random.choice(range(min, max))/100 * 100)
                                        else:
                                            mon['maxlv'] *= (random.choice(range(min, max))/100 * -100)
            #Saves the object tree
            obj.save_typetree(tree)
            text.append("Randomzing MaxLevels Done.")
    # saving an edited file
    # apply modifications to the objects
    # don't forget to use data.save()
        # ...
        # 
        # 
    #This output is uncompressed, make sure to compress using LZ4 in UABEA
    if cwd == os.getcwd():
        Path(modPath).mkdir(parents=True, exist_ok=True)
        os.chdir(modPath)
        
    with open("gamesettings", "wb") as f:
        f.write(env.file.save(packer = (64,2)))
    text.append("Levels Saved.")

    os.chdir(cwd)
   
