#py -m pip install UnityPy
import UnityPy
import random
from PyQt5.QtWidgets import QTextEdit
import os
from pathlib import Path
import struct
from Resources.paths.filenames import filenames
from Resources.paths.loadUnityPath import loadUnityPath
from Resources.paths.paths import paths

#PathIDs inside Unity
#DO NOT CHANGE UNLESS GAME IS UPDATED
from Resources.pathIDs.ev_script_pathIDs import ev_script

fld_item = ev_script.fld_item.value
pathList = [fld_item]

modBasePath = paths.modPath.value
yuzuModPath = paths.ev_script.value
modPath = os.path.join(modBasePath, yuzuModPath)
outputModPath = paths.emulatorPath.value

src = filenames.ev_script.value

def uselessItemRemover(itemNo):
    if itemNo > 428: # Explorer Kit onwards
        return True
    elif itemNo in [0, 70, 71]: # None, Life Orb, Power Orb
        return True
    elif itemNo >= 65 and itemNo <= 69: # Blue Flute to White Flute
        return True
    elif itemNo >= 95 and itemNo <= 98: # Growth Mulch to Gooey Mulch
        return True
    elif itemNo >= 112 and itemNo <= 134: # Griseous Orb to Sweet Heart
        return True
    elif itemNo >= 137 and itemNo <= 148: # Greet Mail to Bridge Mail M
        return True
    elif itemNo == 155: # Oran Berry
        return True
    elif itemNo >= 159 and itemNo <= 212: # Figy Berry to Rowap Berry
        return True
    elif itemNo == 216: # Exp. Share
        return True
    elif itemNo == 236: # Light Ball
        return True
    elif itemNo >= 256 and itemNo <= 264: # Lucky Punch to Yellow Scarf
        return True
    else:
        return False

def isTM(itemNo):
    return (itemNo >= 328 and itemNo <= 464)

#This is taken directly from xLumas original randomizer
def encode_float(var):
	var = float(var)
	data = int(struct.unpack('<I', struct.pack('<f', var))[0])
	return data

def decode_int(var):
	var = int(var)
	data = float(struct.unpack('!f', struct.pack('!I', var & 0xFFFFFFFF))[0])
	return data
        
    
def generateRandom():
    lowRange = 1
    highRange = 327
    
    itemNo = random.randrange(lowRange, highRange)
    ##while item is useless generate a different item
    while uselessItemRemover(itemNo):
        itemNo = random.randrange(lowRange, highRange)
    return itemNo
    
def RandomizeFieldItems(text, romFSPath):
    # Checks if romfs path already exist
    
    cwd = os.getcwd()
    
    outputPath = os.path.join(cwd, outputModPath, modPath)
    romFSPath = os.path.join(romFSPath, yuzuModPath)
    
    env = loadUnityPath(romFSPath, outputPath, src, text)

    for obj in env.objects:
        if obj.path_id in pathList:
            
            print("Found {}".format(src))
            
            tree = obj.read_typetree()
            if tree['m_Name'] == "fld_item":
                for item in tree["Scripts"]:
                    # print(item["Commands"])
                    if item["Commands"][0]["Arg"][0]["data"] in [41, 187, 194]: ##This is just a hack since scripts are also included in field items
                            fldItem = item["Commands"][0]["Arg"][1]["data"] #Don't ask why it's stored like this I wouldn't know
                            decoded = decode_int(fldItem)
                            if not isTM(decoded) and len(str(fldItem)) >= 9:
                                ##Set item to new encoded value
                                item["Commands"][0]["Arg"][1]["data"] = encode_float(generateRandom())
                obj.save_typetree(tree)
            else:
                print("Error use different path_id")        
            
            
            
            
    text.append("Field Items Randomized.")                
    # saving an edited file
    # apply modifications to the objects
    # don't forget to use data.save()
        # ...
        # 
        # 
    #This output is compressed, thanks to Copycat#8110
    if not os.path.exists(outputPath):
        os.makedirs(outputPath, 0o666)
        
    os.chdir(outputPath)
        
    with open(src, "wb") as f:
        f.write(env.file.save(packer = (64,2)))
    text.append("Field Items Saved.")
    
    os.chdir(cwd)
