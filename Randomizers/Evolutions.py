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

evolveTable = personal_masterdatas.EvolveTable.value
pathList = [evolveTable]

modBasePath = paths.modPath.value
yuzuModPath = paths.personal_masterdatas.value
modPath = os.path.join(modBasePath, yuzuModPath)

src = filenames.personal_masterdatas.value

# make sure the file personal_masterdatas is in this folder
# personal_masterdatas is inside Pml
def RandomizeEvolutions(text, romFSPath):

    # Checks if romfs path already exist
    cwd = os.getcwd()

    outputPath = os.path.join(cwd, "mods", modPath)
    romFSPath = os.path.join(romFSPath, yuzuModPath)
    
    env = loadUnityPath(romFSPath, outputPath, src, text)

    ##One to one
    r = random.sample(range(1,494), 493)

    i = 0

    for obj in env.objects:
        
        if obj.path_id in pathList:
            
            print("Found {}".format(src))
            
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
