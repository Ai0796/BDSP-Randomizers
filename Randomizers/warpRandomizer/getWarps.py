import UnityPy
import random
from PyQt5.QtWidgets import QTextEdit
import os
from pathlib import Path
from WarpNode import WarpNode


#PathIDs inside Unity
#DO NOT CHANGE UNLESS GAME IS UPDATED

modPath = "romfs/Data/StreamingAssets/AssetAssistant/Dpr"
yuzuModPath = "StreamingAssets/AssetAssistant/Dpr"


def getWarps(romFSPath):
    # make sure masterdatas is in same folder
    cwd = os.getcwd()
    
    text = []
    
    src = "masterdatas"
    
    outputPath = os.path.join(cwd, "mods", modPath)

    if os.path.exists(outputPath) and os.path.isfile(os.path.join(outputPath, src)):
        os.chdir(outputPath)
        env = UnityPy.load(os.path.join(outputPath, src))
        
    elif os.path.exists(os.path.join(romFSPath, yuzuModPath)) and os.path.isfile(os.path.join(romFSPath, yuzuModPath, src)):
        os.chdir(romFSPath)
        env = UnityPy.load(os.path.join(romFSPath, yuzuModPath, src))
        
    else:
        text.append("ERROR: masterdatas not found ")
        return

    extract_dir = "Walker"
    text.append("Trainers Loaded.")
    
    print(os.getcwd())
    
    warpList = []
    
    for obj in env.objects:
        if obj.type.name == "MonoBehaviour":
            tree = obj.read_typetree()

            #TrainerPoke
            if tree['m_Name'][:7] == "MapWarp":
                for warp in tree['Data']:
                    warpNode = WarpNode(warp["WarpZone"], warp["WarpIndex"])
                    warpList.append(warpNode)
                
                
    return warpList
                
                
romFSPath = "C:/Users/moald/AppData/Roaming/yuzu/dump/0100000011D90000/romfs"
getWarps(romFSPath)