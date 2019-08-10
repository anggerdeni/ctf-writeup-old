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