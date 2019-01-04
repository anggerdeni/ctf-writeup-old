# __ASGama CTF__ 
## _Probabilitas dan Stokastika_

## Information
**Category:** | **Points:** | **Writeup Author**
--- | --- | ---
Cryptography | 300 | l0l

**Description:** 

> Pak Jihan adalah seorang dosen mata kuliah Probabilitas dan Stokastika.Untuk tujuan tugas akhir,mahasiswa diminta untuk menyelesaikan sebuah problem yang menggunakan proses randomisasi.Sebagai reward,jika berhasil maka nilai akhir manjadi A++.
>
> nc asgama.web.id 42001
> 
> [probstok.py](./probstok.py)


### Probabilitas dan Stokastika
Service ketika dijalankan :
```
$ nc asgama.web.id 42001
Masukan indeks untuk memasukan secret : 0

Choose Option
1.)Get encrypted flag
2.)Encrypt a string
3.)Check flag

>>> 1
Mau berapa kali ? : 1
Ciphernya : ['ca2cf76fdeb5630182d02b0fe84cd1ac8c277057940c482002f14e2e22']
>>> 2
Mau berapa kali ? : 1
Masukan plaintext : AAAAAAAAAAAAAAAAAAAAAAAAAAAAA
Ciphernya : ['add3801a826a2aea147132640b11352fa87579f9dde39ae88cb3739712'] 
```

Dilihat dari script servicenya, pertama service meminta user memasukkan index lalu menyiapkan random box sejumlah karakter flag (29 karakter) dengan box pada index yang dimasukkan user tadi diisi 9 angka yang dijamin sama ( meningkatkan peluang diambilnya angka tersebut ).

Lalu setiap karakter pada flag di xor dengan memilih angka random pada box dengan index yang sama dengan index karakter pada flag tersebut.

Disini kita diperkenankan memilih index, mengenkripsi string sendiri sebanyak maksimal 5000 kali, lalu mengenkripsi flag sebanyak maksimal 5000 kali.


### Payload
[solve.py](./solve.py)

### Result
```
.
.
.
.
Searching Flag..........
M0st_c0mmon_D3feat_Rand0m,
[*] Closed connection to asgama.web.id port 42001
Char at 26
[+] Opening connection to asgama.web.id on port 42001: Done
Searching Key..........
145
Searching Flag..........
M0st_c0mmon_D3feat_Rand0m,3
[*] Closed connection to asgama.web.id port 42001
Char at 27
[+] Opening connection to asgama.web.id on port 42001: Done
Searching Key..........
62
Searching Flag..........
M0st_c0mmon_D3feat_Rand0m,3s
[*] Closed connection to asgama.web.id port 42001
Char at 28
[+] Opening connection to asgama.web.id on port 42001: Done
Searching Key..........
145
Searching Flag..........
M0st_c0mmon_D3feat_Rand0m,3ss
[*] Closed connection to asgama.web.id port 42001
```

```
Masukan indeks untuk memasukan secret : 0

Choose Option
1.)Get encrypted flag
2.)Encrypt a string
3.)Check flag

>>> 3
Masukan string flag : M0st_c0mmon_D3feat_Rand0mn3ss
Correct,your flag : GamaCTF{M0st_c0mmon_D3feat_Rand0mn3ss}
```

### Flag
GamaCTF{M0st_c0mmon_D3feat_Rand0mn3ss}