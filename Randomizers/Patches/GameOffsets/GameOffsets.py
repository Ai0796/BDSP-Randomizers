from ..Enums.GameRevision import GameRevision
from ..Enums.GameType import GameType
from ..GameOffsets.BD import *
from ..GameOffsets.SP import *

class GameOffsets:
    def __init__(self, gameType: GameType, gameRevision: GameRevision):
        if gameType == GameType.BD:
            if gameRevision == GameRevision.REV_100:
                offsets = BDGameOffsets100.BDGameOffsets100()
            elif gameRevision == GameRevision.REV_110:
                offsets = BDGameOffsets110.BDGameOffsets110()
            elif gameRevision == GameRevision.REV_111:
                offsets = BDGameOffsets111.BDGameOffsets111()
            elif gameRevision == GameRevision.REV_112:
                offsets = BDGameOffsets112.BDGameOffsets112()
            elif gameRevision == GameRevision.REV_113:
                offsets = BDGameOffsets113.BDGameOffsets113()
            elif gameRevision == GameRevision.REV_120:
                offsets = BDGameOffsets120.BDGameOffsets120()
            elif gameRevision == GameRevision.REV_130:
                offsets = BDGameOffsets130.BDGameOffsets130()
        if gameType == GameType.SP:
            if gameRevision == GameRevision.REV_100:
                offsets = SPGameOffsets100.SPGameOffsets100()
            elif gameRevision == GameRevision.REV_110:
                offsets = SPGameOffsets110.SPGameOffsets110()
            elif gameRevision == GameRevision.REV_111:
                offsets = SPGameOffsets111.SPGameOffsets111()
            elif gameRevision == GameRevision.REV_112:
                offsets = SPGameOffsets112.SPGameOffsets112()
            elif gameRevision == GameRevision.REV_113:
                offsets = SPGameOffsets113.SPGameOffsets113()
            elif gameRevision == GameRevision.REV_120:
                offsets = SPGameOffsets120.SPGameOffsets120()
            elif gameRevision == GameRevision.REV_130:
                offsets = SPGameOffsets130.SPGameOffsets130()
        
        self.buildID = offsets.buildID

        self.starterGrassOffset = offsets.starterGrassOffset
        self.starterFireOffset = offsets.starterFireOffset
        self.starterWaterOffset = offsets.starterWaterOffset
        
        self.rivalGrassOffset = offsets.rivalGrassOffset
        self.rivalFireOffset = offsets.rivalFireOffset
        self.rivalWaterOffset = offsets.rivalWaterOffset
