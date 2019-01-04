from os import system
from qrtools import QR 
from PIL import Image,ImageOps

dir = "/home/l0l/CTF/Soal/Writeup/ctf-writeup/ASGamaCTF/Forensics/Behind The Scene"

system("echo $(ls qr) > names")

names = open("names","r").read()[:-1].split(' ')
names.sort()

chars = []

# invert color
for i in names:
    im = Image.open("qr/{}".format(i))
    im = ImageOps.invert(im)
    im.save("qr-inv/{}".format(i),"png")

for i in names:
    myQR = QR(filename="qr-inv/{}".format(i))
    myQR.decode()
    chars.append(myQR.data)

print ''.join(chars)