
class zoneIDs():
    
    def __init__(self):
        filepath = "Resources/zoneIDs.txt"
        self.zoneDic = {}
        self.nameDic = {}
        
        with open(filepath) as f:
            for line in f.read().splitlines():
                line = line.split(",")
                name = line[1]
                zoneID = line[0]
                self.zoneDic[name] = int(zoneID)
                self.zoneDicKeys = list(self.zoneDic.keys())
                self.nameDic[zoneID] = name
    
    def getZoneID(self, name):
        if name in self.zoneDicKeys:
            return self.zoneDic[name]
        else:
            return 0
    
    def getName(self, zoneID):
        return self.nameDic[str(zoneID)]