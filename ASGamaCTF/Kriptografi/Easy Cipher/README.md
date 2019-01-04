# __ASGama CTF__ 
## _Easy Cipher_

## Information
**Category:** | **Points:** | **Writeup Author**
--- | --- | ---
Cryptography | 200 | l0l

**Description:** 

> Pak Sanul diberikan pesan yang terenkripsi beserta file untuk mengenkripsi. Bantu dia untuk mendekripsi pesannya.
> 
> [encrypt.py](./encrypt.py)
> 
> [encrypted.txt](./encrypted.txt)


### Easy Cipher
Diberikan sebuah algoritma enkripsi 
```py
if (len(flag) % len(key) != 0):
	n = len(key) - len(flag) % len(key)
	for i in range(n):
		flag += " "
h = []
for a in range(len(key)):
	i = a
	for b in range(len(flag)/len(key)):
		h.append(ord(flag[i])^ ord(key[a]))
		i += len(key)

encrypted = ""
for j in range(len(h)):
	encrypted +="%02x" % h[j]
```

Inti dari algoritma tersebut adalah: 
> Flag kita beri padding sehingga panjangnya merupakan kelipatan key
> Setiap karakter dixor dengan ketentuan: di xor dengan index ke [hasil modulo dari posisi karakter tersebut dengan panjang key]

Jadi:

char[0] akan dixor dengan key[0],
char[1] akan dixor dengan key[1],
.
.
.
char[len( key )*1+0 ] dixor dengan key[0]
char[len( key )*1+1 ] dixor dengan key[1]

Lalu hasilnya diurutkan berdasarkan urutan index key, hasil ciphernya adalah: 

char[0]:char[len(key) * 1+0]:char[len(key) * 2+0]...


### Payload
```py
c = open("encrypted.txt",'r').read().decode('hex')

key = "Qk3j4cnmb8"
flag = [' ' for i in range(len(c))]

for i in range(len(key)):
    a = i
    for j in range(len(flag)/len(key)):
        flag[a] = chr(ord(c[i*(len(flag)/len(key))+j])^ord(key[i]))
        a+=len(key)

print ''.join(flag)
```

### Result
```
$ python solve.py
GamaCTF{1ts_n0t_an_0rdin4ry_XOR}
```

### Flag
GamaCTF{1ts_n0t_an_0rdin4ry_XOR}
