class BDGameOffsets120:
    def __init__(self):
        self.buildID = '35B9D8779B1951418FB609945CCC8C7E'

        # Starter Pokémon Offsets
        get_DefaultPokeNoAddress = 0x2334E30

        self.starterGrassOffset = get_DefaultPokeNoAddress + 0xC8
        self.starterFireOffset = self.starterGrassOffset + 0x8C
        self.starterWaterOffset = self.starterFireOffset + 0x4

        # Rival Pokémon Offsets
        get_RivalPokeNoAddress = 0x23351B0

        self.rivalGrassOffset = get_RivalPokeNoAddress + 0xC8
        self.rivalFireOffset = self.rivalGrassOffset + 0x8C
        self.rivalWaterOffset = self.rivalFireOffset + 0x4