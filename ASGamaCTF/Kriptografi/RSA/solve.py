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