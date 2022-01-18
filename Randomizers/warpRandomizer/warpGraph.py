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
    
    def getReturnWarpPool(self):
        
        return self.returnWarpPool
    
    def getNodes(self):
        
        return self.nodes