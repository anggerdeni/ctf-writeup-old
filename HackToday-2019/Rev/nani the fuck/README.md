# nani the fuk
## 490 points | 3 solves
### Description
> aku dimana?  
> unrelated: https://www.youtube.com/watch?v=1AhDtMxwnvI  
> https://challs.codepwnda.id/rev/nanithefuk.zip  
> author: circleous  

Diberikan stripped binary.
```
$ file nani-the-fuk
nani-the-fuk: ELF 64-bit LSB pie executable, x86-64, version 1 (SYSV), dynamically linked, interpreter /lib64/ld-linux-x86-64.so.2, BuildID[sha1]=9322119a59e371fe62297edfc1cb83cdb0d525ca, for GNU/Linux 3.2.0, stripped

gdb-peda$ checksec
CANARY    : disabled
FORTIFY   : disabled
NX        : ENABLED
PIE       : ENABLED
RELRO     : Partial
```

Setelah melakukan debuggin dari gdb, diketahui main program berada pada offset 0x555555555e50 - 0x555555555080 dari entry point, yaitu 0xdd0 dari entry point, dalam kasus ini offset '0x1e50'. Langsung bongkar pake ghidra

```c
undefined8 FUN_00101e50(void)

{
  real_main(); // sudah direname
  return 0;
}


void real_main(void)
{
  syscall(1,1,"aku dimana?\n",0xd);
  malloc_pertama = malloc(0x1d);
  FUN_00101226();
  FUN_00101d76();
  return;
}

void FUN_00101226(void)

{
  memset(&DAT_001040a0,0,0x98);
  sigemptyset((sigset_t *)&DAT_001040a8);
  _DAT_001040a0 = FUN_001011f7;
  _DAT_00104128 = 4;
  sigaction(8,(sigaction *)&DAT_001040a0,(sigaction *)0x0);
  return;
}

void FUN_00101d76(void)
{
  uint uVar1;
  uint extraout_var;
  bool in_ZF;
  
  if ((!in_ZF) && (in_ZF)) {
    func_0x059d6646();
                    /* WARNING: Bad instruction - Truncating control flow here */
    halt_baddata();
  }
  DAT_00104080 = FUN_00101cdd;
  syscall(1,1,&UNK_00102030,0xe);
  syscall(0,0,DAT_00104068,2);
  uVar1 = (int)*DAT_00104068 << 3 ^ 0x398;
  syscall(0x3c,0xff / (long)(int)uVar1 & 0xffffffff,
          0xff % (long)(int)uVar1 & 0xffffffffU | (ulong)extraout_var << 0x20,(ulong)uVar1);
  return;
}

void FUN_001011f7(undefined8 uParm1,undefined8 uParm2,long lParm3)
{
  *(undefined8 *)(lParm3 + 0xa8) = DAT_00104080;
  return;
}
```

```c
int sigaction(int signum, const struct sigaction *act,struct sigaction *oldact);
```
> The `sigaction()` system call is used to change the action taken by a process on receipt of a specific signal.  (See signal(7) for an overview of signals.)  
> signum specifies the signal and can be any valid signal except SIGKILL and SIGSTOP.  
> If act is non-NULL, the new action for signal signum is installed from act.
> If oldact is non-NULL, the previous action is saved in oldact.  

`sigemptyset()` initializes the signal set given by set to empty, with all signals excluded from the set.

Hmm, dari sini kita lihat bahwa signal(8), `SIGFPE`, yang biasanya muncul ketika ada computational error seperti division by zero.  
```c
void FUN_00101226(void)
{
  memset(&DAT_001040a0,0,0x98);
  sigemptyset((sigset_t *)&DAT_001040a8);
  _DAT_001040a0 = FUN_001011f7;
  _DAT_00104128 = 4;
  sigaction(8,(sigaction *)&DAT_001040a0,(sigaction *)0x0);
  return;
}
```

Dari debugging diketahui bahwa malloc pertama digunakan untuk menyimpan input, misal input = '1\n' disimpan \x0a\x31, lalu hanya diambil 0x31 saja ketika diprosess di `uVar1 = (int)*malloc_pertama << 3 ^ 0x398;` 


