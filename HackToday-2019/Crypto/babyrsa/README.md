# babyrsa
## 410 points | 7 solves

### Description
> Wait a minute.. I see something unusual  
> author: deomkicer

Diberikan dua buah file [babyrsa.py](./challenge/babyrsa.py) dan [flag.enc](./challenge/flag.enc).  
File pertama berisi algoritma (RSA) yang digunakan untuk mengenkripsi file flag, sedangkan yang kedua adalah hasil enkripsi itu sendiri.  
Sedikit berbeda dari RSA biasanya, setelah file flag dibuka lalu diencode `hex`, hasilnya diinterpretasikan ke integer namun dianggap sebagai base `0x16` yaitu base-22. Bukan sebagai base-16.
```py 
m = int(flag.encode("hex"), 0x16)
```
Pemilihan n juga sedikit unik, dimana 0x54012066b18843995165c3c0d783aa9e31e796f6928ea4bfe0728b1d1bad6271 setelah difaktorkan di [factordb](http://factordb.com/index.php?query=37996269752553143762620204978239299540564965267273808381787520677145280864881&use=x&x=1&b=1&d=1&VP=on&VC=on&EV=on&OD=on&PR=on&FF=on&PRP=on&CF=on&U=on&C=on&perpage=20&format=1), ternyata memiliki 4 faktor prima.  
`FF 	77 (show) 	(194926318778540379438386258755918352359<39>)^2 = (11630107594679429833<20> · 16760491439280901423<20>)^2`

Dari sini kita ketahui bahwa n tersusun dari 11630107594679429833^2 * 16760491439280901423^2.
Kemudian berdasarkan rumus dari [wikipedia](https://en.wikipedia.org/wiki/Carmichael_function), untuk menghitung nilai totient dari suatu bilangan n, dimana `n = p1**(r1) * p2**(r2) ....`,  dapat kita gunakan rumus:   
`totient(n) = lcm(totient(p1**r1), totient(p2**r2), ....)`

```Carmichael's theorem explains how to compute λ of a prime power p**r: for a power of an odd prime and for 2 and 4, λ(p**r) is equal to the Euler totient φ(p**r); for powers of 2 greater than 4 it is equal to half of the Euler totient. ```

Karena p dan q prima, maka `λ(p) = φ(p**r)` dan `λ(q) = φ(q**r)`.  
Euler's function for prime powers p**r is given by:  
`φ(p**r) = p**(r-1) (p-1)`

Maka `λ(n) = lcm(λ(p**2), λ(q**2)) = lcm(φ(p**r),φ(q**r)) = lcm(p*(p-1), q*(q-1))`


Dengan begitu dapat kita buat script solver nya

```py
from Crypto.Util.number import inverse
from gmpy2 import lcm, gcd

def int2base(a, base, numerals="0123456789abcdefghijklmnopqrstuvwxyz"):
    baseit = lambda a=a, b=base: (not a) and numerals[0]  or baseit(a-a%b,b*base)+numerals[a%b%(base-1) or (a%b) and (base-1)]
    return baseit()

p = 11630107594679429833
q = 16760491439280901423
c = 34800025394951925292080924856671179486606568805409940926874542700517211148095
n = 0x54012066b18843995165c3c0d783aa9e31e796f6928ea4bfe0728b1d1bad6271
e = 0x10001

totient = lcm(p*(p-1), q*(q-1))
assert gcd(e, totient) == 1
d = inverse(e, totient)
m = int2base(pow(c,d,n), 0x16)[1:] # remove preceding zero
print m.decode('hex')
```

### Flag
hacktoday{Welc0m3_to_RSA}

### Note
> Cari faktor bisa pake tools YAFU