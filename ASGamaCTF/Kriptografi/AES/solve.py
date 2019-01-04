from pwn import *

r = remote('asgama.web.id',42002)

r.recvuntil('kode rahasia : ')
kode = r.recvuntil('\n')[:-1]

r.recvuntil('IV-nya : ')
IV = r.recvuntil('\n')[:-1]
target = 'kamu_kok_gitu???'

IVbaru = xor(target,IV,kode)
r.recv()

r.sendline('2') # (2) IV
r.recvuntil('Masukan IV : ')
r.sendline(IVbaru)
print r.recv()