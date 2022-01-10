class SPGameOffsets111:
    def __init__(self):
        self.buildID = '3C70CAE153DF0B4F8A7B24C60FD8D0E7'
        
        # Starter Pokémon Offsets
        get_DefaultPokeNoAddress = 0x238DD00

        self.starterGrassOffset = get_DefaultPokeNoAddress + 0xC8
        self.starterFireOffset = self.starterGrassOffset + 0x8C
        self.starterWaterOffset = self.starterFireOffset + 0x4
        
        # Rival Pokémon Offsets
        get_RivalPokeNoAddress = 0x238E080
        
        self.rivalGrassOffset = get_RivalPokeNoAddress + 0xC8
        self.rivalFireOffset = self.rivalGrassOffset + 0x8C
        self.rivalWaterOffset = self.rivalFireOffset + 0x4
