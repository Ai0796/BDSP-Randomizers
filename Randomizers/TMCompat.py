import UnityPy
import random
from PyQt5.QtWidgets import QTextEdit
import os
from pathlib import Path

#PathIDs inside Unity
#DO NOT CHANGE UNLESS GAME IS UPDATED
personalTable = 6925071152922426992
pathList = [personalTable]

modPath = "romfs/Data/StreamingAssets/AssetAssistant/Pml"
yuzuModPath = "StreamingAssets/AssetAssistant/Pml"

'''
TM Compatibility is broken into 3 32 bit integers and one 4 bit integer to cover all 100 TMs
'''

#Chance that a TM will be compatible, set to .5 as default
chance = .5

def generateInt(bitAmount):
    bitString = ""
    for TM in range(bitAmount):
        if random.random() < chance:
            bitString += "1"
        else:
            bitString += "0"
    return int(bitString, 2)
    

# make sure the file personal_masterdatas is in this folder
# personal_masterdatas is inside Pml
def RandomizeCompat(text, romFSPath):

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

    text.append("TM Compatibility Loaded.")

    for obj in env.objects:
        
        # if obj.path_id in pathList:
            tree = obj.read_typetree()
            
            if tree['m_Name'] == "PersonalTable":
                for monID in tree['Personal'][1:]: ##There's dummy data for the 0th pokemon, probably for indexing reasons
                    ##I don't know how else you would do this so this is just gonna be hardcoded
                    monID["machine1"] = generateInt(32)
                    monID["machine2"] = generateInt(32)
                    monID["machine3"] = generateInt(32)
                    monID["machine4"] = generateInt(4) ##Last one is only 4 to max out at 100
                    
                #Saves the object tree
                obj.save_typetree(tree)
            else:
                print("Error use different path_id")

    text.append("TM Compatibility Randomized.")
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
    text.append("TM Compatibility Saved.")
    
    os.chdir(cwd)
