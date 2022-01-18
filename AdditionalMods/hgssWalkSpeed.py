from inspect import getblock
import os
import random
from pathlib import Path

import UnityPy
from PyQt5.QtWidgets import QTextEdit
from Resources.pathIDs.masterdatas_pathIDs import masterdatas
from Resources.paths.filenames import filenames
from Resources.paths.loadUnityPath import loadUnityPath
from Resources.paths.paths import paths

#PathIDs inside Unity
#DO NOT CHANGE UNLESS GAME IS UPDATED
modBasePath = paths.modPath.value
yuzuModPath = paths.masterdatas.value
modPath = os.path.join(modBasePath, yuzuModPath)
outputModPath = paths.emulatorPath.value

src = filenames.masterdatas.value

PokemonInfo = masterdatas.PokemonInfo.value

pathList = [PokemonInfo]

def getBodySize():
    bodySizeList = []
    path = "Resources/pokeBodySize.txt"
    with open(path, "r", encoding="utf8") as f:
        for line in f.read().splitlines():
            line = line.split(",")
            bodySizeList.append(float(line[1]))
            
    return bodySizeList

def getRunSpeed5():
    runSpeedList = []
    path = "Resources/runSpeed5.txt"
    with open(path, "r", encoding="utf8") as f:
        for line in f.read().splitlines():
            runSpeedList.append(int(line))
            
    return runSpeedList

def HGSSfollowing(text, romFSPath):
    # make sure masterdatas is in same folder
    cwd = os.getcwd()
    
    bodySizeList = getBodySize()
    runSpeedList = getRunSpeed5()

    outputPath = os.path.join(cwd, outputModPath, modPath)
    romFSPath = os.path.join(romFSPath, yuzuModPath)
    
    env = loadUnityPath(romFSPath, outputPath, src, text)
    
    for obj in env.objects:
        if obj.path_id in pathList:
            tree = obj.read_typetree()
            
            print("Found {}".format(src))

            #TrainerPoke
            if tree['m_Name'] == "PokemonInfo":
                for dic in tree['Catalog']:
                    
                    dic["WalkSpeed"] = 1.7
                    dic["RunSpeed"] = 3.1
                    dic["WalkStart"] = 0.1
                    dic["RunStart"] = 0.6
                    if dic["Waitmoving"] == 1:
                        dic["Waitmoving"] = 0
                    monsno = int(dic["MonsNo"])
                    dic["BodySize"] = bodySizeList[monsno]
                    if monsno in runSpeedList:
                        dic["RunSpeed"] = 5.0
                        
                    if monsno == 384: ##Really special case for Rayquaza
                        dic["MoveType"] = 2
                                              
                obj.save_typetree(tree)
                
            else:
                
                print("Error use different path_id")
                
                
    text.append("HG/SS Following Added.")                
    # saving an edited file
    # apply modifications to the objects
    # don't forget to use data.save()
        # ...
        # 
        # 
    #This output is compressed, thanks to Copycat#8110        
    # outputPath = os.path.join(cwd, "mods", modPath)
    
    if not os.path.exists(outputPath):
        os.makedirs(outputPath, 0o666)
        
    os.chdir(outputPath)
    
    with open("masterdatas", "wb") as f:
        f.write(env.file.save(packer = (64,2)))
    text.append("True Size Saved.")
    
    os.chdir(cwd)