```
Dump of assembler code from 0x555555555dd1 to 0x555555555dff::  Dump of assembler code from 0x555555555dd1 to 0x555555555dff:
   0x0000555555555dd1:  mov    rax,QWORD PTR [rip+0x2290]        # 0x555555558068
   0x0000555555555dd8:  movzx  eax,BYTE PTR [rax]
   0x0000555555555ddb:  movsx  eax,al
   0x0000555555555dde:  shl    eax,0x3
   0x0000555555555de1:  xor    eax,0x398
   0x0000555555555de6:  mov    ecx,eax
   0x0000555555555de8:  mov    eax,0xff
   0x0000555555555ded:  cdq
   0x0000555555555dee:  idiv   ecx
   0x0000555555555df0:  mov    esi,eax
   0x0000555555555df2:  mov    edi,0x3c
   0x0000555555555df7:  mov    eax,0x0
=> 0x0000555555555dfc:  call   0x555555555050 <syscall@plt>

```

Berdasarkan table [ini](https://filippo.io/linux-syscall-table/), syscal 0x3c (60) yang dipanggil di atas adalah exit, jadi kita ingin menghindari ini. Terlihat juga nilai 0xff akan dibagi dengan input << 3 ^ 0x398, jika kita bisa mengset nilai ini menjadi 0 maka akan terjadi division by zero sehingga terpanggil `SIGFPE`, yang sampai sekarang kita belum tau apa yang dia lakukan, 

```py
>>> 0x398 ^ 0
920
>>> 920 >> 3
115
>>> hex(115)
'0x73'
>>> chr(115)
's'
```

Jika kita run di gbd hasilnya program berhenti: 
```
Legend: code, data, rodata, value
Stopped reason: SIGFPE
0x0000555555555dee in ?? ()
```

Namun dapat kita teruskan dengan command `ni`.
Dan jika kita run di luar gdb program mengeksekusi fungsi yang mengoverwrite SIGFPE dengan lancar dan point kita bertambah. Sepertinya jika kita bisa memastikan bahwa division by zero terjadi sebanyak 20 kali kita akan mendapatkan flag: 
```
$ ./nani-the-fuk
aku dimana?
(01/20) ???? s
(02/20) ????
```

Setelah debugging, dengan memasukkan nilai-nilai yang benar, ternyata fungsi yang dilakukan untuk mengecek input berbeda-beda, dan untungnya address fungsinya berurutan mulai dari paling bawah (FUN_00101d76):  
> 0x1d76 => uVar1 = (int)*malloc_pertama << 3 ^ 0x398;  
> 0x1cdd => uVar1 = (int)*(char *)(malloc_pertama + 1) * 5 - 0xf5;  
> 0x1c43 => uVar1 = (int)*(char *)(malloc_pertama + 2) * 7 ^ 0x2d1;  
> 0x1bb4 => uVar1 = SEXT14((char)(*(byte *)(malloc_pertama + 3) ^ 0x5f));  
> 0x1b25 => uVar1 = SEXT14((char)(*(byte *)(malloc_pertama + 4) ^ 99));  
> xxxxxx => uVar1 = (int)*(char *)(malloc_pertama + 5) << 2 ^ 0xc0;  
> xxxxxx => uVar1 = (int)*(char *)(malloc_pertama + 6) * 10 ^ 0x44c;  
> xxxxxx => uVar1 = SEXT14((char)(*(byte *)(malloc_pertama + 7) ^ 0x74));  
> xxxxxx => uVar1 = (int)*(char *)(malloc_pertama + 8) * 9 ^ 999;  
> xxxxxx => uVar1 = SEXT14((char)((char)(*(byte *)(malloc_pertama + 9) + (*(byte *)(malloc_pertama + 9) >> 7))>> 1 ^ 0x39));  
> xxxxxx => uVar1 = (int)*(char *)(malloc_pertama + 10) - 0x6c;  
> xxxxxx => uVar1 = SEXT14((char)(*(byte *)(malloc_pertama + 0xb) ^ 0x5f));  
> xxxxxx => uVar1 = SEXT14((char)(*(byte *)(malloc_pertama + 0xc) ^ 0x66));  
> xxxxxx => uVar1 = (int)*(char *)(malloc_pertama + 0xd) * 6 ^ 0x288;  
> xxxxxx => uVar1 = (int)*(char *)(malloc_pertama + 0xe) + 5U ^ 0x35;  
> xxxxxx => uVar1 = (int)*(char *)(malloc_pertama + 0xf) << 3 ^ 0x3b8;  
> xxxxxx => uVar1 = SEXT14((char)(*(byte *)(malloc_pertama + 0x10) ^ 0x5f));  
> xxxxxx => uVar1 = (int)*(char *)(malloc_pertama + 0x11) - 0x20U ^ 0x58;  
> xxxxxx => uVar1 = (int)*(char *)(malloc_pertama + 0x12) + 0x20U ^ 100;  
> xxxxxx => uVar1 = SEXT14((char)(*(byte *)(malloc_pertama + 0x13) ^ 0x5f));  


Tinggal koding:
```py
from sys import stdout
#1
for i in range(0x100):
    if (i<<3 ^ 0x398) == 0: stdout.write(chr(i))

#2
for i in range(0x100):
    if(i*5 - 0xf5) == 0: stdout.write(chr(i))

#3
for i in range(0x100):
    if(i*7 ^ 0x2d1) == 0: stdout.write(chr(i))

#4
for i in range(0x100):
    if(i ^ 0x5f) == 0: stdout.write(chr(i))

#5
for i in range(0x100):
    if(i^99) == 0: stdout.write(chr(i))

#6
for i in range(0x100):
    if((i<<2) ^ 0xc0) == 0: stdout.write(chr(i))

#7
for i in range(0x100):
    if(i*10 ^ 0x44c) == 0: stdout.write(chr(i))

#8
for i in range(0x100):
    if(i^ 0x74) == 0: stdout.write(chr(i))

#9
for i in range(0x100):
    if(i*9 ^ 999) == 0: stdout.write(chr(i))

#10
for i in range(0x100):
    if( (i + (i>> 7))>> 1 ^ 0x39) == 0: stdout.write(chr(i))

#11
for i in range(0x100):
    if(i - 0x6c) == 0: stdout.write(chr(i))

#12
for i in range(0x100):
    if(i^ 0x5f) == 0: stdout.write(chr(i))

#13
for i in range(0x100):
    if(i^ 0x66) == 0: stdout.write(chr(i))

#14
for i in range(0x100):
    if(i * 6 ^ 0x288) == 0: stdout.write(chr(i))

#15
for i in range(0x100):
    if(i + 5 ^ 0x35) == 0: stdout.write(chr(i))

#16
for i in range(0x100):
    if(i << 3 ^ 0x3b8) == 0: stdout.write(chr(i))

#17
for i in range(0x100):
    if(i ^ 0x5f) == 0: stdout.write(chr(i))

#18
for i in range(0x100):
    if(i - 0x20 ^ 0x58) == 0: stdout.write(chr(i))

#19
for i in range(0x100):
    if(i + 0x20 ^ 100) == 0: stdout.write(chr(i))

#20
for i in range(0x100):
    if(i ^ 0x5f) == 0: stdout.write(chr(i))

```

Setelah dirun, anehnya kita mendapat 21 karakter: 
`s1g_c0ntorsl_fl0w_xD_`  
Lalu coba masukkan satu per satu, error pada input ke 11.  
```
$ ./nani-the-fuk
aku dimana?
(01/20) ???? s
(02/20) ???? 1
(03/20) ???? g
(04/20) ???? _
(05/20) ???? c
(06/20) ???? 0
(07/20) ???? n
(08/20) ???? t
(09/20) ???? o
(10/20) ???? r
(11/20) ???? s
[l0l@l0l hacktoday]$

```

Coba hilangkan s-nya, : 
```
$ ./nani-the-fuk
aku dimana?
(01/20) ???? s
(02/20) ???? 1
(03/20) ???? g
(04/20) ???? _
(05/20) ???? c
(06/20) ???? 0
(07/20) ???? n
(08/20) ???? t
(09/20) ???? o
(10/20) ???? r
(11/20) ???? l
(12/20) ???? _
(13/20) ???? f
(14/20) ???? l
(15/20) ???? 0
(16/20) ???? w
(17/20) ???? _
(18/20) ???? x
(19/20) ???? D
(20/20) ???? _

hacktoday{s1g_c0ntorl_fl0w_xD_}
??????????????????????
```

### Flag 
hacktoday{s1g_c0ntorl_fl0w_xD_}