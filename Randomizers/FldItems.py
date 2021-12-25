#py -m pip install UnityPy
import UnityPy
import random
from PyQt5.QtWidgets import QTextEdit
import os
from pathlib import Path
import struct

#PathIDs inside Unity
#DO NOT CHANGE UNLESS GAME IS UPDATED
fld_item = -4074276362271022109
pathList = [fld_item]

modPath = "romfs/Data/StreamingAssets/AssetAssistant/Dpr"
yuzuModPath = "StreamingAssets/AssetAssistant/Dpr"

def uselessItemRemover(itemNo):
    
    if itemNo > 428: ##Explorer kit
        return True
    elif itemNo >= 159 and itemNo <= 212: #Figy Berry to Rowap Berry
        return True
    elif itemNo >= 137 and itemNo <= 148: #Grass mail to Brick mail
        return True
    elif itemNo >= 113 and itemNo <= 134: #Braces and Arceus Plates
        return True
    elif itemNo in [236, 155, 70, 71]: #Light ball, Oran berry, Shoal Salt, and Shoal Shell
        return True
    elif itemNo >= 95 and itemNo <= 98: #Mulches for Berry Planting
        return True
    elif itemNo >= 256 and itemNo <= 264: #Lucky punch to Yellow scarf
        return True
    elif itemNo == 216: #EXP Share
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
        
    src = "ev_script"
    
    cwd = os.getcwd()
    
    outputPath = os.path.join(cwd, "mods", modPath)
    
    if os.path.exists(outputPath) and os.path.isfile(os.path.join(outputPath, src)):
        os.chdir(outputPath)
        env = UnityPy.load(os.path.join(outputPath, src))
        
    elif os.path.exists(os.path.join(romFSPath, yuzuModPath)) and os.path.isfile(os.path.join(romFSPath, yuzuModPath, src)):
        os.chdir(romFSPath)
        env = UnityPy.load(os.path.join(romFSPath, yuzuModPath, src))
    else:
        text.append("ERROR: ev_script not found")
        return
    
    extract_dir = "Walker"
    text.append("Field Items Loaded.")

    for obj in env.objects:
        # if obj.path_id in pathList:
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
