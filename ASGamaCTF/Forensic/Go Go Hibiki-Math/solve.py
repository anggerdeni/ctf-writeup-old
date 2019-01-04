from pwn import *
from qrtools import QR
from PIL import Image
from sys import stdout

target = "asgama.web.id"
port = 40400
h_qr = 21
w_qr = 44

# receive connection r and list of row qr
def answer(qr):
    if len(qr)>30 :
        tmp = xor(qr)
    else:
        tmp=[]
        for i in qr:
            tmp+=map(lambda x: convert(x),i)
        to_be_arr = decode(tmp)

        # invert
        if to_be_arr == 'NULL':
            tmp=[]
            for i in qr:
                tmp+=map(lambda x: convert(x,"invert"),i)
    result = decode(tmp)
    return result

def xor(qr):
    qr1 = qr[:21]
    qr2 = qr[22:]

    tmp1 = []
    tmp2 = []
    tmp = []
    for i in range(len(qr1)):
        tmp1+=map(lambda x: convert(x),qr1[i])
        tmp2+=map(lambda x: convert(x),qr2[i])

    tmp = map(lambda x,y: x^y,tmp1,tmp2)
    
    return tmp

def qrdecode():
    myQR = QR(filename='tmp.png')
    myQR.decode()
    return myQR.data

def decode(data):
    # gambar QR
    im = Image.new('L',(w_qr,h_qr),color=255)
    im.putdata(data)

    # margin
    im2 = Image.new('L',(w_qr+20,h_qr+20),color=255)
    im2.paste(im,(10,10))
    im2.save('tmp.png','png')
    return qrdecode()

def convert(char,mode="normal"):
    if mode=="normal":
        if char==' ':
            return 255
        else:
            return 0
    else:
        if char==' ':
            return 0
        else:
            return 255

def main():
    r = remote(target,port)
    index = 1

    while True:
        a = r.recvline_contains(["Given an operation below : ","}"])
        if "Gama" in a:
            print 
            print "Found Flag : {}".format(a)
            break

        text = r.recvuntil("  Your answer :")
        qr = text[:-17].split('\n')
        jawab = answer(qr)
        stdout.flush()
        stdout.write("\n {} . {} {}".format(index,jawab,eval(jawab[:-2])))
        jawab = str(eval(jawab[:-2]))
        r.sendline(jawab)
        r.recvuntil('\n')
        index += 1
    



if __name__ == "__main__":
    main()