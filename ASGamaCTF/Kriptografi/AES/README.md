# __ASGama CTF__ 
## _AES_

## Information
**Category:** | **Points:** | **Writeup Author**
--- | --- | ---
Cryptography | 250 | l0l

**Description:** 

> Dekripsi lengkap ada di service ;)
>
> nc asgama.web.id 42002
> 
> [aes.py](./aes.py)


### AES
Ketika connect ke service : 
```
-------------------------------------------------------------BANK AES-------------------------------------------------------------------
Pada suatu hari Pak Gege ingin mengirimkan pesan rahasia kepada Pak Wepe,tetapi agar aman ia mengenkripsinya terlebih dahulu di BANK AES
Pak Gege ingin mengirim kode rahasia : e1c99f63c8ea7a90
Seorang petugas bank yang bernama Pak Setiawan usil ingin mengganti hasil dekripsi pesan ke Pak Wepe
Tetapi Pak Setiawan hanya memiliki wewenang mengganti ciphertext atau IV-nya
Bagaimana cara Pak Setiawan mengganti hasil dekripsi menjadi : kamu_kok_gitu???
Sementara Ciphernya(encoded hex) : 70e3ff32457388f17a71e780c68a60ba97d99cebf81528816c8033c494b5c9b3 dan IV-nya : 891ef2da2f319d53

Apa yang mau diganti ?
(1)Cipher
(2)IV
>>> 
```

#### main service
```py
while True:
    choice = raw_input(">>> ")
    if choice == "1":
        cipher_baru = raw_input("Masukan Ciper : ")
        if len(cipher_baru) % BLOCK_SIZE != 0:
            print "Masukan len cipher kelipatan block size !"
            continue
        dekripsi = decrypt(cipher_baru)
        check(dekripsi)
    if choice == "2":
        iv = raw_input("Masukan IV : ")
        if len(iv) % BLOCK_SIZE != 0:
            print "len IV harus 16 !"
            continue
        dekripsi = decrypt(cipher)
        check(dekripsi)
```

#### functions
```py
BLOCK_SIZE = AES.block_size
kode_rahasia = os.urandom(8).encode("hex")
iv = os.urandom(8).encode("hex")
key = os.urandom(8).encode("hex")
target = "kamu_kok_gitu???"

pad = lambda x : x + (chr(BLOCK_SIZE - (len(x) % BLOCK_SIZE)) * \
(BLOCK_SIZE - (len(x) % BLOCK_SIZE)) )
unpad = lambda y : y[:len(y) - ord(y[-1])]

def encrypt(plaintext):
   enc_obj = AES.new(key, AES.MODE_CBC, iv)
   ciphertext = enc_obj.encrypt(pad(plaintext))
   return ciphertext

def decrypt(ciphertext):
   dec_obj = AES.new(key, AES.MODE_CBC, iv)
   plaintext = dec_obj.decrypt(ciphertext)
   return unpad(plaintext)

def check(var):
    if var == target:
        print flag
        sys.exit(0)
    else:
        print "SALAH !!!!"

cipher = encrypt(kode_rahasia)
```

Intinya kita diperkenankan mengganti IV atau cipher agar hasil dekripsi menjadi `kamu_kok_gitu???`. Pilihan kedua (mengganti cipher) sepertinya tidak memungkinkan karena kita tidak memiliki clue sama sekali tentang key. Berarti kita hanya bisa mengubah IV.


Algoritma yang digunakan untuk enkripsi adalah AES dalam mode CBC. Enkripsi ini bertipe block cipher dimana plain text dibagi dalam beberapa block, lalu tiap block dienkrip berdasarkan hasil enkripsi block sebelumnya. Pada block pertama, sebelum dienkripsi, block itu terlebih dahulu di XOR dengan IV. 

Dengan demikian untuk mengubah hasil dekripsi dari cipher yang diberikan, kita hanya perlu mengubah IV dengan ketentuan sebagai berikut.

C1 = Cipher block 1  
P1 = Plain text block 1  
E  = Encrypt  
D  = Decrypt  

C1 = E(P1 ^ IV) => D(C1) = P1 ^ IV

P1 ^ IVLama = Target ^ IVBaru
IVBaru = P1 ^ IVLama ^ Target

Jika kita perhatikan, pesan yang dikirim adalah `kode rahasia` yang panjangnya tepat 1 block cipher. Sehingga kita akan mendapatkan 2 block cipher dengan block kedua hanya berisi padding.

Oleh karena itu, kita hanya perlu mengubah block pertama agar hasil dekripsi tidak kacau dan sesuai dengan keinginan dengan melakukan xor `kamu_kok_gitu???` dengan `kode rahasia` yang diberikan server.


### Payload
```py
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
```

### Result
```
$ python solve.py 
[+] Opening connection to asgama.web.id on port 42002: Done
GamaCTF{th3_L4st__Defen5e_0f_d4Ta_1s_ind33D_cRypt0__bruH}
```

### Flag
GamaCTF{th3_L4st__Defen5e_0f_d4Ta_1s_ind33D_cRypt0__bruH}