

import UnityPy
import random
from PyQt5.QtWidgets import QTextEdit
import os
from pathlib import Path
from WarpGraph import WarpGraph
from WarpNode import WarpNode
from getWarps import getWarps
from repackWarps import repackWarps


modPath = "romfs/Data/StreamingAssets/AssetAssistant/Dpr"
yuzuModPath = "StreamingAssets/AssetAssistant/Dpr"


##Goal, Make sure every map in the game can be reached (except Wayward Cave)
##Make sure the game can be completeable in order (gyms 1-8, e4 1-4, champion)

    
def getUniqueIndexes(List, num):
    return random.sample(range(len(List)), num)

def checkZoneIDs(warpNode):
    zoneID = warpNode.getZoneID()
    if zoneID <= 0: #Invalid
        return False
    elif zoneID >= 264 and zoneID <= 284: ##Turnback Cave
        return False
    elif zoneID >= 620 and zoneID <= 623: ##Secret Bases 1
        return False
    elif zoneID >= 627 and zoneID <= 647: ##Secret Bases 2
        return False
    return True

def randomizeWarps(romFSPath):
    # make sure masterdatas is in same folder
    cwd = os.getcwd()
    
    text = []
    
    src = "masterdatas"
    
    warps = getWarps(romFSPath)
    
    # warps.randomize()
    
    # repackWarps(romFSPath, warps)
    # warpsRandom = random.sample(warps, len(warps))
    
    # outputPath = os.path.join(cwd, "mods", modPath)
    
    # text.append("Trainers Loaded.")
    
    # print(os.getcwd())
    # i = 0
    
    warpPool = warps.getWarpPool()
    returnWarpPool = warps.getReturnWarpPool()
    zoneDic = warps.getZoneDic()
    indexDic = warps.getNodeIndexes()
    
    # print(len(warpPool))
    # print(len(returnWarpPool))
    print(zoneDic.keys())
    
    
    ##Get two random edges, swap them around
    while len(warpPool) > 4:
        warpEdgeIndexes = getUniqueIndexes(warpPool, 2)
        edgeList = []
        returnEdgeList = []
        
        warpEdgeIndexes.sort(reverse=True) ##Done so indexes get pulled from the end to not affect anything
        for index in warpEdgeIndexes:
            edgeIndex = random.randrange(0, len(warpPool[index]))
            edgeList.append(warpPool[index].pop(edgeIndex))
            
            if len(warpPool[index]) == 0:
                warpPool.pop(index)
                
        for edge in edgeList:
            returnEdge = zoneDic[str(edge[0])].getEdge(edge[1])
            returnEdgeList.append([returnEdge.getWarpZone(), returnEdge.getWarpIndex()])
        
        print(edgeList)
        print(returnEdgeList)
        returnEdgeList.reverse()
        
        
        for i in range(len(edgeList)):
            startWarp = edgeList[i]
            endWarp = returnEdgeList[i]
            
            startIndex = indexDic[str(endWarp[0])]
            startNodeIndex = endWarp[1]
            
            endIndex = indexDic[str(startWarp[0])]
            endNodeIndex = startWarp[1]
            
            print(returnWarpPool[startIndex])
            print(returnWarpPool[endIndex])
            
            returnWarpPool[startIndex][startNodeIndex] = startWarp
            returnWarpPool[endIndex][endNodeIndex] = endWarp
            
    warps.repack(returnWarpPool)
    repackWarps(romFSPath, WarpGraph)
    
    # for obj in env.objects:
    #     if obj.type.name == "MonoBehaviour":
    #         tree = obj.read_typetree()

    #         #TrainerPoke
    #         if tree['m_Name'][:7] == "MapWarp":
                
    #             for warp in tree['Data']:
                    
    #                 warp["WarpZone"] = warpsRandom[i].getWarpZone()
    #                 warp["WarpIndex"] = warpsRandom[i].getWarpIndex()
                    
    #                 i += 1
                
    #             obj.save_typetree(tree)
                     
    # saving an edited file
    # apply modifications to the objects
    # don't forget to use data.save()
        # ...
        # 
        # 
    #This output is compressed, thanks to Copycat#8110        
    # outputPath = os.path.join(cwd, "mods", modPath)
    
    # if not os.path.exists(outputPath):
    #     os.makedirs(outputPath, 0o666)
        
    # os.chdir(outputPath)
    
    # print(outputPath)
    
    # with open("masterdatas", "wb") as f:
    #     f.write(env.file.save(packer = (64,2)))
    
    # os.chdir(cwd)
                
                
romFSPath = "C:/Users/moald/AppData/Roaming/yuzu/dump/0100000011D90000/romfs"
randomizeWarps(romFSPath)