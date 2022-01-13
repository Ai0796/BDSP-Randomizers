from keystone import *

class Patch:
    def __init__(self, shift: int = 0, ks: Ks = None):
        self.shift = shift
        self.ks = ks
        self.patches = []

    def addPatch(self, address: int, instruction):
        if type(instruction) != int and type(instruction) == str:
            address, instruction = self._addPatch(address, instruction)
        else:
            instruction = instruction.to_bytes((instruction.bit_length() + 7) // 8, 'big')
        
        address += self.shift
        if address > 0xFFFFFFFF:
            raise ValueError
        
        address = address.to_bytes(4, 'big')
        self.patches.append((address, instruction))  

    def _addPatch(self, address: int, instruction: str):
        if self.ks == None:
            self.ks = Ks(KS_ARCH_ARM64, KS_MODE_LITTLE_ENDIAN)
        
        instruction = bytearray(self.ks.asm(instruction)[0])
        return (address, instruction)

    def generateIPS32Patch(self):
        outBuffer = bytearray('IPS32', 'ascii')
        for patch in self.patches:
            address, instruction = patch
            outBuffer += address
            outBuffer += len(instruction).to_bytes(2, 'big')
            outBuffer += instruction
        outBuffer += bytearray('EEOF', 'ascii')
        return outBuffer
