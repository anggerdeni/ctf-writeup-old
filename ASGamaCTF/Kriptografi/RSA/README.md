# __ASGama CTF__ 
## _RSA_

## Information
**Category:** | **Points:** | **Writeup Author**
--- | --- | ---
Cryptography | 90 | l0l

**Description:** 

> latihan rsa gan
> 
> [enc_flag](./enc_flag)
> 
> [public_key.pem](./public_key.pem)


### RSA
Ini adalah challenge RSA basic. Dimana kita diberi public key dengan n yang cukup rendah. Hanya perlu load public key untuk mendapatkan n dan e (bisa dengan `python` atau command terminal `openssl`) lalu cari p dan q dengan [factordb](http://factordb.com/index.php?query=15719648961151124406259408275130518526692619002644355904409352031187)

### Payload
```py
from Crypto.PublicKey import RSA
from Crypto.Util.number import *

c = int(open("enc_flag",'r').read())

key = RSA.importKey(open("public_key.pem","rb"))
n = key.n
e = key.e
print "n = {}\ne = {}".format(n,e)

# Look for p and q at factordb
p = 3852454912858673504993326758109153
q = 4080423863932134851980426919817779

phi = (p-1)*(q-1)
d = inverse(e,phi)
print long_to_bytes(pow(c,d,n))
```

### Result
```
$ python solve.py
n = 15719648961151124406259408275130518526692619002644355904409352031187
e = 65537
GamaCTF{RSA_carry_the_world}
```

### Flag
GamaCTF{RSA_carry_the_world}
