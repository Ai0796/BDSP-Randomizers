from WarpEdge import WarpEdge
from zoneIDs import zoneIDs

class WarpNode():
    
    zoneConverter = zoneIDs()
    
    def __init__(self, warpEdges: list, name: str):
        
        ##I'm 90% sure you just need WarpZone and WarpIndex for teleportation
        self.warpEdges = warpEdges
        self.name = name
        self.zoneID = WarpNode.zoneConverter.getZoneID(name)
        
    def getWarpEdges(self):
        return self.warpEdges
    
    def getSize(self):
        return len(self.warpEdges)
    
    def setEdges(self, warpEdges: list):
        self.warpEdges = warpEdges
        
    def getName(self):
        return self.name
    
    def getZoneID(self):
        return self.zoneID