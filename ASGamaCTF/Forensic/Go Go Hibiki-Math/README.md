# __ASGama CTF__ 
## _Go! Go! Hibiki-Math_

## Information
**Category:** | **Points:** | **Writeup Author**
--- | --- | ---
Forensics | 250 | l0l

**Description:** 

> [Misc]
>
> Math was originally fun & it was Hibiki's favorite stuff. But, everything changed when Calculus invaded. Only the ones who hold the solid feels and determination could stop the darkness within Hibiki's inner heart.
>
> The Hibiki's fate is on your hands. Could you save her?
>
> nc asgama.web.id 40400


### Go! Go! Hibiki-Math  
Tampilan service : 
```
****************************************************************************************************


                             %@/    %@.  @&  &@       #@#  @&      .@%                             
                             %@/    %@.      &@            @&                                      
                             %@/    %@.  @&  &@%@@@#  #@#  @&  #@/ .@%                             
                             %@@@@@@@@.  @&  &@.  &@  #@#  @&.@&   .@%                             
                             %@/    %@.  @&  &@   &@  %@#  @@@%@*  .@%                             
                             %@/    %@.  @&  &@@#&@@  #@#  @&  /@% .@%                             
                                                                                                   
                                **      ,,.                 *,                                     
                                @@@    #@@*           /@&   @@                                     
                                @@@%   @@@*   *&@&*   &@@#  @@,&@#                                 
                                @@/@( &%*@*   .  .@@  /@&   @@. ,@@                                
                                @@ (@&@ ,@*  (@@@@@@  /@&   @@   @@                                
                                @@  %@, *@* .@@   @@  /@&   @@   @@                                
                                %%      ,%,   (&%,#%   *%#  %%   #%                                

		  

 Welcome to Hibiki Math Challenge
 In this game, you'll be presented with several questions, represented in a Math operation
 The rule's simple. Just submit the correct answer for each given question
 Remember, you only have 1.5 s to submit your answer

****************************************************************************************************


1. Given an operation below : 
 UUUUUUUUUUUUUU    UUUUUUUU  UUUUUUUUUUUUUU 
 UU          UU    UU        UU          UU 
 UU  UUUUUU  UU  UU  UU      UU  UUUUUU  UU 
 UU  UUUUUU  UU  UUUUUU      UU  UUUUUU  UU 
 UU  UUUUUU  UU    UU  UU    UU  UUUUUU  UU 
 UU          UU    UUUU      UU          UU 
 UUUUUUUUUUUUUU  UU  UU  UU  UUUUUUUUUUUUUU 
                       UUUU                 
       UUUU  UUUU  UUUU            UUUU     
 UU    UUUU    UU  UUUUUU  UU    UU    UU   
       UUUU  UUUUUUUUUU    UUUUUU    UU  UU 
 UU  UUUUUU          UU  UU    UUUUUUUU  UU 
 UU  UU    UUUUUU  UU    UU  UU    UU    UU 
                 UU    UUUU    UUUU         
 UUUUUUUUUUUUUU  UUUU    UUUUUUUUUU    UU   
 UU          UU      UUUU        UU  UUUU   
 UU  UUUUUU  UU  UU  UU  UU  UUUU      UUUU 
 UU  UUUUUU  UU  UUUU  UUUU        UU       
 UU  UUUUUU  UU      UU    UU  UUUU  UUUUUU 
 UU          UU    UUUUUU      UU    UUUUUU 
 UUUUUUUUUUUUUU      UU  UUUU  UU  UU       

  Your answer : 
```


Secara singkat service hanya memberi `qrcode` namun dalam bentuk text. Tugas kita adalah untuk mendecode QRcode tersebut lalu submit hasilnya dalam waktu 1.5 detik.  

