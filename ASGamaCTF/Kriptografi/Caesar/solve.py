from string import uppercase, lowercase
cipher = "BvhvXOA{xvzzn5vm_nj_zut}"

def decrypt(c,rotation):
 ret = ""
 for i in c:
  if i in uppercase:
   index = uppercase.find(i)
   index += rotation
   ret += uppercase[index % 26]
  elif i in lowercase:
   index = lowercase.find(i)
   index += rotation
   ret += lowercase[index % 26]
  else :
   ret +=i

 return ret

for i in range(1,14):
 print i,decrypt(cipher,i)
