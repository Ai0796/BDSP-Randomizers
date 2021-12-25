import UnityPy
import random
from PyQt5.QtWidgets import QTextEdit
import os
from pathlib import Path

#PathIDs inside Unity
#DO NOT CHANGE UNLESS GAME IS UPDATED
evolveTable = 5139195221601552760
pathList = [evolveTable]

modPath = "romfs/Data/StreamingAssets/AssetAssistant/Pml"
yuzuModPath = "StreamingAssets/AssetAssistant/Pml"

# make sure the file personal_masterdatas is in this folder
# personal_masterdatas is inside Pml
def RandomizeEvolutions(text, romFSPath):

    # Checks if romfs path already exist
    cwd = os.getcwd()
    # text.append(cwd)
    src = "personal_masterdatas"

    outputPath = os.path.join(cwd, "mods", modPath)

    if os.path.exists(outputPath) and os.path.isfile(os.path.join(outputPath, src)):
        os.chdir(outputPath)
        env = UnityPy.load(os.path.join(outputPath, src))
        
    elif os.path.exists(os.path.join(romFSPath, yuzuModPath)) and os.path.isfile(os.path.join(romFSPath, yuzuModPath, src)):
        os.chdir(romFSPath)
        env = UnityPy.load(os.path.join(romFSPath, yuzuModPath, src))
        
    else:
        text.append("ERROR: personal_masterdatas not found ")
        return

    text.append("Evolutions Loaded.")

    ##One to one
    r = random.sample(range(1,494), 493)

    i = 0

    for obj in env.objects:
        
        # if obj.path_id in pathList:
            tree = obj.read_typetree()
            
            if tree['m_Name'] == "EvolveTable":
                for monID in tree['Evolve']:
                    monID["ar"] = [4, 0, r[i], 0, 1]
                    i += 1
                    # UGLY FIX ASAP - Copycat
                    if i == 493:
                        break
                #Saves the object tree
                obj.save_typetree(tree)
            else:
                print("Error use different path_id")

    text.append("Evolutions Randomized.")
    # saving an edited file
    # apply modifications to the objects
    # don't forget to use data.save()
        # ...
        # 
        # 
    #This output is compressed, thanks to Copycat#8110
        
    if not os.path.exists(outputPath):
        os.makedirs(outputPath, 0o666)
        
    os.chdir(outputPath)
    
    with open("personal_masterdatas", "wb") as f:
        f.write(env.file.save(packer = (64,2)))
    text.append("Evolutions Saved.")
    
    os.chdir(cwd)
