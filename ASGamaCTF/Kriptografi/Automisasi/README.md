# __ASGama CTF__ 
## _Automisasi_

## Information
**Category:** | **Points:** | **Writeup Author**
--- | --- | ---
Cryptography | 250 | l0l

**Description:** 

> Mas Burhan mendapati sequence string yang berisi angka-angka.Dia ingin mengembalikannya ke semula tetapi Dia bingung.Bantu Mas Burhan gan !
> 
> [encrypted](./encrypted)
> 
> [soal.py](./soal.py)


### Automisasi
Cukup gunakan algoritma enkripsi yang diberikan untuk bruteforce.


### Payload
```py
from string import printable

guess = "GamaCTF"
def enc(flag):
    encrypt = ''
    for x in range(len(flag)):
        for y in range(x):
            for z in range(y):
                encrypt+=str(ord(flag[z]) + ord(flag[x]) - ord(flag[y]))
    return encrypt

encrypted = open("encrypted","r").read()

counter = 0
while(True):
    if counter > len(guess): 
        break
    for i in printable:
        temp = guess+i
        cek = enc(temp)
        if(cek==encrypted[0:len(cek)]):
            guess = temp
            break
    counter+=1
print guess
```

### Result
```
$ python solve.py
GamaCTF{z3_wiLl_oWn_the_3qu4tion_l1ke_n0thing}
```

### Flag
GamaCTF{z3_wiLl_oWn_the_3qu4tion_l1ke_n0thing}
