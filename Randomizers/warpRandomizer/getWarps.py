from tokenize import String
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

def getWarps(romFSPath: String):
    # make sure masterdatas is in same folder
    cwd = os.getcwd()
    
    text = []
    
    src = "masterdatas"
    
    # outputPath = os.path.join(cwd, "mods", modPath)
    outputPath = cwd

    if os.path.exists(outputPath) and os.path.isfile(os.path.join(outputPath, src)):
        os.chdir(outputPath)
        env = UnityPy.load(os.path.join(outputPath, src))
        
    elif os.path.exists(os.path.join(romFSPath, yuzuModPath)) and os.path.isfile(os.path.join(romFSPath, yuzuModPath, src)):
        os.chdir(romFSPath)
        env = UnityPy.load(os.path.join(romFSPath, yuzuModPath, src))
        
    else:
        text.append("ERROR: masterdatas not found ")
        return

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
                    # warpEdge = WarpEdge(warp["WarpZone"], warp["WarpIndex"])
                    warp["WarpZone"] = 502
                    warp["WarpIndex"] = 0
                #     if warp["ExitLabel"] != 999:
                #         print(name, WarpNode(warpList, name, obj.path_id).getZoneID(), warp["WarpZone"], warp["ScriptLabel"], warp["ExitLabel"])
                #     warpList.append(warpEdge)
                    
                # warpNode = WarpNode(warpList, name, obj.path_id)
                # if checkZoneIDs(warpNode):
                #     graph.addNode(warpNode)
                obj.save_typetree(tree)
                # if len(warpList) > 1 and name[0] == "A": 
                #     print(warpNode.getZoneID())
                
    os.chdir(cwd)
    print(cwd)
    
    with open("masterdatas_new", "wb") as f:
        f.write(env.file.save(packer=(64, 2)))
                
    return graph
                
               
if __name__ == "__main__": 
    romFSPath = "D:\\Users\\moald\\OneDrive\\Projects\\BDSP-Randomizers"
    dic = getWarps(romFSPath)