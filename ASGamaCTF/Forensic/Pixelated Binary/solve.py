from PIL import Image

im = Image.open("soal5.png")
w,h = im.size

data = ""

# read left-rigth top-bottom
# pixel 0 -> black -> 1 in binary

for i in range(h):
    for j in range(w):
        px = im.getpixel((j,i))
        if px == 0:
            data+='1'
        else: 
            data+='0'

data2=""
for i in range(len(data)/8):
    data2+=chr(int(data[i*8:i*8+8],2))

print data2.decode('base64')
