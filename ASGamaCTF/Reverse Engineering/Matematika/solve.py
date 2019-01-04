text = """
movzx  eax,BYTE PTR [rax]
movsx  eax,al
add    eax,0x28
imul   eax,eax,0x6b
cmp    eax,0x4134
je     0x40118b <check+41>
mov    eax,0x0
jmp    0x4014fc <check+922>
mov    rax,QWORD PTR [rbp-0x8]
add    rax,0x1
movzx  eax,BYTE PTR [rax]
movsx  eax,al
add    eax,0x67
imul   eax,eax,0x65
cmp    eax,0x3d27
je     0x4011b0 <check+78>
mov    eax,0x0
jmp    0x4014fc <check+922>
mov    rax,QWORD PTR [rbp-0x8]
add    rax,0x2
movzx  eax,BYTE PTR [rax]
movsx  eax,al
add    eax,0x61
imul   eax,eax,0x74
cmp    eax,0x5d58
je     0x4011d5 <check+115>
mov    eax,0x0
jmp    0x4014fc <check+922>
mov    rax,QWORD PTR [rbp-0x8]
add    rax,0x3
movzx  eax,BYTE PTR [rax]
movsx  eax,al
add    eax,0x6b
imul   eax,eax,0x65
cmp    eax,0x3d8c
je     0x4011fa <check+152>
mov    eax,0x0
jmp    0x4014fc <check+922>
mov    rax,QWORD PTR [rbp-0x8]
add    rax,0x4
movzx  eax,BYTE PTR [rax]
movsx  eax,al
add    eax,0x20
imul   eax,eax,0x6d
cmp    eax,0x2357
je     0x40121f <check+189>
mov    eax,0x0
jmp    0x4014fc <check+922>
mov    rax,QWORD PTR [rbp-0x8]
add    rax,0x5
movzx  eax,BYTE PTR [rax]
movsx  eax,al
add    eax,0x6e
imul   eax,eax,0x75
cmp    eax,0x5e9b
je     0x401244 <check+226>
mov    eax,0x0
jmp    0x4014fc <check+922>
mov    rax,QWORD PTR [rbp-0x8]
add    rax,0x6
movzx  eax,BYTE PTR [rax]
movsx  eax,al
add    eax,0x61
shl    eax,0x5
cmp    eax,0x1520
je     0x401269 <check+263>
mov    eax,0x0
jmp    0x4014fc <check+922>
mov    rax,QWORD PTR [rbp-0x8]
add    rax,0x7
movzx  eax,BYTE PTR [rax]
movsx  eax,al
add    eax,0x6d
imul   eax,eax,0x70
cmp    eax,0x5940
je     0x40128e <check+300>
mov    eax,0x0
jmp    0x4014fc <check+922>
mov    rax,QWORD PTR [rbp-0x8]
add    rax,0x8
movzx  eax,BYTE PTR [rax]
movsx  eax,al
add    eax,0x62
imul   eax,eax,0x65
cmp    eax,0x4441
je     0x4012b3 <check+337>
mov    eax,0x0
jmp    0x4014fc <check+922>
mov    rax,QWORD PTR [rbp-0x8]
add    rax,0x9
movzx  eax,BYTE PTR [rax]
movsx  eax,al
add    eax,0x61
imul   eax,eax,0x73
cmp    eax,0x42ef
je     0x4012d8 <check+374>
mov    eax,0x0
jmp    0x4014fc <check+922>
mov    rax,QWORD PTR [rbp-0x8]
add    rax,0xa
movzx  eax,BYTE PTR [rax]
movsx  eax,al
add    eax,0x68
imul   eax,eax,0x61
cmp    eax,0x4434
je     0x4012fd <check+411>
mov    eax,0x0
jmp    0x4014fc <check+922>
mov    rax,QWORD PTR [rbp-0x8]
add    rax,0xb
movzx  eax,BYTE PTR [rax]
movsx  eax,al
add    eax,0x20
imul   eax,eax,0x6e
cmp    eax,0x22ce
je     0x401322 <check+448>
mov    eax,0x0
jmp    0x4014fc <check+922>
mov    rax,QWORD PTR [rbp-0x8]
add    rax,0xc
movzx  eax,BYTE PTR [rax]
movsx  eax,al
add    eax,0x70
shl    eax,0x5
cmp    eax,0x19e0
je     0x401347 <check+485>
mov    eax,0x0
jmp    0x4014fc <check+922>
mov    rax,QWORD PTR [rbp-0x8]
add    rax,0xd
movzx  eax,BYTE PTR [rax]
movsx  eax,al
add    eax,0x6f
imul   eax,eax,0x72
cmp    eax,0x5bbc
je     0x40136c <check+522>
mov    eax,0x0
jmp    0x4014fc <check+922>
mov    rax,QWORD PTR [rbp-0x8]
add    rax,0xe
movzx  eax,BYTE PTR [rax]
movsx  eax,al
add    eax,0x69
imul   eax,eax,0x61
cmp    eax,0x4434
je     0x401391 <check+559>
mov    eax,0x0
jmp    0x4014fc <check+922>
mov    rax,QWORD PTR [rbp-0x8]
add    rax,0xf
movzx  eax,BYTE PTR [rax]
movsx  eax,al
add    eax,0x6e
imul   eax,eax,0x68
cmp    eax,0x5c38
je     0x4013b6 <check+596>
mov    eax,0x0
jmp    0x4014fc <check+922>
mov    rax,QWORD PTR [rbp-0x8]
add    rax,0x10
movzx  eax,BYTE PTR [rax]
movsx  eax,al
add    eax,0x74
imul   eax,eax,0x61
cmp    eax,0x5726
je     0x4013db <check+633>
mov    eax,0x0
jmp    0x4014fc <check+922>
mov    rax,QWORD PTR [rbp-0x8]
add    rax,0x11
movzx  eax,BYTE PTR [rax]
movsx  eax,al
add    eax,0x20
imul   eax,eax,0x73
cmp    eax,0x25bc
je     0x401400 <check+670>
mov    eax,0x0
jmp    0x4014fc <check+922>
mov    rax,QWORD PTR [rbp-0x8]
add    rax,0x12
movzx  eax,BYTE PTR [rax]
movsx  eax,al
add    eax,0x79
imul   eax,eax,0x69
cmp    eax,0x5ebf
je     0x401425 <check+707>
mov    eax,0x0
jmp    0x4014fc <check+922>
mov    rax,QWORD PTR [rbp-0x8]
add    rax,0x13
movzx  eax,BYTE PTR [rax]
movsx  eax,al
add    eax,0x61
imul   eax,eax,0x61
cmp    eax,0x3937
je     0x40144a <check+744>
mov    eax,0x0
jmp    0x4014fc <check+922>
mov    rax,QWORD PTR [rbp-0x8]
add    rax,0x14
movzx  eax,BYTE PTR [rax]
movsx  eax,al
add    eax,0x61
shl    eax,0x5
cmp    eax,0x1800
je     0x40146f <check+781>
mov    eax,0x0
jmp    0x4014fc <check+922>
mov    rax,QWORD PTR [rbp-0x8]
add    rax,0x15
movzx  eax,BYTE PTR [rax]
movsx  eax,al
add    eax,0x20
imul   eax,eax,0x6e
cmp    eax,0x2a1c
je     0x401491 <check+815>
mov    eax,0x0
jmp    0x4014fc <check+922>
mov    rax,QWORD PTR [rbp-0x8]
add    rax,0x16
movzx  eax,BYTE PTR [rax]
movsx  eax,al
add    eax,0x3a
imul   eax,eax,0x69
cmp    eax,0x3f93
je     0x4014b3 <check+849>
mov    eax,0x0
jmp    0x4014fc <check+922>
mov    rax,QWORD PTR [rbp-0x8]
add    rax,0x17
movzx  eax,BYTE PTR [rax]
movsx  eax,al
add    eax,0x76
imul   eax,eax,0x68
cmp    eax,0x4cc8
je     0x4014d5 <check+883>
mov    eax,0x0
jmp    0x4014fc <check+922>
mov    rax,QWORD PTR [rbp-0x8]
add    rax,0x18
movzx  eax,BYTE PTR [rax]
movsx  eax,al
add    eax,0x29
shl    eax,0x5
cmp    eax,0xb40
""".replace('add    rax,0x','').split('je')

# replace 'add rax,0x' -> tambah index saja, jadi kita hilangkan

for i in range(len(text)):
    text[i] = text[i].split('\n')

flag = [' ']*0x19

for i in range(len(text)):
    result = int(text[i][-2].split('ax,')[-1][2:],16)
    for j in range(len(text[i])-1,-1,-1):
        if 'add' in text[i][j]:
            op = int(text[i][j].split('ax,')[-1][2:],16)
            result = result - op
        if 'imul' in text[i][j]:
            op = int(text[i][j].split('ax,')[-1][2:],16)
            result = result / op
        if 'shl' in text[i][j]:
            op = int(text[i][j].split('ax,')[-1][2:],16)
            result = result >> op
    flag[i] = chr(result)
flag = ''.join(flag)
print "Flag : GamaCTF{%s}" % (flag)