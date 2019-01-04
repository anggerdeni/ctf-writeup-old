from string import printable
f = open('soal','r').read()[:-1].decode('hex')

strings = []
for i in range(256):
 tmp = ''
 flag = True
 for j in f:
  tmp_chr = chr(ord(j)^i)
  if tmp_chr not in printable:
   flag = False
   break
  tmp+=tmp_chr
 if flag:
  strings.append(tmp)

for i in strings:
 print i
