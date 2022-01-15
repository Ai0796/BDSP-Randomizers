import UnityPy
import random
from PyQt5.QtWidgets import QTextEdit
import os
from pathlib import Path

#PathIDs inside Unity
#DO NOT CHANGE UNLESS GAME IS UPDATED
from Resources.pathIDs.personal_masterdatas_pathIDs import personal_masterdatas

personalTable = personal_masterdatas.PersonalTable.value
pathList = [personalTable]

modPath = "romfs/Data/StreamingAssets/AssetAssistant/Pml"
yuzuModPath = "StreamingAssets/AssetAssistant/Pml"

'''
Broken Abilities
Wonder Guard 25
Disguise 209
Stance Change 176
Battle Bond 210
Power Construct 211
RKS System 225
Gulp Missile 241
Ice Face 248
Hunger Switch 258
As One (1) 266
As One (2) 267
'''

brokenAbilities = [25, 209, 176, 210, 211, 225, 241, 248, 258, 266, 267]

def verifyAbilities(ability):
    return ability in brokenAbilities

def getAbilities():
    min = 1
    max = 268
    abilityList = random.sample(range(min, max), 3)
    for i in range(len(abilityList)):
        while verifyAbilities(abilityList[i]):
            abilityList[i] = random.randrange(min, max)
            
    return abilityList


# make sure the file personal_masterdatas is in this folder
# personal_masterdatas is inside Pml
def RandomizeAbilities(text, romFSPath):

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

    text.append("Abilities Loaded.")

    for obj in env.objects:
        
        if obj.path_id in pathList:
            
            print("Found {}".format(src))
            
            tree = obj.read_typetree()
            
            if tree['m_Name'] == "PersonalTable":
                for monID in tree['Personal'][1:]: ##There's dummy data for the 0th pokemon, probably for indexing reasons
                    abilities  = getAbilities()
                    for i in range(len(abilities)):
                        monID["tokusei"f"{i + 1}"] = abilities[i]
                    
                #Saves the object tree
                obj.save_typetree(tree)
            else:
                print("Error use different path_id")

    text.append("Abilities Randomized.")
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
    text.append("Abilities Saved.")
    
    os.chdir(cwd)
