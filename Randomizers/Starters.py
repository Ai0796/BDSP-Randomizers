#py -m pip install UnityPy
from platform import version
import UnityPy
import random
import os
from pathlib import Path
from PyQt5.QtWidgets import QTextEdit
from keystone import *
from Randomizers.Patches.Enums.GameRevision import GameRevision
from Randomizers.Patches.Enums.GameType import GameType
from Randomizers.Patches.GameOffsets.GameOffsets import GameOffsets
from Randomizers.Patches.Patch import Patch
from Resources.paths.filenames import filenames
from Resources.paths.loadUnityPath import loadUnityPath
from Resources.paths.paths import paths

#Change hardcoded pokemon name 
#AssetAssistant/Message/English
#PathIDs inside Unity
#DO NOT CHANGE UNLESS GAME IS UPDATED
from Resources.pathIDs.english_pathIDs import english

engMsgPathID = english.english_dp_scenario1.value
pathList = [engMsgPathID]

modBasePath = paths.modPath.value
exefsModPath = paths.exefsModPath.value
yuzuModPath = paths.english.value
modPathEng = os.path.join(modBasePath, yuzuModPath)
outputModPath = paths.emulatorPath.value
modPath = os.path.join(outputModPath, exefsModPath)


src = filenames.english.value

BD = GameType.BD
SP = GameType.SP

gameVersionIDs = [x for x in GameRevision]

gameVersionNames = ["100", "110", "111", "112", "113", "120", "130"]
#8-EV_POKESELECT_02 Worddata 6(0 idx) Turtwig
#8-EV_POKESELECT_03 Worddata 6(0 idx) Chimchar
#8-EV_POKESELECT_04 Worddata 6(0 idx) Piplup
def getPokemonNames():
    
    filepath = "Resources//pokemon.txt"
    with open(filepath, "r") as f:
        return f.read().splitlines()

def getPokemonCategory():
    
    filepath = "Resources//categories.txt"
    with open(filepath, "r") as f:
        return f.read().splitlines()

def getPokemonColor():

    filepath = "Resources//color.txt"
    with open(filepath, "r") as f:
        return f.read().splitlines()

def colorPokemon(monID):
    color = "<color=#FFFFFFFF>"

    try:
        colorHex = {0 : "<color=#F01E1EFF>", # Red
                    1 : "<color=#0064FFFF>", # Blue
                    2 : "<color=#CB1003FF>", # Yellow
                    3 : "<color=#00FF00FF>", # Green
                    4 : "<color=#383431FF>", # Black
                    5 : "<color=#8E5B2CFF>", # Brown
                    6 : "<color=#CC00CCFF>", # Purple
                    7 : "<color=#669999FF>", # Gray
                    8 : "<color=#b0b0b0FF>", # White
                    9 : "<color=#FF00FFFF>" # Pink
            }

        for i in getPokemonColor():
            for j in i.split(","):
                if getPokemonNames()[monID] == j:
                    color = colorHex[getPokemonColor().index(i)]
                    
    except:
        print("UTF-8 Error, Pokemon color will be default")

    return color

def GenerateStarterPatches(gameOffsets: GameOffsets, starter1: int, starer2: int, starter3: int) -> bytearray:
    patch = Patch(shift=0x100)

    patch.addPatch(gameOffsets.starterGrassOffset, f'mov w0, #{hex(starter1)}')
    patch.addPatch(gameOffsets.starterFireOffset, f'mov w8, #{hex(starer2)}')
    patch.addPatch(gameOffsets.starterWaterOffset, f'mov w9, #{hex(starter3)}')

    patch.addPatch(gameOffsets.rivalGrassOffset, f'mov w0, #{hex(starer2)}')
    patch.addPatch(gameOffsets.rivalFireOffset, f'mov w8, #{hex(starter3)}')
    patch.addPatch(gameOffsets.rivalWaterOffset, f'mov w8, #{hex(starter1)}')
    return patch.generateIPS32Patch()

