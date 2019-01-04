from pwn import *
r = remote('asgama.web.id',40501)

# definisikan input password bebas asal panjangnya 0x14
password = 'A'*0x14

# hitung formulasi id untuk input di atas
kali = 1 # rbp+var_10
tambah = 0 # rbp+var_c

for i in range(len(password)):
    if (i%5==0): kali*=ord(password[i])
    else: tambah += ord(password[i])

r.recvuntil('Pass : ')
r.sendline(password)

r.recvuntil('ID : ')
r.sendline(str(kali-tambah))

print r.recvall()