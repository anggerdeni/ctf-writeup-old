# __ASGama CTF__ 
## _Pixelated Binary_

## Information
**Category:** | **Points:** | **Writeup Author**
--- | --- | ---
Forensics | 80 | l0l

**Description:** 

> format flag CTF{}
>
> [PixelatedBinary](./soal5.jpg)

### Pixelated Binary  
Sesuai dengan judul soal, dugaan saya pada soal ini sebuah file diencoding menjadi gambar berdasarkan angka binernya.

### Payload
```py
from PIL import Image

im = Image.open("soal5.png")
w,h = im.size

data = ""

# read left-rigth top-bottom
# pixel 0 -> black -> 1 in binary

for i in range(h):
    for j in range(w):
        px = im.getpixel((j,i))
        if px == 0:
            data+='1'
        else: 
            data+='0'

data2=""
for i in range(len(data)/8):
    data2+=chr(int(data[i*8:i*8+8],2))

print data2.decode('base64')
```

### Result
```
$ python solve.py
Congratz, Here is the Flag : CTF{p1x3liz4t10n__is_n0t_4_big_d3al}
```

### Flag
CTF{p1x3liz4t10n__is_n0t_4_big_d3al}