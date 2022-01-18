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
from Resources.pathIDs.personal_masterdatas_pathIDs import personal_masterdatas

personalTable = personal_masterdatas.PersonalTable.value
pathList = [personalTable]

modBasePath = paths.modPath.value
yuzuModPath = paths.personal_masterdatas.value
modPath = os.path.join(modBasePath, yuzuModPath)
outputModPath = paths.emulatorPath.value

src = filenames.personal_masterdatas.value

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

    outputPath = os.path.join(cwd, outputModPath, modPath)
    romFSPath = os.path.join(romFSPath, yuzuModPath)
    
    env = loadUnityPath(romFSPath, outputPath, src, text)

    text.append("TM Compatibility Loaded.")

    for obj in env.objects:
        
        if obj.path_id in pathList:
            tree = obj.read_typetree()
            
            print("Found {}".format(src))
            
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
