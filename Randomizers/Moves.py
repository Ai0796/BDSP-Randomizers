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

moveTable = personal_masterdatas.WazaOboeTable.value
pathList = [moveTable]

modBasePath = paths.modPath.value
yuzuModPath = paths.personal_masterdatas.value
modPath = os.path.join(modBasePath, yuzuModPath)
outputModPath = paths.emulatorPath.value

src = filenames.personal_masterdatas.value
    
def getMoveList():
    
    filepath = "Resources//moveIndex.txt"
    with open(filepath, "r") as f:
        return f.read().splitlines()
    
def saveMoveList(file):
    filepath = "Resources//tempMoveIndex.txt"
    with open(filepath, "w") as f:
        f.write(file)

# make sure the file personal_masterdatas is in this folder
# personal_masterdatas is inside Pml
def RandomizerMoves(text, romFSPath):

    # Checks if romfs path already exist
    cwd = os.getcwd()
    # text.append(cwd)

    
    moveList = getMoveList()

    outputPath = os.path.join(cwd, outputModPath, modPath)
    romFSPath = os.path.join(romFSPath, yuzuModPath)
    
    env = loadUnityPath(romFSPath, outputPath, src, text)
    
    moveString = "" ##Used in order to import new movesets into trainer pokemon

    for obj in env.objects:
        
        if obj.path_id in pathList:
            
            print("Found {}".format(src))
            
            tree = obj.read_typetree()
            
            if tree['m_Name'] == "WazaOboeTable":
                for monID in tree['WazaOboe']:
                    if len(monID["ar"]) > 0: #Checks if it's not empty
                        mon = monID["ar"]
                        moveNum = 0
                        pokeMoveList = random.sample(moveList, int(len(mon)/2)) ##Learnset is level, move. So every other index is move
                        for i in range(1, len(mon), 2):
                            mon[i] = int(pokeMoveList[moveNum])
                            moveString += str(mon[i-1]) + ", " + str(mon[i]) + ", "
                            moveNum += 1
                        moveString = moveString[:-1] + "\n" ##Removes extra comma and adds newline
                        
                #Saves the object tree
                obj.save_typetree(tree)
                
            else:
                
                print("Error use different path_id")
                
    

    text.append("Movesets Randomized.")
    # saving an edited file
    # apply modifications to the objects
    # don't forget to use data.save()
        # ...
        # 
        # 
        
    if not os.path.exists(outputPath):
        os.makedirs(outputPath, 0o666)
        
    os.chdir(outputPath)
    
    with open(src, "wb") as f:
        f.write(env.file.save(packer = (64,2)))
    text.append("Movesets Saved.")
    
    os.chdir(cwd)
    
    saveMoveList(moveString)