from enum import Enum

from Resources.pathIDs.personal_masterdatas_pathIDs import personal_masterdatas


#Unused
class paths(Enum):
    
    modPath = "romfs/Data"
    exefsModPath = "exefs"
    emulatorPath = "emulatorRandomized"
    atmospherePath = "atmosphereRandomized/atmosphere"
    atmosphereRomfsDiamond = "contents/0100000011D90000"
    atmosphereRomfsPearl = "contents/010018E011D92000"
    atmosphereExefsPath = "exefs_patches/Starters/"
    english = "StreamingAssets/AssetAssistant/Message"
    masterdatas = "StreamingAssets/AssetAssistant/Dpr"
    gamesettings = "StreamingAssets/AssetAssistant/Dpr/scriptableobjects"
    personal_masterdatas = "StreamingAssets/AssetAssistant/Pml"
    ev_script = "StreamingAssets/AssetAssistant/Dpr"
    ugdata = "StreamingAssets/AssetAssistant/UnderGround/data"