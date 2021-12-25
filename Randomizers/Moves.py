import UnityPy
import random
from PyQt5.QtWidgets import QTextEdit
import os
from pathlib import Path

#PathIDs inside Unity
#DO NOT CHANGE UNLESS GAME IS UPDATED
moveTable = 1345203096983357567
pathList = [moveTable]

modPath = "romfs/Data/StreamingAssets/AssetAssistant/Pml"
yuzuModPath = "StreamingAssets/AssetAssistant/Pml"

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
    src = "personal_masterdatas"
    
    moveList = getMoveList()

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

    text.append("Movesets Loaded.")
    
    moveString = "" ##Used in order to import new movesets into trainer pokemon

    for obj in env.objects:
        
        # if obj.path_id in pathList:
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
    
    with open("personal_masterdatas", "wb") as f:
        f.write(env.file.save(packer = (64,2)))
    text.append("Movesets Saved.")
    
    os.chdir(cwd)
    
    saveMoveList(moveString)