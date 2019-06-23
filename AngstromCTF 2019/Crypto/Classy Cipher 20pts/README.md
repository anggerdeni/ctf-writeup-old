# __Angstrom CTF 2019__ 
## _Classy Cipher_

## Information
**Category:** | **Points:** | **Writeup Author**
--- | --- | ---
Crypto | 20 | l0l

**Description:** 

> 20points 731 solves
> WEvery CTF starts off with a Caesar cipher, but we're more classy.
>
> Author: defund
>
> Given : [script](./classy_cipher.py)


### Classy Cipher
```py
from secret import flag, shift

def encrypt(d, s):
	e = ''
	for c in d:
		e += chr((ord(c)+s) % 0xff)
	return e

assert encrypt(flag, shift) == ':<M?TLH8<A:KFBG@V'
```

#### Solve
Enkripsi klasik biasa yaitu ROT, namun dirotate hingga 0xff.


### Payload
```py
from string import printable
c = ':<M?TLH8<A:KFBG@V'
for i in range(1,0x100):
   p = ''
   for j in c:
      p+=chr((ord(j)+0xff-i) % 0xff)
   # if all([x in printable] for x in p):
   #    print p
   if 'actf' in p:
      print p
```

### Flag 
actf{so_charming}