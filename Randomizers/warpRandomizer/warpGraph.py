from WarpNode import WarpNode
from WarpEdge import WarpEdge
from random import choice, randrange
class WarpGraph():
    
    def __init__(self):
        
        self.nodes = []
        self.warpPool = []
        self.returnWarpPool = []
    
    def addNode(self, node : WarpNode):
        
        self.nodes.append(node)
        self.warpPool.append(node.getWarpIndexes())
        self.returnWarpPool.append(node.getReturnWarps())
        
    def getWarpPool(self):
        
        return self.warpPool
    
    def getNameDic(self):
        nameDic = {}
        for node in self.nodes:
            nameDic[node.getName()] = node
            
        return nameDic
    
    def getReturnWarpPool(self):
        
        return self.returnWarpPool
    
    def getNodeIndexes(self):
        indexDic = {}
        duplicateList = [] #Used to identify duplicates
        i = 0
        for node in self.nodes:
            if node.getZoneID() not in duplicateList:
                indexDic[str(node.getZoneID())] = i
                duplicateList.append(node.getZoneID())
                i += 1
                
            else:
                print(node.getName())
                print("Duplicate Zone Found {}".format(node.getZoneID()))
                return None
            
        return indexDic
    
    def getNodes(self):
        
        return self.nodes
    
    def getZoneDic(self):
        
        zoneDic = {}
        duplicateList = [] #Used to identify duplicates
        for node in self.nodes:
            if node.getZoneID() not in duplicateList:
                zoneDic[str(node.getZoneID())] = node
                duplicateList.append(node.getZoneID())
                
            else:
                print(node.getName())
                print("Duplicate Zone Found {}".format(node.getZoneID()))
                return None
            
        return zoneDic
    
    def repack(self, warpIndexes):
        for i in range(len(self.nodes)):
            edgeList = []
            for edge in warpIndexes:
                edgeList.append(WarpEdge(edge[0], edge[1]))
                
            self.nodes[i].setEdges(edgeList)