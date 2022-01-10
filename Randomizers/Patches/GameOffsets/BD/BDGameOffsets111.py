class BDGameOffsets111:
    def __init__(self):
        self.buildID = 'D9E96FB92878E3458AAE7E8D31AB32A9'
        
        # Starter Pokémon Offsets
        get_DefaultPokeNoAddress = 0x1FEA960

        self.starterGrassOffset = get_DefaultPokeNoAddress + 0xC8
        self.starterFireOffset = self.starterGrassOffset + 0x8C
        self.starterWaterOffset = self.starterFireOffset + 0x4
        
        # Rival Pokémon Offsets
        get_RivalPokeNoAddress = 0x1FEACE0
        
        self.rivalGrassOffset = get_RivalPokeNoAddress + 0xC8
        self.rivalFireOffset = self.rivalGrassOffset + 0x8C
        self.rivalWaterOffset = self.rivalFireOffset + 0x4
