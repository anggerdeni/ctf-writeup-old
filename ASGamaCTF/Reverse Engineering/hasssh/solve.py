from pwn import *

# p = process('./hasssh') # local
# p.recvuntil('!\n')

r = remote('asgama.web.id',40500)
r.recvuntil('!\n')
i = 0
oldstring = ""
while True:
    # receive = p.recvline()[:-1]
    # if "FLAG" not in receive
    receive = r.recvline()[:-1]
    if "CTF" not in receive:
        soal = int(receive)
        jawab = '\x01'
        while soal > 0:
            if soal > 127: # lebih dari 127 diinterpretasi negatif oleh program
                jawab = chr(127)+jawab
                soal -= 127
            else :
                jawab = chr(soal)+jawab
                soal = 0
        #p.sendline(jawab)
        r.sendline(jawab)

    else:
        print receive
        break
    print "loop: {}\tsoal: {}\tjawab: {}".format(hex(i),receive,jawab.encode('hex'))
    i+=1