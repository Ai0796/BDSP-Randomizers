import UnityPy
import random
from PyQt5.QtWidgets import QTextEdit
import os
from distutils.dir_util import copy_tree as copytree
from Resources.paths.filenames import filenames
from Resources.paths.loadUnityPath import loadUnityPath
from Resources.paths.paths import paths

inputBasePath = paths.emulatorPath.value
romfsBasePath = paths.modPath.value
exefsBasePath = paths.exefsModPath.value
modOutputPath = paths.atmospherePath.value
modRomfsPathD = paths.atmosphereRomfsDiamond.value
modRomfsPathP = paths.atmosphereRomfsPearl.value
modExefsPath = paths.atmosphereExefsPath.value


def makedir(path):
    if not os.path.exists(path):
        os.makedirs(path, 0o666)

##Used to move all the generated files into a setup meant for atmosphere
def MovePath(text):

    cwd = os.getcwd()
    
    romfsInputPath = os.path.join(cwd, inputBasePath, romfsBasePath)
    exefsInputPath = os.path.join(cwd, inputBasePath, exefsBasePath)
    romfsOutputPathD = os.path.join(cwd, modOutputPath, modRomfsPathD, romfsBasePath)
    romfsOutputPathP = os.path.join(cwd, modOutputPath, modRomfsPathP, romfsBasePath)
    exefsOutputPath = os.path.join(cwd, modOutputPath, modExefsPath)
    
    print(romfsInputPath)
    print(exefsInputPath)
    print(romfsOutputPathD)
    print(romfsOutputPathP)
    print(exefsOutputPath)     
    
    if os.path.exists(romfsInputPath):
        
        makedir(romfsOutputPathD)
        makedir(romfsOutputPathP)
        
        copytree(romfsInputPath, romfsOutputPathD)
        copytree(romfsInputPath, romfsOutputPathP)
        text.append("Created Atmosphere RomFS")
        
    if os.path.exists(exefsInputPath):
        makedir(exefsOutputPath)

        copytree(exefsInputPath, exefsOutputPath)
        text.append("Created Atmosphere ExeFS")

if __name__ == "__main__":
    text = []
    MovePath(text)
    print(text)
    