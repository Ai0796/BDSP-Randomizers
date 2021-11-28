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

        
def RandomizeLevels(text, flat, min, max):

    # Checks if romfs path already exist
    cwd = os.getcwd()
    
    src = "gamesettings"
    
    outputPath = os.path.join(cwd, "mods", modPath)
    
    if os.path.exists(outputPath) and os.path.isfile(os.path.join(outputPath, src)):
        os.chdir(outputPath)
    
    elif os.path.exists(modPath) and os.path.isfile(os.path.join(modPath, src)):
        os.chdir(modPath)
            
    else:
        text.append("ERROR: gamesettings not found")
        return

    
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
    text.append("Randomzing Levels Done.")


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
        
    if not os.path.exists(outputPath):
        os.makedirs(outputPath, 0o666)
        
    os.chdir(outputPath)
        
    with open("gamesettings", "wb") as f:
        f.write(env.file.save(packer = (64,2)))
    text.append("Levels Saved.")

    os.chdir(cwd)