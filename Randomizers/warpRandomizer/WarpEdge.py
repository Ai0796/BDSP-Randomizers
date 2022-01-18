# class WarpNode():
    
#     def __init__(self, Position: tuple, WarpZone: int, WarpIndex: int, InputDir: int, FlagIndex: int, ScriptLabel: int, ExitLabel: int, ConnectionName: String):
        
#         self.x = Position[0]
#         self.y = Position[1]
#         self.z = Position[2]
        
        
#         ##I'm 90% sure you just need WarpZone and WarpIndex for teleportation
#         self.WarpZone = WarpZone
#         self.WarpIndex = WarpIndex
#         self.InputDir = InputDir
#         self.FlagIndex = FlagIndex
#         self.ScriptLabel = ScriptLabel
#         self.ExitLabel = ExitLabel
#         self.ConnectionName = ConnectionName
        
#     def setPosition(self, Position: tuple):
        
#         self.x = Position[0]
#         self.y = Position[1]
#         self.z = Position[2]
        
#     def getWarpZone(self):
#         return self.WarpZone
    
#     def getWarpIndex(self):
#         return self.WarpIndex
        
    
class WarpEdge():
    
    def __init__(self, WarpZone: int, WarpIndex: int):
        
        ##I'm 90% sure you just need WarpZone and WarpIndex for teleportation
        self.WarpZone = WarpZone
        self.WarpIndex = WarpIndex
        
    def getWarpZone(self):
        return self.WarpZone
    
    def getWarpIndex(self):
        return self.WarpIndex