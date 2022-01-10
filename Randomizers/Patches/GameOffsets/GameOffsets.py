from ..Enums.GameRevision import GameRevision
from ..Enums.GameType import GameType
from ..GameOffsets.BD import *
from ..GameOffsets.SP import *

class GameOffsets:
    def __init__(self, gameType: GameType, gameRevision: GameRevision):
        match gameType:
            case GameType.BD:
                match gameRevision:
                    case GameRevision.REV_100:
                        offsets = BDGameOffsets100.BDGameOffsets100()
                    case GameRevision.REV_110:
                        offsets = BDGameOffsets110.BDGameOffsets110()
                    case GameRevision.REV_111:
                        offsets = BDGameOffsets111.BDGameOffsets111()
                    case GameRevision.REV_112:
                        offsets = BDGameOffsets112.BDGameOffsets112()
                    case GameRevision.REV_113:
                        offsets = BDGameOffsets113.BDGameOffsets113()
            case GameType.SP:
                match gameRevision:
                    case GameRevision.REV_100:
                        offsets = SPGameOffsets100.SPGameOffsets100()
                    case GameRevision.REV_110:
                        offsets = SPGameOffsets110.SPGameOffsets110()
                    case GameRevision.REV_111:
                        offsets = SPGameOffsets111.SPGameOffsets111()
                    case GameRevision.REV_112:
                        offsets = SPGameOffsets112.SPGameOffsets112()
                    case GameRevision.REV_113:
                        offsets = SPGameOffsets113.SPGameOffsets113()
        
        self.buildID = offsets.buildID

        self.starterGrassOffset = offsets.starterGrassOffset
        self.starterFireOffset = offsets.starterFireOffset
        self.starterWaterOffset = offsets.starterWaterOffset
        
        self.rivalGrassOffset = offsets.rivalGrassOffset
        self.rivalFireOffset = offsets.rivalFireOffset
        self.rivalWaterOffset = offsets.rivalWaterOffset
