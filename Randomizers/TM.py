#py -m pip install UnityPy
import UnityPy
import random
from PyQt5.QtWidgets import QTextEdit
import os
from pathlib import Path

#PathIDs inside Unity
#DO NOT CHANGE UNLESS GAME IS UPDATED
ItemTable = 252928009371549925
modPath = "romfs/Data/StreamingAssets/AssetAssistant/Pml"
yuzuModPath = "romfs/StreamingAssets/AssetAssistant/Pml"
pathList = [ItemTable]

def getMoveList():
    
    filepath = "Resources//moveIndex.txt"
    with open(filepath, "r") as f:
        return f.read().splitlines()
    
def RandomizeTMs(text):
    
    
    TMList = getMoveList()
    src = "personal_masterdatas"
    
    cwd = os.getcwd()
    
    outputPath = os.path.join(cwd, "mods", modPath)
    
    if os.path.exists(outputPath) and os.path.isfile(os.path.join(outputPath, src)):
        os.chdir(outputPath)
        
    elif os.path.exists(modPath) and os.path.isfile(os.path.join(modPath, src)):
        os.chdir(modPath)
        
    elif os.path.exists(yuzuModPath) and os.path.isfile(os.path.join(yuzuModPath, src)):
        os.chdir(yuzuModPath)
        
    else:
        text.append("ERROR: personal_masterdatas not found ")
        return
            
    
    
    env = UnityPy.load(src)
    extract_dir = "Walker"
    text.append("TMs loaded.")

    for obj in env.objects:
        if obj.path_id in pathList:
            tree = obj.read_typetree()
            if tree['m_Name'] == "ItemTable":
                ##Selects 100 unique moves
                r = random.sample(TMList, 100)
                i = 0
                for TM in tree["WazaMachine"]:
                    if TM["machineNo"] <= 100 and TM["machineNo"] > 0:
                        TM["wazaNo"] = int(r[i])
                        i += 1
                    ##There's 200 defined TMs for some reason so break once past 100
                    else:
                        break
            else:
                print("Error use different path_id")        
            obj.save_typetree(tree)
            
            
    text.append("TMs Randomized.")                
    # saving an edited file
    # apply modifications to the objects
    # don't forget to use data.save()
        # ...
        # 
        # 
    #This output is compressed, thanks to Copycat#8110
    if cwd == os.getcwd():
        Path(modPath).mkdir(parents=True, exist_ok=True)
        os.chdir(modPath)

    if not os.path.exists(outputPath):
        os.makedirs(outputPath, 0o666)
        
    os.chdir(outputPath)
    
    with open("personal_masterdatas", "wb") as f:
        f.write(env.file.save(packer = (64,2)))
    text.append("TMs Saved.")

    os.chdir(cwd)