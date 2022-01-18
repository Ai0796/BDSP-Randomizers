from WarpEdge import WarpEdge
from zoneIDs import zoneIDs
from random import randrange

class WarpNode():
    
    zoneConverter = zoneIDs()
    
    def __init__(self, warpEdges: list, name: str, path_id: int):
        
        ##I'm 90% sure you just need WarpZone and WarpIndex for teleportation
        self.warpEdges = warpEdges
        self.name = name
        self.zoneID = WarpNode.zoneConverter.getZoneID(name)
        self.path_id = int
        
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
    
    def getWarpIndexes(self):
        warpList = []
        for warpEdge in self.warpEdges:
            warpList.append([warpEdge.getWarpZone(), warpEdge.getWarpIndex()])
        return warpList
    
    def getReturnWarps(self):
        warpList = []
        for warpIndex in range(len(self.warpEdges)):
            warpList.append([self.zoneID, warpIndex])
        return warpList
            
    def getPathID(self):
        return self.path_id
    
    def getRandomWarp(self):
        warpList = self.getWarpIndexes()
        warpNum = randrange(0, len(warpList))
        returnWarpList = self.getReturnWarps()
        
        return (warpList[warpNum], returnWarpList[warpNum])