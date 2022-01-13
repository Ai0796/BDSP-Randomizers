import UnityPy
import random
from PyQt5.QtWidgets import QTextEdit
import os
from pathlib import Path

##PathID Enum
from Resources.pathIDs.ugdata_pathIDs import ugdata
#PathIDs inside Unity
#DO NOT CHANGE UNLESS GAME IS UPDATED
UgEncount_02 = ugdata.UgEncount_02
UgEncount_03 = ugdata.UgEncount_03
UgEncount_04 = ugdata.UgEncount_04
UgEncount_05 = ugdata.UgEncount_05
UgEncount_06 = ugdata.UgEncount_06
UgEncount_07 = ugdata.UgEncount_07
UgEncount_08 = ugdata.UgEncount_08
UgEncount_09 = ugdata.UgEncount_09
UgEncount_10 = ugdata.UgEncount_10
UgEncount_11 = ugdata.UgEncount_11
UgEncount_12 = ugdata.UgEncount_12
UgSpecialPokemon = ugdata.UgSpecialPokemon
#UgEncount_20 just seems like the digletts and dugtrios that can be found in the underground
pathList = [UgEncount_02, UgEncount_03, UgEncount_04, UgEncount_05, UgEncount_06, UgEncount_07, UgEncount_08, UgEncount_09, UgEncount_10, UgEncount_11, UgEncount_12]
modPath = "romfs/Data/StreamingAssets/AssetAssistant/UnderGround/data"
yuzuModPath = "StreamingAssets/AssetAssistant/UnderGround/data"

src = "ugdata"
# make sure the file UgData is in this folder
# UgData is inside UnderGround/Data

def generateSample(min, max, size):
    return random.sample(range(min, max + 1), size)

def RandomizeUG(text, romFSPath):
    
    # legendaryList = [144, 145, 146, 150, 151, 243, 244, 245, 249, 250, 251, 377, 378, 379, 380, 381, 382, 383, 384, 385, 386, 480, 481, 482, 483, 484, 485, 486, 487, 488, 489, 490, 491, 492, 493]

    cwd = os.getcwd()
    
    outputPath = os.path.join(cwd, "mods", modPath)
    
    if os.path.exists(outputPath) and os.path.isfile(os.path.join(outputPath, src)):
        os.chdir(outputPath)
        env = UnityPy.load(os.path.join(outputPath, src))
        
    elif os.path.exists(os.path.join(romFSPath, yuzuModPath)) and os.path.isfile(os.path.join(romFSPath, yuzuModPath, src)):
        os.chdir(romFSPath)
        env = UnityPy.load(os.path.join(romFSPath, yuzuModPath, src))
        
    else:
        text.append("ERROR: ugdata not found ")
        return
    
    text.append("ugdata Loaded.")

    for obj in env.objects:
        
        if obj.path_id in pathList:
            # save decoded data
            tree = obj.read_typetree()
            
            # print(str(i) + ": " + str(data))
            if tree["m_Name"][:10] == "UgEncount_":
                tableLength = len(tree["table"])
                sample = generateSample(1, 493, tableLength)
                i = 0
                for mon in tree["table"]:
                    mon["monsno"] = sample[i]
                    i += 1
            
            elif tree["m_Name"] == "UgSpecialPokemon":
                tableLength = len(tree["Sheet1"])
                sample = generateSample(1, 493, tableLength)
                i = 0
                
                for mon in tree["Sheet1"]:
                    mon["monsno"] = sample[i]
            
            else:
                print("Error use different path_id")
                    
            obj.save_typetree(tree)
                    
    # text.append("UGData Randomized.")                
    # saving an edited file
    # apply modifications to the objects
    # don't forget to use data.save()
        # ...
        # 
        # 
    if not os.path.exists(outputPath):
        os.makedirs(outputPath, 0o666)
        
    os.chdir(outputPath)

    with open("ugdata", "wb") as f:
        f.write(env.file.save(packer = (64,2)))
    text.append("UGData Randomized. in " + os.path.join("mods", modPath))

    os.chdir(cwd)
