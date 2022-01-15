import os, UnityPy



#Unused
def loadUnityPath(romfsPath, outputPath, src, text):
    
    
    if os.path.exists(outputPath) and os.path.isfile(os.path.join(outputPath, src)):
        os.chdir(outputPath)
        env = UnityPy.load(os.path.join(outputPath, src))
        
    elif os.path.exists(romfsPath) and os.path.isfile(os.path.join(romfsPath, src)):
        os.chdir(romfsPath)
        env = UnityPy.load(os.path.join(romfsPath, src))
        
    else:
        text.append(f"ERROR: {src} not found ")
        return
    
    text.append(f"{src} Loaded.")
    
    return env