def RandomizeStarters(text, romFSPath):
    cwd = os.getcwd()
    pokeNames = getPokemonNames()
    pokeCateg = getPokemonCategory()

    text.append("Randomizing Starters!")
    
    mon1 = random.randint(1, 493)
    mon2 = random.randint(1, 493)
    mon3 = random.randint(1, 493)
    
    colorPokemonmon1 = colorPokemon(mon1)
    colorPokemonmon2 = colorPokemon(mon2)
    colorPokemonmon3 = colorPokemon(mon3) 
    

    src = "english"
    
    outputPath = os.path.join(cwd, outputModPath, modPathEng)
    romFSPath = os.path.join(romFSPath, yuzuModPath)
    
    env = loadUnityPath(romFSPath, outputPath, src, text)
        
    #do pokemon name patching before anything else. 
    if not os.path.exists(outputPath):
        os.makedirs(outputPath, 0o666)
        
    os.chdir(outputPath)
    for obj in env.objects:
        
        if obj.path_id in pathList:
            
            print("Found {}".format(src))
            
            tree = obj.read_typetree()
            
            #Disgusting things have been done.
            #Hard coded english message values. 
            #print("Old starter1 name :" + tree['labelDataArray'][28]['wordDataArray'][6]['str'])
            tree['labelDataArray'][28]['wordDataArray'][1]['str'] = colorPokemonmon1
            tree['labelDataArray'][28]['wordDataArray'][2]['str'] = pokeCateg[mon1]
            tree['labelDataArray'][28]['wordDataArray'][5]['str'] = colorPokemonmon1
            tree['labelDataArray'][28]['wordDataArray'][6]['str'] = pokeNames[mon1]
            #print("New starter1 name :" + tree['labelDataArray'][28]['wordDataArray'][6]['str'])
            #print("Old starter2 name :" + tree['labelDataArray'][29]['wordDataArray'][6]['str'])
            tree['labelDataArray'][29]['wordDataArray'][1]['str'] = colorPokemonmon2
            tree['labelDataArray'][29]['wordDataArray'][2]['str'] = pokeCateg[mon2]
            tree['labelDataArray'][29]['wordDataArray'][5]['str'] = colorPokemonmon2
            tree['labelDataArray'][29]['wordDataArray'][6]['str'] = pokeNames[mon2]
            #print("New starter2 name :" + tree['labelDataArray'][29]['wordDataArray'][6]['str'])
            #print("Old starter3 name :" + tree['labelDataArray'][30]['wordDataArray'][6]['str'])
            tree['labelDataArray'][30]['wordDataArray'][1]['str'] = colorPokemonmon3
            tree['labelDataArray'][30]['wordDataArray'][2]['str'] = pokeCateg[mon3]
            tree['labelDataArray'][30]['wordDataArray'][5]['str'] = colorPokemonmon3
            tree['labelDataArray'][30]['wordDataArray'][6]['str'] = pokeNames[mon3]
            #print("New starter3 name :" + tree['labelDataArray'][30]['wordDataArray'][6]['str'])
            #Saves the object tree
            obj.save_typetree(tree)
    
    with open(src, "wb") as f:
        f.write(env.file.save(packer = (64,2)))
 
    #Change back to root dir before working on ips patches
    os.chdir(cwd)

    if not os.path.exists(modPath):
        os.makedirs(modPath, 0o666)

    os.chdir(modPath)
    
    text.append("Creating Starter IPS patches.")
    for versionID in gameVersionIDs:
        
        gameOffsets = GameOffsets(BD, versionID)
        with open(f'{gameOffsets.buildID}.ips', 'wb') as ipsFile:
            ipsFile.write(GenerateStarterPatches(gameOffsets, mon1, mon2, mon3))
        
        gameOffsets = GameOffsets(SP, versionID)
        with open(f'{gameOffsets.buildID}.ips', 'wb') as ipsFile:
            ipsFile.write(GenerateStarterPatches(gameOffsets, mon1, mon2, mon3))
        
    # Return to original directory
    text.append("Starters Randomized.")
    os.chdir(cwd)
