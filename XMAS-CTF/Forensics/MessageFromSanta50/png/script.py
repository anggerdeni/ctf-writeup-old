from PIL import Image
data ="""File Name                       : 00000080.png
Image Offset                    : 1640, 1093 (pixels)
File Name                       : 00000092.png
Image Offset                    : 273, 1093 (pixels)
File Name                       : 00000100.png
Image Offset                    : 820, 820 (pixels)
File Name                       : 00000168.png
Image Offset                    : 547, 273 (pixels)
File Name                       : 00000260.png
Image Offset                    : 1093, 0 (pixels)
File Name                       : 00000272.png
Image Offset                    : 547, 0 (pixels)
File Name                       : 00000324.png
Image Offset                    : 1366, 820 (pixels)
File Name                       : 00000408.png
Image Offset                    : 0, 547 (pixels)
File Name                       : 00000620.png
Image Offset                    : 0, 1093 (pixels)
File Name                       : 00000640.png
Image Offset                    : 1093, 547 (pixels)
File Name                       : 00000784.png
File Name                       : 00000856.png
Image Offset                    : 0, 273 (pixels)
File Name                       : 00000960.png
Image Offset                    : 547, 820 (pixels)
File Name                       : 00001052.png
Image Offset                    : 1366, 273 (pixels)
File Name                       : 00001196.png
Image Offset                    : 1640, 547 (pixels)
File Name                       : 00001400.png
Image Offset                    : 1093, 820 (pixels)
File Name                       : 00001500.png
Image Offset                    : 0, 820 (pixels)
File Name                       : 00001652.png
Image Offset                    : 1366, 0 (pixels)
File Name                       : 00001664.png
Image Offset                    : 273, 0 (pixels)
File Name                       : 00001748.png
Image Offset                    : 273, 273 (pixels)
File Name                       : 00001840.png
Image Offset                    : 1093, 273 (pixels)
File Name                       : 00001976.png
Image Offset                    : 1640, 0 (pixels)
File Name                       : 00002028.png
Image Offset                    : 273, 547 (pixels)
File Name                       : 00002188.png
Image Offset                    : 820, 547 (pixels)
File Name                       : 00002308.png
Image Offset                    : 820, 0 (pixels)
File Name                       : 00002312.png
Image Offset                    : 820, 273 (pixels)
File Name                       : 00002380.png
Image Offset                    : 1366, 547 (pixels)
File Name                       : 00002560.png
Image Offset                    : 547, 547 (pixels)
File Name                       : 00002672.png
Image Offset                    : 820, 1093 (pixels)
File Name                       : 00002680.png
Image Offset                    : 1640, 820 (pixels)
File Name                       : 00002868.png
Image Offset                    : 273, 820 (pixels)
File Name                       : 00003028.png
Image Offset                    : 1640, 273 (pixels)
File Name                       : 00003152.png
Image Offset                    : 547, 1093 (pixels)
File Name                       : 00003160.png
Image Offset                    : 1093, 1093 (pixels)
File Name                       : 00003168.png
Image Offset                    : 1366, 1093 (pixels)
""".split('\n')[:-1]

name = []
offset = []


for i in range(0,len(data)/2,2):
  print data[i]
  print data[i+1]
  name.append(data[i].split(': ')[1])
  awal = data[i+1].find(': ')
  akhir = data[i+1].find(' (')
  tmp = data[i+1][awal+2:akhir].split(',')
  offset.append((int(tmp[0]),int(tmp[1])))
