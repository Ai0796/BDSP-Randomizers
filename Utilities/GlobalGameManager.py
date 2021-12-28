#py -m pip install UnityPy
import UnityPy
import random
from PyQt5.QtWidgets import QTextEdit
import struct
import os
from pathlib import Path

#PathIDs inside Unity
#DO NOT CHANGE UNLESS GAME IS UPDATED
timeManager = 8
qualityManager = 12

modPath = "romfs/Data"
yuzuModPath = ""

pathList = [timeManager, qualityManager]

def ApplyUtilities(VSync, timeStep, text, romFSPath):
    
    cwd = os.getcwd()
    src = "globalgamemanagers"
    
    outputPath = os.path.join(cwd, "mods", modPath)

    if os.path.exists(outputPath) and os.path.isfile(os.path.join(outputPath, src)):
        os.chdir(outputPath)
        env = UnityPy.load(os.path.join(outputPath, src))
    elif os.path.exists(os.path.join(romFSPath, yuzuModPath)) and os.path.isfile(os.path.join(romFSPath, yuzuModPath, src)):
        os.chdir(romFSPath)
        env = UnityPy.load(os.path.join(romFSPath, yuzuModPath, src))
    else:
        text.append("ERROR: GlobalGameManagers not found ")
        return
        
    text.append("GlobalGameManagers Loaded.")
    ChangeSettings(VSync, timeStep, env, text)
    # saving an edited file
    # apply modifications to the objects
    # don't forget to use data.save()
        # ...
        # 
        # 
    #This output is uncompressed, make sure to compress using LZ4 in UABEA
    if not os.path.exists(outputPath):
        os.makedirs(outputPath, 0o666)
        
    os.chdir(outputPath)
        
    with open("globalgamemanagers", "wb") as f:
        f.write(env.file.save())
    text.append("GlobalGameManagers Saved.")

    os.chdir(cwd)
 
#Have to move this outside of the function because im calling it from another file -- Sangawku
# Legends = 1 will keep legendariy encounters legendary, i.e. Palkia will become Mewtwo or something, not wurmple
def ChangeSettings(VSync, timeStep, env, text):
    text.append("Applying Utilities.")
    #have to assign these locally. 
    fixed_timestep = 0.0333333
    maximum_allowed_timestep = 0.05
    m_timescale = 1.0
    maximum_particle_timestep = 0.0333333
    
    for obj in env.objects:
        
        if obj.path_id in pathList:
            
            if timeStep != 1.0 and obj.type.name == "TimeManager":
                text.append("Timestep Enabled.")
                tree = obj.get_raw_data()
                fixed_timestep = fixed_timestep / timeStep
                m_timescale = m_timescale * timeStep
                maximum_particle_timestep = maximum_particle_timestep / timeStep
                tree = struct.pack('4f', fixed_timestep, maximum_allowed_timestep, m_timescale, maximum_particle_timestep)
                #Saves the object tree
                obj.set_raw_data(tree)
                
            elif VSync and obj.type.name == "QualitySettings":
                text.append("60FPS Mod Enabled.")
                tree = obj.get_raw_data()
                # print(obj.read())
                tree2 = bytearray(tree)
                tree2[0x58] = 1
                finaltree = bytes(tree2)
                #Saves the object tree
                obj.set_raw_data(finaltree)
        else:
            obj.set_raw_data(obj.get_raw_data())

    text.append("Utilities Applied.")        
