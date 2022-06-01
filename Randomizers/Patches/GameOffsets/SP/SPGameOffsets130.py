class SPGameOffsets130:
    def __init__(self):
        self.buildID = '38F59CBDA2EB9C44B72F94C4D25935A2'

        # Starter Pokémon Offsets
        get_DefaultPokeNoAddress = 0x238C8E0

        self.starterGrassOffset = get_DefaultPokeNoAddress + 0xC8
        self.starterFireOffset = self.starterGrassOffset + 0x8C
        self.starterWaterOffset = self.starterFireOffset + 0x4

        # Rival Pokémon Offsets
        get_RivalPokeNoAddress = 0x238CC60

        self.rivalGrassOffset = get_RivalPokeNoAddress + 0xC8
        self.rivalFireOffset = self.rivalGrassOffset + 0x8C
        self.rivalWaterOffset = self.rivalFireOffset + 0x4
