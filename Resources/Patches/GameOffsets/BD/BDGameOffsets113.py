class BDGameOffsets113:
    def __init__(self):
        self.buildID = 'BC259F7EE8E79A4995CDC79E69CAC6CD'
        
        # Starter Pokémon Offsets
        get_DefaultPokeNoAddress = 0x237CCF0

        self.starterGrassOffset = get_DefaultPokeNoAddress + 0xC8
        self.starterFireOffset = self.starterGrassOffset + 0x8C
        self.starterWaterOffset = self.starterFireOffset + 0x4
        
        # Rival Pokémon Offsets
        get_RivalPokeNoAddress = 0x237D070
        
        self.rivalGrassOffset = get_RivalPokeNoAddress + 0xC8
        self.rivalFireOffset = self.rivalGrassOffset + 0x8C
        self.rivalWaterOffset = self.rivalFireOffset + 0x4
