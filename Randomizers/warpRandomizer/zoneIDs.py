
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
                self.nameDic[zoneID] = name
    
    def getZoneID(self, name):
        return self.zoneDic[name]
    
    def getName(self, zoneID):
        return self.nameDic[str(zoneID)]