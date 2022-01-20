import UnityPy
import random
from PyQt5.QtWidgets import QTextEdit
import os
from pathlib import Path
from Resources.paths.filenames import filenames
from Resources.paths.loadUnityPath import loadUnityPath
from Resources.paths.paths import paths
from Resources.pathIDs.gamesettings_pathIDs import gamesettings

#PathIDs inside Unity
#DO NOT CHANGE UNLESS GAME IS UPDATED
modBasePath = paths.modPath.value
yuzuModPath = paths.gamesettings.value
modPath = os.path.join(modBasePath, yuzuModPath)
outputModPath = paths.emulatorPath.value

src = filenames.gamesettings.value

PokemonInfo = gamesettings.MapInfo.value

pathList = [PokemonInfo]

##List of weathers to remove
weather = [8, 14, 15, 16, 18, 19]

def removeWeather(text, romFSPath):
    # make sure masterdatas is in same folder
    cwd = os.getcwd()

    outputPath = os.path.join(cwd, outputModPath, modPath)
    romFSPath = os.path.join(romFSPath, yuzuModPath)
    
    env = loadUnityPath(romFSPath, outputPath, src, text)
    
    for obj in env.objects:
        if obj.path_id in pathList:
            tree = obj.read_typetree()
            
            print("Found {}".format(src))

            if tree['m_Name'] == "MapInfo":
                for zone in tree["ZoneData"]:
                    if int(zone["Weather"]) in weather:
                        zone["Weather"] = 0
                        
                    elif int(zone["Weather"]) == 7:
                        zone["Weather"] = 6
                    
                    zone["Bicycle"] = 1
                    
                obj.save_typetree(tree)
                
            else:
                print("Error use different path_id")
                
                
    text.append("Remove Fog/Bike Everywhere Added.")                
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
    text.append("Remove Fog/Bike Everywhere Saved.")
    
    os.chdir(cwd)