class BDGameOffsets110:
    def __init__(self):
        self.buildID = 'EA058A067CBD6943A6CF65B4588B6098'
        
        # Starter Pokémon Offsets
        get_DefaultPokeNoAddress = 0x238C6B0

        self.starterGrassOffset = get_DefaultPokeNoAddress + 0xC8
        self.starterFireOffset = self.starterGrassOffset + 0x8C
        self.starterWaterOffset = self.starterFireOffset + 0x4
        
        # Rival Pokémon Offsets
        get_RivalPokeNoAddress = 0x238CA30
        
        self.rivalGrassOffset = get_RivalPokeNoAddress + 0xC8
        self.rivalFireOffset = self.rivalGrassOffset + 0x8C
        self.rivalWaterOffset = self.rivalFireOffset + 0x4