Di service ini ada 3 macam QRCode:  
1. Normal QRCode
```
 UUUUUUUUUUUUUU    UUUUUUUU  UUUUUUUUUUUUUU 
 UU          UU    UU        UU          UU 
 UU  UUUUUU  UU  UU  UU      UU  UUUUUU  UU 
 UU  UUUUUU  UU  UUUUUU      UU  UUUUUU  UU 
 UU  UUUUUU  UU    UU  UU    UU  UUUUUU  UU 
 UU          UU    UUUU      UU          UU 
 UUUUUUUUUUUUUU  UU  UU  UU  UUUUUUUUUUUUUU 
                       UUUU                 
       UUUU  UUUU  UUUU            UUUU     
 UU    UUUU    UU  UUUUUU  UU    UU    UU   
       UUUU  UUUUUUUUUU    UUUUUU    UU  UU 
 UU  UUUUUU          UU  UU    UUUUUUUU  UU 
 UU  UU    UUUUUU  UU    UU  UU    UU    UU 
                 UU    UUUU    UUUU         
 UUUUUUUUUUUUUU  UUUU    UUUUUUUUUU    UU   
 UU          UU      UUUU        UU  UUUU   
 UU  UUUUUU  UU  UU  UU  UU  UUUU      UUUU 
 UU  UUUUUU  UU  UUUU  UUUU        UU       
 UU  UUUUUU  UU      UU    UU  UUUU  UUUUUU 
 UU          UU    UUUUUU      UU    UUUUUU 
 UUUUUUUUUUUUUU      UU  UUUU  UU  UU       
```

2. Inverted QRCode
```
               UU  UU    UUUU               
   UUUUUUUUUU  UUUUUUUUUU  UU  UUUUUUUUUU   
   UU      UU  UUUU  UU  UUUU  UU      UU   
   UU      UU  UU  UUUUUU  UU  UU      UU   
   UU      UU  UUUUUU  UUUUUU  UU      UU   
   UUUUUUUUUU  UUUUUU  UUUUUU  UUUUUUUUUU   
               UU  UU  UU  UU               
 UUUUUUUUUUUUUUUUUU  UUUU  UUUUUUUUUUUUUUUU 
 UUUU  UU      UU      UU    UUUUUU  UUUU   
 UUUU  UUUU  UU    UU  UU    UU  UUUUUUUU   
     UUUU        UU  UUUUUU    UU  UU  UU   
     UU      UU      UU        UUUU  UU     
   UUUU    UU  UU  UU    UUUUUU  UUUUUUUU   
 UUUUUUUUUUUUUUUU    UU      UUUU      UU   
               UUUU  UUUUUU  UUUU    UUUU   
   UUUUUUUUUU  UU    UUUU        UU  UUUU   
   UU      UU  UU  UU  UU  UUUUUU    UU     
   UU      UU  UUUU  UU            UUUU  UU 
   UU      UU  UU  UUUUUU  UU  UU  UU  UU   
   UUUUUUUUUU  UUUU      UUUUUU      UU  UU 
               UUUUUUUU    UUUUUU    UU     
```

