"""
0x601010 <flag>:	0xb18de5aa	0xcddeeabf	0xc9acdfb9	0x819cdfe1
0x601020 <flag+16>:	0xa0818ef9	0xa1d19db1	0x8ee5adb0	0x0000bb9c
"""

from pwn import *

c = """b18de5aa cddeeabf c9acdfb9 819cdfe1 a0818ef9 a1d19db1 8ee5adb0 bb9c""".split(' ')
c2 = ""
for i in c:
    c2+=i.decode('hex')[::-1]

c = c2
key = "deadbeeeef".decode('hex')
flag = ""

for i in range(len(c)):
    flag += chr(ord(c[i])^ord(key[i%len(key)]))

print flag