# __ASGama CTF__ 
## _Behind The Scene_

## Information
**Category:** | **Points:** | **Writeup Author**
--- | --- | ---
Forensics | 60 | l0l

**Description:** 

> format flag CTF{}
>
> [BehindTheScene](./soal4.jpg)

### Behind The Scene  
Coba buka dengan exiftool :  
```
ExifTool Version Number         : 10.80
File Name                       : soal4.jpg
Directory                       : .
File Size                       : 2.5 MB
File Modification Date/Time     : 2018:12:30 06:35:51+07:00
File Access Date/Time           : 2018:12:30 06:35:56+07:00
File Inode Change Date/Time     : 2018:12:30 06:35:51+07:00
File Permissions                : rw-rw-r--
File Type                       : JPEG
File Type Extension             : jpg
MIME Type                       : image/jpeg
JFIF Version                    : 1.01
Resolution Unit                 : inches
X Resolution                    : 72
Y Resolution                    : 72
Profile CMM Type                : Linotronic
Profile Version                 : 2.1.0
Profile Class                   : Display Device Profile
Color Space Data                : RGB
Profile Connection Space        : XYZ
Profile Date Time               : 1998:02:09 06:49:00
Profile File Signature          : acsp
Primary Platform                : Microsoft Corporation
CMM Flags                       : Not Embedded, Independent
Device Manufacturer             : Hewlett-Packard
Device Model                    : sRGB
Device Attributes               : Reflective, Glossy, Positive, Color
Rendering Intent                : Perceptual
Connection Space Illuminant     : 0.9642 1 0.82491
Profile Creator                 : Hewlett-Packard
Profile ID                      : 0
Profile Copyright               : Copyright (c) 1998 Hewlett-Packard Company
Profile Description             : sRGB IEC61966-2.1
Media White Point               : 0.95045 1 1.08905
Media Black Point               : 0 0 0
Red Matrix Column               : 0.43607 0.22249 0.01392
Green Matrix Column             : 0.38515 0.71687 0.09708
Blue Matrix Column              : 0.14307 0.06061 0.7141
Device Mfg Desc                 : IEC http://www.iec.ch
Device Model Desc               : IEC 61966-2.1 Default RGB colour space - sRGB
Viewing Cond Desc               : Reference Viewing Condition in IEC61966-2.1
Viewing Cond Illuminant         : 19.6445 20.3718 16.8089
Viewing Cond Surround           : 3.92889 4.07439 3.36179
Viewing Cond Illuminant Type    : D50
Luminance                       : 76.03647 80 87.12462
Measurement Observer            : CIE 1931
Measurement Backing             : 0 0 0
Measurement Geometry            : Unknown
Measurement Flare               : 0.999%
Measurement Illuminant          : D65
Technology                      : Cathode Ray Tube Display
Red Tone Reproduction Curve     : (Binary data 2060 bytes, use -b option to extract)
Green Tone Reproduction Curve   : (Binary data 2060 bytes, use -b option to extract)
Blue Tone Reproduction Curve    : (Binary data 2060 bytes, use -b option to extract)
Image Width                     : 4896
Image Height                    : 3264
Encoding Process                : Baseline DCT, Huffman coding
Bits Per Sample                 : 8
Color Components                : 3
Y Cb Cr Sub Sampling            : YCbCr4:2:0 (2 2)
Image Size                      : 4896x3264
Megapixels                      : 16.0
```

Perhatikan bagian ini :  
```
Red Tone Reproduction Curve     : (Binary data 2060 bytes, use -b option to extract)
Green Tone Reproduction Curve   : (Binary data 2060 bytes, use -b option to extract)
Blue Tone Reproduction Curve    : (Binary data 2060 bytes, use -b option to extract)
```

Dari sini kita tahu ada file lain dalam file ini. Jadi kita extract dengan foremost, hasilnya ada banyak file png berisi qr code. Tapi tidak ada satupun yang bisa didecode.

Setelah dicek kembali ternyata warnanya tertukar antara hitam dengan putih, maka kita harus invert dulu baru didecode.

### Payload
```py
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
```

### Result
```
$ python solve.py
CTF{scr1pt1ng__1s_just_t0_4we5om3}
```

### Flag
CTF{scr1pt1ng__1s_just_t0_4we5om3}