# __ASGama CTF__ 
## _1byte ROXy?_

## Information
**Category:** | **Points:** | **Writeup Author**
--- | --- | ---
Cryptography | 45 | l0l

**Description:** 

> e7c1cdc1e3f4e6dbcfcec5ffc2d9d4c5ffd8cfd2d29f9fdd

### 1 byte ROXy?
Dari judul soalnya, kemungkinan soal ini adalah XOR dengan key 1 byte. Dengan demikian kita harus melakukan brute force sebanyak 256 kali untuk masing-masing key yang mungkin.

### Payload
```py
from string import printable
f = open('soal','r').read()[:-1].decode('hex')

strings = []
for i in range(256):
 tmp = ''
 flag = True
 for j in f:
  tmp_chr = chr(ord(j)^i)
  if tmp_chr not in printable:
   flag = False
   break
  tmp+=tmp_chr
 if flag:
  strings.append(tmp)

for i in strings:
 print i
```

### Result
```
OS_SqftI]\WmPKFWmJ]@@
tR^RpguH\]VlQJGVlK\AA

                     N
sUYUw`rO[ZQkVM@QkL[FF

                     I
rTXTvasNZ[PjWLAPjMZGG

H
qW[WubpMYXSiTOBSiNYDD		K
GamaCTF{one_byte_xorr??}
F`l`BUGznod^cxud^ynss>>|
Dbnb@WExlmf\azwf\{lqq<<~
BdhdFQC~jk`Zg|q`Z}jww::x
OieiK\NsgfmWjq|mWpgzz77u
NhdhJ]OrfglVkp}lVqf{{66t
MkgkI^LqedoUhs~oUrexx55w
KmamOXJwcbiSnuxiStc~~33q
IocoMZHua`kQlwzkQva||11s
HnbnL[It`ajPmv{jPw`}}00r
Tr~rPGUh|}vLqjgvLk|aa,,n
SuyuW@Ro{zqKvm`qKl{ff++i
RtxtVASnz{pJwlapJmzgg**h
Qw{wUBPmyxsItobsInydd))k
PvzvTCQlxyrHuncrHoxee((j
_yuy[L^cwv}Gzal}G`wjj''e
^xtxZM_bvw|F{`m|Favkk&&d
\zvzXO]`tu~Dybo~Dctii$$f
[}q}_HZgsryC~ehyCdsnn##a
X~r~\KYdpqz@}fkz@gpmm  b
```

### Flag
GamaCTF{one_byte_xorr??}