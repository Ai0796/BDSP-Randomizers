import UnityPy
import random
from PyQt5.QtWidgets import QTextEdit
import os
from pathlib import Path
from WarpNode import WarpNode
from WarpEdge import WarpEdge
import rapidjson
from WarpGraph import WarpGraph


#PathIDs inside Unity
#DO NOT CHANGE UNLESS GAME IS UPDATED

modPath = "romfs/Data/StreamingAssets/AssetAssistant/Dpr"
yuzuModPath = "StreamingAssets/AssetAssistant/Dpr"

def checkZoneIDs(warpNode):
    zoneID = warpNode.getZoneID()
    if zoneID <= 0: #Invalid
        return False
    # elif zoneID >= 264 and zoneID <= 284: ##Turnback Cave
    #     return False
    elif zoneID >= 620 and zoneID <= 623: ##Secret Bases 1
        return False
    elif zoneID >= 627 and zoneID <= 647: ##Secret Bases 2
        return False
    return True

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

    graph = WarpGraph()
    for obj in env.objects:
        if obj.type.name == "MonoBehaviour":
            tree = obj.read_typetree()

            #TrainerPoke
            if tree['m_Name'][:7] == "MapWarp":
                name = tree['m_Name'].split("_")[1]
                warpList = []
                for warp in tree['Data']:
                    warpEdge = WarpEdge(warp["WarpZone"], warp["WarpIndex"])
                    if warp["ExitLabel"] != 999:
                        print(name, WarpNode(warpList, name, obj.path_id).getZoneID(), warp["WarpZone"], warp["ScriptLabel"], warp["ExitLabel"])
                    warpList.append(warpEdge)
                    
                warpNode = WarpNode(warpList, name, obj.path_id)
                if checkZoneIDs(warpNode):
                    graph.addNode(warpNode)
                # if len(warpList) > 1 and name[0] == "A": 
                #     print(warpNode.getZoneID())
                
    os.chdir(cwd)
                
    return graph
                
               
if __name__ == "__main__": 
    romFSPath = "C:/Users/moald/AppData/Roaming/yuzu/dump/0100000011D90000/romfs"
    dic = getWarps(romFSPath)