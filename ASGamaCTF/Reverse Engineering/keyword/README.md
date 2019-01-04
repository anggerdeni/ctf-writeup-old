# __ASGama CTF__ 
## _keyword_

## Information
**Category:** | **Points:** | **Writeup Author**
--- | --- | ---
Reverse Engineering | 30 | l0l

**Description:** 

> [kwd](./kwd)


### keyword
Diberikan sebuah executable binary file.  
`$ file kwd`  
`kwd: ELF 64-bit LSB shared object, x86-64, version 1 (SYSV), dynamically linked, interpreter /lib64/ld-linux-x86-64.so.2, for GNU/Linux 3.2.0, BuildID[sha1]=3d3e81c0d691bf19be9ca2f3821c6db28ad994d7, not stripped`

Coba run dulu programnya.  
`$ ./kwd`  
`Usage : ./kwd keyword`  

Membutuhkan keyword jadi kita masukkan sembarang keyword  
`$ ./kwd AAAA`  
`Nope`

Langkah pertama adalah mencari keyword dengan perintah `$ strings kwd`. Siapa tahu keyword dihardcode dalam program tanpa enkripsi.
```
.
.
.
AWAVI
AUATL
[]A\A]A^A_
Usage : %s keyword
PlZ_G1v3_m3_4_Fl46!!1!1
okay, take it :) => GamaCTF{%s}
Nope
;*3$"
.
.
.
```

String "PlZ_G1v3_m3_4_Fl46!!1!1" sepertinya adalah keyword yang dimaksud. Langsung coba saja eksekusi program dengan keyword ini. Dan jangan lupa untuk escape character '!'.  
`$ ./kwd PlZ_G1v3_m3_4_Fl46\!\!1\!1`
`okay, take it :) => GamaCTF{t1s_pR0b_iS_Tuuu_3z}`

Cara lainnya yang dapat kita coba adalah dengan menjalankan program dengan perintah `ltrace ./kwd` yang akan melakukan tracing terhadap semua pemanggilan fungsi dalam libc.

```
$ ltrace ./kwd AAAA
strcmp("AAAA", "PlZ_G1v3_m3_4_Fl46!!1!1")                                                                              = -15
puts("Nope"Nope
)                                                                                                           = 5

```

Terlihat argumen kita dibandingkan dengan string "PlZ_G1v3_m3_4_Fl46!!1!1" menggunakan fungsi strcmp.


### Payload
`$ ./kwd PlZ_G1v3_m3_4_Fl46\!\!1\!1`


### Result
`okay, take it :) => GamaCTF{t1s_pR0b_iS_Tuuu_3z}`

### Flag
GamaCTF{t1s_pR0b_iS_Tuuu_3z}