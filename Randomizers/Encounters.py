#py -m pip install UnityPy
import UnityPy
import random
import os
from pathlib import Path
from PyQt5.QtWidgets import QTextEdit

#PathIDs inside Unity
#DO NOT CHANGE UNLESS GAME IS UPDATED
modPath = "romfs/Data/StreamingAssets/AssetAssistant/Dpr/scriptableobjects"
yuzuModPath = "StreamingAssets/AssetAssistant/Dpr/scriptableobjects"

diamondEncount = 361824127573837173
pearlEncount = -9035030829162387677

pathList = [diamondEncount, pearlEncount]
lengendaries = [144,145,146,150,151,243,244,245,249,250,251,377,378,379,380,381,382,383,384,385,386,480,481,482,483,484,485,486,487,488,491]
encPool = []
encLegPool = []

# make sure the file gamesettings is in this folder
# gamesettings is in Dpr/scriptableassets

# Takes a list i.e [1,2] and generates a pool of pokemon for those gens to be used in Encount()
def pool(gens):
    for i in gens:
        if i == 1:
            encPool.extend(range(1,151))
            encLegPool.extend([144,145,146,150,151])
        if i == 2:
            encPool.extend(range(151,252))
            encLegPool.extend([243,244,245,249,250,251])
        if i == 3:
            encPool.extend(range(252,387))
            encLegPool.extend([377,378,379,380,381,382,383,384,385,386])
        if i == 4:
            encPool.extend(range(387,494))
            encLegPool.extend([480,481,482,483,484,485,486,487,488,491])
        
def RandomizeEncounters(text, legends, pools, safari, romFSPath):

    # Checks if romfs path already exist
    cwd = os.getcwd()
    
    src = "gamesettings"

    outputPath = os.path.join(cwd, "mods", modPath)

    if os.path.exists(outputPath) and os.path.isfile(os.path.join(outputPath, src)):
        os.chdir(outputPath)
        env = UnityPy.load(os.path.join(outputPath, src))
    elif os.path.exists(os.path.join(romFSPath, yuzuModPath)) and os.path.isfile(os.path.join(romFSPath, yuzuModPath, src)):
        os.chdir(romFSPath)
        env = UnityPy.load(os.path.join(romFSPath, yuzuModPath, src))
    else:
        text.append("ERROR: gamesettings not found ")
        return
    
    pool(pools)
    text.append("Gamesettings Loaded.")
    Encount(safari, legends, env, text)
    # saving an edited file
    # apply modifications to the objects
    # don't forget to use data.save()
        # ...
        # 
        # 

    # If you arent in romfs path, make path and enter it
    

    #if cwd == os.getcwd():
    #    Path(modPath).mkdir(parents=True, exist_ok=True)
    #    os.chdir(modPath)
        
    if not os.path.exists(outputPath):
        os.makedirs(outputPath, 0o666)
        
    os.chdir(outputPath)

    with open("gamesettings", "wb") as f:
        f.write(env.file.save(packer = (64,2)))
    text.append("Encounters Saved.")
    # Returns to regular directory
    
    os.chdir(cwd)
     
#Have to move this outside of the function because im calling it from another file -- Sangawku
# Legends = 1 will keep legendariy encounters legendary, i.e. Palkia will become Mewtwo or something, not wurmple
def Encount(safari, legend, env, text):
    text.append("Randomizing Pokemon.")
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
                                    if legend == 1:
                                        for legsNo in lengendaries:
                                            if mon['monsNo'] == legsNo:
                                                mon['monsNo'] = random.choice(encLegPool)
                                            else:
                                                mon['monsNo'] = random.choice(encPool)
                                    else:
                                        mon['monsNo'] = random.choice(encPool)
            if safari:
                for area in tree['safari']:
                    for key in area.keys():
                        if type(area[key]) != int:
                            if type(area[key][0]) == dict:
                                for mon in area[key]:
                                    if mon['MonsNo'] != 0:
                                        mon['MonsNo'] = random.choice(encPool)
            #Saves the object tree
            obj.save_typetree(tree)
    text.append("Randomzing Done.")
