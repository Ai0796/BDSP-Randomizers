#py -m pip install UnityPy
import UnityPy
import random
import os
from pathlib import Path
from PyQt5.QtWidgets import QTextEdit
from keystone import *

#DO NOT CHANGE UNLESS GAME IS UPDATED
modPath = "mods/exefs/"



#file name has to be the build id for IPS patches. 
#for pchtxt patches it can be named whatever so we will use starter.pchtxt
diamondBuildID = 'D9E96FB92878E3458AAE7E8D31AB32A9'
pearlBuildID = '3C70CAE153DF0B4F8A7B24C60FD8D0E7'

#diamond 
#turtwig w0, 183
#chimchar w8, 186
#Pilup w9, 189
diamondStarter1Off = '{:08X}'.format(0x01FEAB28)
diamondStarter2Off = '{:08X}'.format(0x01FEABB4)
diamondStarter3Off = '{:08X}'.format(0x01FEABB8)
#diamond rival
#you pick turtwig he pick chimchar w0, 186
#you pick chimchar he pick pillup w8,189 
#you Pilup he pick turtwig w9, 183
diamondStarterRival1Off = '{:08X}'.format(0x01FEAEA8)
diamondStarterRival2Off = '{:08X}'.format(0x01FEAF34)
diamondStarterRival3Off = '{:08X}'.format(0x01FEAF38)

#pearl
#turtwig w0, 183
#chimchar w8, 186
#Pilup w9, 189
pearlStarter1Off =  '{:08X}'.format(0x0238DEC8)
pearlStarter2Off =  '{:08X}'.format(0x0238DF54)
pearlStarter3Off =  '{:08X}'.format(0x0238DF58)

#pearl rival
#you pick turtwig he pick chimchar w0, 186
#you pick chimchar he pick pillup w8,189 
#you Pilup he pick turtwig w9, 183
pearlStarterRival1Off = '{:08X}'.format(0x0238E248)
pearlStarterRival2Off = '{:08X}'.format(0x0238E2D4)
pearlStarterRival3Off = '{:08X}'.format(0x0238E2D8)

#Change hardcoded pokemon name 
#AssetAssistant/Message/English
#PathIDs inside Unity
#DO NOT CHANGE UNLESS GAME IS UPDATED
engMsgPathID = -5307844841844767521
pathList = [engMsgPathID]

modPathEng = "mods/romfs/Data/StreamingAssets/AssetAssistant/Message"
yuzuModPathEng = "StreamingAssets/AssetAssistant/Message"
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

    return color
                
def RandomizeStarters(text, romFSPath):
    cwd = os.getcwd()
    pokeNames = getPokemonNames()
    pokeCateg = getPokemonCategory()

    text.append("Randomizing Starters!")
    
    #initialize Keystone-Engine 
    ks = Ks(KS_ARCH_ARM64, KS_MODE_LITTLE_ENDIAN)
    #randomize our mons. 
    mon1 = random.choice(range(1, 493))
    mon2 = random.choice(range(1, 493))
    mon3 = random.choice(range(1, 493))

    #color mons
    colorPokemonmon1 = colorPokemon(mon1)
    colorPokemonmon2 = colorPokemon(mon2)
    colorPokemonmon3 = colorPokemon(mon3)
    
    #assign build the asm string
    starter1 = "mov w0, #" + hex(mon1)
    starter2 = "mov w8, #" + hex(mon2)
    starter3 = "mov w9, #" + hex(mon3)
    #rival build. 
    rival1 = "mov w0, #" + hex(mon2)
    rival2 = "mov w8, #" + hex(mon3)
    rival3 = "mov w8, #" + hex(mon1)
    
    #build our asm patch
    patch1 = ks.asm(starter1)
    patch2 = ks.asm(starter2)
    patch3 = ks.asm(starter3)
    patchR1 = ks.asm(rival1)
    patchR2 = ks.asm(rival2)
    patchR3 = ks.asm(rival3)
    
    text.append("Assembling Patch.")
    #convert to strings. 
    hex1 = ''.join( ['{:02X}'.format(b) for b in patch1[0]] )
    hex2 = ''.join( ['{:02X}'.format(b) for b in patch2[0]] )
    hex3 = ''.join( ['{:02X}'.format(b) for b in patch3[0]] )
    hex4 = ''.join( ['{:02X}'.format(b) for b in patchR1[0]] )
    hex5 = ''.join( ['{:02X}'.format(b) for b in patchR2[0]] )
    hex6 = ''.join( ['{:02X}'.format(b) for b in patchR3[0]] )
    hexIds = [hex1, hex2, hex3, hex4, hex5, hex6]
    
    text.append("Building Patch files.")
    #build diamond patch file. 
    pchDiamondPatch = ["@nsobid-{}".format(diamondBuildID),"","@enabled",
    "{} {}".format(diamondStarter1Off, hex1),
    "{} {}".format(diamondStarter2Off, hex2),
    "{} {}".format(diamondStarter3Off, hex3),
    "{} {}".format(diamondStarterRival1Off, hex4),
    "{} {}".format(diamondStarterRival2Off, hex5),
    "{} {}".format(diamondStarterRival3Off, hex6),
    ""]
    
    src = "english"
    
    outputPath = os.path.join(cwd, "mods", modPathEng)
    if os.path.exists(outputPath) and os.path.isfile(os.path.join(outputPath, src)):
        env = UnityPy.load(os.path.join(outputPath, src))
        
    elif os.path.exists(os.path.join(romFSPath, yuzuModPathEng)) and os.path.isfile(os.path.join(romFSPath, yuzuModPathEng, src)):
        env = UnityPy.load(os.path.join(romFSPath, yuzuModPathEng, src))
        
    else:
        text.append("ERROR: English messages not found ")
        return
        
    #do pokemon name patching before anything else. 
    if not os.path.exists(modPathEng):
        os.makedirs(modPathEng, 0o666)
        
    os.chdir(modPathEng)
    for obj in env.objects:
        
        if obj.path_id in pathList:
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
    
    with open("english", "wb") as f:
        f.write(env.file.save(packer = (64,2)))
        
    #Change back to root dir before working on pchtxt patches
    os.chdir(cwd)

    #write out diamond patch
    if not os.path.exists(modPath):
        os.makedirs(modPath, 0o666)

    os.chdir(modPath)
    
    diamond = open("starterDiamond.pchtxt", "w")
    for element in pchDiamondPatch:
        diamond.write(element + "\n")
    diamond.close()
    
    #build our IPS file
    #we can't currently build ips's because of the 3 byte address limitation 
    #i have no clue how to fix. 
    #build_diamond_ips(hexIds)
    
    
    #build pearl patch file. 
    pchPearlPatch = ["@nsobid-{}".format(pearlBuildID),"","@enabled",
    "{} {}".format(pearlStarter1Off, hex1),
    "{} {}".format(pearlStarter2Off, hex2),
    "{} {}".format(pearlStarter3Off, hex3),
    "{} {}".format(pearlStarterRival1Off, hex4),
    "{} {}".format(pearlStarterRival2Off, hex5),
    "{} {}".format(pearlStarterRival3Off, hex6),
    ""]
    
    #write out pearl patch
    pearl = open("starterPearl.pchtxt", "w")
    for element in pchPearlPatch:
        pearl.write(element + "\n")
    pearl.close()
    
    
    
    text.append("Starters Randomized.")

    os.chdir(cwd)
