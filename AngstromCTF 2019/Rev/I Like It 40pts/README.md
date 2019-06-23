# __Angstrom CTF 2019__ 
## _I Like It_

## Information
**Category:** | **Points:** | **Writeup Author**
--- | --- | ---
Rev | 40 | l0l

**Description:** 

> 40points 609solves
> Now I like dollars, I like diamonds, I like ints, I like strings. Make Cardi like it please.
>
> Author: SirIan
>
> Given : [binary](./i_like_it)

**Hints:**

> Pop open a dissassembler or decompiler and check out the comparisons.
>

### I Like It
```
i_like_it: ELF 64-bit LSB executable, x86-64, version 1 (SYSV), dynamically linked, interpreter /lib64/ld-linux-x86-64.so.2, for GNU/Linux 2.6.32, BuildID[sha1]=5b91e9b31dffd010d9f32b21580ac3675db92a62, not stripped
```

```
...
   0x00000000004007c4 <+30>:	mov    edi,0x400978						# "I like the string that I'm thinking of: "
   0x00000000004007c9 <+35>:	call   0x400610 <puts@plt>
   0x00000000004007ce <+40>:	mov    rdx,QWORD PTR [rip+0x20089b]        	# 0x601070 <stdin@@GLIBC_2.2.5>
   0x00000000004007d5 <+47>:	lea    rax,[rbp-0x20]
   0x00000000004007d9 <+51>:	mov    esi,0x14
   0x00000000004007de <+56>:	mov    rdi,rax
   0x00000000004007e1 <+59>:	call   0x400660 <fgets@plt>
   0x00000000004007e6 <+64>:	lea    rax,[rbp-0x20]
   0x00000000004007ea <+68>:	mov    rdi,rax
   0x00000000004007ed <+71>:	call   0x400620 <strlen@plt>
   0x00000000004007f2 <+76>:	sub    rax,0x1
   0x00000000004007f6 <+80>:	mov    BYTE PTR [rbp+rax*1-0x20],0x0
   0x00000000004007fb <+85>:	lea    rax,[rbp-0x20]
   0x00000000004007ff <+89>:	mov    esi,0x4009a1						#"okrrrrrrr"
   0x0000000000400804 <+94>:	mov    rdi,rax
   0x0000000000400807 <+97>:	call   0x400670 <strcmp@plt>
   0x000000000040080c <+102>:	test   eax,eax
   0x000000000040080e <+104>:	je     0x400824 <main+126>
   0x0000000000400810 <+106>:	mov    edi,0x4009ab						# "Cardi don't like that."
   0x0000000000400815 <+111>:	call   0x400610 <puts@plt>
   0x000000000040081a <+116>:	mov    edi,0x0
   0x000000000040081f <+121>:	call   0x400690 <exit@plt>
   0x0000000000400824 <+126>:	mov    edi,0x4009c2						# "I said I like it like that!"
   0x0000000000400829 <+131>:	call   0x400610 <puts@plt>
   0x000000000040082e <+136>:	mov    edi,0x4009e0						# "I like two integers that I'm thinking of (space separated): "
   0x0000000000400833 <+141>:	call   0x400610 <puts@plt>
   0x0000000000400838 <+146>:	mov    rdx,QWORD PTR [rip+0x200831]        	# 0x601070 <stdin@@GLIBC_2.2.5>
   0x000000000040083f <+153>:	lea    rax,[rbp-0x30]
   0x0000000000400843 <+157>:	mov    esi,0xc
   0x0000000000400848 <+162>:	mov    rdi,rax
   0x000000000040084b <+165>:	call   0x400660 <fgets@plt>
   0x0000000000400850 <+170>:	lea    rcx,[rbp-0x34]
   0x0000000000400854 <+174>:	lea    rdx,[rbp-0x38]
   0x0000000000400858 <+178>:	lea    rax,[rbp-0x30]
   0x000000000040085c <+182>:	mov    esi,0x400a1d						# "%d %d"
   0x0000000000400861 <+187>:	mov    rdi,rax
   0x0000000000400864 <+190>:	mov    eax,0x0
   0x0000000000400869 <+195>:	call   0x400680 <__isoc99_sscanf@plt>
   0x000000000040086e <+200>:	mov    edx,DWORD PTR [rbp-0x38]
   0x0000000000400871 <+203>:	mov    eax,DWORD PTR [rbp-0x34]
   0x0000000000400874 <+206>:	add    eax,edx
   0x0000000000400876 <+208>:	cmp    eax,0x88
   0x000000000040087b <+213>:  jne    0x400897 <main+241>
   0x000000000040087d <+215>:	mov    edx,DWORD PTR [rbp-0x38]
   0x0000000000400880 <+218>:	mov    eax,DWORD PTR [rbp-0x34]
   0x0000000000400883 <+221>:	imul   eax,edx
   0x0000000000400886 <+224>:	cmp    eax,0xec7
   0x000000000040088b <+229>:	jne    0x400897 <main+241>
   0x000000000040088d <+231>:	mov    edx,DWORD PTR [rbp-0x38]
   0x0000000000400890 <+234>:	mov    eax,DWORD PTR [rbp-0x34]
   0x0000000000400893 <+237>:	cmp    edx,eax
   0x0000000000400895 <+239>:	jl     0x4008ab <main+261>
   0x0000000000400897 <+241>:	mov    edi,0x4009ab						# "Cardi don't like that."
   0x000000000040089c <+246>:	call   0x400610 <puts@plt>
   0x00000000004008a1 <+251>:	mov    edi,0x0
   0x00000000004008a6 <+256>:	call   0x400690 <exit@plt>
   0x00000000004008ab <+261>:	mov    edi,0x4009c2						# "I said I like it like that!"
   0x00000000004008b0 <+266>:	call   0x400610 <puts@plt>
   0x00000000004008b5 <+271>:	mov    ecx,DWORD PTR [rbp-0x34]
   0x00000000004008b8 <+274>:	mov    edx,DWORD PTR [rbp-0x38]
   0x00000000004008bb <+277>:	lea    rax,[rbp-0x20]
   0x00000000004008bf <+281>:	mov    rsi,rax
   0x00000000004008c2 <+284>:	mov    edi,0x400a23						# "Flag: actf{%s_%d_%d}\n"
   0x00000000004008c7 <+289>:	mov    eax,0x0
   0x00000000004008cc <+294>:	call   0x400640 <printf@plt>
   0x00000000004008d1 <+299>:	mov    eax,0x0
   0x00000000004008d6 <+304>:	mov    rcx,QWORD PTR [rbp-0x8]
   0x00000000004008da <+308>:	xor    rcx,QWORD PTR fs:0x28
   0x00000000004008e3 <+317>:	je     0x4008ea <main+324>
   0x00000000004008e5 <+319>:	call   0x400630 <__stack_chk_fail@plt>
   0x00000000004008ea <+324>:	leave  
   0x00000000004008eb <+325>:	ret    
```

#### Solve
Komparasi sederhana. Pada input pertama kita harus masukkan "okrrrrrrr". Lalu diminta memasukkan 2 bilangan yang jika dijumlahka hasilnya 0x88 (136) dan jika dikalikan hasilnya 0xec7 (3783). Cari saja dengan python : 

```
>>> for i in range(100):
...  for j in range(100):
...   if (i+j == 136 and i*j == 3783):
...    print i,j
...
39 97
97 39
```


### Payload
```
python2 -c "print 'okrrrrrrr\n39 97'" | ./i_like_it
I like the string that I'm thinking of:
I said I like it like that!
I like two integers that I'm thinking of (space separated):
I said I like it like that!
Flag: actf{okrrrrrrr_39_97}

```

### Flag 
actf{okrrrrrrr_39_97}