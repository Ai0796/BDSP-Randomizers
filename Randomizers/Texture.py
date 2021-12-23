##Changes the Texture of all the pokemon by a random color value
import UnityPy
import random
from PyQt5.QtWidgets import QTextEdit
import os
from pathlib import Path
import glob

#PathIDs inside Unity
#DO NOT CHANGE UNLESS GAME IS UPDATED
moveTable = 1345203096983357567
pathList = [moveTable]

modPath = "romfs/Data/StreamingAssets/AssetAssistant/Pml/Pokemon Database/pokemons/common/"
yuzuModPath = "StreamingAssets/AssetAssistant/Pml/Pokemon Database/pokemons/common/"



def randomizeTextures(text, romFSPath):
    
    
    TMList = getMoveList()
    src = "personal_masterdatas"
    
    cwd = os.getcwd()
    
    outputPath = os.path.join(cwd, "mods", modPath)
    
    if os.path.exists(os.path.join(romFSPath, yuzuModPath)):
        os.chdir(romFSPath)
        env = UnityPy.load(os.path.join(romFSPath, yuzuModPath, src))

    else:
        text.append("ERROR: Pokemon Textures not found ")
        return
    
    for filename in glob.glob(yuzuModPath):
        env = UnityPy.load(filename)
        
        for obj in env.objects:
            if obj.type.name == "Texture2D":
                # export texture
                data = obj.read()
                fp = os.path.join(extract_dir, f"{tree['m_Name']}.png")
                
                pil_img = Image.open(fp)
                data.image = pil_img
                data.save()