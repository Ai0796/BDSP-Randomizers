import UnityPy
import random
from PyQt5.QtWidgets import QTextEdit
import os
from pathlib import Path
from WarpNode import WarpNode
from WarpEdge import WarpEdge
import getWarps
import rapidjson
from WarpGraph import WarpGraph


#PathIDs inside Unity
#DO NOT CHANGE UNLESS GAME IS UPDATED

modPath = "romfs/Data/StreamingAssets/AssetAssistant/Dpr"
yuzuModPath = "StreamingAssets/AssetAssistant/Dpr"

def checkZoneIDs(warpNode):
    zoneID = warpNode.getZoneID
    if zoneID <= 0: #Invalid
        return False
    elif zoneID >= 264 and zoneID <= 284: ##Turnback Cave
        return False
    elif zoneID >= 620 and zoneID <= 623: ##Secret Bases 1
        return False
    elif zoneID >= 627 and zoneID <= 647: ##Secret Bases 2
        return False
    return True

def repackWarps(romFSPath, warpGraph : WarpGraph):
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

    text.append("Trainers Loaded.")
    
    print(os.getcwd())


    nameDic = warpGraph.getNameDic()
    nameDicKeys = list(nameDic.keys())
    for obj in env.objects:
        if obj.type.name == "MonoBehaviour":
            tree = obj.read_typetree()

            #TrainerPoke
            if tree['m_Name'][:7] == "MapWarp":
                name = tree['m_Name'].split("_")[1]
                if name in nameDicKeys:
                    warpList = nameDic[name].getWarpEdges()
                    if len(warpList) != len(tree["Data"]):
                        print("Error, length doesn't match in", name)
                    for i in range(len(tree['Data'])):
                        tree["Data"][i]["WarpZone"] = warpList[i].getWarpZone()
                        tree["Data"][i]["WarpIndex"] = warpList[i].getWarpIndex()
                        # warpList.append(warpEdge)
                        
                    # warpNode = WarpNode(warpList, name, obj.path_id)
                    # graph.addNode(warpNode)
                    # if len(warpList) > 1 and name[0] == "A": 
                    #     print(warpNode.getZoneID())
                obj.save_typetree(tree)
    os.chdir(cwd)
    
    if not os.path.exists(outputPath):
        os.makedirs(outputPath, 0o666)
        
    os.chdir(outputPath)
    
    print(outputPath)
    
    with open("masterdatas", "wb") as f:
        f.write(env.file.save(packer = (64,2)))
    
    with open(src, "wb") as f:
        f.write(env.file.save(packer=(64, 2)))
                
               
if __name__ == "__main__": 
    romFSPath = "C:/Users/moald/AppData/Roaming/yuzu/dump/0100000011D90000/romfs"
    dic = getWarps(romFSPath)