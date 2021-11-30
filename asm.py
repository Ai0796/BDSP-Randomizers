from keystone import *
import argparse


parser = argparse.ArgumentParser(description='Convert ASM to HEX instructions for.')
parser.add_argument('asm', nargs='?', help='asm function you want to convert.')


args = parser.parse_args()
d = vars(args)
if d['asm'] is not None:
    print(d['asm'])
    ks = Ks(KS_ARCH_ARM64, KS_MODE_LITTLE_ENDIAN)
    patch1 = ks.asm(d['asm'], addr=0x0)
    hex1 = ''.join( ['{:02X}'.format(b) for b in patch1[0]] )
    print(hex1)
else:
    print("Please insert the ASM you wish to assemble")
    print("make sure if you are calling a label to change address in addr")