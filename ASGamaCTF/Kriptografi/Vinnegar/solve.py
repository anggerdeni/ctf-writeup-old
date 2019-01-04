from string import uppercase, lowercase
cipher = "Qa_vsbiw_autz_kwev"
key = "milo"

def decrypt(c,key):
 rotation = lowercase.find(key)
 
 if c in uppercase:
  index = uppercase.find(c)
  index -= rotation
  return uppercase[index % 26]

 elif c in lowercase:
  index = lowercase.find(c)
  index -= rotation
  return lowercase[index % 26]

 else :
  return c


flag = ""
j = 0
for i in range(len(cipher)):
 if(cipher[i]=='_'):
     flag+=cipher[i]
     continue
 flag += decrypt(cipher[i],key[j % len(key)])
 j+=1;

print flag