3. XOR QRCode
```
 UUUUUUUUUUUUUU      UUUU    UUUUUUUUUUUUUU 
 UU          UU  UU      UU  UU          UU 
 UU  UUUUUU  UU      UUUUUU  UU  UUUUUU  UU 
 UU  UUUUUU  UU      UUUU    UU  UUUUUU  UU 
 UU  UUUUUU  UU    UU    UU  UU  UUUUUU  UU 
 UU          UU  UU      UU  UU          UU 
 UUUUUUUUUUUUUU  UU  UU  UU  UUUUUUUUUUUUUU 
                 UUUUUUUU                   
         UUUUUUUU            UUUU      UU   
   UUUUUU      UUUU      UU    UU  UU  UUUU 
     UU    UUUU    UU  UUUU  UUUUUUUUUU     
 UU    UUUUUU  UU  UUUU    UU    UU  UU     
   UU  UU    UUUU  UUUU  UU          UU  UU 
                 UU    UUUU          UU  UU 
 UUUUUUUUUUUUUU  UUUU    UU  UU          UU 
 UU          UU  UU    UU    UUUU  UU       
 UU  UUUUUU  UU  UUUU          UUUUUUUUUUUU 
 UU  UUUUUU  UU      UUUUUU    UU  UU  UUUU 
 UU  UUUUUU  UU    UUUU        UUUUUUUU     
 UU          UU    UU  UUUU      UU  UU  UU 
 UUUUUUUUUUUUUU    UUUU  UUUUUU      UUUUUU 

 UUUUUUUUUUUUUUUU    UUUU  UUUUUUUUUUUUUUUU 
 UUUUUUUUUUUUUUUU    UU    UUUUUUUUUUUUUUUU 
 UUUUUUUUUUUUUUUUUUUU      UUUUUUUUUUUUUUUU 
 UUUUUUUUUUUUUUUU  UU      UUUUUUUUUUUUUUUU 
 UUUUUUUUUUUUUUUUUUUU  UU  UUUUUUUUUUUUUUUU 
 UUUUUUUUUUUUUUUU    UUUUUUUUUUUUUUUUUUUUUU 
 UUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUU 
 UUUUUUUUUUUUUUUU  UUUUUU  UUUUUUUUUUUUUUUU 
 UUUU  UUUUUUUU        UUUU      UU  UU     
         UUUUUUUU  UU  UU  UUUUUUUUUU    UU 
 UU  UU      UU      UUUUUUUUUU  UU  UUUU   
     UU      UU  UUUU      UU  UU           
         UU  UUUUUUUUUUUUUUUUUU  UUUU  UUUU 
 UUUUUUUUUUUUUUUUUUUU        UUUU  UUUUUUUU 
 UUUUUUUUUUUUUUUU  UUUUUUUU  UUUU      UUUU 
 UUUUUUUUUUUUUUUUUUUUUUUU  UU  UUUUUUUUUU   
 UUUUUUUUUUUUUUUUUUUUUUUUUUUU    UUUU  UUUU 
 UUUUUUUUUUUUUUUUUU    UU  UUUUUU  UUUUUU   
 UUUUUUUUUUUUUUUU    UUUU  UU    UUUUUUUU   
 UUUUUUUUUUUUUUUUUUUUUU  UUUUUUUUUU         
 UUUUUUUUUUUUUUUUUUUUUUUU    UU        UUUU
```


Pada Normal QRCode, yang perlu kita lakukan hanyalah melakukan decoding, hasilnya berupa operasi aritmatika yang dapat diselesaikan dengan mudah dengan program.

Selanjutnya Inverted QRCode, mirip seperti normal QRCode, hanya saja pewarnaannya dibalik (hitam jadi putih dan sebaliknya). Yang perlu kita lakukan adalah menginverse terlebih dahulu, baru didecode dan evaluasi operasi aritmatikanya.

Jenis yang ketiga yaitu XOR QRCode. Disini kita diberi dua buah "gambar" / "QRCode" yang terlebih dahulu harus kita xor antar baris yang bersesuaian agar mendapatkan QRCode yang asli.


### Payload
```py
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
```

### Result
```
python solve.py
[+] Opening connection to asgama.web.id on port 40400: Done

 1 . 81*71 = 5751
 2 . 47-82 = -35
 3 . 55-75 = -20
 4 . 88*99 = 8712
 5 . 30+25 = 55
 6 . 49+88 = 137
 7 . 41+78 = 119
 8 . 82*98 = 8036
 9 . 34-53 = -19
 10 . 80*32 = 2560
 11 . 27+15 = 42
 12 . 89-98 = -9
 13 . 13*58 = 754
 14 . 39-38 = 1
 15 . 79*78 = 6162
 16 . 21*58 = 1218
 17 . 83+26 = 109
 18 . 45+19 = 64
 19 . 12*51 = 612
 20 . 71+65 = 136
Found Flag :  GamaCTF{m4th_1s_fr3ak_h1b1k1_1s_luv}
[*] Closed connection to asgama.web.id port 40400
```

### Flag
GamaCTF{m4th_1s_fr3ak_h1b1k1_1s_luv}