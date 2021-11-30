import UnityPy
import random
from PyQt5.QtWidgets import QTextEdit
import os
from pathlib import Path
#PathIDs inside Unity
#DO NOT CHANGE UNLESS GAME IS UPDATED
UgEncount_02 = 2921998521783056987
UgEncount_03 = 3120829428501700040
UgEncount_04 = 8994974075820978024
UgEncount_05 = 554439615776598099
UgEncount_06 = 1749855953384930022
UgEncount_07 = -233820855963829723
UgEncount_08 = -8064315274480865434
UgEncount_09 = 6067500095907821527
UgEncount_10 = -6533677965289877687
UgEncount_11 = -117713607888148647
UgEncount_12 = -4148679105701947902
#UgEncount_20 just seems like the digletts and dugtrios that can be found in the underground
pathList = [UgEncount_02, UgEncount_03, UgEncount_04, UgEncount_05, UgEncount_06, UgEncount_07, UgEncount_08, UgEncount_09, UgEncount_10, UgEncount_11, UgEncount_12]
modPath = "romfs/Data/StreamingAssets/AssetAssistant/UnderGround/data"
yuzuModPath = "StreamingAssets/AssetAssistant/UnderGround/data"
# make sure the file UgData is in this folder
# UgData s is inside UnderGround/Data
def RandomizeUG(text, romFSPath):

    src = "UgData"
    
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
        text.append("ERROR: UGData not found ")
        return
    
    text.append("UGData Loaded.")

    for obj in env.objects:
        
        if obj.path_id in pathList:
                # save decoded data
            tree = obj.read_typetree()
            
            # print(str(i) + ": " + str(data))
            if tree["m_Name"][:10] == "UgEncount_":
                for mon in tree["table"]:
                    mon["monsno"] = random.randint(1, 493)
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

    with open("UgData", "wb") as f:
        f.write(env.file.save(packer = (64,2)))
    text.append("UGData Randomized. in " + os.path.join("mods", modPath))

    os.chdir(cwd)
