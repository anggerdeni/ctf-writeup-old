# __ASGama CTF__ 
## _M4th_

## Information
**Category:** | **Points:** | **Writeup Author**
--- | --- | ---
Reverse Engineering | 250 | l0l

**Description:** 

> Mirip matematika, cuma lebih kerad
>
> [M4th](./M4th)


### M4th

#### file
```
$ file M4Th 
M4Th: ELF 64-bit LSB executable, x86-64, version 1 (SYSV), dynamically linked, interpreter /lib64/ld-linux-x86-64.so.2, for GNU/Linux 3.2.0, BuildID[sha1]=13b4988788c67e17f2d9e8a2dc1674f70cfe335b, not stripped
```

#### info function
```
gdb-peda$ info func
All defined functions:

Non-debugging symbols:
.
.
0x0000000000401162  level_1
0x00000000004012f7  level_2
0x00000000004015c4  level_3
0x00000000004018c9  level_4
0x0000000000401cd2  level_5
0x0000000000401db7  main
.
.
```

Seperti yang terlihat ada 5 level di program ini. 

#### main
```
gdb-peda$ pdisass main
Dump of assembler code for function main:
   0x0000000000401db7 <+0>:	push   rbp
   0x0000000000401db8 <+1>:	mov    rbp,rsp
   0x0000000000401dbb <+4>:	sub    rsp,0x120
   0x0000000000401dc2 <+11>:	mov    rax,QWORD PTR fs:0x28
   0x0000000000401dcb <+20>:	mov    QWORD PTR [rbp-0x8],rax
   0x0000000000401dcf <+24>:	xor    eax,eax
   0x0000000000401dd1 <+26>:	mov    DWORD PTR [rbp-0x114],0x0
   0x0000000000401ddb <+36>:	lea    rdi,[rip+0x1226]        # 0x403008
   0x0000000000401de2 <+43>:	mov    eax,0x0
   0x0000000000401de7 <+48>:	call   0x401060 <printf@plt>

   # input kita disimpan pada [rbp-0x40]
   0x0000000000401dec <+53>:	lea    rax,[rbp-0x40]
   0x0000000000401df0 <+57>:	mov    rsi,rax
   0x0000000000401df3 <+60>:	lea    rdi,[rip+0x1219]        # 0x403013
   0x0000000000401dfa <+67>:	mov    eax,0x0
   0x0000000000401dff <+72>:	call   0x401070 <__isoc99_scanf@plt>
   0x0000000000401e04 <+77>:	lea    rax,[rbp-0x40]

   # Cek panjang string : harus 0x32
   0x0000000000401e08 <+81>:	mov    rdi,rax
   0x0000000000401e0b <+84>:	call   0x401040 <strlen@plt>
   0x0000000000401e10 <+89>:	cmp    rax,0x32
   0x0000000000401e14 <+93>:	je     0x401e2c <main+117>
   0x0000000000401e16 <+95>:	lea    rdi,[rip+0x11fb]        # 0x403018 : "no!"
   0x0000000000401e1d <+102>:	call   0x401030 <puts@plt>
   0x0000000000401e22 <+107>:	mov    eax,0x0
   0x0000000000401e27 <+112>:	jmp    0x401f7c <main+453>


   0x0000000000401e2c <+117>:	mov    DWORD PTR [rbp-0x11c],0x0
   0x0000000000401e36 <+127>:	jmp    0x401e90 <main+217>
   0x0000000000401e38 <+129>:	mov    DWORD PTR [rbp-0x118],0x0

    # [rbp-0x118] * 5 lalu ditambah [rbp-0x11c]
    # input[j*5 + i] -> masukkan ke char ke-k ([rbp-0x114]) pada [rbp-0x110]
    0x0000000000401e42 <+139>:	jmp    0x401e80 <main+201>
    0x0000000000401e44 <+141>:	mov    edx,DWORD PTR [rbp-0x118]
    0x0000000000401e4a <+147>:	mov    eax,edx
    0x0000000000401e4c <+149>:	shl    eax,0x2
    0x0000000000401e4f <+152>:	add    edx,eax
    0x0000000000401e51 <+154>:	mov    eax,DWORD PTR [rbp-0x11c]
    0x0000000000401e57 <+160>:	add    eax,edx
    0x0000000000401e59 <+162>:	cdqe   
    0x0000000000401e5b <+164>:	movzx  eax,BYTE PTR [rbp+rax*1-0x40]
    0x0000000000401e60 <+169>:	movsx  edx,al
    0x0000000000401e63 <+172>:	mov    eax,DWORD PTR [rbp-0x114]
    0x0000000000401e69 <+178>:	cdqe   
    0x0000000000401e6b <+180>:	mov    DWORD PTR [rbp+rax*4-0x110],edx
    0x0000000000401e72 <+187>:	add    DWORD PTR [rbp-0x114],0x1          # index string hasil+=1 
    0x0000000000401e79 <+194>:	add    DWORD PTR [rbp-0x118],0x1          # j+=1
    0x0000000000401e80 <+201>:	cmp    DWORD PTR [rbp-0x118],0x9
    0x0000000000401e87 <+208>:	jle    0x401e44 <main+141>

   0x0000000000401e89 <+210>:	add    DWORD PTR [rbp-0x11c],0x1          # i+=1
   0x0000000000401e90 <+217>:	cmp    DWORD PTR [rbp-0x11c],0x4 
   0x0000000000401e97 <+224>:	jle    0x401e38 <main+129>

   


   0x0000000000401e99 <+226>:	lea    rax,[rbp-0x110]
   0x0000000000401ea0 <+233>:	mov    rdi,rax
   0x0000000000401ea3 <+236>:	call   0x401162 <level_1>
   0x0000000000401ea8 <+241>:	test   eax,eax
   0x0000000000401eaa <+243>:	je     0x401f6b <main+436>
   0x0000000000401eb0 <+249>:	lea    rax,[rbp-0x110]
   0x0000000000401eb7 <+256>:	mov    rdi,rax
   0x0000000000401eba <+259>:	call   0x4012f7 <level_2>
   0x0000000000401ebf <+264>:	test   eax,eax
   0x0000000000401ec1 <+266>:	je     0x401f58 <main+417>
   0x0000000000401ec7 <+272>:	lea    rax,[rbp-0x110]
   0x0000000000401ece <+279>:	mov    rdi,rax
   0x0000000000401ed1 <+282>:	call   0x4015c4 <level_3>
   0x0000000000401ed6 <+287>:	test   eax,eax
   0x0000000000401ed8 <+289>:	je     0x401f45 <main+398>
   0x0000000000401eda <+291>:	lea    rax,[rbp-0x110]
   0x0000000000401ee1 <+298>:	mov    rdi,rax
   0x0000000000401ee4 <+301>:	call   0x4018c9 <level_4>
   0x0000000000401ee9 <+306>:	test   eax,eax
   0x0000000000401eeb <+308>:	je     0x401f32 <main+379>
   0x0000000000401eed <+310>:	lea    rax,[rbp-0x110]
   0x0000000000401ef4 <+317>:	mov    rdi,rax
   0x0000000000401ef7 <+320>:	call   0x401cd2 <level_5>
   0x0000000000401efc <+325>:	test   eax,eax
   0x0000000000401efe <+327>:	je     0x401f1f <main+360>
   0x0000000000401f00 <+329>:	lea    rax,[rbp-0x40]
   0x0000000000401f04 <+333>:	mov    rsi,rax
   0x0000000000401f07 <+336>:	lea    rdi,[rip+0x1112]        # 0x403020 : "Mantab!\nNih flagnya ==> GamaCTF{%s}\n"
   0x0000000000401f0e <+343>:	mov    eax,0x0
   0x0000000000401f13 <+348>:	call   0x401060 <printf@plt>
   0x0000000000401f18 <+353>:	mov    eax,0x0
   0x0000000000401f1d <+358>:	jmp    0x401f7c <main+453>
   0x0000000000401f1f <+360>:	lea    rdi,[rip+0x111f]        # 0x403045
   0x0000000000401f26 <+367>:	call   0x401030 <puts@plt>
   0x0000000000401f2b <+372>:	mov    eax,0x0
   0x0000000000401f30 <+377>:	jmp    0x401f7c <main+453>
   0x0000000000401f32 <+379>:	lea    rdi,[rip+0x1126]        # 0x40305f
   0x0000000000401f39 <+386>:	call   0x401030 <puts@plt>
   0x0000000000401f3e <+391>:	mov    eax,0x0
   0x0000000000401f43 <+396>:	jmp    0x401f7c <main+453>
   0x0000000000401f45 <+398>:	lea    rdi,[rip+0x1128]        # 0x403074
   0x0000000000401f4c <+405>:	call   0x401030 <puts@plt>
   0x0000000000401f51 <+410>:	mov    eax,0x0
   0x0000000000401f56 <+415>:	jmp    0x401f7c <main+453>
   0x0000000000401f58 <+417>:	lea    rdi,[rip+0x1125]        # 0x403084
   0x0000000000401f5f <+424>:	call   0x401030 <puts@plt>
   0x0000000000401f64 <+429>:	mov    eax,0x0
   0x0000000000401f69 <+434>:	jmp    0x401f7c <main+453>
   0x0000000000401f6b <+436>:	lea    rdi,[rip+0x111d]        # 0x40308f
   0x0000000000401f72 <+443>:	call   0x401030 <puts@plt>
   0x0000000000401f77 <+448>:	mov    eax,0x0

   # close
   0x0000000000401f7c <+453>:	mov    rcx,QWORD PTR [rbp-0x8]
   0x0000000000401f80 <+457>:	xor    rcx,QWORD PTR fs:0x28
   0x0000000000401f89 <+466>:	je     0x401f90 <main+473>
   0x0000000000401f8b <+468>:	call   0x401050 <__stack_chk_fail@plt>
   0x0000000000401f90 <+473>:	leave  
   0x0000000000401f91 <+474>:	ret    
End of assembler dump.
```

