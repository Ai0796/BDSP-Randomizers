class SPGameOffsets110:
    def __init__(self):
        self.buildID = '609FAC97880FA04CA6A8626D54A2BAB2'
        
        # Starter Pokémon Offsets
        get_DefaultPokeNoAddress = 0x238C6D0

        self.starterGrassOffset = get_DefaultPokeNoAddress + 0xC8
        self.starterFireOffset = self.starterGrassOffset + 0x8C
        self.starterWaterOffset = self.starterFireOffset + 0x4
        
        # Rival Pokémon Offsets
        get_RivalPokeNoAddress = 0x238CA50
        
        self.rivalGrassOffset = get_RivalPokeNoAddress + 0xC8
        self.rivalFireOffset = self.rivalGrassOffset + 0x8C
        self.rivalWaterOffset = self.rivalFireOffset + 0x4
