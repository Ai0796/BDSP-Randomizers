

import UnityPy
import random
from PyQt5.QtWidgets import QTextEdit
import os
from pathlib import Path
from WarpNode import WarpNode
from getWarps import getWarps
from repackWarps import repackWarps


modPath = "romfs/Data/StreamingAssets/AssetAssistant/Dpr"
yuzuModPath = "StreamingAssets/AssetAssistant/Dpr"


##Goal, Make sure every map in the game can be reached (except Wayward Cave)
##Make sure the game can be completeable in order (gyms 1-8, e4 1-4, champion)

    
def getUniqueNodes(nodeList, num):
    return random.sample(nodeList, num)

def randomizeWarps(romFSPath):
    # make sure masterdatas is in same folder
    cwd = os.getcwd()
    
    text = []
    
    src = "masterdatas"
    
    warps = getWarps(romFSPath)
    
    warps.randomize()
    
    repackWarps(romFSPath, warps)
    # warpsRandom = random.sample(warps, len(warps))
    
    # outputPath = os.path.join(cwd, "mods", modPath)
    
    # text.append("Trainers Loaded.")
    
    # print(os.getcwd())
    # i = 0
    
    # warpPool = warps.getWarpPool()
    # returnWarpPool = warps.getReturnWarpPool()
    
    # for i in range(2000):
    #     singleNodes = 4
    #     while singleNodes > 2: ##Two needs need to be at least multiple node based
    #         startNodes = getUniqueNodes(warpPool, 2)
    #         endNodes = []
    #         for node in startNodes:
    #             endNodes.append(node.getRandomWarp())
            
        
    
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