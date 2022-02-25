class SPGameOffsets120:
    def __init__(self):
        self.buildID = 'D75246EC33C2F64BB1D8C893D4823FFC'

        # Starter Pokémon Offsets
        get_DefaultPokeNoAddress = 0x2334E50

        self.starterGrassOffset = get_DefaultPokeNoAddress + 0xC8
        self.starterFireOffset = self.starterGrassOffset + 0x8C
        self.starterWaterOffset = self.starterFireOffset + 0x4

        # Rival Pokémon Offsets
        get_RivalPokeNoAddress = 0x23351D0

        self.rivalGrassOffset = get_RivalPokeNoAddress + 0xC8
        self.rivalFireOffset = self.rivalGrassOffset + 0x8C
        self.rivalWaterOffset = self.rivalFireOffset + 0x4