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
modPath = "romfs/StreamingAssets/AssetAssistant/UnderGround/data"
# make sure the file UgData is in this folder
# UgData s is inside UnderGround/Data
def RandomizeUG(text):

    filename = "UgData"
    text.append("UGData Loaded.")

    # legendaryList = [144, 145, 146, 150, 151, 243, 244, 245, 249, 250, 251, 377, 378, 379, 380, 381, 382, 383, 384, 385, 386, 480, 481, 482, 483, 484, 485, 486, 487, 488, 489, 490, 491, 492, 493]

    cwd = os.getcwd()
    if os.path.exists(modPath) == True:
        if os.path.isfile(modPath + '/UgData') == True:
            os.chdir(modPath)

    env = UnityPy.load(filename)
    
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
                    
    text.append("UGData Randomized.")                
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

    with open("UgData", "wb") as f:
        f.write(env.file.save(packer = (64,2)))
    text.append("UGData Randomized.")

    os.chdir(cwd)
