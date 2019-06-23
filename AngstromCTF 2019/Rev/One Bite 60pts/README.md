# __Angstrom CTF 2019__ 
## _One Bite_

## Information
**Category:** | **Points:** | **Writeup Author**
--- | --- | ---
Rev | 60 | l0l

**Description:** 

> 60points 523 solves
> Whenever I have friends over, I love to brag about things that I can eat in a single bite. Can you give this program a tasty flag that fits the bill?
>
> Author: SirIan
>
> Given : [binary](./one_bite)

**Hints:**

> What else can be done with a single bite?
>

### One Bite
```
one_bite: ELF 64-bit LSB executable, x86-64, version 1 (SYSV), dynamically linked, interpreter /lib64/ld-linux-x86-64.so.2, for GNU/Linux 2.6.32, BuildID[sha1]=1378c7ef8cdf59c2cbe4d84274295b2567a09e91, not stripped
```

```
...
   0x00000000004006c5 <+31>:	mov    edi,0x400808                         # "Give me a flag to eat: "
   0x00000000004006ca <+36>:	call   0x400540 <puts@plt>
   0x00000000004006cf <+41>:	mov    rdx,QWORD PTR [rip+0x20098a]          # 0x601060 <stdin@@GLIBC_2.2.5>
   0x00000000004006d6 <+48>:	lea    rax,[rbp-0x40]
   0x00000000004006da <+52>:	mov    esi,0x22
   0x00000000004006df <+57>:	mov    rdi,rax
   0x00000000004006e2 <+60>:	call   0x400580 <fgets@plt>
   0x00000000004006e7 <+65>:	mov    DWORD PTR [rbp-0x4c],0x0
   0x00000000004006ee <+72>:	jmp    0x40070c <main+102>
   0x00000000004006f0 <+74>:	mov    eax,DWORD PTR [rbp-0x4c]
   0x00000000004006f3 <+77>:	cdqe   
   0x00000000004006f5 <+79>:	movzx  eax,BYTE PTR [rbp+rax*1-0x40]
   0x00000000004006fa <+84>:	xor    eax,0x3c
   0x00000000004006fd <+87>:	mov    edx,eax
   0x00000000004006ff <+89>:	mov    eax,DWORD PTR [rbp-0x4c]
   0x0000000000400702 <+92>:	cdqe   
   0x0000000000400704 <+94>:	mov    BYTE PTR [rbp+rax*1-0x40],dl
   0x0000000000400708 <+98>:	add    DWORD PTR [rbp-0x4c],0x1
   0x000000000040070c <+102>:	mov    eax,DWORD PTR [rbp-0x4c]
   0x000000000040070f <+105>:	movsxd rbx,eax
   0x0000000000400712 <+108>:	lea    rax,[rbp-0x40]
   0x0000000000400716 <+112>:	mov    rdi,rax
   0x0000000000400719 <+115>:	call   0x400550 <strlen@plt>
   0x000000000040071e <+120>:	cmp    rbx,rax
   0x0000000000400721 <+123>:	jb     0x4006f0 <main+74>
   0x0000000000400723 <+125>:	mov    QWORD PTR [rbp-0x48],0x400820           # "]_HZGUcHTURWcUQc[SUR[cHSc^YcOU_WA"
   0x000000000040072b <+133>:	mov    rdx,QWORD PTR [rbp-0x48]
   0x000000000040072f <+137>:	lea    rax,[rbp-0x40]
   0x0000000000400733 <+141>:	mov    rsi,rdx
   0x0000000000400736 <+144>:	mov    rdi,rax
   0x0000000000400739 <+147>:	call   0x400590 <strcmp@plt>
   0x000000000040073e <+152>:	test   eax,eax
   0x0000000000400740 <+154>:	jne    0x40074e <main+168>
   0x0000000000400742 <+156>:	mov    edi,0x400842
   0x0000000000400747 <+161>:	call   0x400540 <puts@plt>
   0x000000000040074c <+166>:	jmp    0x400758 <main+178>
   0x000000000040074e <+168>:	mov    edi,0x40085e
   0x0000000000400753 <+173>:	call   0x400540 <puts@plt>
...
```

#### Solve
Simple one-byte xor. Input kita di xor dengan 0x3c lalu hasilnya dibandingkan dengan "]_HZGUcHTURWcUQc[SUR[cHSc^YcOU_WA".


### Payload
```
>>> from pwn import xor
>>> xor("]_HZGUcHTURWcUQc[SUR[cHSc^YcOU_WA",0x3c)
'actf{i_think_im_going_to_be_sick}'
```

### Flag 
actf{i_think_im_going_to_be_sick}