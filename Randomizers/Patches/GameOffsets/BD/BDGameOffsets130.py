class BDGameOffsets130:
    def __init__(self):
        self.buildID = '94CEAE325C205C4B9D6F7235552F28FD'

        # Starter Pokémon Offsets
        get_DefaultPokeNoAddress = 0x2CF13D0

        self.starterGrassOffset = get_DefaultPokeNoAddress + 0xC8
        self.starterFireOffset = self.starterGrassOffset + 0x8C
        self.starterWaterOffset = self.starterFireOffset + 0x4

        # Rival Pokémon Offsets
        get_RivalPokeNoAddress = 0x2CF1750

        self.rivalGrassOffset = get_RivalPokeNoAddress + 0xC8
        self.rivalFireOffset = self.rivalGrassOffset + 0x8C
        self.rivalWaterOffset = self.rivalFireOffset + 0x4
