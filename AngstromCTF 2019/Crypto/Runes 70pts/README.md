# __Angstrom CTF 2019__ 
## _Runes_

## Information
**Category:** | **Points:** | **Writeup Author**
--- | --- | ---
Crypto | 70 | l0l

**Description:** 

> 70points 244 solves
> The year is 20XX. ångstromCTF only has pwn challenges, and the winner is solely determined by who can establish a socket connection first. In the data remnants of an ancient hard disk, we've recovered a string of letters and digits. The only clue is the etching on the disk's surface: Paillier.
>
> Author: defund
>
> Given : [txt](./runes.txt)


### Runes
[Paillier cryptosystem](https://en.wikipedia.org/wiki/Paillier_cryptosystem)

```
n = 99157116611790833573985267443453374677300242114595736901854871276546481648883
g = 99157116611790833573985267443453374677300242114595736901854871276546481648884
c = 2433283484328067719826123652791700922735828879195114568755579061061723786565164234075183183699826399799223318790711772573290060335232568738641793425546869
```

#### Solve
Untuk dekripsi, pertama-tama kita harus mengetahui p dan q. Karena n yang cukup kecil, dapat dengan mudah kita faktorkan misalnya dengan [factordb](http://factordb.com/)

### Payload
```py
from gmpy import lcm,invert
from Crypto.Util.number import long_to_bytes
def L(x,n):
   return (x-1)/n

g = 99157116611790833573985267443453374677300242114595736901854871276546481648884
p = 310013024566643256138761337388255591613
q = 319848228152346890121384041219876391791
n = p*q
lambd = lcm(p-1,q-1)
myu = invert(L(pow(g,lambd,n**2),n),n)
c = 2433283484328067719826123652791700922735828879195114568755579061061723786565164234075183183699826399799223318790711772573290060335232568738641793425546869
m = (L(pow(c,lambd,n*n),n)*myu) %n

print long_to_bytes(m)

```


### Flag 
actf{crypto_lives}