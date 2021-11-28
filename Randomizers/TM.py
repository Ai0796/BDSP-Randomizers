#py -m pip install UnityPy
import UnityPy
import random
from PyQt5.QtWidgets import QTextEdit
import os
from pathlib import Path

#PathIDs inside Unity
#DO NOT CHANGE UNLESS GAME IS UPDATED
ItemTable = 252928009371549925
modPath = "romfs/StreamingAssets/AssetAssistant/Pml"
pathList = [ItemTable]

def getMoveList():
    
    filepath = "Resources//moveIndex.txt"
    with open(filepath, "r") as f:
        return f.readlines()
    
def RandomizeTMs(text):

    cwd = os.getcwd()
    if os.path.exists(modPath) == True:
        if os.path.isfile(modPath + '/personal_masterdatas') == True:
            os.chdir(modPath)
            
    src = "personal_masterdatas"
    
    env = UnityPy.load(src)
    extract_dir = "Walker"
    text.append("TMs loaded.")

    for obj in env.objects:
        if obj.path_id in pathList:
            tree = obj.read_typetree()
            print(tree)
            if tree['m_Name'] == "ItemTable":
                ##Selects 100 unique moves
                r = random.sample(range(getMoveList()), 100)
                i = 0
                for TM in tree["WazaMachine"]:
                    if TM["MachineNo"] <= 100 and TM["MachineNo"] > 0:
                        TM["WazaNo"] = r[i]
                        i += 1
                    ##There's 200 defined TMs for some reason so break once past 100
                    else:
                        break
                    
            obj.save_typetree(tree)
        else:
            print("Error use different path_id")
            
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

    with open("masterdatas", "wb") as f:
        f.write(env.file.save(packer = (64,2)))
    text.append("TMs Saved.")

    os.chdir(cwd)
