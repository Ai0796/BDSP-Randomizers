import os, UnityPy



#Unused
def loadUnityPath(romFSPath, outputPath, src, text):
    
    if os.path.exists(outputPath) and os.path.isfile(os.path.join(outputPath, src)):
        os.chdir(outputPath)
        env = UnityPy.load(os.path.join(outputPath, src))
        
    elif os.path.exists(romFSPath) and os.path.isfile(os.path.join(romFSPath, src)):
        os.chdir(romFSPath)
        env = UnityPy.load(os.path.join(romFSPath, src))
        
    else:
        text.append(f"ERROR: {src} not found ")
        return
    
    text.append(f"{src} Loaded.")
    
    return env