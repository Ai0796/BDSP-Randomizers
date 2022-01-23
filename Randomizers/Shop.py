#py -m pip install UnityPy
import UnityPy
import random
from PyQt5.QtWidgets import QTextEdit
import os
from pathlib import Path
from Resources.paths.filenames import filenames
from Resources.paths.loadUnityPath import loadUnityPath
from Resources.paths.paths import paths

#PathIDs inside Unity
#DO NOT CHANGE UNLESS GAME IS UPDATED
from Resources.pathIDs.masterdatas_pathIDs import masterdatas

shopTable = masterdatas.ShopTable.value
pathList = [shopTable]

modBasePath = paths.modPath.value
yuzuModPath = paths.masterdatas.value
modPath = os.path.join(modBasePath, yuzuModPath)
outputModPath = paths.emulatorPath.value

src = filenames.masterdatas.value

def uselessItemRemover(itemNo):
    if itemNo > 428: # Explorer Kit onwards
        return True
    elif itemNo in [0, 1, 5, 70, 71]: # None, Master Ball, Safari Ball, Life Orb, Power Orb
        return True
    elif itemNo >= 65 and itemNo <= 69: # Blue Flute to White Flute
        return True
    elif itemNo >= 95 and itemNo <= 98: # Growth Mulch to Gooey Mulch
        return True
    elif itemNo >= 112 and itemNo <= 134: # Griseous Orb to Sweet Heart
        return True
    elif itemNo >= 137 and itemNo <= 148: # Greet Mail to Bridge Mail M
        return True
    elif itemNo == 155: # Oran Berry
        return True
    elif itemNo >= 159 and itemNo <= 212: # Figy Berry to Rowap Berry
        return True
    elif itemNo == 216: # Exp. Share
        return True
    elif itemNo == 236: # Light Ball
        return True
    elif itemNo >= 256 and itemNo <= 264: # Lucky Punch to Yellow Scarf
        return True
    else:
        return False

def generateRandom(amount):
    randomList = []
    lowRange = 1
    highRange = 327
    
    for i in range(amount - 1):
        itemNo = random.randrange(lowRange, highRange)
        ##while item is useless generate a different item
        while uselessItemRemover(itemNo) or itemNo in randomList:
            itemNo = random.randrange(lowRange, highRange)
            
        randomList.append(itemNo)
        
    return randomList
    
def RandomizeShops(text, romFSPath):


    # Checks if romfs path already exist
    
    cwd = os.getcwd()
    
    outputPath = os.path.join(cwd, outputModPath, modPath)
    romFSPath = os.path.join(romFSPath, yuzuModPath)
    
    env = loadUnityPath(romFSPath, outputPath, src, text)
    
    shopList = ["FS", "FixedShop"]
    
    text.append("Items Shop Loaded.")

    for obj in env.objects:
        if obj.path_id in pathList:
            
            print("Found {}".format(src))
            
            tree = obj.read_typetree()
            if tree['m_Name'] == "ShopTable":
                for shop in shopList:
                    itemList = generateRandom(len(tree[shop]))
                    i = 0
                    for item in tree[shop]:
                        item["ItemNo"] = itemList[i]
                        i += 1
            else:
                print("Error use different path_id")        
            
            obj.save_typetree(tree)
            
            
    text.append("Items Shop Randomized.")                
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
        
    with open(src, "wb") as f:
        f.write(env.file.save(packer = (64,2)))
    text.append("Item shop Saved.")
    
    os.chdir(cwd)
