#py -m pip install UnityPy
import UnityPy
import random
from PyQt5.QtWidgets import QTextEdit
import struct

#PathIDs inside Unity
#DO NOT CHANGE UNLESS GAME IS UPDATED
timeManager = 8
qualityManager = 12



pathList = [timeManager, qualityManager]

def ApplyUtilities(VSync, timeStep, text):
    src = "globalgamemanagers"
    env = UnityPy.load(src)  
    text.append("GlobalGameManagers Loaded.")
    ChangeSettings(VSync, timeStep, env, text)
    # saving an edited file
    # apply modifications to the objects
    # don't forget to use data.save()
        # ...
        # 
        # 
    #This output is uncompressed, make sure to compress using LZ4 in UABEA
    with open("globalgamemanagers", "wb") as f:
        f.write(env.file.save())
    text.append("GlobalGameManagers Saved.")
 
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
            if timeStep != 1.0 and obj.path_id == 8:
                text.append("Timestep Enabled.")
                tree = obj.get_raw_data()
                fixed_timestep = fixed_timestep / timeStep
                m_timescale = m_timescale * timeStep
                maximum_particle_timestep = maximum_particle_timestep / timeStep
                tree = struct.pack('4f', fixed_timestep, maximum_allowed_timestep, m_timescale, maximum_particle_timestep)
                #Saves the object tree
                obj.set_raw_data(tree)
            elif VSync and obj.path_id == 12:
                text.append("60FPS Mod Enabled.")
                tree = obj.get_raw_data()
                tree2 = bytearray(tree)
                tree2[0x58] = 0
                finaltree = bytes(tree2)
                #Saves the object tree
                obj.set_raw_data(finaltree)
        else:
            obj.set_raw_data(obj.get_raw_data())

    text.append("Utilities Applied.")        