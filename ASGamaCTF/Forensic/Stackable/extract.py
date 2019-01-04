data = open("soal3.png","rb").read()[0x1f1:]


gambar1 = open("gambar1","wb")
gambar2 = open("gambar2","wb")

data1=""
data2=""

for i,j in zip(data[::2],data[1::2]):
    data1+=i
    data2+=j

# kalo pake yang bawah hasilnya gakebaca
"""
for i in range(0,len(data)/2,2):
    data1+=data[i]
    data2+=data[i+1]

"""

gambar1.write(data1)
gambar2.write(data2)

gambar1.close()
gambar2.close()