Pertama-tama program meminta input yang disimpan pada address `[rbp-0x40]`. Kemudian input kita dicek panjang nya apakah 0x32. Setelah itu program looping untuk melakukan pengacakan string yang jika diterjemahkan ke bahasa python jadi seperti ini:

```py
k = 0
for i in range(5):
  for j in range(10):
    hasil[k] = asli[j*5 + i]
    k+=1
```

Jadi misal input kita adalah "ABCDE"*0x32, hasilnya menjadi "AAAAAAAAAABBBBBBBBBBCCCCCCCCCCDDDDDDDDDDEEEEEEEEEE". Hasilnya disimpan pada `[rbp-0x110]` dengan catatan setiap karakter disimpan dalam memory berukuran word, bukan char. Jadi jarak antar karakter adalah 4 bytes.

Selanjutnya, program masuk berurutan ke fungsi `level1`,`level2`,`level3`,`level4`,`level5` dengan catatan fungsi sebelumnya return valuenya bukan 0. Jika berhasil melewati semua level, maka flag akan dicetak.

Mirip dengan soal [Matematika](../Matematika/README.md), hanya saja pengecekannya jauh lebih banyak. Hanya perlu masukkan ke z3-solver.

### Payload
[solve.py](./solve.py)

### Result
```
$ python solve.py
M4Th_15_lYf3_M4Th_15_L0p3eEe__M4Th_5Ur3E_i1SS5_FuN
```

```
$ ./M4Th 
M4Th???
> M4Th_15_lYf3_M4Th_15_L0p3eEe__M4Th_5Ur3E_i1SS5_FuN
Mantab!
Nih flagnya ==> GamaCTF{M4Th_15_lYf3_M4Th_15_L0p3eEe__M4Th_5Ur3E_i1SS5_FuN}
```

### Flag
GamaCTF{M4Th_15_lYf3_M4Th_15_L0p3eEe__M4Th_5Ur3E_i1SS5_FuN}