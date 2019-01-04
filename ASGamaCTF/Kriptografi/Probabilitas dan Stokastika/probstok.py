#!/usr/bin/python
import random
import sys

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


flag = "< REDACTED >"
secret = [random.randint(3,225)]*9
RANDOM_BOX = []

try:
    ind_secret = int(raw_input("Masukan indeks untuk memasukan secret : "))
    assert ind_secret in range(len(flag))
except:
    print "error!"
    sys.exit(0)


for i in range(len(flag)):
    temp = [random.randint(0,255) for x in range(555)]
    if i == ind_secret:
        temp = temp[:-9] + secret
    RANDOM_BOX.append(temp)


print '''
Choose Option
1.)Get encrypted flag
2.)Encrypt a string
3.)Check flag
'''

while True:
    pilih = raw_input(">>> ").lower()
    if pilih == "1" or pilih == "2":
        try:
            jumlah = int(raw_input("Mau berapa kali ? : "))
            if jumlah > 5000 or jumlah < 1:
                sys.exit(0)
        except:
            print "error!"
            sys.exit(0)
        arr_cipher = []
        var = flag
        if pilih == "2":
            var = raw_input("Masukan plaintext : ")
            if len(var) != len(flag):
                print "Panjang plaintext harus sepanjang flag"
                break
        for n in range(jumlah):
            cipher = ""
            for indeks in range(len(var)):
                cipher += chr(ord(var[indeks]) ^ random.choice(RANDOM_BOX[indeks]))
            arr_cipher.append(cipher.encode("hex"))
        print "Ciphernya : {}".format(arr_cipher)
    elif pilih == "3":
        flag_input = raw_input("Masukan string flag : ")
        if flag_input == flag:
            print "Correct,your flag : GamaCTF{%s}" % flag
        else:
            print "WRONG !"
        break
    else:
        print "Invalid"
        break
