

import UnityPy
import random
from PyQt5.QtWidgets import QTextEdit
import os
from pathlib import Path
from WarpNode import WarpNode
from getWarps import getWarps


modPath = "romfs/Data/StreamingAssets/AssetAssistant/Dpr"
yuzuModPath = "StreamingAssets/AssetAssistant/Dpr"


##Goal, Make sure every map in the game can be reached (except Wayward Cave)
##Make sure the game can be completeable in order (gyms 1-8, e4 1-4, champion)

def show_graph_with_labels(adjacency_matrix, mylabels):
    rows, cols = np.where(adjacency_matrix == 1)
    edges = zip(rows.tolist(), cols.tolist())
    gr = nx.Graph()
    gr.add_edges_from(edges)
    nx.draw(gr, node_size=500, labels=mylabels, with_labels=True)
    plt.show()
    
def getUniqueNodes(nodeList, num):
    return random.sample(nodeList, num)

def randomizeWarps(romFSPath):
    # make sure masterdatas is in same folder
    cwd = os.getcwd()
    
    text = []
    
    src = "masterdatas"
    
    warps = getWarps(romFSPath)
    
    warpsRandom = random.sample(warps, len(warps))
    
    outputPath = os.path.join(cwd, "mods", modPath)

    # if os.path.exists(outputPath) and os.path.isfile(os.path.join(outputPath, src)):
    #     os.chdir(outputPath)
    #     env = UnityPy.load(os.path.join(outputPath, src))
        
    # elif os.path.exists(os.path.join(romFSPath, yuzuModPath)) and os.path.isfile(os.path.join(romFSPath, yuzuModPath, src)):
    #     os.chdir(romFSPath)
    #     env = UnityPy.load(os.path.join(romFSPath, yuzuModPath, src))
        
    # else:
    #     text.append("ERROR: masterdatas not found ")
    #     return
    
    text.append("Trainers Loaded.")
    
    print(os.getcwd())
    i = 0
    
    warpPool = warps.getWarpPool()
    returnWarpPool = warps.getReturnWarpPool()
    
    for i in range(2000):
        singleNodes = 4
        while singleNodes > 2: ##Two needs need to be at least multiple node based
            startNodes = getUniqueNodes(warpPool, 2)
            endNodes = []
            for node in startNodes:
                endNodes.append(node.getRandomWarp())
            
        
    
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
    
    if not os.path.exists(outputPath):
        os.makedirs(outputPath, 0o666)
        
    os.chdir(outputPath)
    
    print(outputPath)
    
    with open("masterdatas", "wb") as f:
        f.write(env.file.save(packer = (64,2)))
    
    os.chdir(cwd)
                
                
romFSPath = "C:/Users/moald/AppData/Roaming/yuzu/dump/0100000011D90000/romfs"
randomizeWarps(romFSPath)