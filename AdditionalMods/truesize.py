import UnityPy
import random
from PyQt5.QtWidgets import QTextEdit
import os
from pathlib import Path
from Resources.paths.filenames import filenames
from Resources.paths.loadUnityPath import loadUnityPath
from Resources.paths.paths import paths
from Resources.pathIDs.masterdatas_pathIDs import masterdatas

#PathIDs inside Unity
#DO NOT CHANGE UNLESS GAME IS UPDATED
modBasePath = paths.modPath.value
yuzuModPath = paths.masterdatas.value
modPath = os.path.join(modBasePath, yuzuModPath)
outputModPath = paths.emulatorPath.value

src = filenames.masterdatas.value

PokemonInfo = masterdatas.PokemonInfo.value

pathList = [PokemonInfo]

def truesize(text, romFSPath):
    # make sure masterdatas is in same folder
    cwd = os.getcwd()

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
                    
                    dic["BattleScale"] = 1.0
                    dic["ContestScale"] = 1.0
                    dic["ContestSize"] = 1
                    dic["FieldScale"] = 1.0
                    dic["FieldChikaScale"] = 1.0
                    # dic["StatueScale"] = 1.0
                    dic["FieldWalkingScale"] = 1.0
                    dic["FieldFureaiScale"] = 1.0     
                                              
                obj.save_typetree(tree)
                
            else:
                print("Error use different path_id")
                
                
    text.append("True Size Added.")                
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
    
    with open(src, "wb") as f:
        f.write(env.file.save(packer = (64,2)))
    text.append("True Size Saved.")
    
    os.chdir(cwd)