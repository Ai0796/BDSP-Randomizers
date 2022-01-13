class SPGameOffsets112:
    def __init__(self):
        self.buildID = '5D3A3B56321FFD4CB5B5AEDC62550AFB'
        
        # Starter Pokémon Offsets
        get_DefaultPokeNoAddress = 0x238E490

        self.starterGrassOffset = get_DefaultPokeNoAddress + 0xC8
        self.starterFireOffset = self.starterGrassOffset + 0x8C
        self.starterWaterOffset = self.starterFireOffset + 0x4
        
        # Rival Pokémon Offsets
        get_RivalPokeNoAddress = 0x238E810
        
        self.rivalGrassOffset = get_RivalPokeNoAddress + 0xC8
        self.rivalFireOffset = self.rivalGrassOffset + 0x8C
        self.rivalWaterOffset = self.rivalFireOffset + 0x4
