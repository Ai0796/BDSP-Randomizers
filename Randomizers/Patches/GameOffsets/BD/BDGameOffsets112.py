class BDGameOffsets112:
    def __init__(self):
        self.buildID = '1B5215DF918BA04BB3894852387F82FF'
        
        # Starter Pokémon Offsets
        get_DefaultPokeNoAddress = 0x238E470

        self.starterGrassOffset = get_DefaultPokeNoAddress + 0xC8
        self.starterFireOffset = self.starterGrassOffset + 0x8C
        self.starterWaterOffset = self.starterFireOffset + 0x4
        
        # Rival Pokémon Offsets
        get_RivalPokeNoAddress = 0x238E7F0
        
        self.rivalGrassOffset = get_RivalPokeNoAddress + 0xC8
        self.rivalFireOffset = self.rivalGrassOffset + 0x8C
        self.rivalWaterOffset = self.rivalFireOffset + 0x4
