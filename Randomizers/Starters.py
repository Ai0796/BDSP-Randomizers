#py -m pip install UnityPy
import UnityPy
import random
import os
from pathlib import Path
from PyQt5.QtWidgets import QTextEdit
from keystone import *

#DO NOT CHANGE UNLESS GAME IS UPDATED
modPath = "mods/exefs/Data/"

#file name has to be the build id for IPS patches. 
#for pchtxt patches it can be named whatever so we will use starter.pchtxt
diamondBuildID = 'D9E96FB92878E3458AAE7E8D31AB32A9'
pearlBuildID = '3C70CAE153DF0B4F8A7B24C60FD8D0E7'


diamondStarter1Off = '{:08X}'.format(0x01FEAB28)
diamondStarter2Off = '{:08X}'.format(0x01FEABB4)
diamondStarter3Off = '{:08X}'.format(0x01FEABB8)


pearlStarter1Off =  '{:08X}'.format(0x0248DDC8)
pearlStarter2Off =  '{:08X}'.format(0x0248DE54)
pearlStarter3Off =  '{:08X}'.format(0x0248DE58)


def RandomizeStarters(text):
    cwd = os.getcwd()

    text.append("Randomizing Starters!")

    #initialize Keystone-Engine 
    ks = Ks(KS_ARCH_ARM64, KS_MODE_LITTLE_ENDIAN)
    #randomize our mons. 
    mon1 = random.choice(range(1, 493))
    mon2 = random.choice(range(1, 493))
    mon3 = random.choice(range(1, 493))
    #assign build the asm string
    starter1 = "mov w0, #" + hex(mon1)
    starter2 = "mov w8, #" + hex(mon2)
    starter3 = "mov w9, #" + hex(mon3)

    #build our asm patch
    patch1 = ks.asm(starter1)
    patch2 = ks.asm(starter2)
    patch3 = ks.asm(starter3)
    text.append("Assembling Patch.")
    #convert to strings. 
    hex1 = ''.join( ['{:02X}'.format(b) for b in patch1[0]] )
    hex2 = ''.join( ['{:02X}'.format(b) for b in patch2[0]] )
    hex3 = ''.join( ['{:02X}'.format(b) for b in patch3[0]] )
    
    text.append("Building Patch files.")
    #build diamond patch file. 
    pchDiamondPatch = ["@nsobid-{}".format(diamondBuildID),"","@enabled",
    "{} {}".format(diamondStarter1Off, hex1),
    "{} {}".format(diamondStarter2Off, hex2),
    "{} {}".format(diamondStarter3Off, hex3),
    ""]
    #write out diamond patch
    if not os.path.exists(modPath):
        os.makedirs(modPath, 0o666)

    os.chdir(modPath)
    
    diamond = open("starterDiamond.pchtxt", "w")
    for element in pchDiamondPatch:
        diamond.write(element + "\n")
    diamond.close()

    #build pearl patch file. 
    pchPearlPatch = ["@nsobid-{}".format(pearlBuildID),"","@enabled",
    "{} {}".format(pearlStarter1Off, hex1),
    "{} {}".format(pearlStarter1Off, hex2),
    "{} {}".format(pearlStarter1Off, hex3),
    ""]
    
    #write out pearl patch
    
    pearl = open("starterPearl.pchtxt", "w")
    for element in pchPearlPatch:
        pearl.write(element + "\n")
    pearl.close()
    
    text.append("Starters Randomized.")
