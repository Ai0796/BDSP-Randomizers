class BDGameOffsets100:
    def __init__(self):
        self.buildID = 'F87FC6075104EC4D9642A4AA6BB22216'
        
        # Starter Pokémon Offsets
        get_DefaultPokeNoAddress = 0x1BBBBB0

        self.starterGrassOffset = get_DefaultPokeNoAddress + 0xC8
        self.starterFireOffset = self.starterGrassOffset + 0x8C
        self.starterWaterOffset = self.starterFireOffset + 0x4
        
        # Rival Pokémon Offsets
        get_RivalPokeNoAddress = 0x1BBBF30
        
        self.rivalGrassOffset = get_RivalPokeNoAddress + 0xC8
        self.rivalFireOffset = self.rivalGrassOffset + 0x8C
        self.rivalWaterOffset = self.rivalFireOffset + 0x4
