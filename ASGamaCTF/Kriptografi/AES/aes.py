#!/usr/bin/python
import os, sys
from Crypto.Cipher import AES
flag = "< REDACTED >"

class Unbuffered(object):
   def __init__(self, stream):
       self.stream = stream
   def write(self, data):
       self.stream.write(data)
       self.stream.flush()
   def writelines(self, datas):
       self.stream.writelines(datas)
       self.stream.flush()
   def __getattr__(self, attr):
       return getattr(self.stream, attr)

sys.stdout = Unbuffered(sys.stdout)

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

print '''-------------------------------------------------------------BANK AES-------------------------------------------------------------------
Pada suatu hari Pak Gege ingin mengirimkan pesan rahasia kepada Pak Wepe,tetapi agar aman ia mengenkripsinya terlebih dahulu di BANK AES
Pak Gege ingin mengirim kode rahasia : {}
Seorang petugas bank yang bernama Pak Setiawan usil ingin mengganti hasil dekripsi pesan ke Pak Wepe
Tetapi Pak Setiawan hanya memiliki wewenang mengganti ciphertext atau IV-nya
Bagaimana cara Pak Setiawan mengganti hasil dekripsi menjadi : {}
Sementara Ciphernya(encoded hex) : {} dan IV-nya : {}'''.format(kode_rahasia,target,cipher.encode("hex"),iv)

print '''
Apa yang mau diganti ?
(1)Cipher
(2)IV'''

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

